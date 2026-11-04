"""Ask a model the same questions over the same facts, given in different ways, and grade the answers.

    python run.py                                   # credit domain, Sonnet, all conditions, 5 repeats
    python run.py --runs 1 --only csv               # a quick check
    python run.py --llm-grade-all                   # also grade every answer the old way, to compare
    python run.py --resume results/credit/<run>     # finish a stopped run
    python run.py --dry-run                         # write the prompts only

Each answer ends with a JSON block holding the structured answer to every question that has
a typed key; those are graded by code (grade.py). Questions with a checklist instead are
graded by an LLM, twice. Each run writes results/<domain>/<timestamp>-<model>/: meta.json,
the prompts, one answers file per condition and repeat, grades.json and report.md.
"""
import argparse
import importlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import grade
import providers
import report

HERE = Path(__file__).parent
CONDITIONS = ["csv", "rdf", "rdf+ontology", "csv+ontology", "csv+markdown", "csv+padding"]

INSTRUCTIONS = """Answer each question below from the data above. Start each answer on a new line with its
number in bold, like **Q1.**, give the direct answer first, then at most two sentences of
reasoning that cite the records (IDs) you relied on.

Then end with one JSON block (```json) holding the structured answer to each question listed
here, with exactly these fields, shaped like {{"Q1": {{"field": value}}, ...}}. {entity_hint}

{fields}"""

KINDS = {"rating": 'a rating, or "none"', "yesno": '"yes", "no" or "depends"', "outlook": "an outlook",
         "country": "a country code", "entity": "a record ID", "entities": "a list of record IDs", "count": "a number"}


def prompt(domain, condition, questions):
    fields = "\n".join(
        f"- {q['id']}: " + ", ".join(f"{f} ({KINDS[k]})" for f, k in q["fields"].items())
        for q in questions if "fields" in q)
    qs = "\n".join(f"{q['id']}. {q['question']}" for q in questions)
    text = INSTRUCTIONS.format(entity_hint=domain.ENTITY_HINT, fields=fields)
    return f"## The data\n\n{domain.context(condition)}\n\n## Questions\n\n{text}\n\n{qs}\n"


def split_answers(text, questions):
    """{'Q1': '...', ...} from an answer that marks each question **Qn.**, without the JSON block."""
    text = re.sub(r"```json.*?```", "", text, flags=re.S)
    marks = list(re.finditer(r"\*\*(Q\d+)\.?\*\*\.?", text))
    found = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        found.setdefault(m.group(1), text[m.end():end].strip())
    return {q["id"]: found.get(q["id"], "(no answer found)") for q in questions}


def commit():
    """The repo's commit, so a result can be traced to the data and questions it ran on."""
    out = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=HERE)
    dirty = subprocess.run(["git", "status", "--porcelain", "domains"], capture_output=True, text=True, cwd=HERE).stdout
    return out.stdout.strip() + ("-dirty" if dirty.strip() else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", default="credit")
    ap.add_argument("--model", default="claude:sonnet", help="provider:model for the answers")
    ap.add_argument("--grader", default="claude:sonnet", help="provider:model for checklist grading")
    ap.add_argument("--runs", type=int, default=5, help="repeats per condition (default 5)")
    ap.add_argument("--only", nargs="+", choices=CONDITIONS)
    ap.add_argument("--llm-grade-all", action="store_true",
                    help="also grade every answer with the old LLM grader, into grades-llm.json")
    ap.add_argument("--resume", type=Path, help="a run folder to finish: answers already there are kept")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--regrade", type=Path, help="a run folder: redo its code grading, with no model calls")
    args = ap.parse_args()

    domain = importlib.import_module(f"domains.{args.domain}.domain")
    questions = json.loads(domain.QUESTIONS.read_text())
    conditions = args.only or CONDITIONS
    canon = domain.canonical()

    if args.regrade:
        grades = json.loads((args.regrade / "grades.json").read_text())
        for c, sheets in grades.items():
            for r, sheet in enumerate(sheets):
                text = (args.regrade / f"answers-{c}-run{r + 1}.md").read_text()
                sheets[r] = grade.regrade(questions, sheet, grade.structured(text), canon)
        (args.regrade / "grades.json").write_text(json.dumps(grades, indent=2) + "\n")
        report.write(args.regrade, questions)
        print(f"regraded: {args.regrade / 'report.md'}")
        return

    out = args.resume or HERE / "results" / args.domain / f"{datetime.now():%Y-%m-%d-%H%M}-{providers.split(args.model)[1]}"
    (out / "prompts").mkdir(parents=True, exist_ok=True)
    meta = {"domain": args.domain, "model": args.model, "grader": args.grader, "runs": args.runs,
            "conditions": conditions, "started": f"{datetime.now():%Y-%m-%d %H:%M}",
            "questions": len(questions), "commit": commit()}
    if not (out / "meta.json").exists():
        (out / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    # Every prompt is built once, at the start, and kept: editing the data mid-run can't
    # mix two datasets in one run, and a resumed run asks exactly what it asked before.
    prompts = {}
    for c in conditions:
        f = out / "prompts" / f"{c}.md"
        if not f.exists():
            f.write_text(f"<!-- system: {domain.SYSTEM} -->\n\n{prompt(domain, c, questions)}")
        prompts[c] = f.read_text().split(" -->\n\n", 1)[1]
    if args.dry_run:
        print(f"prompts written to {out}/prompts/")
        return

    def ask_grader(text, system):
        return providers.ask(text, system, args.grader)

    grades = {c: [] for c in conditions}
    llm = {c: [] for c in conditions}
    for c in conditions:
        for r in range(args.runs):
            f = out / f"answers-{c}-run{r + 1}.md"
            if not f.exists():
                print(f"asking: {c}, run {r + 1} ...", flush=True)
                f.write_text(providers.ask(prompts[c], domain.SYSTEM, args.model))
            text = f.read_text()
            prose = split_answers(text, questions)
            print(f"grading: {c}, run {r + 1} ...", flush=True)
            grades[c].append(grade.grade(questions, prose, grade.structured(text), canon, ask_grader))
            if args.llm_grade_all:
                llm[c].append(grade.by_llm(questions, prose, ask_grader, grade.LLM_ALL))
            (out / "grades.json").write_text(json.dumps({k: v for k, v in grades.items() if v}, indent=2) + "\n")
            if args.llm_grade_all:
                (out / "grades-llm.json").write_text(json.dumps({k: v for k, v in llm.items() if v}, indent=2) + "\n")
    report.write(out, questions)
    print(f"report: {out / 'report.md'}")


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    main()
