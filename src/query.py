"""Phase 2: the model never sees the rows. It gets a schema, writes queries, and answers from their results.

    python src/query.py                                # credit, Sonnet, all query conditions, 5 repeats
    python src/query.py --only sql sparql --runs 1     # a quick check

Conditions:
  sql              DuckDB tables, one per CSV file: the schema only
  sql+markdown     the same, plus the ontology's definitions as Markdown
  sparql           the RDF in rdflib: the classes and properties used, no definitions
  sparql+ontology  the RDF with the ontology loaded beside it, plus the same Markdown definitions
  sql+executed     the rules run in the store: DuckDB holds the executed tables (run.py's executed condition)
  sparql+axioms    the rules run in the store: the RDF after axioms.ttl's SHACL rules, with what they derived

The runner owns the loop, so any provider can play: each reply may hold several ```sql or
```sparql blocks, which are run and their results sent back, for up to eight rounds. A reply
with a ```json block and no queries is the final answer, graded as in run.py. Each run writes
results/<domain>/<timestamp>-<model>-query/ with a transcript per condition and repeat.

The SPARQL conditions run on rdflib by default. With --store graphdb they run on a local GraphDB
(GRAPHDB_URL, default http://localhost:7200), in a repository of their own with no inference, loaded
with exactly the triples rdflib would hold, so only the engine changes. Such a run's folder ends -query-graphdb.
"""
import argparse
import csv
import importlib
import json
import re
import signal
import sys
import urllib.error
import urllib.parse
import urllib.request
import os
from datetime import datetime
from pathlib import Path

import duckdb
from rdflib import BNode, Graph, URIRef

import grade
import providers
import report
from run import INSTRUCTIONS, KINDS, commit, split_answers

ROOT = Path(__file__).resolve().parent.parent  # the repo: domains/ and results/
CONDITIONS = ["sql", "sql+markdown", "sparql", "sparql+ontology", "sql+executed", "sparql+axioms"]
ROUNDS = 8
MAX_ROWS = 60
TIMEOUT = 60  # seconds per query: a query that runs longer is reported to the model as failed
STORE = "rdflib"  # or "graphdb", from --store
GRAPHDB = os.environ.get("GRAPHDB_URL", "http://localhost:7200")
GRAPHDB_REPO = "semantics-ladder"
GRAPHDB_CONFIG = """@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix rep: <http://www.openrdf.org/config/repository#>.
@prefix sr: <http://www.openrdf.org/config/repository/sail#>.
@prefix sail: <http://www.openrdf.org/config/sail#>.
@prefix graphdb: <http://www.ontotext.com/config/graphdb#>.
[] a rep:Repository ; rep:repositoryID "%s" ; rdfs:label "semantics-ladder query runs (cleared each session)" ;
   rep:repositoryImpl [ rep:repositoryType "graphdb:SailRepository" ;
     sr:sailImpl [ sail:sailType "graphdb:Sail" ; graphdb:ruleset "empty" ; graphdb:disable-sameAs "true" ] ] .
""" % GRAPHDB_REPO

PROTOCOL = """You can't see the data, but you can query it. {how}

To run queries, reply with one or more fenced blocks (```{lang}), and nothing else is needed:
each is run and its results sent back to you. You have up to {rounds} rounds of queries.
When you have what you need, reply with the final answers and no queries."""

HOW = {
    "sql": "It is in DuckDB, in the tables below. Write DuckDB SQL.",
    "sparql": "It is in an RDF store, described below. Write SPARQL 1.1 SELECT or ASK queries.",
}


class SQLStore:
    lang = "sql"

    def __init__(self, domain, executed=False):
        self.db = duckdb.connect()
        folder, files = (domain.DATA / "executed", domain.EXECUTED_TABLES) if executed else (domain.DATA, domain.CSV_FILES)
        for name in files:
            table = name.removesuffix(".csv")
            self.db.execute(f"CREATE TABLE {table} AS SELECT * FROM read_csv('{folder / name}', all_varchar=true)")
        self.db.execute("SET enable_external_access = false")  # no reading files from here on
        self.tables = [n.removesuffix(".csv") for n in files]

    def schema(self):
        out = []
        for t in self.tables:
            cols = self.db.execute(f"DESCRIBE {t}").fetchall()
            n = self.db.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
            out.append(f"- `{t}` ({n} rows): " + ", ".join(c[0] for c in cols))
        return "All columns are text (VARCHAR); dates are ISO strings.\n\n" + "\n".join(out)

    def run(self, q):
        cur = self.db.execute(q)
        cols = [d[0] for d in cur.description]
        return cols, cur.fetchall()


class SPARQLStore:
    lang = "sparql"

    def __init__(self, domain, extra=""):
        if extra == "axioms":  # the facts with what the rules derived; the schema lists the derived terms too
            self.g = inferred(domain)
            terms = set(Graph().parse(domain.ONTOLOGY).subjects()) | set(Graph().parse(domain.HERE / "axioms.ttl").subjects())
            self.facts = Graph()
            self.facts.bind("lad", "https://example.org/ladder/")
            for s, p, o in self.g:
                if s not in terms and not isinstance(s, BNode):
                    self.facts.add((s, p, o))
            return
        self.g = Graph().parse(domain.DATA / "facts.ttl")
        if extra == "ontology":
            self.g.parse(domain.ONTOLOGY)
        self.facts = Graph().parse(domain.DATA / "facts.ttl")

    def schema(self):
        rows = self.facts.query("""SELECT ?class ?p (COUNT(DISTINCT ?s) AS ?n) WHERE { ?s a ?class ; ?p ?o }
                                   GROUP BY ?class ?p ORDER BY ?class ?p""")
        by_class = {}
        for c, p, n in rows:
            by_class.setdefault(self.facts.qname(c), []).append(self.facts.qname(p))
        prefixes = "\n".join(f"PREFIX {k}: <{v}>" for k, v in self.facts.namespaces()
                             if k in ("lad", "res", "rdfs", "xsd", "skos", "rdf"))
        lines = [f"- `{c}`: " + ", ".join(f"`{p}`" for p in ps) for c, ps in by_class.items()]
        return f"Prefixes:\n```\n{prefixes}\n```\n\nClasses and the properties their resources use:\n\n" + "\n".join(lines)

    def run(self, q):
        if re.search(r"\b(SERVICE|LOAD|INSERT|DELETE|CLEAR|DROP)\b", q, re.I):
            raise ValueError("only SELECT and ASK queries over the store are allowed")
        res = self.g.query(q)
        if res.type == "ASK":
            return ["ask"], [(res.askAnswer,)]
        return [str(v) for v in res.vars], [tuple(self.short(x) for x in row) for row in res]

    def short(self, x):
        if x is None:
            return None
        try:
            return self.g.qname(x) if hasattr(x, "n3") and x.__class__.__name__ == "URIRef" else str(x)
        except Exception:
            return str(x)


class GraphDBStore(SPARQLStore):
    """The same triples as SPARQLStore, loaded into a local GraphDB with no inference, and queried there."""

    def __init__(self, domain, extra=""):
        super().__init__(domain, extra)
        graphdb_repo()
        url = f"{GRAPHDB}/repositories/{GRAPHDB_REPO}/statements"
        http(url, method="DELETE")
        http(url, data=self.g.serialize(format="nt").encode(), headers={"Content-Type": "application/n-triples"})

    def run(self, q):
        if re.search(r"\b(SERVICE|LOAD|INSERT|DELETE|CLEAR|DROP)\b", q, re.I):
            raise ValueError("only SELECT and ASK queries over the store are allowed")
        body = urllib.parse.urlencode({"query": q, "timeout": TIMEOUT}).encode()
        try:
            res = json.loads(http(f"{GRAPHDB}/repositories/{GRAPHDB_REPO}", data=body, headers={
                "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/sparql-results+json"}))
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace").strip()
            if "timeout" in msg.lower() or "timed out" in msg.lower():
                raise TimeoutError(f"stopped after {TIMEOUT} seconds")
            raise ValueError(msg.splitlines()[0] if msg else str(e))
        if "boolean" in res:
            return ["ask"], [(res["boolean"],)]
        cols = res["head"]["vars"]
        cell = lambda b: None if b is None else self.short(URIRef(b["value"])) if b["type"] == "uri" else b["value"]
        return cols, [tuple(cell(row.get(c)) for c in cols) for row in res["results"]["bindings"]]


def http(url, data=None, headers=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=TIMEOUT + 30) as r:
        return r.read().decode()


def graphdb_repo():
    """Create the runs' own repository, with no inference, unless it's there. Nothing else in GraphDB is touched."""
    try:
        http(f"{GRAPHDB}/rest/repositories/{GRAPHDB_REPO}")
        return
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    boundary = "----semanticsladder"
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"config\"; filename=\"config.ttl\"\r\n"
            f"Content-Type: text/turtle\r\n\r\n{GRAPHDB_CONFIG}\r\n--{boundary}--\r\n").encode()
    http(f"{GRAPHDB}/rest/repositories", data=body, headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})


def timed(run, q):
    """run(q), stopped after TIMEOUT seconds. rdflib can loop for hours on a bad join."""
    def stop(*_):
        raise TimeoutError(f"stopped after {TIMEOUT} seconds")
    signal.signal(signal.SIGALRM, stop)
    signal.alarm(TIMEOUT)
    try:
        return run(q)
    finally:
        signal.alarm(0)


def queries_in(reply, lang):
    """The queries in a reply: fenced blocks, or the tool-call markup models sometimes write instead."""
    found = re.findall(rf"```{lang}\s*(.*?)```", reply, re.S | re.I)
    found += re.findall(rf'<(?:invoke|parameter) name="{lang}">\s*(.*?)\s*</(?:invoke|parameter)>', reply, re.S | re.I)
    clean = [re.sub(r"</?(?:invoke|parameter)[^>]*>|```", "", q).strip() for q in found]
    return list(dict.fromkeys(q for q in clean if q))


def table(cols, rows):
    shown = rows[:MAX_ROWS]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join("" if v is None else str(v) for v in r) + " |" for r in shown]
    if len(rows) > MAX_ROWS:
        lines.append(f"({len(rows) - MAX_ROWS} more rows not shown)")
    return "\n".join(lines) if rows else "(no rows)"


def inferred(domain):
    """The facts, ontology and axioms after the SHACL rules have run, cached in data/inferred.ttl."""
    cache = domain.DATA / "inferred.ttl"
    if not cache.exists():
        from pyshacl import validate
        axioms = domain.HERE / "axioms.ttl"
        g = Graph().parse(domain.DATA / "facts.ttl").parse(domain.ONTOLOGY).parse(axioms)
        validate(g, shacl_graph=Graph().parse(axioms), advanced=True, inplace=True, allow_infos=True)
        g.serialize(cache, format="turtle")
    return Graph().parse(cache)


def store_for(domain, condition):
    if condition.startswith("sql"):
        return SQLStore(domain, executed=condition.endswith("+executed"))
    return (GraphDBStore if STORE == "graphdb" else SPARQLStore)(domain, condition.partition("+")[2])


def opening(domain, condition, store, questions):
    fields = "\n".join(f"- {q['id']}: " + ", ".join(f"{f} ({KINDS[k]})" for f, k in q["fields"].items())
                       for q in questions if "fields" in q)
    parts = ["## The data", "", PROTOCOL.format(how=HOW[store.lang], lang=store.lang, rounds=ROUNDS), "",
             store.schema()]
    extra = condition.partition("+")[2]
    if extra == "executed":
        parts += ["", domain.EXECUTED_NOTE]
    elif extra == "axioms":
        parts += ["", domain.AXIOMS_NOTE]
    elif extra:
        parts += ["", "### ontology.md (the vocabulary the data uses)", "", (domain.HERE / "ontology.md").read_text()]
    qs = "\n".join(f"{q['id']}. {q['question']}" for q in questions)
    parts += ["", "## Questions", "", INSTRUCTIONS.format(entity_hint=domain.ENTITY_HINT, fields=fields), "", qs]
    return "\n".join(parts)


def converse(domain, condition, questions, model):
    """One session: queries and results until a final answer. Returns (final text, transcript, stats)."""
    store = store_for(domain, condition)
    first = opening(domain, condition, store, questions)
    transcript = [("user", first)]
    stats = {"queries": 0, "failed": 0, "rounds": 0, "timeouts": 0}
    for rnd in range(ROUNDS + 1):
        text = "\n\n".join(f"### {who}\n\n{msg}" for who, msg in transcript) if rnd else first
        reply = providers.ask(text if rnd else first, domain.SYSTEM, model)
        transcript.append(("assistant", reply))
        blocks = queries_in(reply, store.lang)
        if not blocks and "```json" not in reply and not stats.get("nudged") and rnd < ROUNDS:
            # neither queries the runner can see nor a final answer: ask once, rather than grade it as empty
            stats["nudged"] = 1
            transcript.append(("user", f"The runner found no ```{store.lang} block and no ```json block in your reply. "
                                       f"Put each query in its own ```{store.lang} fenced block, or give the final answers."))
            continue
        if not blocks:
            return reply, transcript, stats
        stats["rounds"] += 1
        results = []
        for i, q in enumerate(blocks, 1):
            stats["queries"] += 1
            try:
                results.append(f"Query {i}:\n\n" + table(*timed(store.run, q)))
            except Exception as e:
                stats["failed"] += 1
                stats["timeouts"] += isinstance(e, TimeoutError)
                results.append(f"Query {i} failed: {str(e).splitlines()[0][:300]}")
        note = ("This was the last round: give the final answers now, with no more queries."
                if rnd + 1 >= ROUNDS else "Run more queries, or give the final answers.")
        transcript.append(("user", "\n\n".join(results) + "\n\n" + note))
    return transcript[-1][1], transcript, stats


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", default="credit")
    ap.add_argument("--model", default="claude:sonnet")
    ap.add_argument("--grader", default="claude:sonnet")
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--only", nargs="+", choices=CONDITIONS)
    ap.add_argument("--resume", type=Path)
    ap.add_argument("--store", choices=["rdflib", "graphdb"], default="rdflib", help="the engine for the SPARQL conditions")
    args = ap.parse_args()
    global STORE
    STORE = args.store

    domain = importlib.import_module(f"domains.{args.domain}.domain")
    questions = json.loads(domain.QUESTIONS.read_text())
    conditions = args.only or CONDITIONS
    canon = domain.canonical()
    out = args.resume or ROOT / "results" / args.domain / f"{datetime.now():%Y-%m-%d-%H%M}-{providers.split(args.model)[1]}-query{'-graphdb' if STORE == 'graphdb' else ''}"
    out.mkdir(parents=True, exist_ok=True)
    if not (out / "questions.json").exists():  # the questions as asked, keys included, kept with the run
        (out / "questions.json").write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n")
    if not (out / "meta.json").exists():
        (out / "meta.json").write_text(json.dumps({
            "domain": args.domain, "model": args.model, "grader": args.grader, "runs": args.runs, "mode": "query",
            "conditions": conditions, "started": f"{datetime.now():%Y-%m-%d %H:%M}", "rounds": ROUNDS,
            "questions": len(questions), "commit": commit(), "store": STORE}, indent=2) + "\n")

    def ask_grader(text, system):
        return providers.ask(text, system, args.grader)

    grades, stats = {c: [] for c in conditions}, {c: [] for c in conditions}
    for c in conditions:
        for r in range(args.runs):
            f, t = out / f"answers-{c}-run{r + 1}.md", out / f"transcript-{c}-run{r + 1}.json"
            if not f.exists():
                print(f"querying: {c}, run {r + 1} ...", flush=True)
                final, transcript, s = converse(domain, c, questions, args.model)
                t.write_text(json.dumps({"stats": s, "turns": transcript}, indent=1))
                f.write_text(final)
            stats[c].append(json.loads(t.read_text())["stats"])
            text = f.read_text()
            print(f"grading: {c}, run {r + 1} ...", flush=True)
            grades[c].append(grade.grade(questions, split_answers(text, questions), grade.structured(text), canon, ask_grader))
            (out / "grades.json").write_text(json.dumps({k: v for k, v in grades.items() if v}, indent=2) + "\n")
            (out / "stats.json").write_text(json.dumps({k: v for k, v in stats.items() if v}, indent=2) + "\n")
    report.write(out, questions)
    print(f"report: {out / 'report.md'}")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    main()
