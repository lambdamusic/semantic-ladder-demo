An invented credit-ratings world: issuers, the bonds they issue, and the rating actions on both, as an analyst's extract from two internal systems would come. The codes (`LTIDR`, `AF`, `RWN`) are left cryptic, and nothing in the files says what they stand for.

The 48 questions are of two kinds:

- **Implicit meanings** (Q1 to Q40): what any credit analyst knows without saying. A rating holds from one action to the next. An outlook isn't a rating change. A withdrawal isn't a default. A Country Ceiling caps foreign-currency ratings. A guaranteed note carries the guarantor's risk. Two records with one LEI are one entity. A strong model gets many of these right from general knowledge.
- **Local meanings** (Q41 to Q48): rules this dataset sets for itself, stated only in the ontology. QA records are test data. Domicile comes from the RESEARCH system, and names and parents from RATINGS. `XVD` and `CVK` are local currency codes. `CO` is a credit opinion, not a rating. `EX` is an expected rating, not yet assigned. No model can know these without being told, which is where an ontology should earn its place.

One ontology and one question bank are asked of three datasets. Each dataset computes its own answer keys from its own data.

## The datasets

### The base data

19 entity records (two of them sovereigns), 8 instruments and 47 rating actions, every one designed by hand so that each question has its point. Small enough to read in full, it's where the ladder was first tested.

### At 300 issuers

The base records plus 300 invented issuers that repeat the same traps many times over: duplicate RESEARCH records, QA test records, group chains, finance subsidiaries, local currencies, expected ratings, withdrawals, Watches, and rows out of date order. That makes 370 entity records, 115 instruments and 787 rating actions. The same 48 questions now need counting and joining across many records, which is where reading the data should start to fail and writing queries should pay off. `scale.py` builds it from a fixed seed.

This dataset still uses the domain's version 1 rules, where the RATINGS record holds for every field (see the [ontology](/domains/credit/ontology/)).

### Ownership paths

Does the store need to be a graph? With one or two levels of parent, the data can't show a graph's strength. This dataset is the 300-issuer data, on the current rules, plus six invented groups four to six levels deep, built so that answering means walking parent and guarantee links:

- in the largest group, a parent link names a **RESEARCH record** of the parent, so the chain goes on from that entity's RATINGS record;
- a RESEARCH record gives a **stale parent** in another group, which the RATINGS record overrules;
- a member is **in Valdoria by its RESEARCH record**, which holds for country, while RATINGS puts it in the Netherlands;
- a note is **guaranteed by another group's top entity**;
- a **QA test record** sits under one group's top, with a rating of its own.

It asks the 48 questions plus 13 that follow links (Q49 to Q61). `paths.py` builds it, and the designed entities' IDs go in `anchors.json`.

## Version 2

Since commit 18a2f42, domicile comes from RESEARCH. In version 1 the RATINGS record held for everything, and `csv` got those questions right in every run, because "RATINGS" sounds authoritative, so the rule could be guessed. Runs before that commit used version 1's keys, and each run's page grades it against its own.
