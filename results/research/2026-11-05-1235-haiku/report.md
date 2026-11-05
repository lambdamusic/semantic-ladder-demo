# research: claude:haiku, 2026-11-05 12:35

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **45%** | 32% to 59% | 8 of 48 |
| `rdf` | **43%** | 30% to 57% | 4 of 48 |
| `rdf+ontology` | **98%** | 95% to 100% | 2 of 48 |
| `csv+ontology` | **96%** | 92% to 99% | 6 of 48 |
| `csv+markdown` | **99%** | 96% to 100% | 3 of 48 |
| `csv+padding` | **44%** | 31% to 57% | 6 of 48 |
| `executed` | **92%** | 84% to 98% | 4 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -3 points | -7 to +2 |
| `rdf+ontology` | +53 points | +40 to +66 |
| `csv+ontology` | +51 points | +38 to +64 |
| `csv+markdown` | +53 points | +40 to +66 |
| `csv+padding` | -1 points | -5 to +2 |
| `executed` | +46 points | +32 to +61 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` | `executed` |
|---|---|---|---|---|---|---|---|---|
| Q1 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ❌ ✅ | ✅ ❌ ❌ ❌ ✅ | ❌ ❌ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ❌ | ✅ ❌ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ❌ ✅ ✅ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ 🟡 ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q21 | code | ✅ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ 🟡 ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q47 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 ✅ 🟡 🟡 | ✅ 🟡 🟡 🟡 ✅ | ✅ 🟡 🟡 🟡 🟡 | ✅ 🟡 🟡 🟡 🟡 | ✅ 🟡 🟡 🟡 ✅ | ✅ 🟡 🟡 🟡 ✅ |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ 🟡 | ✅ ✅ ✅ 🟡 ✅ | ❌ ❌ ❌ ❌ ❌ | 🟡 🟡 🟡 ✅ 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 33% | 89% |
| `rdf` | 33% | 89% |
| `rdf+ontology` | 100% | 100% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 100% | 100% |
| `csv+padding` | 37% | 90% |
| `executed` | 63% | 82% |

**The checklist grader agreed with itself** on 60 of 70 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf` run 2: count: expected 2, got 1
- `rdf` run 4: count: expected 2, got 1
- `rdf+ontology` run 2: count: expected 2, got 1
- `rdf+ontology` run 3: count: expected 2, got 1
- `rdf+ontology` run 4: count: expected 2, got 1
- `csv+ontology` run 1: count: expected 2, got 1
- `csv+ontology` run 2: count: expected 2, got 1
- `csv+ontology` run 5: count: expected 2, got 1
- `csv+markdown` run 5: count: expected 2, got 1
- `csv+padding` run 2: count: expected 2, got 1
- `csv+padding` run 4: count: expected 2, got 1
- `csv+padding` run 5: count: expected 2, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `csv` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `rdf` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `rdf` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `rdf` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `rdf` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `rdf` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv+padding` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv+padding` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv+padding` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv+padding` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']

**Q3.** Is the Jonas Brandt who wrote W37 the same person as the Jonas Brandt who wrote W38?

- `csv+ontology` run 2: same: expected no, got None

**Q5.** Is the M. Ellison who wrote W08 the same person as the Mara Ellison who wrote W01?

- `csv+ontology` run 2: same: expected no, got None

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `csv` run 1: author: expected A01, got A07, A08 (tie, 4 each)
- `csv` run 4: author: expected A01, got A07
- `rdf` run 1: author: expected A01, got A07
- `rdf` run 2: author: expected A01, got A07
- `rdf` run 3: author: expected A01, got A07
- `rdf` run 4: author: expected A01, got A07
- `rdf` run 5: author: expected A01, got A07
- `csv+padding` run 1: author: expected A01, got A07
- `csv+padding` run 2: author: expected A01, got A07
- `csv+padding` run 3: author: expected A01, got A07

**Q7.** How many research works has Mara Ellison authored?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 7
- `csv` run 3: count: expected 5, got 7
- `csv` run 4: count: expected 5, got 3
- `csv` run 5: count: expected 5, got 7
- `rdf` run 1: count: expected 5, got 7
- `rdf` run 2: count: expected 5, got 3
- `rdf` run 3: count: expected 5, got 3
- `rdf` run 4: count: expected 5, got 3
- `rdf` run 5: count: expected 5, got 7
- `csv+padding` run 1: count: expected 5, got 3
- `csv+padding` run 2: count: expected 5, got 7
- `csv+padding` run 3: count: expected 5, got 7
- `csv+padding` run 4: count: expected 5, got 6
- `csv+padding` run 5: count: expected 5, got 7

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 8, got 12
- `csv` run 2: count: expected 8, got 13
- `csv` run 3: count: expected 8, got 13
- `csv` run 4: count: expected 8, got 12
- `csv` run 5: count: expected 8, got 13
- `rdf` run 1: count: expected 8, got 13
- `rdf` run 2: count: expected 8, got 13
- `rdf` run 3: count: expected 8, got 13
- `rdf` run 4: count: expected 8, got 13
- `rdf` run 5: count: expected 8, got 13
- `csv+padding` run 1: count: expected 8, got 13
- `csv+padding` run 2: count: expected 8, got 13
- `csv+padding` run 3: count: expected 8, got 13
- `csv+padding` run 4: count: expected 8, got 12
- `csv+padding` run 5: count: expected 8, got 13

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 12, got 16
- `csv` run 2: count: expected 12, got 17
- `csv` run 3: count: expected 12, got 17
- `csv` run 4: count: expected 12, got 16
- `csv` run 5: count: expected 12, got 17
- `rdf` run 1: count: expected 12, got 17
- `rdf` run 2: count: expected 12, got 17
- `rdf` run 3: count: expected 12, got 17
- `rdf` run 4: count: expected 12, got 17
- `rdf` run 5: count: expected 12, got 17
- `csv+padding` run 1: count: expected 12, got 17
- `csv+padding` run 2: count: expected 12, got 17
- `csv+padding` run 3: count: expected 12, got 17
- `csv+padding` run 4: count: expected 12, got 16
- `csv+padding` run 5: count: expected 12, got 17

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 1: count: expected 6, got 9
- `csv` run 2: count: expected 6, got 10
- `csv` run 3: count: expected 6, got 9
- `csv` run 4: count: expected 6, got 9
- `csv` run 5: count: expected 6, got 8
- `rdf` run 1: count: expected 6, got 9
- `rdf` run 2: count: expected 6, got 9
- `rdf` run 3: count: expected 6, got 9
- `rdf` run 4: count: expected 6, got 9
- `rdf` run 5: count: expected 6, got 10
- `csv+padding` run 1: count: expected 6, got 9
- `csv+padding` run 2: count: expected 6, got 9
- `csv+padding` run 3: count: expected 6, got 9
- `csv+padding` run 4: count: expected 6, got 9
- `csv+padding` run 5: count: expected 6, got 9

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `executed` run 4: full: expected I09, got tie

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `csv` run 1: count: expected 10, got 11
- `csv` run 2: count: expected 10, got 11
- `csv` run 3: count: expected 10, got 11
- `csv` run 4: count: expected 10, got 11
- `csv` run 5: count: expected 10, got 11
- `rdf` run 1: count: expected 10, got 11
- `rdf` run 2: count: expected 10, got 11
- `rdf` run 3: count: expected 10, got 11
- `rdf` run 4: count: expected 10, got 11
- `rdf` run 5: count: expected 10, got 11
- `csv+padding` run 1: count: expected 10, got 11
- `csv+padding` run 2: count: expected 10, got 11
- `csv+padding` run 3: count: expected 10, got 11
- `csv+padding` run 4: count: expected 10, got 11
- `csv+padding` run 5: count: expected 10, got 11

**Q18.** How many distinct research works has Priya Ramanathan (A07) authored?

- `csv` run 3: count: expected 4, got 5
- `csv` run 5: count: expected 4, got 5
- `rdf` run 1: count: expected 4, got 5
- `rdf` run 2: count: expected 4, got 5
- `rdf` run 3: count: expected 4, got 5
- `rdf` run 4: count: expected 4, got 5
- `rdf` run 5: count: expected 4, got 5
- `csv+padding` run 1: count: expected 4, got 5
- `csv+padding` run 2: count: expected 4, got 5
- `csv+padding` run 3: count: expected 4, got 5
- `csv+padding` run 5: count: expected 4, got 5

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `executed` run 1: works: expected ['W02', 'W42'], got []
- `executed` run 2: works: expected ['W02', 'W42'], got []
- `executed` run 3: works: expected ['W02', 'W42'], got []
- `executed` run 4: works: expected ['W02', 'W42'], got []
- `executed` run 5: works: expected ['W02', 'W42'], got []

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `csv` run 2: count: expected 4, got 5
- `csv` run 3: count: expected 4, got 5
- `csv` run 5: count: expected 4, got 5
- `rdf` run 1: count: expected 4, got 5
- `rdf` run 2: count: expected 4, got 5
- `rdf` run 3: count: expected 4, got 5
- `rdf` run 4: count: expected 4, got 5
- `rdf` run 5: count: expected 4, got 5
- `csv+padding` run 1: count: expected 4, got 5
- `csv+padding` run 2: count: expected 4, got 5
- `csv+padding` run 3: count: expected 4, got 5
- `csv+padding` run 5: count: expected 4, got 5

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `rdf` run 1: count: expected 3, got 4
- `rdf` run 2: count: expected 3, got 4
- `rdf` run 3: count: expected 3, got 4
- `rdf` run 4: count: expected 3, got 4
- `rdf` run 5: count: expected 3, got 4
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got 4
- `csv+padding` run 4: count: expected 3, got 4
- `csv+padding` run 5: count: expected 3, got 4

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 1: count: expected 6, got 10
- `csv` run 2: count: expected 6, got 10
- `csv` run 3: count: expected 6, got 10
- `csv` run 4: count: expected 6, got 10
- `csv` run 5: count: expected 6, got 9
- `rdf` run 1: count: expected 6, got 10
- `rdf` run 2: count: expected 6, got 10
- `rdf` run 3: count: expected 6, got 10
- `rdf` run 4: count: expected 6, got 10
- `rdf` run 5: count: expected 6, got 10
- `csv+padding` run 1: count: expected 6, got 10
- `csv+padding` run 2: count: expected 6, got 10
- `csv+padding` run 3: count: expected 6, got 10
- `csv+padding` run 4: count: expected 6, got 10
- `csv+padding` run 5: count: expected 6, got 10

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 1: counts: expected no, got depends
- `csv` run 2: counts: expected no, got depends
- `csv` run 3: counts: expected no, got depends
- `csv` run 4: counts: expected no, got yes
- `rdf` run 1: counts: expected no, got yes
- `rdf` run 2: counts: expected no, got yes
- `rdf` run 3: counts: expected no, got depends
- `rdf` run 4: counts: expected no, got depends
- `rdf` run 5: counts: expected no, got yes
- `csv+padding` run 1: counts: expected no, got depends
- `csv+padding` run 2: counts: expected no, got yes
- `csv+padding` run 3: counts: expected no, got yes
- `csv+padding` run 4: counts: expected no, got depends
- `csv+padding` run 5: counts: expected no, got depends

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `csv` run 4: author: expected 2, got 1

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `rdf` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv+padding` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

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

**Q33.** Which of Kesting University's research works has the most citations?

- `csv` run 1: work: expected W20, got W22
- `csv` run 2: work: expected W20, got W22
- `csv` run 3: work: expected W20, got W22
- `csv` run 4: work: expected W20, got W22
- `csv` run 5: work: expected W20, got W22
- `rdf` run 1: work: expected W20, got W22
- `rdf` run 2: work: expected W20, got W22
- `rdf` run 3: work: expected W20, got W22
- `rdf` run 4: work: expected W20, got W22
- `rdf` run 5: work: expected W20, got W22
- `csv+padding` run 1: work: expected W20, got W22
- `csv+padding` run 2: work: expected W20, got W22
- `csv+padding` run 3: work: expected W20, got W22
- `csv+padding` run 4: work: expected W20, got W22
- `csv+padding` run 5: work: expected W20, got W22

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 1: count: expected 3, got 5
- `csv` run 2: count: expected 3, got 6
- `csv` run 3: count: expected 3, got 5
- `csv` run 4: count: expected 3, got 5
- `csv` run 5: count: expected 3, got 5
- `rdf` run 1: count: expected 3, got 5
- `rdf` run 2: count: expected 3, got 5
- `rdf` run 3: count: expected 3, got 5
- `rdf` run 4: count: expected 3, got 5
- `rdf` run 5: count: expected 3, got 6
- `csv+padding` run 1: count: expected 3, got 5
- `csv+padding` run 2: count: expected 3, got 5
- `csv+padding` run 3: count: expected 3, got 5
- `csv+padding` run 4: count: expected 3, got 5
- `csv+padding` run 5: count: expected 3, got 5

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf` run 1: count: expected 2, got 1
- `rdf` run 2: count: expected 2, got 1
- `rdf` run 3: count: expected 2, got 1
- `rdf` run 4: count: expected 2, got 1
- `csv+padding` run 1: count: expected 2, got 1
- `csv+padding` run 2: count: expected 2, got 1
- `csv+padding` run 3: count: expected 2, got 1
- `csv+padding` run 4: count: expected 2, got 1
- `csv+padding` run 5: count: expected 2, got 1

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 1: count: expected 2, got 0
- `csv` run 3: count: expected 2, got 0
- `csv` run 4: count: expected 2, got 0
- `csv` run 5: count: expected 2, got 0
- `rdf` run 1: count: expected 2, got 0
- `rdf` run 2: count: expected 2, got 0
- `rdf` run 3: count: expected 2, got 0
- `rdf` run 4: count: expected 2, got 0
- `csv+padding` run 1: count: expected 2, got 0
- `csv+padding` run 2: count: expected 2, got 0
- `csv+padding` run 3: count: expected 2, got 0
- `csv+padding` run 4: count: expected 2, got 0
- `csv+padding` run 5: count: expected 2, got 0

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04, I06
- `csv` run 2: institution: expected I06, got I04
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04
- `rdf` run 1: institution: expected I06, got I04 and I06
- `rdf` run 2: institution: expected I06, got I04; I06
- `rdf` run 3: institution: expected I06, got I04
- `rdf` run 4: institution: expected I06, got I04
- `rdf` run 5: institution: expected I06, got I04
- `csv+padding` run 1: institution: expected I06, got I04
- `csv+padding` run 2: institution: expected I06, got I04
- `csv+padding` run 3: institution: expected I06, got I04
- `csv+padding` run 4: institution: expected I06, got I04
- `csv+padding` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

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
- `csv+padding` run 1: count: expected 3, got 4
- `csv+padding` run 2: count: expected 3, got 4
- `csv+padding` run 3: count: expected 3, got 4
- `csv+padding` run 4: count: expected 3, got 4
- `csv+padding` run 5: count: expected 3, got 4

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
- `executed` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']

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
- `csv+ontology` run 1: count: expected 3, got 2
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
- `executed` run 1: parent: expected I06, got I01
- `executed` run 2: parent: expected I06, got I01
- `executed` run 3: parent: expected I06, got I01
- `executed` run 4: parent: expected I06, got I01
- `executed` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Kesting's larger shares (W22 single-author, half of W20) are covered, but it doesn't state that each Rostval work has four authors, so a quarter each, and it misses W21 as a half share.
- `csv` run 2: Gets Rostval's four-author works at 0.25 each and Kesting's single-author W22, but omits Kesting's half share of W21 (only mentions W20) and doesn't clearly state one Rostval author per work.
- `csv` run 3: Gives the Kesting side (W22 single-author, W21 half) and says Rostval's works have 4 authors, but doesn't state that only one author per work is from Rostval, i.e. a quarter each; also W20 is described as 2 authors rather than a half share, which is imprecise.
- `csv` run 4: Gives the one-quarter shares for Rostval's multi-author works and Kesting's single-author W22, but omits that Kesting also holds half of W20 and W21 (its larger shares).
- `csv` run 5: Gets Rostval at one of four authors per work and Kesting's larger shares, but the shares given (0.5, 0.5, 1.0) are consistent with the key's W20/W21 halves and W22 single-author; it omits naming W20-W22 and the 'a quarter each' framing is only implied via 1/4. Stated total of 1.0 for Rostval is consistent with 4 × 0.25.
- `rdf` run 1: Gives the quarter-share for Rostval's four-author works, but for Kesting it cites W20 (2 authors) and W22 (1 author) without mentioning W21 or the half-share of W20 and W21 explicitly.
- `rdf` run 2: Gets Rostval's four-author works and Kesting's solo W22 and shorter author lists right, but never says Rostval has only one author per work (a quarter each) or that Kesting holds half of W20 and W21; the claim that W20 has two authors is only loosely matched.
- `rdf` run 4: Gives Rostval's quarter-each shares and Kesting's W22 single-author review and half-shares, but never says the institutions swap places or explains the rank reversal; the W21 share (2/4) is also oddly stated, though it equals 1/2.
- `rdf` run 5: Rostval quarter-share reasoning is correct (1.0), but Kesting's explanation is inaccurate: it says W20 has two authors but omits W21 and misstates the shares (W22 solo plus half of W20 and W21).
- `rdf+ontology` run 2: Rostval quarter shares are correct, but the answer says Kesting has W22 (one author) and W20 (two authors) and omits W21 being half Kesting's; it doesn't cover the half of W20 and W21.
- `rdf+ontology` run 3: Gets the swap and the totals (Kesting 2.0 vs Rostval 1.0), but never says each Rostval work has four authors with one from Rostval. It gives Kesting's author counts as 2, 4 and 1, which contradicts the key's half shares of W20 and W21 and does not add up to 2.0.
- `rdf+ontology` run 4: Covers the Rostval quarter shares and Kesting's W22 full share, but omits Kesting's half shares of W20 and W21, and says 'most' rather than each Rostval work has four authors.
- `csv+ontology` run 2: Explains fractional shares and Kesting's larger share (W22 at 1.0, halves), but doesn't say Rostval's works have four authors with one from Rostval; uses IDs, and doesn't name W20/W21 halves precisely or mention the swap
- `csv+ontology` run 3: Gives Rostval's four-author works (0.25 each) and Kesting's single-author W22, but omits Kesting's half shares of W20 and W21 and doesn't say only one author is from Rostval
- `csv+ontology` run 4: Correctly says Kesting has larger shares (W22 single-author, half of W20/W21) and Rostval gets 1/4 per work, but says Kesting has fewer authors per work generally and doesn't state that each of Rostval's works has four authors with one from Rostval explicitly; mostly matches, though the 'half of W21' split across I07/I08 is muddled.
- `csv+ontology` run 5: Covers Rostval's four-author, quarter-share point and Kesting's W22 single-author review, but omits Kesting's half shares of W20 and W21.
- `csv+markdown` run 2: Gives the quarter-share point for Rostval (though it lists only three works, W27-W29, while claiming four), but never says Kesting's larger shares come from half of W20 and W21 as well as the single-author W22.
- `csv+markdown` run 3: Gives Rostval's quarter shares and Kesting's W22 full credit and W20 half, but omits W21's half share for Kesting and doesn't state that W22 is a review; the totals are stated without a W21 breakdown.
- `csv+markdown` run 4: Gets Rostval's quarter-share per work, but says Kesting has W20 (2 authors) and W22 only, omitting W21 and misdescribing W20/W22 shares; doesn't state one Rostval author per work.
- `csv+markdown` run 5: Rostval's quarter shares are covered, but Kesting's shares are not: the answer says 'W20 and W22 have few authors' and omits the single-author W22 and the half shares of W20 and W21.
- `csv+padding` run 2: Correctly says Rostval's four works give 1.0 total (a quarter each) and Kesting holds larger shares (2.0), but doesn't state the four-authors/one-from-Rostval reason or the specific single-author W22 and half shares of W20/W21.
- `csv+padding` run 3: Gets Rostval's four-author, one-Rostval-author quarter shares, but does not identify Kesting's W22 single-author review and half shares of W20/W21 (only vague 'larger share'); also states a total without that basis
- `csv+padding` run 4: Correctly says Rostval's works have four authors each (0.25 per work) and Kesting has larger shares, but doesn't identify the single-author review W22 or the half shares of W20 and W21.
- `executed` run 2: Gets Kesting's W22 full and half credits on W20/W21, and Rostval's 0.25 shares, but omits that each Rostval work has four authors with only one from Rostval.
- `executed` run 3: Gets Kesting's larger shares (W22 single-author, W21 two of four) and Rostval's one-of-four per work, but omits that Rostval's four works each have four authors with a quarter each as stated, and cites W21 instead of W20 and W21 as half-shares.
- `executed` run 4: Gets the fractional logic (four authors per I09 work, so quarter shares) but denies the swap, counts I09 as three works instead of four, and never names W22 or the half shares in W20 and W21.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Answer rejects the premise and says W70 is credited to Tessel and counts under Albury; the key says only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv` run 2: Answer claims W70 counts for the University of Albury via Tessel Laboratory; key says only the last-listed affiliation (Halloran Institute, an affiliated institute not a unit) counts, so it doesn't roll up to UoA.
- `csv` run 3: Rejects the premise; the key says only the last-listed affiliation counts, so W70 goes to Halloran Institute, an affiliated institute that does not roll up to Albury.
- `csv` run 4: Claims W70 does count for Albury via both affiliations, contradicting the key that only the last-listed affiliation (Halloran Institute, an affiliated institute that doesn't roll up) counts.
- `csv` run 5: Answer says W70 counts for Albury, contradicting the key: only the last-listed affiliation (Halloran) counts and Halloran is an affiliated institute that doesn't roll up.
- `rdf` run 1: Rejects the premise and credits W70 to Tessel/University of Albury, whereas the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, an affiliated institute and not a unit.
- `rdf` run 2: Rejects the premise and counts W70 for Albury, contradicting the key that only the last-listed affiliation (Halloran Institute) counts and that Halloran is an affiliated institute that doesn't roll up to Albury.
- `rdf` run 3: The answer says W70 does count toward Albury via both affiliations, which contradicts the key (only the last-listed affiliation counts, so it goes to Halloran, an affiliated institute that does not roll up to Albury).
- `rdf` run 4: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, crediting the Halloran Institute, an affiliated institute that does not roll up to Albury.
- `rdf` run 5: Answer rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, crediting the Halloran Institute, an affiliated institute that does not roll up to Albury.
- `csv+ontology` run 3: Says only the last-listed affiliation counts and that it goes to I06, an affiliated institute not a unit of Albury, which meets both points, but names IDs rather than the Halloran Institute and doesn't explicitly tie it to the Tessel Laboratory being ignored beyond a brief mention
- `csv+ontology` run 5: Says only the last affiliation counts so W70 goes to I06 (Halloran), outside Albury's unit tree, but doesn't state explicitly that Halloran is an affiliated institute rather than a unit.
- `csv+markdown` run 4: Says last-listed affiliation counts and it's an institute outside the Albury tree, but doesn't name W70 credited to Halloran Institute explicitly or that affiliated institutes' works don't roll up to the University; the Tessel Laboratory (I04) point is only implied.
- `csv+padding` run 1: Answer says W70 is credited to Albury via Tessel and Halloran, contradicting the key (only last-listed affiliation counts, Halloran is an affiliated institute not a unit, so W70 doesn't roll up to Albury).
- `csv+padding` run 2: Rejects the premise and says W70 counts for Albury, contradicting the key: only the last-listed affiliation counts (Halloran), and Halloran is an affiliated institute, not a unit, so it doesn't roll up.
- `csv+padding` run 3: Rejects the premise; the key says only the last-listed affiliation counts, so W70 goes to Halloran, an affiliated institute not rolling up to Albury
- `csv+padding` run 4: Rejects the premise and says W70 is an Albury work; the key says only the last-listed affiliation counts, crediting W70 to Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 5: Contradicts the key: says W70 is credited to Albury and Halloran is a unit, but the key says only the last affiliation counts and Halloran is an affiliated institute that doesn't roll up.
- `executed` run 1: Says the credit goes to Halloran (I06) and that I06 doesn't roll up to the University of Albury, but never states that only the last-listed affiliation counts, and never says Halloran is an affiliated institute rather than a unit.
- `executed` run 2: Says Halloran is credited and not rolled up to Albury, but doesn't state the last-listed-affiliation rule or that Halloran is an affiliated institute rather than a unit; it also rejects the premise instead of explaining it.
- `executed` run 3: Says W70 is credited to Halloran (I06) and its works don't roll up to Albury, but doesn't state the last-listed-affiliation rule or that Halloran is an affiliated institute rather than a unit.
- `executed` run 5: Says W70 is credited to Halloran (AFF) and that it doesn't roll up to Albury, but never states the 'last-listed affiliation counts' rule.

