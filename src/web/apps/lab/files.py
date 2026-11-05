"""Everything the pages show, read from the experiment's files when a page opens. Nothing is copied."""
import csv
import json
import re
from pathlib import Path

import markdown
from django.conf import settings
from django.utils.safestring import mark_safe

import report

ROOT = settings.REPO_ROOT
DOMAINS = ROOT / "domains"
RESULTS = ROOT / "results"
MARK = {"correct": "✅", "partial": "🟡", "wrong": "❌"}


# --- conditions: a short label for each, R for reading the data and D for querying a database ---

LABELS = {c: f"R{i}" for i, c in enumerate(["csv", "rdf", "csv+padding", "csv+markdown", "csv+ontology", "rdf+ontology",
                                             "csv+neutral", "csv+axioms", "csv+axioms+markdown", "executed"], 1)}
LABELS |= {c: f"D{i}" for i, c in enumerate(["sql", "sql+markdown", "sql+executed",
                                              "sparql", "sparql+ontology", "sparql+axioms"], 1)}


def by_label(c):
    """Sort key: conditions in ladder order, R before D, any without a label last."""
    lab = LABELS.get(c, "Z0")
    return lab[0] == "D", lab[0] == "Z", int(lab[1:])


def cond(c):
    """A condition as the pages show it: its label, then its name."""
    lab = LABELS.get(c)
    return mark_safe((f'<span class="lbl">{lab}</span> ' if lab else "") + f"<code>{c}</code>")


def md(text):
    """Markdown to HTML, with links to the repo's own Markdown files pointed at GitHub, links
    off the site opening in a new tab, and every condition written as `name` given its label."""
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    for name in ("README.md", "RESULTS.md"):
        html = html.replace(f'href="{name}"', f'href="{settings.REPO_URL}/blob/main/{name}"')
    html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)
    html = re.sub(r"<code>([a-z+]+)</code>", lambda m: cond(m[1]) if m[1] in LABELS else m[0], html)
    return mark_safe(html)


# --- site structure: a section of pages per domain --------------------------------------------

CONTENT = ROOT / "docs"  # the pages' text
SECTIONS = [("", "Introduction"), ("data", "Data"), ("questions", "Questions and traps"),
            ("ontology", "Ontology")]
# A domain is one ontology and one question bank, asked of one or more datasets, each a folder in domains/.
# Conditions a dataset's runs leave out on purpose, with the reason the score tables give in their row.
LEFT_OUT = {"research_850": {c: "left out: the prompt, about 770 KB, is too large for the model's context"
                             for c in ("rdf", "rdf+ontology")}}
GROUPS = [("credit", "Credit ratings", [("credit", "The base data"), ("credit_300", "At 300 issuers"),
                                         ("credit_paths", "Ownership paths")]),
          ("research", "Research analytics", [("research", "The base data"), ("research_850", "At 850 works")])]


def page(name):
    """A page's own text: docs/<name>.md, rendered, or "" if there is none."""
    f = CONTENT / f"{name}.md"
    return md(f.read_text()) if f.exists() else ""


def nav():
    """The sidebar's domains, each with a page per section, and its datasets."""
    return [{"name": g, "title": title, "datasets": [{"name": d, "label": label} for d, label in sets
                                                     if (DOMAINS / d / "questions.json").exists()],
             "sections": [{"slug": s, "label": label, "url": f"/domains/{g}/" + (f"{s}/" if s else "")}
                          for s, label in SECTIONS]}
            for g, title, sets in GROUPS]


def group(name):
    """The domain a name belongs to, whether it names the domain or one of its datasets, or None."""
    return next((g for g in nav() if name == g["name"] or name in {d["name"] for d in g["datasets"]}), None)


def title(domain):
    g = group(domain)
    return g["title"] if g else domain


def where(dataset):
    """A dataset as the pages name it: "Credit ratings: at 300 issuers", or just the domain if it has one dataset."""
    g = group(dataset)
    if not g:
        return dataset
    if len(g["datasets"]) == 1:
        return g["title"]
    label = next(d["label"] for d in g["datasets"] if d["name"] == dataset)
    return f"{g['title']}: {label[0].lower()}{label[1:]}"


def trap(q):
    """The trap a question sets, from its `tests` line: ("Time", "a rating holds from ...")."""
    name, _, why = q["tests"].partition(":")
    return name.strip(), why.strip()


def headline(domain):
    """The finished runs on the domain's current questions, the latest for each model, mode and set of
    conditions, leaving out a run whose conditions a newer one with the same model and mode all asked:
    reading before querying, then by model, oldest first."""
    current = json.loads((DOMAINS / domain / "questions.json").read_text())
    found = {}
    for d, f in run_folders(domain):  # newest first
        own = f / "questions.json"
        if own.exists() and json.loads(own.read_text()) != current:
            continue  # asked before the domain last changed: its keys differ
        s = summary(d, f)
        key = (s["mode"], s["meta"]["model"], frozenset(s["meta"]["conditions"]))
        covered = any(k[:2] == key[:2] and key[2] <= k[2] for k in found)
        if s["finished"] and not covered:
            found[key] = s
    return sorted(found.values(), key=lambda s: (s["mode"] != "read", s["meta"]["model"], s["id"]))


def score_table(runs, dataset=""):
    """Runs side by side: a column per run, a row per condition in ladder order, blank where a run didn't ask it,
    and a row for each condition the dataset leaves out on purpose, saying why."""
    left_out = LEFT_OUT.get(dataset, {})
    conditions = sorted({c["condition"] for r in runs for c in r["rows"] if c["repeats"]} | set(left_out), key=by_label)
    cells = [{c["condition"]: c for c in r["rows"] if c["repeats"]} for r in runs]
    return {"runs": runs, "rows": [{"condition": c, "cells": [x.get(c) for x in cells], "left_out": left_out.get(c)}
                                   for c in conditions]}


def domains():
    """Each domain folder with questions: its name, size and conditions."""
    out = []
    for d in sorted(p for p in DOMAINS.iterdir() if (p / "questions.json").exists()):
        out.append({"name": d.name, "questions": len(json.loads((d / "questions.json").read_text())),
                    "scaled": "_" in d.name})
    return out


def domain_info(name):
    folder = DOMAINS / name
    if not (folder / "questions.json").exists():
        return None
    files = sorted(p.name for p in (folder / "data").glob("*.csv"))
    tables = []
    for f in files:
        with open(folder / "data" / f, newline="") as fh:
            rows = list(csv.reader(fh))
        tables.append({"name": f, "header": rows[0], "rows": rows[1:], "n": len(rows) - 1})
    notes = next((folder / n for n in ("NOTES.md", "concepts.md") if (folder / n).exists()), None)
    return {"name": name, "folder": folder, "tables": tables,
            "questions": json.loads((folder / "questions.json").read_text()),
            "notes": md(notes.read_text()) if notes else "", "notes_name": notes.name if notes else "",
            "has": {f: (folder / "ontology" / f).exists() for f in ("ontology.ttl", "ontology.md", "axioms.ttl", "padding.md")}}


def diagram(domain):
    """The domain's ontology diagram, shared by its scaled copies (credit_300 uses credit's): its static path,
    and its <desc> (or else its <title>) as the alt text. None if it has none."""
    name = f"img/{domain.split('_')[0]}-ontology.svg"
    path = settings.WEB_DIR / "static" / name
    if not path.exists():
        return None
    alt = re.search(r"<desc>(.*?)</desc>", path.read_text(), re.S) or re.search(r"<title>(.*?)</title>", path.read_text(), re.S)
    return {"src": name, "alt": alt[1] if alt else ""}


def text(path):
    return path.read_text() if path.exists() else ""


# --- runs ------------------------------------------------------------------------------------

def run_folders(domain=None):
    for d in sorted(RESULTS.iterdir()) if RESULTS.exists() else []:
        if not d.is_dir() or (domain and d.name != domain):
            continue
        for r in sorted(d.iterdir(), reverse=True):
            if (r / "meta.json").exists():
                yield d.name, r


def questions_for(domain, folder, grades):
    """The questions a run was graded on: its own copy if it kept one, else the domain's, filtered."""
    own = folder / "questions.json"
    qs = json.loads(own.read_text()) if own.exists() else json.loads((DOMAINS / domain / "questions.json").read_text())
    asked = {q for sheets in grades.values() for s in sheets for q in s}
    return [q for q in qs if q["id"] in asked]


def summary(domain, folder):
    meta = json.loads((folder / "meta.json").read_text())
    grades_file = folder / "grades.json"
    grades = json.loads(grades_file.read_text()) if grades_file.exists() else {}
    questions = questions_for(domain, folder, grades) if grades else []
    rows = []
    for c in sorted(meta["conditions"], key=by_label):
        sheets = grades.get(c, [])
        if not sheets or not questions:
            rows.append({"condition": c, "repeats": 0})
            continue
        m, lo, hi = report.bootstrap(list(report.per_question(sheets, questions).values()))
        rows.append({"condition": c, "repeats": len(sheets), "acc": round(100 * m), "lo": round(100 * lo), "hi": round(100 * hi)})
    done = sum(r["repeats"] for r in rows)
    return {"domain": domain, "where": where(domain), "id": folder.name, "meta": meta, "rows": rows, "questions": len(questions),
            "mode": meta.get("mode", "read"), "done": done, "planned": meta["runs"] * len(meta["conditions"]),
            "finished": (folder / "report.md").exists() and done >= meta["runs"] * len(meta["conditions"])}


def run_detail(domain, run_id):
    folder = RESULTS / domain / run_id
    if not (folder / "meta.json").exists():
        return None
    s = summary(domain, folder)
    grades = json.loads((folder / "grades.json").read_text()) if (folder / "grades.json").exists() else {}
    questions = questions_for(domain, folder, grades) if grades else []
    conditions = sorted((c for c in s["meta"]["conditions"] if c in grades), key=by_label)
    grid = []
    for q in questions:
        cells = [[{"mark": MARK.get(sh.get(q["id"], {}).get("grade"), "?"),
                   "title": f"{c} run {i + 1}: {sh.get(q['id'], {}).get('grade', '?')}. {sh.get(q['id'], {}).get('why', '')}"}
                  for i, sh in enumerate(grades[c])] for c in conditions]
        grid.append({"q": q, "cells": cells})
    stats = json.loads((folder / "stats.json").read_text()) if (folder / "stats.json").exists() else {}
    query_stats = [{"condition": c, "queries": sum(x["queries"] for x in v), "failed": sum(x["failed"] for x in v),
                    "rounds": round(sum(x["rounds"] for x in v) / len(v), 1), "repeats": len(v),
                    "timeouts": sum(x.get("timeouts", 0) for x in v)} for c, v in sorted(stats.items(), key=lambda kv: by_label(kv[0]))]
    return {**s, "conditions": conditions, "grid": grid, "report": md(text(folder / "report.md")),
            "query_stats": query_stats, "folder": folder}


def answers_for(domain, run_id, qid):
    folder = RESULTS / domain / run_id
    grades = json.loads((folder / "grades.json").read_text())
    q = next((q for q in questions_for(domain, folder, grades) if q["id"] == qid), None)
    if not q:
        return None, []
    from run import split_answers
    import grade
    cards = []
    for c, sheets in grades.items():
        for i, sh in enumerate(sheets):
            f = folder / f"answers-{c}-run{i + 1}.md"
            body = f.read_text() if f.exists() else ""
            g = sh.get(qid, {})
            cards.append({"condition": c, "repeat": i + 1, "grade": g.get("grade", "?"), "mark": MARK.get(g.get("grade"), "?"),
                          "why": g.get("why", ""), "by": g.get("by", ""),
                          "prose": split_answers(body, [q])[qid] if body else "",
                          "json": json.dumps(grade.structured(body).get(qid)) if body else "",
                          "transcript": (folder / f"transcript-{c}-run{i + 1}.json").exists()})
    return q, cards


def transcript(domain, run_id, condition, repeat):
    f = RESULTS / domain / run_id / f"transcript-{condition}-run{repeat}.json"
    if not f.exists():
        return None
    t = json.loads(f.read_text())
    turns = [{"who": who, "text": msg, "first": i == 0} for i, (who, msg) in enumerate(t["turns"])]
    return {"stats": t["stats"], "turns": turns}


def prompt(domain, run_id, condition):
    f = RESULTS / domain / run_id / "prompts" / f"{condition}.md"
    return f.read_text() if f.exists() else ""


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
