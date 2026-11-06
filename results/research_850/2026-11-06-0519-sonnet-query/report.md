# research_850: claude:sonnet, 2026-11-06 05:19

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `sql` | **38%** | 26% to 50% | 10 of 48 |
| `sql+markdown` | **80%** | 74% to 85% | 32 of 48 |
| `sql+executed` | **92%** | 84% to 98% | 4 of 48 |
| `sparql` | **30%** | 20% to 41% | 18 of 48 |
| `sparql+ontology` | **85%** | 79% to 90% | 25 of 48 |

## Against `sql`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `sql+markdown` | +42 points | +31 to +54 |
| `sql+executed` | +54 points | +39 to +68 |
| `sparql` | -7 points | -13 to -2 |
| `sparql+ontology` | +48 points | +35 to +60 |

## By question

| Question | Graded by | `sql` | `sql+markdown` | `sql+executed` | `sparql` | `sparql+ontology` |
|---|---|---|---|---|---|---|
| Q1 | code | ✅ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ❌ ❌ ❌ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ❌ | ❌ ❌ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q11 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q12 | code | ❌ ✅ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ 🟡 🟡 🟡 |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ❌ |
| Q14 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ❌ ❌ | ✅ ❌ 🟡 ❌ ❌ |
| Q15 | code | ❌ ✅ ❌ ✅ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q16 | code | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ❌ ❌ ✅ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ✅ |
| Q21 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ❌ ❌ | 🟡 ✅ ✅ ✅ ✅ |
| Q23 | code | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ 🟡 ✅ | 🟡 🟡 ❌ ❌ ❌ | 🟡 ❌ ✅ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q26 | code | ❌ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | 🟡 🟡 🟡 🟡 🟡 | ✅ 🟡 ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 ❌ 🟡 🟡 ❌ | ✅ 🟡 ✅ ✅ 🟡 |
| Q30 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q33 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ❌ ✅ ❌ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ✅ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ❌ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 ✅ ✅ 🟡 🟡 | 🟡 🟡 🟡 ✅ 🟡 | 🟡 ❌ ❌ 🟡 ❌ | 🟡 🟡 🟡 ❌ 🟡 |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 | ❌ ❌ 🟡 ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `sql` | 43% | 92% |
| `sql+markdown` | 87% | 89% |
| `sql+executed` | 67% | 83% |
| `sparql` | 37% | 87% |
| `sparql+ontology` | 80% | 89% |

**The checklist grader agreed with itself** on 43 of 50 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `sql` run 2: count: expected 3, got 1
- `sql` run 3: count: expected 3, got 1
- `sql` run 4: count: expected 3, got 1
- `sql` run 5: count: expected 3, got 1
- `sql+markdown` run 1: count: expected 3, got 1
- `sql+markdown` run 3: count: expected 3, got 1
- `sql+markdown` run 4: count: expected 3, got 1
- `sql+markdown` run 5: count: expected 3, got 1
- `sql+executed` run 5: count: expected 3, got 1
- `sparql` run 1: count: expected 3, got 1
- `sparql` run 2: count: expected 3, got 1
- `sparql` run 3: count: expected 3, got 1
- `sparql` run 4: count: expected 3, got 1
- `sparql` run 5: count: expected 3, got 1
- `sparql+ontology` run 1: count: expected 3, got 1
- `sparql+ontology` run 3: count: expected 3, got 1
- `sparql+ontology` run 4: count: expected 3, got 1
- `sparql+ontology` run 5: count: expected 3, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `sql+markdown` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W06', 'W09', 'W10', 'W11', 'W12']
- `sql+executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984']
- `sql+executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984']
- `sql+executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984']
- `sql+executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984']
- `sql+executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984']
- `sparql` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W04', 'W05', 'W06', 'W1005', 'W12', 'W238', 'W271', 'W374', 'W464', 'W676', 'W813', 'W949', 'W02', 'W07', 'W1048', 'W1050', 'W19', 'W449', 'W663', 'W869', 'W972', 'W03', 'W206', 'W763', 'W817']
- `sparql+ontology` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `sparql+ontology` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']

**Q4.** How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?

- `sql+markdown` run 3: count: expected 9, got 5
- `sparql` run 5: count: expected 9, got 7

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `sparql` run 3: author: expected A01, got A110
- `sparql` run 5: author: expected A01, got None

**Q7.** How many research works has Mara Ellison authored?

- `sql` run 1: count: expected 19, got 23
- `sql` run 2: count: expected 19, got 22
- `sql` run 3: count: expected 19, got 23
- `sql` run 4: count: expected 19, got 22
- `sql` run 5: count: expected 19, got 23
- `sql+markdown` run 3: count: expected 19, got 5
- `sql+markdown` run 4: count: expected 19, got 29
- `sparql` run 1: count: expected 19, got 22
- `sparql` run 2: count: expected 19, got 23
- `sparql` run 3: count: expected 19, got 22
- `sparql` run 4: count: expected 19, got 22
- `sparql` run 5: count: expected 19, got 17

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `sql` run 1: count: expected 95, got 119
- `sql` run 2: count: expected 95, got 106
- `sql` run 3: count: expected 95, got 118
- `sql` run 4: count: expected 95, got 117
- `sql` run 5: count: expected 95, got 118
- `sql+markdown` run 2: count: expected 95, got 65
- `sql+markdown` run 3: count: expected 95, got 65
- `sql+markdown` run 4: count: expected 95, got 111
- `sparql` run 1: count: expected 95, got 116
- `sparql` run 2: count: expected 95, got 141
- `sparql` run 3: count: expected 95, got 117
- `sparql` run 4: count: expected 95, got 116
- `sparql` run 5: count: expected 95, got 116
- `sparql+ontology` run 1: count: expected 95, got 53

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `sql` run 1: count: expected 140, got 176
- `sql` run 2: count: expected 140, got 155
- `sql` run 3: count: expected 140, got 173
- `sql` run 4: count: expected 140, got 174
- `sql` run 5: count: expected 140, got 173
- `sql+markdown` run 2: count: expected 140, got 72
- `sql+markdown` run 3: count: expected 140, got 72
- `sql+markdown` run 4: count: expected 140, got 159
- `sparql` run 1: count: expected 140, got 171
- `sparql` run 2: count: expected 140, got 201
- `sparql` run 3: count: expected 140, got 174
- `sparql` run 4: count: expected 140, got 171
- `sparql` run 5: count: expected 140, got 171
- `sparql+ontology` run 1: count: expected 140, got 85

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `sql` run 1: count: expected 59, got 89
- `sql` run 2: count: expected 59, got 58
- `sql` run 3: count: expected 59, got 89
- `sql` run 4: count: expected 59, got 65
- `sql` run 5: count: expected 59, got 89
- `sql+markdown` run 2: count: expected 59, got 48
- `sql+markdown` run 3: count: expected 59, got 48
- `sql+markdown` run 4: count: expected 59, got 92
- `sparql` run 1: count: expected 59, got 84
- `sparql` run 2: count: expected 59, got 111
- `sparql` run 3: count: expected 59, got 65
- `sparql` run 4: count: expected 59, got 65
- `sparql` run 5: count: expected 59, got None
- `sparql+ontology` run 1: count: expected 59, got 48

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `sql` run 1: full: expected 13, got 14; fractional: expected 11, got 12
- `sql` run 3: full: expected 13, got 14; fractional: expected 11, got 12
- `sql` run 4: full: expected 13, got 14; fractional: expected 11, got 12.0
- `sql` run 5: full: expected 13, got 14; fractional: expected 11, got 12
- `sql+markdown` run 2: full: expected 13, got 10; fractional: expected 11, got 6.75
- `sql+markdown` run 3: full: expected 13, got 10; fractional: expected 11, got 5.5
- `sparql` run 1: full: expected 13, got 14; fractional: expected 11, got 12
- `sparql` run 2: full: expected 13, got 0; fractional: expected 11, got 0
- `sparql` run 3: full: expected 13, got 15; fractional: expected 11, got 8.5
- `sparql` run 4: full: expected 13, got 14; fractional: expected 11, got 12
- `sparql` run 5: full: expected 13, got None; fractional: expected 11, got None
- `sparql+ontology` run 1: full: expected 13, got 10; fractional: expected 11, got 7.5
- `sparql+ontology` run 3: fractional: expected 11, got 8.5
- `sparql+ontology` run 4: fractional: expected 11, got 6
- `sparql+ontology` run 5: fractional: expected 11, got 5.83

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `sparql` run 2: full: expected I09, got I07; fractional: expected I07, got I09
- `sparql` run 3: full: expected I09, got I07; fractional: expected I07, got I09
- `sparql` run 5: full: expected I09, got None; fractional: expected I07, got None
- `sparql+ontology` run 5: full: expected I09, got I07; fractional: expected I07, got I09

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `sql` run 1: full: expected 46, got 48; fractional: expected 42, got 44
- `sql` run 2: full: expected 46, got 47; fractional: expected 42, got 43
- `sql` run 3: full: expected 46, got 48; fractional: expected 42, got 44
- `sql` run 4: full: expected 46, got 47; fractional: expected 42, got 43.0
- `sql` run 5: full: expected 46, got 48; fractional: expected 42, got 44
- `sql+markdown` run 3: full: expected 46, got 26; fractional: expected 42, got 17.92
- `sparql` run 2: full: expected 46, got 0; fractional: expected 42, got 0
- `sparql` run 3: full: expected 46, got 30; fractional: expected 42, got 17.5
- `sparql` run 4: full: expected 46, got 47; fractional: expected 42, got 43
- `sparql` run 5: full: expected 46, got None; fractional: expected 42, got None
- `sparql+ontology` run 2: full: expected 46, got 45; fractional: expected 42, got 41.67
- `sparql+ontology` run 3: fractional: expected 42, got 40
- `sparql+ontology` run 4: full: expected 46, got 36; fractional: expected 42, got 30
- `sparql+ontology` run 5: full: expected 46, got 29; fractional: expected 42, got 15.5

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `sql` run 1: count: expected 25, got 27
- `sql` run 3: count: expected 25, got 27
- `sql` run 5: count: expected 25, got 27
- `sql+markdown` run 3: count: expected 25, got 1
- `sparql` run 2: count: expected 25, got 0
- `sparql` run 3: count: expected 25, got 20
- `sparql` run 5: count: expected 25, got None
- `sparql+ontology` run 1: count: expected 25, got 30

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `sql` run 1: count: expected 88, got 97
- `sql` run 2: count: expected 88, got 89
- `sql` run 3: count: expected 88, got 97
- `sql` run 5: count: expected 88, got 97
- `sql+markdown` run 3: count: expected 88, got 5
- `sparql` run 1: count: expected 88, got 95
- `sparql` run 2: count: expected 88, got 106
- `sparql` run 3: count: expected 88, got 95
- `sparql` run 5: count: expected 88, got None

**Q17.** Which of Mara Ellison's works are not research output because of their document type?

- `sql` run 2: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W02', 'W04', 'W05', 'W271', 'W612', 'W663', 'W813', 'W936', 'W949']
- `sql` run 3: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W271', 'W936', 'W05', 'W813', 'W949', 'W02', 'W612', 'W663']
- `sql` run 5: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W612', 'W663', 'W271', 'W949', 'W02', 'W813', 'W05', 'W936']
- `sql+markdown` run 3: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W06']
- `sparql` run 4: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W02', 'W04', 'W05', 'W271', 'W612', 'W663', 'W813', 'W936', 'W949']
- `sparql` run 5: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W271', 'W05', 'W813', 'W949']
- `sparql+ontology` run 2: works: expected ['W04', 'W05', 'W271', 'W813', 'W936', 'W949'], got ['W04', 'W05']

**Q18.** How many distinct research works has Priya Ramanathan (A07) authored?

- `sql+markdown` run 3: count: expected 15, got 5
- `sql+markdown` run 4: count: expected 15, got 16

**Q19.** How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?

- `sql` run 1: count: expected 27, got 30
- `sql` run 2: count: expected 27, got 30
- `sql` run 3: count: expected 27, got 30
- `sql` run 4: count: expected 27, got 30
- `sql` run 5: count: expected 27, got 30
- `sql+markdown` run 3: count: expected 27, got 6
- `sparql` run 1: count: expected 27, got 30
- `sparql` run 2: count: expected 27, got 30
- `sparql` run 3: count: expected 27, got 30
- `sparql` run 4: count: expected 27, got 30
- `sparql` run 5: count: expected 27, got 30
- `sparql+ontology` run 2: count: expected 27, got 30

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `sql+markdown` run 3: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got ['W02', 'W42']
- `sql+executed` run 1: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `sql+executed` run 2: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `sql+executed` run 3: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `sql+executed` run 4: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `sql+executed` run 5: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got []
- `sparql` run 1: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got ['W02', 'W42', 'W556', 'W612', 'W663']
- `sparql+ontology` run 1: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got ['W02', 'W42', 'W556', 'W612', 'W663']
- `sparql+ontology` run 2: works: expected ['W02', 'W1049', 'W210', 'W219', 'W226', 'W263', 'W322', 'W407', 'W416', 'W42', 'W432', 'W460', 'W506', 'W522', 'W524', 'W545', 'W556', 'W611', 'W612', 'W663', 'W728', 'W730', 'W877'], got ['W02', 'W42']

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `sql` run 1: count: expected 45, got 47
- `sql` run 2: count: expected 45, got 46
- `sql` run 3: count: expected 45, got 46
- `sql` run 4: count: expected 45, got 47
- `sql` run 5: count: expected 45, got 46
- `sql+markdown` run 4: count: expected 45, got 49
- `sparql` run 1: count: expected 45, got 46
- `sparql` run 2: count: expected 45, got 57
- `sparql` run 3: count: expected 45, got 47
- `sparql` run 4: count: expected 45, got 46
- `sparql` run 5: count: expected 45, got None
- `sparql+ontology` run 1: count: expected 45, got 15

**Q22.** Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?

- `sql+markdown` run 3: more_in_total: expected W30, got W31
- `sparql` run 3: more_in_window: expected W31, got W30
- `sparql` run 4: more_in_total: expected W30, got None; more_in_window: expected W31, got None
- `sparql` run 5: more_in_total: expected W30, got None; more_in_window: expected W31, got None
- `sparql+ontology` run 1: more_in_window: expected W31, got W30

**Q23.** How many citations has W30 received in total, and how many within its publication year and the two years after?

- `sql` run 1: total: expected 16, got 18
- `sql` run 2: total: expected 16, got 18
- `sql` run 3: total: expected 16, got 18
- `sql` run 4: total: expected 16, got 18
- `sql` run 5: total: expected 16, got 18
- `sql+markdown` run 3: total: expected 16, got 4; in_window: expected 2, got 3
- `sql+executed` run 4: in_window: expected 2, got 1
- `sparql` run 1: total: expected 16, got 18
- `sparql` run 2: total: expected 16, got 18
- `sparql` run 3: total: expected 16, got 18; in_window: expected 2, got 18
- `sparql` run 4: total: expected 16, got None; in_window: expected 2, got None
- `sparql` run 5: total: expected 16, got None; in_window: expected 2, got None
- `sparql+ontology` run 1: in_window: expected 2, got 16
- `sparql+ontology` run 2: total: expected 16, got 18; in_window: expected 2, got 3

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `sql` run 1: count: expected 12, got 18
- `sql` run 2: count: expected 12, got 15
- `sql` run 3: count: expected 12, got 18
- `sql` run 5: count: expected 12, got 18
- `sql+markdown` run 3: count: expected 12, got 1
- `sql+markdown` run 4: count: expected 12, got 18
- `sparql` run 1: count: expected 12, got 15
- `sparql` run 2: count: expected 12, got 15
- `sparql` run 5: count: expected 12, got None

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `sql` run 1: count: expected 20, got 42
- `sql` run 2: count: expected 20, got 41
- `sql` run 3: count: expected 20, got 42
- `sql` run 4: count: expected 20, got 41
- `sql` run 5: count: expected 20, got 42
- `sql+markdown` run 3: count: expected 20, got 2
- `sparql` run 1: count: expected 20, got 41
- `sparql` run 2: count: expected 20, got 41
- `sparql` run 3: count: expected 20, got 41
- `sparql` run 4: count: expected 20, got 41
- `sparql` run 5: count: expected 20, got None
- `sparql+ontology` run 2: count: expected 20, got 33

**Q26.** Does W23 count towards Kesting University's research output?

- `sql` run 1: counts: expected no, got yes
- `sql` run 3: counts: expected no, got yes
- `sql` run 5: counts: expected no, got yes
- `sparql` run 5: counts: expected no, got depends

**Q27.** Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?

- `sql` run 1: citing_works: expected 12, got 16
- `sql` run 2: citing_works: expected 12, got 13
- `sql` run 3: citing_works: expected 12, got 16
- `sql` run 4: citing_works: expected 12, got 16
- `sql` run 5: citing_works: expected 12, got 16
- `sql+markdown` run 3: institution: expected I12, got I09; citing_works: expected 12, got 7
- `sparql` run 1: citing_works: expected 12, got 16
- `sparql` run 2: citing_works: expected 12, got 16
- `sparql` run 3: citing_works: expected 12, got 16
- `sparql` run 4: citing_works: expected 12, got 16
- `sparql` run 5: institution: expected I12, got None; citing_works: expected 12, got None
- `sparql+ontology` run 2: institution: expected I12, got I09; citing_works: expected 12, got 4

**Q28.** How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?

- `sql+markdown` run 3: count: expected 4, got 7
- `sparql` run 5: count: expected 4, got None

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `sql` run 1: institution: expected 10, got 12; country: expected 20, got 21
- `sql` run 2: institution: expected 10, got 11; country: expected 20, got 21
- `sql` run 3: institution: expected 10, got 12; country: expected 20, got 21
- `sql` run 4: institution: expected 10, got 12; country: expected 20, got 21
- `sql` run 5: institution: expected 10, got 12; country: expected 20, got 21
- `sql+markdown` run 2: institution: expected 10, got 6
- `sql+markdown` run 3: author: expected 7, got 1; institution: expected 10, got 2; country: expected 20, got 4
- `sparql` run 1: institution: expected 10, got 12; country: expected 20, got 21
- `sparql` run 2: author: expected 7, got 0; institution: expected 10, got 0; country: expected 20, got 0
- `sparql` run 3: institution: expected 10, got 12; country: expected 20, got 21
- `sparql` run 4: institution: expected 10, got 12; country: expected 20, got 21
- `sparql` run 5: author: expected 7, got None; institution: expected 10, got None; country: expected 20, got None
- `sparql+ontology` run 2: author: expected 7, got 8; country: expected 20, got 12
- `sparql+ontology` run 5: country: expected 20, got 19

**Q30.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?

- `sql` run 1: count: expected 14, got 18
- `sql` run 2: count: expected 14, got 16
- `sql` run 3: count: expected 14, got 18
- `sql` run 4: count: expected 14, got 18
- `sql` run 5: count: expected 14, got 18
- `sql+markdown` run 2: count: expected 14, got 5
- `sql+markdown` run 3: count: expected 14, got 3
- `sparql` run 1: count: expected 14, got 18
- `sparql` run 2: count: expected 14, got 0
- `sparql` run 3: count: expected 14, got 18
- `sparql` run 4: count: expected 14, got 18
- `sparql` run 5: count: expected 14, got None
- `sparql+ontology` run 2: count: expected 14, got 12

**Q31.** Which works cite at least one of the works that cite W01?

- `sql` run 1: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W844', 'W895', 'W90', 'W922']
- `sql` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W801', 'W844', 'W1042', 'W396', 'W682', 'W90', 'W922', 'W337', 'W546', 'W51', 'W50', 'W52', 'W895', 'W338']
- `sql` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W396', 'W682', 'W50', 'W52', 'W1042', 'W90', 'W922', 'W51', 'W895', 'W801', 'W844', 'W337', 'W546', 'W338']
- `sql` run 4: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W337', 'W546', 'W51', 'W682', 'W801', 'W844', 'W50', 'W396', 'W1042', 'W895', 'W338', 'W52', 'W90', 'W922']
- `sql` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W801', 'W844', 'W50', 'W396', 'W90', 'W922', 'W337', 'W546', 'W52', 'W51', 'W338', 'W682', 'W895', 'W1042']
- `sql+markdown` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W16', 'W19', 'W25']
- `sparql` run 1: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W682', 'W338', 'W396', 'W50', 'W51', 'W546', 'W895', 'W922', 'W52', 'W90', 'W1042', 'W337', 'W801', 'W844']
- `sparql` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W844', 'W895', 'W90', 'W922']
- `sparql` run 3: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W682', 'W338', 'W396', 'W50', 'W51', 'W546', 'W895', 'W922', 'W52', 'W90', 'W1042', 'W337', 'W801', 'W844']
- `sparql` run 4: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W682', 'W338', 'W396', 'W50', 'W51', 'W546', 'W895', 'W922', 'W52', 'W90', 'W1042', 'W337', 'W801', 'W844']
- `sparql` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got []
- `sparql+ontology` run 2: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W338', 'W396', 'W546', 'W895', 'W922']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `sql` run 1: count: expected 17, got 20
- `sql` run 2: count: expected 17, got 20
- `sql` run 3: count: expected 17, got 20
- `sql` run 4: count: expected 17, got 20
- `sql` run 5: count: expected 17, got 20
- `sql+markdown` run 3: count: expected 17, got 5
- `sparql` run 1: count: expected 17, got 20
- `sparql` run 2: count: expected 17, got 20
- `sparql` run 3: count: expected 17, got 20
- `sparql` run 4: count: expected 17, got 20
- `sparql` run 5: count: expected 17, got None
- `sparql+ontology` run 2: count: expected 17, got 15

**Q33.** Which of Kesting University's research works has the most citations?

- `sql` run 1: work: expected W20, got W22
- `sql` run 2: work: expected W20, got W22
- `sql` run 3: work: expected W20, got W22
- `sql` run 4: work: expected W20, got W22
- `sql` run 5: work: expected W20, got W22
- `sql+markdown` run 3: work: expected W20, got W08
- `sparql` run 1: work: expected W20, got W22
- `sparql` run 2: work: expected W20, got W22
- `sparql` run 3: work: expected W20, got W22
- `sparql` run 4: work: expected W20, got W22
- `sparql` run 5: work: expected W20, got None
- `sparql+ontology` run 2: work: expected W20, got W22

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `sql` run 1: count: expected 7, got 26
- `sql` run 2: count: expected 7, got 6
- `sql` run 3: count: expected 7, got 26
- `sql` run 4: count: expected 7, got 6
- `sql` run 5: count: expected 7, got 26
- `sql+markdown` run 2: count: expected 7, got 6
- `sql+markdown` run 3: count: expected 7, got 6
- `sparql` run 1: count: expected 7, got 25
- `sparql` run 2: count: expected 7, got 0
- `sparql` run 3: count: expected 7, got 5
- `sparql` run 4: count: expected 7, got 6
- `sparql` run 5: count: expected 7, got None
- `sparql+ontology` run 1: count: expected 7, got 6

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `sql` run 2: count: expected 25, got 24
- `sql` run 4: count: expected 25, got 24
- `sql+markdown` run 4: count: expected 25, got 26
- `sparql` run 1: count: expected 25, got 24
- `sparql` run 2: count: expected 25, got 33
- `sparql` run 3: count: expected 25, got 24
- `sparql` run 4: count: expected 25, got 24
- `sparql` run 5: count: expected 25, got None

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `sql` run 1: count: expected 36, got 26
- `sql` run 2: count: expected 36, got 26
- `sql` run 3: count: expected 36, got 26
- `sql` run 4: count: expected 36, got 26
- `sql` run 5: count: expected 36, got 26
- `sql+markdown` run 3: count: expected 36, got 1
- `sparql` run 1: count: expected 36, got 26
- `sparql` run 2: count: expected 36, got 43
- `sparql` run 3: count: expected 36, got 26
- `sparql` run 4: count: expected 36, got 26
- `sparql` run 5: count: expected 36, got None

**Q37.** Which institution is W70 credited to?

- `sql` run 1: institution: expected I06, got I04
- `sql` run 2: institution: expected I06, got I04
- `sql` run 3: institution: expected I06, got I04
- `sql` run 4: institution: expected I06, got I04
- `sql` run 5: institution: expected I06, got I04
- `sparql` run 1: institution: expected I06, got I04
- `sparql` run 2: institution: expected I06, got I04
- `sparql` run 3: institution: expected I06, got I04
- `sparql` run 4: institution: expected I06, got I04
- `sparql` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `sql` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sql` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sql` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I02', 'I01', 'I06']
- `sql` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sql` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sparql` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I02', 'I01', 'I06']
- `sparql` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `sparql` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sparql` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I02', 'I01', 'I06']
- `sparql` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `sql` run 1: count: expected 19, got 21
- `sql` run 3: count: expected 19, got 21
- `sql` run 4: count: expected 19, got 21
- `sql` run 5: count: expected 19, got 21
- `sql+markdown` run 2: count: expected 19, got 13
- `sql+markdown` run 3: count: expected 19, got 18
- `sparql` run 1: count: expected 19, got 21
- `sparql` run 2: count: expected 19, got 21
- `sparql` run 3: count: expected 19, got 20
- `sparql` run 4: count: expected 19, got 21
- `sparql` run 5: count: expected 19, got None
- `sparql+ontology` run 1: count: expected 19, got 15

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `sql` run 1: count: expected 0, got 13
- `sql` run 2: count: expected 0, got 13
- `sql` run 3: count: expected 0, got 13
- `sql` run 4: count: expected 0, got 13
- `sql` run 5: count: expected 0, got 13
- `sparql` run 1: count: expected 0, got 13
- `sparql` run 2: count: expected 0, got 13
- `sparql` run 3: count: expected 0, got 13
- `sparql` run 4: count: expected 0, got 13
- `sparql` run 5: count: expected 0, got None

**Q43.** Is W07 research output?

- `sql` run 1: research: expected no, got yes
- `sql` run 2: research: expected no, got yes
- `sql` run 3: research: expected no, got yes
- `sql` run 4: research: expected no, got yes
- `sql` run 5: research: expected no, got yes
- `sparql` run 1: research: expected no, got yes
- `sparql` run 2: research: expected no, got yes
- `sparql` run 3: research: expected no, got yes
- `sparql` run 4: research: expected no, got yes
- `sparql` run 5: research: expected no, got yes

**Q44.** Which institutions are part of the Albury University System, at any level below it?

- `sql` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sql` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sql` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sql` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sparql` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sparql` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sparql` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sparql` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']
- `sparql` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05', 'I19', 'I20'], got ['I02', 'I03', 'I04', 'I05', 'I06', 'I19', 'I20', 'I21']

**Q45.** How many research works is the Halloran Institute for Coastal Studies (I06) credited with?

- `sql` run 1: count: expected 16, got 22
- `sql` run 2: count: expected 16, got 22
- `sql` run 3: count: expected 16, got 22
- `sql` run 4: count: expected 16, got 22
- `sql` run 5: count: expected 16, got 22
- `sparql` run 1: count: expected 16, got 22
- `sparql` run 2: count: expected 16, got 22
- `sparql` run 3: count: expected 16, got 22
- `sparql` run 4: count: expected 16, got 22
- `sparql` run 5: count: expected 16, got None

**Q46.** What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?

- `sql` run 1: parent: expected I06, got I01
- `sql` run 2: parent: expected I06, got I01
- `sql` run 3: parent: expected I06, got I01
- `sql` run 4: parent: expected I06, got I01
- `sql` run 5: parent: expected I06, got I01
- `sql+executed` run 1: parent: expected I06, got I01
- `sql+executed` run 2: parent: expected I06, got I01
- `sql+executed` run 3: parent: expected I06, got I01
- `sql+executed` run 5: parent: expected I06, got I01
- `sparql` run 1: parent: expected I06, got I01
- `sparql` run 2: parent: expected I06, got I01
- `sparql` run 3: parent: expected I06, got I01
- `sparql` run 4: parent: expected I06, got I01
- `sparql` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `sql` run 1: Says Kesting (I07) keeps larger shares because its authors dominate, but doesn't say Rostval's works have several authors with only one from Rostval; it does say I09 has many outside authors, which is roughly equivalent, though institutions aren't named
- `sql` run 2: Says Rostval's works are shared with other institutions (small share), but doesn't say Kesting holds larger shares; it says Kesting's works are mostly credited to its own authors, which does match the second point, though it omits that Rostval's works mostly have one Rostval author among several.
- `sql` run 3: Explains the low-share side (I09, presumably Rostval) due to co-authorship, and that I07 has few authors, but doesn't say only one author is from that institution or that Kesting has many sole-institution works; roughly matches both points loosely using IDs
- `sql` run 4: Says Rostval's works have many authors so shares are small, and Kesting has fewer authors; but doesn't state that only one author per work is from Rostval, and Kesting's explanation is only loosely aligned (fewer authors, not Kesting-alone/few co-authors).
- `sql` run 5: Explains Kesting's (I07) larger shares from works mostly credited to its own authors, but doesn't say Rostval's works are multi-author with only one Rostval author getting a small share; it says shares go to other institutions, which is roughly aligned yet vague, and it doesn't name the institutions or the 2024 swap clearly.
- `sql+markdown` run 1: Says Rostval's works have many authors credited elsewhere (matches point 1) but doesn't say Kesting holds larger shares, e.g. sole or few co-authors; only states Kesting keeps 11.0.
- `sql+markdown` run 4: Covers Rostval's (I09) small shares from split authorship, but never says Kesting's works are mostly solo or have few co-authors; it gives only the 11.0 vs 4.0 totals.
- `sql+markdown` run 5: Says Rostval's works have many authors so shares are thin and Kesting's have few authors so shares stay large, but omits that only one author per work is from Rostval and that many Kesting works are by Kesting authors alone.
- `sql+executed` run 1: The final point that I09's 2024 works are heavily shared matches Rostval's small share per work. But the answer contradicts itself (its first sentence says I07 has more co-authors), uses IDs instead of names, and never says Kesting's works are mostly solo or few-author.
- `sql+executed` run 2: Says I09 (Rostval) is heavily co-authored so gets small shares, but doesn't say only one author is from Rostval per work, and doesn't state that Kesting holds larger shares via solo or few co-authors; also uses IDs rather than names.
- `sql+executed` run 3: Says Rostval's works are shared with other institutions so its share is small (meets point 1), and Kesting's are mostly Kesting-only (meets point 2); but it doesn't explicitly say Rostval has only one author per work, and the 'Kesting-only' claim is stated. Treated as largely meeting both, yet the 'only one from Rostval' detail is missing.
- `sql+executed` run 5: Rostval's small share from many outside co-authors is covered, but Kesting's larger shares are only vaguely stated as 'few authors', not explicitly authors from Kesting alone or with few co-authors; also the Rostval point says 'many authors from other institutions' rather than only one from Rostval
- `sparql` run 1: Gets Kesting's large fractional share (few co-authors) and Rostval's many-author works, but doesn't clearly say only one Rostval author per work gives it a small share; also adds counts not in checklist.
- `sparql` run 2: Answer gives no explanation and meets neither point about Rostval's shared authorship or Kesting's larger shares.
- `sparql` run 3: Says not computed; its guess (Kesting has larger author lists) contradicts the key, which says Kesting holds larger shares and Rostval's works have many co-authors.
- `sparql` run 4: Covers Rostval's small shares from co-authorship and Kesting's larger shares, but doesn't say Rostval's works have only one Rostval author each or that Kesting's are sole/few-coauthor; admits not verified, still roughly matches both points
- `sparql` run 5: No answer given; meets none of the checklist points
- `sparql+ontology` run 1: Says Rostval's works are spread across more authors per work (matches first point loosely, doesn't say only one is from Rostval), but omits Kesting holding larger shares via sole or few co-authors.
- `sparql+ontology` run 2: Rostval point is covered (many authors, small share), but the answer doesn't say only one author is from Rostval; Kesting's fewer authors is vague and misses that Kesting authors hold larger shares (sole or few co-authors).
- `sparql+ontology` run 3: Gives the general mechanism and says the full-count leader's works have more authors with smaller shares, but never explicitly says Kesting holds larger shares (sole or few co-authors), and the fractional figures were not checked.
- `sparql+ontology` run 4: Guesses I09 works have more authors, which is unverified and doesn't match the checklist's Rostval/Kesting explanation (Rostval single-author share of multi-author works; Kesting larger shares).
- `sparql+ontology` run 5: Says I09 (Kesting) has fewer authors per work and larger shares, but omits that Rostval's works have several authors with only one from Rostval, giving it small shares.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `sql` run 1: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, crediting Halloran Institute, an affiliated institute not rolling up to Albury
- `sql` run 2: Claims W70 should count for Albury; misses that only the last-listed affiliation (Halloran Institute) counts and that it is an affiliated institute, not a unit.
- `sql` run 3: Rejects the premise and misses both points: the last-listed affiliation rule and Halloran being an affiliated institute, not a unit
- `sql` run 4: Contradicts the key: W70 is not a University of Albury work because the last-listed affiliation (Halloran Institute) is credited, and that institute is affiliated, not a unit, so it doesn't roll up.
- `sql` run 5: Rejects the premise and says W70 counts for Albury; the checklist says only the last-listed affiliation counts (Halloran Institute), and that institute is affiliated, not a unit, so it does not roll up.
- `sql+executed` run 1: It says W70 is credited to the Halloran Institute and that affiliates don't roll up to the University of Albury. It omits the rule that only the last-listed affiliation counts.
- `sql+executed` run 2: Says the author is credited to I06 (Halloran), an affiliate that doesn't roll up to I02, but omits that only the last-listed affiliation counts.
- `sql+executed` run 3: Gives the affiliate/no roll-up point and the credit to I06, but omits that only the last-listed affiliation counts.
- `sql+executed` run 4: Says the work is credited to the affiliate I06, which doesn't roll up to I02, but never states that only the last-listed affiliation counts.
- `sql+executed` run 5: Says the Halloran Institute is an affiliate with no roll-up to the University, but does not state that only the last-listed affiliation counts
- `sparql` run 1: Denies that W70 is excluded and misses both points: only the last-listed affiliation counts (Halloran Institute) and Halloran is an affiliated institute, not a unit, so it doesn't roll up.
- `sparql` run 2: Answer does not state the last-listed-affiliation rule or that Halloran is an affiliated institute not rolling up; it only says not determined.
- `sparql` run 3: Does not state the last-listed-affiliation rule or that the Halloran Institute is an affiliate, not a unit, so its works don't roll up; it only guesses at the itype-AFF exclusion and admits it is unconfirmed.
- `sparql` run 4: Does not state the last-listed-affiliation rule or Halloran Institute being an affiliated institute, not a unit; says reason could not be confirmed
- `sparql` run 5: No answer given; meets none of the checklist points

