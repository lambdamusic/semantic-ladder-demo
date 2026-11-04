"""Write questions.json: each question's key computed from the CSV files, and checked against the key written by hand.

    python domains/credit/build_questions.py

Two answers for every typed key: the one written below by hand, and one computed by the
functions here from the data. The build stops if they differ, so a key can't silently
disagree with the data after an edit.
"""
import csv
import json
import os
from pathlib import Path

HERE = Path(__file__).parent
# A scaled copy of the domain (scale.py) sets CREDIT_FOLDER: its data is read and its
# questions written there, with keys computed from the data only, since none were written by hand.
FOLDER = Path(os.environ.get("CREDIT_FOLDER", HERE))
DATA = FOLDER / "data"
SCALE = ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-",
         "BB+", "BB", "BB-", "B+", "B", "B-", "CCC", "CC", "C", "RD", "D"]
NOW = "2026-10-01"


def rows(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


# The local rules the ontology states, applied here as the data's owner would:
# QA records are test data, so they and their actions are dropped; expected ratings (EX)
# are not ratings yet; credit opinions (CO) never count as ratings, since only the types
# asked for are read; where records of one entity disagree, RESEARCH holds for country and
# RATINGS for everything else.
QA = {e["entity_id"] for e in rows("entities.csv") if e["source_system"] == "QA"}
ENTITIES = {e["entity_id"]: e for e in rows("entities.csv") if e["entity_id"] not in QA}
INSTRUMENTS = {i["instrument_id"]: i for i in rows("instruments.csv")}
ACTIONS = sorted((a for a in rows("rating_actions.csv") if a["rated_id"] not in QA and a["action"] != "EX"),
                 key=lambda a: a["date"])
CANON = {i: e["lei"] or i for i, e in ENTITIES.items()}
LOCAL = {"XVD": "VD", "CVK": "CV"}  # the local currency codes, and whose domestic currency each is


def record_of(entity, system):
    """The entity's record from this system if it has one, else its lowest record ID."""
    return sorted(same(entity), key=lambda i: (ENTITIES[i]["source_system"] != system, i))[0]


def country(entity):
    """Where the entity is domiciled, by its RESEARCH record where its records disagree."""
    return ENTITIES[record_of(entity, "RESEARCH")]["country"]


def canonical_id(record):
    return min(same(record))


def same(a):
    """The records that are the same entity as record a."""
    return {i for i in ENTITIES if CANON[i] == CANON[a]}


def latest(thing, kind="LTIDR", basis="FC", as_of=NOW):
    """The latest action on or before as_of for this thing (any of its records), type and basis."""
    things = same(thing) if thing in ENTITIES else {thing}
    found = [a for a in ACTIONS if a["rated_id"] in things and a["rating_type"] == kind
             and (a["ccy_basis"] == basis or kind in ("INST", "CC")) and a["date"] <= as_of]
    return found[-1] if found else None


def rating(thing, kind="LTIDR", basis="FC", as_of=NOW):
    a = latest(thing, kind, basis, as_of)
    return a["rating"] if a else "none"


def investment_grade(r):
    return r in SCALE and SCALE.index(r) <= SCALE.index("BBB-")


def issuers_rated(as_of=NOW):
    """One record per entity with an issuer rating in force (not withdrawn)."""
    found = {}
    for i in ENTITIES:
        for basis in ("FC", "LC"):
            a = latest(i, "LTIDR", basis, as_of)
            if a and a["rating"] != "WD":
                found.setdefault(CANON[i], min(same(i)))
    return sorted(found.values())


def downgrades(entity, start="0000", end="9999"):
    return [a for a in ACTIONS if a["rated_id"] in same(entity) and a["action"] == "DG"
            and a["rating_type"] == "LTIDR" and start <= a["date"] <= end]


def parent(e):
    """The entity's parent, by its RATINGS record, as a canonical record ID ("" for none)."""
    p = ENTITIES[record_of(e, "RATINGS")]["parent_id"]
    return canonical_id(p) if p else ""


def chain(e):
    """The entity's ancestors, nearest first, as canonical record IDs."""
    out, e = [], canonical_id(e)
    while parent(e):
        e = parent(e)
        out.append(e)
    return out


def ultimate_parent(e):
    up = chain(e)
    return up[-1] if up else canonical_id(e)


def group(top):
    """Distinct entities whose chain of parents ends at top, top included."""
    return {CANON[i] for i in ENTITIES if CANON[ultimate_parent(i)] == CANON[top]}


def ceiling(country, as_of=NOW):
    sovereigns = [i for i, e in ENTITIES.items() if e["entity_type"] == "SOV" and e["country"] == country]
    return rating(sovereigns[0], "CC", as_of=as_of) if sovereigns else "none"


def at_or_above_ceiling(above):
    out = []
    for i in issuers_rated():
        r, c = rating(i), ceiling(country(i))
        if r in SCALE and c in SCALE and ENTITIES[i]["entity_type"] != "SOV":
            if (SCALE.index(r) < SCALE.index(c)) if above else (r == c):
                out.append(i)
    return out


def risk_of(instrument):
    i = INSTRUMENTS[instrument]
    return i["guarantor_id"] or i["issuer_id"]


# id, question, fields, the key by hand, the key computed, what it tests
Q = [
    ("Q1", "What was Kestrel Energy's rating on 1 January 2025?", {"rating": "rating"},
     {"rating": "A-"}, lambda: {"rating": rating("E01", as_of="2025-01-01")},
     "Time: a rating holds from one action to the next, so 'the rating on a date' is the latest action on or before it."),
    ("Q2", "Has Kestrel Energy been downgraded in 2026?", {"downgraded": "yesno"},
     {"downgraded": "no"}, lambda: {"downgraded": "yes" if downgrades("E01", "2026") else "no"},
     "Outlook versus rating: an affirmation with a negative outlook is not a rating change."),
    ("Q3", "Is Kestrel Energy's 2031 note investment grade?", {"investment_grade": "yesno", "rating": "rating"},
     {"investment_grade": "no", "rating": "BB+"},
     lambda: {"investment_grade": "yes" if investment_grade(rating("I02", "INST")) else "no", "rating": rating("I02", "INST")},
     "Issuer versus instrument rating: a subordinated instrument is notched below the issuer."),
    ("Q4", "What is Northwind Holdings' current outlook?", {"outlook": "outlook"},
     {"outlook": "positive"}, lambda: {"outlook": {"POS": "positive", "NEG": "negative", "STA": "stable"}[latest("E02")["outlook"]]},
     "Identity: two records with the same LEI are one entity, whatever their names."),
    ("Q5", "Whose credit risk does a holder of the Northwind Finance 2030 notes take, and how is it rated?",
     {"risk_of": "entity", "rating": "rating"},
     {"risk_of": "E02", "rating": "A"}, lambda: {"risk_of": risk_of("I03"), "rating": rating("I03", "INST")},
     "Roles: issuer versus guarantor; a finance subsidiary's guaranteed debt carries the guarantor's risk."),
    ("Q7", "Which issuers were downgraded in 2026?", {"issuers": "entities"},
     {"issuers": ["E08", "E10"]},
     lambda: {"issuers": sorted({min(same(a["rated_id"])) for i in ENTITIES for a in downgrades(i, "2026")})},
     "Action types: outlook changes, Watch placements and withdrawals are not downgrades."),
    ("Q8", "Which entities were in default on 1 October 2026?", {"entities": "entities"},
     {"entities": ["E08"]}, lambda: {"entities": [i for i in issuers_rated() if rating(i) in ("RD", "D")]},
     "Default semantics: RD is a default; WD (withdrawn) is not a credit event."),
    ("Q9", "As of 1 October 2026, how many distinct issuers hold an issuer rating?", {"count": "count"},
     {"count": 12}, lambda: {"count": len(issuers_rated())},
     "Everything at once: identity, withdrawal, instrument versus issuer, ceiling versus rating."),
    ("Q10", "Is Valdoria Telecom investment grade?", {"investment_grade": "yesno"},
     {"investment_grade": "depends"},
     lambda: {"investment_grade": "depends" if investment_grade(rating("E05", basis="LC")) != investment_grade(rating("E05")) else "?"},
     "Ambiguity: 'the rating' of a company is several ratings; the investment-grade line is BBB-."),

    # Time
    ("Q11", "What was Marlow Utilities' rating on 1 June 2025?", {"rating": "rating"},
     {"rating": "BBB+"}, lambda: {"rating": rating("E14", as_of="2025-06-01")},
     "Time: Marlow's actions are not in date order in the file."),
    ("Q12", "What was Marlow Utilities' rating on 1 January 2024?", {"rating": "rating"},
     {"rating": "A-"}, lambda: {"rating": rating("E14", as_of="2024-01-01")},
     "Time: the rating on a date before a later downgrade."),
    ("Q13", "How many times has Marlow Utilities been downgraded?", {"count": "count"},
     {"count": 1}, lambda: {"count": len(downgrades("E14"))},
     "Action types over time: a Watch placement and an affirmation are not downgrades."),
    ("Q14", "What was Halden Foods' rating on 1 January 2024?", {"rating": "rating"},
     {"rating": "none"}, lambda: {"rating": rating("E12", as_of="2024-01-01")},
     "Time: before its first action, an entity has no rating."),
    ("Q15", "What was Halden Bank's rating on 1 January 2026?", {"rating": "rating"},
     {"rating": "A-"}, lambda: {"rating": rating("E10", as_of="2026-01-01")},
     "Time: the downgrade came later in 2026."),

    # Outlook and Watch
    ("Q16", "Has Marlow Utilities' rating changed since 1 January 2025?", {"changed": "yesno"},
     {"changed": "no"}, lambda: {"changed": "yes" if rating("E14") != rating("E14", as_of="2025-01-01") else "no"},
     "Watch versus rating: a Watch placement and an affirmation leave the rating where it was."),
    ("Q17", "Was Orrin Bank downgraded in 2026?", {"downgraded": "yesno"},
     {"downgraded": "no"}, lambda: {"downgraded": "yes" if downgrades("E06", "2026") else "no"},
     "Watch versus rating: Rating Watch Negative is not a downgrade."),
    ("Q18", "Which issuers were on Rating Watch Negative on 1 October 2026?", {"issuers": "entities"},
     {"issuers": ["E06"]}, lambda: {"issuers": [i for i in issuers_rated() if latest(i)["watch"] == "RWN"]},
     "Watch over time: Marlow's Watch ended with its 2026 affirmation."),
    ("Q19", "Which issuers had a Negative outlook on 1 October 2026?", {"issuers": "entities"},
     {"issuers": ["E01", "E09"]}, lambda: {"issuers": [i for i in issuers_rated() if latest(i)["outlook"] == "NEG"]},
     "Outlooks: set by affirmations, without a rating change."),

    # Withdrawn and default
    ("Q20", "Is Pellam Retail in default?", {"in_default": "yesno"},
     {"in_default": "no"}, lambda: {"in_default": "yes" if rating("E07") in ("RD", "D") else "no"},
     "Withdrawn is not defaulted."),
    ("Q21", "Which entities had an issuer rating at some point but no longer had one on 1 October 2026?",
     {"entities": "entities"}, {"entities": ["E07"]},
     lambda: {"entities": sorted({min(same(a["rated_id"])) for a in ACTIONS if a["rating_type"] == "LTIDR"} - set(issuers_rated()))},
     "Withdrawals: a withdrawn rating is no rating."),
    ("Q22", "Which entities have ever been in default?", {"entities": "entities"},
     {"entities": ["E08"]},
     lambda: {"entities": sorted({min(same(a["rated_id"])) for a in ACTIONS if a["rating"] in ("RD", "D")})},
     "Default semantics: RD is a default; WD is not."),

    # What is rated
    ("Q23", "What is Kestrel Energy's short-term rating?", {"rating": "rating"},
     {"rating": "F2"}, lambda: {"rating": rating("E01", "STIDR")},
     "Rating types: the short-term rating is a different rating, on a different scale."),
    ("Q24", "Is Kestrel Energy's issuer rating investment grade?", {"investment_grade": "yesno"},
     {"investment_grade": "yes"}, lambda: {"investment_grade": "yes" if investment_grade(rating("E01")) else "no"},
     "Issuer versus instrument: BBB, at the issuer, even though one note is below investment grade."),
    ("Q25", "How many instruments held an investment-grade rating on 1 October 2026?", {"count": "count"},
     {"count": 5}, lambda: {"count": sum(investment_grade(rating(i, "INST")) for i in INSTRUMENTS)},
     "Instrument ratings: counted on the instrument's own rating, not its issuer's."),
    ("Q26", "What is Corvenia Power's local-currency rating?", {"rating": "rating"},
     {"rating": "A+"}, lambda: {"rating": rating("E15", basis="LC")},
     "Currency basis: the local-currency rating is a separate rating."),
    ("Q27", "How is Corvenia Power's 2032 note rated?", {"rating": "rating"},
     {"rating": "A-"}, lambda: {"rating": rating("I06", "INST")},
     "Instrument versus issuer: the subordinated note sits below the issuer."),

    # Ceilings and sovereigns
    ("Q28", "What is the Republic of Corvenia's foreign-currency issuer rating?", {"rating": "rating"},
     {"rating": "BBB+"}, lambda: {"rating": rating("CV")},
     "Ceiling versus sovereign rating: Corvenia's ceiling (A) is not its rating (BBB+)."),
    ("Q29", "What is the Republic of Valdoria's issuer rating?", {"rating": "rating"},
     {"rating": "none"}, lambda: {"rating": rating("VD")},
     "Ceilings: Valdoria has a Country Ceiling and no issuer rating."),
    ("Q30", "Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?",
     {"entities": "entities"}, {"entities": ["E05", "E15"]}, lambda: {"entities": at_or_above_ceiling(False)},
     "Ceilings: which ratings the cap binds."),
    ("Q31", "Did any company have a foreign-currency issuer rating above its country's ceiling on 1 October 2026?",
     {"any": "yesno"}, {"any": "no"}, lambda: {"any": "yes" if at_or_above_ceiling(True) else "no"},
     "Ceilings: the sovereign's own rating can be below its ceiling, and a local-currency rating above it."),

    # Groups and support
    ("Q32", "Who is Halden Leasing's ultimate parent?", {"parent": "entity"},
     {"parent": "E09"}, lambda: {"parent": ultimate_parent("E11")},
     "Groups: the chain of parents, two levels up."),
    ("Q33", "Whose credit risk does a holder of the Halden Leasing 2028 notes take, and how is it rated?",
     {"risk_of": "entity", "rating": "rating"},
     {"risk_of": "E10", "rating": "BBB+"}, lambda: {"risk_of": risk_of("I05"), "rating": rating("I05", "INST")},
     "Roles: the guarantor is the parent, not the ultimate parent."),
    ("Q34", "Is Halden Foods part of the same group as Halden Bank?", {"same_group": "yesno"},
     {"same_group": "no"}, lambda: {"same_group": "yes" if ultimate_parent("E12") == ultimate_parent("E10") else "no"},
     "Groups: a shared name is not a shared group."),
    ("Q35", "How many entities are in the Halden group, the parent included?", {"count": "count"},
     {"count": 3}, lambda: {"count": len(group("E09"))},
     "Groups: membership comes from parent links, not names."),
    ("Q36", "How many entities are in the Northwind group, the parent included?", {"count": "count"},
     {"count": 2}, lambda: {"count": len(group("E02"))},
     "Groups and identity: two records of the parent are one entity."),

    # Identity
    ("Q37", "How many distinct legal entities does the data describe?", {"count": "count"},
     {"count": 16}, lambda: {"count": len(set(CANON.values()))},
     "Identity: records with the same LEI are one entity."),
    ("Q38", "Are Orrin Bank AG and Orrin Bancorp Inc the same entity?", {"same": "yesno"},
     {"same": "no"}, lambda: {"same": "yes" if CANON["E06"] == CANON["E13"] else "no"},
     "Identity: similar names, different LEIs."),
    ("Q39", "What is Northwind Holdings' current rating?", {"rating": "rating"},
     {"rating": "A"}, lambda: {"rating": rating("E02")},
     "Identity: the latest action sits on the other record."),
    ("Q40", "How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?", {"count": "count"},
     {"count": 5}, lambda: {"count": sum(country(i) == "GB" for i in issuers_rated())},
     "Identity and withdrawal: Northwind counted once, Pellam not at all, the QA record ignored."),

    # Local meanings: rules this dataset sets for itself, stated only in the ontology
    ("Q41", "What is Brindle Capital's current rating?", {"rating": "rating"},
     {"rating": "none"}, lambda: {"rating": rating("E16")},
     "Local rule: QA records are test data and describe no real entity."),
    ("Q42", "In which country is Halden Bank domiciled?", {"country": "country"},
     {"country": "LU"}, lambda: {"country": country("E10")},
     "Local rule: where records disagree on country, the RESEARCH record holds."),
    ("Q43", "How many distinct entities are domiciled in Luxembourg (LU)?", {"count": "count"},
     {"count": 1}, lambda: {"count": len({CANON[i] for i in ENTITIES if country(i) == "LU"})},
     "Local rule: the RESEARCH record's country holds over the RATINGS record's, so Halden Bank is in LU."),
    ("Q44", "Is Valdoria Telecom's 2027 note a local-currency obligation?", {"local_currency": "yesno"},
     {"local_currency": "yes"},
     lambda: {"local_currency": "yes" if LOCAL.get(INSTRUMENTS["I07"]["currency"]) == country("E05") else "no"},
     "Local codes: XVD is the Valdorian dollar."),
    ("Q45", "Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?",
     {"above_ceiling": "yesno"}, {"above_ceiling": "no"},
     lambda: {"above_ceiling": "yes" if LOCAL.get(INSTRUMENTS["I07"]["currency"]) != country("E05")
              and SCALE.index(rating("I07", "INST")) < SCALE.index(ceiling("VD")) else "no"},
     "Local codes and ceilings: local-currency debt is not capped, so BBB- above a BB ceiling is allowed."),
    ("Q46", "Does Halden Leasing have an issuer rating?", {"issuer_rating": "yesno"},
     {"issuer_rating": "no"}, lambda: {"issuer_rating": "yes" if rating("E11") != "none" else "no"},
     "Local type: a credit opinion (CO) is not a rating."),
    ("Q47", "How is Corvenia Power's 2034 note rated?", {"rating": "rating"},
     {"rating": "none"}, lambda: {"rating": rating("I08", "INST")},
     "Local action: an expected rating (EX) is not a rating until assigned."),
    ("Q48", "How many instruments held a rating on 1 October 2026?", {"count": "count"},
     {"count": 7}, lambda: {"count": sum(rating(i, "INST") != "none" for i in INSTRUMENTS)},
     "Local action: the expected rating doesn't count."),
]

# Answered in prose and graded by an LLM against a checklist.
CHECKLIST = {
    "Q6": ("Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?",
           ["Names the Country Ceiling for Valdoria (BB) as the cause",
            "Says the ceiling caps foreign-currency ratings and not local-currency ones"],
           "Ceilings: a Country Ceiling is a cap on foreign-currency ratings, not a rating of the sovereign or of the company."),
}


def name(e):
    return ENTITIES[record_of(e, "RATINGS")]["name"]


def nearest_common(a, b):
    up = [canonical_id(a)] + chain(a)
    return next((x for x in [canonical_id(b)] + chain(b) if x in up), "none")


def path_questions(anchors):
    """Questions that follow parent and guarantee links: written from the designed groups in anchors.json."""
    G = anchors["groups"]
    top = [g["top"] for g in G]
    deep = G[0]["deepest"]
    stale = anchors["stale_parent"]["entity"]
    # two members of the same level with different parents but a common ancestor below the top
    pair = next((a, b) for g in G for lv in g["levels"][3:] for a in lv for b in lv
                if a < b and parent(a) != parent(b) and nearest_common(a, b) != g["top"])
    note = anchors["cross_note"]
    for e in [deep, stale, *top, *pair]:  # each entity a question names must be the only one with that name
        assert sum(ENTITIES[i]["name"].lower() == name(e).lower() for i in ENTITIES if CANON[i] != CANON[e]) == 0, name(e)
    members = lambda t: sorted({canonical_id(i) for i in ENTITIES if ultimate_parent(i) == canonical_id(t)})
    below = lambda e: {x for x in members(ultimate_parent(e)) if e in chain(x)}
    exposed = sorted(i for i in issuers_rated() if any(country(a) == "VD" for a in chain(i)))
    cross = sorted({canonical_id(INSTRUMENTS[i]["guarantor_id"]) for i in INSTRUMENTS if INSTRUMENTS[i]["guarantor_id"]
                    and ultimate_parent(INSTRUMENTS[i]["guarantor_id"]) != ultimate_parent(INSTRUMENTS[i]["issuer_id"])})
    fc = lambda e: rating(e)
    lowest = max((fc(e) for e in members(top[4]) if fc(e) in SCALE), key=SCALE.index, default="none")
    return [
        ("Q49", f"Who is {name(deep)}'s ultimate parent?", {"parent": "entity"}, None,
         lambda: {"parent": ultimate_parent(deep)},
         "Paths and identity: a chain of parents several levels long, with one link naming a RESEARCH record of the parent."),
        ("Q50", f"How many levels of ownership separate {name(deep)} from its ultimate parent?", {"count": "count"}, None,
         lambda: {"count": len(chain(deep))},
         "Paths: the length of the chain, counted across the RESEARCH record."),
        ("Q51", f"How many entities are in the {name(top[0])} group, the parent included?", {"count": "count"}, None,
         lambda: {"count": len(members(top[0]))},
         "Paths: every level of the tree, the QA record under the top left out, the RESEARCH record not counted twice."),
        ("Q52", f"How many entities are in the {name(top[2])} group, the parent included?", {"count": "count"}, None,
         lambda: {"count": len(members(top[2]))},
         "Paths and sources: a RESEARCH record names this top as a parent, but RATINGS holds for parent links."),
        ("Q53", f"Are {name(stale)} and {name(top[2])} in the same group?", {"same_group": "yesno"}, None,
         lambda: {"same_group": "yes" if ultimate_parent(stale) == canonical_id(top[2]) else "no"},
         "Sources: the stale parent from RESEARCH is overruled by the RATINGS record."),
        ("Q54", f"Which members of the {name(top[3])} group are domiciled in Valdoria (VD)?", {"entities": "entities"}, None,
         lambda: {"entities": [e for e in members(top[3]) if country(e) == "VD"]},
         "Paths and the domicile rule: one member is in VD by its RESEARCH record, which holds for country."),
        ("Q55", "If Valdoria (VD) came under stress, how many entities with an issuer rating in force have an entity domiciled in VD somewhere above them in their chain of parents?",
         {"count": "count"}, None, lambda: {"count": len(exposed)},
         "Exposure through ownership: walk up every chain, with domicile by the RESEARCH rule."),
        ("Q56", f"What is the lowest current foreign-currency issuer rating held by any member of the {name(top[4])} group?",
         {"rating": "rating"}, None, lambda: {"rating": lowest},
         "Paths and time: the whole tree, each member's latest action."),
        ("Q57", f"Which is the nearest entity that {name(pair[0])} and {name(pair[1])} both have in their chains of parents?",
         {"entity": "entity"}, None, lambda: {"entity": nearest_common(*pair)},
         "Paths: the nearest common ancestor, below the top of the group."),
        ("Q58", "Which entities guarantee a note issued by an entity outside their own group?", {"entities": "entities"}, None,
         lambda: {"entities": cross},
         "Paths and roles: guarantee links compared with ownership chains."),
        ("Q59", f"How many entities in the {name(top[0])} group sit exactly three levels below the top?", {"count": "count"}, None,
         lambda: {"count": sum(len(chain(e)) == 3 for e in members(top[0]))},
         "Paths: depth in the tree, across the RESEARCH record."),
        ("Q60", f"Whose credit risk does a holder of the {INSTRUMENTS[note]['description']} take, and is that entity in the same group as the issuer?",
         {"risk_of": "entity", "same_group": "yesno"}, None,
         lambda: {"risk_of": canonical_id(risk_of(note)),
                  "same_group": "yes" if ultimate_parent(risk_of(note)) == ultimate_parent(INSTRUMENTS[note]["issuer_id"]) else "no"},
         "Roles across groups: the guarantor belongs to another group."),
        ("Q61", f"How many members of the {name(top[0])} group, the top included, hold a foreign-currency issuer rating below investment grade?",
         {"count": "count"}, None,
         lambda: {"count": sum(fc(e) in SCALE and not investment_grade(fc(e)) for e in members(top[0]))},
         "Paths and test data: the QA record under the top has a B- rating, and is ignored."),
    ]


def main():
    scaled = FOLDER != HERE
    first = {q["id"]: q for q in json.loads((HERE / "questions.json").read_text())}
    out = []
    questions = list(Q)
    if (FOLDER / "anchors.json").exists():
        questions += path_questions(json.loads((FOLDER / "anchors.json").read_text()))
    for qid, text, fields, key, compute, tests in questions:
        got = compute()
        if scaled:
            key = got
        assert got == key, (qid, "by hand", key, "from the data", got)
        expected = (first[qid]["expected"] if qid in first and qid not in ("Q7", "Q9", "Q42", "Q43") and not scaled
                    else json.dumps(key))
        out.append({"id": qid, "question": text, "expected": expected, "tests": tests, "fields": fields, "key": key})
    for qid, (text, checklist, tests) in CHECKLIST.items():
        out.append({"id": qid, "question": text, "expected": first[qid]["expected"], "tests": tests,
                    "checklist": checklist})
    out.sort(key=lambda q: int(q["id"][1:]))
    (FOLDER / "questions.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(out)} questions" + (", keys computed from the data" if scaled else ", every typed key matches the data"))


if __name__ == "__main__":
    main()
