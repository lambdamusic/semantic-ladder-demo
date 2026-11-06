Reading, every condition, on the version 2 rules ([Sonnet](/runs/credit_300/2026-11-05-2135-sonnet/), [Haiku](/runs/credit_300/2026-11-05-2135-haiku/)), five repeats:

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 83% | 74% |
| `rdf` | 79% (−4, −8 to −0) | 64% (−10, −17 to −3) |
| `csv+padding` | 83% (+0) | 69% (−4, −8 to −1) |
| `csv+markdown` | 95% (+12) | 88% (+14) |
| `csv+ontology` | 95% (+12) | 89% (+15) |
| `rdf+ontology` | 96% (+13) | 84% (+10) |
| `csv+neutral` | 97% (+14) | 88% (+15) |
| `csv+axioms` | 94% (+11) | 89% (+15) |
| `csv+axioms+markdown` | 95% (+12) | 85% (+11) |
| `executed` | 95% (+12) | 93% (+19) |

- **Definitions matter as much at scale:** +11 to +14 points for Sonnet and +10 to +19 for Haiku, in every form.
- **Size costs Haiku more than Sonnet:** with the definitions, Sonnet reaches 94–97% and Haiku 84–93%, against 96–100% for both on the base data. The misses are mostly long lists of 28 to 32 issuers (Q7, Q18, Q19), where an answer is wrong if it misses or adds a single one.
- **Raw RDF costs more at this size:** −4 for Sonnet and −10 for Haiku. The decoy glossary costs Haiku 4 points.
- **Q18 counts a Watch on either currency.** Its key first counted only Watches on the foreign-currency rating, and missed two issuers here (E1019 and E1059) on Watch Negative on their local-currency rating. The key was fixed and the runs regraded. The base data has no such case.

Querying, the six conditions, on the version 2 rules ([Sonnet](/runs/credit_300/2026-11-06-0041-sonnet-query/)), five repeats, against reading with the same model:

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading | `csv` 83% | `csv+markdown` 95% | `executed` 95% |
| SQL | `sql` 80% | `sql+markdown` 99% | `sql+executed` 99% |
| SPARQL | `sparql` 77% | `sparql+ontology` 97% | `sparql+axioms` 88% |

- **Definitions matter as much when querying:** +19 points with SQL and +20 with SPARQL, against +12 reading.
- **Querying beats reading a little, with the definitions:** 97–99% against 95%. The gain is on the long lists, which SQL gets entirely right more often than reading does. Without the definitions, querying is no better than reading.
- **A graph store doesn't help with these questions:** SPARQL is 3 points below SQL without the definitions and 2 below with them. These questions need joins, not paths.
- **The rules run over the graph help less than the definitions:** `sparql+axioms` reaches 88%. It answers Q7, the 2026 downgrades, with an empty list in all five sessions.
- **Writing queries was rarely the problem:** 17 of 578 queries failed, and 3 timed out.
- One `sparql+axioms` session was refused by the API ("safeguards flagged this message") and asked again on resume.
