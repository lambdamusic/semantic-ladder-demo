# research: claude:sonnet, 2026-11-04 20:10

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **56%** | 42% to 68% | 10 of 48 |
| `rdf` | **50%** | 36% to 64% | 5 of 48 |
| `rdf+ontology` | **98%** | 95% to 100% | 3 of 48 |
| `csv+ontology` | **97%** | 92% to 100% | 2 of 48 |
| `csv+markdown` | **97%** | 92% to 100% | 1 of 48 |
| `csv+padding` | **55%** | 41% to 68% | 5 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -6 points | -14 to +2 |
| `rdf+ontology` | +42 points | +30 to +55 |
| `csv+ontology` | +41 points | +29 to +54 |
| `csv+markdown` | +41 points | +29 to +55 |
| `csv+padding` | -1 points | -4 to +1 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` |
|---|---|---|---|---|---|---|---|
| Q1 | code | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q11 | code | ✅ ✅ ✅ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ 🟡 ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q26 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ❌ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ✅ |
| Q32 | code | ✅ ❌ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q35 | code | ❌ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q36 | code | ❌ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q40 | code | ❌ ✅ ✅ ✅ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ❌ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q47 | llm | 🟡 🟡 🟡 ✅ 🟡 | 🟡 ✅ 🟡 ✅ 🟡 | ✅ 🟡 🟡 ✅ ✅ | ✅ 🟡 ✅ 🟡 ✅ | 🟡 ✅ 🟡 ✅ 🟡 | 🟡 🟡 ✅ ✅ ✅ |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 60% | 95% |
| `rdf` | 50% | 94% |
| `rdf+ontology` | 100% | 100% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 100% | 100% |
| `csv+padding` | 60% | 95% |

**The checklist grader agreed with itself** on 53 of 60 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf+ontology` run 2: count: expected 2, got 1
- `rdf+ontology` run 3: count: expected 2, got 1
- `rdf+ontology` run 4: count: expected 2, got 1
- `csv+ontology` run 1: count: expected 2, got 1
- `csv+ontology` run 2: count: expected 2, got 1
- `csv+ontology` run 3: count: expected 2, got 1
- `csv+ontology` run 4: count: expected 2, got 1
- `csv+ontology` run 5: count: expected 2, got 1
- `csv+markdown` run 1: count: expected 2, got 1
- `csv+markdown` run 2: count: expected 2, got 1
- `csv+markdown` run 3: count: expected 2, got 1
- `csv+markdown` run 4: count: expected 2, got 1
- `csv+markdown` run 5: count: expected 2, got 1
- `csv+padding` run 1: count: expected 2, got 1
- `csv+padding` run 2: count: expected 2, got 1
- `csv+padding` run 3: count: expected 2, got 1
- `csv+padding` run 4: count: expected 2, got 1
- `csv+padding` run 5: count: expected 2, got 1

**Q7.** How many research works has Mara Ellison authored?

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

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 8, got 12
- `csv` run 2: count: expected 8, got 12
- `csv` run 3: count: expected 8, got 12
- `csv` run 4: count: expected 8, got 12
- `csv` run 5: count: expected 8, got 12
- `rdf` run 1: count: expected 8, got 12
- `rdf` run 2: count: expected 8, got 12
- `rdf` run 3: count: expected 8, got 12
- `rdf` run 4: count: expected 8, got 12
- `rdf` run 5: count: expected 8, got 12
- `csv+padding` run 1: count: expected 8, got 12
- `csv+padding` run 2: count: expected 8, got 12
- `csv+padding` run 3: count: expected 8, got 12
- `csv+padding` run 4: count: expected 8, got 12
- `csv+padding` run 5: count: expected 8, got 12

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 12, got 16
- `csv` run 2: count: expected 12, got 16
- `csv` run 3: count: expected 12, got 16
- `csv` run 4: count: expected 12, got 16
- `csv` run 5: count: expected 12, got 16
- `rdf` run 1: count: expected 12, got 16
- `rdf` run 2: count: expected 12, got 16
- `rdf` run 3: count: expected 12, got 16
- `rdf` run 4: count: expected 12, got 16
- `rdf` run 5: count: expected 12, got 16
- `csv+padding` run 1: count: expected 12, got 16
- `csv+padding` run 2: count: expected 12, got 16
- `csv+padding` run 3: count: expected 12, got 16
- `csv+padding` run 4: count: expected 12, got 16
- `csv+padding` run 5: count: expected 12, got 16

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 4: count: expected 6, got 7
- `rdf` run 1: count: expected 6, got 9
- `rdf` run 2: count: expected 6, got 9
- `rdf` run 3: count: expected 6, got 9
- `rdf` run 4: count: expected 6, got 9
- `rdf` run 5: count: expected 6, got 8

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `csv` run 1: count: expected 4, got 3

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `rdf` run 1: count: expected 10, got 11
- `rdf` run 2: count: expected 10, got 11
- `rdf` run 3: count: expected 10, got 11
- `rdf` run 4: count: expected 10, got 11
- `rdf` run 5: count: expected 10, got 11

**Q22.** Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?

- `csv+padding` run 4: more_in_total: expected W30, got W31

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4
- `rdf` run 1: count: expected 3, got 4
- `rdf` run 2: count: expected 3, got 4
- `rdf` run 3: count: expected 3, got 4
- `rdf` run 4: count: expected 3, got 4
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got 4
- `csv+padding` run 4: count: expected 3, got 4
- `csv+padding` run 5: count: expected 3, got 4

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 1: count: expected 6, got 7
- `csv` run 2: count: expected 6, got 7
- `csv` run 3: count: expected 6, got 7
- `csv` run 4: count: expected 6, got 7
- `csv` run 5: count: expected 6, got 7
- `rdf` run 1: count: expected 6, got 10
- `rdf` run 2: count: expected 6, got 10
- `rdf` run 3: count: expected 6, got 10
- `rdf` run 4: count: expected 6, got 10
- `rdf` run 5: count: expected 6, got 9
- `csv+padding` run 1: count: expected 6, got 7
- `csv+padding` run 2: count: expected 6, got 7
- `csv+padding` run 3: count: expected 6, got 7
- `csv+padding` run 4: count: expected 6, got 7
- `csv+padding` run 5: count: expected 6, got 7

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 1: counts: expected no, got yes
- `csv` run 2: counts: expected no, got yes
- `csv` run 3: counts: expected no, got yes
- `csv` run 4: counts: expected no, got yes
- `csv` run 5: counts: expected no, got yes
- `rdf` run 1: counts: expected no, got yes
- `rdf` run 2: counts: expected no, got depends
- `rdf` run 3: counts: expected no, got yes
- `rdf` run 4: counts: expected no, got depends
- `csv+padding` run 1: counts: expected no, got depends
- `csv+padding` run 2: counts: expected no, got yes
- `csv+padding` run 3: counts: expected no, got yes
- `csv+padding` run 4: counts: expected no, got yes
- `csv+padding` run 5: counts: expected no, got yes

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `csv` run 2: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6
- `rdf` run 1: count: expected 5, got 6
- `rdf` run 2: count: expected 5, got 6
- `rdf` run 3: count: expected 5, got 6
- `rdf` run 4: count: expected 5, got 6
- `rdf` run 5: count: expected 5, got 6
- `csv+padding` run 1: count: expected 5, got 6
- `csv+padding` run 2: count: expected 5, got 6

**Q33.** Which of Kesting University's research works has the most citations?

- `rdf` run 1: work: expected W20, got W22
- `rdf` run 2: work: expected W20, got W22
- `rdf` run 3: work: expected W20, got W22
- `rdf` run 4: work: expected W20, got W22
- `rdf` run 5: work: expected W20, got W22

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 1: count: expected 3, got 2
- `csv` run 2: count: expected 3, got 2
- `csv` run 3: count: expected 3, got 2
- `csv` run 5: count: expected 3, got 2
- `rdf` run 1: count: expected 3, got 5
- `rdf` run 2: count: expected 3, got 5
- `rdf` run 3: count: expected 3, got 5
- `rdf` run 4: count: expected 3, got 5
- `rdf` run 5: count: expected 3, got 5
- `csv+padding` run 1: count: expected 3, got 2
- `csv+padding` run 2: count: expected 3, got 2
- `csv+padding` run 3: count: expected 3, got 2
- `csv+padding` run 4: count: expected 3, got 2
- `csv+padding` run 5: count: expected 3, got 1

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf` run 1: count: expected 2, got 1
- `rdf` run 2: count: expected 2, got 1
- `rdf` run 3: count: expected 2, got 1
- `rdf` run 4: count: expected 2, got 1
- `rdf` run 5: count: expected 2, got 1
- `csv+padding` run 1: count: expected 2, got 1
- `csv+padding` run 2: count: expected 2, got 1
- `csv+padding` run 3: count: expected 2, got 1
- `csv+padding` run 4: count: expected 2, got 1
- `csv+padding` run 5: count: expected 2, got 1

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 1: count: expected 2, got 0
- `csv` run 2: count: expected 2, got 0
- `csv` run 3: count: expected 2, got 0
- `csv` run 5: count: expected 2, got 0
- `rdf` run 1: count: expected 2, got 0
- `rdf` run 2: count: expected 2, got 0
- `rdf` run 3: count: expected 2, got 0
- `rdf` run 4: count: expected 2, got 0
- `rdf` run 5: count: expected 2, got 0
- `csv+padding` run 1: count: expected 2, got 0
- `csv+padding` run 2: count: expected 2, got 0
- `csv+padding` run 3: count: expected 2, got 0
- `csv+padding` run 4: count: expected 2, got 0
- `csv+padding` run 5: count: expected 2, got 0

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04
- `csv` run 2: institution: expected I06, got I04
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04
- `rdf` run 1: institution: expected I06, got I02
- `rdf` run 2: institution: expected I06, got I02
- `rdf` run 3: institution: expected I06, got I02
- `rdf` run 4: institution: expected I06, got I02
- `rdf` run 5: institution: expected I06, got I02
- `csv+padding` run 1: institution: expected I06, got I04
- `csv+padding` run 2: institution: expected I06, got I04
- `csv+padding` run 3: institution: expected I06, got I04
- `csv+padding` run 4: institution: expected I06, got I04
- `csv+padding` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I06', 'I02', 'I01']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I06', 'I02', 'I01']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I02', 'I01', 'I06']
- `rdf` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `rdf` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `rdf` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `rdf` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I02', 'I01', 'I06']
- `csv+padding` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `csv` run 1: count: expected 3, got 1
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got None
- `rdf` run 1: count: expected 3, got 4
- `rdf` run 2: count: expected 3, got 4
- `rdf` run 3: count: expected 3, got None
- `rdf` run 4: count: expected 3, got 4
- `rdf` run 5: count: expected 3, got 4
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got None
- `csv+padding` run 4: count: expected 3, got None
- `csv+padding` run 5: count: expected 3, got 1

**Q40.** Which source is in the highest tier?

- `csv` run 1: source: expected S01, got S04
- `csv` run 5: source: expected S01, got None
- `rdf` run 3: source: expected S01, got None
- `csv+padding` run 3: source: expected S01, got None
- `csv+padding` run 4: source: expected S01, got None
- `csv+padding` run 5: source: expected S01, got S04

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `csv` run 1: higher: expected no, got depends
- `csv` run 2: higher: expected no, got depends
- `csv` run 3: higher: expected no, got depends
- `csv` run 4: higher: expected no, got depends
- `csv` run 5: higher: expected no, got depends
- `rdf` run 1: higher: expected no, got depends
- `rdf` run 2: higher: expected no, got depends
- `rdf` run 3: higher: expected no, got depends
- `rdf` run 4: higher: expected no, got depends
- `csv+padding` run 1: higher: expected no, got depends
- `csv+padding` run 2: higher: expected no, got depends
- `csv+padding` run 3: higher: expected no, got depends
- `csv+padding` run 4: higher: expected no, got depends
- `csv+padding` run 5: higher: expected no, got depends

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `csv` run 1: count: expected 0, got 2
- `csv` run 2: count: expected 0, got 2
- `csv` run 3: count: expected 0, got 2
- `csv` run 4: count: expected 0, got 2
- `csv` run 5: count: expected 0, got 2
- `rdf` run 1: count: expected 0, got 2
- `rdf` run 2: count: expected 0, got 2
- `rdf` run 3: count: expected 0, got 2
- `rdf` run 4: count: expected 0, got 2
- `rdf` run 5: count: expected 0, got 2
- `csv+padding` run 1: count: expected 0, got 2
- `csv+padding` run 2: count: expected 0, got 2
- `csv+padding` run 3: count: expected 0, got 2
- `csv+padding` run 4: count: expected 0, got 2
- `csv+padding` run 5: count: expected 0, got 2

**Q43.** Is W07 research output?

- `csv` run 1: research: expected no, got yes
- `csv` run 2: research: expected no, got yes
- `csv` run 3: research: expected no, got yes
- `csv` run 4: research: expected no, got yes
- `csv` run 5: research: expected no, got yes
- `rdf` run 1: research: expected no, got yes
- `rdf` run 2: research: expected no, got yes
- `rdf` run 3: research: expected no, got yes
- `rdf` run 4: research: expected no, got yes
- `rdf` run 5: research: expected no, got yes
- `csv+padding` run 1: research: expected no, got yes
- `csv+padding` run 2: research: expected no, got yes
- `csv+padding` run 3: research: expected no, got yes
- `csv+padding` run 4: research: expected no, got yes
- `csv+padding` run 5: research: expected no, got yes

**Q44.** Which institutions are part of the Albury University System, at any level below it?

- `csv` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `rdf` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `rdf` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `rdf` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `rdf` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `rdf` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv+padding` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv+padding` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv+padding` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv+padding` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv+padding` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']

**Q45.** How many research works is the Halloran Institute for Coastal Studies (I06) credited with?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4
- `rdf` run 1: count: expected 3, got 4
- `rdf` run 2: count: expected 3, got 4
- `rdf` run 3: count: expected 3, got 4
- `rdf` run 4: count: expected 3, got 4
- `rdf` run 5: count: expected 3, got 4
- `rdf+ontology` run 2: count: expected 3, got 2
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got 4
- `csv+padding` run 4: count: expected 3, got 4
- `csv+padding` run 5: count: expected 3, got 4

**Q46.** What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?

- `csv` run 1: parent: expected I06, got I01
- `csv` run 2: parent: expected I06, got I01
- `csv` run 3: parent: expected I06, got I01
- `csv` run 4: parent: expected I06, got I01
- `csv` run 5: parent: expected I06, got I01
- `rdf` run 1: parent: expected I06, got I01
- `rdf` run 2: parent: expected I06, got I01
- `rdf` run 3: parent: expected I06, got I01
- `rdf` run 4: parent: expected I06, got I01
- `rdf` run 5: parent: expected I06, got I01
- `csv+padding` run 1: parent: expected I06, got I01
- `csv+padding` run 2: parent: expected I06, got I01
- `csv+padding` run 3: parent: expected I06, got I01
- `csv+padding` run 4: parent: expected I06, got I01
- `csv+padding` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Correctly gives Rostval's four works with one of four authors (0.25 each) and Kesting's W22 plus halves of W20 and W21, but it also says W21 is one of Rostval's works, which conflicts with the stated Kesting share, and it does not say Kesting's shares are larger.
- `csv` run 2: Correctly notes Rostval's works are quarter-shares and Kesting's W20/W21 are half-shares, but omits that each Rostval work has four authors with one from Rostval, and omits Kesting's single-author review W22; its 3-work full count is also not tied to W22.
- `csv` run 3: Gives Rostval's quarter share per work and Kesting's W22 plus half-shares of W20/W21, but says Rostval has 4 works in 2024 vs Kesting 3 only partly matching; the answer states Rostval 4 works, 0.25 each, so it meets both points, though it never explicitly says 'four authors with one from Rostval' as a fixed fact for all four works
- `csv` run 5: Covers Rostval's quarter shares (0.25 each) and Kesting's W22 plus half of W20/W21, but doesn't state that each work has four authors with one from Rostval; it also doesn't explicitly say the ranking swaps, though that is implied.
- `rdf` run 1: Gets Rostval's quarter shares (four authors each) and Kesting's larger shares (W22 single author, half of W20/W21), but says 4 works for Rostval vs the key's four works too; matches mostly, yet uses IDs I09/I07 without naming the institutions and omits that W22 is a review
- `rdf` run 3: Gets Rostval's quarter shares (1.0 total) and Kesting's single-author W22, but omits Kesting's half shares of W20 and W21 and doesn't state the swap direction explicitly
- `rdf` run 5: Gets Kesting's larger shares (W22 single-author, half of W20/W21) and the swap, but says Rostval is 'usually' one of four authors rather than stating each of its four works has four authors with one from Rostval.
- `rdf+ontology` run 2: Gives Kesting's shares (W22 whole, half of W20/W21) and 0.25 per work for I09, but doesn't state four authors with only one from Rostval; also says 'many co-authors' and omits that Rostval has four works vs 3 only partially matching.
- `rdf+ontology` run 3: Gets Rostval's quarter shares (1 of 4 authors each) and Kesting's W22 sole and W20 half, but omits that Kesting also holds half of W21 and mischaracterizes W21 as a Rostval work; it also lists W21 as Rostval's 4-author work while Kesting shares it.
- `csv+ontology` run 2: Covers Kesting's solo W22 and half shares of W20/W21 and the 0.25 shares for I09, but never names the institutions as Kesting/Rostval, and says W21 is one of I09's works (W21 is also half-shared by I07), which is an inconsistency with the key's four Rostval works; mostly matches though.
- `csv+ontology` run 4: Correctly gives Rostval's quarter-share per work, but Kesting's shares are given only as (0.5, 0.5, 1) without naming W22 as single-author review and W20/W21 as half-shares.
- `csv+markdown` run 1: The Rostval quarter-share point is correct, but the answer omits half of W20 and credits Kesting's 2.0 to W22 plus W21 alone, which only sums to 1.5.
- `csv+markdown` run 3: Rostval's quarter-share point is correct, but the answer credits Kesting with only W22 and half of W20 and omits half of W21 (its 2.0 total needs it).
- `csv+markdown` run 5: Says I09's four works are four-author papers with one quarter each, and I07 holds W22 solely plus half of W20/W21, but never maps these to Rostval/Kesting by name; both checklist points are essentially covered, though the explanation of 'four 2024 works' is consistent. Strictly, it meets both points in substance but uses IDs only.
- `csv+padding` run 1: Gives the quarter-share point for Rostval (four authors, 0.25 each) and Kesting's W22 single-author plus 0.5 each from W20/W21, but doesn't say only one of the four authors is from Rostval; implicit in 0.25. Mostly meets both, though it never states the swap itself.
- `csv+padding` run 2: Gives Rostval's quarter share per work (0.25 each) but does not say each has four authors with one from Rostval explicitly; Kesting's larger shares are only vaguely described (W22 single-author is right, but W20/W21 are 'split fairly evenly' rather than half each).

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, an affiliated institute that does not roll up to Albury.
- `csv` run 2: Claims W70 does count toward Albury; the key says only the last-listed affiliation counts (Halloran Institute), an affiliated institute that doesn't roll up to Albury.
- `csv` run 3: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, so it goes to Halloran Institute, an affiliated institute that doesn't roll up to Albury
- `csv` run 4: Rejects the premise and says W70 counts for Albury; the checklist says only the last-listed affiliation counts, crediting the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv` run 5: Rejects the premise and claims W70 is a University of Albury work; the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, which is an affiliated institute and not a unit, so it doesn't roll up.
- `rdf` run 1: Rejects the premise and says W70 counts for Albury, contradicting the key's points that only the last-listed affiliation counts (Halloran Institute) and that the affiliated institute doesn't roll up to Albury
- `rdf` run 2: Claims W70 is a University of Albury work; contradicts the key, which says only the last-listed affiliation counts (Halloran Institute, an affiliated institute that doesn't roll up) and misses both points.
- `rdf` run 3: Asserts W70 is a University of Albury work, contradicting the key: only the last-listed affiliation (Halloran Institute) counts, and it is an affiliated institute that doesn't roll up
- `rdf` run 4: Rejects the premise and says W70 counts for Albury, contradicting the key: only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that doesn't roll up.
- `rdf` run 5: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, so W70 is credited to Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv+ontology` run 2: Gives last-listed-affiliation rule and credits I06, but says only that the parent link isn't followed because it's an affiliated institute; this covers the second point loosely, yet doesn't say it's an affiliated institute rather than a unit explicitly as the reason for no roll-up.
- `csv+padding` run 1: Rejects the premise and says W70 is an Albury work; the checklist says only the last-listed affiliation counts, crediting the Halloran Institute, which doesn't roll up to Albury.
- `csv+padding` run 2: Claims W70 does count for Albury; the key says only the last-listed affiliation counts (Halloran Institute), and as an affiliated institute it doesn't roll up to Albury.
- `csv+padding` run 3: Claims W70 does belong to Albury via roll-up, contradicting the key (last-listed affiliation only, Halloran Institute is affiliated, not a unit); meets neither point.
- `csv+padding` run 4: Rejects the premise and says W70 counts via Tessel and Halloran; the key says only the last-listed affiliation counts, crediting Halloran, an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 5: Claims W70 is a University of Albury work, contradicting the key: only the last-listed affiliation counts, crediting the Halloran Institute, which is affiliated and not a unit, so it doesn't roll up.

