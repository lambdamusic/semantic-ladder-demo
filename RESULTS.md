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
