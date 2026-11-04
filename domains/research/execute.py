"""Apply the ontology's rules to the data, and write the result as tables: the `executed` condition.

    python domains/research/execute.py      # data/*.csv -> data/executed/*.csv

What a curated store would hold after its rules had run, with no definitions alongside:
- STG test records dropped, with their authorships and the citations they make;
- a preprint merged into its published version (record_ids lists both);
- each work flagged as research output or not (document type, retraction, delisted source);
- author records merged into people by ORCID;
- one credited institution per person and work: the affiliation listed last;
- each institution with every institution it counts towards (an affiliated institute counts only for itself);
- citations between merged works, from citing works that aren't retracted;
- journal tiers ranked, 1 the highest.

The rules are build_questions.py's, imported here, so the tables agree with the keys.
"""
import csv

import build_questions as b

OUT = b.DATA / "executed"
TABLES = ["works.csv", "people.csv", "credits.csv", "institutions.csv", "institution_units.csv",
          "sources.csv", "citations.csv"]
TIER_RANK = {"K3": 1, "K2": 2, "K1": 3}


def write(name, header, rows):
    with open(OUT / name, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def person_id(person):
    return b.record_of(person)


def main():
    OUT.mkdir(exist_ok=True)
    kept = sorted({b.identity(w) for w in b.WORKS if not b.test_record(w)}, key=lambda w: (len(w), w))
    works = []
    for w in kept:
        r = b.WORKS[w]
        works.append([w, r["title"], r["year"], r["type"], r["source_id"], r["is_retracted"],
                      "yes" if w in b.RESEARCH else "no", " ".join(sorted(b.records(w)))])
    write("works.csv", ["work_id", "title", "year", "type", "source_id", "retracted", "research_output", "record_ids"], works)

    people = {}
    for a, r in sorted(b.AUTHORS.items()):
        people.setdefault(b.PERSON[a], []).append(a)
    write("people.csv", ["person_id", "name", "orcid", "author_ids"],
          [[person_id(p), b.AUTHORS[person_id(p)]["name"], b.AUTHORS[person_id(p)]["orcid"], " ".join(ids)]
           for p, ids in sorted(people.items(), key=lambda x: person_id(x[0]))])

    write("credits.csv", ["work_id", "person_id", "institution_id"],
          [[w, person_id(p), i] for w in kept for p, i in sorted(b.credited(w).items(), key=lambda x: person_id(x[0]))])

    write("institutions.csv", ["institution_id", "name", "ror", "country", "type", "parent_id"],
          [[i, r["name"], r["ror"], r["country"], r["type"], r["parent_id"]] for i, r in b.INSTS.items()])
    write("institution_units.csv", ["institution_id", "counts_towards", "levels_up"],
          [[i, up, n] for i in b.INSTS for n, up in enumerate(b.chain(i))])
    write("sources.csv", ["source_id", "name", "issn", "type", "tier", "tier_rank", "delisted"],
          [[s, r["name"], r["issn"], r["type"], r["tier"], TIER_RANK.get(r["tier"], ""), "yes" if r["tier"] == "K0" else "no"]
           for s, r in b.SOURCES.items()])
    cites = sorted({(c, w) for w in kept for c in b.citers(w)}, key=lambda x: (len(x[0]), x))
    write("citations.csv", ["citing_work_id", "cited_work_id"], cites)
    print(f"{OUT}: {len(works)} works, {len(people)} people, {len(cites)} citations")


if __name__ == "__main__":
    main()
