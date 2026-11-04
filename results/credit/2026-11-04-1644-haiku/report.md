# credit: claude:haiku, 2026-11-04 16:44

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **79%** | 68% to 89% | 9 of 48 |
| `rdf` | **75%** | 64% to 85% | 9 of 48 |
| `rdf+ontology` | **97%** | 93% to 100% | 3 of 48 |
| `csv+ontology` | **98%** | 94% to 100% | 0 of 48 |
| `csv+markdown` | **99%** | 98% to 100% | 1 of 48 |
| `csv+padding` | **74%** | 62% to 85% | 6 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -4 points | -9 to +1 |
| `rdf+ontology` | +18 points | +8 to +29 |
| `csv+ontology` | +19 points | +8 to +31 |
| `csv+markdown` | +20 points | +11 to +31 |
| `csv+padding` | -5 points | -10 to -1 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` |
|---|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ |
| Q5 | code | ✅ ✅ ✅ 🟡 ✅ | 🟡 🟡 ✅ 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 🟡 🟡 🟡 |
| Q6 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ✅ ❌ ❌ ✅ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ 🟡 ✅ | 🟡 🟡 ✅ 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 🟡 🟡 🟡 |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q42 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ❌ ❌ |
| Q44 | code | ✅ ❌ ✅ ❌ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ✅ |
| Q45 | code | ✅ ❌ ❌ ❌ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ✅ |
| Q47 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q48 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |

## Lists, with partial credit

The 7 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 83% | 96% |
| `rdf` | 86% | 97% |
| `rdf+ontology` | 97% | 99% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 100% | 100% |
| `csv+padding` | 86% | 97% |

**The checklist grader agreed with itself** on 30 of 30 answers graded twice.

## Why each miss was marked

**Q4.** What is Northwind Holdings' current outlook?

- `csv+padding` run 5: outlook: expected positive, got STA

**Q5.** Whose credit risk does a holder of the Northwind Finance 2030 notes take, and how is it rated?

- `csv` run 4: risk_of: expected E02, got E04
- `rdf` run 1: risk_of: expected E02, got E04
- `rdf` run 2: risk_of: expected E02, got E04
- `rdf` run 4: risk_of: expected E02, got E04
- `rdf` run 5: risk_of: expected E02, got E04
- `csv+padding` run 2: risk_of: expected E02, got E04
- `csv+padding` run 3: risk_of: expected E02, got E04
- `csv+padding` run 4: risk_of: expected E02, got E04
- `csv+padding` run 5: risk_of: expected E02, got E04

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `csv` run 1: Notes FC matches the sovereign BB and is consistent with a ceiling cap, but does not name the Country Ceiling as the cause or state it caps FC and not LC ratings.
- `csv` run 2: Identifies the BB country ceiling as the likely cause but hedges it as inference and never states that the ceiling caps foreign-currency but not local-currency ratings.
- `csv` run 3: Identifies the BB country ceiling as consistent with the FC rating but hedges and doesn't state it as the cause or that it caps FC but not LC ratings.
- `csv` run 4: Notes FC rating equals the BB country ceiling, consistent with a cap, but hedges that it isn't stated and doesn't say the ceiling caps FC and not LC ratings.
- `csv` run 5: Names the BB country ceiling as the cause, but never says it caps foreign-currency ratings and not local-currency ones; it only notes the ceiling sits below the LC rating.
- `rdf` run 1: Notes the BB country ceiling matches the foreign-currency rating and may be the cap, but hedges and does not state it as the cause or that it caps only foreign-currency ratings.
- `rdf` run 2: Notes the sovereign's BB CC-type rating matches the FC rating and may be a ceiling, but hedges and doesn't state the ceiling as the cause or that it caps FC and not LC.
- `rdf` run 3: Points to the BB country ceiling record (A12) as a possible cap but hedges and doesn't state that it caps foreign-currency and not local-currency ratings.
- `rdf` run 4: Identifies the BB country ceiling as matching the FC rating, but doesn't state that the ceiling caps foreign-currency (not local-currency) ratings, and hedges that the cause isn't stated.
- `rdf` run 5: Identifies the pattern of FC rating equal to the BB country ceiling with LC above it, but hedges that the data doesn't state the cause instead of asserting the ceiling caps FC and not LC ratings.
- `csv+padding` run 1: Notes FC rating equals the BB country ceiling and is consistent with a cap, but hedges that the data doesn't state it and never says the ceiling caps FC and not LC ratings.
- `csv+padding` run 2: Links FC rating BB to the BB country ceiling as a possible cause, but hedges and doesn't state that the ceiling caps foreign-currency but not local-currency ratings.
- `csv+padding` run 3: Links the BB FC rating to the BB country ceiling as consistent with capping, but hedges that the data doesn't state it and never says the ceiling applies to FC and not LC.
- `csv+padding` run 4: Identifies the BB country ceiling as consistent with the FC rating but hedges it as an inference, and does not state that the ceiling caps foreign-currency but not local-currency ratings.
- `csv+padding` run 5: Identifies the Valdoria (BB) country ceiling as matching the FC rating and consistent with a cap, but hedges that the cause is unconfirmed and does not state that the ceiling caps FC and not LC ratings.

**Q7.** Which issuers were downgraded in 2026?

- `csv` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv+padding` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv+padding` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv+padding` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv+padding` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv+padding` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']

**Q9.** As of 1 October 2026, how many distinct issuers hold an issuer rating?

- `csv` run 2: count: expected 12, got 13
- `csv` run 3: count: expected 12, got 13
- `csv` run 5: count: expected 12, got 13
- `rdf` run 1: count: expected 12, got 13
- `rdf` run 2: count: expected 12, got 13
- `rdf` run 4: count: expected 12, got 11
- `rdf` run 5: count: expected 12, got 13
- `rdf+ontology` run 1: count: expected 12, got 11
- `rdf+ontology` run 2: count: expected 12, got 11
- `rdf+ontology` run 3: count: expected 12, got 11
- `rdf+ontology` run 5: count: expected 12, got 11
- `csv+padding` run 1: count: expected 12, got 13
- `csv+padding` run 2: count: expected 12, got 13
- `csv+padding` run 3: count: expected 12, got 13
- `csv+padding` run 4: count: expected 12, got 13
- `csv+padding` run 5: count: expected 12, got 13

**Q10.** Is Valdoria Telecom investment grade?

- `rdf+ontology` run 1: investment_grade: expected depends, got no
- `rdf+ontology` run 3: investment_grade: expected depends, got no
- `csv+ontology` run 1: investment_grade: expected depends, got no
- `csv+ontology` run 2: investment_grade: expected depends, got no
- `csv+ontology` run 3: investment_grade: expected depends, got no
- `csv+ontology` run 4: investment_grade: expected depends, got no
- `csv+ontology` run 5: investment_grade: expected depends, got no
- `csv+markdown` run 3: investment_grade: expected depends, got no
- `csv+markdown` run 5: investment_grade: expected depends, got no

**Q25.** How many instruments held an investment-grade rating on 1 October 2026?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6
- `rdf` run 1: count: expected 5, got 6
- `rdf` run 3: count: expected 5, got 6
- `rdf` run 4: count: expected 5, got 6
- `rdf` run 5: count: expected 5, got 6
- `csv+padding` run 1: count: expected 5, got 6
- `csv+padding` run 2: count: expected 5, got 6
- `csv+padding` run 3: count: expected 5, got 6
- `csv+padding` run 4: count: expected 5, got 6
- `csv+padding` run 5: count: expected 5, got 6

**Q27.** How is Corvenia Power's 2032 note rated?

- `rdf` run 2: rating: expected A-, got none
- `rdf` run 3: rating: expected A-, got none

**Q29.** What is the Republic of Valdoria's issuer rating?

- `csv` run 1: rating: expected none, got BB

**Q30.** Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?

- `csv` run 1: entities: expected ['E05', 'E15'], got ['E05']
- `rdf+ontology` run 5: entities: expected ['E05', 'E15'], got ['E05']

**Q31.** Did any company have a foreign-currency issuer rating above its country's ceiling on 1 October 2026?

- `csv` run 1: any: expected no, got yes

**Q33.** Whose credit risk does a holder of the Halden Leasing 2028 notes take, and how is it rated?

- `csv` run 4: risk_of: expected E10, got E11
- `rdf` run 1: risk_of: expected E10, got E11
- `rdf` run 2: risk_of: expected E10, got E11
- `rdf` run 4: risk_of: expected E10, got E11
- `rdf` run 5: risk_of: expected E10, got E11
- `csv+padding` run 2: risk_of: expected E10, got E11
- `csv+padding` run 3: risk_of: expected E10, got E11
- `csv+padding` run 4: risk_of: expected E10, got E11
- `csv+padding` run 5: risk_of: expected E10, got E11

**Q37.** How many distinct legal entities does the data describe?

- `csv` run 1: count: expected 16, got 17
- `csv` run 2: count: expected 16, got 17
- `csv` run 3: count: expected 16, got 17
- `csv` run 4: count: expected 16, got 17
- `csv` run 5: count: expected 16, got 17
- `rdf` run 1: count: expected 16, got 17
- `rdf` run 2: count: expected 16, got 17
- `rdf` run 3: count: expected 16, got 17
- `rdf` run 4: count: expected 16, got 17
- `rdf` run 5: count: expected 16, got 17
- `csv+padding` run 1: count: expected 16, got 17
- `csv+padding` run 2: count: expected 16, got 17
- `csv+padding` run 3: count: expected 16, got 17
- `csv+padding` run 4: count: expected 16, got 17
- `csv+padding` run 5: count: expected 16, got 17

**Q40.** How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6
- `rdf` run 1: count: expected 5, got 6
- `rdf` run 2: count: expected 5, got 6
- `rdf` run 3: count: expected 5, got 6
- `rdf` run 4: count: expected 5, got 6
- `rdf` run 5: count: expected 5, got 6
- `csv+padding` run 1: count: expected 5, got 6
- `csv+padding` run 2: count: expected 5, got 6
- `csv+padding` run 3: count: expected 5, got 6
- `csv+padding` run 4: count: expected 5, got 6
- `csv+padding` run 5: count: expected 5, got 6

**Q41.** What is Brindle Capital's current rating?

- `csv` run 1: rating: expected none, got BB+
- `csv` run 2: rating: expected none, got BB+
- `csv` run 3: rating: expected none, got BB+
- `csv` run 4: rating: expected none, got BB+
- `csv` run 5: rating: expected none, got BB+
- `rdf` run 1: rating: expected none, got BB+
- `rdf` run 2: rating: expected none, got BB+
- `rdf` run 3: rating: expected none, got BB+
- `rdf` run 4: rating: expected none, got BB+
- `rdf` run 5: rating: expected none, got BB+
- `csv+padding` run 1: rating: expected none, got BB+
- `csv+padding` run 2: rating: expected none, got BB+
- `csv+padding` run 3: rating: expected none, got BB+
- `csv+padding` run 4: rating: expected none, got BB+
- `csv+padding` run 5: rating: expected none, got BB+

**Q43.** How many distinct entities are domiciled in Luxembourg (LU)?

- `csv` run 1: count: expected 0, got 1
- `rdf` run 1: count: expected 0, got 1
- `rdf` run 2: count: expected 0, got 1
- `rdf` run 3: count: expected 0, got 1
- `rdf` run 4: count: expected 0, got 1
- `rdf` run 5: count: expected 0, got 1
- `csv+padding` run 1: count: expected 0, got 1
- `csv+padding` run 3: count: expected 0, got 1
- `csv+padding` run 4: count: expected 0, got 1
- `csv+padding` run 5: count: expected 0, got 1

**Q44.** Is Valdoria Telecom's 2027 note a local-currency obligation?

- `csv` run 2: local_currency: expected yes, got depends
- `csv` run 4: local_currency: expected yes, got depends
- `rdf` run 1: local_currency: expected yes, got depends
- `rdf` run 2: local_currency: expected yes, got depends
- `rdf` run 3: local_currency: expected yes, got depends
- `rdf` run 4: local_currency: expected yes, got depends
- `csv+padding` run 1: local_currency: expected yes, got depends
- `csv+padding` run 2: local_currency: expected yes, got depends
- `csv+padding` run 3: local_currency: expected yes, got depends
- `csv+padding` run 4: local_currency: expected yes, got depends

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `csv` run 2: above_ceiling: expected no, got depends
- `csv` run 3: above_ceiling: expected no, got yes
- `csv` run 4: above_ceiling: expected no, got depends
- `rdf` run 2: above_ceiling: expected no, got depends
- `rdf` run 3: above_ceiling: expected no, got depends
- `rdf` run 4: above_ceiling: expected no, got depends
- `rdf` run 5: above_ceiling: expected no, got depends
- `csv+padding` run 1: above_ceiling: expected no, got depends
- `csv+padding` run 2: above_ceiling: expected no, got depends
- `csv+padding` run 3: above_ceiling: expected no, got depends
- `csv+padding` run 4: above_ceiling: expected no, got depends
- `csv+padding` run 5: above_ceiling: expected no, got depends

**Q46.** Does Halden Leasing have an issuer rating?

- `rdf` run 4: issuer_rating: expected no, got depends
- `csv+padding` run 3: issuer_rating: expected no, got depends
- `csv+padding` run 4: issuer_rating: expected no, got depends

**Q47.** How is Corvenia Power's 2034 note rated?

- `csv` run 1: rating: expected none, got A
- `csv` run 2: rating: expected none, got A
- `csv` run 3: rating: expected none, got A
- `csv` run 4: rating: expected none, got A
- `csv` run 5: rating: expected none, got A
- `rdf` run 1: rating: expected none, got A
- `rdf` run 2: rating: expected none, got A
- `rdf` run 3: rating: expected none, got A
- `rdf` run 4: rating: expected none, got A
- `rdf` run 5: rating: expected none, got A
- `csv+padding` run 1: rating: expected none, got A
- `csv+padding` run 2: rating: expected none, got A
- `csv+padding` run 3: rating: expected none, got A
- `csv+padding` run 4: rating: expected none, got A
- `csv+padding` run 5: rating: expected none, got A

**Q48.** How many instruments held a rating on 1 October 2026?

- `csv` run 1: count: expected 7, got 8
- `csv` run 2: count: expected 7, got 8
- `csv` run 3: count: expected 7, got 8
- `csv` run 4: count: expected 7, got 8
- `csv` run 5: count: expected 7, got 8
- `rdf` run 1: count: expected 7, got 8
- `rdf` run 3: count: expected 7, got 8
- `rdf` run 4: count: expected 7, got 8
- `rdf` run 5: count: expected 7, got 8
- `csv+padding` run 1: count: expected 7, got 8
- `csv+padding` run 2: count: expected 7, got 8
- `csv+padding` run 3: count: expected 7, got 8
- `csv+padding` run 4: count: expected 7, got 8
- `csv+padding` run 5: count: expected 7, got 8

