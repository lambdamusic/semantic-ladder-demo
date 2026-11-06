Reading, at ten times the base data ([Sonnet](/runs/research_850/2026-11-06-0206-sonnet/), [Haiku](/runs/research_850/2026-11-06-0206-haiku/)), five repeats. The prompts are 110 to 160 KB, against 19 to 39 KB for the base data. `rdf` and `rdf+ontology` are left out: as Turtle, the data alone is about 770 KB, too large for the model's context.

| Condition | Sonnet | Haiku | On the base data: Sonnet, Haiku |
|---|---|---|---|
| `csv` | 42% | 21% | 57%, 45% |
| `csv+padding` | 42% (+0) | 30% (+9) | 57%, 44% |
| `csv+markdown` | 87% (+45) | 43% (+22) | 98%, 99% |
| `csv+ontology` | 89% (+47) | 49% (+28) | 98%, 96% |
| `executed` | 79% (+37) | 69% (+48) | 90%, 92% |

- **For Sonnet, the definitions gain as much as on the base data,** +45 to +47 points, and the local rules stay right: 97% on Q33 to Q48 with the definitions, against 21% without. What drops is the general questions, from 97% to 82–85%. These are the counts and roll-ups over the whole data (Q9, Q10, Q11, Q14, Q16, Q19, Q21), which are now ten times longer to tally by reading. Q1 is the odd one: with the definitions, Sonnet answers that the three name forms stand for one person, where the records with those names carry three ORCIDs.
- **Haiku starts to give up.** In 5 of its 25 sessions it answers only some of the questions, sometimes saying so: "Q9–Q48: not yet answered… I'll continue". Four of the five are with the definitions, whose prompts are the largest. Counting only the sessions that answered everything, it scores 23% with `csv`, 58% with `csv+ontology` and 74% with `csv+markdown` (2 sessions).
- **Executed rules matter more as the data grows,** most of all for the weaker model. For Haiku, `executed` is now the best condition: the merging and rolling up are done, and its prompt is the smallest. For Sonnet it is 8 to 10 points short of the definitions, as on the base data.
- **The decoy glossary helps Haiku** by 9 points (+4 to +15). That's the first time it has helped either model, and it may be noise in a run where Haiku answers so unevenly.

Querying, at the same size ([Sonnet](/runs/research_850/2026-11-06-0519-sonnet-query/)), five repeats, against reading with the same model. The domain has no axioms yet, so no `sparql+axioms`.

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading | `csv` 42% | `csv+markdown` 87% | `executed` 79% |
| SQL | `sql` 38% | `sql+markdown` 80% | `sql+executed` 92% |
| SPARQL | `sparql` 30% | `sparql+ontology` 85% | |

- **Querying doesn't recover the counts by itself.** With the definitions, SQL and SPARQL score 80% and 85%, no better than reading. On the general questions they get 75% and 80%, against reading's 82–85%. The model writes the queries, but has to get every join and filter of each count right, and the definitions don't make that any easier.
- **Querying over executed tables is the best condition at this size:** 92%, in every session between 90% and 94%, against 79% when reading those same tables. The merging and roll-ups are done, and the model only has to count what the tables already hold.
- **The definitions are steady when reading, not when querying.** `sql+markdown` ranges from 41% to 97% across the five sessions, and `sparql+ontology` from 73% to 95%. In the weakest session, the model stopped after four rounds and answered from what it had seen.
- **SPARQL alone is the weakest condition again,** at 30%, 7 points below SQL (−13 to −2). Plain `sparql` used all eight rounds in every session.
- 34 of 643 queries failed, and 5 timed out on rdflib.
