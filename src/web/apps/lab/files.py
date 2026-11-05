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


def md(text):
    """Markdown to HTML, with links to the repo's own Markdown files pointed at their pages."""
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    for name, url in (("README.md", "/readme/"), ("PLAN.md", "/plan/"), ("RESULTS.md", "/log/")):
        html = html.replace(f'href="{name}"', f'href="{url}"')
    return mark_safe(html)


def doc(name):
    return md((ROOT / f"{name}.md").read_text())


# --- site structure: a section of pages per domain --------------------------------------------

CONTENT = settings.WEB_DIR / "content"
SECTIONS = [("", "Introduction"), ("data", "Data"), ("questions", "Questions and traps"),
            ("ontology", "Ontology"), ("results", "Results")]
FAMILIES = [("credit", "Credit ratings"), ("credit_300", "Credit at 300 issuers"),
            ("credit_paths", "Credit: ownership paths"), ("research", "Research analytics")]


def page(name):
    """A page's own text: content/<name>.md, rendered, or "" if there is none."""
    f = CONTENT / f"{name}.md"
    return md(f.read_text()) if f.exists() else ""


def nav():
    """The sidebar's domain groups: each domain with a page per section."""
    return [{"name": d, "title": title, "sections": [{"slug": s, "label": label,
             "url": f"/domains/{d}/" + (f"{s}/" if s else "")} for s, label in SECTIONS]}
            for d, title in FAMILIES if (DOMAINS / d / "questions.json").exists()]


def title(domain):
    return dict(FAMILIES).get(domain, domain)


def trap(q):
    """The trap a question sets, from its `tests` line: ("Time", "a rating holds from ...")."""
    name, _, why = q["tests"].partition(":")
    return name.strip(), why.strip()


def headline(domain):
    """The latest finished run of each mode, for a domain's introduction."""
    found = {}
    for d, f in run_folders(domain):
        s = summary(d, f)
        key = (s["mode"], s["meta"]["model"])
        if s["finished"] and key not in found:
            found[key] = s
    return sorted(found.values(), key=lambda s: (s["mode"], s["meta"]["model"]))


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
            "has": {f: (folder / f).exists() for f in ("ontology.ttl", "ontology.md", "axioms.ttl", "padding.md")}}


def diagram(domain):
    """The static path of the domain's ontology diagram, shared by its scaled copies (credit_300 uses credit's), or ""."""
    name = f"img/{domain.split('_')[0]}-ontology.svg"
    return name if (settings.WEB_DIR / "static" / name).exists() else ""


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
    for c in meta["conditions"]:
        sheets = grades.get(c, [])
        if not sheets or not questions:
            rows.append({"condition": c, "repeats": 0})
            continue
        m, lo, hi = report.bootstrap(list(report.per_question(sheets, questions).values()))
        rows.append({"condition": c, "repeats": len(sheets), "acc": round(100 * m), "lo": round(100 * lo), "hi": round(100 * hi)})
    done = sum(r["repeats"] for r in rows)
    return {"domain": domain, "id": folder.name, "meta": meta, "rows": rows, "questions": len(questions),
            "mode": meta.get("mode", "read"), "done": done, "planned": meta["runs"] * len(meta["conditions"]),
            "finished": (folder / "report.md").exists() and done >= meta["runs"] * len(meta["conditions"])}


def run_detail(domain, run_id):
    folder = RESULTS / domain / run_id
    if not (folder / "meta.json").exists():
        return None
    s = summary(domain, folder)
    grades = json.loads((folder / "grades.json").read_text()) if (folder / "grades.json").exists() else {}
    questions = questions_for(domain, folder, grades) if grades else []
    conditions = [c for c in s["meta"]["conditions"] if c in grades]
    grid = []
    for q in questions:
        cells = [[{"mark": MARK.get(sh.get(q["id"], {}).get("grade"), "?"),
                   "title": f"{c} run {i + 1}: {sh.get(q['id'], {}).get('grade', '?')}. {sh.get(q['id'], {}).get('why', '')}"}
                  for i, sh in enumerate(grades[c])] for c in conditions]
        grid.append({"q": q, "cells": cells})
    stats = json.loads((folder / "stats.json").read_text()) if (folder / "stats.json").exists() else {}
    query_stats = [{"condition": c, "queries": sum(x["queries"] for x in v), "failed": sum(x["failed"] for x in v),
                    "rounds": round(sum(x["rounds"] for x in v) / len(v), 1), "repeats": len(v),
                    "timeouts": sum(x.get("timeouts", 0) for x in v)} for c, v in stats.items()]
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
