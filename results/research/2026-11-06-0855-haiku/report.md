# research: claude:haiku, 2026-11-06 08:55

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv+axioms` | **97%** | 92% to 100% | 4 of 48 |
| `csv+axioms+markdown` | **98%** | 94% to 100% | 1 of 48 |

## Against `csv+axioms`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `csv+axioms+markdown` | +1 points | -1 to +4 |

## By question

| Question | Graded by | `csv+axioms` | `csv+axioms+markdown` |
|---|---|---|---|
| Q1 | code | ✅ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ❌ |
| Q2 | code | ✅ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | llm | ✅ 🟡 ✅ 🟡 ✅ | 🟡 🟡 🟡 🟡 🟡 |
| Q48 | llm | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv+axioms` | 93% | 98% |
| `csv+axioms+markdown` | 100% | 100% |

**The checklist grader agreed with itself** on 16 of 20 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv+axioms` run 2: count: expected 2, got 1
- `csv+axioms` run 3: count: expected 2, got 1
- `csv+axioms` run 4: count: expected 2, got 1
- `csv+axioms` run 5: count: expected 2, got 1
- `csv+axioms+markdown` run 2: count: expected 2, got 1
- `csv+axioms+markdown` run 3: count: expected 2, got 1
- `csv+axioms+markdown` run 5: count: expected 2, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `csv+axioms` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv+axioms` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `csv+axioms` run 5: full: expected 7, got 8; fractional: expected 6, got 7.0

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv+axioms` run 2: Correctly says Rostval's works have four authors so each gets 1/4, but omits that Kesting holds larger shares via single-author W22 and half of W20 and W21 (mentions W20 two authors and W22 one, but not W21 or half-shares explicitly).
- `csv+axioms` run 4: Covers Rostval's four works with four authors each and 0.25 share, and mentions W22 single-authored, but omits that Kesting holds half of W20 and W21.
- `csv+axioms+markdown` run 1: Gives Kesting's larger share via W22 single author, but says Rostval's works have four authors each without stating only one is from Rostval (a quarter each), and omits Kesting's half shares of W20 and W21.
- `csv+axioms+markdown` run 2: Covers Rostval's 0.25 shares and Kesting's single-author W22, but omits Kesting's half shares of W20 and W21.
- `csv+axioms+markdown` run 3: Gives Rostval's quarter shares (1/4 on four-author works) and Kesting's single-author W22 plus W20 shares, but doesn't say all four Rostval works have four authors with one Rostval author, and says W20 has 2 authors without mentioning W21's half share.
- `csv+axioms+markdown` run 4: Gives Rostval's quarter shares and Kesting's single-author W22, but never says Kesting holds half of W20 and W21.
- `csv+axioms+markdown` run 5: Covers Rostval's quarter shares (four authors, one from Rostval) but says Kesting's 2.0 comes from W22 and W20 as two-author work; omits W21 half share and doesn't explain W22 as a single-author review with halves of W20 and W21 as stated in the checklist

