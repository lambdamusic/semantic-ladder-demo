# research_850: claude:sonnet, 2026-11-06 08:55

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `sparql+axioms` | **91%** | 85% to 96% | 13 of 48 |

## By question

| Question | Graded by | `sparql+axioms` |
|---|---|---|
| Q1 | code | ❌ ❌ ❌ ❌ ❌ |
| Q2 | code | ✅ ✅ ✅ ✅ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ✅ ❌ |
| Q7 | code | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | 🟡 ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ❌ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ❌ ✅ ✅ ✅ ❌ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | 🟡 ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ✅ ✅ ❌ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | 🟡 ✅ ✅ ✅ ✅ |
| Q30 | code | ❌ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ❌ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ |
| Q47 | llm | ❌ 🟡 ❌ ✅ ✅ |
| Q48 | llm | ❌ 🟡 🟡 🟡 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `sparql+axioms` | 93% | 100% |

**The checklist grader agreed with itself** on 9 of 10 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `sparql+axioms` run 1: count: expected 3, got 1
- `sparql+axioms` run 2: count: expected 3, got 1
- `sparql+axioms` run 3: count: expected 3, got 1
- `sparql+axioms` run 4: count: expected 3, got 1
- `sparql+axioms` run 5: count: expected 3, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `sparql+axioms` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W1005', 'W1048', 'W1050', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W612', 'W663', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984'], got ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19', 'W206', 'W238', 'W271', 'W374', 'W449', 'W464', 'W555', 'W676', 'W763', 'W813', 'W817', 'W843', 'W869', 'W905', 'W936', 'W949', 'W972', 'W984', 'W1005', 'W1048', 'W1050']

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `sparql+axioms` run 5: author: expected A01, got A07

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `sparql+axioms` run 1: fractional: expected 11, got None

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `sparql+axioms` run 1: full: expected 46, got None; fractional: expected 42, got None

**Q19.** How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?

- `sparql+axioms` run 1: count: expected 27, got 30
- `sparql+axioms` run 5: count: expected 27, got 30

**Q23.** How many citations has W30 received in total, and how many within its publication year and the two years after?

- `sparql+axioms` run 1: total: expected 16, got 18

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `sparql+axioms` run 3: count: expected 20, got 19

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `sparql+axioms` run 1: institution: expected 10, got 11; country: expected 20, got 21

**Q30.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?

- `sparql+axioms` run 1: count: expected 14, got 15

**Q31.** Which works cite at least one of the works that cite W01?

- `sparql+axioms` run 5: works: expected ['W1042', 'W337', 'W338', 'W396', 'W50', 'W51', 'W52', 'W546', 'W682', 'W801', 'W895'], got ['W50', 'W51', 'W52', 'W337', 'W338', 'W396', 'W546', 'W682', 'W801', 'W1042']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `sparql+axioms` run 1: count: expected 19, got None

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `sparql+axioms` run 1: No answer given; meets none of the checklist points
- `sparql+axioms` run 2: Gives the co-author dilution for I09 (Rostval) but doesn't say Rostval gets only one author's share, and omits Kesting's larger shares (sole or few co-authors); also admits not querying it.
- `sparql+axioms` run 3: Explicitly unanswered; gives only generic counting definitions, none of the checklist points about Rostval's small shares or Kesting's larger shares.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `sparql+axioms` run 1: No answer given; meets none of the checklist points
- `sparql+axioms` run 2: Says I06 is not a unit of I02 so crediting it doesn't credit I02, but omits that only the last-listed affiliation counts.
- `sparql+axioms` run 3: Says W70 is credited only to I06, an affiliated institute whose works don't go to the parent (second point), but omits that only the last-listed affiliation counts.
- `sparql+axioms` run 4: Says the work is credited to I06 only, which counts only toward itself and not toward the University of Albury. It never states the last-listed-affiliation rule, and it doesn't say outright that the Halloran Institute is an affiliated institute rather than a unit.
- `sparql+axioms` run 5: Says I06 doesn't count toward I02, but never gives the rule that only the last-listed affiliation counts, and doesn't say Halloran is an affiliated institute rather than a unit.

