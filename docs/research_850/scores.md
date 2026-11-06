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
