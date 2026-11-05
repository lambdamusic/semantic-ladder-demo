# credit: claude:sonnet, 2026-11-05 12:27

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **84%** | 73% to 93% | 3 of 48 |
| `rdf` | **85%** | 74% to 94% | 2 of 48 |
| `rdf+ontology` | **100%** | 100% to 100% | 0 of 48 |
| `csv+ontology` | **99%** | 98% to 100% | 1 of 48 |
| `csv+markdown` | **100%** | 100% to 100% | 0 of 48 |
| `csv+padding` | **84%** | 73% to 94% | 0 of 48 |
| `executed` | **99%** | 98% to 100% | 1 of 48 |
| `csv+neutral` | **100%** | 99% to 100% | 1 of 48 |
| `csv+axioms` | **99%** | 98% to 100% | 1 of 48 |
| `csv+axioms+markdown` | **100%** | 99% to 100% | 1 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | +1 points | -1 to +3 |
| `rdf+ontology` | +16 points | +7 to +27 |
| `csv+ontology` | +15 points | +6 to +26 |
| `csv+markdown` | +16 points | +7 to +27 |
| `csv+padding` | +0 points | -1 to +2 |
| `executed` | +15 points | +6 to +27 |
| `csv+neutral` | +16 points | +7 to +27 |
| `csv+axioms` | +15 points | +6 to +26 |
| `csv+axioms+markdown` | +16 points | +7 to +27 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` | `executed` | `csv+neutral` | `csv+axioms` | `csv+axioms+markdown` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | 🟡 ✅ ✅ 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 | ✅ 🟡 🟡 🟡 ✅ | ✅ ✅ ✅ ✅ 🟡 | 🟡 🟡 🟡 ✅ 🟡 | 🟡 ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q48 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |

## Lists, with partial credit

The 7 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 86% | 97% |
| `rdf` | 86% | 97% |
| `rdf+ontology` | 100% | 100% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 100% | 100% |
| `csv+padding` | 86% | 97% |
| `executed` | 100% | 100% |
| `csv+neutral` | 100% | 100% |
| `csv+axioms` | 100% | 100% |
| `csv+axioms+markdown` | 100% | 100% |

**The checklist grader agreed with itself** on 47 of 50 answers graded twice.

## Why each miss was marked

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `csv` run 1: Names the BB Country Ceiling as the cause, but never says the ceiling caps only foreign-currency ratings and not local-currency ones; it only lists the differing ratings.
- `csv` run 4: Identifies the BB country ceiling and FC rating at that level, but hedges that the data states no reason and doesn't explicitly say the ceiling caps FC but not LC ratings.
- `csv` run 5: Identifies the BB Country Ceiling matching the foreign-currency rating, but hedges that the data doesn't state the cause and never says the ceiling applies only to foreign-currency ratings, not local-currency ones.
- `rdf` run 1: Identifies the BB country ceiling equal to the FC rating as consistent with a cap, but hedges it as inference and never states that the ceiling caps FC and not LC ratings.
- `rdf` run 2: Links the FC rating of BB to the Valdoria country ceiling (BB) but hedges that the data doesn't state a reason, and never says the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 3: Mentions the BB Country Ceiling as consistent with the gap but declines to name it as the cause and never says it caps only foreign-currency ratings.
- `rdf` run 4: Mentions the BB Country Ceiling as consistent with the gap but hedges that no reason is stated, and never says the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 5: Links BB foreign-currency rating to the VD country ceiling but only as a hedged inference; doesn't assert the ceiling as the cause or state that it caps foreign-currency but not local-currency ratings.
- `csv+padding` run 1: Names the BB country ceiling as the cause, but doesn't say it caps only foreign-currency ratings and not local-currency ones (only implied by the ratings listed).
- `csv+padding` run 2: Identifies the BB Country Ceiling and that the foreign-currency rating sits at it, but hedges and does not clearly state that the ceiling caps foreign-currency but not local-currency ratings as the cause.
- `csv+padding` run 3: Names the BB country ceiling and the FC/LC rating gap, but hedges that no reason is stated and never says the ceiling caps foreign-currency ratings and not local-currency ones.
- `csv+padding` run 4: Names the BB country ceiling and notes it equals the FC rating, but hedges ('no stated reason') and never says the ceiling caps FC ratings and not LC ratings.
- `csv+padding` run 5: Identifies the BB Valdoria ceiling and FC BB vs LC BBB- as consistent, but hedges that the data states no reason and never says the ceiling caps FC ratings but not LC ones.
- `executed` run 2: Names the BB Country Ceiling as the likely cause, but hedges and never states that the ceiling caps foreign-currency ratings and not local-currency ones.
- `executed` run 3: Identifies the BB ceiling and that FC sits at it while LC is higher, but hedges that the data doesn't state the cause and only says it is 'consistent with' the ceiling capping FC only, rather than asserting it.
- `executed` run 4: Identifies the BB Country Ceiling and that it is consistent with capping FC, but hedges as unconfirmed and doesn't clearly state it caps FC and not LC ratings as the cause.
- `csv+neutral` run 5: Names the BB Country Ceiling as the cause, but never says the ceiling applies only to foreign-currency ratings and not local-currency ones (LC is only shown as higher at BBB-).
- `csv+axioms` run 1: Mentions the Country Ceiling of BB alongside FC BB, but says the data gives no reason and never states the ceiling caps foreign-currency ratings and not local-currency ones.
- `csv+axioms` run 2: Names the BB Country Ceiling as consistent with the FC rating, but hedges that no reason is stated and never says the ceiling caps FC and not LC ratings.
- `csv+axioms` run 3: Identifies the BB Valdoria ceiling and the higher local-currency rating, but hedges that the data states no reason and never says the ceiling caps foreign-currency but not local-currency ratings.
- `csv+axioms` run 5: Notes FC rating equals the BB Country Ceiling but disclaims a stated cause and never says the ceiling caps FC and not LC ratings.
- `csv+axioms+markdown` run 1: Identifies the BB Country Ceiling matching the FC rating and says LC is not capped, but never states that the ceiling is the cause or that it caps foreign-currency ratings specifically.

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

- `csv` run 1: count: expected 12, got 13
- `csv` run 2: count: expected 12, got 13
- `csv` run 3: count: expected 12, got 13
- `csv` run 4: count: expected 12, got 13
- `csv` run 5: count: expected 12, got 13
- `rdf` run 1: count: expected 12, got 13
- `rdf` run 2: count: expected 12, got 13
- `rdf` run 3: count: expected 12, got 13
- `rdf` run 4: count: expected 12, got 13
- `rdf` run 5: count: expected 12, got 13
- `csv+padding` run 1: count: expected 12, got 13
- `csv+padding` run 2: count: expected 12, got 13
- `csv+padding` run 3: count: expected 12, got 13
- `csv+padding` run 4: count: expected 12, got 13
- `csv+padding` run 5: count: expected 12, got 13

**Q10.** Is Valdoria Telecom investment grade?

- `csv+ontology` run 3: investment_grade: expected depends, got no
- `csv+ontology` run 4: investment_grade: expected depends, got no

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

**Q42.** In which country is Halden Bank domiciled?

- `csv` run 1: country: expected LU, got DE
- `csv` run 2: country: expected LU, got DE
- `csv` run 3: country: expected LU, got DE
- `csv` run 4: country: expected LU, got DE
- `csv` run 5: country: expected LU, got DE
- `rdf` run 1: country: expected LU, got DE
- `rdf` run 2: country: expected LU, got DE
- `rdf` run 3: country: expected LU, got DE
- `rdf` run 4: country: expected LU, got DE
- `rdf` run 5: country: expected LU, got DE
- `csv+padding` run 1: country: expected LU, got DE
- `csv+padding` run 2: country: expected LU, got DE
- `csv+padding` run 3: country: expected LU, got DE
- `csv+padding` run 4: country: expected LU, got DE
- `csv+padding` run 5: country: expected LU, got DE

**Q43.** How many distinct entities are domiciled in Luxembourg (LU)?

- `csv` run 1: count: expected 1, got 0
- `csv` run 2: count: expected 1, got 0
- `csv` run 3: count: expected 1, got 0
- `csv` run 4: count: expected 1, got 0
- `csv` run 5: count: expected 1, got 0
- `rdf` run 1: count: expected 1, got 0
- `rdf` run 2: count: expected 1, got 0
- `rdf` run 5: count: expected 1, got 0
- `csv+padding` run 1: count: expected 1, got 0
- `csv+padding` run 2: count: expected 1, got 0
- `csv+padding` run 3: count: expected 1, got 0
- `csv+padding` run 4: count: expected 1, got 0
- `csv+padding` run 5: count: expected 1, got 0

**Q44.** Is Valdoria Telecom's 2027 note a local-currency obligation?

- `csv` run 3: local_currency: expected yes, got depends

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `csv` run 3: above_ceiling: expected no, got depends

**Q47.** How is Corvenia Power's 2034 note rated?

- `rdf` run 3: rating: expected none, got A

