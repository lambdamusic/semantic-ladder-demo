# research_850: claude:sonnet, 2026-11-06 02:06

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **42%** | 30% to 54% | 8 of 48 |
| `csv+padding` | **42%** | 30% to 54% | 12 of 48 |
| `csv+markdown` | **87%** | 78% to 94% | 9 of 48 |
| `csv+ontology` | **89%** | 82% to 95% | 12 of 48 |
| `executed` | **79%** | 69% to 89% | 7 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `csv+padding` | +0 points | -4 to +4 |
| `csv+markdown` | +45 points | +32 to +58 |
| `csv+ontology` | +47 points | +34 to +60 |
| `executed` | +37 points | +23 to +51 |

## By question

| Question | Graded by | `csv` | `csv+padding` | `csv+markdown` | `csv+ontology` | `executed` |
|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q11 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | 🟡 ✅ ❌ ❌ ✅ | ❌ ❌ ❌ 🟡 🟡 | ❌ ✅ ❌ ✅ ✅ |
| Q15 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ✅ |
| Q16 | code | ❌ ❌ ❌ ✅ ❌ | ❌ ✅ ✅ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ❌ | ❌ ✅ ❌ ✅ ❌ | ✅ ❌ ❌ ✅ ❌ | ❌ ✅ ❌ ❌ ❌ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q21 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ❌ ✅ | ✅ ❌ ❌ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ❌ ❌ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ❌ ❌ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ❌ ✅ ✅ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ❌ ✅ ✅ ❌ ❌ | ❌ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q47 | llm | 🟡 ✅ ✅ 🟡 ✅ | 🟡 🟡 ✅ ✅ 🟡 | ✅ ✅ ✅ ✅ 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 🟡 🟡 |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 50% | 94% |
| `csv+padding` | 50% | 95% |
| `csv+markdown` | 100% | 100% |
| `csv+ontology` | 100% | 100% |
| `executed` | 67% | 82% |

**The checklist grader agreed with itself** on 48 of 50 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv+padding` run 2: count: expected 3, got 1
- `csv+markdown` run 2: count: expected 3, got 1
- `csv+markdown` run 3: count: expected 3, got 1
- `csv+markdown` run 4: count: expected 3, got 1
- `csv+markdown` run 5: count: expected 3, got 1
- `csv+ontology` run 1: count: expected 3, got 1
- `csv+ontology` run 2: count: expected 3, got 1
- `csv+ontology` run 3: count: expected 3, got 1
- `csv+ontology` run 4: count: expected 3, got 1
- `csv+ontology` run 5: count: expected 3, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W608', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W608', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W608', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']
- `executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W608', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']

**Q4.** How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?

- `csv+ontology` run 4: count: expected 9, got 8

**Q7.** How many research works has Mara Ellison authored?

- `csv` run 1: count: expected 19, got 22
- `csv` run 2: count: expected 19, got 23
- `csv` run 3: count: expected 19, got 23
- `csv` run 4: count: expected 19, got 22
- `csv` run 5: count: expected 19, got 22
- `csv+padding` run 1: count: expected 19, got 22
- `csv+padding` run 2: count: expected 19, got 23
- `csv+padding` run 3: count: expected 19, got 23
- `csv+padding` run 4: count: expected 19, got 23
- `csv+padding` run 5: count: expected 19, got 23
- `csv+ontology` run 1: count: expected 19, got 20
- `executed` run 2: count: expected 19, got 20
- `executed` run 3: count: expected 19, got 20
- `executed` run 4: count: expected 19, got 20
- `executed` run 5: count: expected 19, got 20

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 95, got 116
- `csv` run 2: count: expected 95, got 118
- `csv` run 3: count: expected 95, got 119
- `csv` run 4: count: expected 95, got 117
- `csv` run 5: count: expected 95, got 117
- `csv+padding` run 1: count: expected 95, got 117
- `csv+padding` run 2: count: expected 95, got 119
- `csv+padding` run 3: count: expected 95, got 119
- `csv+padding` run 4: count: expected 95, got 119
- `csv+padding` run 5: count: expected 95, got 119
- `csv+markdown` run 1: count: expected 95, got 94
- `csv+markdown` run 2: count: expected 95, got 94
- `csv+markdown` run 4: count: expected 95, got 92
- `csv+ontology` run 1: count: expected 95, got 96
- `executed` run 1: count: expected 95, got 93
- `executed` run 2: count: expected 95, got 93
- `executed` run 3: count: expected 95, got 94
- `executed` run 4: count: expected 95, got 93
- `executed` run 5: count: expected 95, got 93

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 140, got 173
- `csv` run 2: count: expected 140, got 174
- `csv` run 3: count: expected 140, got 176
- `csv` run 4: count: expected 140, got 174
- `csv` run 5: count: expected 140, got 174
- `csv+padding` run 1: count: expected 140, got 174
- `csv+padding` run 2: count: expected 140, got 176
- `csv+padding` run 3: count: expected 140, got 176
- `csv+padding` run 4: count: expected 140, got 175
- `csv+padding` run 5: count: expected 140, got 176
- `csv+markdown` run 1: count: expected 140, got 139
- `csv+markdown` run 2: count: expected 140, got 138
- `csv+markdown` run 3: count: expected 140, got 139
- `csv+markdown` run 4: count: expected 140, got 136
- `csv+markdown` run 5: count: expected 140, got 139
- `csv+ontology` run 3: count: expected 140, got 139
- `csv+ontology` run 4: count: expected 140, got 139
- `executed` run 1: count: expected 140, got 138
- `executed` run 2: count: expected 140, got 138
- `executed` run 3: count: expected 140, got 139
- `executed` run 4: count: expected 140, got 138
- `executed` run 5: count: expected 140, got 138

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 1: count: expected 59, got 65
- `csv` run 2: count: expected 59, got 70
- `csv` run 3: count: expected 59, got 68
- `csv` run 4: count: expected 59, got 64
- `csv` run 5: count: expected 59, got 62
- `csv+padding` run 1: count: expected 59, got 65
- `csv+padding` run 2: count: expected 59, got 70
- `csv+padding` run 3: count: expected 59, got 70
- `csv+padding` run 4: count: expected 59, got 70
- `csv+padding` run 5: count: expected 59, got 70
- `csv+markdown` run 1: count: expected 59, got 58
- `csv+markdown` run 2: count: expected 59, got 57
- `csv+markdown` run 3: count: expected 59, got 57
- `csv+ontology` run 3: count: expected 59, got 58
- `csv+ontology` run 5: count: expected 59, got 57

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `csv` run 1: full: expected 13, got 15; fractional: expected 11, got 13
- `csv` run 2: full: expected 13, got 14; fractional: expected 11, got 12
- `csv` run 3: full: expected 13, got 14; fractional: expected 11, got 12
- `csv` run 4: full: expected 13, got 14; fractional: expected 11, got 12.0
- `csv` run 5: full: expected 13, got 14; fractional: expected 11, got 12
- `csv+padding` run 1: full: expected 13, got 14; fractional: expected 11, got 12
- `csv+padding` run 2: full: expected 13, got 14; fractional: expected 11, got 12
- `csv+padding` run 3: full: expected 13, got 14; fractional: expected 11, got 12
- `csv+padding` run 4: full: expected 13, got 14; fractional: expected 11, got 12
- `csv+padding` run 5: full: expected 13, got 15; fractional: expected 11, got 13.0

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `csv` run 1: full: expected 46, got 49; fractional: expected 42, got 44.58
- `csv` run 2: full: expected 46, got 48; fractional: expected 42, got 44
- `csv` run 3: full: expected 46, got 48; fractional: expected 42, got 44
- `csv` run 4: full: expected 46, got 45; fractional: expected 42, got 41.5
- `csv` run 5: full: expected 46, got 47; fractional: expected 42, got 43
- `csv+padding` run 1: full: expected 46, got 49; fractional: expected 42, got 44.75
- `csv+padding` run 2: full: expected 46, got 48; fractional: expected 42, got 44
- `csv+padding` run 3: full: expected 46, got 47; fractional: expected 42, got 43
- `csv+padding` run 4: full: expected 46, got 49; fractional: expected 42, got 44.67
- `csv+padding` run 5: full: expected 46, got 50; fractional: expected 42, got 45.75
- `csv+markdown` run 1: full: expected 46, got 47
- `csv+markdown` run 3: full: expected 46, got 45; fractional: expected 42, got 41
- `csv+markdown` run 4: full: expected 46, got 44; fractional: expected 42, got 40
- `csv+ontology` run 1: full: expected 46, got 48; fractional: expected 42, got 43.67
- `csv+ontology` run 2: full: expected 46, got 45; fractional: expected 42, got 41
- `csv+ontology` run 3: full: expected 46, got 45; fractional: expected 42, got 40.67
- `csv+ontology` run 4: fractional: expected 42, got 40.67
- `csv+ontology` run 5: full: expected 46, got 47
- `executed` run 1: full: expected 46, got 42; fractional: expected 42, got 38.83
- `executed` run 3: full: expected 46, got 47; fractional: expected 42, got 43

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `csv` run 1: count: expected 25, got 26
- `csv` run 2: count: expected 25, got 26
- `csv` run 3: count: expected 25, got 27
- `csv` run 4: count: expected 25, got 24
- `csv+padding` run 2: count: expected 25, got 27
- `csv+padding` run 3: count: expected 25, got 27
- `csv+padding` run 4: count: expected 25, got 27
- `csv+padding` run 5: count: expected 25, got 27
- `csv+ontology` run 2: count: expected 25, got 24
- `executed` run 1: count: expected 25, got 23
- `executed` run 2: count: expected 25, got 23
- `executed` run 4: count: expected 25, got 24

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `csv` run 1: count: expected 88, got 87
- `csv` run 2: count: expected 88, got 89
- `csv` run 3: count: expected 88, got 89
- `csv` run 5: count: expected 88, got 86
- `csv+padding` run 1: count: expected 88, got 84
- `csv+padding` run 4: count: expected 88, got 90
- `csv+padding` run 5: count: expected 88, got 89
- `csv+markdown` run 1: count: expected 88, got 86
- `csv+markdown` run 3: count: expected 88, got 89
- `csv+markdown` run 4: count: expected 88, got 85
- `csv+markdown` run 5: count: expected 88, got 85
- `csv+ontology` run 3: count: expected 88, got 86
- `csv+ontology` run 4: count: expected 88, got 87
- `executed` run 1: count: expected 88, got 84
- `executed` run 2: count: expected 88, got 83
- `executed` run 3: count: expected 88, got 85
- `executed` run 4: count: expected 88, got 86
- `executed` run 5: count: expected 88, got 86

**Q19.** How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?

- `csv` run 1: count: expected 27, got 29
- `csv` run 2: count: expected 27, got 30
- `csv` run 3: count: expected 27, got 29
- `csv` run 4: count: expected 27, got 29
- `csv` run 5: count: expected 27, got 28
- `csv+padding` run 2: count: expected 27, got 28
- `csv+padding` run 3: count: expected 27, got 28
- `csv+padding` run 5: count: expected 27, got 30
- `csv+markdown` run 1: count: expected 27, got 26
- `csv+markdown` run 3: count: expected 27, got 26
- `csv+markdown` run 5: count: expected 27, got 26
- `csv+ontology` run 2: count: expected 27, got 26
- `csv+ontology` run 3: count: expected 27, got 26
- `csv+ontology` run 5: count: expected 27, got 26
- `executed` run 1: count: expected 27, got 26
- `executed` run 3: count: expected 27, got 26
- `executed` run 4: count: expected 27, got 26
- `executed` run 5: count: expected 27, got 26

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `executed` run 1: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 2: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 3: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 4: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `executed` run 5: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `csv` run 1: count: expected 45, got 47
- `csv` run 2: count: expected 45, got 46
- `csv` run 3: count: expected 45, got 46
- `csv` run 4: count: expected 45, got 47
- `csv` run 5: count: expected 45, got 46
- `csv+padding` run 1: count: expected 45, got 47
- `csv+padding` run 2: count: expected 45, got 46
- `csv+padding` run 3: count: expected 45, got 46
- `csv+padding` run 4: count: expected 45, got 46
- `csv+padding` run 5: count: expected 45, got 47
- `csv+markdown` run 1: count: expected 45, got 44
- `csv+markdown` run 2: count: expected 45, got 44
- `csv+markdown` run 3: count: expected 45, got 43
- `csv+markdown` run 4: count: expected 45, got 44
- `csv+markdown` run 5: count: expected 45, got 44
- `csv+ontology` run 1: count: expected 45, got 43
- `csv+ontology` run 2: count: expected 45, got 44
- `csv+ontology` run 4: count: expected 45, got 43
- `executed` run 2: count: expected 45, got 43
- `executed` run 3: count: expected 45, got 44

**Q23.** How many citations has W30 received in total, and how many within its publication year and the two years after?

- `csv` run 1: total: expected 16, got 17
- `csv` run 2: total: expected 16, got 18
- `csv` run 3: total: expected 16, got 18
- `csv` run 4: total: expected 16, got 18
- `csv` run 5: total: expected 16, got 17
- `csv+padding` run 1: total: expected 16, got 17
- `csv+padding` run 2: total: expected 16, got 17
- `csv+padding` run 3: total: expected 16, got 17
- `csv+padding` run 4: total: expected 16, got 17
- `csv+padding` run 5: total: expected 16, got 18

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 2: count: expected 12, got 15
- `csv` run 3: count: expected 12, got 15
- `csv+padding` run 2: count: expected 12, got 15
- `csv+padding` run 3: count: expected 12, got 15
- `csv+padding` run 4: count: expected 12, got 15
- `csv+padding` run 5: count: expected 12, got 15

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 1: count: expected 20, got 22
- `csv` run 2: count: expected 20, got 42
- `csv` run 3: count: expected 20, got 42
- `csv` run 4: count: expected 20, got 41
- `csv` run 5: count: expected 20, got 22
- `csv+padding` run 1: count: expected 20, got 23
- `csv+padding` run 2: count: expected 20, got 23
- `csv+padding` run 3: count: expected 20, got 23
- `csv+padding` run 4: count: expected 20, got 23
- `csv+padding` run 5: count: expected 20, got 42

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 2: counts: expected no, got yes
- `csv` run 3: counts: expected no, got yes
- `csv+padding` run 2: counts: expected no, got yes
- `csv+padding` run 3: counts: expected no, got yes
- `csv+padding` run 4: counts: expected no, got yes
- `csv+padding` run 5: counts: expected no, got yes

**Q27.** Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?

- `csv` run 1: citing_works: expected 12, got 15
- `csv` run 2: citing_works: expected 12, got 14
- `csv` run 3: citing_works: expected 12, got 14
- `csv` run 4: citing_works: expected 12, got 16
- `csv` run 5: citing_works: expected 12, got 15
- `csv+padding` run 1: citing_works: expected 12, got 15
- `csv+padding` run 2: citing_works: expected 12, got 16
- `csv+padding` run 3: citing_works: expected 12, got 16
- `csv+padding` run 4: citing_works: expected 12, got 15
- `csv+padding` run 5: citing_works: expected 12, got 16

**Q28.** How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?

- `csv+padding` run 3: count: expected 4, got 5

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `csv` run 1: institution: expected 10, got 12; country: expected 20, got 21
- `csv` run 2: institution: expected 10, got 12; country: expected 20, got 21
- `csv` run 3: institution: expected 10, got 12; country: expected 20, got 21
- `csv` run 4: institution: expected 10, got 12; country: expected 20, got 21
- `csv` run 5: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 1: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 2: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 3: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 4: institution: expected 10, got 12; country: expected 20, got 21
- `csv+padding` run 5: institution: expected 10, got 12; country: expected 20, got 21

**Q30.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?

- `csv` run 1: count: expected 14, got 18
- `csv` run 2: count: expected 14, got 18
- `csv` run 3: count: expected 14, got 18
- `csv` run 4: count: expected 14, got 18
- `csv` run 5: count: expected 14, got 18
- `csv+padding` run 1: count: expected 14, got 18
- `csv+padding` run 2: count: expected 14, got 18
- `csv+padding` run 3: count: expected 14, got 18
- `csv+padding` run 4: count: expected 14, got 18
- `csv+padding` run 5: count: expected 14, got 18

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 1: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1042']
- `csv` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv` run 4: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']
- `csv` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1042']
- `csv+padding` run 1: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1042']
- `csv+padding` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1042']
- `csv+padding` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1042']
- `csv+padding` run 4: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W895', 'W922', 'W1042']
- `csv+padding` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W90', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W844', 'W895', 'W922', 'W1042']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `csv` run 1: count: expected 17, got 18
- `csv` run 2: count: expected 17, got 20
- `csv` run 3: count: expected 17, got 20
- `csv` run 4: count: expected 17, got 20
- `csv` run 5: count: expected 17, got 18
- `csv+padding` run 1: count: expected 17, got 18
- `csv+padding` run 2: count: expected 17, got 18
- `csv+padding` run 3: count: expected 17, got 18
- `csv+padding` run 4: count: expected 17, got 18
- `csv+padding` run 5: count: expected 17, got 20

**Q33.** Which of Kesting University's research works has the most citations?

- `csv` run 2: work: expected W20, got W22
- `csv` run 3: work: expected W20, got W22
- `csv` run 4: work: expected W20, got W22
- `csv+padding` run 5: work: expected W20, got W22

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 1: count: expected 7, got 6
- `csv` run 4: count: expected 7, got 6
- `csv` run 5: count: expected 7, got 6
- `csv+padding` run 1: count: expected 7, got 6

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 25, got 24
- `csv` run 4: count: expected 25, got 24
- `csv` run 5: count: expected 25, got 24
- `csv+padding` run 1: count: expected 25, got 24
- `csv+padding` run 2: count: expected 25, got 24
- `csv+ontology` run 3: count: expected 25, got 24

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 1: count: expected 36, got 26
- `csv` run 2: count: expected 36, got 26
- `csv` run 3: count: expected 36, got 26
- `csv` run 4: count: expected 36, got 26
- `csv` run 5: count: expected 36, got 26
- `csv+padding` run 1: count: expected 36, got 26
- `csv+padding` run 2: count: expected 36, got 26
- `csv+padding` run 3: count: expected 36, got 26
- `csv+padding` run 4: count: expected 36, got 26
- `csv+padding` run 5: count: expected 36, got 26
- `csv+markdown` run 1: count: expected 36, got 35
- `csv+ontology` run 2: count: expected 36, got 35
- `executed` run 4: count: expected 36, got 37

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04
- `csv` run 2: institution: expected I06, got I04
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04
- `csv+padding` run 1: institution: expected I06, got I04
- `csv+padding` run 2: institution: expected I06, got I04
- `csv+padding` run 3: institution: expected I06, got I04
- `csv+padding` run 4: institution: expected I06, got I04
- `csv+padding` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv+padding` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I06', 'I02', 'I01']
- `csv+padding` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv+padding` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `csv` run 1: count: expected 19, got 21
- `csv` run 2: count: expected 19, got 21
- `csv` run 3: count: expected 19, got 21
- `csv` run 4: count: expected 19, got 20
- `csv` run 5: count: expected 19, got 21
- `csv+padding` run 1: count: expected 19, got 21
- `csv+padding` run 2: count: expected 19, got 21
- `csv+padding` run 3: count: expected 19, got 21
- `csv+padding` run 4: count: expected 19, got 21
- `csv+padding` run 5: count: expected 19, got 21
- `csv+markdown` run 3: count: expected 19, got 20

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `csv+padding` run 5: higher: expected no, got depends

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `csv` run 1: count: expected 0, got 13
- `csv` run 2: count: expected 0, got 13
- `csv` run 3: count: expected 0, got 13
- `csv` run 4: count: expected 0, got 13
- `csv` run 5: count: expected 0, got 13
- `csv+padding` run 1: count: expected 0, got 13
- `csv+padding` run 2: count: expected 0, got 13
- `csv+padding` run 3: count: expected 0, got 13
- `csv+padding` run 4: count: expected 0, got 13
- `csv+padding` run 5: count: expected 0, got 13

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
- `executed` run 1: parent: expected I06, got I01
- `executed` run 2: parent: expected I06, got I01
- `executed` run 3: parent: expected I06, got I01
- `executed` run 4: parent: expected I06, got I01
- `executed` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Explains Rostval's small share (four authors, one from Rostval) but only vaguely says Kesting's works are mostly by its own authors, without clear larger-share reasoning such as few co-authors; the Rostval point is met, Kesting point is roughly met but thin.
- `csv` run 4: Explains Rostval's small share (one of four authors) but says Kesting's works are mostly by Kesting authors, which matches the second point only loosely; it lacks an explicit statement of the swap's cause beyond that, though it covers both. Treated as partial because Kesting's 'larger shares' claim is stated without the few-co-authors detail.
- `csv+padding` run 1: Correctly says Rostval's works are shared across four institutions at small shares, but does not say Kesting holds larger shares via solo or few co-authors beyond 'largely own authors'; roughly meets both but lacks the explicit swap explanation.
- `csv+padding` run 2: Gives Rostval's small share (one of four authors per work), but Kesting's larger shares are only partly stated: 'mostly its own authors' roughly matches, though the explanation is thin and the count of 12 is unsupported.
- `csv+padding` run 5: Correctly says Rostval has one author in four per work, so a small share; but says Kesting's works are mostly by Kesting authors, which matches point 2 only loosely. Actually both points are covered, though 'mostly written by Kesting authors' is acceptable, so this is near-correct but the explanation frames full-count lead rather than the swap clearly.
- `csv+markdown` run 5: Gives Rostval's one-in-four share (small share per multi-author work), and says Kesting's works are mostly by its own authors, but it uses IDs I09/I07 rather than names and doesn't clearly tie the swap to the 2024 ordering; mostly meets both points.
- `executed` run 3: Rostval's small share (one author of four) is covered, but Kesting's larger shares are stated only partly, since '11 in total' is given while the 'mostly Kesting authors alone or small teams' point is present; however the answer never states the swap between full and fractional counting explicitly
- `executed` run 4: Gets Kesting's larger shares (mostly Kesting-only authors), but Rostval's explanation is garbled: it says one Rostval author in four, not that most works are multi-author with a single Rostval author giving a small share.
- `executed` run 5: Explains Rostval's shared co-authorships (one of four authors, 0.25 share) but only says Kesting's works are mostly by Kesting authors; this loosely meets the second point, yet the answer uses IDs I09/I07 without naming institutions and the direction is ambiguous

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise and says W70 is a University of Albury work, contradicting the checklist that it is credited to the Halloran Institute and does not roll up.
- `csv` run 2: Answer contradicts the key: it claims W70 counts toward Albury, whereas the checklist says only the last-listed affiliation counts (Halloran Institute, an affiliated institute, not a unit), so it doesn't roll up.
- `csv` run 3: Rejects the premise; the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, an affiliated institute that doesn't roll up to Albury. Answer meets neither point.
- `csv` run 4: Answer rejects the premise and says W70 counts via first-listed affiliation; checklist says only the last-listed affiliation counts, crediting the Halloran Institute, an affiliated institute not rolling up to Albury.
- `csv` run 5: Asserts the premise is false and that W70 counts for Albury; the key says only the last-listed affiliation counts, crediting Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv+padding` run 1: Contradicts the key: W70 is credited to the Halloran Institute (last-listed affiliation), an affiliated institute that doesn't roll up to Albury; the answer claims it counts for Albury.
- `csv+padding` run 2: Answer says W70 does belong to Albury via I04→I03→I02, contradicting the key (only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that doesn't roll up).
- `csv+padding` run 3: Answer rejects the premise and says W70 counts for Albury; it does not say only the last-listed affiliation counts or that Halloran is an affiliated institute not rolling up.
- `csv+padding` run 4: Answer claims W70 is a University of Albury work, contradicting the checklist: only the last-listed affiliation counts (Halloran) and Halloran is an affiliated institute that does not roll up to Albury.
- `csv+padding` run 5: Rejects the premise; the key says only the last-listed affiliation counts, crediting W70 to Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `executed` run 1: Says W70 is credited to I06 (Halloran) and that I06 is an affiliate outside the unit roll-up, but never states the rule that only the last-listed affiliation counts.
- `executed` run 2: Credits W70 to the Halloran Institute and says I06 doesn't roll up to the University of Albury, but never states the rule that only the last-listed affiliation counts.
- `executed` run 3: Says W70 is credited to I06, an affiliated institute that does not roll up, but omits that only the last-listed affiliation counts
- `executed` run 4: Says the credit is the Halloran Institute and that it is an affiliate not counted toward Albury, but doesn't state that only the last-listed affiliation counts.
- `executed` run 5: Says W70 credits the Halloran Institute (I06) which does not roll up to the University, but never states that only the last-listed affiliation counts

