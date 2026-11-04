"""A scaled copy of the credit domain: the base data plus N invented issuers that repeat its traps.

    python domains/credit/scale.py 300      # -> domains/credit_300/

The base records stay as they are, so every question still has its point. The added
issuers carry the same traps many times over: duplicate records from RESEARCH (some with a
different country, some holding the latest action), QA test records with actions of their
own, group chains, finance subsidiaries with guaranteed notes and credit opinions,
instruments in local currency, expected ratings, withdrawals, Watches, outlook changes, and
rows written out of date order. Seeded, so a size always gives the same data.

The keys are computed from the data by build_questions.py (none are written by hand at
scale), and execute.py writes the executed condition's tables.
"""
import csv
import hashlib
import os
import random
import shutil
import string
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SCALE = ["AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-", "BB+", "BB", "BB-", "B+", "B", "B-"]
CEILING = {"VD": "BB", "CV": "A"}
COUNTRIES = ["GB"] * 5 + ["DE"] * 3 + ["FR"] * 3 + ["NL"] * 2 + ["US"] * 3 + ["IT"] * 2 + ["ES"] * 2 + ["GR", "VD", "CV"]
SUFFIX = {"GB": "plc", "DE": "AG", "FR": "SA", "NL": "BV", "US": "Inc", "IT": "SpA", "ES": "SA", "GR": "SA",
          "VD": "SA", "CV": "SA"}
CURRENCY = {"GB": "GBP", "DE": "EUR", "FR": "EUR", "NL": "EUR", "US": "USD", "IT": "EUR", "ES": "EUR",
            "GR": "EUR", "VD": "XVD", "CV": "CVK"}
SECTORS = ["Energy", "Holdings", "Telecom", "Retail", "Shipping", "Foods", "Utilities", "Capital", "Industries",
           "Logistics", "Mining", "Pharma", "Media", "Airlines", "Chemicals", "Property", "Steel", "Water"]


def word(rng):
    return "".join(rng.choice(s) for s in ("BCDFGHKLMNPRSTVW", "aeiou", "lnrstv", "aeio", "nrdlm")).capitalize()


def lei(rng):
    return rng.choice(["5493", "2138", "9695", "8156", "3912", "7245"]) + "00" + \
        "".join(rng.choice(string.ascii_uppercase + string.digits) for _ in range(12)) + f"{rng.randrange(100):02d}"


def date(rng, start, end):
    y = rng.randint(start, end)
    return f"{y}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}"


def notch(r, by, cap=None):
    i = min(max(SCALE.index(r) + by, 0), len(SCALE) - 1)
    if cap:
        i = max(i, SCALE.index(cap))
    return SCALE[i]


def generate(n, seed):
    rng = random.Random(seed)
    entities, instruments, actions = [], [], []
    ids = {"E": 1000, "I": 1000, "A": 1000}

    def new(kind):
        ids[kind] += 1
        return f"{kind}{ids[kind]}"

    def act(rated, kind, basis, action, rating, outlook, watch, when, comment=""):
        actions.append([new("A"), when, rated, kind, basis, action, rating, outlook, watch, comment])

    def history(rated, basis, rating, cap, start):
        """An assignment, then up to three later actions, in date order (shuffled when written)."""
        act(rated, "LTIDR", basis, "AS", rating, "STA", "", start)
        when = start
        for _ in range(rng.choice([0, 1, 1, 2, 2, 3])):
            when = date(rng, int(when[:4]), 2026)
            if when > "2026-09-30" or when <= start:
                break
            move = rng.choice(["AF", "AF", "DG", "DG", "UG", "RW", "WD"])
            if move == "WD":
                act(rated, "LTIDR", basis, "WD", "WD", "", "", when, "commercial reasons")
                return
            if move == "RW":
                act(rated, "LTIDR", basis, "RW", rating, "", "RWN", when)
                continue
            if move in ("DG", "UG"):
                rating = notch(rating, 1 if move == "DG" else -1, cap)
            act(rated, "LTIDR", basis, move, rating, rng.choice(["STA", "STA", "NEG", "POS"]), "", when)

    issuers = []
    for _ in range(n):
        country = rng.choice(COUNTRIES)
        e = new("E")
        name = f"{word(rng)} {rng.choice(SECTORS)} {SUFFIX[country]}"
        etype = "BANK" if rng.random() < 0.2 else "CORP"
        parent = rng.choice(issuers)[0] if issuers and rng.random() < 0.12 else ""
        code = lei(rng)
        entities.append([e, name, code, country, etype, parent, "RATINGS"])
        issuers.append((e, country, code, name))
        cap = CEILING.get(country)
        fc = notch(rng.choice(SCALE[1:12]), 0, cap)
        start = date(rng, 2022, 2025)
        record = e
        if rng.random() < 0.10:  # a second record from RESEARCH, same LEI: sometimes another country, sometimes the latest action
            dup = new("E")
            other = rng.choice(COUNTRIES) if rng.random() < 0.3 else country
            entities.append([dup, name.upper().replace(" PLC", "").replace(" AG", ""), code, other, etype, "", "RESEARCH"])
            if rng.random() < 0.5:
                record = dup
        history(record, "FC", fc, cap, start)
        if cap and rng.random() < 0.7:
            history(e, "LC", notch(fc, -rng.randint(0, 2)), None, start)
        if rng.random() < 0.3:  # an instrument, rated from the issuer
            i = new("I")
            sub = rng.random() < 0.3
            ccy = CURRENCY[country] if rng.random() < 0.6 else rng.choice(["USD", "EUR"])
            instruments.append([i, f"{name.rsplit(' ', 1)[0]} {rng.randint(2, 8)}.{rng.choice(['00', '25', '50', '75'])}% notes due {rng.randint(2027, 2036)}",
                                e, "", "SUB" if sub else "SU", ccy, f"{rng.randint(2027, 2036)}-06-30"])
            if rng.random() < 0.1:
                act(i, "INST", "", "EX", notch(fc, 1 if sub else 0), "", "", date(rng, 2026, 2026))
            else:
                act(i, "INST", "", "AS", notch(fc, 1 if sub else 0), "", "", start)
    for _ in range(max(1, n // 20)):  # finance subsidiaries: no issuer rating, guaranteed notes, sometimes a credit opinion
        parent, country, _, pname = rng.choice(issuers)
        f = new("E")
        entities.append([f, f"{pname.rsplit(' ', 1)[0]} Finance {SUFFIX[rng.choice(['NL', 'GB', 'FR'])]}", lei(rng),
                         rng.choice(["NL", "GB", "FR"]), "FINSUB", parent, "RATINGS"])
        i = new("I")
        instruments.append([i, f"{pname.rsplit(' ', 1)[0]} Finance {rng.randint(2, 6)}.50% notes due {rng.randint(2027, 2034)}",
                            f, parent, "SU", "EUR", f"{rng.randint(2027, 2034)}-03-31"])
        act(i, "INST", "", "AS", rng.choice(SCALE[2:9]), "", "", date(rng, 2022, 2025))
        if rng.random() < 0.4:
            act(f, "CO", "", "AS", rng.choice(SCALE[3:10]), "", "", date(rng, 2024, 2026))
    for _ in range(max(1, n // 25)):  # QA test records, with actions that look real
        q = new("E")
        country = rng.choice(COUNTRIES[:12])
        entities.append([q, f"{word(rng)} {rng.choice(SECTORS)} {SUFFIX[country]}", lei(rng), country, "CORP", "", "QA"])
        r = rng.choice(SCALE[3:10])
        act(q, "LTIDR", "FC", "AS", r, "STA", "", date(rng, 2023, 2025))
        act(q, "LTIDR", "FC", "DG", notch(r, 1), "NEG", "", date(rng, 2026, 2026))
    rng.shuffle(actions)  # out of date order, as extracts often are
    return entities, instruments, actions


def build(n):
    target = HERE.parent / f"credit_{n}"
    shutil.rmtree(target, ignore_errors=True)
    (target / "data").mkdir(parents=True)
    for name in ["ontology.ttl", "ontology.md", "padding.md", "domain.py", "axioms.ttl"]:
        shutil.copy(HERE / name, target / name)
    entities, instruments, actions = generate(n, seed=int(hashlib.sha256(str(n).encode()).hexdigest()[:8], 16))
    for name, extra in [("entities.csv", entities), ("instruments.csv", instruments), ("rating_actions.csv", actions)]:
        with open(target / "data" / name, "w", newline="") as out:
            out.write((HERE / "data" / name).read_text())
            csv.writer(out, lineterminator="\n").writerows(extra)
    sys.path.insert(0, str(HERE))
    import csv_to_rdf
    csv_to_rdf.DATA = target / "data"
    csv_to_rdf.build().serialize(target / "data" / "facts.ttl", format="turtle")
    env = dict(os.environ, CREDIT_FOLDER=str(target))
    for script in ["build_questions.py", "execute.py"]:
        subprocess.run([sys.executable, str(HERE / script)], env=env, check=True)
    print(f"{target.name}: {len(entities)} entities, {len(instruments)} instruments, {len(actions)} actions added")


if __name__ == "__main__":
    for size in sys.argv[1:] or ["300"]:
        build(int(size))
