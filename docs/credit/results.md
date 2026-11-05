- **Written-down meaning helps, and the gain sits in the local rules.** On version 1, Sonnet went from 88–89% with `csv` to 99–100% with the definitions, and Haiku from 79% to 97–99%. On version 2, with a rule that can't be guessed, Sonnet goes from 85% to 99–100% (+14 to +15 points), and Haiku from 78% to 99–100% (+20 to +22).
- **The form matters little.** Markdown scores the same as Turtle, and RDF alone adds nothing. The decoy glossary (`csv+padding`: bond-market terms, as long as the definitions, none of them relevant) adds nothing for Sonnet and costs Haiku 5 points.
- **Logic works as well as prose.** With only the axioms, Sonnet scores 97–99% and Haiku 98–100%. An axiom is followed to the letter, mistakes included. In version 1 the axioms made `TestRecord` a subclass of `Entity`, and both models counted the test record (Q37). The fix made Q37 right in every run.
- **One sentence can slant an answer.** The ontology called the foreign-currency rating "the headline rating". With it, Q10 ("is Valdoria Telecom investment grade?") was right in 1 run of 5. Made neutral, it was right in 5 of 5. The axioms, which carry no prose, give no slant.
- **Executed rules help as much as definitions:** +9 points on the base data.

The tables below list every run on the base data, version 1 and version 2 together. Each run is graded against the keys it ran with.
