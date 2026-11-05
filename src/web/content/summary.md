Where each of the [five goals](/#goals) stands, from the runs so far. The [results log](/log/) has every run's findings in order, and each run's own page has the numbers behind them. Accuracy is the mean over questions of each question's score across five repeats, unless a run says otherwise. Differences are paired, question by question, with a 95% bootstrap interval.

The credit figures come from the domain's current rules (version 2: [Sonnet](/runs/credit/2026-11-04-2013-sonnet/), [Haiku](/runs/credit/2026-11-04-2028-haiku/)). The earlier credit runs had a rule the model could guess, and the log keeps them.

## 1. Does written-down meaning help?

**Answered: yes, and by a lot where the data has rules of its own.**

| Domain | Model | Data only (`csv`) | With the definitions |
|---|---|---|---|
| Credit | Sonnet | 85% | 99–100% |
| Credit | Haiku | 78% | 99–100% |
| Research | Sonnet | 56% | 97–98% |
| Research | Haiku | 44% | 96–97% |

- **Length doesn't explain it.** `csv+padding`, the data plus a finance text of the same length about other things, scores about the same as `csv`, or a little lower.
- **The gain sits in each dataset's own rules.** These are the meanings an analyst can't know from outside: which record is a test record, which system holds an entity's domicile, whether an affiliated institute counts for its parent. In the research domain they go from 18% to 98% with Sonnet. Where a question only needs general knowledge, the models mostly know it already.
- **The meaning has to be right.** The definitions are followed as written, so one slanted sentence in the prose can flip an answer (see goal 2).

## 2. Does the form of the meaning matter?

**Mostly answered: the format matters little; what's written down, and whether the rules have run, matters more.**

- **Markdown matches Turtle.** The same definitions as a Markdown glossary or as SKOS in `ontology.ttl` score within a point or two of each other in both domains.
- **RDF alone adds nothing.** The same facts as RDF, without the ontology, score the same as the CSV or a little lower, and the prompt is larger.
- **Logic without prose does about as well as prose.** With the definitions removed and only OWL axioms and SHACL rules left (`csv+axioms`), credit scores 99% with Sonnet and 100% with Haiku. The models read and apply the axioms.
- **But axioms are followed to the letter, mistakes included.** When an axiom wrongly made a test record a kind of entity, both models counted it in every repeat. Once the axiom was fixed, the count came right.
- **Prose carries its author's emphasis; axioms don't.** One sentence calling the foreign-currency rating "the headline rating" made Haiku answer a question wrongly in most repeats. With the sentence made neutral, or with the axioms alone, the answer is right.
- **Rules already run over the data get most of the way, but not all.** The `executed` data, with records merged and rules applied and no definitions, gains +9 to +15 points on credit and +35 to +48 on research. It still falls 4 to 6 points short of the definitions on research, because of how the tables were built: merging hides what was merged, and the reasons behind the rules are lost.

*Still open:* axioms for the research domain, and executed tables that keep what they merged.

## 3. Should the model read the data or query it?

**Partly answered: at the sizes tried so far, querying doesn't beat reading, and a graph store doesn't beat SQL.**

At 300 issuers, the model either reads the CSV or writes SQL (DuckDB) or SPARQL (rdflib) without seeing the rows ([reading](/runs/credit_300/2026-11-04-1738-sonnet/), [querying](/runs/credit_300/2026-11-04-1738-sonnet-query/), Sonnet):

| | No definitions | With the definitions |
|---|---|---|
| Reading | 80% | 95% |
| SQL | 86% | 96% |
| SPARQL | 79% | 95% |

- **The definitions matter as much when querying as when reading:** +10 to +16 points in each mode.
- **Querying helps a little with long lists,** where reading misses an item or two.
- **On ownership paths of unknown depth** ([reading](/runs/credit_paths/2026-11-04-2022-sonnet/), [querying](/runs/credit_paths/2026-11-04-2024-sonnet-query/)), a graph store doesn't help without the definitions: SPARQL gets 33% of the path questions and SQL 44%. With the definitions, SPARQL is the steadiest querying condition (92%). A precomputed `ancestors` table gives SQL every path right, and reading the 100 KB of CSV with the definitions also gets every path right.
- **So the graph's advantage, following links of any depth, disappears once the rules have computed the chains.**

*Still open:* the querying runs used three repeats, and one bad session moves a path score by about 30 points, so SQL and SPARQL can't yet be told apart; five repeats are next. Querying should pay off when the data is too large to read, which hasn't been tested yet. The research domain hasn't been queried.

## 4. Does it hold across models?

**Partly answered: for Claude Haiku and Sonnet, yes.**

- **The weaker the model, the more the definitions are worth.** Haiku gains +21 points on credit and +52 on research, against Sonnet's +14 and +41.
- **With the definitions, the two models end up level.** Both reach 96–100% in both domains.
- **A small model is hurt more by irrelevant text:** Haiku lost 5 points with the padding, in an earlier credit run.

*Still open:* Opus and Gemini, set aside for now.

## 5. Does the domain matter?

**Answered for the two domains so far: the pattern is the same, and the size of the gain depends on the domain.**

| | Credit ratings | Research analytics |
|---|---|---|
| Data only (`csv`), Sonnet and Haiku | 85% and 78% | 56% and 44% |
| With the definitions | 99–100% | 96–98% |
| RDF alone, or the length control | no gain | no gain |
| Markdown against Turtle | level | level |
| Executed rules, no definitions | +9 to +15 | +35 to +48 |

- **The findings hold in both:** RDF alone and the length control add nothing, Markdown matches Turtle, and the definitions lift both models to 96–100%.
- **What changes is how much the data says for itself.** Without the definitions, the models start much lower on research, because more of its questions rest on the dataset's own rules and terms (what counts as a "research work", which affiliation is credited, what an affiliated institute's parent link means). So the definitions are worth +41 to +52 points there, against +14 to +21 on credit. A domain whose meaning is mostly general knowledge gains less, and one with many local conventions gains more.
- **Executed rules depend more on the domain:** on research they also depend on how the tables were designed, since merging records and rolling up institutions decide what the data can still answer.

*A caveat:* some of the research questions use the dataset's own terms, which only the ontology defines, so some answers marked wrong without it are defensible readings of the question. A review found they're mostly the questions that depend on the local rules anyway.

*Still open:* two domains can show that the domain matters, but not what it is about a domain that matters. A third domain, with a different balance of general and local meaning, would test the explanation above.
