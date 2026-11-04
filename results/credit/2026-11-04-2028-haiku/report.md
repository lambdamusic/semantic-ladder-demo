# credit: claude:haiku, 2026-11-04 20:28

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **78%** | 67% to 88% | 6 of 48 |
| `csv+ontology` | **99%** | 96% to 100% | 1 of 48 |
| `csv+markdown` | **99%** | 96% to 100% | 3 of 48 |
| `csv+axioms` | **100%** | 99% to 100% | 1 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `csv+ontology` | +21 points | +10 to +32 |
| `csv+markdown` | +20 points | +10 to +32 |
| `csv+axioms` | +22 points | +11 to +33 |

## By question

| Question | Graded by | `csv` | `csv+ontology` | `csv+markdown` | `csv+axioms` |
|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ 🟡 | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | ✅ ✅ ✅ 🟡 ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ 🟡 ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ❌ ✅ | ✅ ✅ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ✅ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q48 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |

## Lists, with partial credit

The 7 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 86% | 97% |
| `csv+ontology` | 100% | 100% |
| `csv+markdown` | 97% | 99% |
| `csv+axioms` | 100% | 100% |

**The checklist grader agreed with itself** on 19 of 20 answers graded twice.

## Why each miss was marked

**Q3.** Is Kestrel Energy's 2031 note investment grade?

- `csv+markdown` run 5: rating: expected BB+, got None

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `csv` run 4: Links FC rating to the BB country ceiling as consistent cause but hedges and disclaims it, and never states that the ceiling caps foreign-currency but not local-currency ratings.
- `csv+axioms` run 2: Names the BB ceiling as capping the foreign-currency rating, but never says local-currency ratings are not capped (the ceiling's scope is left implicit).

**Q7.** Which issuers were downgraded in 2026?

- `csv` run 1: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 2: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 3: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 4: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']
- `csv` run 5: issuers: expected ['E08', 'E10'], got ['E08', 'E10', 'E16']

**Q9.** As of 1 October 2026, how many distinct issuers hold an issuer rating?

- `csv` run 1: count: expected 12, got 13
- `csv` run 2: count: expected 12, got 13
- `csv` run 5: count: expected 12, got 13

**Q10.** Is Valdoria Telecom investment grade?

- `csv+ontology` run 1: investment_grade: expected depends, got no
- `csv+ontology` run 2: investment_grade: expected depends, got no
- `csv+ontology` run 4: investment_grade: expected depends, got no
- `csv+markdown` run 3: investment_grade: expected depends, got no
- `csv+markdown` run 4: investment_grade: expected depends, got no

**Q25.** How many instruments held an investment-grade rating on 1 October 2026?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6

**Q30.** Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?

- `csv+markdown` run 4: entities: expected ['E05', 'E15'], got ['E05']

**Q37.** How many distinct legal entities does the data describe?

- `csv` run 1: count: expected 16, got 17
- `csv` run 2: count: expected 16, got 17
- `csv` run 3: count: expected 16, got 17
- `csv` run 4: count: expected 16, got 17
- `csv` run 5: count: expected 16, got 17

**Q40.** How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6

**Q41.** What is Brindle Capital's current rating?

- `csv` run 1: rating: expected none, got BB+
- `csv` run 2: rating: expected none, got BB+
- `csv` run 3: rating: expected none, got BB+
- `csv` run 4: rating: expected none, got BB+
- `csv` run 5: rating: expected none, got BB+

**Q42.** In which country is Halden Bank domiciled?

- `csv` run 1: country: expected LU, got DE
- `csv` run 2: country: expected LU, got DE
- `csv` run 3: country: expected LU, got DE
- `csv` run 4: country: expected LU, got DE
- `csv` run 5: country: expected LU, got DE

**Q43.** How many distinct entities are domiciled in Luxembourg (LU)?

- `csv` run 1: count: expected 1, got 0
- `csv` run 2: count: expected 1, got 0
- `csv` run 5: count: expected 1, got 0

**Q44.** Is Valdoria Telecom's 2027 note a local-currency obligation?

- `csv` run 1: local_currency: expected yes, got depends

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `csv` run 1: above_ceiling: expected no, got depends
- `csv` run 3: above_ceiling: expected no, got depends
- `csv` run 4: above_ceiling: expected no, got yes
- `csv` run 5: above_ceiling: expected no, got yes

**Q46.** Does Halden Leasing have an issuer rating?

- `csv` run 4: issuer_rating: expected no, got depends

**Q47.** How is Corvenia Power's 2034 note rated?

- `csv` run 1: rating: expected none, got A
- `csv` run 2: rating: expected none, got A
- `csv` run 3: rating: expected none, got A
- `csv` run 4: rating: expected none, got A
- `csv` run 5: rating: expected none, got A

**Q48.** How many instruments held a rating on 1 October 2026?

- `csv` run 1: count: expected 7, got 8
- `csv` run 2: count: expected 7, got 8
- `csv` run 3: count: expected 7, got 8
- `csv` run 4: count: expected 7, got 8
- `csv` run 5: count: expected 7, got 8

