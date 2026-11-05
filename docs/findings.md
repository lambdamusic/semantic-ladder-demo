Where each of the [five goals](/#goals) stands, from the runs so far. The [results](/results/) put each dataset's latest runs side by side, and each run's own page has the numbers behind them. Accuracy is the mean over questions of each question's score across five repeats, unless a run says otherwise. Differences are paired, question by question, with a 95% bootstrap interval.

Goals 1, 2, 4 and 5 rest on one run per model and domain, each asking every reading condition its domain has: credit on its current rules, version 2 ([Sonnet](/runs/credit/2026-11-05-1227-sonnet/), [Haiku](/runs/credit/2026-11-05-1233-haiku/)), and research ([Sonnet](/runs/research/2026-11-05-1234-sonnet/), [Haiku](/runs/research/2026-11-05-1235-haiku/)). Earlier runs, including the credit runs on version 1, whose rule the model could guess, are under [all runs](/runs/).

## 1. Does written-down meaning help?

**Answered: yes, and by a lot where the data has rules of its own.**

| Domain | Model | Data only (`csv`) | With the definitions |
|---|---|---|---|
| Credit | Sonnet | 84% | 99–100% |
| Credit | Haiku | 78% | 98–100% |
| Research | Sonnet | 57% | 98% |
| Research | Haiku | 45% | 96–99% |

- **It isn't just any expert text on the subject.** `csv+padding` gives the data plus a decoy: a glossary as long as the definitions, on the same subject (bond markets; scholarly publishing), that defines none of the terms the questions depend on. It scores within 2 points of `csv` in every case. So the gain comes from what the definitions say, not from a longer prompt full of domain words.
- **The gain sits in each dataset's own rules.** These are the meanings an analyst can't know from outside: which record is a test record, which system holds an entity's domicile, whether an affiliated institute counts for its parent. On those questions, `csv` scores 40–57% on credit and 16–18% on research; with the definitions, 97–100%. Where a question only needs general knowledge, the models mostly know it already.
- **The meaning has to be right.** The definitions are followed as written, so one slanted sentence in the prose can flip an answer (see goal 2).

## 2. Does the form of the meaning matter?

**Mostly answered: the format matters little; what's written down, and whether the rules have run, matters more.**

- **Markdown matches Turtle.** The same definitions as a Markdown glossary or as SKOS in `ontology.ttl` score within one to three points of each other in both domains.
- **RDF alone adds nothing, and can cost.** The same facts as RDF, without the ontology, never beat the CSV. Haiku loses 6 points on credit and Sonnet 9 on research, both with intervals below zero, and the prompt is larger.
- **Logic without prose does about as well as prose.** With the definitions removed and only OWL axioms and SHACL rules left (`csv+axioms`), credit scores 99% with both models. The models read and apply the axioms.
- **But axioms are followed to the letter, mistakes included.** When an earlier version of the axioms wrongly made a test record a kind of entity, both models counted it in every repeat. Once the axiom was fixed, the count came right.
- **Prose carries its author's emphasis; axioms don't.** One sentence calling the foreign-currency rating "the headline rating" makes Haiku answer Q10 wrongly: it's right in 2 of 5 repeats with the Turtle and 1 of 5 with the Markdown. With the sentence made neutral (`csv+neutral`), or with the axioms alone, it's right in 5 of 5. Sonnet slips too, in 2 of 5 with the Turtle.
- **Logic and executed rules say what, not why.** The one question that asks for a cause (Q6, why a rating sits where it does) is answered only partly in most repeats with the axioms alone or the executed data, and in full with the prose.
- **Rules already run over the data match the definitions on credit, but not on research.** The `executed` data, with records merged and rules applied and no definitions, gains +15 to +19 points on credit, reaching 97–99%, and +34 to +46 on research, reaching 90–92%: 6 to 9 points short of the definitions. The research misses come from how the tables were built: merging a preprint into its published version hides it (Q2, Q20), the counting questions lose the per-author shares (Q12, Q13), there's no ultimate-parent column (Q46), and the reasons behind the rules are lost (Q47, Q48).

*Still open:* axioms for the research domain, and executed tables that keep what they merged.

## 3. Should the model read the data or query it?

**Partly answered: at the sizes tried so far, querying doesn't beat reading, and a graph store doesn't beat SQL.**

At 300 issuers, the model either reads the CSV or writes SQL (DuckDB) or SPARQL (rdflib) without seeing the rows ([reading](/runs/credit_300/2026-11-04-1738-sonnet/), [querying](/runs/credit_300/2026-11-04-1738-sonnet-query/), Sonnet):

| | No definitions | With the definitions |
|---|---|---|
| Reading (`csv`, `csv+markdown`) | 80% | 95% |
| SQL (`sql`, `sql+markdown`) | 86% | 96% |
| SPARQL (`sparql`, `sparql+ontology`) | 79% | 95% |

- **The definitions matter as much when querying as when reading:** +10 to +16 points in each mode.
- **Querying helps a little with long lists,** where reading misses an item or two.
- **On ownership paths of unknown depth** ([reading](/runs/credit_paths/2026-11-04-2022-sonnet/), [querying](/runs/credit_paths/2026-11-04-2024-sonnet-query/)), a graph store doesn't help without the definitions: SPARQL gets 33% of the path questions and SQL 44%. With the definitions, SPARQL is the steadiest querying condition (92%). A precomputed `ancestors` table gives SQL every path right, and reading the 100 KB of CSV with the definitions also gets every path right.
- **So the graph's advantage, following links of any depth, disappears once the rules have computed the chains.**

*Still open:* the querying runs used three repeats, and one bad session moves a path score by about 30 points, so SQL and SPARQL can't yet be told apart; five repeats are next. Querying should pay off when the data is too large to read, which hasn't been tested yet. The research domain hasn't been queried.

## 4. Does it hold across models?

**Partly answered: for Claude Haiku and Sonnet, yes.**

- **The weaker the model, the more the definitions are worth.** Haiku gains +20 to +21 points on credit and +51 to +53 on research, against Sonnet's +15 to +16 and +41.
- **With the definitions, the two models end up level.** Both reach 96–100% in both domains.
- **Text that doesn't carry the meaning helps neither model.** The decoy glossary stays within 2 points of `csv` for both. An earlier credit run had Haiku lose 5 points with it, which this run doesn't repeat (−2, −6 to +1).

*Still open:* Opus and Gemini, set aside for now.

## 5. Does the domain matter?

**Answered for the two domains so far: the pattern is the same, and the size of the gain depends on the domain.**

| | Credit ratings | Research analytics |
|---|---|---|
| Data only (`csv`), Sonnet and Haiku | 84% and 78% | 57% and 45% |
| With the definitions | 98–100% | 96–99% |
| RDF alone, or the decoy glossary | no gain | no gain |
| Markdown against Turtle | level | level |
| Executed rules, no definitions | +15 to +19 | +34 to +46 |

- **The findings hold in both:** RDF alone and the decoy glossary add nothing, Markdown matches Turtle, and the definitions lift both models to 96–100%.
- **What changes is how much the data says for itself.** Without the definitions, the models start much lower on research, because more of its questions rest on the dataset's own rules and terms (what counts as a "research work", which affiliation is credited, what an affiliated institute's parent link means). So the definitions are worth +41 to +53 points there, against +15 to +21 on credit. A domain whose meaning is mostly general knowledge gains less, and one with many local conventions gains more.
- **Executed rules depend more on the domain:** they match the definitions on credit and fall short on research, where they also depend on how the tables were designed, since merging records and rolling up institutions decide what the data can still answer.

*A caveat:* some of the research questions use the dataset's own terms, which only the ontology defines, so some answers marked wrong without it are defensible readings of the question. A review found they're mostly the questions that depend on the local rules anyway.

*Still open:* two domains can show that the domain matters, but not what it is about a domain that matters. A third domain, with a different balance of general and local meaning, would test the explanation above.
