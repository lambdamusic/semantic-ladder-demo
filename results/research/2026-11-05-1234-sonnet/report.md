# research: claude:sonnet, 2026-11-05 12:34

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **57%** | 44% to 69% | 11 of 48 |
| `rdf` | **47%** | 34% to 61% | 6 of 48 |
| `rdf+ontology` | **98%** | 94% to 100% | 4 of 48 |
| `csv+ontology` | **98%** | 94% to 100% | 2 of 48 |
| `csv+markdown` | **98%** | 94% to 100% | 2 of 48 |
| `csv+padding` | **57%** | 44% to 70% | 5 of 48 |
| `executed` | **90%** | 84% to 96% | 9 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -9 points | -17 to -3 |
| `rdf+ontology` | +41 points | +29 to +54 |
| `csv+ontology` | +41 points | +29 to +55 |
| `csv+markdown` | +41 points | +29 to +55 |
| `csv+padding` | +0 points | -5 to +5 |
| `executed` | +34 points | +20 to +48 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` | `executed` |
|---|---|---|---|---|---|---|---|---|
| Q1 | code | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ✅ ✅ ✅ | ❌ ✅ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ✅ ❌ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 ✅ 🟡 ✅ 🟡 |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ❌ ❌ ❌ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ❌ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ❌ |
| Q35 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ❌ |
| Q47 | llm | 🟡 ✅ 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ 🟡 | ✅ 🟡 ✅ 🟡 ✅ | ✅ 🟡 🟡 ✅ ✅ | ✅ 🟡 🟡 🟡 🟡 | ❌ 🟡 ❌ 🟡 ❌ |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | 🟡 🟡 🟡 🟡 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 57% | 95% |
| `rdf` | 37% | 91% |
| `rdf+ontology` | 100% | 100% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 100% | 100% |
| `csv+padding` | 63% | 96% |
| `executed` | 80% | 96% |

**The checklist grader agreed with itself** on 57 of 70 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf` run 1: count: expected 2, got 1
- `rdf` run 2: count: expected 2, got 1
- `rdf+ontology` run 1: count: expected 2, got 1
- `rdf+ontology` run 3: count: expected 2, got 1
- `rdf+ontology` run 4: count: expected 2, got 1
- `rdf+ontology` run 5: count: expected 2, got 1
- `csv+ontology` run 1: count: expected 2, got 1
- `csv+ontology` run 3: count: expected 2, got 1
- `csv+ontology` run 4: count: expected 2, got 1
- `csv+ontology` run 5: count: expected 2, got 1
- `csv+markdown` run 1: count: expected 2, got 1
- `csv+markdown` run 2: count: expected 2, got 1
- `csv+markdown` run 3: count: expected 2, got 1
- `csv+markdown` run 4: count: expected 2, got 1
- `csv+padding` run 1: count: expected 2, got 1
- `csv+padding` run 3: count: expected 2, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']

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
- `executed` run 3: count: expected 8, got 7

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
- `executed` run 3: count: expected 12, got 11

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 4: count: expected 6, got 5
- `csv` run 5: count: expected 6, got 5
- `rdf` run 1: count: expected 6, got 9
- `rdf` run 2: count: expected 6, got 9
- `rdf` run 3: count: expected 6, got 9
- `rdf` run 4: count: expected 6, got 8
- `rdf` run 5: count: expected 6, got 9

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `executed` run 1: full: expected 3, got 4; fractional: expected 2, got 3
- `executed` run 3: full: expected 3, got 4; fractional: expected 2, got 3.0
- `executed` run 5: full: expected 3, got 4; fractional: expected 2, got 3

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `executed` run 1: full: expected I09, got None
- `executed` run 3: full: expected I09, got None
- `executed` run 5: full: expected I09, got None

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `csv` run 5: count: expected 4, got 3

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `rdf` run 1: count: expected 10, got 11
- `rdf` run 2: count: expected 10, got 11
- `rdf` run 3: count: expected 10, got 11
- `rdf` run 4: count: expected 10, got 11
- `rdf` run 5: count: expected 10, got 11

**Q17.** Which of Mara Ellison's works are not research output because of their document type?

- `rdf` run 1: works: expected ['W04', 'W05'], got ['W02', 'W04', 'W05']
- `rdf` run 2: works: expected ['W04', 'W05'], got ['W02', 'W04', 'W05']
- `rdf` run 3: works: expected ['W04', 'W05'], got ['W02', 'W04', 'W05']
- `rdf` run 4: works: expected ['W04', 'W05'], got ['W02', 'W04', 'W05']

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `executed` run 2: works: expected ['W02', 'W42'], got []

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `rdf` run 1: count: expected 3, got 4
- `rdf` run 2: count: expected 3, got 4
- `rdf` run 3: count: expected 3, got 4
- `rdf` run 5: count: expected 3, got 4
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got 4
- `csv+padding` run 4: count: expected 3, got 4
- `csv+padding` run 5: count: expected 3, got 4

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 1: count: expected 6, got 7
- `csv` run 2: count: expected 6, got 10
- `csv` run 3: count: expected 6, got 7
- `rdf` run 1: count: expected 6, got 10
- `rdf` run 2: count: expected 6, got 10
- `rdf` run 3: count: expected 6, got 11
- `rdf` run 4: count: expected 6, got 9
- `rdf` run 5: count: expected 6, got 10
- `csv+padding` run 1: count: expected 6, got 7
- `csv+padding` run 2: count: expected 6, got 7
- `csv+padding` run 3: count: expected 6, got 7
- `csv+padding` run 4: count: expected 6, got 7
- `csv+padding` run 5: count: expected 6, got 7

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 1: counts: expected no, got depends
- `csv` run 2: counts: expected no, got depends
- `csv` run 3: counts: expected no, got depends
- `rdf` run 1: counts: expected no, got yes
- `rdf` run 2: counts: expected no, got yes
- `rdf` run 3: counts: expected no, got yes
- `rdf` run 5: counts: expected no, got yes
- `csv+padding` run 1: counts: expected no, got yes
- `csv+padding` run 2: counts: expected no, got depends
- `csv+padding` run 3: counts: expected no, got yes
- `csv+padding` run 4: counts: expected no, got yes
- `csv+padding` run 5: counts: expected no, got yes

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `csv` run 2: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6
- `rdf` run 1: count: expected 5, got 6
- `rdf` run 2: count: expected 5, got 6
- `rdf` run 3: count: expected 5, got 6
- `rdf` run 4: count: expected 5, got 6
- `rdf` run 5: count: expected 5, got 6
- `csv+padding` run 5: count: expected 5, got 6

**Q33.** Which of Kesting University's research works has the most citations?

- `csv` run 2: work: expected W20, got W22
- `rdf` run 1: work: expected W20, got W22
- `rdf` run 2: work: expected W20, got W22
- `rdf` run 3: work: expected W20, got W22
- `rdf` run 4: work: expected W20, got W22
- `rdf` run 5: work: expected W20, got W22

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 1: count: expected 3, got 2
- `csv` run 2: count: expected 3, got 2
- `csv` run 3: count: expected 3, got 2
- `csv` run 4: count: expected 3, got 2
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
- `csv+padding` run 5: count: expected 3, got 2
- `executed` run 1: count: expected 3, got 2
- `executed` run 5: count: expected 3, got 2

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
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
- `csv` run 4: count: expected 2, got 0
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
- `rdf` run 1: institution: expected I06, got I04
- `rdf` run 2: institution: expected I06, got I02
- `rdf` run 3: institution: expected I06, got I02
- `rdf` run 4: institution: expected I06, got I04
- `rdf` run 5: institution: expected I06, got I02
- `csv+padding` run 1: institution: expected I06, got I04
- `csv+padding` run 2: institution: expected I06, got I04
- `csv+padding` run 3: institution: expected I06, got I04
- `csv+padding` run 4: institution: expected I06, got I04
- `csv+padding` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `rdf` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `rdf` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `rdf` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `rdf` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4
- `rdf` run 1: count: expected 3, got 4
- `rdf` run 2: count: expected 3, got 4
- `rdf` run 3: count: expected 3, got 4
- `rdf` run 4: count: expected 3, got None
- `rdf` run 5: count: expected 3, got 4
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got 1
- `csv+padding` run 4: count: expected 3, got 1
- `csv+padding` run 5: count: expected 3, got 4
- `executed` run 3: count: expected 3, got 2

**Q40.** Which source is in the highest tier?

- `rdf` run 4: source: expected S01, got None
- `csv+padding` run 3: source: expected S01, got S04
- `csv+padding` run 4: source: expected S01, got S04

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `csv` run 1: higher: expected no, got depends
- `csv` run 2: higher: expected no, got depends
- `csv` run 3: higher: expected no, got depends
- `csv` run 4: higher: expected no, got depends
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
- `rdf+ontology` run 4: count: expected 3, got 2
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
- `executed` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Gives Kesting's W22 and half shares of W20/W21, but for Rostval says only 'one of four authors on each' giving 0.25, which is essentially the quarter-share point; however it never explicitly states that only one author per work is from Rostval, so it is nearly but not fully matched
- `csv` run 3: Gives Kesting's shares (W22 single-author, 0.5 each from W20/W21) and the 0.25 per four-author paper, but doesn't say only one author per Rostval paper is from Rostval; it also doesn't state the swap explicitly.
- `csv` run 4: Gets Rostval's quarter shares from multiple authors and Kesting's single-author W22, but omits that Kesting holds half of W20 and W21 and that each Rostval work has four authors with only one from Rostval.
- `csv` run 5: Gets the Rostval quarter-share point (1 of 4 each) but doesn't cite Kesting's specific larger shares (single-author W22, half of W20 and W21); says only 'mostly sole-authored', which is vague and conflicts with the half shares.
- `rdf` run 1: Rostval part matches (four authors, 0.25 each); Kesting is described as sole/main contributor with W22=1, W20 and W21=0.5, which matches the checklist's larger shares, but it never says W22 is a single-author review, and it says 'three works' unsupported. Mostly covers both points.
- `rdf` run 2: Gets Rostval's four-author quarter shares and Kesting's larger shares (W22 sole, half of W20/W21), but the answer doesn't state the swap explicitly or the full-vs-fractional ranking; checklist points mostly met except W22 described as 'sole-authored' without calling it a review, and half of W20 and W21 is misstated (W21 2 of 4 = half, W20 1 of 2 = half, fine).
- `rdf` run 3: Captures Kesting's larger shares (single-author W22, split W20) and Rostval being one of several authors, but omits the specifics: four authors per work, a quarter each, and half of W20 and W21.
- `rdf` run 4: Gets Rostval's one-of-four-authors share (though says 1.0 total, implying a quarter each) and Kesting's sole-authored W22 plus half of W20, but omits half of W21 and doesn't state the swap explicitly.
- `rdf` run 5: Gives Kesting's shares (W22 plus halves of W20/W21) and Rostval's quarter shares, but does not state that each Rostval work has four authors with only one from Rostval.
- `rdf+ontology` run 5: Gets the quarter-share for I09 works and Kesting's single-author W22 plus half of W20/W21, but says 'W21 and the other I09 works' without clearly stating each of Rostval's four 2024 works has four authors with only one from Rostval; also doesn't explicitly say the swap in ranking (full vs fractional) is explained by those larger shares, though implied.
- `csv+ontology` run 2: Gives Kesting's larger shares (W22 sole, half of W20) but omits W21 and does not state that each Rostval work has four authors, with one from Rostval, as a quarter each, though it mentions one author's quarter share in multi-author works.
- `csv+ontology` run 4: Gives Rostval's 0.25 shares (multi-author) and Kesting's sole-author W22 plus half shares of W20/W21, but doesn't state four authors with only one from Rostval per work; also doesn't mention the swap explicitly
- `csv+markdown` run 2: Explains Rostval's quarter shares (1.0 total) and Kesting's single-author W22 plus half of W20/W21, but doesn't state that all four Rostval works have four authors each; it assumes it from the totals and omits the explicit swap framing.
- `csv+markdown` run 3: Rostval's quarter-share reasoning is correct, but Kesting is only said to have a larger share, with no mention of the single-author W22 or the half shares of W20 and W21.
- `csv+padding` run 2: Correctly gives Kesting's sole-author W22 as the larger share, but says nothing of Kesting's half shares in W20 and W21, and only implies Rostval's quarter shares (four authors, one from Rostval) without saying that each of its four works is shared that way.
- `csv+padding` run 3: Kesting's shares (W22 sole, half of W20 and W21) are correct, but the answer never says each Rostval work has four authors and a quarter each; it only says 'one of four'.
- `csv+padding` run 4: Gives Rostval's quarter-share reasoning, but for Kesting only says W22 is single-authored and omits the half shares of W20 and W21.
- `csv+padding` run 5: Gets Rostval's quarter-share per work (four authors, one from Rostval), but doesn't identify Kesting's single-author review W22 and half shares of W20 and W21.
- `executed` run 1: Denies the swap and says full counting is a tie; it also never states the quarter-share reasoning for Rostval's four works or Kesting's W22 and half of W20/W21 shares.
- `executed` run 2: Gets Rostval's quarter shares (four authors, 0.25 each) but only mentions Kesting's solo W22, omitting its half shares of W20 and W21; its totals also don't match the checklist's Kesting shares.
- `executed` run 3: Denies a swap and gives a tie/different explanation; misses the Rostval quarter shares and Kesting's W22 and half of W20/W21 shares.
- `executed` run 4: Gives Rostval's four-author quarter shares and Kesting's W22/W20/W21 shares, but never names the two universities as the swap, and does not state that only one of the four authors is from Rostval; the one-from-Rostval point is only implied by the 0.25 share.
- `executed` run 5: Denies the swap and never gives the checklist reasons (Rostval's four-author works at a quarter share each; Kesting's W22 and half of W20/W21).

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise and says W70 counts for Albury; checklist says only the last-listed affiliation counts, crediting the Halloran Institute, which doesn't roll up to Albury
- `csv` run 2: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, crediting Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv` run 3: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, so W70 goes to Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv` run 4: Rejects the premise; the key says only the last-listed affiliation counts, so W70 is credited to the Halloran Institute, an affiliated institute that does not roll up to the University of Albury.
- `csv` run 5: Denies the premise and says W70 counts for Albury; the checklist says only the last-listed affiliation counts (Halloran Institute), which is an affiliated institute and does not roll up to Albury.
- `rdf` run 1: Rejects the premise and says W70 counts for Albury; checklist says only the last-listed affiliation counts (Halloran) and Halloran is affiliated, not a unit, so it doesn't roll up.
- `rdf` run 2: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation (Halloran Institute) counts and it is an affiliated institute, not a unit, so it doesn't roll up.
- `rdf` run 3: Contradicts the key: W70 is not the University of Albury's work, since only the last-listed affiliation (Halloran Institute, an affiliated institute not a unit) counts.
- `rdf` run 4: Rejects the premise; the key says only the last-listed affiliation counts, crediting W70 to the Halloran Institute, an affiliated institute that doesn't roll up to the University of Albury.
- `rdf` run 5: Claims W70 is a University of Albury work; the key says only the last-listed affiliation counts, so it is credited to the Halloran Institute, an affiliated institute that does not roll up to Albury.
- `rdf+ontology` run 5: Correctly says only the last-listed affiliation counts (I06) and that I06 is an affiliated institute whose parent link isn't followed, but doesn't name it as the Halloran Institute or state that W70 is credited to it; IDs are used instead.
- `csv+padding` run 1: Rejects the premise and credits W70 to the University of Albury, contradicting the checklist: only the last-listed affiliation counts, so W70 goes to the Halloran Institute, which is an affiliated institute and doesn't roll up.
- `csv+padding` run 2: Rejects the premise and says W70 counts for Albury, whereas the checklist says only the last-listed affiliation counts, crediting W70 to the Halloran Institute, which is an affiliated institute and does not roll up to Albury.
- `csv+padding` run 3: Claims W70 does count for Albury; misses that only the last-listed affiliation counts (Halloran Institute), an affiliated institute that doesn't roll up.
- `csv+padding` run 4: Claims W70 is an Albury work; the key says only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 5: Rejects the premise and says W70 counts toward Albury via Tessel; the key says only the last-listed affiliation counts, crediting W70 to Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `executed` run 1: Says W70 is credited only to I06, an affiliate that doesn't roll up to I02, but omits that only the last-listed affiliation counts.
- `executed` run 2: Correctly says the Halloran Institute (I06) is an affiliate, not a unit, so W70 doesn't roll up to Albury; omits that only the last-listed affiliation counts, which is why W70 is credited to Halloran.
- `executed` run 3: Says W70 is credited to Halloran (I06) and that I06 doesn't roll up to I02, but doesn't state the last-listed-affiliation rule or that Halloran is an affiliated institute rather than a unit.
- `executed` run 4: Says W70 is credited to the Halloran Institute and that it is an affiliate that does not roll up, but never states that only the last-listed affiliation counts.
- `executed` run 5: Credits W70 to the Halloran Institute and says it doesn't roll up to the University of Albury, but omits the rule that only the last-listed affiliation counts and doesn't say the institute is affiliated rather than a unit.

