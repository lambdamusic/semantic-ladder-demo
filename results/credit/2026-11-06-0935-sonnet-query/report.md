# credit: claude:sonnet, 2026-11-06 09:35

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `sql` | **84%** | 73% to 93% | 4 of 48 |
| `sql+markdown` | **100%** | 99% to 100% | 1 of 48 |
| `sparql` | **82%** | 71% to 91% | 5 of 48 |
| `sparql+ontology` | **100%** | 100% to 100% | 0 of 48 |
| `sql+executed` | **99%** | 98% to 100% | 1 of 48 |
| `sparql+axioms` | **90%** | 81% to 98% | 3 of 48 |

## Against `sql`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `sql+markdown` | +16 points | +7 to +27 |
| `sparql` | -2 points | -4 to +0 |
| `sparql+ontology` | +16 points | +7 to +27 |
| `sql+executed` | +16 points | +6 to +27 |
| `sparql+axioms` | +6 points | +2 to +13 |

## By question

| Question | Graded by | `sql` | `sql+markdown` | `sparql` | `sparql+ontology` | `sql+executed` | `sparql+axioms` |
|---|---|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | 🟡 ✅ ✅ 🟡 ✅ | 🟡 ✅ ✅ ✅ ✅ | 🟡 🟡 🟡 🟡 🟡 | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 🟡 ✅ 🟡 | 🟡 ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ✅ ❌ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q48 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |

## Lists, with partial credit

The 7 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `sql` | 86% | 97% |
| `sql+markdown` | 100% | 100% |
| `sparql` | 86% | 97% |
| `sparql+ontology` | 100% | 100% |
| `sql+executed` | 100% | 100% |
| `sparql+axioms` | 86% | 97% |

**The checklist grader agreed with itself** on 30 of 30 answers graded twice.

## Why each miss was marked

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `sql` run 1: Names the BB Country Ceiling as the likely cause but does not say it caps foreign-currency (not local-currency) ratings, and hedges that the reason isn't stated.
- `sql` run 4: Names the BB Country Ceiling as the cap on foreign-currency rating, but never says the ceiling applies only to foreign-currency and not local-currency ratings.
- `sql+markdown` run 1: Names the BB Country Ceiling as the cap on the FC rating, but never states that it applies only to foreign-currency ratings and not local-currency ones (only implied by the LC rating being higher).
- `sparql` run 1: It names the BB Country Ceiling and shows FC equals it while LC is higher, but it hedges that the data states no reason instead of asserting the ceiling as the cause, and it never explicitly says the ceiling caps FC and not LC.
- `sparql` run 2: Identifies the BB country ceiling matching the FC rating as the likely cause, but hedges as unconfirmed and never states that the ceiling caps foreign-currency ratings and not local-currency ones.
- `sparql` run 3: Names the BB Country Ceiling as the cause, but never says the ceiling caps foreign-currency ratings and not local-currency ones; it only notes the FC rating matches the ceiling.
- `sparql` run 4: Mentions the BB Country Ceiling alongside the FC rating of BB but states no reason and doesn't say the ceiling caps FC and not LC ratings, so it never names the ceiling as the cause.
- `sparql` run 5: Names the BB country ceiling as the likely cause, but never says the ceiling caps foreign-currency ratings and not local-currency ones.
- `sql+executed` run 2: Names the BB Country Ceiling and links it to the FC rating being capped, but hedges ('consistent with') and never states that the ceiling applies to foreign-currency and not local-currency ratings.
- `sql+executed` run 3: Names the BB Country Ceiling as consistent with the gap, but hedges that the data states no reason and never says the ceiling caps foreign-currency ratings and not local-currency ones.
- `sql+executed` run 5: Names the BB Country Ceiling as the likely cause, but never states that it caps foreign-currency ratings and not local-currency ones, and hedges that the cause isn't explicit.
- `sparql+axioms` run 1: Identifies the BB Country Ceiling as matching the foreign-currency rating and implies a cap, but hedges and never says the ceiling applies to foreign-currency and not local-currency ratings.

**Q7.** Which issuers were downgraded in 2026?

- `sql` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sql` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sql` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sql` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sql` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql+axioms` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql+axioms` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql+axioms` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql+axioms` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `sparql+axioms` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']

**Q9.** As of 1 October 2026, how many distinct issuers hold an issuer rating?

- `sql` run 1: count: expected 12, got 13
- `sql` run 2: count: expected 12, got 13
- `sql` run 3: count: expected 12, got 13
- `sql` run 4: count: expected 12, got 13
- `sql` run 5: count: expected 12, got 13
- `sparql` run 1: count: expected 12, got 13
- `sparql` run 2: count: expected 12, got 13
- `sparql` run 3: count: expected 12, got 13
- `sparql` run 4: count: expected 12, got 13
- `sparql` run 5: count: expected 12, got 13
- `sparql+axioms` run 1: count: expected 12, got 13
- `sparql+axioms` run 2: count: expected 12, got 13
- `sparql+axioms` run 3: count: expected 12, got 13
- `sparql+axioms` run 5: count: expected 12, got 13

**Q25.** How many instruments held an investment-grade rating on 1 October 2026?

- `sql` run 1: count: expected 5, got 6
- `sparql` run 4: count: expected 5, got 6
- `sparql` run 5: count: expected 5, got 6

**Q37.** How many distinct legal entities does the data describe?

- `sql` run 1: count: expected 16, got 17
- `sql` run 2: count: expected 16, got 17
- `sql` run 3: count: expected 16, got 17
- `sql` run 4: count: expected 16, got 17
- `sql` run 5: count: expected 16, got 17
- `sparql` run 1: count: expected 16, got 17
- `sparql` run 2: count: expected 16, got 17
- `sparql` run 3: count: expected 16, got 17
- `sparql` run 4: count: expected 16, got 17
- `sparql` run 5: count: expected 16, got 17
- `sparql+axioms` run 1: count: expected 16, got 17
- `sparql+axioms` run 2: count: expected 16, got 17
- `sparql+axioms` run 3: count: expected 16, got 18
- `sparql+axioms` run 4: count: expected 16, got 17
- `sparql+axioms` run 5: count: expected 16, got 17

**Q40.** How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?

- `sql` run 1: count: expected 5, got 6
- `sql` run 2: count: expected 5, got 6
- `sql` run 3: count: expected 5, got 6
- `sql` run 4: count: expected 5, got 6
- `sql` run 5: count: expected 5, got 6
- `sparql` run 1: count: expected 5, got 6
- `sparql` run 2: count: expected 5, got 6
- `sparql` run 3: count: expected 5, got 6
- `sparql` run 4: count: expected 5, got 6
- `sparql` run 5: count: expected 5, got 6
- `sparql+axioms` run 1: count: expected 5, got 6
- `sparql+axioms` run 2: count: expected 5, got 6
- `sparql+axioms` run 3: count: expected 5, got 6
- `sparql+axioms` run 5: count: expected 5, got 6

**Q41.** What is Brindle Capital's current rating?

- `sql` run 1: rating: expected none, got BB+
- `sql` run 2: rating: expected none, got BB+
- `sql` run 3: rating: expected none, got BB+
- `sql` run 4: rating: expected none, got BB+
- `sql` run 5: rating: expected none, got BB+
- `sparql` run 1: rating: expected none, got BB+
- `sparql` run 2: rating: expected none, got BB+
- `sparql` run 3: rating: expected none, got BB+
- `sparql` run 4: rating: expected none, got BB+
- `sparql` run 5: rating: expected none, got BB+
- `sparql+axioms` run 1: rating: expected none, got BB+
- `sparql+axioms` run 2: rating: expected none, got BB+
- `sparql+axioms` run 3: rating: expected none, got BB+
- `sparql+axioms` run 4: rating: expected none, got BB+
- `sparql+axioms` run 5: rating: expected none, got BB+

**Q42.** In which country is Halden Bank domiciled?

- `sql` run 1: country: expected LU, got DE
- `sql` run 2: country: expected LU, got DE
- `sql` run 3: country: expected LU, got DE
- `sql` run 4: country: expected LU, got DE
- `sql` run 5: country: expected LU, got DE
- `sparql` run 1: country: expected LU, got DE
- `sparql` run 2: country: expected LU, got DE
- `sparql` run 3: country: expected LU, got DE
- `sparql` run 4: country: expected LU, got DE
- `sparql` run 5: country: expected LU, got DE

**Q43.** How many distinct entities are domiciled in Luxembourg (LU)?

- `sql` run 1: count: expected 1, got 0
- `sql` run 2: count: expected 1, got 0
- `sql` run 3: count: expected 1, got 0
- `sql` run 4: count: expected 1, got 0
- `sql` run 5: count: expected 1, got 0
- `sparql` run 1: count: expected 1, got 0
- `sparql` run 3: count: expected 1, got 0
- `sparql` run 4: count: expected 1, got 0
- `sparql` run 5: count: expected 1, got 0

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `sparql` run 1: above_ceiling: expected no, got yes

**Q47.** How is Corvenia Power's 2034 note rated?

- `sql` run 1: rating: expected none, got A
- `sparql` run 4: rating: expected none, got A
- `sparql` run 5: rating: expected none, got A

**Q48.** How many instruments held a rating on 1 October 2026?

- `sql` run 1: count: expected 7, got 8
- `sparql` run 4: count: expected 7, got 8
- `sparql` run 5: count: expected 7, got 8

