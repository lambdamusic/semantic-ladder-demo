Sonnet, five repeats: reading ([run](/runs/credit_paths/2026-11-04-2022-sonnet/)), querying with SPARQL on rdflib ([run](/runs/credit_paths/2026-11-05-1515-sonnet-query/)), and the SPARQL conditions again on GraphDB ([run](/runs/credit_paths/2026-11-05-1819-sonnet-query-graphdb/)).

| | All 61 questions | The 13 path questions | Path score in each session |
|---|---|---|---|
| Reading: `csv` | 83% | 77% | 69, 85, 62, 85, 85 |
| Reading: `csv+markdown` | 96% | 100% | 100 in all five |
| Reading: `executed` | 95% | 97% | 92, 100, 92, 100, 100 |
| Reading: `csv+axioms` | 94% | 97% | 92, 100, 100, 92, 100 |
| SQL: `sql` | 75% | 60% | 38, 62, 62, 69, 69 |
| SQL: `sql+markdown` | 99% | 100% | 100 in all five |
| SQL: `sql+executed` | 97% | 100% | 100 in all five |
| SPARQL: `sparql` | 59% | 32% | 46, 62, 0, 31, 23 |
| SPARQL: `sparql+ontology` | 77% | 42% | 4, 8, 46, 77, 77 |
| SPARQL: `sparql+axioms` | 85% | 77% | 100, 100, 100, 8, 77 |
| SPARQL on GraphDB: `sparql` | 69% | 40% | 23, 38, 38, 38, 62 |
| SPARQL on GraphDB: `sparql+ontology` | 83% | 60% | 85, 85, 0, 100, 31 |
| SPARQL on GraphDB: `sparql+axioms` | 80% | 68% | 92, 0, 85, 92, 69 |

- **A graph store doesn't help with paths, with or without definitions.** Without them, SPARQL gets 32% of the path questions and SQL 60%. With them, SQL gets every path right in all five sessions, and SPARQL swings from 4% to 77%. The chains run through a RESEARCH record, and a test record sits inside a group, so neither store can be walked correctly without knowing what those records mean.
- **SPARQL is the less steady store here, and not because of the engine.** On rdflib, the model's large queries with the ontology were stopped after 60 seconds, up to three a session. On GraphDB, the same triples with no inference, no query timed out, and accuracy against rdflib went up 10 points without definitions and 6 with the ontology, but down 5 over the graph after the rules. Its poor sessions still happen: the model stops after three of its eight rounds, saying results were malformed when none were, or spends its rounds fetching whole classes of records, 60 rows at a time, and runs out before the path questions. With SQL, the same model asks for what each question needs, and no session fails that way.
- **Precomputed chains win.** With an `ancestors` table, SQL gets every path question right in every session, and so do three of the five sessions over the graph after the SHACL rules. Once rules have computed the chains, a table does as well as a graph.
- **Reading does as well at this size.** With the definitions, reading the 100 KB of CSV gets all 13 right in all five sessions, as SQL with the definitions does. Querying should pay off when the data is too big to read, which this isn't.

An earlier querying run with three repeats ([run](/runs/credit_paths/2026-11-04-2024-sonnet-query/)) had SPARQL with the ontology as the steadiest condition (92% on paths) and SQL with the definitions at 71%. With five repeats the order is reversed, which shows how much a single session moves these scores.
