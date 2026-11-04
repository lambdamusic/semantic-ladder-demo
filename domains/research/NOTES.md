# Research domain: notes

The second domain for Phase 4: research analytics shaped like OpenAlex (works, authors,
institutions, sources, authorships, citations). Same interface and files as
`domains/credit/`, plus `generate_data.py`, which writes the CSV files.

**Everything is invented:** the works, people, institutions, journals, ORCIDs, RORs, ISSNs and
DOIs. Nothing was downloaded from OpenAlex. The ORCIDs aren't checksummed, and the DOIs use
the prefix 10.55555 (I haven't checked that the prefix is unassigned).

## Rebuilding

```bash
python domains/research/generate_data.py      # data/*.csv (seeded, deterministic)
python domains/research/csv_to_rdf.py         # data/facts.ttl
python ontology_to_md.py research             # ontology.md
python domains/research/build_questions.py    # questions.json, checking every key against the data
python run.py --domain research --only csv rdf rdf+ontology csv+ontology csv+markdown csv+padding
```

`--only` is needed for now: see "Shared-file changes" below.

## What the data contains

| File | Rows | What |
|---|---|---|
| `institutions.csv` | 18 | 14 designed institutions in GB, DE, NL and FR (a system, universities, labs, an affiliated institute, a company, a government body), and 4 background ones in US, JP, CA and ES |
| `authors.csv` | 38 | 22 designed author records for 20 people (Mara Ellison under 3 records, one ORCID; a different "M. Ellison"; two Jonas Brandts; one record with no ORCID), and 16 background authors |
| `sources.csv` | 8 | journals in tiers K3, K2 and K1, a delisted (K0) journal, a repository, a proceedings journal, and 2 background journals |
| `works.csv` | 85 | 52 designed works (W01 to W92, with gaps), 8 designed background citers (W60 to W67) and 25 seeded background works (W101 to W125) |
| `authorships.csv` | 138 | one row per work, author and affiliation; `affil_seq` orders an author's affiliations on a work |
| `citations.csv` | 71 | citing work, cited work |

The background works are only noise. Their authors are at the four background institutions,
they appear in the two background journals, and they cite only each other. The exceptions
are W60 to W67, which cite W30, W31 and W42 for the citation-window questions. So no
background work changes a key.

The hierarchy: Tessel Laboratory (I04, LAB) sits under the Albury Centre for Marine Robotics
(I03, LAB), under the University of Albury (I02, UNI), under the Albury University System
(I01, SYS), which also holds Albury Metropolitan University (I05). Halloran Institute (I06, AFF)
has I02 as its parent but is not a unit of it. Kesting Institute of Hydrodynamics (I08, LAB)
sits under Kesting University (I07).

## The traps, and the questions that test each

48 questions: 46 typed (graded by code) and 2 checklists (Q47, Q48).

| Trap | Questions | How the data sets it |
|---|---|---|
| Who is who | Q1 to Q7 | A01, A02 and A03 are Mara Ellison (one ORCID); A04, also "M. Ellison", is someone else at Kesting; A05 and A06 are two Jonas Brandts. By record, Priya Ramanathan (A07, 4 works) beats each Mara record; merged, Mara has 5 (Q6). Q7 combines identity, versions, document types and the delisted source |
| Institution hierarchy | Q8 to Q11 (also Q38, Q44, Q46) | Ultimate parent three levels up (Q8); a university's count includes its labs (Q9); a system's count includes both universities, with W12 shared between them counted once (Q10) |
| Counting method | Q12 to Q14, Q47 | Kesting 2024: full 3, fractional 2. Rostval 2024: full 4, fractional 1 (four works, one author of four from Rostval on each), so the ranking flips (Q13). GB 2024: full 7, fractional 6. All fractional answers are whole numbers by design |
| Document types | Q15 to Q17 | Editorials (W04, W76), an erratum (W05), paratext (W09, W10) |
| Versions | Q18 to Q21 | W02 is the preprint of W03 and W42 of W31 (`version_of`); W18 is a preprint with no published version; W15 cites both W02 and W03 |
| Citation windows | Q22, Q23 | W30 (2019) has 5 citations in all but 1 within its year plus two; W31 (2023) has 4 in all, all within the window |
| Retractions | Q24 to Q26 | W23 (Lena Vossberg, Kesting) is retracted and cited once (W39) |
| Citations at several levels | Q27 to Q32 | Kesting is cited by three single-author Lorvain works and by one Rostval work with four Rostval authors (counted per author, Rostval would win: Q27, Q28). The sonar paper (W02/W03) is cited by 7 works: author self-citations 2, University of Albury 2, the system 3, GB 4 (Q29, Q30). Two hops from W01: W40 and W41, then W50, W51 and W52, with W51 citing both and a test record W90 left out (Q31, Q32) |
| Local rules | Q33 to Q46, Q48 | see below |

Q7, Q9, Q11, Q16 and Q25 also depend on local rules: they combine several traps, as the
credit domain's Q9 did.

## The local rules, and where the ontology states them

Each is stated only in the ontology, and none can be guessed from a code's name or from
general conventions.

| Rule | Where it's stated | Questions |
|---|---|---|
| **STG records are test data.** Works with `record_source` STG (W90 to W92, at Kesting, by A21) describe no real work: they're ignored, with their authorships and the citations they make. With them, W22 would be Kesting's most-cited work (4 citations against W20's 3) | `res:origin-STG`; `res:Work` (condition 1); `res:Citation` | Q33, Q34 (also Q11, Q16, Q25, Q31) |
| **SUP means supplement article, not supplementary material.** A peer-reviewed article in a supplement issue, counted like an article (W17, W24) | `res:wtype-SUP`; `res:Work` (condition 2) | Q34, Q35, Q36 |
| **Only the affiliation listed last counts.** When an author gives several affiliations on one work, only the one with the highest `affil_seq` is credited. W70 lists Tessel and then Halloran, so it goes to Halloran; W71 lists Halloran and then Tessel, so it goes to Tessel | `res:affiliationSeq` (also `res:Authorship`, `res:country`) | Q37, Q38, Q45 (also Q9, Q48) |
| **Journal tiers count upwards, and K0 is a delisting.** K3 is the highest tier and K1 the lowest, the reverse of the natural guess. Works in a K0 source (W07, W75) aren't research output | `res:tier`, `res:tier-K3` to `res:tier-K0`; `res:Work` (condition 4) | Q39, Q40, Q41 (tiers); Q42, Q43 (K0; also Q7) |
| **An affiliated institute (AFF) is not a unit of its parent.** Halloran's parent link records an agreement, so its works are never credited to the University of Albury or the system, and its ultimate parent is itself | `res:itype-AFF`; `res:Institution`; `res:parent` | Q44, Q45, Q46 (also Q9, Q48) |

## Things I wasn't sure about

- **"Research work" is the dataset's own term.** Most count questions ask for research works.
  Without the ontology, the model has to decide for itself what counts: that's the
  document-type trap. But it also means some `csv` answers that count editorials could be
  called a reasonable reading rather than an error. Credit's "issuer rating" was the same.
- **Author self-citation is defined broadly:** the citing and cited works share any author.
  So Q29's author count is 2 (Mara Ellison, and her co-author Priya Ramanathan, on W13). A
  model that counts only Mara's own citations says 1, which is a defensible reading without
  the ontology. Q29's institution count is also 2, by coincidence.
- **Citation windows** have only two questions, and each question states the window ("its
  publication year and the two years after"), so the trap is only raw counts against windowed
  ones. No question sets a house window length. That could be a sixth local rule.
- **Citations from any type of work count** (an editorial citing a paper is a citation), apart
  from test records and retracted works. No question depends on this choice.
- **Versions:** a merged pair takes the published version's year, source and byline. The
  build checks that each preprint's credited authors match its published version's.
  `canonical()` merges author records by ORCID only. It doesn't merge a preprint with its
  published version, because Q20 asks which records are preprints, and merging would accept
  the wrong record of the pair.
- **Field-normalised citations,** the plan's "normalisation" trap, aren't covered: the data has
  no fields, and the trap needs a decimal answer.
- **The names are invented, but could collide with real ones.** Some person names (Pieter Maas,
  Jonas Brandt) are common enough to belong to real people, and some place-based names
  (Albury, Dunmore) use real towns. Before publishing, check that no journal or institution
  name belongs to a real one.
- **Size:** the RDF is about 75 KB, against 19 KB for credit, because authorships and
  citations are one resource per row. So `rdf` and `rdf+ontology` are the largest prompts
  (82 KB and 100 KB, about 20,000 to 25,000 tokens). To shrink them, citations could become
  a direct `res:cites` triple, but the conversion would then no longer be strictly
  one-resource-per-row.

## Dry-run prompt sizes (`run.py --dry-run`)

| Condition | Bytes |
|---|---|
| `csv` | 20,780 |
| `csv+padding` | 31,851 |
| `csv+markdown` | 32,281 |
| `csv+ontology` | 38,967 |
| `rdf` | 82,085 |
| `rdf+ontology` | 100,193 |

`ontology.md` is 11,452 characters and `padding.md` 11,051 (3.5% shorter).

## Shared-file changes needed (not made, as asked)

1. **`run.py`: conditions per domain.** `CONDITIONS` includes `executed` and `csv+neutral`,
   which this domain doesn't have, so a run without `--only` stops at once, with a
   `ValueError` naming the conditions it does have. Suggestion: `domain.py` here defines
   `CONDITIONS`, and `run.py` could default to `getattr(domain, "CONDITIONS", CONDITIONS)`.
   The same applies to `--only`'s `choices`.
2. **`ontology_to_md.py`: column names.** It reads `conv.ENTITY_COLS`, `conv.INSTRUMENT_COLS`
   and `conv.ACTION_COLS`, which are the credit domain's tables, and catches only `ImportError`
   (a converter without these names would raise `AttributeError`). Here, `csv_to_rdf.py` defines
   its six tables' dicts and groups them onto those three names, so that no column name occurs
   twice with different properties in one group: three tables have a `type` column. Suggestion:
   a converter exposes `COLUMNS = [dict, ...]`, and `ontology_to_md.py` uses it when present.
3. **`ontology_to_md.py` drops `skos:definition` on a `skos:ConceptScheme`.** I moved the one
   sentence that was there (the tier order) onto the `res:tier` property, so the Markdown and
   the Turtle say the same thing.
4. **`grade.py`: a decimal kind** for fractional counts and field-normalised scores, such as
   `number`, normalised with `float()` and compared within a tolerance (`abs(got - want) <= 0.01`).
   Until then, every fractional answer here is a whole number.
5. **`README.md`** lists only `domains/credit/` in its layout table.
6. **Phase 2 (`query.py`)** loads `CSV_FILES` into DuckDB as tables named after the files
   (`works`, `authorships`, ...), so it should work here as it is. I haven't run it.
