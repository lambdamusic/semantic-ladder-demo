# credit: claude:haiku, 2026-11-05 12:33

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **78%** | 67% to 88% | 7 of 48 |
| `rdf` | **72%** | 60% to 83% | 4 of 48 |
| `rdf+ontology` | **97%** | 92% to 100% | 4 of 48 |
| `csv+ontology` | **99%** | 96% to 100% | 1 of 48 |
| `csv+markdown` | **98%** | 94% to 100% | 2 of 48 |
| `csv+padding` | **76%** | 64% to 87% | 7 of 48 |
| `executed` | **97%** | 92% to 100% | 1 of 48 |
| `csv+neutral` | **100%** | 99% to 100% | 1 of 48 |
| `csv+axioms` | **99%** | 98% to 100% | 2 of 48 |
| `csv+axioms+markdown` | **99%** | 97% to 100% | 2 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -6 points | -12 to -1 |
| `rdf+ontology` | +19 points | +8 to +31 |
| `csv+ontology` | +21 points | +10 to +32 |
| `csv+markdown` | +20 points | +9 to +32 |
| `csv+padding` | -2 points | -6 to +1 |
| `executed` | +19 points | +8 to +31 |
| `csv+neutral` | +22 points | +11 to +33 |
| `csv+axioms` | +21 points | +12 to +32 |
| `csv+axioms+markdown` | +21 points | +10 to +32 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` | `executed` | `csv+neutral` | `csv+axioms` | `csv+axioms+markdown` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | 🟡 🟡 🟡 🟡 ✅ | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 ❌ | 🟡 🟡 ✅ 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 ✅ 🟡 ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ❌ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ✅ ✅ ❌ ✅ | ❌ ❌ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q48 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |

## Lists, with partial credit

The 7 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 83% | 96% |
| `rdf` | 83% | 95% |
| `rdf+ontology` | 97% | 99% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 97% | 99% |
| `csv+padding` | 86% | 97% |
| `executed` | 100% | 100% |
| `csv+neutral` | 97% | 99% |
| `csv+axioms` | 100% | 100% |
| `csv+axioms+markdown` | 97% | 99% |

**The checklist grader agreed with itself** on 49 of 50 answers graded twice.

## Why each miss was marked

**Q4.** What is Northwind Holdings' current outlook?

- `csv` run 5: outlook: expected positive, got unresolved: STA or POS
- `rdf` run 1: outlook: expected positive, got STA
- `rdf` run 2: outlook: expected positive, got STA
- `rdf` run 3: outlook: expected positive, got STA
- `rdf` run 4: outlook: expected positive, got STA
- `rdf` run 5: outlook: expected positive, got ambiguous (STA per E02; POS per E03)

**Q5.** Whose credit risk does a holder of the Northwind Finance 2030 notes take, and how is it rated?

- `rdf` run 1: risk_of: expected E02, got E04
- `rdf` run 2: risk_of: expected E02, got E04
- `rdf` run 3: risk_of: expected E02, got E04
- `rdf` run 4: risk_of: expected E02, got E04
- `rdf` run 5: risk_of: expected E02, got E04
- `csv+padding` run 2: risk_of: expected E02, got E04

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `csv` run 1: Names the BB foreign-currency country ceiling as consistent with the lower rating, but hedges that the cause isn't stated and never says the ceiling caps foreign-currency ratings and not local-currency ones.
- `csv` run 2: Names the BB Country Ceiling as the cause, but never says it caps foreign-currency ratings and not local-currency ones.
- `csv` run 3: Only hedges that the FC rating matches the BB ceiling and is 'consistent with' a cap; doesn't assert the Country Ceiling as the cause or that it caps FC but not LC ratings.
- `csv` run 4: Notes FC rating equals the BB Country Ceiling, consistent with a cap, but hedges that it's unconfirmed and doesn't state that the ceiling caps FC and not LC ratings.
- `rdf` run 1: Identifies the BB country ceiling matching the FC rating as consistent with a cap, but hedges ('data gives no reason') and never states that the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 2: Identifies the BB country ceiling as fitting a cap on the FC rating, but hedges that the cause isn't stated and never says the ceiling doesn't apply to LC ratings.
- `rdf` run 3: Notes the BB rating matches Valdoria's BB country ceiling as consistent with a cap, but says no rationale is recorded and never states that the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 4: Notes the FC rating equals the Valdoria ceiling (BB), consistent with a cap, but hedges that the data doesn't state it and never says the ceiling caps foreign- but not local-currency ratings.
- `rdf` run 5: Names the BB country ceiling as the likely cause, but never says the ceiling caps foreign-currency ratings and not local-currency ones; it only implies this by contrasting the two ratings.
- `csv+padding` run 1: Identifies the BB country ceiling match as the likely cause, but only hedged, and never says the ceiling caps foreign-currency ratings and not local-currency ones.
- `csv+padding` run 2: Notes the FC rating equals the BB country ceiling, consistent with a cap, but hedges that the data doesn't state it and never says the ceiling caps FC but not LC ratings.
- `csv+padding` run 3: Notes the FC rating equals the BB country ceiling, consistent with a cap, but does not state the ceiling as the cause or that it caps foreign-currency and not local-currency ratings.
- `csv+padding` run 4: Notes FC rating equals the BB country ceiling, but says the data doesn't state the cause and doesn't say the ceiling caps FC and not LC ratings.
- `csv+padding` run 5: Answer says the data doesn't explain it and never names the Country Ceiling (BB) or says it caps foreign-currency ratings only.
- `executed` run 1: Identifies the BB country ceiling as the cause (point 1), but hedges ('does not state it') and never says the ceiling caps foreign-currency ratings and not local-currency ones (point 2).
- `executed` run 2: Notes FC rating equals the BB Valdoria ceiling while LC sits above it, but doesn't state the ceiling caps foreign-currency and not local-currency ratings as the cause; it disclaims an explicit reason.
- `executed` run 4: Names the Valdoria BB country ceiling as the cause (hedged as inferred), but never says the ceiling caps foreign-currency ratings and not local-currency ones.
- `executed` run 5: Identifies the BB ceiling matching the FC rating but hedges, says no reason is stated, and does not state that the ceiling caps FC and not LC ratings.
- `csv+axioms` run 2: Identifies the BB country ceiling matching the FC rating and that it is consistent with capping FC only, but hedges that the data doesn't state the reason rather than asserting the ceiling as the cause.
- `csv+axioms` run 4: Identifies that the FC rating sits at Valdoria's BB country ceiling (point 1 largely met), but explicitly declines to state the ceiling as the cause and never says it caps FC but not LC ratings.

**Q7.** Which issuers were downgraded in 2026?

- `csv` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `rdf` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E11', 'E16']
- `rdf` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E11', 'E16']
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
- `csv` run 4: count: expected 12, got 13
- `csv` run 5: count: expected 12, got 13
- `rdf` run 1: count: expected 12, got 13
- `rdf` run 2: count: expected 12, got 13
- `rdf` run 3: count: expected 12, got 14
- `rdf` run 4: count: expected 12, got 13
- `rdf` run 5: count: expected 12, got 13
- `rdf+ontology` run 2: count: expected 12, got 11
- `rdf+ontology` run 3: count: expected 12, got 11
- `csv+padding` run 1: count: expected 12, got 13
- `csv+padding` run 2: count: expected 12, got 13
- `csv+padding` run 3: count: expected 12, got 13
- `csv+padding` run 4: count: expected 12, got 13
- `csv+padding` run 5: count: expected 12, got 13

**Q10.** Is Valdoria Telecom investment grade?

- `rdf+ontology` run 1: investment_grade: expected depends, got no
- `rdf+ontology` run 2: investment_grade: expected depends, got no
- `rdf+ontology` run 3: investment_grade: expected depends, got no
- `rdf+ontology` run 5: investment_grade: expected depends, got no
- `csv+ontology` run 1: investment_grade: expected depends, got no
- `csv+ontology` run 2: investment_grade: expected depends, got no
- `csv+ontology` run 3: investment_grade: expected depends, got no
- `csv+markdown` run 2: investment_grade: expected depends, got no
- `csv+markdown` run 3: investment_grade: expected depends, got no
- `csv+markdown` run 4: investment_grade: expected depends, got no
- `csv+markdown` run 5: investment_grade: expected depends, got no
- `csv+axioms+markdown` run 1: investment_grade: expected depends, got no
- `csv+axioms+markdown` run 4: investment_grade: expected depends, got no

**Q18.** Which issuers were on Rating Watch Negative on 1 October 2026?

- `rdf` run 4: issuers: expected ['E06'], got ['E06', 'E14']

**Q19.** Which issuers had a Negative outlook on 1 October 2026?

- `csv` run 5: issuers: expected ['E01', 'E09'], got ['E01']
- `csv+axioms+markdown` run 3: issuers: expected ['E01', 'E09'], got ['E01']

**Q25.** How many instruments held an investment-grade rating on 1 October 2026?

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

**Q28.** What is the Republic of Corvenia's foreign-currency issuer rating?

- `rdf+ontology` run 3: rating: expected BBB+, got none

**Q30.** Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?

- `rdf+ontology` run 3: entities: expected ['E05', 'E15'], got ['E05']
- `csv+markdown` run 4: entities: expected ['E05', 'E15'], got ['E05']
- `csv+neutral` run 4: entities: expected ['E05', 'E15'], got ['E05']

**Q31.** Did any company have a foreign-currency issuer rating above its country's ceiling on 1 October 2026?

- `csv` run 3: any: expected no, got depends
- `csv+padding` run 1: any: expected no, got depends

**Q33.** Whose credit risk does a holder of the Halden Leasing 2028 notes take, and how is it rated?

- `rdf` run 1: risk_of: expected E10, got E11
- `rdf` run 2: risk_of: expected E10, got E11
- `rdf` run 3: risk_of: expected E10, got E11
- `rdf` run 4: risk_of: expected E10, got E11
- `rdf` run 5: risk_of: expected E10, got E11
- `csv+padding` run 2: risk_of: expected E10, got E11

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
- `rdf` run 5: count: expected 16, got 15
- `csv+padding` run 1: count: expected 16, got 17
- `csv+padding` run 2: count: expected 16, got 17
- `csv+padding` run 3: count: expected 16, got 17
- `csv+padding` run 4: count: expected 16, got 17
- `csv+padding` run 5: count: expected 16, got 17
- `csv+axioms` run 3: count: expected 16, got 14

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

**Q42.** In which country is Halden Bank domiciled?

- `csv` run 1: country: expected LU, got DE
- `csv` run 2: country: expected LU, got DE
- `csv` run 3: country: expected LU, got DE
- `csv` run 4: country: expected LU, got DE
- `csv` run 5: country: expected LU, got DE or LU (unresolved)
- `rdf` run 1: country: expected LU, got DE
- `rdf` run 2: country: expected LU, got DE
- `rdf` run 3: country: expected LU, got DE
- `rdf` run 4: country: expected LU, got DE
- `rdf` run 5: country: expected LU, got ambiguous (DE or LU)
- `csv+padding` run 1: country: expected LU, got DE
- `csv+padding` run 2: country: expected LU, got DE
- `csv+padding` run 3: country: expected LU, got DE
- `csv+padding` run 4: country: expected LU, got DE
- `csv+padding` run 5: country: expected LU, got DE

**Q44.** Is Valdoria Telecom's 2027 note a local-currency obligation?

- `rdf` run 1: local_currency: expected yes, got depends
- `rdf` run 2: local_currency: expected yes, got depends
- `rdf` run 4: local_currency: expected yes, got depends
- `rdf` run 5: local_currency: expected yes, got depends
- `csv+padding` run 3: local_currency: expected yes, got depends
- `csv+padding` run 4: local_currency: expected yes, got depends
- `csv+padding` run 5: local_currency: expected yes, got depends

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `csv` run 1: above_ceiling: expected no, got yes
- `csv` run 4: above_ceiling: expected no, got depends
- `rdf` run 1: above_ceiling: expected no, got depends
- `rdf` run 2: above_ceiling: expected no, got depends
- `rdf` run 4: above_ceiling: expected no, got depends
- `rdf` run 5: above_ceiling: expected no, got depends
- `csv+padding` run 2: above_ceiling: expected no, got yes
- `csv+padding` run 3: above_ceiling: expected no, got depends
- `csv+padding` run 4: above_ceiling: expected no, got depends
- `csv+padding` run 5: above_ceiling: expected no, got depends
- `executed` run 1: above_ceiling: expected no, got depends
- `executed` run 2: above_ceiling: expected no, got yes
- `executed` run 3: above_ceiling: expected no, got depends
- `executed` run 4: above_ceiling: expected no, got depends
- `executed` run 5: above_ceiling: expected no, got yes

**Q46.** Does Halden Leasing have an issuer rating?

- `csv` run 1: issuer_rating: expected no, got depends
- `csv` run 2: issuer_rating: expected no, got depends
- `rdf` run 5: issuer_rating: expected no, got depends
- `csv+padding` run 2: issuer_rating: expected no, got depends

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
- `rdf` run 2: count: expected 7, got 8
- `rdf` run 3: count: expected 7, got 8
- `rdf` run 4: count: expected 7, got 8
- `rdf` run 5: count: expected 7, got 8
- `csv+padding` run 1: count: expected 7, got 8
- `csv+padding` run 2: count: expected 7, got 8
- `csv+padding` run 3: count: expected 7, got 8
- `csv+padding` run 4: count: expected 7, got 8
- `csv+padding` run 5: count: expected 7, got 8

