"""Run axioms.ttl's SHACL rules over the data and check what they derive against build_questions.py's rules.

    python domains/research/check_axioms.py domains/research
    python domains/research/check_axioms.py domains/research_850

The keys are computed by build_questions.py, so the rules must derive the same research works,
people, credited institutions, hierarchy and citations, or the sparql+axioms condition would be
answering from a different reading of the data.
"""
import os
import sys
import time
from pathlib import Path

from pyshacl import validate
from rdflib import Graph

folder = Path(sys.argv[1])
os.environ["RESEARCH_FOLDER"] = str(folder)
sys.path.insert(0, str(Path(__file__).parent))
import build_questions as b  # noqa: E402  reads RESEARCH_FOLDER

start = time.time()
data = Graph().parse(folder / "data/facts.ttl").parse(folder / "ontology/ontology.ttl").parse(folder / "ontology/axioms.ttl")
shapes = Graph().parse(folder / "ontology/axioms.ttl")
conforms, _, text = validate(data, shacl_graph=shapes, advanced=True, inplace=True, allow_infos=True)
print(f"rules run in {time.time() - start:.0f}s; conforms: {conforms}")
if not conforms:
    print(text[:1500])

PREFIX = "PREFIX res: <https://example.org/research/> "
local = lambda x: str(x).rsplit("/", 1)[-1]
q = lambda s: [tuple(local(v) for v in row) for row in data.query(PREFIX + s)]
failures = 0


def check(what, derived, expected):
    global failures
    ok = derived == expected
    failures += not ok
    print(f"{'ok  ' if ok else 'FAIL'} {what}")
    if not ok:
        print("     only derived:", sorted(derived - expected)[:10], "| only expected:", sorted(expected - derived)[:10])


check("research works", {w for (w,) in q("SELECT ?w { ?w a res:ResearchWork }")}, set(b.RESEARCH))
check("counts as", set(q("SELECT ?w ?v { ?w res:countsAs ?v }")), {(w, b.identity(w)) for w in b.WORKS})
check("people on each work", set(q("SELECT ?w ?a { ?w res:hasPerson ?a }")),
      {(w, b.record_of(p)) for w in {b.identity(x) for x in b.WORKS} for p in b.people(w)})
works = {b.identity(w) for w in b.WORKS}
check("credited institutions", {x for x in q("SELECT ?w ?i { ?w res:creditedInstitution ?i }") if x[0] in works},
      {(w, i) for w in works for i in b.institutions_of(w)})
check("credited countries", {(w, str(c)) for w, c in q("SELECT ?w ?c { ?w res:creditedCountry ?c }") if w in works},
      {(w, c) for w in works for c in b.countries_of(w)})
check("counts towards", set(q("SELECT ?i ?up { ?i res:countsTowards ?up }")), {(i, up) for i in b.INSTS for up in b.chain(i)})
check("ultimate parents", set(q("SELECT ?i ?u { ?i res:ultimateParent ?u }")), {(i, b.ultimate_parent(i)) for i in b.INSTS})
check("citations", set(q("SELECT ?c ?w { ?c res:cites ?w }")), {(c, w) for w in works for c in b.citers(w)})
# the constraints must catch a breach: make an article a version of another work and validate again
from rdflib import Namespace  # noqa: E402
RES = Namespace("https://example.org/research/")
bad = Graph().parse(folder / "data/facts.ttl").parse(folder / "ontology/ontology.ttl").parse(folder / "ontology/axioms.ttl")
bad.add((RES.W03, RES.versionOf, RES.W01))
c2, _, t2 = validate(bad, shacl_graph=shapes, advanced=True, inplace=True, allow_infos=True)
check("an article marked as a version is caught", {c2}, {False})
print("all rules agree with the keys" if not failures else f"{failures} rule(s) disagree")
sys.exit(1 if failures else 0)
