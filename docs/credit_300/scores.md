Reading, every condition, on the version 2 rules ([Sonnet](/runs/credit_300/2026-11-05-2135-sonnet/), [Haiku](/runs/credit_300/2026-11-05-2135-haiku/)), five repeats:

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 81% | 74% |
| `rdf` | 77% (−4, −8 to −0) | 63% (−10, −17 to −4) |
| `csv+padding` | 81% (+0) | 69% (−4, −8 to −1) |
| `csv+markdown` | 93% (+12) | 87% (+13) |
| `csv+ontology` | 92% (+11) | 89% (+15) |
| `rdf+ontology` | 94% (+13) | 83% (+10) |
| `csv+neutral` | 95% (+14) | 88% (+15) |
| `csv+axioms` | 92% (+11) | 88% (+14) |
| `csv+axioms+markdown` | 94% (+12) | 85% (+11) |
| `executed` | 94% (+13) | 91% (+17) |

- **Definitions matter as much at scale:** +11 to +14 points for Sonnet and +10 to +17 for Haiku, in every form.
- **But size costs something even with them:** 92–95% for Sonnet and 83–91% for Haiku, against 96–100% for both on the base data. The misses are mostly long lists of 28 to 31 issuers (Q7, Q18, Q19), where an answer is wrong if it misses or adds a single one.
- **Raw RDF costs more at this size:** −4 for Sonnet and −10 for Haiku. The decoy glossary costs Haiku 4 points.
- **Q18's key is too narrow.** It counts a Rating Watch only on an issuer's foreign-currency rating. Two issuers here, E1019 and E1059, are on Watch Negative on their local-currency rating, and every session in every condition lists them, so Q18 is marked wrong throughout. The base data has no such case.

Querying, the six conditions, on the version 2 rules ([Sonnet](/runs/credit_300/2026-11-06-0041-sonnet-query/)), five repeats, against reading with the same model:

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading | `csv` 81% | `csv+markdown` 93% | `executed` 94% |
| SQL | `sql` 80% | `sql+markdown` 97% | `sql+executed` 97% |
| SPARQL | `sparql` 76% | `sparql+ontology` 95% | `sparql+axioms` 87% |

- **Definitions matter as much when querying:** +16 points with SQL and +19 with SPARQL, against +12 reading.
- **Querying beats reading a little, with the definitions:** 95–97% against 93%. The gain is on the long lists: with the definitions, 60% of them are entirely right when reading and 83% with SQL. Without the definitions, querying is no better than reading.
- **A graph store doesn't help with these questions:** SPARQL is 4 points below SQL without the definitions and 2 below with them. These questions need joins, not paths.
- **The rules run over the graph help less than the definitions:** `sparql+axioms` reaches 87%. It answers Q7, the 2026 downgrades, with an empty list in all five sessions.
- **Writing queries was rarely the problem:** 17 of 578 queries failed, and 3 timed out.
- One `sparql+axioms` session was refused by the API ("safeguards flagged this message") and asked again on resume.
