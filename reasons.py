"""Right for the right reason? A second look at the answers graded correct by code.

    python reasons.py results/credit/<run>                    # every condition, every question
    python reasons.py results/credit/<run> --only Q41 Q42 Q43 # some questions
    python reasons.py results/credit/<run> --conditions csv csv+markdown

Code grading checks only the final value, so an answer can be right by luck, by a guess at a
convention, or by a rule the data doesn't state. Here an LLM grader reads each correct answer's
explanation beside what the question tests, and marks the reasoning sound, unsound (the right
value reached another way) or unclear. Writes reasons.json and reasons.md in the run folder.
"""
import argparse
import json
import re
import sys
from pathlib import Path

import providers
from run import split_answers

SYSTEM = "You check the reasoning behind answers that are already known to be right. You are strict and brief."
PROMPT = """Each answer below reached the right final value. Check how it got there, against what the
question tests. Mark it "sound" if it applies that point, "unsound" if it reached the value another way
(a guess, a convention the data doesn't state, a different rule, or by luck), and "unclear" if it doesn't
say. Reply with JSON only, no code fence, shaped like {{"Q1/csv/1": {{"verdict": "sound", "why": "one short clause"}}}}.

{items}"""
BATCH = 12


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run", type=Path)
    ap.add_argument("--only", nargs="+", help="question IDs")
    ap.add_argument("--conditions", nargs="+", help="conditions (default: all in the run)")
    ap.add_argument("--grader", default="claude:sonnet")
    args = ap.parse_args()
    questions = {q["id"]: q for q in json.loads((args.run / "questions.json").read_text()) if "key" in q}
    if args.only:
        questions = {k: v for k, v in questions.items() if k in args.only}
    grades = json.loads((args.run / "grades.json").read_text())
    items = []
    for c, sheets in grades.items():
        if args.conditions and c not in args.conditions:
            continue
        for r, sheet in enumerate(sheets, 1):
            f = args.run / f"answers-{c}-run{r}.md"
            prose = split_answers(f.read_text(), list(questions.values()))
            for qid, q in questions.items():
                if sheet.get(qid, {}).get("grade") == "correct":
                    items.append((f"{qid}/{c}/{r}", q, prose[qid]))
    out_file = args.run / "reasons.json"
    verdicts = json.loads(out_file.read_text()) if out_file.exists() else {}
    todo = [i for i in items if i[0] not in verdicts]
    for start in range(0, len(todo), BATCH):
        batch = todo[start:start + BATCH]
        text = "\n\n".join(f"{key}. {q['question']}\nWhat it tests: {q['tests']}\nRight value: {json.dumps(q['key'])}\n"
                           f"Answer: {prose}" for key, q, prose in batch)
        print(f"checking {start + 1} to {start + len(batch)} of {len(todo)} ...", flush=True)
        raw = re.sub(r"^```(?:json)?|```$", "", providers.ask(PROMPT.format(items=text), SYSTEM, args.grader).strip()).strip()
        try:
            found = json.loads(raw)
        except json.JSONDecodeError:
            continue
        verdicts.update({k: found[k] for k, _, _ in batch if k in found})
        out_file.write_text(json.dumps(verdicts, indent=1) + "\n")
    write(args.run, verdicts, questions)


def write(run, verdicts, questions):
    conditions = list(dict.fromkeys(k.split("/")[1] for k in verdicts))
    lines = ["# Right for the right reason?", "",
             "Answers graded correct by code, with their reasoning checked by an LLM against what each question tests.", "",
             "| Condition | Correct answers checked | Sound | Unsound | Unclear |", "|---|---|---|---|---|"]
    for c in conditions:
        vs = [v["verdict"] for k, v in verdicts.items() if k.split("/")[1] == c]
        lines.append(f"| `{c}` | {len(vs)} | {vs.count('sound')} | {vs.count('unsound')} | {vs.count('unclear')} |")
    lines += ["", "## Unsound and unclear", ""]
    for k, v in sorted(verdicts.items(), key=lambda x: (int(x[0].split("/")[0][1:]), x[0])):
        if v["verdict"] != "sound":
            lines.append(f"- **{k}** ({v['verdict']}): {v.get('why', '')}")
    (run / "reasons.md").write_text("\n".join(lines) + "\n")
    print(f"report: {run / 'reasons.md'}")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()
