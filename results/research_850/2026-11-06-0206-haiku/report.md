# research_850: claude:haiku, 2026-11-06 02:06

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **21%** | 12% to 31% | 15 of 48 |
| `csv+padding` | **30%** | 19% to 41% | 11 of 48 |
| `csv+markdown` | **43%** | 34% to 51% | 37 of 48 |
| `csv+ontology` | **49%** | 40% to 58% | 36 of 48 |
| `executed` | **69%** | 58% to 79% | 17 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `csv+padding` | +9 points | +4 to +15 |
| `csv+markdown` | +22 points | +13 to +30 |
| `csv+ontology` | +28 points | +19 to +38 |
| `executed` | +48 points | +36 to +60 |

## By question

| Question | Graded by | `csv` | `csv+padding` | `csv+markdown` | `csv+ontology` | `executed` |
|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ❌ ✅ | ✅ ❌ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ❌ |
| Q5 | code | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ✅ ❌ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ |
| Q11 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q12 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ✅ ✅ ❌ ✅ ❌ |
| Q13 | code | 🟡 ❌ 🟡 ❌ 🟡 | ✅ ✅ ✅ 🟡 🟡 | ❌ ❌ ✅ ❌ ✅ | ❌ 🟡 🟡 ❌ 🟡 | 🟡 ✅ ✅ 🟡 🟡 |
| Q14 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ 🟡 | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q15 | code | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q16 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ✅ |
| Q17 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ✅ ❌ ❌ | ❌ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ |
| Q19 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q21 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q22 | code | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | 🟡 🟡 🟡 ❌ 🟡 | 🟡 🟡 🟡 🟡 🟡 | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | 🟡 ❌ 🟡 ❌ 🟡 | 🟡 🟡 🟡 🟡 🟡 | ❌ ❌ ✅ ❌ 🟡 | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ❌ ❌ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | 🟡 ❌ 🟡 ❌ ❌ | 🟡 🟡 🟡 🟡 🟡 | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ 🟡 🟡 ✅ |
| Q30 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ❌ ✅ |
| Q35 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ❌ ❌ | ❌ ❌ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ❌ ❌ |
| Q36 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ❌ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ❌ | ❌ ✅ ❌ ❌ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ❌ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q47 | llm | ❌ ❌ 🟡 ❌ ❌ | ✅ 🟡 🟡 ❌ ❌ | ❌ ❌ 🟡 ❌ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ 🟡 ✅ ❌ ❌ |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ❌ 🟡 ✅ 🟡 ✅ | 🟡 🟡 🟡 🟡 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 13% | 78% |
| `csv+padding` | 20% | 86% |
| `csv+markdown` | 43% | 53% |
| `csv+ontology` | 63% | 76% |
| `executed` | 57% | 81% |

**The checklist grader agreed with itself** on 46 of 50 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv+padding` run 1: count: expected 3, got 1
- `csv+ontology` run 2: count: expected 3, got 1
- `csv+ontology` run 4: count: expected 3, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `csv` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W676', 'W813', 'W949', 'W1005']
- `csv` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `csv` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `csv` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `csv` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `csv+padding` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `csv+padding` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W676', 'W813', 'W949', 'W1005']
- `csv+padding` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `csv+padding` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W676', 'W813', 'W949', 'W1005']
- `csv+padding` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `csv+markdown` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W676', 'W813', 'W949', 'W1005', 'W02', 'W07', 'W19', 'W449', 'W663', 'W869', 'W972', 'W1048', 'W1050', 'W03', 'W206', 'W763', 'W817', 'W555', 'W612', 'W843', 'W905', 'W936', 'W984']
- `csv+markdown` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `csv+ontology` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W1005']
- `executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']

**Q3.** Is the Jonas Brandt who wrote W37 the same person as the Jonas Brandt who wrote W38?

- `csv` run 5: same: expected no, got None

**Q4.** How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?

- `csv` run 1: count: expected 9, got 7
- `csv` run 2: count: expected 9, got 7
- `csv` run 3: count: expected 9, got 7
- `csv` run 4: count: expected 9, got 7
- `csv` run 5: count: expected 9, got 7
- `csv+padding` run 1: count: expected 9, got 7
- `csv+padding` run 2: count: expected 9, got 7
- `csv+padding` run 3: count: expected 9, got 7
- `csv+padding` run 4: count: expected 9, got 7
- `csv+markdown` run 1: count: expected 9, got 8
- `csv+ontology` run 1: count: expected 9, got 8
- `csv+ontology` run 2: count: expected 9, got 8
- `csv+ontology` run 5: count: expected 9, got 8
- `executed` run 5: count: expected 9, got 8

**Q5.** Is the M. Ellison who wrote W08 the same person as the Mara Ellison who wrote W01?

- `csv` run 5: same: expected no, got None

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `csv` run 2: author: expected A01, got A07
- `csv` run 3: author: expected A01, got A07
- `csv` run 4: no structured answer
- `csv` run 5: author: expected A01, got A07
- `csv+padding` run 1: author: expected A01, got A07
- `csv+padding` run 2: author: expected A01, got A07
- `csv+padding` run 3: author: expected A01, got A07 and A110 (tie, 15 each)
- `csv+padding` run 4: author: expected A01, got A07
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 4: author: expected A01, got None

**Q7.** How many research works has Mara Ellison authored?

- `csv` run 1: count: expected 19, got 21
- `csv` run 2: count: expected 19, got 10
- `csv` run 3: count: expected 19, got 26
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 19, got 9
- `csv+padding` run 1: count: expected 19, got 8
- `csv+padding` run 2: count: expected 19, got 7
- `csv+padding` run 3: count: expected 19, got 8
- `csv+padding` run 4: count: expected 19, got 8
- `csv+padding` run 5: count: expected 19, got 25
- `csv+markdown` run 2: count: expected 19, got 20
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: count: expected 19, got 22
- `csv+ontology` run 4: count: expected 19, got 20

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 95, got 114
- `csv` run 2: count: expected 95, got 123
- `csv` run 3: count: expected 95, got 123
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 95, got 121
- `csv+padding` run 1: count: expected 95, got None
- `csv+padding` run 2: count: expected 95, got 112
- `csv+padding` run 3: count: expected 95, got 120
- `csv+padding` run 4: count: expected 95, got 119
- `csv+padding` run 5: count: expected 95, got 124
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 95, got 94
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 95, got 91
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 95, got 91
- `csv+ontology` run 3: count: expected 95, got 93
- `csv+ontology` run 4: count: expected 95, got None
- `csv+ontology` run 5: count: expected 95, got 94
- `executed` run 1: count: expected 95, got 87
- `executed` run 3: count: expected 95, got 88
- `executed` run 4: count: expected 95, got 91
- `executed` run 5: count: expected 95, got 93

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 140, got 166
- `csv` run 2: count: expected 140, got 178
- `csv` run 3: count: expected 140, got 181
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 140, got 179
- `csv+padding` run 1: count: expected 140, got None
- `csv+padding` run 2: count: expected 140, got 166
- `csv+padding` run 3: count: expected 140, got 176
- `csv+padding` run 4: count: expected 140, got 176
- `csv+padding` run 5: count: expected 140, got 181
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 140, got 135
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 140, got 136
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 140, got 136
- `csv+ontology` run 3: count: expected 140, got 134
- `csv+ontology` run 4: count: expected 140, got None
- `csv+ontology` run 5: count: expected 140, got 136
- `executed` run 1: count: expected 140, got 132
- `executed` run 3: count: expected 140, got 131
- `executed` run 4: count: expected 140, got 135
- `executed` run 5: count: expected 140, got 137

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 1: count: expected 59, got 81
- `csv` run 2: count: expected 59, got None
- `csv` run 3: count: expected 59, got 95
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 59, got 101
- `csv+padding` run 1: count: expected 59, got 97
- `csv+padding` run 2: count: expected 59, got 88
- `csv+padding` run 3: count: expected 59, got 82
- `csv+padding` run 4: count: expected 59, got 89
- `csv+padding` run 5: count: expected 59, got 89
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 59, got 61
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 59, got 58
- `csv+ontology` run 3: count: expected 59, got 53
- `csv+ontology` run 4: count: expected 59, got None
- `csv+ontology` run 5: count: expected 59, got 56
- `executed` run 1: count: expected 59, got 58
- `executed` run 2: count: expected 59, got 60
- `executed` run 3: count: expected 59, got 57
- `executed` run 4: count: expected 59, got 56
- `executed` run 5: count: expected 59, got 57

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `csv` run 1: full: expected 13, got 14; fractional: expected 11, got 12
- `csv` run 2: full: expected 13, got None; fractional: expected 11, got None
- `csv` run 3: full: expected 13, got 14; fractional: expected 11, got 12
- `csv` run 4: no structured answer
- `csv` run 5: full: expected 13, got 15; fractional: expected 11, got 13
- `csv+padding` run 2: full: expected 13, got 14; fractional: expected 11, got 12.0
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: full: expected 13, got 12; fractional: expected 11, got 10.5
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: full: expected 13, got 14; fractional: expected 11, got 12
- `csv+ontology` run 4: full: expected 13, got None; fractional: expected 11, got None
- `executed` run 3: full: expected 13, got 12; fractional: expected 11, got 10.5
- `executed` run 5: full: expected 13, got 12; fractional: expected 11, got 10.5

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `csv` run 1: full: expected I09, got I07
- `csv` run 2: full: expected I09, got None; fractional: expected I07, got None
- `csv` run 3: full: expected I09, got tie
- `csv` run 4: no structured answer
- `csv` run 5: full: expected I09, got I07
- `csv+padding` run 4: full: expected I09, got I07
- `csv+padding` run 5: full: expected I09, got I07
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: full: expected I09, got I07
- `csv+ontology` run 3: full: expected I09, got I07
- `csv+ontology` run 4: full: expected I09, got None; fractional: expected I07, got None
- `csv+ontology` run 5: full: expected I09, got I07
- `executed` run 1: full: expected I09, got I07
- `executed` run 4: full: expected I09, got None
- `executed` run 5: full: expected I09, got I07

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `csv` run 1: full: expected 46, got 44; fractional: expected 42, got 41
- `csv` run 2: full: expected 46, got None; fractional: expected 42, got None
- `csv` run 3: full: expected 46, got 47; fractional: expected 42, got 43.5
- `csv` run 4: no structured answer
- `csv` run 5: full: expected 46, got 45; fractional: expected 42, got 41.5
- `csv+padding` run 1: full: expected 46, got None; fractional: expected 42, got None
- `csv+padding` run 2: full: expected 46, got 47; fractional: expected 42, got 43.5
- `csv+padding` run 3: full: expected 46, got None; fractional: expected 42, got None
- `csv+padding` run 4: full: expected 46, got 48; fractional: expected 42, got 44
- `csv+padding` run 5: fractional: expected 42, got 43.17
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: full: expected 46, got 41; fractional: expected 42, got 38.33
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: full: expected 46, got None; fractional: expected 42, got None
- `csv+ontology` run 3: full: expected 46, got None; fractional: expected 42, got None
- `csv+ontology` run 4: full: expected 46, got None; fractional: expected 42, got None
- `csv+ontology` run 5: full: expected 46, got 196; fractional: expected 42, got None
- `executed` run 1: full: expected 46, got None; fractional: expected 42, got None
- `executed` run 2: full: expected 46, got 44; fractional: expected 42, got 40
- `executed` run 3: full: expected 46, got None; fractional: expected 42, got None
- `executed` run 4: full: expected 46, got None; fractional: expected 42, got None
- `executed` run 5: full: expected 46, got None; fractional: expected 42, got None

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `csv` run 1: count: expected 25, got 24
- `csv` run 2: count: expected 25, got 24
- `csv` run 4: count: expected 25, got 27
- `csv` run 5: count: expected 25, got 27
- `csv+padding` run 1: count: expected 25, got 27
- `csv+padding` run 2: count: expected 25, got 24
- `csv+padding` run 3: count: expected 25, got 20
- `csv+padding` run 4: count: expected 25, got 24
- `csv+padding` run 5: count: expected 25, got 23
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 25, got 24
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 25, got 23
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 25, got 24
- `csv+ontology` run 5: count: expected 25, got 24
- `executed` run 1: count: expected 25, got 22
- `executed` run 2: count: expected 25, got 20
- `executed` run 3: count: expected 25, got 22
- `executed` run 4: count: expected 25, got 24
- `executed` run 5: count: expected 25, got 22

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `csv` run 1: count: expected 88, got 91
- `csv` run 2: count: expected 88, got None
- `csv` run 3: count: expected 88, got 91
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 88, got 92
- `csv+padding` run 1: count: expected 88, got 97
- `csv+padding` run 3: count: expected 88, got 92
- `csv+padding` run 4: count: expected 88, got 96
- `csv+padding` run 5: count: expected 88, got 83
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 88, got 78
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 88, got 82
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 88, got 85
- `csv+ontology` run 3: count: expected 88, got None
- `csv+ontology` run 4: count: expected 88, got None
- `csv+ontology` run 5: count: expected 88, got 75
- `executed` run 2: count: expected 88, got 75
- `executed` run 3: count: expected 88, got 82
- `executed` run 4: count: expected 88, got None

**Q17.** Which of Mara Ellison's works are not research output because of their document type?

- `csv` run 1: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W813', 'W949']
- `csv` run 2: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271']
- `csv` run 3: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W813', 'W949']
- `csv` run 4: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W813', 'W949']
- `csv` run 5: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W949']
- `csv+padding` run 1: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W813', 'W949']
- `csv+padding` run 2: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W813', 'W949']
- `csv+padding` run 3: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W813', 'W949']
- `csv+padding` run 4: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W949']
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271', 'W936', 'W949']
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05', 'W271']

**Q18.** How many distinct research works has Priya Ramanathan (A07) authored?

- `csv` run 2: count: expected 15, got 17
- `csv` run 3: count: expected 15, got 17
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 15, got 17
- `csv+padding` run 1: count: expected 15, got 18
- `csv+padding` run 5: count: expected 15, got 17
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: count: expected 15, got 14
- `executed` run 4: count: expected 15, got 14

**Q19.** How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?

- `csv` run 1: count: expected 27, got 30
- `csv` run 2: count: expected 27, got 26
- `csv` run 3: count: expected 27, got 30
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 27, got 30
- `csv+padding` run 1: count: expected 27, got 29
- `csv+padding` run 2: count: expected 27, got 29
- `csv+padding` run 3: count: expected 27, got 29
- `csv+padding` run 4: count: expected 27, got 30
- `csv+padding` run 5: count: expected 27, got 30
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 27, got 26
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: count: expected 27, got 23
- `csv+ontology` run 4: count: expected 27, got None
- `csv+ontology` run 5: count: expected 27, got 22
- `executed` run 3: count: expected 27, got 26

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `csv` run 4: no structured answer
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got ['W02', 'W42', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W1049']
- `executed` run 1: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 2: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 3: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 4: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 5: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `csv` run 1: count: expected 45, got 39
- `csv` run 2: count: expected 45, got 44
- `csv` run 3: count: expected 45, got 49
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 45, got 42
- `csv+padding` run 1: count: expected 45, got 48
- `csv+padding` run 2: count: expected 45, got 46
- `csv+padding` run 3: count: expected 45, got 40
- `csv+padding` run 4: count: expected 45, got 43
- `csv+padding` run 5: count: expected 45, got 47
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 45, got 41
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 45, got 41
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 45, got 37
- `csv+ontology` run 3: count: expected 45, got 41
- `csv+ontology` run 4: count: expected 45, got None
- `csv+ontology` run 5: count: expected 45, got 37
- `executed` run 1: count: expected 45, got 39
- `executed` run 2: count: expected 45, got 42
- `executed` run 3: count: expected 45, got 43
- `executed` run 4: count: expected 45, got 38
- `executed` run 5: count: expected 45, got 39

**Q22.** Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?

- `csv` run 4: no structured answer
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 4: more_in_total: expected W30, got None; more_in_window: expected W31, got None

**Q23.** How many citations has W30 received in total, and how many within its publication year and the two years after?

- `csv` run 1: total: expected 16, got 18
- `csv` run 2: total: expected 16, got 18
- `csv` run 3: total: expected 16, got 18
- `csv` run 4: no structured answer
- `csv` run 5: total: expected 16, got 18
- `csv+padding` run 1: total: expected 16, got 18
- `csv+padding` run 2: total: expected 16, got 18
- `csv+padding` run 3: total: expected 16, got 18
- `csv+padding` run 4: total: expected 16, got 18
- `csv+padding` run 5: total: expected 16, got 18
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 4: total: expected 16, got None; in_window: expected 2, got None

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 2: count: expected 12, got 13
- `csv` run 3: count: expected 12, got 14
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 12, got 14
- `csv+padding` run 1: count: expected 12, got 14
- `csv+padding` run 2: count: expected 12, got 14
- `csv+padding` run 3: count: expected 12, got 14
- `csv+padding` run 4: count: expected 12, got 14
- `csv+padding` run 5: count: expected 12, got 18
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 12, got 11
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 12, got 11
- `csv+ontology` run 1: no structured answer
- `executed` run 1: count: expected 12, got 11

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 1: count: expected 20, got 40
- `csv` run 2: count: expected 20, got 41
- `csv` run 3: count: expected 20, got 42
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 20, got 39
- `csv+padding` run 1: count: expected 20, got 41
- `csv+padding` run 2: count: expected 20, got 40
- `csv+padding` run 3: count: expected 20, got 41
- `csv+padding` run 4: count: expected 20, got 41
- `csv+padding` run 5: count: expected 20, got 41
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 4: count: expected 20, got None

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 2: counts: expected no, got depends
- `csv` run 3: counts: expected no, got depends
- `csv` run 4: no structured answer
- `csv` run 5: counts: expected no, got depends
- `csv+padding` run 1: counts: expected no, got yes
- `csv+padding` run 2: counts: expected no, got yes
- `csv+padding` run 3: counts: expected no, got depends
- `csv+padding` run 4: counts: expected no, got depends
- `csv+padding` run 5: counts: expected no, got depends
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer

**Q27.** Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?

- `csv` run 1: citing_works: expected 12, got 15
- `csv` run 2: institution: expected I12, got None; citing_works: expected 12, got None
- `csv` run 3: citing_works: expected 12, got 16
- `csv` run 4: no structured answer
- `csv` run 5: citing_works: expected 12, got 16
- `csv+padding` run 1: citing_works: expected 12, got 13
- `csv+padding` run 2: citing_works: expected 12, got 14
- `csv+padding` run 3: citing_works: expected 12, got 15
- `csv+padding` run 4: citing_works: expected 12, got 11
- `csv+padding` run 5: citing_works: expected 12, got 15
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: citing_works: expected 12, got 13
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 4: institution: expected I12, got None; citing_works: expected 12, got None

**Q28.** How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?

- `csv` run 1: count: expected 4, got 3
- `csv` run 2: count: expected 4, got None
- `csv` run 4: no structured answer
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 4: count: expected 4, got None

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `csv` run 1: institution: expected 10, got 12; country: expected 20, got 21
- `csv` run 2: author: expected 7, got None; institution: expected 10, got None; country: expected 20, got None
- `csv` run 3: institution: expected 10, got 12; country: expected 20, got 21
- `csv` run 4: no structured answer
- `csv` run 5: author: expected 7, got 4; institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 1: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 2: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 3: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 4: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 5: institution: expected 10, got 12; country: expected 20, got 21
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: author: expected 7, got 6; institution: expected 10, got 9; country: expected 20, got 18
- `csv+ontology` run 4: author: expected 7, got None; institution: expected 10, got None; country: expected 20, got None
- `csv+ontology` run 5: author: expected 7, got 5; institution: expected 10, got 8; country: expected 20, got 17
- `executed` run 3: institution: expected 10, got 8; country: expected 20, got 19
- `executed` run 4: institution: expected 10, got 11; country: expected 20, got 21

**Q30.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?

- `csv` run 1: count: expected 14, got 18
- `csv` run 2: count: expected 14, got None
- `csv` run 3: count: expected 14, got 18
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 14, got 18
- `csv+padding` run 1: count: expected 14, got 18
- `csv+padding` run 2: count: expected 14, got 18
- `csv+padding` run 3: count: expected 14, got 18
- `csv+padding` run 4: count: expected 14, got 18
- `csv+padding` run 5: count: expected 14, got 18
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 14, got 15
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: count: expected 14, got 13
- `csv+ontology` run 4: count: expected 14, got None
- `csv+ontology` run 5: count: expected 14, got 11
- `executed` run 3: count: expected 14, got 13
- `executed` run 4: count: expected 14, got 15

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 1: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1039', 'W1042']
- `csv` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv` run 4: no structured answer
- `csv` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1039', 'W1042']
- `csv+padding` run 1: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv+padding` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv+padding` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv+padding` run 4: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1039', 'W1042']
- `csv+padding` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W337', 'W682', 'W801', 'W1042']
- `csv+ontology` run 4: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got None
- `csv+ontology` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W1039', 'W1042']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `csv` run 1: count: expected 17, got 20
- `csv` run 2: count: expected 17, got 21
- `csv` run 3: count: expected 17, got 20
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 17, got 21
- `csv+padding` run 1: count: expected 17, got 20
- `csv+padding` run 2: count: expected 17, got 20
- `csv+padding` run 3: count: expected 17, got 20
- `csv+padding` run 4: count: expected 17, got 21
- `csv+padding` run 5: count: expected 17, got 20
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 3: count: expected 17, got 9
- `csv+ontology` run 4: count: expected 17, got None
- `csv+ontology` run 5: count: expected 17, got 18

**Q33.** Which of Kesting University's research works has the most citations?

- `csv` run 1: work: expected W20, got W22
- `csv` run 2: work: expected W20, got None
- `csv` run 3: work: expected W20, got W22
- `csv` run 4: no structured answer
- `csv` run 5: work: expected W20, got W22
- `csv+padding` run 1: work: expected W20, got W22
- `csv+padding` run 2: work: expected W20, got W22
- `csv+padding` run 3: work: expected W20, got W22
- `csv+padding` run 4: work: expected W20, got W22
- `csv+padding` run 5: work: expected W20, got W22
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 4: work: expected W20, got None

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 1: count: expected 7, got 24
- `csv` run 2: count: expected 7, got None
- `csv` run 3: count: expected 7, got 27
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 7, got 31
- `csv+padding` run 1: count: expected 7, got 28
- `csv+padding` run 2: count: expected 7, got 26
- `csv+padding` run 3: count: expected 7, got 20
- `csv+padding` run 4: count: expected 7, got 24
- `csv+padding` run 5: count: expected 7, got 25
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 7, got 5
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 7, got 5
- `csv+ontology` run 3: count: expected 7, got 5
- `csv+ontology` run 4: count: expected 7, got None
- `executed` run 4: count: expected 7, got 6

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 25, got 24
- `csv` run 2: count: expected 25, got 26
- `csv` run 3: count: expected 25, got 30
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 25, got 30
- `csv+padding` run 1: count: expected 25, got 30
- `csv+padding` run 4: count: expected 25, got 27
- `csv+padding` run 5: count: expected 25, got 29
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 25, got 23
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 25, got 23
- `csv+ontology` run 3: count: expected 25, got 24
- `csv+ontology` run 4: count: expected 25, got None
- `csv+ontology` run 5: count: expected 25, got 24
- `executed` run 4: count: expected 25, got 23
- `executed` run 5: count: expected 25, got 24

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 1: count: expected 36, got 26
- `csv` run 2: count: expected 36, got 25
- `csv` run 3: count: expected 36, got 23
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 36, got 24
- `csv+padding` run 1: count: expected 36, got 29
- `csv+padding` run 2: count: expected 36, got 26
- `csv+padding` run 3: count: expected 36, got 24
- `csv+padding` run 4: count: expected 36, got 24
- `csv+padding` run 5: count: expected 36, got 23
- `csv+markdown` run 1: count: expected 36, got 34
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 36, got 31
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 36, got 34
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 36, got 35
- `csv+ontology` run 3: count: expected 36, got 31
- `csv+ontology` run 4: count: expected 36, got None
- `csv+ontology` run 5: count: expected 36, got 33
- `executed` run 2: count: expected 36, got 32
- `executed` run 3: count: expected 36, got 32
- `executed` run 4: count: expected 36, got 33
- `executed` run 5: count: expected 36, got 35

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04
- `csv` run 2: institution: expected I06, got I04
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04, I06
- `csv+padding` run 1: institution: expected I06, got I04; I06
- `csv+padding` run 2: institution: expected I06, got I04, I06
- `csv+padding` run 3: institution: expected I06, got I04 and I06
- `csv+padding` run 4: institution: expected I06, got I04
- `csv+padding` run 5: institution: expected I06, got I04
- `csv+markdown` run 2: no structured answer
- `csv+ontology` run 1: no structured answer

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I02', 'I03', 'I01']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+padding` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `csv` run 1: count: expected 19, got 21
- `csv` run 2: count: expected 19, got None
- `csv` run 3: count: expected 19, got 21
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 19, got 18
- `csv+padding` run 1: count: expected 19, got 20
- `csv+padding` run 2: count: expected 19, got 21
- `csv+padding` run 3: count: expected 19, got 21
- `csv+padding` run 4: count: expected 19, got 21
- `csv+padding` run 5: count: expected 19, got 20
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 3: count: expected 19, got 18
- `csv+markdown` run 4: no structured answer
- `csv+markdown` run 5: count: expected 19, got 17
- `csv+ontology` run 1: no structured answer
- `csv+ontology` run 2: count: expected 19, got 18
- `csv+ontology` run 4: count: expected 19, got None
- `csv+ontology` run 5: count: expected 19, got 18
- `executed` run 1: count: expected 19, got 16
- `executed` run 3: count: expected 19, got 16
- `executed` run 4: count: expected 19, got 18

**Q40.** Which source is in the highest tier?

- `csv+markdown` run 2: no structured answer
- `csv+ontology` run 1: no structured answer

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `csv+markdown` run 2: no structured answer
- `csv+ontology` run 1: no structured answer

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `csv` run 1: count: expected 0, got 13
- `csv` run 2: count: expected 0, got 13
- `csv` run 3: count: expected 0, got 12
- `csv` run 4: no structured answer
- `csv` run 5: count: expected 0, got 13
- `csv+padding` run 1: count: expected 0, got 13
- `csv+padding` run 2: count: expected 0, got 12
- `csv+padding` run 3: count: expected 0, got 13
- `csv+padding` run 4: count: expected 0, got 13
- `csv+padding` run 5: count: expected 0, got 13
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer

**Q43.** Is W07 research output?

- `csv` run 1: research: expected no, got yes
- `csv` run 2: research: expected no, got yes
- `csv` run 3: research: expected no, got yes
- `csv` run 4: research: expected no, got yes
- `csv` run 5: research: expected no, got yes
- `csv+padding` run 1: research: expected no, got yes
- `csv+padding` run 2: research: expected no, got yes
- `csv+padding` run 3: research: expected no, got yes
- `csv+padding` run 4: research: expected no, got yes
- `csv+padding` run 5: research: expected no, got yes
- `csv+markdown` run 2: no structured answer
- `csv+ontology` run 1: no structured answer

**Q44.** Which institutions are part of the Albury University System, at any level below it?

- `csv` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv+padding` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv+padding` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv+padding` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv+padding` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv+padding` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer
- `executed` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `executed` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `executed` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']

**Q45.** How many research works is the Halloran Institute for Coastal Studies (I06) credited with?

- `csv` run 1: count: expected 16, got 22
- `csv` run 2: count: expected 16, got 22
- `csv` run 3: count: expected 16, got 22
- `csv` run 4: count: expected 16, got 22
- `csv` run 5: count: expected 16, got 22
- `csv+padding` run 1: count: expected 16, got 22
- `csv+padding` run 2: count: expected 16, got 22
- `csv+padding` run 3: count: expected 16, got 22
- `csv+padding` run 4: count: expected 16, got 22
- `csv+padding` run 5: count: expected 16, got 22
- `csv+markdown` run 1: no structured answer
- `csv+markdown` run 2: no structured answer
- `csv+markdown` run 4: no structured answer
- `csv+ontology` run 1: no structured answer

**Q46.** What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?

- `csv` run 1: parent: expected I06, got I01
- `csv` run 2: parent: expected I06, got I01
- `csv` run 3: parent: expected I06, got I01
- `csv` run 4: parent: expected I06, got I01
- `csv` run 5: parent: expected I06, got I01
- `csv+padding` run 1: parent: expected I06, got I01
- `csv+padding` run 2: parent: expected I06, got I01
- `csv+padding` run 3: parent: expected I06, got I01
- `csv+padding` run 4: parent: expected I06, got I01
- `csv+padding` run 5: parent: expected I06, got I01
- `csv+markdown` run 2: no structured answer
- `csv+ontology` run 1: no structured answer
- `executed` run 1: parent: expected I06, got I01
- `executed` run 2: parent: expected I06, got I01
- `executed` run 3: parent: expected I06, got I01
- `executed` run 4: parent: expected I06, got I01
- `executed` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Rejects the premise and gives none of the checklist points (Rostval's small shares of multi-author works, Kesting's larger shares).
- `csv` run 2: No answer given; defers computation and states neither Rostval's small shares nor Kesting's larger shares.
- `csv` run 3: Covers Rostval's small shares (four-author papers, one Rostval author each), but never explains Kesting's larger shares, and it rejects the swap premise.
- `csv` run 4: No answer given; meets none of the checklist points
- `csv` run 5: Rejects the premise and gives no explanation of Rostval's small fractional shares or Kesting's larger shares; meets neither checklist point.
- `csv+padding` run 2: Covers Kesting's larger shares via fewer authors, and implies Rostval's one-author-per-paper share, but it doesn't clearly say Rostval's small share per multi-author work explains the swap; it does say four-author papers with one Rostval author, so it mostly meets both points, though the explanation is framed mainly around Kesting.
- `csv+padding` run 3: Gets Rostval's small share per multi-author work (one quarter), and says Kesting's works have most or all authors at Kesting, but this is stated as 'more often' rather than as larger shares from solo/few co-authors; largely meets both points, though Rostval's 'only one from Rostval' is only implied by 'about one quarter'.
- `csv+padding` run 4: Rejects the premise and denies a swap; mentions neither Rostval's multi-author shares nor Kesting's larger shares.
- `csv+padding` run 5: Rejects the premise as false and never gives either checklist point (Rostval's small shares of multi-author works, Kesting's larger shares).
- `csv+markdown` run 1: No answer was given, so neither checklist point is met
- `csv+markdown` run 2: No answer given; meets none of the checklist points
- `csv+markdown` run 3: Says Rostval gets 0.25 per work from four authors (one Rostval), but only vaguely says Kesting has a larger share, without noting many sole-Kesting or few-co-author works
- `csv+markdown` run 4: No answer was given, so neither checklist point is met.
- `csv+ontology` run 1: No answer given; meets none of the checklist points
- `csv+ontology` run 2: Rejects the premise and says there is no swap; meets neither point about Rostval's shared authorship or Kesting's larger shares.
- `csv+ontology` run 3: Rejects the premise and gives no explanation of Rostval's small shares or Kesting's larger shares of 2024 works
- `csv+ontology` run 4: No answer given; meets none of the checklist points
- `csv+ontology` run 5: Rejects the premise and doesn't give either checklist point (Rostval's shared multi-author works, Kesting's larger shares).
- `executed` run 1: Rejects the premise instead of giving the checklist's explanation (Rostval's small shares of multi-author works; Kesting's larger shares); neither point is made.
- `executed` run 2: Gives Rostval's four-author works with one credit (small share) but does not say Kesting holds larger shares via solo or few-author works in general terms beyond examples; mostly meets point 1, point 2 only loosely via 'fewer-author works'
- `executed` run 4: Rejects the premise and gives neither the Rostval multi-author small-share explanation nor the Kesting larger-share explanation.
- `executed` run 5: Rejects the premise instead of giving either checklist point: Rostval's multi-author works with small shares, or Kesting's larger shares.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise and says W70 counts for Albury, contradicting the checklist (last-listed affiliation only, Halloran is an affiliated institute not a unit).
- `csv` run 2: Rejects the premise; the key says only the last-listed affiliation counts, so W70 is credited to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv` run 3: Contradicts the checklist: it says Halloran is a unit of Albury and W70 counts, whereas the checklist says only the last affiliation counts and Halloran is an affiliated institute that does not roll up.
- `csv` run 4: No answer given; meets none of the checklist points
- `csv` run 5: Rejects the premise and claims W70 counts; misses the last-listed-affiliation rule and that Halloran is an affiliated institute not rolling up to Albury.
- `csv+padding` run 1: Answer denies the premise and says W70 is an Albury work; checklist says it is credited only to Halloran Institute (last affiliation), an affiliated institute that doesn't roll up, so it is not Albury's.
- `csv+padding` run 2: Rejects the premise; the key says only the last-listed affiliation counts, so W70 is credited to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 3: Answer denies the premise and says W70 is Albury's; checklist says it is credited only to Halloran, an affiliated institute not rolling up to Albury.
- `csv+padding` run 4: Rejects the premise instead of saying only the last-listed affiliation counts (Halloran) and that Halloran is an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 5: Says W70 is an Albury work and never mentions the last-listed-affiliation rule or the Halloran Institute being affiliated rather than a unit.
- `csv+markdown` run 2: No answer given; meets none of the checklist points
- `csv+ontology` run 1: No answer given; meets none of the checklist points
- `csv+ontology` run 2: Says only the last-listed affiliation counts and it is Halloran (I06), but omits that Halloran is an affiliated institute rather than a unit so its works don't roll up to Albury.
- `csv+ontology` run 4: Correctly says last-listed affiliation (I06) counts and it is an affiliated institute not a unit of the University, but doesn't name it as the Halloran Institute (only I06) or explicitly credit W70 to it
- `executed` run 1: Says W70 is credited to Halloran (I06) and that I06 doesn't roll up to Albury, but doesn't state that only the last-listed affiliation counts.
- `executed` run 2: Says Halloran (I06) is not a unit so it doesn't roll up to Albury, but doesn't state the last-listed-affiliation rule explicitly
- `executed` run 3: Gets Halloran credit and that it doesn't roll up to Albury, but never states the last-listed-affiliation rule and instead denies the Tessel premise.
- `executed` run 4: Says W70 is credited to the Halloran Institute, but gives no last-listed-affiliation rule and does not say the institute is affiliated rather than a unit, so its works don't roll up to Albury.
- `executed` run 5: Says W70 is credited only to Halloran (I06) and that I06 is not one of I02's units, but never states the last-listed-affiliation rule or that Halloran is an affiliated institute.

