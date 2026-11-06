# credit_300: claude:haiku, 2026-11-05 21:35

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **74%** | 62% to 85% | 7 of 48 |
| `rdf` | **63%** | 50% to 76% | 7 of 48 |
| `rdf+ontology` | **83%** | 74% to 92% | 7 of 48 |
| `csv+ontology` | **89%** | 80% to 96% | 5 of 48 |
| `csv+markdown` | **87%** | 78% to 95% | 7 of 48 |
| `csv+padding` | **69%** | 57% to 81% | 7 of 48 |
| `executed` | **91%** | 84% to 97% | 8 of 48 |
| `csv+neutral` | **88%** | 80% to 95% | 7 of 48 |
| `csv+axioms` | **88%** | 80% to 95% | 9 of 48 |
| `csv+axioms+markdown` | **85%** | 75% to 93% | 7 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -10 points | -17 to -4 |
| `rdf+ontology` | +10 points | +3 to +18 |
| `csv+ontology` | +15 points | +5 to +25 |
| `csv+markdown` | +13 points | +4 to +23 |
| `csv+padding` | -4 points | -8 to -1 |
| `executed` | +17 points | +7 to +28 |
| `csv+neutral` | +15 points | +7 to +23 |
| `csv+axioms` | +14 points | +7 to +23 |
| `csv+axioms+markdown` | +11 points | +2 to +20 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` | `executed` | `csv+neutral` | `csv+axioms` | `csv+axioms+markdown` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 ✅ ✅ 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | 🟡 🟡 🟡 ✅ 🟡 | 🟡 🟡 ❌ 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ❌ | ✅ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ✅ ❌ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q19 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ❌ | ✅ ❌ ✅ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ❌ | ✅ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ✅ ❌ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ❌ ❌ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ❌ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 ✅ ✅ 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ✅ ✅ ✅ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ❌ | ❌ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | code | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q48 | code | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ❌ | ✅ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ✅ ❌ |

## Lists, with partial credit

The 7 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 43% | 76% |
| `rdf` | 29% | 86% |
| `rdf+ontology` | 49% | 91% |
| `csv+ontology` | 57% | 95% |
| `csv+markdown` | 60% | 92% |
| `csv+padding` | 37% | 73% |
| `executed` | 63% | 98% |
| `csv+neutral` | 54% | 87% |
| `csv+axioms` | 60% | 89% |
| `csv+axioms+markdown` | 57% | 76% |

**The checklist grader agreed with itself** on 48 of 50 answers graded twice.

## Why each miss was marked

**Q4.** What is Northwind Holdings' current outlook?

- `csv` run 5: outlook: expected positive, got STA
- `rdf` run 1: outlook: expected positive, got Stable
- `rdf` run 2: outlook: expected positive, got STA
- `rdf` run 3: outlook: expected positive, got STA
- `rdf` run 4: outlook: expected positive, got STA
- `rdf` run 5: outlook: expected positive, got STA
- `csv+padding` run 1: outlook: expected positive, got STA
- `csv+padding` run 3: outlook: expected positive, got STA
- `csv+padding` run 4: outlook: expected positive, got STA

**Q5.** Whose credit risk does a holder of the Northwind Finance 2030 notes take, and how is it rated?

- `rdf` run 1: risk_of: expected E02, got E04
- `rdf` run 2: risk_of: expected E02, got E04
- `rdf` run 5: risk_of: expected E02, got E04
- `csv+padding` run 3: risk_of: expected E02, got E04

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `csv` run 1: Identifies the country ceiling (BB) as capping the FC rating, but never states that it applies to foreign-currency and not local-currency ratings; it also says the data doesn't state the reason explicitly, weakening the causal claim.
- `csv` run 2: Identifies the BB country ceiling matching the FC rating as consistent with a cap, but hedges ('no stated reason') and doesn't state that the ceiling caps FC but not LC ratings.
- `csv` run 3: Points to the BB country ceiling as consistent with the FC rating but explicitly declines to confirm it as the cause, and does not say the ceiling caps FC and not LC ratings.
- `csv` run 5: Identifies the FC rating matching the BB country ceiling, but hedges on causation and never states that the ceiling caps FC and not LC ratings.
- `rdf` run 1: Identifies the BB country ceiling as matching the foreign-currency rating, but hedges that the data doesn't state it as the cause and doesn't say the ceiling applies only to foreign-currency ratings.
- `rdf` run 2: Links FC rating to the BB country ceiling as consistent with a cap, but hedges that it isn't stated and doesn't say the ceiling applies to FC and not LC.
- `rdf` run 3: Does not name the Country Ceiling (BB) as the cause or say it caps foreign-currency ratings; states the reason is not recorded.
- `rdf` run 4: Notes FC rating equals the BB Country Ceiling, but hedges that the data doesn't state a cause and never says the ceiling caps FC and not LC ratings.
- `rdf` run 5: Notes FA BB matches the sovereign record and is consistent with a ceiling cap, but does not name the Country Ceiling as the cause or state that it caps foreign-currency only; claims the data gives no reason.
- `csv+ontology` run 3: No answer was provided, so neither checklist point is met.
- `csv+padding` run 1: Names the country ceiling (BB) as the consistent cause, but never states that the ceiling caps foreign-currency ratings and not local-currency ones.
- `csv+padding` run 2: Identifies the BB country ceiling matching the FC rating as a likely cap, but hedges it as inference rather than stating it as the cause, and doesn't say the ceiling applies to FC and not LC.
- `csv+padding` run 3: Identifies the BB sovereign ceiling and the FC/LC rating gap, but hedges that the cause isn't confirmed and never states the ceiling caps foreign-currency but not local-currency ratings.
- `csv+padding` run 4: Identifies the BB country ceiling as consistent with the FC rating but hedges and does not assert it as the cause, and never says the ceiling caps FC but not LC.
- `csv+padding` run 5: Notes the FC rating equals the BB country ceiling and that it fits a transfer cap, but hedges that the data doesn't state it as the cause and never says the ceiling applies to foreign- and not local-currency ratings.
- `executed` run 2: Names the BB country ceiling as the level the FC rating sits at, but never says the ceiling caps FC and not LC ratings, and disclaims giving the reason.
- `csv+axioms` run 2: Identifies the BB Country Ceiling as consistent with the FC rating but hedges that no source states it as the cause, and never says the ceiling caps FC but not LC ratings.

**Q7.** Which issuers were downgraded in 2026?

- `csv` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1349', 'E1350', 'E1351']
- `csv` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv` run 4: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv` run 5: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `rdf` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `rdf` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `rdf` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `rdf` run 4: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `rdf` run 5: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `rdf+ontology` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307']
- `rdf+ontology` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1300', 'E1307']
- `rdf+ontology` run 4: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1144', 'E1151', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307']
- `csv+ontology` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307']
- `csv+padding` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E11', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv+padding` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv+padding` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv+padding` run 4: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `csv+padding` run 5: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E16', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351']
- `executed` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E07', 'E08', 'E10', 'E1007', 'E1032', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1155', 'E1158', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1172', 'E1186', 'E1213', 'E1218', 'E1219', 'E1228', 'E1229', 'E1234', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1303', 'E1307']
- `csv+neutral` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307']
- `csv+axioms+markdown` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307'], got None

**Q9.** As of 1 October 2026, how many distinct issuers hold an issuer rating?

- `csv` run 1: count: expected 278, got 289
- `csv` run 2: count: expected 278, got None
- `csv` run 3: count: expected 278, got None
- `csv` run 4: count: expected 278, got None
- `csv` run 5: count: expected 278, got None
- `rdf` run 1: count: expected 278, got None
- `rdf` run 2: count: expected 278, got None
- `rdf` run 3: count: expected 278, got None
- `rdf` run 4: count: expected 278, got None
- `rdf` run 5: count: expected 278, got None
- `rdf+ontology` run 1: count: expected 278, got 270
- `rdf+ontology` run 2: count: expected 278, got 280
- `rdf+ontology` run 3: count: expected 278, got None
- `rdf+ontology` run 4: count: expected 278, got None
- `rdf+ontology` run 5: count: expected 278, got 268
- `csv+ontology` run 3: count: expected 278, got 277
- `csv+ontology` run 4: count: expected 278, got None
- `csv+markdown` run 1: count: expected 278, got None
- `csv+markdown` run 2: count: expected 278, got 281
- `csv+markdown` run 4: count: expected 278, got 277
- `csv+markdown` run 5: count: expected 278, got None
- `csv+padding` run 1: count: expected 278, got None
- `csv+padding` run 2: count: expected 278, got None
- `csv+padding` run 3: count: expected 278, got None
- `csv+padding` run 4: count: expected 278, got None
- `csv+padding` run 5: count: expected 278, got None
- `executed` run 1: count: expected 278, got 277
- `csv+neutral` run 1: count: expected 278, got 277
- `csv+neutral` run 2: count: expected 278, got 283
- `csv+neutral` run 4: count: expected 278, got None
- `csv+neutral` run 5: count: expected 278, got None
- `csv+axioms` run 2: count: expected 278, got None
- `csv+axioms` run 4: count: expected 278, got None
- `csv+axioms` run 5: count: expected 278, got None
- `csv+axioms+markdown` run 1: count: expected 278, got None
- `csv+axioms+markdown` run 2: count: expected 278, got None
- `csv+axioms+markdown` run 3: count: expected 278, got None
- `csv+axioms+markdown` run 5: count: expected 278, got None

**Q10.** Is Valdoria Telecom investment grade?

- `rdf+ontology` run 3: investment_grade: expected depends, got no
- `rdf+ontology` run 5: investment_grade: expected depends, got no
- `csv+ontology` run 1: investment_grade: expected depends, got no
- `csv+ontology` run 2: investment_grade: expected depends, got no
- `csv+ontology` run 3: investment_grade: expected depends, got no
- `csv+ontology` run 4: investment_grade: expected depends, got no
- `csv+ontology` run 5: investment_grade: expected depends, got no
- `csv+markdown` run 1: investment_grade: expected depends, got no
- `csv+markdown` run 2: investment_grade: expected depends, got no
- `csv+markdown` run 3: investment_grade: expected depends, got no
- `csv+markdown` run 4: investment_grade: expected depends, got no
- `csv+markdown` run 5: investment_grade: expected depends, got no
- `csv+axioms+markdown` run 1: investment_grade: expected depends, got no
- `csv+axioms+markdown` run 2: investment_grade: expected depends, got no
- `csv+axioms+markdown` run 3: investment_grade: expected depends, got no
- `csv+axioms+markdown` run 5: investment_grade: expected depends, got no

**Q16.** Has Marlow Utilities' rating changed since 1 January 2025?

- `executed` run 1: changed: expected no, got depends

**Q18.** Which issuers were on Rating Watch Negative on 1 October 2026?

- `csv` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1037', 'E1039', 'E1061', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1013', 'E1019', 'E1059', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1059', 'E1061', 'E1088', 'E1098', 'E1099', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1314', 'E1317', 'E1323']
- `csv` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got None
- `csv` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got None
- `csv` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf+ontology` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf+ontology` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf+ontology` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf+ontology` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `rdf+ontology` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+ontology` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+ontology` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+ontology` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1194', 'E1203', 'E1242', 'E1039', 'E1133', 'E1099', 'E1088', 'E1019', 'E1013', 'E1059', 'E1061', 'E1098', 'E1109', 'E1132', 'E1146', 'E1209', 'E1126', 'E1317', 'E1314', 'E1323', 'E1238', 'E1006', 'E1066', 'E1297', 'E1266', 'E1181', 'E1168', 'E1260', 'E1264']
- `csv+ontology` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1126', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+ontology` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+markdown` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1098', 'E1297', 'E1266', 'E1267', 'E1194', 'E1203', 'E1133', 'E1088', 'E1146', 'E1317', 'E1209', 'E1019', 'E1059', 'E1126', 'E1013', 'E1037', 'E1061', 'E1099', 'E1109', 'E1132', 'E1168', 'E1181', 'E1242', 'E1264', 'E1314', 'E1323', 'E1260', 'E1238']
- `csv+markdown` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1194', 'E1203', 'E1126', 'E1132', 'E1133', 'E1146', 'E1181', 'E1209', 'E1238', 'E1242', 'E1260', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323', 'E1013', 'E1037', 'E1061', 'E1059', 'E1098', 'E1099', 'E1109', 'E1088', 'E1168', 'E1019']
- `csv+markdown` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1242', 'E1194', 'E1203', 'E1133', 'E1088', 'E1209', 'E1019', 'E1146', 'E1317', 'E1013', 'E1099', 'E1098', 'E1168', 'E1314', 'E1264', 'E1132', 'E1059', 'E1126', 'E1266', 'E1238', 'E1323', 'E1297', 'E1109', 'E1181', 'E1061', 'E1037', 'E1066', 'E1260', 'E1039', 'E1006']
- `csv+markdown` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1194', 'E1203', 'E1099', 'E1088', 'E1133', 'E1132', 'E1109', 'E1098', 'E1059', 'E1168', 'E1181', 'E1209', 'E1242', 'E1264', 'E1266', 'E1297', 'E1314', 'E1317', 'E1323', 'E1013', 'E1019', 'E1061', 'E1066', 'E1126', 'E1146', 'E1260', 'E1238', 'E1037', 'E1039', 'E1006']
- `csv+markdown` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+padding` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1194', 'E1181', 'E1203', 'E1210', 'E1019', 'E1059', 'E1013', 'E1061', 'E1037', 'E1088', 'E1098', 'E1099', 'E1126', 'E1132', 'E1133', 'E1146', 'E1264', 'E1266', 'E1267', 'E1317', 'E1323', 'E1238', 'E1260', 'E1297', 'E1314', 'E1109', 'E1168', 'E1039']
- `csv+padding` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1059', 'E1061', 'E1066', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1242', 'E1260', 'E1264', 'E1266', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+padding` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1059', 'E1061', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+padding` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1194', 'E1203', 'E1242', 'E1039', 'E1133', 'E1088', 'E1210', 'E1019', 'E1317', 'E1098', 'E1059', 'E1132', 'E1146', 'E1013', 'E1099', 'E1109', 'E1264', 'E1266', 'E1314', 'E1061', 'E1037', 'E1238', 'E1297', 'E1323', 'E1181', 'E1260', 'E1168', 'E1126']
- `csv+padding` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got None
- `executed` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `executed` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `executed` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `executed` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `executed` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+neutral` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1194', 'E1203', 'E1133', 'E1088', 'E1099', 'E1109', 'E1098', 'E1209', 'E1168', 'E1181', 'E1242', 'E1260', 'E1264', 'E1266', 'E1297', 'E1314', 'E1317', 'E1323', 'E1146', 'E1013', 'E1059', 'E1061', 'E1037', 'E1126', 'E1132', 'E1238', 'E1066']
- `csv+neutral` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1066', 'E1098', 'E1238', 'E1266', 'E1297']
- `csv+neutral` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+neutral` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got None
- `csv+neutral` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1194', 'E1203', 'E1133', 'E1088', 'E1099', 'E1019', 'E1168', 'E1209', 'E1098', 'E1037', 'E1061', 'E1264', 'E1132', 'E1126', 'E1059', 'E1314', 'E1317', 'E1146', 'E1013', 'E1181', 'E1266', 'E1238', 'E1297', 'E1323', 'E1260', 'E1066', 'E1242', 'E1109', 'E1039']
- `csv+axioms` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+axioms` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+axioms` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+axioms` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1267', 'E1242', 'E1194', 'E1203', 'E1019', 'E1133', 'E1088', 'E1209', 'E1146', 'E1317', 'E1126', 'E1013', 'E1059', 'E1061', 'E1066', 'E1098', 'E1099', 'E1109', 'E1132', 'E1168', 'E1181', 'E1238', 'E1266', 'E1297', 'E1314', 'E1323', 'E1264', 'E1039', 'E1260']
- `csv+axioms` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1039', 'E1242', 'E1194', 'E1203', 'E1133', 'E1132', 'E1088', 'E1099', 'E1098', 'E1168', 'E1209', 'E1264', 'E1314', 'E1317', 'E1146', 'E1126', 'E1013', 'E1066', 'E1109', 'E1181', 'E1260', 'E1266', 'E1297', 'E1323', 'E1238', 'E1267', 'E1037', 'E1061']
- `csv+axioms+markdown` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1006', 'E1019', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1126', 'E1132', 'E1133', 'E1146', 'E1181', 'E1194', 'E1203', 'E1238', 'E1264', 'E1266', 'E1267', 'E1297', 'E1317']
- `csv+axioms+markdown` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1181', 'E1194', 'E1203', 'E1210', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323']
- `csv+axioms+markdown` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got None
- `csv+axioms+markdown` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1194', 'E1203', 'E1099', 'E1133', 'E1132', 'E1168', 'E1059', 'E1146', 'E1210', 'E1126', 'E1181', 'E1238', 'E1242', 'E1266', 'E1264', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323', 'E1061', 'E1037', 'E1019', 'E1013', 'E1039', 'E1109', 'E1098', 'E1006', 'E1088']
- `csv+axioms+markdown` run 5: issuers: expected ['E06', 'E1006', 'E1013', 'E1037', 'E1039', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got None

**Q19.** Which issuers had a Negative outlook on 1 October 2026?

- `csv` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1161', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1262', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1347', 'E1348', 'E1350', 'E1351']
- `csv` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `rdf` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1029', 'E1034', 'E1046', 'E1055', 'E1060', 'E1064', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1161', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1262', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1347', 'E1348', 'E1350', 'E1351']
- `rdf` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1057', 'E1060', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1172', 'E1188', 'E1190', 'E1211', 'E1228', 'E1262', 'E1271', 'E1282', 'E1294', 'E1300', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1347', 'E1348', 'E1350', 'E1351']
- `rdf` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `rdf` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `rdf` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1060', 'E1064', 'E1072', 'E1079', 'E1080', 'E1132', 'E1190', 'E1211', 'E1248', 'E1262', 'E1282', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1347', 'E1348', 'E1350', 'E1351']
- `rdf+ontology` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1118', 'E1146', 'E1161', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1262', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `rdf+ontology` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1079', 'E1080', 'E1160', 'E1188', 'E1190', 'E1211', 'E1261', 'E1263', 'E1271', 'E1294', 'E1300']
- `rdf+ontology` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `rdf+ontology` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `rdf+ontology` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1060', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1161', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+ontology` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1161', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+ontology` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+ontology` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+ontology` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+ontology` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+markdown` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1158', 'E1064', 'E1034', 'E1080', 'E1105', 'E1079', 'E1132', 'E1146', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1294', 'E1300', 'E1072', 'E1029', 'E1046', 'E1055', 'E1056', 'E1059', 'E1118', 'E1160', 'E1282']
- `csv+markdown` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1034', 'E1046', 'E1055', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1029', 'E1056', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E1160']
- `csv+markdown` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1158', 'E1190', 'E1188', 'E1079', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E1160', 'E1118', 'E1211', 'E1034', 'E1029', 'E1132', 'E1146', 'E1105', 'E1080', 'E1064', 'E1072', 'E1046', 'E1056', 'E1055', 'E1059']
- `csv+markdown` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+padding` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+padding` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+padding` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+padding` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+padding` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `executed` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `executed` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `executed` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+neutral` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+neutral` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1055', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1132', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1300']
- `csv+neutral` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1160', 'E1188', 'E1190', 'E1196', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+neutral` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+neutral` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+axioms` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1034', 'E1046', 'E1055', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+axioms` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+axioms` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+axioms` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1029', 'E1034', 'E1046', 'E1056', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+axioms+markdown` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E1158']
- `csv+axioms+markdown` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+axioms+markdown` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None
- `csv+axioms+markdown` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1132', 'E1146', 'E1158', 'E1161', 'E1188', 'E1190', 'E1228', 'E1248', 'E1262', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300']
- `csv+axioms+markdown` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300'], got None

**Q21.** Which entities had an issuer rating at some point but no longer had one on 1 October 2026?

- `csv` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1032', 'E1041', 'E1057', 'E1062', 'E1063', 'E1076', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got None
- `csv` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1124', 'E1032', 'E1002', 'E1063', 'E1279', 'E1308', 'E1140', 'E1320', 'E1138', 'E1155', 'E1159', 'E1172', 'E1166', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1048', 'E1041', 'E1062', 'E1076', 'E1107', 'E1121', 'E1007', 'E1021', 'E1057', 'E1316']
- `rdf` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `rdf` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1115', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1158', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1303', 'E1308', 'E1316', 'E1320']
- `rdf` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `rdf` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1115', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1308', 'E1316', 'E1320']
- `rdf` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1115', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1303', 'E1308', 'E1316', 'E1320']
- `rdf+ontology` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1115', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `rdf+ontology` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320']
- `rdf+ontology` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1002', 'E07', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1106', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+ontology` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+ontology` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+ontology` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+ontology` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+markdown` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1124', 'E1032', 'E1063', 'E1218', 'E1219', 'E1225', 'E1234', 'E1205', 'E1206', 'E1233', 'E1253', 'E1277', 'E1279', 'E1138', 'E1140', 'E1155', 'E1159', 'E1172', 'E1166', 'E1200', 'E1062', 'E1076', 'E1041', 'E1048', 'E1057', 'E1107', 'E1121', 'E1244', 'E1308', 'E1316', 'E1320', 'E1007', 'E1021', 'E1084']
- `csv+markdown` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1124', 'E1032', 'E1063', 'E1279', 'E1084', 'E1308', 'E1218', 'E1219', 'E1057', 'E1159', 'E1155', 'E1234', 'E1244', 'E1200', 'E1166', 'E1076', 'E1107', 'E1041', 'E1048', 'E1121', 'E1140', 'E1138', 'E1062', 'E1172', 'E1205', 'E1206', 'E1233', 'E1277', 'E1316', 'E1320', 'E1225']
- `csv+markdown` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1124', 'E1032', 'E1063', 'E1233', 'E1001', 'E1279', 'E1218', 'E1206', 'E1084', 'E1205', 'E1121', 'E1041', 'E1062', 'E1140', 'E1200', 'E1225', 'E1107', 'E1076', 'E1048', 'E1155', 'E1159', 'E1057', 'E1007', 'E1021', 'E1253', 'E1138', 'E1166', 'E1244', 'E1316', 'E1277', 'E1172', 'E1308', 'E1234', 'E1320', 'E1219']
- `csv+markdown` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got None
- `csv+padding` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1032', 'E1057', 'E1124']
- `csv+padding` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got None
- `csv+padding` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1032', 'E1041', 'E1057', 'E1062', 'E1063', 'E1085', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1234', 'E1244', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+padding` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1032', 'E1063', 'E1138', 'E1140', 'E1155', 'E1159', 'E1172', 'E1166', 'E1041', 'E1062', 'E1076', 'E1107', 'E1121', 'E1124', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320', 'E1007', 'E1021', 'E1002', 'E1057']
- `csv+padding` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+neutral` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1115', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320', 'E07']
- `csv+neutral` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1007', 'E1032', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1244', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+neutral` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1124', 'E1032', 'E1063', 'E1084', 'E1218', 'E1279', 'E1138', 'E1001', 'E1140', 'E1076', 'E1062', 'E1041', 'E1205', 'E1206', 'E1233', 'E1225', 'E1277', 'E1200', 'E1166', 'E1244', 'E1021', 'E1320', 'E1107', 'E1121', 'E1155', 'E1316', 'E1308', 'E1172', 'E1159', 'E1234', 'E1219', 'E1048', 'E1057', 'E1007']
- `csv+neutral` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+axioms` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1002', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1254', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+axioms` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got None
- `csv+axioms` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1032', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1205', 'E1206', 'E1218', 'E1219', 'E1021', 'E1041', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+axioms+markdown` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1115', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1277', 'E1279', 'E1308', 'E1316', 'E1320']
- `csv+axioms+markdown` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got None
- `csv+axioms+markdown` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1124', 'E1032', 'E1218', 'E1308', 'E1063', 'E1279', 'E1084', 'E1140', 'E1225', 'E1002', 'E1007', 'E1076', 'E1206', 'E1062', 'E1121', 'E1048', 'E1107', 'E1233', 'E1234', 'E1205', 'E1041', 'E1155', 'E1166', 'E1159', 'E1320', 'E1316', 'E1244', 'E1200', 'E1254', 'E1172', 'E1057', 'E1277', 'E1219', 'E1021']
- `csv+axioms+markdown` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1032', 'E1048', 'E1057', 'E1063', 'E1076', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1277', 'E1308', 'E1316', 'E1320']

**Q25.** How many instruments held an investment-grade rating on 1 October 2026?

- `csv` run 1: count: expected 66, got 69
- `csv` run 3: count: expected 66, got None
- `csv` run 4: count: expected 66, got None
- `csv` run 5: count: expected 66, got None
- `rdf` run 1: count: expected 66, got 69
- `rdf` run 2: count: expected 66, got None
- `rdf` run 3: count: expected 66, got None
- `rdf` run 4: count: expected 66, got None
- `rdf` run 5: count: expected 66, got 69
- `rdf+ontology` run 3: count: expected 66, got None
- `rdf+ontology` run 4: count: expected 66, got None
- `csv+markdown` run 5: count: expected 66, got None
- `csv+padding` run 1: count: expected 66, got None
- `csv+padding` run 2: count: expected 66, got None
- `csv+padding` run 3: count: expected 66, got None
- `csv+padding` run 4: count: expected 66, got 69
- `csv+padding` run 5: count: expected 66, got None
- `csv+neutral` run 4: count: expected 66, got None
- `csv+neutral` run 5: count: expected 66, got None
- `csv+axioms` run 2: count: expected 66, got None
- `csv+axioms` run 4: count: expected 66, got None
- `csv+axioms` run 5: count: expected 66, got None
- `csv+axioms+markdown` run 1: count: expected 66, got None
- `csv+axioms+markdown` run 2: count: expected 66, got None
- `csv+axioms+markdown` run 3: count: expected 66, got None
- `csv+axioms+markdown` run 5: count: expected 66, got None

**Q29.** What is the Republic of Valdoria's issuer rating?

- `rdf` run 2: rating: expected none, got BB
- `rdf` run 3: rating: expected none, got BB
- `rdf` run 5: rating: expected none, got BB
- `csv+padding` run 3: rating: expected none, got BB

**Q30.** Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?

- `rdf` run 1: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194']
- `rdf` run 2: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1101', 'E1126', 'E15', 'E1194']
- `rdf` run 3: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E15', 'E1194', 'E1028', 'E1101', 'E1126', 'E1236']
- `rdf` run 4: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1101', 'E1028', 'E1126', 'E1236', 'E15', 'E1194']
- `rdf` run 5: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1101', 'E1126', 'E1236', 'E15', 'E1039', 'E1194']
- `rdf+ontology` run 3: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1101', 'E1236', 'E15', 'E1039', 'E1194']
- `rdf+ontology` run 4: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1101', 'E1126', 'E1194', 'E15']
- `csv+markdown` run 4: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1101', 'E1126', 'E1236', 'E15', 'E1194']
- `csv+padding` run 1: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1126', 'E1236', 'E15', 'E1039', 'E1194']
- `csv+padding` run 2: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1126', 'E1236', 'E15', 'E1039', 'E1194']
- `executed` run 1: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E15', 'E1194', 'E05', 'E1028', 'E1101', 'E1126', 'E1236']
- `executed` run 2: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E15', 'E1028', 'E1101', 'E1126', 'E1194', 'E1236']
- `executed` run 3: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E15', 'E1028', 'E1101', 'E1126', 'E1194', 'E1236']
- `executed` run 5: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E15', 'E1028', 'E1101', 'E1126', 'E1194', 'E1236']
- `csv+neutral` run 1: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1126', 'E1236', 'E15', 'E1039', 'E1194']
- `csv+axioms` run 1: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1101', 'E1126', 'E1236', 'E15', 'E1194']
- `csv+axioms` run 3: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15'], got ['E05', 'E1028', 'E1101', 'E1126', 'E1236']

**Q33.** Whose credit risk does a holder of the Halden Leasing 2028 notes take, and how is it rated?

- `rdf` run 1: risk_of: expected E10, got E11
- `rdf` run 2: risk_of: expected E10, got E11
- `rdf` run 5: risk_of: expected E10, got E11
- `csv+padding` run 3: risk_of: expected E10, got E11

**Q37.** How many distinct legal entities does the data describe?

- `csv` run 1: count: expected 331, got 344
- `csv` run 2: count: expected 331, got 344
- `csv` run 3: count: expected 331, got 344
- `csv` run 4: count: expected 331, got None
- `csv` run 5: count: expected 331, got None
- `rdf` run 1: count: expected 331, got None
- `rdf` run 2: count: expected 331, got None
- `rdf` run 3: count: expected 331, got None
- `rdf` run 4: count: expected 331, got None
- `rdf` run 5: count: expected 331, got None
- `rdf+ontology` run 1: count: expected 331, got 280
- `rdf+ontology` run 2: count: expected 331, got 332
- `rdf+ontology` run 3: count: expected 331, got None
- `rdf+ontology` run 4: count: expected 331, got None
- `rdf+ontology` run 5: count: expected 331, got 327
- `csv+markdown` run 5: count: expected 331, got None
- `csv+padding` run 1: count: expected 331, got 344
- `csv+padding` run 2: count: expected 331, got 342
- `csv+padding` run 3: count: expected 331, got 344
- `csv+padding` run 4: count: expected 331, got 344
- `csv+padding` run 5: count: expected 331, got None
- `csv+axioms` run 2: count: expected 331, got 344
- `csv+axioms+markdown` run 3: count: expected 331, got None

**Q40.** How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?

- `csv` run 1: count: expected 66, got 74
- `csv` run 2: count: expected 66, got None
- `csv` run 3: count: expected 66, got None
- `csv` run 4: count: expected 66, got None
- `csv` run 5: count: expected 66, got None
- `rdf` run 1: count: expected 66, got None
- `rdf` run 2: count: expected 66, got None
- `rdf` run 3: count: expected 66, got None
- `rdf` run 4: count: expected 66, got None
- `rdf` run 5: count: expected 66, got None
- `rdf+ontology` run 1: count: expected 66, got 65
- `rdf+ontology` run 2: count: expected 66, got 65
- `rdf+ontology` run 3: count: expected 66, got None
- `rdf+ontology` run 4: count: expected 66, got None
- `rdf+ontology` run 5: count: expected 66, got 64
- `csv+ontology` run 1: count: expected 66, got 64
- `csv+ontology` run 2: count: expected 66, got 65
- `csv+ontology` run 3: count: expected 66, got 65
- `csv+ontology` run 4: count: expected 66, got 65
- `csv+markdown` run 1: count: expected 66, got 65
- `csv+markdown` run 2: count: expected 66, got None
- `csv+markdown` run 3: count: expected 66, got 62
- `csv+markdown` run 4: count: expected 66, got 65
- `csv+markdown` run 5: count: expected 66, got None
- `csv+padding` run 1: count: expected 66, got None
- `csv+padding` run 2: count: expected 66, got None
- `csv+padding` run 3: count: expected 66, got None
- `csv+padding` run 4: count: expected 66, got None
- `csv+padding` run 5: count: expected 66, got None
- `executed` run 1: count: expected 66, got 65
- `executed` run 2: count: expected 66, got 65
- `executed` run 4: count: expected 66, got 65
- `executed` run 5: count: expected 66, got 65
- `csv+neutral` run 1: count: expected 66, got 65
- `csv+neutral` run 2: count: expected 66, got None
- `csv+neutral` run 4: count: expected 66, got None
- `csv+neutral` run 5: count: expected 66, got None
- `csv+axioms` run 2: count: expected 66, got None
- `csv+axioms` run 3: count: expected 66, got 65
- `csv+axioms` run 4: count: expected 66, got None
- `csv+axioms` run 5: count: expected 66, got None
- `csv+axioms+markdown` run 1: count: expected 66, got None
- `csv+axioms+markdown` run 2: count: expected 66, got None
- `csv+axioms+markdown` run 3: count: expected 66, got None
- `csv+axioms+markdown` run 4: count: expected 66, got 64
- `csv+axioms+markdown` run 5: count: expected 66, got None

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
- `rdf+ontology` run 2: rating: expected none, got BB+
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

- `csv` run 2: count: expected 1, got 0

**Q44.** Is Valdoria Telecom's 2027 note a local-currency obligation?

- `rdf` run 5: local_currency: expected yes, got depends

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `csv` run 1: above_ceiling: expected no, got depends
- `csv` run 5: above_ceiling: expected no, got yes
- `rdf` run 1: above_ceiling: expected no, got depends
- `rdf` run 3: above_ceiling: expected no, got depends
- `rdf` run 4: above_ceiling: expected no, got depends
- `rdf` run 5: above_ceiling: expected no, got depends
- `csv+padding` run 1: above_ceiling: expected no, got depends
- `csv+padding` run 2: above_ceiling: expected no, got yes
- `csv+padding` run 5: above_ceiling: expected no, got depends
- `executed` run 1: above_ceiling: expected no, got depends
- `executed` run 2: above_ceiling: expected no, got yes

**Q46.** Does Halden Leasing have an issuer rating?

- `rdf` run 1: issuer_rating: expected no, got depends
- `rdf` run 3: issuer_rating: expected no, got depends
- `rdf` run 4: issuer_rating: expected no, got depends
- `rdf` run 5: issuer_rating: expected no, got yes
- `csv+padding` run 3: issuer_rating: expected no, got depends

**Q47.** How is Corvenia Power's 2034 note rated?

- `csv` run 1: rating: expected none, got A
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

- `csv` run 1: count: expected 106, got 112
- `csv` run 3: count: expected 106, got None
- `csv` run 4: count: expected 106, got None
- `csv` run 5: count: expected 106, got None
- `rdf` run 1: count: expected 106, got 112
- `rdf` run 2: count: expected 106, got None
- `rdf` run 3: count: expected 106, got None
- `rdf` run 4: count: expected 106, got None
- `rdf` run 5: count: expected 106, got 112
- `rdf+ontology` run 3: count: expected 106, got None
- `rdf+ontology` run 4: count: expected 106, got None
- `csv+markdown` run 5: count: expected 106, got None
- `csv+padding` run 1: count: expected 106, got None
- `csv+padding` run 2: count: expected 106, got None
- `csv+padding` run 3: count: expected 106, got None
- `csv+padding` run 4: count: expected 106, got 112
- `csv+padding` run 5: count: expected 106, got None
- `csv+neutral` run 4: count: expected 106, got None
- `csv+neutral` run 5: count: expected 106, got None
- `csv+axioms` run 2: count: expected 106, got None
- `csv+axioms` run 4: count: expected 106, got None
- `csv+axioms` run 5: count: expected 106, got None
- `csv+axioms+markdown` run 1: count: expected 106, got None
- `csv+axioms+markdown` run 2: count: expected 106, got None
- `csv+axioms+markdown` run 3: count: expected 106, got None
- `csv+axioms+markdown` run 5: count: expected 106, got None

