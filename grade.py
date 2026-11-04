"""Grading: by code against typed keys where a question has them, by an LLM with a checklist otherwise.

A question with `fields` and `key` is graded by code: the answer's JSON block must give each
field, and each is compared with the key after normalising (ratings, yes/no/depends,
outlooks, entities by the domain's canonical IDs, counts). All fields right is correct,
some is partial, none is wrong. A question with a `checklist` is graded by the LLM, twice,
so the grader's own agreement can be measured.
"""
import json
import re

OUTLOOKS = {"sta": "stable", "stable": "stable", "pos": "positive", "positive": "positive",
            "neg": "negative", "negative": "negative"}


def structured(text):
    """The answer's last ```json block, as a dict keyed by question ID, or {}."""
    blocks = re.findall(r"```json\s*(.*?)```", text, re.S)
    if not blocks:
        return {}
    try:
        found = json.loads(blocks[-1])
    except json.JSONDecodeError:
        return {}
    return found if isinstance(found, dict) else {}


def normalise(kind, value, canon):
    if kind == "rating":  # no rating can come as null, "none", "NR" or "not rated"
        r = "" if value is None else str(value).strip().upper().replace(" ", "").replace("−", "-")
        return "NONE" if r in ("", "NONE", "NULL", "NR", "NOTRATED", "N/A") else r
    if value is None:
        return None
    if kind == "yesno":
        if isinstance(value, bool):
            return "yes" if value else "no"
        return str(value).strip().lower()
    if kind == "outlook":
        return OUTLOOKS.get(str(value).strip().lower(), str(value).strip().lower())
    if kind == "entity":
        return canon.get(str(value).strip(), str(value).strip())
    if kind == "entities":
        items = value if isinstance(value, list) else [value]
        return sorted({canon.get(str(v).strip(), str(v).strip()) for v in items})
    if kind == "count":
        try:
            return int(value)
        except (TypeError, ValueError):
            return None
    raise ValueError(kind)


def by_code(q, answer, canon):
    if not answer:
        return {"grade": "wrong", "why": "no structured answer", "by": "code"}
    right, wrong = [], []
    for field, kind in q["fields"].items():
        got, want = normalise(kind, answer.get(field), canon), normalise(kind, q["key"][field], canon)
        (right if got == want else wrong).append(f"{field}: expected {q['key'][field]}, got {answer.get(field)}")
    grade = "correct" if not wrong else "partial" if right else "wrong"
    return {"grade": grade, "why": "; ".join(wrong) or "all fields match", "by": "code"}


GRADER_SYSTEM = "You grade answers against an answer key. You are strict and brief."

GRADER = """For each question, check the answer against its checklist and grade it: "correct" if it
meets every point, "partial" if it meets some, "wrong" if it meets none. Reply with JSON only,
no code fence, shaped like {{"Q6": {{"grade": "correct", "why": "one short clause"}}}}.

{pairs}"""

LLM_ALL = """For each question, compare the answer with the expected answer and grade it:
"correct" if it reaches the expected conclusion, "partial" if it is right in part or right
for the wrong reason, "wrong" otherwise. Reply with JSON only, no code fence, shaped like
{{"Q1": {{"grade": "correct", "why": "one short clause"}}, ...}}.

{pairs}"""


def by_llm(questions, answers, ask, template=GRADER):
    """One grader call over several questions; one retry if the reply isn't JSON."""
    if template is GRADER:
        pairs = "\n\n".join(
            f"{q['id']}. {q['question']}\nChecklist:\n" + "\n".join(f"- {p}" for p in q["checklist"])
            + f"\nAnswer: {answers[q['id']]}" for q in questions)
    else:
        pairs = "\n\n".join(f"{q['id']}. {q['question']}\nExpected: {q['expected']}\nAnswer: {answers[q['id']]}"
                            for q in questions)
    for _ in range(2):
        raw = re.sub(r"^```(?:json)?|```$", "", ask(template.format(pairs=pairs), GRADER_SYSTEM).strip()).strip()
        try:
            found = json.loads(raw)
            return {q["id"]: dict(found.get(q["id"], {"grade": "?", "why": "not graded"}), by="llm") for q in questions}
        except json.JSONDecodeError:
            pass
    return {q["id"]: {"grade": "?", "why": "grader reply was not JSON", "by": "llm"} for q in questions}


def regrade(questions, sheet, parsed, canon):
    """Redo the code grading of one sheet, keeping its LLM grades: after a grader fix, with no calls."""
    new = dict(sheet)
    for q in questions:
        if "key" in q:
            new[q["id"]] = by_code(q, parsed.get(q["id"]), canon)
    return new


def grade(questions, prose, parsed, canon, ask, llm_repeats=2):
    """One sheet: {question ID: {grade, why, by}}, plus the second LLM grading where there is one."""
    sheet = {q["id"]: by_code(q, parsed.get(q["id"]), canon) for q in questions if "key" in q}
    checked = [q for q in questions if "checklist" in q]
    if checked:
        rounds = [by_llm(checked, prose, ask) for _ in range(llm_repeats)]
        for q in checked:
            sheet[q["id"]] = dict(rounds[0][q["id"]], also=[r[q["id"]]["grade"] for r in rounds[1:]])
    return sheet
