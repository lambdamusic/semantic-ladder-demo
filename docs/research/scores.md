The table shows every reading condition in one run per model ([Sonnet](/runs/research/2026-11-05-1234-sonnet/), [Haiku](/runs/research/2026-11-05-1235-haiku/)). `csv+axioms` and `csv+axioms+markdown` come from their own runs ([Sonnet](/runs/research/2026-11-06-0855-sonnet/), [Haiku](/runs/research/2026-11-06-0855-haiku/)): `csv+axioms` scores 97% with both models and `csv+axioms+markdown` 98%, as the prose definitions do. The misses are Q1, which most conditions read as the three name forms, and partial answers to the "why" questions (Q47, Q48): the logic says what counts, not why.

- **The same pattern as credit, and larger.** The definitions add +41 points for Sonnet and +51 to +53 for Haiku. The decoy glossary (`csv+padding`) adds nothing, Markdown matches Turtle, and RDF alone costs Sonnet 9 points (−17 to −3).
- **The gain sits in the dataset's own rules.** On the local rules (Q33 to Q48), `csv` scores 16% for Sonnet and 18% for Haiku, and the definitions take them to 97–99%. On the general questions (Q1 to Q32), `csv` scores 77% and 59%. Most of that general gap also rests on rules that belong to the dataset: retracted works aren't research output (Q24 to Q26), and the hierarchy counts depend on the affiliation and affiliate rules (Q7, Q9, Q10). Without the ontology, the model has noticed the retraction flag and said dropping retracted works "would be a policy choice the data doesn't make". That's a fair reading, and exactly what an ontology is for.
- **Executed rules get most of the way, but not all:** 90% for Sonnet and 92% for Haiku, 6 to 9 points short of the definitions. The misses come from the tables' design. Merging a preprint into its published version hides it (Q2, Q20). The counting questions lose the per-author shares (Q12, Q13). There's no ultimate-parent column (Q46). And executed rules don't say why (Q47, Q48).

Querying, with Sonnet and five repeats ([run](/runs/research/2026-11-06-0808-sonnet-query/); `sparql+axioms` in [its own run](/runs/research/2026-11-06-1127-sonnet-query/)), against reading with the same model.

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading | `csv` 57% | `csv+markdown` 98% | `executed` 90% |
| SQL | `sql` 52% | `sql+markdown` 96% | `sql+executed` 93% |
| SPARQL | `sparql` 40% | `sparql+ontology` 81% | `sparql+axioms` 72% |

- **At this size, querying with the definitions does as well as reading with them:** 96% with SQL, every session between 96% and 97%, against 98% reading. The local rules are right in 99% of answers.
- **Executed tables don't beat the definitions here:** 93% with SQL. At 850 works the order reverses: SQL with the definitions drops to 80% and SQL over executed tables holds at 92% ([scores at 850 works](/scores/#research_850)). So the case for running the rules first grows with the data.
- **SPARQL sessions break down in a way SQL sessions don't.** `sparql+ontology` scores 97–98% in four sessions and 17% in the fifth, where the model gave up after one round, saying the store returned "repeated, contradictory rows" when no query had failed. One `sparql` session and one `sparql+axioms` session scored 0%: the model began writing tool-call markup instead of query blocks and ended without answers. The other four `sparql+axioms` sessions score 81–98%, about 90% on average, level with the executed tables. The misses there are Q1 and partial answers to the "why" questions (Q47, Q48).
- **Without the definitions, querying is no better than reading:** 52% with SQL and 40% with SPARQL, against 57%.
