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

The querying runs here were made on the version 1 rules, before this dataset was rebuilt, and are in the [run archive](/runs/). There, with Sonnet, SQL scored 86% without the definitions and 96% with them, and SPARQL 79% and 95%. A querying run on version 2 is under way.
