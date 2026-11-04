An invented credit-ratings world: 19 entity records (two of them sovereigns), 8 instruments and the rating actions on them, as an analyst's extract would come. The codes (`LTIDR`, `AF`, `RWN`) are left cryptic, and nothing in the files says what they stand for.

The 48 questions are of two kinds:

- **Implicit meanings** (Q1 to Q40): what any credit analyst knows without saying. A rating holds from one action to the next. An outlook isn't a rating change. A withdrawal isn't a default. A Country Ceiling caps foreign-currency ratings. A guaranteed note carries the guarantor's risk. Two records with one LEI are one entity. A strong model gets many of these right from general knowledge.
- **Local meanings** (Q41 to Q48): rules this dataset sets for itself, stated only in the ontology. QA records are test data. Domicile comes from the RESEARCH system, and names and parents from RATINGS. `XVD` and `CVK` are local currency codes. `CO` is a credit opinion, not a rating. `EX` is an expected rating, not yet assigned. No model can know these without being told, which is where an ontology should earn its place.

**Version 2.** Since commit 18a2f42, domicile comes from RESEARCH. In version 1 the RATINGS record held for everything, and `csv` got those questions right in every run, because "RATINGS" sounds authoritative, so the rule could be guessed. Runs before that commit used version 1's keys, and each run's page grades it against its own.

**In this section:** the [data](/domains/credit/data/), the [questions and their traps](/domains/credit/questions/), the [ontology](/domains/credit/ontology/) with its diagram and axioms, and the [results](/domains/credit/results/).
