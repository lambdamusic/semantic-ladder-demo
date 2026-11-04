"""Apply the ontology's rules to the data, and write the result as tables: the `executed` condition.

    python domains/credit/execute.py      # data/*.csv -> data/executed/*.csv

What a curated graph would hold after its rules had run, with no definitions alongside:
- QA records and their actions dropped;
- records with the same LEI merged into one entity, with RATINGS winning where they disagree;
- each rating with the dates it held (valid_from to valid_to; blank valid_to means in force
  on 1 October 2026), with expected ratings and credit opinions left out, since neither is a rating;
- each instrument with whose credit risk it carries, and whether it pays in local currency;
- each country's ceiling.

The rules are the ones build_questions.py uses for the keys, written once and imported here.
In Phase 2 they become SQL views and SPARQL rules; this is the same logic as tables.
"""
import csv

import build_questions as b

OUT = b.DATA / "executed"


def canonical_id(record):
    return min(b.same(record))


def write(name, header, rows):
    with open(OUT / name, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main():
    OUT.mkdir(exist_ok=True)
    entities = []
    for e in sorted({canonical_id(i) for i in b.ENTITIES}, key=lambda i: (len(i), i)):
        records = sorted(b.same(e))
        ratings_record = next((r for r in records if b.ENTITIES[r]["source_system"] == "RATINGS"), records[0])
        row = b.ENTITIES[ratings_record]
        parent = row["parent_id"]
        top = b.ultimate_parent(e)
        entities.append([e, row["name"], row["lei"], b.country(e), row["entity_type"],
                         canonical_id(parent) if parent else "", canonical_id(top) if top != e else "",
                         " ".join(records)])
    write("entities.csv", ["entity_id", "name", "lei", "country", "entity_type", "parent_id",
                           "ultimate_parent_id", "record_ids"], entities)

    instruments = []
    for i, r in b.INSTRUMENTS.items():
        issuer = r["issuer_id"]
        local = "yes" if b.LOCAL.get(r["currency"], "") == b.country(issuer) else "no"
        instruments.append([i, r["description"], canonical_id(issuer),
                            canonical_id(r["guarantor_id"]) if r["guarantor_id"] else "",
                            canonical_id(b.risk_of(i)), r["seniority"], r["currency"], local, r["maturity"]])
    write("instruments.csv", ["instrument_id", "description", "issuer_id", "guarantor_id", "credit_risk_of",
                              "seniority", "currency", "local_currency", "maturity"], instruments)

    history, ceilings = [], []
    actions = [a for a in b.ACTIONS if a["rating_type"] != "CO"]
    for a in actions:
        thing = canonical_id(a["rated_id"]) if a["rated_id"] in b.ENTITIES else a["rated_id"]
        if a["rating_type"] == "CC":
            ceilings.append([b.ENTITIES[thing]["country"], a["rating"], a["date"]])
            continue
        same_line = [x for x in actions if x["rating_type"] == a["rating_type"] and x["ccy_basis"] == a["ccy_basis"]
                     and (canonical_id(x["rated_id"]) if x["rated_id"] in b.ENTITIES else x["rated_id"]) == thing]
        later = [x["date"] for x in same_line if x["date"] > a["date"]]
        history.append([thing, a["rating_type"], a["ccy_basis"], a["rating"], a["outlook"], a["watch"],
                        a["action"], a["date"], min(later) if later else "", a["action_id"]])
    history.sort(key=lambda h: (len(h[0]), h[0], h[1], h[2], h[7]))
    write("ratings.csv", ["rated_id", "rating_type", "ccy_basis", "rating", "outlook", "watch", "action",
                          "valid_from", "valid_to", "action_id"], history)
    write("ceilings.csv", ["country", "ceiling", "valid_from"], ceilings)
    print(f"{OUT}: {len(entities)} entities, {len(instruments)} instruments, "
          f"{len(history)} rating periods, {len(ceilings)} ceilings")


if __name__ == "__main__":
    main()
