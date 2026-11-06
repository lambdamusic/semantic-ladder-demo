# research: claude:sonnet, 2026-11-06 11:27

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `sparql+axioms` | **72%** | 68% to 77% | 48 of 48 |

## By question

| Question | Graded by | `sparql+axioms` |
|---|---|---|
| Q1 | code | ❌ ❌ ✅ ❌ ❌ |
| Q2 | code | ✅ ✅ ✅ ✅ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ❌ |
| Q4 | code | ✅ ✅ ✅ ✅ ❌ |
| Q5 | code | ✅ ✅ ✅ ✅ ❌ |
| Q6 | code | ✅ ✅ ✅ ✅ ❌ |
| Q7 | code | ✅ ✅ ✅ ✅ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ❌ |
| Q9 | code | ✅ ✅ ✅ ✅ ❌ |
| Q10 | code | ✅ ✅ ✅ ✅ ❌ |
| Q11 | code | ✅ ✅ ✅ ✅ ❌ |
| Q12 | code | ✅ 🟡 ✅ ✅ ❌ |
| Q13 | code | ✅ ✅ ✅ ✅ ❌ |
| Q14 | code | ✅ ✅ ✅ ✅ ❌ |
| Q15 | code | ✅ ✅ ✅ ✅ ❌ |
| Q16 | code | ✅ ✅ ✅ ✅ ❌ |
| Q17 | code | ✅ ✅ ✅ ✅ ❌ |
| Q18 | code | ✅ ✅ ✅ ✅ ❌ |
| Q19 | code | ✅ ✅ ✅ ✅ ❌ |
| Q20 | code | ✅ ✅ ✅ ✅ ❌ |
| Q21 | code | ✅ ✅ ✅ ✅ ❌ |
| Q22 | code | ✅ ✅ ✅ ✅ ❌ |
| Q23 | code | ✅ ✅ ✅ ✅ ❌ |
| Q24 | code | ✅ ✅ ✅ ✅ ❌ |
| Q25 | code | ✅ ✅ ✅ ❌ ❌ |
| Q26 | code | ✅ ✅ ✅ ✅ ❌ |
| Q27 | code | ✅ ✅ ✅ ✅ ❌ |
| Q28 | code | ✅ ✅ ✅ ✅ ❌ |
| Q29 | code | ✅ ✅ ✅ ✅ ❌ |
| Q30 | code | ✅ ✅ ✅ ✅ ❌ |
| Q31 | code | ✅ ✅ ✅ ❌ ❌ |
| Q32 | code | ✅ ✅ ✅ ❌ ❌ |
| Q33 | code | ✅ ✅ ✅ ❌ ❌ |
| Q34 | code | ✅ ✅ ✅ ✅ ❌ |
| Q35 | code | ✅ ✅ ✅ ✅ ❌ |
| Q36 | code | ✅ ✅ ✅ ✅ ❌ |
| Q37 | code | ✅ ✅ ✅ ✅ ❌ |
| Q38 | code | ✅ ✅ ✅ ✅ ❌ |
| Q39 | code | ✅ ❌ ✅ ❌ ❌ |
| Q40 | code | ✅ ❌ ✅ ❌ ❌ |
| Q41 | code | ✅ ❌ ✅ ❌ ❌ |
| Q42 | code | ✅ ✅ ✅ ✅ ❌ |
| Q43 | code | ✅ ✅ ✅ ✅ ❌ |
| Q44 | code | ✅ ✅ ✅ ✅ ❌ |
| Q45 | code | ✅ ✅ ✅ ✅ ❌ |
| Q46 | code | ✅ ✅ ✅ ✅ ❌ |
| Q47 | llm | ❌ 🟡 🟡 🟡 ❌ |
| Q48 | llm | ❌ 🟡 🟡 🟡 ❌ |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `sparql+axioms` | 77% | 80% |

**The checklist grader agreed with itself** on 9 of 10 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `sparql+axioms` run 1: count: expected 2, got 1
- `sparql+axioms` run 2: count: expected 2, got 1
- `sparql+axioms` run 4: count: expected 2, got 1
- `sparql+axioms` run 5: no structured answer

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `sparql+axioms` run 5: no structured answer

**Q3.** Is the Jonas Brandt who wrote W37 the same person as the Jonas Brandt who wrote W38?

- `sparql+axioms` run 5: no structured answer

**Q4.** How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?

- `sparql+axioms` run 5: no structured answer

**Q5.** Is the M. Ellison who wrote W08 the same person as the Mara Ellison who wrote W01?

- `sparql+axioms` run 5: no structured answer

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `sparql+axioms` run 5: no structured answer

**Q7.** How many research works has Mara Ellison authored?

- `sparql+axioms` run 5: no structured answer

**Q8.** What is the ultimate parent of the Tessel Laboratory for Ocean Sensing (I04)?

- `sparql+axioms` run 5: no structured answer

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `sparql+axioms` run 5: no structured answer

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `sparql+axioms` run 5: no structured answer

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `sparql+axioms` run 5: no structured answer

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `sparql+axioms` run 2: fractional: expected 2, got 1.75
- `sparql+axioms` run 5: no structured answer

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `sparql+axioms` run 5: no structured answer

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `sparql+axioms` run 5: no structured answer

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `sparql+axioms` run 5: no structured answer

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `sparql+axioms` run 5: no structured answer

**Q17.** Which of Mara Ellison's works are not research output because of their document type?

- `sparql+axioms` run 5: no structured answer

**Q18.** How many distinct research works has Priya Ramanathan (A07) authored?

- `sparql+axioms` run 5: no structured answer

**Q19.** How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?

- `sparql+axioms` run 5: no structured answer

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `sparql+axioms` run 5: no structured answer

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `sparql+axioms` run 5: no structured answer

**Q22.** Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?

- `sparql+axioms` run 5: no structured answer

**Q23.** How many citations has W30 received in total, and how many within its publication year and the two years after?

- `sparql+axioms` run 5: no structured answer

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `sparql+axioms` run 5: no structured answer

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `sparql+axioms` run 4: count: expected 6, got 9
- `sparql+axioms` run 5: no structured answer

**Q26.** Does W23 count towards Kesting University's research output?

- `sparql+axioms` run 5: no structured answer

**Q27.** Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?

- `sparql+axioms` run 5: no structured answer

**Q28.** How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?

- `sparql+axioms` run 5: no structured answer

**Q29.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?

- `sparql+axioms` run 5: no structured answer

**Q30.** Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?

- `sparql+axioms` run 5: no structured answer

**Q31.** Which works cite at least one of the works that cite W01?

- `sparql+axioms` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `sparql+axioms` run 5: no structured answer

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `sparql+axioms` run 4: count: expected 5, got 6
- `sparql+axioms` run 5: no structured answer

**Q33.** Which of Kesting University's research works has the most citations?

- `sparql+axioms` run 4: work: expected W20, got W22
- `sparql+axioms` run 5: no structured answer

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `sparql+axioms` run 5: no structured answer

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `sparql+axioms` run 5: no structured answer

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `sparql+axioms` run 5: no structured answer

**Q37.** Which institution is W70 credited to?

- `sparql+axioms` run 5: no structured answer

**Q38.** Which institutions is W71 credited to, at every level?

- `sparql+axioms` run 5: no structured answer

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `sparql+axioms` run 2: count: expected 3, got 2
- `sparql+axioms` run 4: count: expected 3, got 2
- `sparql+axioms` run 5: no structured answer

**Q40.** Which source is in the highest tier?

- `sparql+axioms` run 2: source: expected S01, got S03
- `sparql+axioms` run 4: source: expected S01, got S03
- `sparql+axioms` run 5: no structured answer

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `sparql+axioms` run 2: higher: expected no, got yes
- `sparql+axioms` run 4: higher: expected no, got yes
- `sparql+axioms` run 5: no structured answer

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `sparql+axioms` run 5: no structured answer

**Q43.** Is W07 research output?

- `sparql+axioms` run 5: no structured answer

**Q44.** Which institutions are part of the Albury University System, at any level below it?

- `sparql+axioms` run 5: no structured answer

**Q45.** How many research works is the Halloran Institute for Coastal Studies (I06) credited with?

- `sparql+axioms` run 5: no structured answer

**Q46.** What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?

- `sparql+axioms` run 5: no structured answer

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `sparql+axioms` run 1: No answer given; meets none of the checklist points
- `sparql+axioms` run 2: Explains the swap and says I09 holds one of four authors per work, but uses IDs rather than names and omits that this makes each a quarter; also only vaguely notes I07's shares (sole on W22, half of W20 but not W21).
- `sparql+axioms` run 3: Gives Rostval's quarter-share per work (four authors, one from Rostval) but says only that Kesting holds W22 wholly and omits that it holds half of W20 and W21.
- `sparql+axioms` run 4: Correctly gives Rostval a quarter share per work, but doesn't identify Kesting's larger shares (single-author W22, half of W20 and W21); it gives only a vague 'shares them' and a total of 2.0 without the reason for the swap.
- `sparql+axioms` run 5: No answer given; meets none of the checklist points

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `sparql+axioms` run 1: No answer given; meets none of the checklist points
- `sparql+axioms` run 2: Says W70 is credited only to the affiliate I06 and that I06 is not a unit of I02, but never states that the last-listed affiliation is the one that counts.
- `sparql+axioms` run 3: Correctly says W70 is credited only to the Halloran Institute (I06) and that I06 does not count towards Albury, but doesn't state the 'last listed affiliation counts' rule or that Halloran is an affiliated institute rather than a unit.
- `sparql+axioms` run 4: Says W70 is credited only to I06 (the last-listed affiliation) and that I06 is an affiliate not a unit so it doesn't count toward I02; the 'last listed affiliation counts' rule is only implied, and the Halloran Institute is named only by ID.
- `sparql+axioms` run 5: No answer given; meets none of the checklist points

