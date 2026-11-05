Every reading condition in one run per model ([Sonnet](/runs/research/2026-11-05-1234-sonnet/), [Haiku](/runs/research/2026-11-05-1235-haiku/)). The domain has no axioms yet, so no `csv+axioms`.

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 57% | 45% |
| `rdf` | 47% | 43% |
| `csv+padding` | 57% | 44% |
| `csv+markdown` | 98% | 99% |
| `csv+ontology` | 98% | 96% |
| `rdf+ontology` | 98% | 98% |
| `executed` | 90% | 92% |

- **The same pattern as credit, and larger.** The definitions add +41 points for Sonnet and +51 to +53 for Haiku. The decoy glossary (`csv+padding`) adds nothing, Markdown matches Turtle, and RDF alone costs Sonnet 9 points (−17 to −3).
- **The gain sits in the dataset's own rules.** On the local rules (Q33 to Q48), `csv` scores 16% for Sonnet and 18% for Haiku, and the definitions take them to 97–99%. On the general questions (Q1 to Q32), `csv` scores 77% and 59%. Most of that general gap also rests on rules that belong to the dataset: retracted works aren't research output (Q24 to Q26), and the hierarchy counts depend on the affiliation and affiliate rules (Q7, Q9, Q10). Without the ontology, the model has noticed the retraction flag and said dropping retracted works "would be a policy choice the data doesn't make". That's a fair reading, and exactly what an ontology is for.
- **Executed rules get most of the way, but not all:** 90% for Sonnet and 92% for Haiku, 6 to 9 points short of the definitions. The misses come from the tables' design. Merging a preprint into its published version hides it (Q2, Q20). The counting questions lose the per-author shares (Q12, Q13). There's no ultimate-parent column (Q46). And executed rules don't say why (Q47, Q48).
