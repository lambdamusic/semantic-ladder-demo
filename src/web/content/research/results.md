## What the runs show

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 56% | 44% |
| `rdf` | 50% | 44% |
| `csv+padding` | 55% | 45% |
| `csv+markdown` | 97% | 96% |
| `csv+ontology` | 97% | 97% |
| `rdf+ontology` | 98% | 97% |

- **The same pattern as credit, and larger.** The definitions add +41 points for Sonnet and +52 for Haiku. RDF alone and the length control add nothing, and Markdown matches Turtle.
- **The gain sits in the dataset's own rules.** For Sonnet, the local rules go from 18% to 98%, and the general questions from 75% to 97%. Most of the general gap rests on rules that also belong to the dataset. Retracted works aren't research output (Q24 to Q26). The hierarchy counts depend on the affiliation and affiliate rules (Q7, Q9, Q10). Without the ontology, the model noticed the retraction flag and said dropping retracted works "would be a policy choice the data doesn't make". That's a fair reading, and exactly what an ontology is for.

`csv` against `executed` for both models is under way.
