# Lab notebook

What each run showed, in the order they ran, newest last. The reports in `results/` hold the numbers; this file
holds what they mean, and what changed because of them.

## 4 November 2026: baseline, ten questions

`results/credit/2026-11-04-1526-sonnet/`, Sonnet, four conditions, five repeats.

- **No condition stands out:** accuracy ranged from 93% (`rdf`) to 99% (`rdf+ontology`), and all the intervals overlap. Only `rdf+ontology` gained clearly against `csv`: +4 points (+0 to +12), nearly all on Q6.
- **The LLM grader added the noise:** code grading and the LLM grader agreed on 170 of 180 answers. Nine of the ten disagreements were the LLM grader giving partial credit to right answers; under code grading, only one question in one condition varied across repeats.
- **An ontology can mislead:** in `csv+ontology`, Q10 got a flat "No" in two of five repeats where the key says "depends", because the ontology calls the foreign-currency rating "the headline rating".

## 4 November 2026: forty questions

`results/credit/2026-11-04-1616-sonnet/`, after a grader fix (null and NR accepted as no rating).

- **Still at the ceiling:** 98% to 100% in every condition. Sonnet already knows general credit conventions (dates, outlooks, withdrawals, guarantors, groups), so an ontology restating them adds nothing.
- **What did separate:** Q6 again, where without the ontology the model sees the ceiling but won't name it as the cause.

## 4 November 2026: local meanings

`results/credit/2026-11-04-1643-sonnet/`, 48 questions, six conditions. Five rules the dataset sets for itself, stated only in the ontology.

| Condition | Accuracy | Against `csv` (95% interval) |
|---|---|---|
| `csv` | 88% | |
| `rdf` | 89% | +1 (−2 to +4) |
| `csv+padding` | 86% | −2 (−4 to +0) |
| `csv+ontology` | 99% | +11 (+3 to +21) |
| `rdf+ontology` | 100% | +12 (+4 to +22) |
| `csv+markdown` | 100% | +12 (+4 to +22) |

- **The first clear effect:** the definitions add 11 to 12 points, and a text of the same length about other things adds nothing.
- **Form doesn't matter here:** Markdown matches Turtle.
- **The QA rule carries most of it:** without the definitions, Sonnet treats the test record as a real issuer every time, which also spoils four earlier questions. The local currency code helps in some repeats.
- **Three rules made no difference.** Sonnet guessed the system of record from the LEI, because the invented LEIs then contained the country code (fixed afterwards: LEIs are now opaque). It knew a credit opinion isn't an issuer rating. And it got the expected rating right in `csv`, once for the wrong reason ("expired"), which code grading can't see.

## 4 November 2026: opaque LEIs, Sonnet again

`results/credit/2026-11-04-1711-sonnet/`, the same 48 questions after the LEIs were made opaque.

- **The same picture:** `csv` 89%; `csv+ontology`, `csv+markdown` and `rdf+ontology` 100%, each +11 points (+3 to +20 or +21). `csv+padding` gains nothing, and `rdf` alone loses 3 points (−5 to −1).
- **The system of record is still guessed:** with nothing in the LEI to go on, plain `csv` still picks the RATINGS record for Halden Bank in every repeat. The system's name gives it away, so this rule isn't local enough to test.
- **What only the definitions supply:** the QA rule, every time (Q7, Q9, Q37, Q40, Q41), and the cause in Q6.

## 4 November 2026: executed rules, Sonnet

`results/credit/2026-11-04-1712-sonnet/`: `csv` against `executed`, the data after its rules have run, with no definitions.

- **Curation buys most of it:** `executed` 98% against `csv` 89%, +9 points (+2 to +18). Dropping the QA record fixes the questions it spoiled.
- **It doesn't fix counting:** `executed` missed the entity count (Q37) in three of five repeats, saying 15 for a table of 16 rows.
- **It doesn't explain:** with a ceilings table and no definition, Q6 hedged in four of five repeats.

## 4 November 2026: local meanings, Haiku

`results/credit/2026-11-04-1644-haiku/` (with the old, leaky LEIs, so set aside Q42 and Q43).

| Condition | Accuracy | Against `csv` (95% interval) |
|---|---|---|
| `csv` | 79% | |
| `rdf` | 75% | −4 (−9 to +1) |
| `csv+padding` | 74% | −5 (−10 to −1) |
| `rdf+ontology` | 97% | +18 (+8 to +29) |
| `csv+ontology` | 98% | +19 (+8 to +31) |
| `csv+markdown` | 99% | +20 (+11 to +31) |

- **The weaker the model, the more the definitions are worth:** the gain is about twice Sonnet's, and with them Haiku nearly matches Sonnet.
- **Irrelevant text costs a small model:** the padding loses 5 points, with an interval below zero.
- **The expected-rating rule now separates:** Haiku fails it without the definitions; Sonnet had guessed it.
- **The ontology's slant is worse:** `csv+ontology` answered Q10 "No" in all five repeats.

## 4 November 2026: one sentence of slant, Haiku

`results/credit/2026-11-04-1723-haiku/`: `csv+ontology` against `csv+neutral`, the same ontology with one sentence changed, from "The foreign-currency (FC) one is the headline rating" to "An entity may have a foreign-currency (FC) one, a local-currency (LC) one, or both".

- **One sentence decides the answer:** Q10 is right in one of five repeats with the original wording and in five of five with the neutral one. The wrong answers quote the sentence back.
- **An ontology carries its authors' emphasis as well as its meaning.** A definition that ranks one reading above another is followed, even where the question needs both.

## 4 November 2026: reading at 300 issuers, Sonnet

`results/credit_300/2026-11-04-1738-sonnet/`: the 48 questions over the base data plus 300 invented issuers that repeat its traps.

- **Scale widens the gap:** `csv` falls to 80%; `csv+markdown` and `executed` reach 95%, both +15 points (+7 to +24 or +25).
- **Curated data catches up with the definitions at scale,** and fixes the entity count that it missed on the base data.
- **Long lists fail everywhere:** the Watch list (about 30 issuers, Q18) is wrong in every repeat of every condition, and the negative outlooks (Q19) in all but two. One wrong ID fails the list.

## 4 November 2026: the meaning as logic, Sonnet and Haiku

`results/credit/2026-11-04-1825-sonnet/` and `2026-11-04-1824-haiku/`. `csv+axioms` gets the ontology with every definition and comment removed (names and codes kept) plus `axioms.ttl`: OWL axioms and SHACL rules, which run in pySHACL and agree with the keys.

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 89% | 78% |
| `csv+ontology` (prose) | 100% (+11) | 100% (+22) |
| `csv+axioms` (logic, no prose) | 97% (+8) | 98% (+20) |
| `csv+axioms+markdown` | 100% (+11) | 98% (+20) |

- **Models use logic they have to read:** with only the axioms, both apply the test-record rule in every repeat, from `TestRecord ≡ sourceSystem "QA"` and its disjointness from `Issuer`.
- **An axiom is followed to the letter, errors included:** the entity count (Q37) is wrong in all ten repeats with the axioms alone, because the axioms declare `TestRecord rdfs:subClassOf lad:Entity`, where the prose says a test record describes no real entity. The mistake is the author's, and the model reproduces it faithfully.
- **Logic says what, not why:** Sonnet hedged on Q6's cause in three of five repeats with the axioms alone. Haiku didn't.
- **Without prose there's no slant:** Q10 is right in every axioms-only repeat. With the Markdown added back, Haiku answers it "No" in four of five, quoting the "headline rating" sentence.
- **Form matters little again:** for both models, logic alone comes within 2 to 3 points of prose, and the two together add nothing over prose.

## 4 November 2026: the research domain, Haiku

`results/research/2026-11-04-1752-haiku/`: an invented domain shaped like OpenAlex, 48 questions, built by a subagent and reviewed.

| Condition | Accuracy | Against `csv` (95% interval) |
|---|---|---|
| `csv` | 44% | |
| `rdf` | 44% | +0 (−4 to +6) |
| `csv+padding` | 45% | +2 (−1 to +5) |
| `csv+markdown` | 96% | +52 (+39 to +65) |
| `csv+ontology` | 97% | +54 (+40 to +67) |
| `rdf+ontology` | 97% | +54 (+40 to +67) |

- **The same pattern in a second domain:** RDF alone and the length control add nothing; Markdown matches Turtle.
- **Much larger:** local rules go from 14–20% to 99–100%, and the general questions from 56–58% to 96–98%.
- **To check before quoting it:** many general questions rest on the dataset's own terms ("research work", which affiliation is "credited"), which only the ontology defines, so some answers marked wrong without it may be defensible readings. A Sonnet run and a review of those questions come first.

## 4 November 2026: querying at 300 issuers, Sonnet

`results/credit_300/2026-11-04-1738-sonnet-query/`: the model never sees the rows. It writes SQL (DuckDB) or SPARQL (rdflib), up to eight rounds, and answers from the results. The same 48 questions as reading at 300 issuers.

| | No definitions | With the definitions (Markdown) |
|---|---|---|
| Reading (`csv`, `csv+markdown`) | 80% | 95% |
| SQL (`sql`, `sql+markdown`) | 86% | 96% |
| SPARQL (`sparql`, `sparql+ontology`) | 79% | 95% |

- **Querying beats reading only a little:** +6 points without definitions and +1 with them. The definitions are worth about the same in both modes (+10 for SQL, +16 for SPARQL, +15 for reading).
- **A graph store doesn't help here:** SPARQL without definitions is 7 points below SQL (−11 to −3), and with them the two tie. These questions need joins, not paths, which is why the path questions came next (`domains/credit_paths`).
- **Lists are where querying pays:** strict list accuracy is 60% for `sql` and 86% for `sql+markdown`, against 51% and 71% reading. Mean F1 is 92–100% everywhere, so the misses are an item or two.
- **Writing queries was rarely the problem:** 9 of 413 queries failed, 2 of them on the 60-second limit added after one rdflib query ran for two hours. Sessions used six to seven rounds.

## 4 November 2026: credit domain v2, Sonnet and Haiku

`results/credit/2026-11-04-2013-sonnet/`: the domain changed (commit 18a2f42), so these scores aren't comparable with the runs above. In v1 `csv` got Q42 and Q43 right in every run, so the system-of-record rule was guessable: RATINGS sounds authoritative. In v2 domicile comes from RESEARCH, and names and parents from RATINGS. The axioms' test-record mistake is fixed.

Haiku's run is `results/credit/2026-11-04-2028-haiku/`.

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 85% | 78% |
| `csv+ontology` | 99% (+14, +5 to +25) | 99% (+21, +10 to +32) |
| `csv+markdown` | 100% (+15, +6 to +25) | 99% (+20, +10 to +32) |
| `csv+axioms` | 99% (+14, +5 to +25) | 100% (+22, +11 to +33) |

- **The new rule can't be guessed:** `csv` gets Q42 and Q43 wrong in all five runs; every condition with the meaning written down gets them right.
- **The fixed axiom works:** Q37 is right in all five `csv+axioms` runs for both models (0 of 5 before).
- **Logic alone is enough for Haiku:** 100% with the axioms and no prose. Q10's slant comes back with the prose: Haiku answers it wrong in 3 of 5 runs with `csv+ontology` and 2 of 5 with `csv+markdown`, and in none with the axioms.

## 4 November 2026: right for the right reason? Credit v2, Sonnet

`results/credit/2026-11-04-2013-sonnet/reasons.md`: `reasons.py` had Sonnet read the reasoning behind every answer graded correct in `csv` and `csv+markdown`, against what each question tests.

| Condition | Correct answers | Sound | Unsound | Unclear |
|---|---|---|---|---|
| `csv` | 200 | 156 (78%) | 18 (9%) | 26 (13%) |
| `csv+markdown` | 235 | 210 (89%) | 6 (3%) | 19 (8%) |

- **Without the definitions, more right answers rest on shaky reasoning:** 9% against 3% unsound. Examples are Marlow's rating taken from file order rather than dates (Q11), and the note's rating read without the notching it tests (Q3).
- **Most "unclear" verdicts are terse answers:** the system prompt asks for concision, so many answers give the value and an action ID only.
- **Treat it as indicative:** this grader is an LLM, and some of its verdicts contradict themselves (it marks Q35 "unsound" while saying the reasoning holds). It's a second look, not a score.

## 4 November 2026: the research domain, Sonnet

`results/research/2026-11-04-2010-sonnet/`: the same six conditions as Haiku's run.

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 56% | 44% |
| `rdf` | 50% (−6, −14 to +2) | 44% |
| `csv+padding` | 55% (−1) | 45% |
| `csv+markdown` | 97% (+41, +29 to +55) | 96% |
| `csv+ontology` | 97% (+41) | 97% |
| `rdf+ontology` | 98% (+42) | 97% |

- **It holds with the stronger model:** a smaller gain than Haiku's (+41 against +52) because `csv` starts higher. With the definitions, both models reach 96–98%. Format and length add nothing, again.
- **Where the gap sits:** the local rules (Q33 to Q48) go from 18% to 98%, and the general questions (Q1 to Q32) from 75% to 97%.
- **The review of the general questions:** most of the general-question gap is the retraction questions (Q24 to Q26) and the hierarchy counts that also depend on local rules (Q7, Q9, Q10). On Q26 the `csv` answer saw the retraction flag and said that dropping retracted works "would be a policy choice the data doesn't make". That's a fair reading: whether a retracted work is research output is the dataset's own rule, stated only in the ontology. Counted with the local rules, the general questions the model can't know are few.

## 4 November 2026: the research domain, executed rules

`results/research/2026-11-04-2035-haiku/` and `2026-11-04-2053-sonnet/`: `csv` against `executed`, the tables `domains/research/execute.py` writes after applying the rules, with no definitions.

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 58% | 42% |
| `executed` | 93% (+35, +21 to +48) | 90% (+48, +33 to +62) |
| for reference, `csv+markdown` in the runs above | 97% | 96% |

- **Executed rules get most of the way:** 4 to 6 points short of the definitions.
- **The misses come from how the tables were built, not from the models:**
  - Merging a preprint into its published version hides the preprint, so the questions about versions (Q2, Q20) lose what they ask about.
  - The institutions table keeps the raw parent link and has no ultimate-parent column, so the model followed Halloran's parent link (Q46), although the roll-up table says Halloran counts only for itself.
  - The "why" questions (Q47, Q48) lose their reasons, since executed tables apply the rules without stating them. Credit's Q6 behaved the same way.
- **What this says about curation:** rules applied upstream do the work, but they decide what the data can still answer. A store that keeps the records it merged, and the rules it ran, answers more.

## 4 November 2026: ownership paths, reading against querying, Sonnet

`results/credit_paths/2026-11-04-2022-sonnet/` (reading, 5 repeats) and `2026-11-04-2024-sonnet-query/` (querying, 3 repeats): the 300-issuer data on the version 2 rules, plus six groups four to six levels deep and 13 path questions (Q49 to Q61). Three query sessions first failed on format: Sonnet wrote its queries as tool-call markup, which the runner didn't see. The runner now reads that markup and asks once for the right format. The three sessions were rerun, and the failed ones are kept in `failed/`.

| | All 61 questions | Path questions | Path score in each session |
|---|---|---|---|
| `csv` | 81% | 77% | 69, 85, 62, 85, 85 |
| `csv+markdown` | 95% | 100% | 100 in all five |
| `executed` | 94% | 97% | 92, 100, 92, 100, 100 |
| `csv+axioms` | 93% | 97% | 92, 100, 100, 92, 100 |
| `sql` | 73% | 44% | 69, 31, 31 |
| `sql+markdown` | 85% | 71% | 12, 100, 100 |
| `sparql` | 65% | 33% | 31, 54, 15 |
| `sparql+ontology` | 94% | 92% | 100, 85, 92 |
| `sql+executed` (with an `ancestors` table) | 93% | 100% | 100 in all three |
| `sparql+axioms` (after the SHACL rules) | 81% | 82% | 100, 46, 100 |

- **Without definitions, a graph doesn't help with paths:** `sparql` scores 33% on them and `sql` 44%. The chain runs through a RESEARCH record, and a test record sits inside a group. Neither store says what those records mean, so neither model can walk the chain correctly.
- **With definitions, both stores mostly get there.** `sparql+ontology` is the steadiest querying condition (85 to 100). `sql+markdown` scored 100 twice, but one session stopped after two rounds and guessed (12). `sparql+axioms` also scored 100 twice, with one session that got empty results (46). With three repeats, one bad session moves a path score by about 30 points, so the SQL and SPARQL averages don't separate them.
- **Precomputing the closure wins:** with an `ancestors` table, SQL gets every path question right in every session. The graph's advantage is that it can follow links of any depth at query time. Once the rules have computed the chains, a table does as well.
- **Reading beats querying at this size:** with the definitions, reading the 100 KB of CSV gets all 13 path questions right in all five sessions. Querying pays off when the data is too big to read, not because it's a graph.

## 5 November 2026: every reading condition, one run per model and domain

`results/credit/2026-11-05-1227-sonnet/` and `2026-11-05-1233-haiku/` (credit, version 2, R1 to R10), and `results/research/2026-11-05-1234-sonnet/` and `2026-11-05-1235-haiku/` (research, R1 to R6 and R10). Until now each condition's figures came from whichever run had asked it, some on credit's version 1 rules. These runs ask every condition together, so each table comes from one run per model, on the current keys.

| Condition | Credit, Sonnet | Credit, Haiku | Research, Sonnet | Research, Haiku |
|---|---|---|---|---|
| `csv` | 84% | 78% | 57% | 45% |
| `rdf` | 85% (+1) | 72% (−6, −12 to −1) | 47% (−9, −17 to −3) | 43% (−3) |
| `csv+padding` | 84% (+0) | 76% (−2) | 57% (+0) | 44% (−1) |
| `csv+markdown` | 100% (+16) | 98% (+20) | 98% (+41) | 99% (+53) |
| `csv+ontology` | 99% (+15) | 99% (+21) | 98% (+41) | 96% (+51) |
| `rdf+ontology` | 100% (+16) | 97% (+19) | 98% (+41) | 98% (+53) |
| `csv+neutral` | 100% (+16) | 100% (+22) | | |
| `csv+axioms` | 99% (+15) | 99% (+21) | | |
| `csv+axioms+markdown` | 100% (+16) | 99% (+21) | | |
| `executed` | 99% (+15) | 97% (+19) | 90% (+34) | 92% (+46) |

- **The earlier findings hold in one run.** Every form of the definitions reaches 96–100%, Markdown matches Turtle, and the decoy stays within 2 points of `csv`.
- **RDF alone can cost.** It never beats the CSV, and twice the loss has an interval below zero: Haiku on credit (−6) and Sonnet on research (−9).
- **The decoy doesn't hurt Haiku after all.** An earlier credit run had it at −5 with an interval below zero. Here it's −2 (−6 to +1).
- **Executed rules now match the definitions on credit:** +15 and +19, where version 1 gave +9. On research they're still 6 to 9 points short: versions (Q2, Q20), counting shares (Q12, Q13), the ultimate parent (Q46) and the "why" questions (Q47, Q48).
- **The slant is still there.** Haiku gets Q10 right in 2 of 5 repeats with `csv+ontology`, 1 of 5 with `csv+markdown` and 3 of 5 with `csv+axioms+markdown`, against 5 of 5 with `csv+neutral` and with `csv+axioms`. Sonnet slips in 2 of 5 with `csv+ontology`.
- **Logic and executed tables say what, not why.** Q6 is mostly partial with `csv+axioms` and `executed`, and right with the prose.

## 5 November 2026: ownership paths, querying with five repeats, Sonnet

`results/credit_paths/2026-11-05-1515-sonnet-query/`: the six querying conditions again, with five repeats instead of three, since one session moved a path score by about 30 points. One session was refused by the API ("safeguards flagged this message") and redone on resume.

| | All 61 questions | Path questions | Path score in each session |
|---|---|---|---|
| `sql` | 75% | 60% | 38, 62, 62, 69, 69 |
| `sql+markdown` | 98% | 100% | 100 in all five |
| `sql+executed` | 96% | 100% | 100 in all five |
| `sparql` | 59% | 32% | 46, 62, 0, 31, 23 |
| `sparql+ontology` | 77% | 42% | 4, 8, 46, 77, 77 |
| `sparql+axioms` | 84% | 77% | 100, 100, 100, 8, 77 |

- **The order of the stores reverses.** With three repeats, `sparql+ontology` was the steadiest querying condition (92% on paths) and `sql+markdown` 71%. With five, `sql+markdown` gets every path right in every session and `sparql+ontology` 42%. Against `sql`, `sparql+ontology` is now +2 points overall (−5 to +10), and `sql+markdown` +23 (+13 to +32).
- **The SPARQL sessions fail on the store as well as the meaning.** In `sparql+ontology`, rdflib stopped up to three of the model's large queries a session after 60 seconds, and in the worst session it answered after six rounds with most path answers empty. `sparql+axioms` used all eight rounds in four sessions of five. No SQL query timed out. Plain `sparql` had no timeouts and still scored lowest, so without the definitions the meaning is missing too.
- **Precomputed chains still win:** `sql+executed` gets every path right in every session.
- **So the graph's advantage doesn't show here, at any level of meaning.** With rdflib as the store, SPARQL is slower and less steady than SQL. A faster triple store could change that, and is worth trying before concluding against graphs.

## 5 November 2026: ownership paths, SPARQL on GraphDB, Sonnet

`results/credit_paths/2026-11-05-1819-sonnet-query-graphdb/`: the three SPARQL conditions again, on a local GraphDB (free edition, 11.5) instead of rdflib, five repeats. Each session loads exactly the triples rdflib holds, into a repository with no inference, so only the engine changes. Paused once by the Claude usage limit and resumed.

| | rdflib: all / paths | GraphDB: all / paths | GraphDB path score in each session | GraphDB against rdflib |
|---|---|---|---|---|
| `sparql` | 59% / 32% | 68% / 40% | 23, 38, 38, 38, 62 | +9 (+6 to +13) |
| `sparql+ontology` | 77% / 42% | 82% / 60% | 85, 85, 0, 100, 31 | +5 (+1 to +10) |
| `sparql+axioms` | 84% / 77% | 79% / 68% | 92, 0, 85, 92, 69 | −5 (−8 to −1) |

- **No query timed out on GraphDB.** The seven queries rdflib stopped at 60 seconds in `sparql+ontology` finish there in under 3.
- **A fast engine helps a little, not much.** +9 and +5 points, and −5 over the graph after the rules. `sql+markdown`, at 98% overall and 100% on paths, stays well ahead.
- **The poor SPARQL sessions come from the model, not the store.** In `sparql+ontology` run 3 it stopped after three of eight rounds, saying later results were malformed when no query had failed, and left every path answer empty. In run 5 it reran the same entity query in several rounds and ran out before the paths. In `sparql+axioms` run 2 it spent all eight rounds fetching whole classes 60 rows at a time and saw only part of the 540 entities.
- **So the gap between SQL and SPARQL here is how the model works in the query loop.** With SQL it asks for what each question needs. With SPARQL it more often pages through the graph first. More rounds, or a larger row limit, might close the gap, if SQL gets the same.


## 6 November 2026: credit at 300 issuers, version 2, every reading condition, Sonnet and Haiku

`results/credit_300/2026-11-05-2135-sonnet/` and `2026-11-05-2135-haiku/`: R1 to R10, five repeats, on the 300-issuer data rebuilt on the version 2 rules. One Haiku session (`csv+neutral` run 2) came back with only the second half of its answer and was asked again on resume.

| Condition | Sonnet | Haiku |
|---|---|---|
| `csv` | 81% | 74% |
| `rdf` | 77% (−4, −8 to −0) | 63% (−10, −17 to −4) |
| `csv+padding` | 81% (+0) | 69% (−4, −8 to −1) |
| `csv+markdown` | 93% (+12) | 87% (+13) |
| `csv+ontology` | 92% (+11) | 89% (+15) |
| `rdf+ontology` | 94% (+13) | 83% (+10) |
| `csv+neutral` | 95% (+14) | 88% (+15) |
| `csv+axioms` | 92% (+11) | 88% (+14) |
| `csv+axioms+markdown` | 94% (+12) | 85% (+11) |
| `executed` | 94% (+13) | 91% (+17) |

- **The gain from the definitions holds at scale:** +11 to +14 for Sonnet and +10 to +17 for Haiku, about what it is on the base data.
- **The ceiling drops:** 92–95% for Sonnet and 83–91% for Haiku with the definitions, against 96–100% for both on the base data. So the two models no longer end level. Most of the loss is on long lists of 28 to 31 issuers (Q7, Q18, Q19), graded strictly.
- **RDF alone costs more here:** −4 for Sonnet and −10 for Haiku. The decoy costs Haiku 4 points (−8 to −1).
- **Q18's key is too narrow.** `build_questions.py` reads the Watch from the foreign-currency issuer rating only. E1019 and E1059 are on Watch Negative on their local-currency rating, and every session lists them, so Q18 is wrong in every condition for both models. Counting both bases would make the key 32 issuers here and in `credit_paths`, and leave the base data's unchanged. Q19, the Negative outlooks, is the same either way.

## 6 November 2026: credit at 300 issuers, version 2, querying, Sonnet

`results/credit_300/2026-11-06-0041-sonnet-query/`: the six querying conditions, five repeats, rdflib as the store. One `sparql+axioms` session was refused by the API ("safeguards flagged this message") and asked again on resume.

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading (same data, Sonnet) | `csv` 81% | `csv+markdown` 93% | `executed` 94% |
| SQL | `sql` 80% | `sql+markdown` 97% (+16, +6 to +28) | `sql+executed` 97% (+16) |
| SPARQL | `sparql` 76% (−4, −10 to +2) | `sparql+ontology` 95% (+15) | `sparql+axioms` 87% (+6, −2 to +16) |

- **The version 1 picture holds.** There it was 86% and 96% for SQL, 79% and 95% for SPARQL.
- **With the definitions, querying edges out reading:** 95–97% against 93%, on the long lists: 83% of them are entirely right with `sql+markdown`, against 60% with `csv+markdown` (mean F1 99% and 98%).
- **SPARQL is no better than SQL on joins,** with or without the definitions.
- **`sparql+axioms` trails the ontology by 8 points.** It answers Q7 with an empty list in every session.
- **Q18 stays wrong** in every condition but `sql` (3 of 5) and `sparql` (1 of 5): the narrow key (backlog #22). The conditions with definitions list the two local-currency Watches.
- 17 of 578 queries failed and 3 timed out, all three in `sparql+ontology`.

## 6 November 2026: research at 850 works, reading, Sonnet and Haiku

`results/research_850/2026-11-06-0206-sonnet/` and `2026-11-06-0206-haiku/`: `csv`, `csv+padding`, `csv+markdown`, `csv+ontology` and `executed`, five repeats, on the research data at ten times the size (850 works, built by `domains/research/scale.py 850`). The prompts are 110 to 160 KB, against 19 to 39 KB on the base data. `rdf` and `rdf+ontology` are left out: the Turtle alone is about 770 KB.

| Condition | Sonnet | Haiku | Base data: Sonnet, Haiku |
|---|---|---|---|
| `csv` | 42% | 21% | 57%, 45% |
| `csv+padding` | 42% (+0) | 30% (+9, +4 to +15) | 57%, 44% |
| `csv+markdown` | 87% (+45) | 43% (+22) | 98%, 99% |
| `csv+ontology` | 89% (+47) | 49% (+28) | 98%, 96% |
| `executed` | 79% (+37) | 69% (+48) | 90%, 92% |

- **Sonnet keeps the meaning and loses the arithmetic.** With the definitions, it gets 97% of the local-rule questions (Q33 to Q46, Q48), as on the base data, but 82–85% of the general ones (Q1 to Q32, Q47), against 97%. The misses are counts and roll-ups over the whole data: Q9, Q10, Q11, Q14, Q16, Q19 and Q21.
- **Q1:** with the definitions, Sonnet answers 1 person in 9 of 10 sessions, reading the question as the three name forms. The six records with those names carry three ORCIDs, and the key says 3. Without the definitions it answers 3.
- **Haiku answers only part of the questions in 5 of 25 sessions** (`csv` run 4, `csv+markdown` runs 1, 2 and 4, `csv+ontology` run 1), three of them saying so ("Q9–Q48: not yet answered… I'll continue"). The answers are complete as sent, so they're graded as they are. On the sessions that answered everything: `csv` 23%, `csv+ontology` 58%, `csv+markdown` 74% (two sessions).
- **`executed` is Haiku's best condition here,** at 69%: the merging and roll-ups are already done, and its prompt is the smallest.
- **So at this size, reading starts to fail on work, not meaning.** The definitions still carry the local rules, but the model has to tally too much by hand. That's where querying should help: the querying run on this data is next.

## 6 November 2026: research at 850 works, querying, Sonnet

`results/research_850/2026-11-06-0519-sonnet-query/`: `sql`, `sql+markdown`, `sql+executed`, `sparql` and `sparql+ontology`, five repeats, rdflib as the store. The research domain has no axioms, so no `sparql+axioms`. The first querying run on research.

| | No definitions | With the definitions | Rules executed |
|---|---|---|---|
| Reading (same data, Sonnet) | `csv` 42% | `csv+markdown` 87% | `executed` 79% |
| SQL | `sql` 38% | `sql+markdown` 80% (+42) | `sql+executed` 92% (+54) |
| SPARQL | `sparql` 30% (−7, −13 to −2) | `sparql+ontology` 85% (+48) | |

Score in each session: `sql` 33–42, `sql+markdown` 97, 84, 41, 80, 97, `sql+executed` 90–94, `sparql` 15–38, `sparql+ontology` 74, 73, 95, 93, 91.

- **Querying doesn't recover what reading lost at this size.** On the general questions (Q1 to Q32, Q47), `sql+markdown` gets 75% and `sparql+ontology` 80%, against 82–85% reading. The local rules stay right (91% and 96%). Q1 is still read as the three name forms.
- **Querying over executed tables is the best condition:** 92% and steady, against 79% reading the same tables. The rules have merged the records and rolled up the hierarchy, so each count is a simple query.
- **The definitions alone make querying unsteady.** `sql+markdown` run 3 stopped after four rounds and answered many counts from a partial view: 41%.
- **Without definitions, querying is no better than reading:** 38% and 30%, against 42%.
- 34 of 643 queries failed and 5 timed out, all on rdflib.
- **So the case for querying, at this size, rests on the rules having been run.**
