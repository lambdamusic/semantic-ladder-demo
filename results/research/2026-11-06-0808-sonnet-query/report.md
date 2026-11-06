# research: claude:sonnet, 2026-11-06 08:08

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `sql` | **52%** | 39% to 65% | 4 of 48 |
| `sql+markdown` | **96%** | 91% to 100% | 1 of 48 |
| `sql+executed` | **93%** | 87% to 98% | 6 of 48 |
| `sparql` | **40%** | 29% to 51% | 28 of 48 |
| `sparql+ontology` | **81%** | 77% to 85% | 39 of 48 |

## Against `sql`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `sql+markdown` | +45 points | +32 to +58 |
| `sql+executed` | +41 points | +26 to +56 |
| `sparql` | -12 points | -16 to -7 |
| `sparql+ontology` | +30 points | +16 to +43 |

## By question

| Question | Graded by | `sql` | `sql+markdown` | `sql+executed` | `sparql` | `sparql+ontology` |
|---|---|---|---|---|---|---|
| Q1 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q11 | code | ❌ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | 🟡 ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q16 | code | ❌ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q26 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ 🟡 ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q33 | code | ❌ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q35 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q36 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 ❌ 🟡 🟡 | 🟡 ❌ 🟡 🟡 🟡 | ✅ ✅ ❌ ✅ 🟡 |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ 🟡 ✅ 🟡 | 🟡 🟡 🟡 🟡 🟡 | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `sql` | 50% | 94% |
| `sql+markdown` | 100% | 100% |
| `sql+executed` | 73% | 89% |
| `sparql` | 40% | 75% |
| `sparql+ontology` | 83% | 86% |

**The checklist grader agreed with itself** on 45 of 50 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `sql` run 1: count: expected 2, got 1
- `sql` run 2: count: expected 2, got 1
- `sql` run 3: count: expected 2, got 1
- `sql` run 4: count: expected 2, got 1
- `sql` run 5: count: expected 2, got 1
- `sql+markdown` run 1: count: expected 2, got 1
- `sql+markdown` run 2: count: expected 2, got 1
- `sql+markdown` run 3: count: expected 2, got 1
- `sql+markdown` run 4: count: expected 2, got 1
- `sql+markdown` run 5: count: expected 2, got 1
- `sparql` run 1: count: expected 2, got 1
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 2, got 1
- `sparql` run 5: count: expected 2, got 1
- `sparql+ontology` run 1: count: expected 2, got 1
- `sparql+ontology` run 2: count: expected 2, got 1
- `sparql+ontology` run 3: count: expected 2, got 1
- `sparql+ontology` run 4: count: expected 2, got 1
- `sparql+ontology` run 5: count: expected 2, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `sql+executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `sql+executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `sql+executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `sql+executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `sql+executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got None

**Q3.** Is the Jonas Brandt who wrote W37 the same person as the Jonas Brandt who wrote W38?

- `sparql` run 2: no structured answer

**Q4.** How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: count: expected 2, got None

**Q5.** Is the M. Ellison who wrote W08 the same person as the Mara Ellison who wrote W01?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: same: expected no, got depends

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: author: expected A01, got None

**Q7.** How many research works has Mara Ellison authored?

- `sql` run 1: count: expected 5, got 6
- `sql` run 2: count: expected 5, got 6
- `sql` run 3: count: expected 5, got 6
- `sql` run 4: count: expected 5, got 6
- `sql` run 5: count: expected 5, got 6
- `sparql` run 1: count: expected 5, got 6
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 5, got 6
- `sparql` run 4: count: expected 5, got 6
- `sparql` run 5: count: expected 5, got 6
- `sparql+ontology` run 3: count: expected 5, got None

**Q8.** What is the ultimate parent of the Tessel Laboratory for Ocean Sensing (I04)?

- `sparql` run 2: no structured answer

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `sql` run 1: count: expected 8, got 12
- `sql` run 2: count: expected 8, got 12
- `sql` run 3: count: expected 8, got 12
- `sql` run 4: count: expected 8, got 12
- `sql` run 5: count: expected 8, got 12
- `sparql` run 1: count: expected 8, got 12
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 8, got 12
- `sparql` run 4: count: expected 8, got 12
- `sparql` run 5: count: expected 8, got 12
- `sparql+ontology` run 3: count: expected 8, got None

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `sql` run 1: count: expected 12, got 16
- `sql` run 2: count: expected 12, got 16
- `sql` run 3: count: expected 12, got 16
- `sql` run 4: count: expected 12, got 16
- `sql` run 5: count: expected 12, got 16
- `sparql` run 1: count: expected 12, got 16
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 12, got 16
- `sparql` run 4: count: expected 12, got 16
- `sparql` run 5: count: expected 12, got 16
- `sparql+ontology` run 3: count: expected 12, got None

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `sql` run 1: count: expected 6, got 9
- `sql` run 5: count: expected 6, got 9
- `sparql` run 1: count: expected 6, got 9
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 6, got 9
- `sparql` run 4: count: expected 6, got 9
- `sparql` run 5: count: expected 6, got 8
- `sparql+ontology` run 3: count: expected 6, got None

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `sql+executed` run 3: full: expected 3, got 4; fractional: expected 2, got 3
- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: full: expected 3, got None; fractional: expected 2, got None

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `sql+executed` run 3: full: expected I09, got tie
- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: full: expected I09, got None; fractional: expected I07, got None

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `sql+executed` run 1: fractional: expected 6, got 5.5
- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: full: expected 7, got None; fractional: expected 6, got None

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: count: expected 4, got None

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `sql` run 1: count: expected 10, got 11
- `sql` run 5: count: expected 10, got 11
- `sparql` run 1: count: expected 10, got 11
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 10, got 11
- `sparql` run 4: count: expected 10, got 11
- `sparql+ontology` run 3: count: expected 10, got None

**Q17.** Which of Mara Ellison's works are not research output because of their document type?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: works: expected ['W04', 'W05'], got None

**Q18.** How many distinct research works has Priya Ramanathan (A07) authored?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: count: expected 4, got None

**Q19.** How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: count: expected 7, got None

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `sql+executed` run 2: works: expected ['W02', 'W42'], got []
- `sql+executed` run 3: works: expected ['W02', 'W42'], got []
- `sql+executed` run 5: works: expected ['W02', 'W42'], got []
- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: works: expected ['W02', 'W42'], got ['W02']

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: count: expected 4, got None

**Q22.** Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: more_in_total: expected W30, got None; more_in_window: expected W31, got None

**Q23.** How many citations has W30 received in total, and how many within its publication year and the two years after?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: total: expected 5, got None; in_window: expected 1, got None

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `sql` run 1: count: expected 3, got 4
- `sql` run 2: count: expected 3, got 4
- `sql` run 3: count: expected 3, got 4
- `sql` run 4: count: expected 3, got 4
- `sql` run 5: count: expected 3, got 4
- `sparql` run 1: count: expected 3, got 4
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 3, got 4
- `sparql` run 4: count: expected 3, got 4
- `sparql+ontology` run 3: count: expected 3, got None

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `sql` run 1: count: expected 6, got 10
- `sql` run 2: count: expected 6, got 7
- `sql` run 3: count: expected 6, got 7
- `sql` run 4: count: expected 6, got 7
- `sql` run 5: count: expected 6, got 10
- `sparql` run 1: count: expected 6, got 10
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 6, got 10
- `sparql` run 4: count: expected 6, got 10
- `sparql` run 5: count: expected 6, got 9
- `sparql+ontology` run 3: count: expected 6, got None

**Q26.** Does W23 count towards Kesting University's research output?

- `sql` run 1: counts: expected no, got yes
- `sql` run 2: counts: expected no, got yes
- `sql` run 3: counts: expected no, got yes
- `sql` run 4: counts: expected no, got yes
- `sql` run 5: counts: expected no, got yes
- `sparql` run 1: counts: expected no, got yes
- `sparql` run 2: no structured answer
- `sparql` run 3: counts: expected no, got yes
- `sparql` run 4: counts: expected no, got depends

**Q27.** Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: institution: expected I12, got None; citing_works: expected 3, got None

**Q28.** How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?

- `sparql` run 2: no structured answer
- `sparql+ontology` run 3: count: expected 1, got None

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `sparql` run 2: no structured answer
- `sparql` run 3: author: expected 2, got 3; institution: expected 2, got 3
- `sparql+ontology` run 3: author: expected 2, got None; institution: expected 2, got None; country: expected 4, got None

**Q30.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?

- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 3, got 4
- `sparql+ontology` run 3: count: expected 3, got None

**Q31.** Which works cite at least one of the works that cite W01?

- `sql` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sql` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sql` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sql` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sql` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sparql` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sparql` run 2: no structured answer
- `sparql` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sparql` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sparql` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sparql+ontology` run 3: works: expected ['W50', 'W51', 'W52'], got None

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `sql` run 1: count: expected 5, got 6
- `sql` run 2: count: expected 5, got 6
- `sql` run 3: count: expected 5, got 6
- `sql` run 4: count: expected 5, got 6
- `sql` run 5: count: expected 5, got 6
- `sparql` run 1: count: expected 5, got 6
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 5, got 6
- `sparql` run 4: count: expected 5, got 6
- `sparql` run 5: count: expected 5, got 6
- `sparql+ontology` run 3: count: expected 5, got None

**Q33.** Which of Kesting University's research works has the most citations?

- `sql` run 1: work: expected W20, got W22
- `sql` run 5: work: expected W20, got W22
- `sparql` run 1: work: expected W20, got W22
- `sparql` run 2: no structured answer
- `sparql` run 3: work: expected W20, got W22
- `sparql` run 4: work: expected W20, got W22
- `sparql` run 5: work: expected W20, got W22
- `sparql+ontology` run 3: work: expected W20, got None

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `sql` run 1: count: expected 3, got 5
- `sql` run 2: count: expected 3, got 2
- `sql` run 3: count: expected 3, got 2
- `sql` run 4: count: expected 3, got 2
- `sql` run 5: count: expected 3, got 5
- `sparql` run 1: count: expected 3, got 5
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 3, got 5
- `sparql` run 4: count: expected 3, got 5
- `sparql` run 5: count: expected 3, got 5
- `sparql+ontology` run 3: count: expected 3, got None

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `sql` run 1: count: expected 2, got 1
- `sql` run 2: count: expected 2, got 1
- `sql` run 3: count: expected 2, got 1
- `sql` run 4: count: expected 2, got 1
- `sql` run 5: count: expected 2, got 1
- `sparql` run 1: count: expected 2, got 1
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 2, got 4
- `sparql` run 4: count: expected 2, got 1
- `sparql` run 5: count: expected 2, got 1
- `sparql+ontology` run 3: count: expected 2, got None

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `sql` run 1: count: expected 2, got 0
- `sql` run 2: count: expected 2, got 0
- `sql` run 3: count: expected 2, got 0
- `sql` run 4: count: expected 2, got 0
- `sql` run 5: count: expected 2, got 0
- `sparql` run 1: count: expected 2, got 0
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 2, got 0
- `sparql` run 4: count: expected 2, got 0
- `sparql` run 5: count: expected 2, got 0
- `sparql+ontology` run 3: count: expected 2, got None

**Q37.** Which institution is W70 credited to?

- `sql` run 1: institution: expected I06, got I04
- `sql` run 2: institution: expected I06, got I04
- `sql` run 3: institution: expected I06, got I04
- `sql` run 4: institution: expected I06, got I04
- `sql` run 5: institution: expected I06, got I04
- `sparql` run 1: institution: expected I06, got I04
- `sparql` run 2: no structured answer
- `sparql` run 3: institution: expected I06, got I02
- `sparql` run 4: institution: expected I06, got I04
- `sparql` run 5: institution: expected I06, got I04
- `sparql+ontology` run 3: institution: expected I06, got None

**Q38.** Which institutions is W71 credited to, at every level?

- `sql` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sql` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `sql` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sql` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sql` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sparql` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I03', 'I02', 'I01', 'I06']
- `sparql` run 2: no structured answer
- `sparql` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `sparql` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `sparql` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `sparql+ontology` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got None

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `sql` run 1: count: expected 3, got 4
- `sql` run 2: count: expected 3, got 4
- `sql` run 3: count: expected 3, got 4
- `sql` run 4: count: expected 3, got 4
- `sql` run 5: count: expected 3, got 4
- `sparql` run 1: count: expected 3, got 4
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 3, got 4
- `sparql` run 4: count: expected 3, got 4
- `sparql` run 5: count: expected 3, got 4
- `sparql+ontology` run 3: count: expected 3, got None

**Q40.** Which source is in the highest tier?

- `sparql` run 2: no structured answer

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `sql` run 3: higher: expected no, got depends
- `sql` run 4: higher: expected no, got depends
- `sparql` run 2: no structured answer

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `sql` run 1: count: expected 0, got 2
- `sql` run 2: count: expected 0, got 2
- `sql` run 3: count: expected 0, got 2
- `sql` run 4: count: expected 0, got 2
- `sql` run 5: count: expected 0, got 2
- `sparql` run 1: count: expected 0, got 2
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 0, got 2
- `sparql` run 4: count: expected 0, got 2
- `sparql` run 5: count: expected 0, got 2
- `sparql+ontology` run 3: count: expected 0, got None

**Q43.** Is W07 research output?

- `sql` run 1: research: expected no, got yes
- `sql` run 2: research: expected no, got yes
- `sql` run 3: research: expected no, got yes
- `sql` run 4: research: expected no, got yes
- `sql` run 5: research: expected no, got yes
- `sparql` run 1: research: expected no, got yes
- `sparql` run 2: no structured answer
- `sparql` run 3: research: expected no, got yes
- `sparql` run 4: research: expected no, got yes
- `sparql` run 5: research: expected no, got yes

**Q44.** Which institutions are part of the Albury University System, at any level below it?

- `sql` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sql` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sql` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sql` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sql` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sparql` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sparql` run 2: no structured answer
- `sparql` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sparql` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `sparql` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']

**Q45.** How many research works is the Halloran Institute for Coastal Studies (I06) credited with?

- `sql` run 1: count: expected 3, got 4
- `sql` run 2: count: expected 3, got 4
- `sql` run 3: count: expected 3, got 4
- `sql` run 4: count: expected 3, got 4
- `sql` run 5: count: expected 3, got 4
- `sparql` run 1: count: expected 3, got 4
- `sparql` run 2: no structured answer
- `sparql` run 3: count: expected 3, got 4
- `sparql` run 4: count: expected 3, got 4
- `sparql` run 5: count: expected 3, got 4
- `sparql+ontology` run 3: count: expected 3, got None

**Q46.** What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?

- `sql` run 1: parent: expected I06, got I01
- `sql` run 2: parent: expected I06, got I01
- `sql` run 3: parent: expected I06, got I01
- `sql` run 4: parent: expected I06, got I01
- `sql` run 5: parent: expected I06, got I01
- `sql+executed` run 1: parent: expected I06, got I01
- `sql+executed` run 3: parent: expected I06, got I01
- `sparql` run 1: parent: expected I06, got I01
- `sparql` run 2: no structured answer
- `sparql` run 3: parent: expected I06, got I01
- `sparql` run 4: parent: expected I06, got I01
- `sparql` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `sql` run 1: Gets Kesting's larger shares (sole-authored W22, shared W20/W21) but omits that each Rostval work has four authors with one from Rostval, i.e. a quarter each, and does not say Kesting holds half of W20 and W21.
- `sql` run 2: Gets Rostval's one-author-per-paper point and Kesting's larger shares, but never says each paper has four authors (a quarter each) or that W20/W21 are half shares for Kesting.
- `sql` run 3: Captures that Rostval's works are shared among 4 authors (fractional 1.0) and Kesting has fewer co-authors, but doesn't say only one author per work is from Rostval (a quarter each) or identify Kesting's single-author W22 and half-shares of W20 and W21.
- `sql` run 4: Gets Kesting's larger shares (W22 whole, half of W20 and W21) right, but never says Rostval's works each have four authors with one from Rostval, so a quarter each.
- `sql` run 5: Gets Rostval's four works with a quarter each (four authors, one from Rostval), but for Kesting it only says W22 is single-author and that W20 and W21 'split credit less', not that Kesting holds half of W20 and W21.
- `sql+markdown` run 1: Gets Kesting's larger shares (W22=1, W20=0.5) but doesn't say Rostval's works each have four authors with one from Rostval; says 'spread across several institutions' and omits W21 and the four-author detail.
- `sql+markdown` run 2: Gives Kesting's larger shares (W22 solely Kesting's, W20 and W21 split), but never says Rostval's four works each have four authors with one from Rostval, a quarter each.
- `sql+markdown` run 3: Gives the four-author, one-from-Rostval fractional effect but omits Kesting's larger shares (single-author W22 and half of W20/W21).
- `sql+markdown` run 4: Correctly says Rostval's four works have four authors each, 0.25 each, but doesn't mention only one author being from Rostval, and omits Kesting's half shares of W20 and W21 (cites only W22).
- `sql+markdown` run 5: Gives the general idea of shared authorship cutting Rostval's share, but omits the four-authors/one-from-Rostval quarter-each detail and Kesting's W22 single-author review plus half of W20 and W21.
- `sql+executed` run 1: Says Kesting holds larger shares, but omits Rostval's four-author works giving a quarter each and Kesting's specific W22 single-author and half-shares of W20/W21.
- `sql+executed` run 2: Correctly says Rostval is one of four authors on each work, so its share is lower, and Kesting's shares are larger; but it omits the quarter-each figure and does not name Kesting's single-author review (W22) or its half shares of W20 and W21.
- `sql+executed` run 3: Denies the swap, which contradicts the key. It never mentions Rostval's four-author works at a quarter each, nor Kesting's W22 and half-shares of W20 and W21.
- `sql+executed` run 4: Says Rostval's four works are split four ways (1.0) and Kesting has W22 sole-authored plus half of W20, but omits that only one author per work is from Rostval and does not mention half of W21 explicitly.
- `sql+executed` run 5: Says Rostval's works are shared among 4 authors (quarter each) and Kesting has W22 sole and half of W20, but omits half of W21 and doesn't explicitly say only one of the four authors is from Rostval.
- `sparql` run 1: Gets Kesting's larger shares (single-author W22, A09 and A10 both Kesting) but never says Rostval's works have four authors with one from Rostval, so a quarter each; it only says 'many are co-authored'.
- `sparql` run 2: No answer was given, so neither checklist point is met
- `sparql` run 3: Correctly says Kesting holds W22 wholly and half of W20 and W21, but misses that each Rostval work has four authors with one from Rostval (a quarter each); only 'shares most' is vague.
- `sparql` run 4: Correctly says Rostval's works are shared among four authors at different institutions, but doesn't state one author each from Rostval giving a quarter share, and it misattributes Kesting's lead (omits the single-author review W22 and half shares of W20 and W21, claiming only 'more authors at Kesting').
- `sparql` run 5: Gives Kesting's larger share but omits the four-authors/quarter-each detail and the W22/W20/W21 breakdown; the 'one of four' is stated but not the quarter share
- `sparql+ontology` run 3: No answer given; meets none of the checklist points
- `sparql+ontology` run 5: Gets Rostval's quarter shares, but omits Kesting's specifics (single-author W22, half of W20 and W21), saying only 'larger author shares'.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `sql` run 1: Contradicts the key: only the last-listed affiliation counts, so W70 is credited to the Halloran Institute, an affiliated institute that does not roll up to the University of Albury; the answer claims W70 is Albury's.
- `sql` run 2: Contradicts the key: W70 is credited to the Halloran Institute (last-listed affiliation), an affiliated institute that doesn't roll up to Albury; the answer claims it does.
- `sql` run 3: Rejects the premise and says W70 counts for Albury, contradicting the key: only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `sql` run 4: Contradicts the key: it says W70 does count for Albury, but the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, which is affiliated and not a unit, so it doesn't roll up to Albury.
- `sql` run 5: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, so it goes to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `sql+markdown` run 3: Says only the last affiliation (I06) counts and that it is an affiliated institute giving no credit to Albury, but does not explicitly name the Halloran Institute, though I06 is implied; the 'affiliated institute, not a unit' point is met.
- `sql+markdown` run 5: Says the last-listed affiliation I06 is credited and that it is an affiliated institute, not a unit of I02, but never names it as the Halloran Institute; it does cover both checklist points in substance, though the answer is stated only in IDs.
- `sql+executed` run 1: Says W70 is credited only to the Halloran Institute, an affiliate that doesn't roll up to Albury, but doesn't state the last-listed-affiliation rule.
- `sql+executed` run 2: Says W70 is credited to the Halloran Institute and that it is an affiliated institution not rolling up to Albury; but it does not state the rule that only the last-listed affiliation counts.
- `sql+executed` run 3: Correctly says Halloran is an affiliated institution that doesn't roll up to Albury. It never states the rule that only the last-listed affiliation counts.
- `sql+executed` run 4: Says W70 is credited to Halloran Institute, an affiliate not counting to the University of Albury, but does not state that only the last-listed affiliation counts, nor that Halloran is an affiliated institute rather than a unit.
- `sql+executed` run 5: Says W70 is credited to Halloran Institute (I06) and that it is affiliated and counts only for itself, but doesn't state the rule that only the last-listed affiliation counts, and doesn't say explicitly that the Tessel Laboratory is not credited because of that rule.
- `sparql` run 1: Rejects the premise and counts W70 for Albury, contradicting the key: only the last-listed affiliation counts (Halloran Institute), and an affiliated institute does not roll up to Albury.
- `sparql` run 2: No answer was given, so neither checklist point is met
- `sparql` run 3: Rejects the premise; the key says only the last-listed affiliation counts, crediting W70 to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `sparql` run 4: Rejects the premise; the key says W70 is credited only to the last-listed affiliation (Halloran Institute), an affiliated institute that does not roll up to the University of Albury.
- `sparql` run 5: Claims W70 is a University of Albury work, contradicting the key (last-listed affiliation counts, Halloran is an affiliated institute that doesn't roll up)
- `sparql+ontology` run 3: No answer given; meets none of the checklist points

