"""The report for one run folder: scores with confidence intervals, and how far the graders agree.

    python report.py results/credit/<run>

Questions are the unit. Each question's score in a condition is its mean over repeats; the
condition's accuracy is the mean over questions, with a 95% bootstrap interval from
resampling questions. Differences between conditions are paired: computed question by
question, then resampled the same way.
"""
import json
import random
import sys
from pathlib import Path

SCORE = {"correct": 1.0, "partial": 0.5, "wrong": 0.0}
MARK = {"correct": "✅", "partial": "🟡", "wrong": "❌"}
DRAWS = 5000


def per_question(sheets, questions):
    """{question ID: mean score over the repeats}"""
    return {q["id"]: sum(SCORE.get(s.get(q["id"], {}).get("grade"), 0) for s in sheets) / len(sheets)
            for q in questions}


def bootstrap(values, seed=1):
    rng = random.Random(seed)
    means = sorted(sum(rng.choices(values, k=len(values))) / len(values) for _ in range(DRAWS))
    return sum(values) / len(values), means[int(0.025 * DRAWS)], means[int(0.975 * DRAWS)]


def pct(x):
    return f"{100 * x:.0f}%"


def unstable(sheets, questions):
    """How many questions got different grades across repeats."""
    return sum(len({s.get(q["id"], {}).get("grade") for s in sheets}) > 1 for q in questions)


def write(out, questions):
    out = Path(out)
    meta = json.loads((out / "meta.json").read_text())
    grades = json.loads((out / "grades.json").read_text())
    conditions = [c for c in meta["conditions"] if c in grades]
    scores = {c: per_question(grades[c], questions) for c in conditions}
    n = len(questions)
    lines = [f"# {meta['domain']}: {meta['model']}, {meta['started']}", "",
             f"{n} questions, {min(len(grades[c]) for c in conditions)} repeats per condition. "
             f"Correct = 1, partial = ½. Graded by code where a question has a typed key, by "
             f"{meta['grader']} with a checklist otherwise.", "",
             "## Accuracy", "",
             "| Condition | Accuracy | 95% interval | Questions unstable across repeats |",
             "|---|---|---|---|"]
    for c in conditions:
        m, lo, hi = bootstrap(list(scores[c].values()))
        lines.append(f"| `{c}` | **{pct(m)}** | {pct(lo)} to {pct(hi)} | {unstable(grades[c], questions)} of {n} |")

    base = conditions[0]
    if len(conditions) > 1:
        lines += ["", f"## Against `{base}`, question by question", "",
                  "| Condition | Difference | 95% interval |", "|---|---|---|"]
        for c in conditions[1:]:
            m, lo, hi = bootstrap([scores[c][q["id"]] - scores[base][q["id"]] for q in questions])
            lines.append(f"| `{c}` | {100 * m:+.0f} points | {100 * lo:+.0f} to {100 * hi:+.0f} |")

    lines += ["", "## By question", "", "| Question | Graded by | " + " | ".join(f"`{c}`" for c in conditions) + " |",
              "|---|---|" + "---|" * len(conditions)]
    for q in questions:
        by = grades[conditions[0]][0].get(q["id"], {}).get("by", "?")
        cells = [" ".join(MARK.get(s.get(q["id"], {}).get("grade"), "?") for s in grades[c]) for c in conditions]
        lines.append(f"| {q['id']} | {by} | " + " | ".join(cells) + " |")

    twice = [(s[q["id"]]["grade"], g) for c in conditions for s in grades[c] for q in questions
             if s.get(q["id"], {}).get("also") for g in s[q["id"]]["also"]]
    if twice:
        same = sum(a == b for a, b in twice)
        lines += ["", f"**The checklist grader agreed with itself** on {same} of {len(twice)} answers graded twice."]

    llm_file = out / "grades-llm.json"
    if llm_file.exists():
        llm = json.loads(llm_file.read_text())
        keyed = [q for q in questions if "key" in q]
        pairs = [(grades[c][r][q["id"]]["grade"], llm[c][r].get(q["id"], {}).get("grade"))
                 for c in conditions if c in llm for r in range(len(llm[c])) for q in keyed]
        same = sum(a == b for a, b in pairs)
        lines += ["", "## Code grading against the old LLM grader", "",
                  f"On the questions with typed keys, the two agreed on {same} of {len(pairs)} answers.", "",
                  "| Condition | Accuracy, code | Accuracy, LLM grader | Unstable, code | Unstable, LLM grader |",
                  "|---|---|---|---|---|"]
        for c in [c for c in conditions if c in llm]:
            code = per_question(grades[c], keyed)
            old = per_question(llm[c], keyed)
            lines.append(f"| `{c}` | {pct(sum(code.values()) / len(keyed))} | {pct(sum(old.values()) / len(keyed))} | "
                         f"{unstable(grades[c], keyed)} of {len(keyed)} | {unstable(llm[c], keyed)} of {len(keyed)} |")

    lines += ["", "## Why each miss was marked", ""]
    for q in questions:
        misses = [f"`{c}` run {r + 1}: {s[q['id']]['why']}" for c in conditions for r, s in enumerate(grades[c])
                  if s.get(q["id"], {}).get("grade") != "correct"]
        if misses:
            lines += [f"**{q['id']}.** {q['question']}", ""] + [f"- {m}" for m in misses] + [""]
    (out / "report.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    folder = Path(sys.argv[1])
    meta = json.loads((folder / "meta.json").read_text())
    domain_questions = Path(__file__).parent / "domains" / meta["domain"] / "questions.json"
    write(folder, json.loads(domain_questions.read_text()))
