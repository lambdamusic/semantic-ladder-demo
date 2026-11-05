The table shows the current rules (version 2), with every reading condition in one run per model ([Sonnet](/runs/credit/2026-11-05-1227-sonnet/), [Haiku](/runs/credit/2026-11-05-1233-haiku/)).

- **Written-down meaning helps, and the gain sits in the local rules.** The definitions add +15 to +16 points for Sonnet and +20 to +21 for Haiku. On the local rules (Q41 to Q48), `csv` scores 57% and 40%; every condition with the meaning reaches 88–100%.
- **The form matters little.** Markdown scores the same as Turtle. RDF alone adds nothing, and costs Haiku 6 points. The decoy glossary (`csv+padding`: bond-market terms, as long as the definitions, none of them relevant) stays within 2 points of `csv`.
- **Logic works as well as prose.** With only the axioms, both models score 99%. An axiom is followed to the letter, mistakes included: in version 1 the axioms made `TestRecord` a subclass of `Entity`, and both models counted the test record (Q37). The fix made Q37 right.
- **One sentence can slant an answer.** The ontology calls the foreign-currency rating "the headline rating". With it, Haiku gets Q10 ("is Valdoria Telecom investment grade?") right in 2 of 5 repeats with the Turtle and 1 of 5 with the Markdown. Made neutral, it's right in 5 of 5, and so it is with the axioms, which carry no prose.
- **Executed rules help as much as definitions** on this data: +15 points for Sonnet and +19 for Haiku. What they don't give is the reason: the one "why" question (Q6) is answered only partly in most repeats.

The list of every run below has version 1 and version 2 together. Each run is graded against the keys it ran with.
