"""Write questions.json: each question's key computed from the CSV files, and checked against the key written by hand.

    python domains/research/build_questions.py

Two answers for every typed key: the one written below by hand, and one computed by the
functions here from the data. The build stops if they differ, so a key can't silently
disagree with the data after an edit (to generate_data.py, then the CSV files).
"""
import csv
import json
import os
from collections import Counter
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).parent
# A scaled copy of the domain (scale.py) sets RESEARCH_FOLDER: its data is read and its
# questions written there, with keys computed from the data only, since none were written by hand.
FOLDER = Path(os.environ.get("RESEARCH_FOLDER", HERE))
DATA = FOLDER / "data"


def rows(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


WORKS = {w["work_id"]: w for w in rows("works.csv")}
INSTS = {i["institution_id"]: i for i in rows("institutions.csv")}
SOURCES = {s["source_id"]: s for s in rows("sources.csv")}
AUTHORS = {a["author_id"]: a for a in rows("authors.csv")}
AUTHORSHIPS = rows("authorships.csv")
CITES = [(c["citing_work_id"], c["cited_work_id"]) for c in rows("citations.csv")]
PERSON = {a: r["orcid"] or a for a, r in AUTHORS.items()}  # author record -> the person (ORCID)
RESEARCH_TYPES = {"ART", "REV", "SUP", "PPR"}  # SUP is a supplement article here (a local meaning)


# The rules the ontology states, applied here as the data's owner would.
def test_record(w):
    """Local rule: STG records are test data, and so is everything they say."""
    return WORKS[w]["record_source"] == "STG"


def is_research(w):
    r = WORKS[w]
    return (not test_record(w) and r["type"] in RESEARCH_TYPES and r["is_retracted"] == "false"
            and SOURCES[r["source_id"]]["tier"] != "K0")  # local rule: K0 sources are delisted


@cache  # the rules are pure; cached so a scaled copy builds in seconds
def identity(w):
    """A preprint with its published version in the data is that version."""
    v = WORKS[w]["version_of"]
    return v if v in WORKS else w


RESEARCH = {identity(w) for w in WORKS if is_research(w)}
assert all(is_research(w) for w in RESEARCH)


def year(w):
    return int(WORKS[w]["year"])


@cache
def records(work):
    return [w for w in WORKS if identity(w) == work]


@cache
def people(work):
    """The distinct people on any record of the work."""
    return {PERSON[a["author_id"]] for a in AUTHORSHIPS if a["work_id"] in records(work)}


@cache
def credited(work):
    """{person: the one institution credited for them}: local rule, the affiliation listed last.

    Read from the published version's record; the build checks a preprint's agrees."""
    best = {}
    for a in AUTHORSHIPS:
        if a["work_id"] == work:
            p, seq = PERSON[a["author_id"]], int(a["affil_seq"])
            if p not in best or seq > best[p][0]:
                best[p] = (seq, a["institution_id"])
    return {p: inst for p, (_, inst) in best.items()}


@cache
def chain(inst):
    """The institution and every one above it; an affiliated institute (AFF) is not a unit of its parent."""
    out = [inst]
    while INSTS[out[-1]]["type"] != "AFF" and INSTS[out[-1]]["parent_id"]:
        out.append(INSTS[out[-1]]["parent_id"])
    return out


def ultimate_parent(inst):
    return chain(inst)[-1]


@cache
def institutions_of(work):
    return {i for inst in credited(work).values() for i in chain(inst)}


@cache
def countries_of(work):
    return {INSTS[i]["country"] for i in credited(work).values()}


def works_of(inst=None, yr=None, person=None, country=None):
    return sorted(w for w in RESEARCH
                  if (inst is None or inst in institutions_of(w)) and (yr is None or year(w) == yr)
                  and (person is None or person in people(w)) and (country is None or country in countries_of(w)))


def fractional(inst=None, yr=None, country=None):
    total = Fraction(0)
    for w in works_of(yr=yr):
        shares = credited(w)
        total += Fraction(sum((inst is None or inst in chain(i)) and (country is None or INSTS[i]["country"] == country)
                              for i in shares.values()), len(shares))
    return total


def whole(x):
    assert x.denominator == 1, x
    return int(x)


@cache
def citers(work):
    """The distinct works citing either record of a work, test records and retracted works left out."""
    return sorted({identity(c) for c, d in CITES if identity(d) == work
                   and not test_record(c) and WORKS[c]["is_retracted"] == "false"})


def in_window(work, years):
    return [c for c in citers(work) if 0 <= year(c) - year(work) <= years]


def citations(work):
    return len(citers(work)) if work in RESEARCH else 0


def citing_works_by(inst, of):
    """Distinct works crediting inst that cite any of the works `of`: once per citing work."""
    return {c for w in of for c in citers(w) if inst in institutions_of(c)}


def record_of(person):
    return min(a for a in AUTHORS if PERSON[a] == person)


MARA, PRIYA, LENA, JONAS_GB = PERSON["A01"], PERSON["A07"], PERSON["A09"], PERSON["A05"]
SONAR = "W03"  # "Drift-aware mapping with low-cost sonar", with its preprint W02
KESTING = works_of("I07")


def top_author(inst):
    counts = Counter(p for w in works_of(inst) for p, i in credited(w).items() if inst in chain(i))
    (best, n), (_, second) = counts.most_common(2)
    assert n > second
    return record_of(best)


def self_citations(work, level):
    found = []
    for c in citers(work):
        if level == "author":
            same = people(c) & people(work)
        elif level == "country":
            same = countries_of(c) & countries_of(work)
        else:  # an institution: both credited to it, its units included
            same = level in institutions_of(c) and level in institutions_of(work)
        if same:
            found.append(c)
    return len(found)


def two_hops(work):
    first = set(citers(work))
    return sorted({c for f in first for c in citers(f)} - {work})


def yn(x):
    return "yes" if x else "no"


# id, question, fields, the key by hand, the key computed, what it tests, the expected answer in words
Q = [
    # Who is who
    ("Q1", 'How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?',
     {"count": "count"}, {"count": 2},
     lambda: {"count": len({PERSON[a] for a, r in AUTHORS.items() if r["name"] in ("Mara Ellison", "M. Ellison", "Ellison, Mara J.")})},
     "Identity: A01, A02 and A03 share an ORCID; A04, also 'M. Ellison', has another.",
     "Two: Mara Ellison (A01, A02, A03, one ORCID) and a different M. Ellison (A04, at Kesting University, another ORCID)."),
    ("Q2", "List every work, of any type, that Mara Ellison (A01) is an author of.", {"works": "entities"},
     {"works": ["W01", "W02", "W03", "W04", "W05", "W06", "W07", "W12", "W19"]},
     lambda: {"works": sorted({a["work_id"] for a in AUTHORSHIPS if PERSON[a["author_id"]] == MARA})},
     "Identity: her works are spread over three author records, and A04's works (W08, W16) are not hers.",
     "W01, W04, W05, W06, W12 (as A01), W02, W07, W19 (as A02) and W03 (as A03); not W08 or W16, by A04, a different M. Ellison."),
    ("Q3", "Is the Jonas Brandt who wrote W37 the same person as the Jonas Brandt who wrote W38?", {"same": "yesno"},
     {"same": "no"}, lambda: {"same": yn(PERSON["A05"] == PERSON["A06"])},
     "Identity: the same name, different ORCIDs.",
     "No. A05 (Albury Metropolitan University) and A06 (Université de Lorvain) have different ORCIDs."),
    ("Q4", "How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?", {"count": "count"},
     {"count": 2}, lambda: {"count": len(works_of(person=JONAS_GB))},
     "Identity: the other Jonas Brandt's works (W28, W34, W38) are not his.",
     "Two: W14 and W37."),
    ("Q5", "Is the M. Ellison who wrote W08 the same person as the Mara Ellison who wrote W01?", {"same": "yesno"},
     {"same": "no"}, lambda: {"same": yn(PERSON["A04"] == PERSON["A01"])},
     "Identity: a name variant shared with a different person.",
     "No. W08's author is A04, whose ORCID differs from Mara Ellison's (A01, A02, A03)."),
    ("Q6", "Which author has the most research works credited to the University of Albury, its units included?",
     {"author": "entity"}, {"author": "A01"}, lambda: {"author": top_author("I02")},
     "Identity: Mara Ellison's five works are split over three records; by record, Priya Ramanathan (four) would come first.",
     "Mara Ellison (A01 = A02 = A03): W01, W03, W06, W12 and W19. Priya Ramanathan (A07) has four."),
    ("Q7", "How many research works has Mara Ellison authored?", {"count": "count"},
     {"count": 5}, lambda: {"count": len(works_of(person=MARA))},
     "Everything at once: identity, versions (W02 is W03), document types (W04, W05) and the delisted source (W07).",
     "Five: W01, W03 (with its preprint W02), W06, W12 and W19. W04 is an editorial, W05 an erratum, and W07 appeared in a delisted (K0) source."),

    # Institution hierarchy
    ("Q8", "What is the ultimate parent of the Tessel Laboratory for Ocean Sensing (I04)?", {"parent": "entity"},
     {"parent": "I01"}, lambda: {"parent": ultimate_parent("I04")},
     "Hierarchy: three levels up, lab to centre to university to system.",
     "The Albury University System (I01): I04 is under I03, under I02, under I01."),
    ("Q9", "How many research works is the University of Albury (I02) credited with, its units included?", {"count": "count"},
     {"count": 8}, lambda: {"count": len(works_of("I02"))},
     "Hierarchy: the labs' works count, each work once; also versions, types, the affiliation rule and the affiliated institute.",
     "Eight: W01, W03, W06, W12, W13, W19, W71 and W72."),
    ("Q10", "How many research works is the Albury University System (I01) credited with, all its units included?", {"count": "count"},
     {"count": 12}, lambda: {"count": len(works_of("I01"))},
     "Hierarchy: both universities and their labs, a work shared between them (W12) counted once.",
     "Twelve: the University of Albury's eight, plus W14, W28, W29 and W37 from Albury Metropolitan University."),
    ("Q11", "How many research works is Kesting University (I07) credited with, its units included?", {"count": "count"},
     {"count": 6}, lambda: {"count": len(KESTING)},
     "Hierarchy with retraction and test records: the institute's W24 counts; W23 (retracted) and W90 to W92 (STG) don't.",
     "Six: W08, W16, W20, W21, W22 and W24."),

    # Counting method
    ("Q12", "How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?",
     {"full": "count", "fractional": "count"}, {"full": 3, "fractional": 2},
     lambda: {"full": len(works_of("I07", 2024)), "fractional": whole(fractional("I07", 2024))},
     "Counting method: W20 is half Kesting's, W21 two quarters, W22 whole.",
     "Full: 3 (W20, W21, W22). Fractional: 1/2 + 2/4 + 1 = 2."),
    ("Q13", "In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?",
     {"full": "entity", "fractional": "entity"}, {"full": "I09", "fractional": "I07"},
     lambda: {"full": max(["I07", "I09"], key=lambda i: len(works_of(i, 2024))),
              "fractional": max(["I07", "I09"], key=lambda i: fractional(i, 2024))},
     "Counting method: the ranking flips.",
     "Full: Rostval, 4 to 3. Fractional: Kesting, 2 to 1, since each of Rostval's four works has four authors and only one of them from Rostval."),
    ("Q14", "How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?",
     {"full": "count", "fractional": "count"}, {"full": 7, "fractional": 6},
     lambda: {"full": len(works_of(country="GB", yr=2024)), "fractional": whole(fractional(country="GB", yr=2024))},
     "Counting method at country level.",
     "Full: 7 (W06, W12, W13, W28, W29, W71, W72). Fractional: five whole works plus half of W28 and half of W29 = 6."),

    # Document types
    ("Q15", "How many research works appeared in Ocean Sensing Letters (S02) in 2024?", {"count": "count"},
     {"count": 4}, lambda: {"count": sum(WORKS[w]["source_id"] == "S02" for w in works_of(yr=2024))},
     "Document types: the erratum W05 and the front matter W10 are not research output.",
     "Four: W12, W21, W28 and W51."),
    ("Q16", "How many research works appeared in the Journal of Marine Autonomy (S01)?", {"count": "count"},
     {"count": 10}, lambda: {"count": sum(WORKS[w]["source_id"] == "S01" for w in RESEARCH)},
     "Document types: an editorial (W04) and paratext (W09) are not research output; also a test record (W91).",
     "Ten: W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74."),
    ("Q17", "Which of Mara Ellison's works are not research output because of their document type?", {"works": "entities"},
     {"works": ["W04", "W05"]},
     lambda: {"works": sorted(a["work_id"] for a in AUTHORSHIPS if PERSON[a["author_id"]] == MARA
                              and WORKS[a["work_id"]]["type"] not in RESEARCH_TYPES)},
     "Document types: an editorial and an erratum, under two author records.",
     "W04, an editorial, and W05, an erratum."),

    # Versions
    ("Q18", "How many distinct research works has Priya Ramanathan (A07) authored?", {"count": "count"},
     {"count": 4}, lambda: {"count": len(works_of(person=PRIYA))},
     "Versions: W02 is the preprint of W03; also the erratum W05 is not a work of research.",
     "Four: W01, W03 (with its preprint W02), W13 and W72."),
    ("Q19", 'How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?', {"count": "count"},
     {"count": 7}, lambda: {"count": len(citers(SONAR))},
     "Versions: citations to the preprint W02 and to W03 are citations of one work; W15 cites both and counts once.",
     "Seven: W12, W13, W14, W15, W16, W17 and W18."),
    ("Q20", "Which works in the data are preprints of another work that is also in the data?", {"works": "entities"},
     {"works": ["W02", "W42"]}, lambda: {"works": sorted(w for w in WORKS if identity(w) != w)},
     "Versions: a shared title is the clue, version_of the evidence; W18 is a preprint with no published version.",
     "W02 (of W03) and W42 (of W31)."),
    ("Q21", "How many research works is Oskel Polytechnic (I14) credited with?", {"count": "count"},
     {"count": 4}, lambda: {"count": len(works_of("I14"))},
     "Versions: W42 is the preprint of W31.",
     "Four: W27, W31 (with its preprint W42), W39 and W50."),

    # Citation windows
    ("Q22", "Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?",
     {"more_in_total": "entity", "more_in_window": "entity"}, {"more_in_total": "W30", "more_in_window": "W31"},
     lambda: {"more_in_total": max(["W30", "W31"], key=lambda w: len(citers(w))),
              "more_in_window": max(["W30", "W31"], key=lambda w: len(in_window(w, 2)))},
     "Citation windows: the older work has had more time; over the same span the newer one leads.",
     "In total W30 (5 to 4). Within three years W31 (4, from 2023 to 2025, one of them citing its preprint W42) against W30's 1 (2019 to 2021)."),
    ("Q23", "How many citations has W30 received in total, and how many within its publication year and the two years after?",
     {"total": "count", "in_window": "count"}, {"total": 5, "in_window": 1},
     lambda: {"total": len(citers("W30")), "in_window": len(in_window("W30", 2))},
     "Citation windows: a citation's year is the citing work's year.",
     "Five in total (W60 to W64); one, W60 (2020), within 2019 to 2021."),

    # Retractions
    ("Q24", "How many research works has Lena Vossberg (A09) authored?", {"count": "count"},
     {"count": 3}, lambda: {"count": len(works_of(person=LENA))},
     "Retractions: W23 is retracted.",
     "Three: W20, W21 and W22. W23 was retracted."),
    ("Q25", "What is the total of the citation counts of Lena Vossberg's research works?", {"count": "count"},
     {"count": 6}, lambda: {"count": sum(citations(w) for w in works_of(person=LENA))},
     "Retractions and test records: W23's citation (W39) doesn't count, nor do the STG works citing W22.",
     "Six: W20 three, W21 two, W22 one."),
    ("Q26", "Does W23 count towards Kesting University's research output?", {"counts": "yesno"},
     {"counts": "no"}, lambda: {"counts": yn("W23" in KESTING)},
     "Retractions: a retracted work is not research output.",
     "No: it has been retracted."),

    # Citations at several levels
    ("Q27", "Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?",
     {"institution": "entity", "citing_works": "count"}, {"institution": "I12", "citing_works": 3},
     lambda: (lambda best: {"institution": best, "citing_works": len(citing_works_by(best, KESTING))})(
         max((i for i in INSTS if i not in chain("I07") and i != "I08"), key=lambda i: len(citing_works_by(i, KESTING)))),
     "Citations rolled up: Rostval's one citing work has four Rostval authors; counted per author it would win.",
     "Université de Lorvain (I12), with three works (W33, W34, W35). Rostval has one work (W32) with four authors, Brevin one (W36) citing two Kesting works."),
    ("Q28", "How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?", {"count": "count"},
     {"count": 1}, lambda: {"count": len(citing_works_by("I09", KESTING))},
     "Citations rolled up: a work counts once, not once per author.",
     "One: W32, which has four authors from Rostval."),
    ("Q29", 'Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?',
     {"author": "count", "institution": "count", "country": "count"}, {"author": 2, "institution": 2, "country": 4},
     lambda: {"author": self_citations(SONAR, "author"), "institution": self_citations(SONAR, "I02"),
              "country": self_citations(SONAR, "country")},
     "Self-citation depends on the level; W12 is Mara Ellison under another record, W13 her co-author; W16 is the other M. Ellison.",
     "Author: 2 (W12 by Mara Ellison, W13 by her co-author Priya Ramanathan). University of Albury: 2 (the same). GB: 4 (also W14 and W15)."),
    ("Q30", 'Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?',
     {"count": "count"}, {"count": 3}, lambda: {"count": self_citations(SONAR, "I01")},
     "Self-citation at a level between institution and country.",
     "Three: W12, W13 and W14 (Albury Metropolitan University, in the same system)."),
    ("Q31", "Which works cite at least one of the works that cite W01?", {"works": "entities"},
     {"works": ["W50", "W51", "W52"]}, lambda: {"works": two_hops("W01")},
     "Two hops; W51 cites both first-hop works; W90 is a test record.",
     "W50, W51 and W52 (citing W40 or W41, which cite W01). W90 also cites W41, but it is a test record."),
    ("Q32", "How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?", {"count": "count"},
     {"count": 5}, lambda: {"count": len(set(citers("W01")) | set(two_hops("W01")))},
     "Two hops, counted once each.",
     "Five: W40 and W41, then W50, W51 and W52."),

    # Local rules, stated only in the ontology
    ("Q33", "Which of Kesting University's research works has the most citations?", {"work": "entity"},
     {"work": "W20"}, lambda: {"work": max(KESTING, key=citations)},
     "Local rule: STG records are test data; with them W22 would lead.",
     "W20, with three (W32, W35, W36). W22 has one real citation; the other three are STG test records."),
    ("Q34", "How many research works was Kesting University (units included) credited with in 2025?", {"count": "count"},
     {"count": 3}, lambda: {"count": len(works_of("I07", 2025))},
     "Local rules: STG records are test data; SUP is a research article.",
     "Three: W08, W16 and W24 (a supplement article). W90 to W92 are test records."),
    ("Q35", "How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?", {"count": "count"},
     {"count": 2}, lambda: {"count": len(works_of("I08"))},
     "Local code: SUP is a supplement article, research output, not supplementary material.",
     "Two: W21 and W24 (SUP, a supplement article)."),
    ("Q36", "How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?", {"count": "count"},
     {"count": 2}, lambda: {"count": sum(WORKS[w]["source_id"] == "S06" for w in RESEARCH)},
     "Local code: both SUP works count; the foreword (EDT) doesn't.",
     "Two: W17 and W24, both supplement articles. W76 is an editorial."),
    ("Q37", "Which institution is W70 credited to?", {"institution": "entity"},
     {"institution": "I06"}, lambda: {"institution": credited("W70")[PERSON["A08"]]},
     "Local rule: only the affiliation listed last counts.",
     "The Halloran Institute for Coastal Studies (I06), listed second, after the Tessel Laboratory."),
    ("Q38", "Which institutions is W71 credited to, at every level?", {"institutions": "entities"},
     {"institutions": ["I01", "I02", "I03", "I04"]}, lambda: {"institutions": sorted(institutions_of("W71"))},
     "Local rule on affiliations, then the hierarchy: the Tessel Laboratory is listed last, so Halloran gets nothing.",
     "The Tessel Laboratory (I04) and the institutions above it: I03, I02 and I01. Not Halloran (I06), listed first."),
    ("Q39", "How many of the University of Albury's research works (units included) appeared in a source of the highest tier?",
     {"count": "count"}, {"count": 3},
     lambda: {"count": sum(SOURCES[WORKS[w]["source_id"]]["tier"] == "K3" for w in works_of("I02"))},
     "Local code: the tiers count upwards, K3 the highest.",
     "Three, in the Journal of Marine Autonomy (K3): W01, W13 and W71."),
    ("Q40", "Which source is in the highest tier?", {"source": "entity"},
     {"source": "S01"}, lambda: {"source": next(s for s, r in SOURCES.items() if r["tier"] == "K3")},
     "Local code: K3 is the highest tier, not K1.",
     "The Journal of Marine Autonomy (S01), tier K3."),
    ("Q41", "Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?", {"higher": "yesno"},
     {"higher": "no"}, lambda: {"higher": yn(SOURCES["S03"]["tier"] > SOURCES["S02"]["tier"])},
     "Local code: K1 is below K2.",
     "No: S03 is K1, the lowest tier; S02 is K2."),
    ("Q42", "How many research works appeared in Global Marine Science Reports (S04)?", {"count": "count"},
     {"count": 0}, lambda: {"count": sum(WORKS[w]["source_id"] == "S04" for w in RESEARCH)},
     "Local code: K0 is a delisted source, whose works are not research output.",
     "None: S04 is delisted (K0), so W07 and W75 don't count."),
    ("Q43", "Is W07 research output?", {"research": "yesno"},
     {"research": "no"}, lambda: {"research": yn("W07" in RESEARCH)},
     "Local code: an article in a delisted source.",
     "No: it is an article, but it appeared in Global Marine Science Reports, a delisted (K0) source."),
    ("Q44", "Which institutions are part of the Albury University System, at any level below it?", {"institutions": "entities"},
     {"institutions": ["I02", "I03", "I04", "I05"]}, lambda: {"institutions": sorted(i for i in INSTS if i != "I01" and "I01" in chain(i))},
     "Local type: an affiliated institute (AFF) is not a unit of its parent.",
     "I02, I03, I04 and I05. The Halloran Institute (I06) is an affiliated institute, not a unit."),
    ("Q45", "How many research works is the Halloran Institute for Coastal Studies (I06) credited with?", {"count": "count"},
     {"count": 3}, lambda: {"count": len(works_of("I06"))},
     "Local rule on affiliations: W71 lists Halloran first, so it goes to the Tessel Laboratory.",
     "Three: W70, W73 and W74."),
    ("Q46", "What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?", {"parent": "entity"},
     {"parent": "I06"}, lambda: {"parent": ultimate_parent("I06")},
     "Local type: an affiliated institute's parent link is an agreement, not membership.",
     "Itself (I06): as an affiliated institute it is not a unit of the University of Albury."),
]

# Answered in prose and graded by an LLM against a checklist.
CHECKLIST = {
    "Q47": ("Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?",
            ["Says each of Rostval's four 2024 works has four authors with only one from Rostval, so a quarter each",
             "Says Kesting holds larger shares: a single-author review (W22) and half of W20 and W21"],
            "Counting method: why the ranking flips.",
            "Rostval is on four 2024 works (W21, W27, W28, W29), but on each it has one author of four: 4 x 1/4 = 1. "
            "Kesting is on three, with larger shares: W22 alone, half of W20, two of the four authors of W21: 2."),
    "Q48": ("Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?",
            ["Says only the affiliation listed last counts, so W70 is credited to the Halloran Institute",
             "Says the Halloran Institute is an affiliated institute, not a unit, so its works don't roll up to the University of Albury"],
            "Local rules: the last-listed affiliation, and affiliated institutes.",
            "Tomasz Wierzba lists the Tessel Laboratory first and the Halloran Institute second; the house rule credits "
            "the last-listed one, Halloran. Halloran is an affiliated institute (AFF): its parent link is an agreement, "
            "so its works are not the University of Albury's."),
}


def scaled_q47():
    """Q47's checklist and expected answer for a scaled copy: the same question, the numbers read from the data."""
    def side(inst):
        shares = {w: Fraction(sum(inst in chain(i) for i in credited(w).values()), len(credited(w)))
                  for w in works_of(inst, 2024)}
        return len(shares), sum(shares.values()), sum(s <= Fraction(1, 4) for s in shares.values()), sum(s == 1 for s in shares.values())
    nr, fr, small, _ = side("I09")
    nk, fk, _, alone = side("I07")
    checklist = ["Says most of Rostval's 2024 works have several authors with only one from Rostval, so it gets a small share of each",
                 "Says Kesting holds larger shares of its 2024 works: many by Kesting authors alone, or with few co-authors"]
    expected = (f"Rostval is on {nr} works in 2024, but on {'every one' if small == nr else small} of them it has at most a quarter of the authors, "
                f"so its shares add up to {fr}. Kesting is on {nk}, {alone} of them by Kesting authors alone, "
                f"so its shares add up to {fk}.")
    return checklist, expected


def main():
    scaled = FOLDER != HERE
    # The preprints' bylines agree with their published versions', so reading credit from the latter is safe.
    for w in WORKS:
        if identity(w) != w:
            assert credited(w) == credited(identity(w)), w
    out = []
    for qid, text, fields, key, compute, tests, expected in Q:
        got = compute()
        if scaled:
            key, expected = got, json.dumps(got)
        assert got == key, (qid, "by hand", key, "from the data", got)
        out.append({"id": qid, "question": text, "expected": expected, "tests": tests, "fields": fields, "key": key})
    for qid, (text, checklist, tests, expected) in CHECKLIST.items():
        if scaled and qid == "Q47":
            checklist, expected = scaled_q47()
        out.append({"id": qid, "question": text, "expected": expected, "tests": tests, "checklist": checklist})
    out.sort(key=lambda q: int(q["id"][1:]))
    (FOLDER / "questions.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(out)} questions" + (", keys computed from the data" if scaled else ", every typed key matches the data"))


if __name__ == "__main__":
    main()
