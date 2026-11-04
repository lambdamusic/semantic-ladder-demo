# Results log

What each run showed, newest last. The reports in `results/` hold the numbers; this file
holds what they mean, and what changed because of them.

## 4 November 2026: baseline, ten questions

`results/credit/2026-11-04-1526-sonnet/`, Sonnet, four conditions, five repeats.

- **No condition stands out:** accuracy ranged from 93% (`rdf`) to 99% (`rdf+ontology`), and all the intervals overlap. Only `rdf+ontology` gained clearly against `csv`: +4 points (+0 to +12), nearly all on Q6.
- **The first round's grader added the noise:** code grading and the LLM grader agreed on 170 of 180 answers. Nine of the ten disagreements were the LLM grader giving partial credit to right answers; under code grading, only one question in one condition varied across repeats.
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
