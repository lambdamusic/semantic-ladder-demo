Sonnet. The query runs used three repeats.

| | All 61 questions | The 13 path questions |
|---|---|---|
| Reading: `csv` | 81% | 77% |
| Reading: `csv+markdown` | 95% | 100% |
| Reading: `executed` | 94% | 97% |
| Reading: `csv+axioms` | 93% | 97% |
| SQL: `sql` | 73% | 44% |
| SQL: `sql+markdown` | 85% | 71% |
| SQL: `sql+executed` | 93% | 100% |
| SPARQL: `sparql` | 65% | 33% |
| SPARQL: `sparql+ontology` | 94% | 92% |
| SPARQL: `sparql+axioms` | 81% | 82% |

- **Without definitions, a graph doesn't help with paths.** Both stores score a third to a half on them. The chains run through a RESEARCH record, and a test record sits inside a group, and neither store says what those mean.
- **With definitions, both stores mostly get there.** SPARQL with the ontology is the steadiest querying condition, at 85–100% on the path questions in each session. The lower SQL and axioms averages each come from one bad session, one that stopped early and one that got empty results. With three repeats, one session moves a score by about 30 points.
- **Precomputed chains win.** With an `ancestors` table, SQL gets every path question right in every session. The graph's strength is following links of any depth at query time. Once rules have computed the chains, a table does as well.
- **Reading beats querying at this size.** With the definitions, reading the data gets all 13 right in all five sessions. Querying should pay off when the data is too big to read, which this isn't.
