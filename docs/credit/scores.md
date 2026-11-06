The table shows every reading condition in one run per model ([Sonnet](/runs/credit/2026-11-05-1227-sonnet/), [Haiku](/runs/credit/2026-11-05-1233-haiku/)).

- **Written-down meaning helps, and the gain sits in the local rules.** The definitions add +15 to +16 points for Sonnet and +20 to +21 for Haiku. On the local rules (Q41 to Q48), `csv` scores 57% and 40%; every condition with the meaning reaches 88–100%.
- **The form matters little.** Markdown scores the same as Turtle. RDF alone adds nothing, and costs Haiku 6 points. The decoy glossary (`csv+padding`: bond-market terms, as long as the definitions, none of them relevant) stays within 2 points of `csv`.
- **Logic works as well as prose.** With only the axioms, both models score 99%. An axiom is followed to the letter, mistakes included: when an earlier draft of the axioms made `TestRecord` a subclass of `Entity`, both models counted the test record (Q37). Fixing the axiom made Q37 right.
- **One sentence can slant an answer.** The ontology calls the foreign-currency rating "the headline rating". With it, Haiku gets Q10 ("is Valdoria Telecom investment grade?") right in 2 of 5 repeats with the Turtle and 1 of 5 with the Markdown. Made neutral, it's right in 5 of 5, and so it is with the axioms, which carry no prose.
- **Executed rules help as much as definitions** on this data: +15 points for Sonnet and +19 for Haiku. What they don't give is the reason: the one "why" question (Q6) is answered only partly in most repeats.


Querying ([Sonnet](/runs/credit/2026-11-06-0935-sonnet-query/)), five repeats, against reading with the same model:

| | No definitions | With the definitions | Rules run |
|---|---|---|---|
| Reading | `csv` 84% | `csv+markdown` 100% | `executed` 99% |
| SQL | `sql` 84% | `sql+markdown` 100% | `sql+executed` 99% |
| SPARQL | `sparql` 82% | `sparql+ontology` 100% | `sparql+axioms` 90% |

- **At this size, querying and reading end up level:** 100% with the definitions either way, and 82–84% without them. The data is small enough that the model fetches whole tables in a few queries and then reads them.
- **SPARQL with the ontology is as good as SQL with the definitions:** 100% in all five sessions.
- **`sparql+axioms` misses the test record.** Its five misses (Q7, Q9, Q37, Q40, Q41) all come from E16, Brindle Capital, a `QA` test record that describes no real entity. The executed tables drop test records. The graph after the axioms' rules keeps it, unmarked, and the note on what the rules derived doesn't mention it, so the model counts it, and its 2026 downgrade, as real. The same misses explain the 300-issuer run's empty or wrong answers to Q7. A rule that marks test records, and a line in the note, would close the gap.
