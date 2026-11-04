# research: claude:haiku, 2026-11-04 17:52

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **44%** | 30% to 57% | 5 of 48 |
| `rdf` | **44%** | 30% to 58% | 3 of 48 |
| `rdf+ontology` | **97%** | 93% to 100% | 2 of 48 |
| `csv+ontology` | **97%** | 92% to 100% | 1 of 48 |
| `csv+markdown` | **96%** | 92% to 99% | 6 of 48 |
| `csv+padding` | **45%** | 32% to 59% | 7 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | +0 points | -4 to +6 |
| `rdf+ontology` | +54 points | +40 to +67 |
| `csv+ontology` | +54 points | +40 to +67 |
| `csv+markdown` | +52 points | +39 to +65 |
| `csv+padding` | +2 points | -1 to +5 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` | `csv+markdown` | `csv+padding` |
|---|---|---|---|---|---|---|---|
| Q1 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ✅ ❌ ❌ ✅ ❌ |
| Q2 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ❌ ❌ ✅ ❌ ✅ | ✅ ❌ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ❌ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q11 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ✅ ❌ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ❌ ❌ ✅ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ❌ ❌ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q26 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q33 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q35 | code | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ |
| Q36 | code | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q47 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | 🟡 ✅ 🟡 🟡 🟡 | ✅ 🟡 🟡 ✅ 🟡 | 🟡 🟡 ✅ 🟡 ✅ |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 33% | 89% |
| `rdf` | 33% | 89% |
| `rdf+ontology` | 100% | 100% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 100% | 100% |
| `csv+padding` | 33% | 89% |

**The checklist grader agreed with itself** on 52 of 60 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf+ontology` run 1: count: expected 2, got 1
- `rdf+ontology` run 2: count: expected 2, got 1
- `rdf+ontology` run 4: count: expected 2, got 1
- `rdf+ontology` run 5: count: expected 2, got 1
- `csv+ontology` run 1: count: expected 2, got 1
- `csv+ontology` run 2: count: expected 2, got 1
- `csv+ontology` run 3: count: expected 2, got 1
- `csv+ontology` run 4: count: expected 2, got 1
- `csv+ontology` run 5: count: expected 2, got 1
- `csv+markdown` run 1: count: expected 2, got 1
- `csv+markdown` run 2: count: expected 2, got 1
- `csv+markdown` run 4: count: expected 2, got 1
- `csv+markdown` run 5: count: expected 2, got 1
- `csv+padding` run 2: count: expected 2, got 1
- `csv+padding` run 3: count: expected 2, got 1
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
- `csv+padding` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `csv` run 1: author: expected A01, got A07
- `csv` run 2: author: expected A01, got A07
- `csv` run 4: author: expected A01, got A07
- `rdf` run 2: author: expected A01, got A07
- `rdf` run 4: author: expected A01, got A07
- `rdf` run 5: author: expected A01, got A07
- `csv+markdown` run 1: author: expected A01, got tie: A01, A07
- `csv+padding` run 1: author: expected A01, got A07
- `csv+padding` run 2: author: expected A01, got A07
- `csv+padding` run 4: author: expected A01, got A07
- `csv+padding` run 5: author: expected A01, got A07

**Q7.** How many research works has Mara Ellison authored?

- `csv` run 1: count: expected 5, got 3
- `csv` run 2: count: expected 5, got 3
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 7
- `csv` run 5: count: expected 5, got 6
- `rdf` run 1: count: expected 5, got 7
- `rdf` run 2: count: expected 5, got 7
- `rdf` run 3: count: expected 5, got 7
- `rdf` run 4: count: expected 5, got 3
- `rdf` run 5: count: expected 5, got 3
- `csv+padding` run 1: count: expected 5, got 3
- `csv+padding` run 2: count: expected 5, got 6
- `csv+padding` run 3: count: expected 5, got 7
- `csv+padding` run 4: count: expected 5, got 7
- `csv+padding` run 5: count: expected 5, got 7

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 8, got 13
- `csv` run 2: count: expected 8, got 13
- `csv` run 3: count: expected 8, got 12
- `csv` run 4: count: expected 8, got 13
- `csv` run 5: count: expected 8, got 12
- `rdf` run 1: count: expected 8, got 13
- `rdf` run 2: count: expected 8, got 13
- `rdf` run 3: count: expected 8, got 13
- `rdf` run 4: count: expected 8, got 13
- `rdf` run 5: count: expected 8, got 13
- `csv+markdown` run 1: count: expected 8, got 7
- `csv+padding` run 1: count: expected 8, got 13
- `csv+padding` run 2: count: expected 8, got 12
- `csv+padding` run 3: count: expected 8, got 13
- `csv+padding` run 4: count: expected 8, got 13
- `csv+padding` run 5: count: expected 8, got 13

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 12, got 17
- `csv` run 2: count: expected 12, got 17
- `csv` run 3: count: expected 12, got 16
- `csv` run 4: count: expected 12, got 17
- `csv` run 5: count: expected 12, got 16
- `rdf` run 1: count: expected 12, got 17
- `rdf` run 2: count: expected 12, got 17
- `rdf` run 3: count: expected 12, got 17
- `rdf` run 4: count: expected 12, got 17
- `rdf` run 5: count: expected 12, got 17
- `csv+markdown` run 1: count: expected 12, got 11
- `csv+padding` run 1: count: expected 12, got 17
- `csv+padding` run 2: count: expected 12, got 16
- `csv+padding` run 3: count: expected 12, got 17
- `csv+padding` run 4: count: expected 12, got 17
- `csv+padding` run 5: count: expected 12, got 17

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 1: count: expected 6, got 9
- `csv` run 2: count: expected 6, got 9
- `csv` run 3: count: expected 6, got 10
- `csv` run 4: count: expected 6, got 9
- `csv` run 5: count: expected 6, got 9
- `rdf` run 1: count: expected 6, got 9
- `rdf` run 2: count: expected 6, got 9
- `rdf` run 3: count: expected 6, got 9
- `rdf` run 4: count: expected 6, got 9
- `rdf` run 5: count: expected 6, got 9
- `csv+padding` run 1: count: expected 6, got 10
- `csv+padding` run 2: count: expected 6, got 9
- `csv+padding` run 3: count: expected 6, got 9
- `csv+padding` run 4: count: expected 6, got 10
- `csv+padding` run 5: count: expected 6, got 9

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `rdf` run 3: fractional: expected 6, got 5.0

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

- `csv` run 1: count: expected 4, got 5
- `csv` run 2: count: expected 4, got 5
- `csv` run 3: count: expected 4, got 3
- `csv` run 4: count: expected 4, got 5
- `rdf` run 2: count: expected 4, got 5
- `rdf` run 3: count: expected 4, got 5
- `rdf` run 4: count: expected 4, got 5
- `rdf` run 5: count: expected 4, got 5
- `csv+padding` run 1: count: expected 4, got 5
- `csv+padding` run 3: count: expected 4, got 5
- `csv+padding` run 5: count: expected 4, got 5

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `csv` run 1: count: expected 4, got 5
- `csv` run 2: count: expected 4, got 5
- `csv` run 4: count: expected 4, got 5
- `rdf` run 1: count: expected 4, got 5
- `rdf` run 2: count: expected 4, got 5
- `rdf` run 3: count: expected 4, got 5
- `rdf` run 4: count: expected 4, got 5
- `rdf` run 5: count: expected 4, got 5
- `csv+padding` run 1: count: expected 4, got 5
- `csv+padding` run 3: count: expected 4, got 5
- `csv+padding` run 4: count: expected 4, got 5
- `csv+padding` run 5: count: expected 4, got 5

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
- `csv` run 5: count: expected 6, got 10
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

- `csv` run 1: counts: expected no, got yes
- `csv` run 2: counts: expected no, got depends
- `csv` run 3: counts: expected no, got depends
- `csv` run 4: counts: expected no, got depends
- `csv` run 5: counts: expected no, got depends
- `rdf` run 1: counts: expected no, got yes
- `rdf` run 2: counts: expected no, got depends
- `rdf` run 3: counts: expected no, got yes
- `rdf` run 4: counts: expected no, got depends
- `rdf` run 5: counts: expected no, got depends
- `csv+padding` run 1: counts: expected no, got depends
- `csv+padding` run 2: counts: expected no, got yes
- `csv+padding` run 3: counts: expected no, got depends
- `csv+padding` run 4: counts: expected no, got depends
- `csv+padding` run 5: counts: expected no, got depends

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
- `csv` run 2: count: expected 3, got 5
- `csv` run 3: count: expected 3, got 6
- `csv` run 4: count: expected 3, got 5
- `csv` run 5: count: expected 3, got 5
- `rdf` run 1: count: expected 3, got 5
- `rdf` run 2: count: expected 3, got 5
- `rdf` run 3: count: expected 3, got 5
- `rdf` run 4: count: expected 3, got 5
- `rdf` run 5: count: expected 3, got 5
- `csv+padding` run 1: count: expected 3, got 6
- `csv+padding` run 2: count: expected 3, got 5
- `csv+padding` run 3: count: expected 3, got 5
- `csv+padding` run 4: count: expected 3, got 6
- `csv+padding` run 5: count: expected 3, got 5

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1
- `rdf` run 1: count: expected 2, got 1
- `rdf` run 2: count: expected 2, got 1
- `rdf` run 3: count: expected 2, got 0
- `rdf` run 4: count: expected 2, got 1
- `rdf` run 5: count: expected 2, got 1
- `csv+padding` run 2: count: expected 2, got 1
- `csv+padding` run 3: count: expected 2, got 1
- `csv+padding` run 5: count: expected 2, got 1

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 1: count: expected 2, got 0
- `csv` run 2: count: expected 2, got 0
- `csv` run 4: count: expected 2, got 0
- `csv` run 5: count: expected 2, got 0
- `rdf` run 1: count: expected 2, got 0
- `rdf` run 2: count: expected 2, got 0
- `rdf` run 3: count: expected 2, got 0
- `rdf` run 4: count: expected 2, got 0
- `rdf` run 5: count: expected 2, got 0
- `csv+padding` run 2: count: expected 2, got 0
- `csv+padding` run 3: count: expected 2, got 0
- `csv+padding` run 5: count: expected 2, got 0

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04
- `csv` run 2: institution: expected I06, got I04
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04
- `rdf` run 1: institution: expected I06, got I04
- `rdf` run 2: institution: expected I06, got I04, I06
- `rdf` run 3: institution: expected I06, got I04
- `rdf` run 4: institution: expected I06, got I04
- `rdf` run 5: institution: expected I06, got I04
- `csv+padding` run 1: institution: expected I06, got I04
- `csv+padding` run 2: institution: expected I06, got I04 and I06
- `csv+padding` run 3: institution: expected I06, got I04
- `csv+padding` run 4: institution: expected I06, got I04
- `csv+padding` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `rdf` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `rdf` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `rdf` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
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
- `csv+markdown` run 4: count: expected 3, got 4
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

- `csv` run 1: Gives the quarter-share for Rostval and the larger Kesting shares via W22 and W20, but omits W21 and the half-share of W20 and W21 detail; mostly matches both points though less specific
- `csv` run 2: Correctly says Rostval holds one of four author slots per work and Kesting has larger shares (2.0 vs 1.0), but doesn't name W22 as a single-author review or the half shares on W20/W21, and the 'quarter each' is only implied.
- `csv` run 3: Gets the four-author, 1/4 credit point for Rostval, and notes Kesting has fewer authors (W20 two, W22 one), but never says only one of Rostval's four authors is from Rostval, and doesn't state Kesting's half of W20/W21 explicitly.
- `csv` run 4: Gives the Rostval four-authors/0.25 share point and says Kesting's shares are larger, but misdescribes W20 (checklist says Kesting holds half) and omits W22 being a single-author review credited to Kesting in full; the W22 and half-of-W20/W21 detail is not clearly matched.
- `csv` run 5: Gets Rostval's quarter shares (1 of 4 authors each) but only gives Kesting's totals (3 full, 2.0 fractional), not the W22 single-author review and half shares of W20/W21.
- `rdf` run 1: Rostval's quarter share per work is right, but Kesting is described only loosely: W22 is not said to be a single-author review, and W20/W21 are not identified as half shares.
- `rdf` run 2: Gives Kesting's shares (W22 full, ½ each of W20/W21) but says I09 gets ¼ of each work without stating that each has four authors with only one from Rostval
- `rdf` run 3: Gets Rostval's four-author works (1/4 each) and Kesting's W22 single-author and W20 two-author, but omits W21 and says Rostval has 4 works at 1/4 each only implicitly; misses that Kesting holds half of W20 and W21 explicitly.
- `rdf` run 4: Rostval's quarter shares are correct, and W22 is named as single-authored, but the answer never says Kesting holds half of W20 and W21, only that its other shares are larger.
- `rdf` run 5: Gets Rostval's quarter-share per work, but omits Kesting's W21 half share and misattributes W22/W20 detail incompletely (W20 half stated, W21 missing).
- `rdf+ontology` run 1: Gets Rostval's four works at 0.25 each and W22 single-author, but omits Kesting's half-shares of W20 and W21 (only says 'fewer authors').
- `rdf+ontology` run 2: Rostval's four works at 1/4 each is covered (though it lists W21, W27-29 and doesn't state four authors per work explicitly), but Kesting's shares are wrong or incomplete: it says W20 is 2-author and omits half of W21, giving Kesting 2 without explaining the W22 single-author review plus half of W20 and W21.
- `rdf+ontology` run 3: Gives the four-way split for I09 and W22 as single-author, but never gives the quarter shares explicitly or Kesting's half shares of W20 and W21.
- `rdf+ontology` run 4: Covers Rostval's four-author works at 0.25 each and Kesting's W22 single authorship, but never says Kesting holds half of W20 and W21.
- `rdf+ontology` run 5: Rostval's quarter shares are correct, but Kesting's shares are wrong: it says W20 is single-author, where the key says W22 is single-author and W20 and W21 are half-shares.
- `csv+ontology` run 1: Gets Kesting's larger shares (W22 single-author, W20/W21) and Rostval's quarter per paper, but doesn't state that each Rostval work has four authors with only one from Rostval, and says 'each author's share goes to one institution' vaguely; also Kesting's half shares of W20/W21 are not stated.
- `csv+ontology` run 3: Gets Rostval's quarter-share per four-author work, but omits that Kesting's shares come from W22 solo review and half of W20 and W21; only mentions solo W22.
- `csv+ontology` run 4: Gives four authors per work and a Rostval total of 1.0, but never says only one author is from Rostval. It also says Kesting has 'shares' of W20 and W21 without stating they are half shares.
- `csv+ontology` run 5: Says Kesting has single-author/two-author works (W22, W20) and Rostval's shares are 0.25, but omits W21 and doesn't state clearly that each Rostval work has four authors with one from Rostval; also 'four or more' is imprecise.
- `csv+markdown` run 2: The Rostval quarter-share point is met, but the Kesting part omits W21's half share and wrongly credits W20 and W22 with 2.0 (they give 1.5).
- `csv+markdown` run 3: Gets the quarter shares for the three exclusive works and the single-author W22, but never says W21 is also a quarter for Rostval or that Kesting holds half of W20 and W21.
- `csv+markdown` run 5: Gets the quarter share for Rostval's four works and Kesting's single-author W22, but never says Kesting holds half of W20 and W21 (its 2.0 total is only implied).
- `csv+padding` run 1: Gets Kesting's shares right (W22 full, half of W20/W21 per W22 and two-author works) but says Rostval gets 1/4 per work without stating that each work has four authors, and its framing is basically consistent; it omits that explicit four-author detail and the W21 half
- `csv+padding` run 2: Gives Kesting's shares (W22 single-author, half of W20 and W21) and says Rostval gets 1/4 on its papers, but says only three four-author papers, not four as the checklist requires, and lists W21 as a Rostval work with Kesting getting 1/2 of it, which conflicts with the 'four works, quarter each' point.
- `csv+padding` run 4: Rostval's quarter-share is covered (four authors, one from Rostval, total 1.0), but it never says W22 is single-author or that Kesting holds half of W20 and W21; it only gives the 2.0 total.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise; the checklist says only the last-listed affiliation counts (Halloran) and Halloran is an affiliated institute, not a unit, so W70 does not roll up to Albury
- `csv` run 2: Rejects the premise; the key says only the last-listed affiliation counts (Halloran Institute), and as an affiliated institute not a unit it doesn't roll up to Albury.
- `csv` run 3: Claims W70 is credited to Albury, contradicting the key: only the last-listed affiliation (Halloran Institute) counts, and it is an affiliated institute, not a unit, so it doesn't roll up.
- `csv` run 4: Rejects the premise, whereas the checklist says only the last-listed affiliation counts so W70 goes to the Halloran Institute, an affiliated institute that does not roll up to Albury.
- `csv` run 5: Contradicts the key: only the last-listed affiliation counts so W70 goes to Halloran Institute, an affiliated institute not a unit, so it doesn't roll up to Albury.
- `rdf` run 1: Answer rejects the premise and says W70 rolls up to Albury; the key says only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that does not roll up.
- `rdf` run 2: Rejects the premise and says W70 counts for Albury, contradicting the key (last-listed affiliation only, Halloran is an affiliated institute not a unit)
- `rdf` run 3: Rejects the premise and claims W70 counts for Albury; the key says only the last-listed affiliation counts, crediting Halloran, an affiliated institute that doesn't roll up.
- `rdf` run 4: The answer rejects the premise and credits W70 to Albury via Tessel. The key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, an affiliated institute that does not roll up to Albury.
- `rdf` run 5: Answer says W70 is credited to Albury via Tessel; checklist says only the last-listed affiliation counts, crediting Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `rdf+ontology` run 2: Says only the last-listed affiliation counts and that I06 is affiliated so the parent link is not followed, but uses codes (I06, I02) rather than naming the Halloran Institute and University of Albury, and doesn't state that it is an affiliated institute rather than a unit in those terms.
- `csv+padding` run 1: Rejects the premise and says W70 is in Albury's tree, contradicting the key that only the last-listed affiliation (Halloran, an affiliated institute not a unit) counts so W70 is not Albury's
- `csv+padding` run 2: Rejects the premise and says W70 counts for Albury; the checklist says only the last-listed affiliation counts, so it is credited to Halloran, which is an affiliated institute not rolling up to Albury, so neither point is met.
- `csv+padding` run 3: Rejects the premise and says W70 is an Albury work, contradicting the key: only the last-listed affiliation counts (Halloran Institute), and as an affiliated institute it does not roll up to Albury.
- `csv+padding` run 4: It rejects the premise and credits W70 to Albury, but the key says only the last-listed affiliation counts, so W70 goes to Halloran, an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 5: Answer rejects the premise and says W70 is credited to Albury, contradicting the key (only last-listed affiliation counts, so it goes to Halloran, an affiliated institute that doesn't roll up to Albury); neither checklist point is met.

