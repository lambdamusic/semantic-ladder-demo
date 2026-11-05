The runs below were made on the version 1 rules, where the RATINGS record held for every field, before this dataset was rebuilt on version 2. Their keys differ in Q42 and Q43, and each is graded against its own. Runs on version 2 will replace them in the table.

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading | `csv` 80% | `csv+markdown` 95% | `executed` 95% |
| SQL | `sql` 86% | `sql+markdown` 96% | |
| SPARQL | `sparql` 79% | `sparql+ontology` 95% | |

- **Definitions matter as much at scale:** +15 points reading, +10 with SQL, +16 with SPARQL.
- **Querying beats reading only a little:** +6 points without definitions and +1 with them.
- **A graph store doesn't help with these questions:** SPARQL without definitions is 7 points below SQL, and with them the two tie. These questions need joins, not paths.
- **Long lists are nearly right:** strict list accuracy is 51–86%, but mean F1 is 92–100%. The misses are an item or two, and querying cuts them.
- **Writing queries was rarely the problem:** 9 of 413 queries failed.
