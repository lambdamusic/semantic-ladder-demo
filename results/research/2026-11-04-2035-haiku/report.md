# research: claude:haiku, 2026-11-04 20:35

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **42%** | 29% to 55% | 5 of 48 |
| `executed` | **90%** | 82% to 97% | 3 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `executed` | +48 points | +33 to +62 |

## By question

| Question | Graded by | `csv` | `executed` |
|---|---|---|---|
| Q1 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ❌ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ |
| Q14 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q21 | code | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ✅ ❌ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q47 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 🟡 ❌ 🟡 🟡 |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | 🟡 🟡 🟡 🟡 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 33% | 89% |
| `executed` | 60% | 82% |

**The checklist grader agreed with itself** on 17 of 20 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `csv` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `csv` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W04', 'W05', 'W06', 'W12']
- `executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `csv` run 1: author: expected A01, got A07
- `csv` run 2: author: expected A01, got A07
- `csv` run 3: author: expected A01, got A07

**Q7.** How many research works has Mara Ellison authored?

- `csv` run 1: count: expected 5, got 3
- `csv` run 2: count: expected 5, got 7
- `csv` run 3: count: expected 5, got 3
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 7

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 8, got 12
- `csv` run 2: count: expected 8, got 13
- `csv` run 3: count: expected 8, got 13
- `csv` run 4: count: expected 8, got 12
- `csv` run 5: count: expected 8, got 13

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 12, got 16
- `csv` run 2: count: expected 12, got 17
- `csv` run 3: count: expected 12, got 17
- `csv` run 4: count: expected 12, got 16
- `csv` run 5: count: expected 12, got 17

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 1: count: expected 6, got 9
- `csv` run 2: count: expected 6, got 9
- `csv` run 3: count: expected 6, got 9
- `csv` run 4: count: expected 6, got 9
- `csv` run 5: count: expected 6, got 9

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `executed` run 3: full: expected I09, got None

**Q14.** How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?

- `csv` run 1: full: expected 7, got 8; fractional: expected 6, got 7

**Q16.** How many research works appeared in the Journal of Marine Autonomy (S01)?

- `csv` run 1: count: expected 10, got 11
- `csv` run 2: count: expected 10, got 11
- `csv` run 3: count: expected 10, got 11
- `csv` run 4: count: expected 10, got 11
- `csv` run 5: count: expected 10, got 11

**Q18.** How many distinct research works has Priya Ramanathan (A07) authored?

- `csv` run 1: count: expected 4, got 5
- `csv` run 2: count: expected 4, got 5
- `csv` run 3: count: expected 4, got 5
- `csv` run 5: count: expected 4, got 5

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `executed` run 1: works: expected ['W02', 'W42'], got []
- `executed` run 2: works: expected ['W02', 'W42'], got []
- `executed` run 3: works: expected ['W02', 'W42'], got []
- `executed` run 4: works: expected ['W02', 'W42'], got []
- `executed` run 5: works: expected ['W02', 'W42'], got []

**Q21.** How many research works is Oskel Polytechnic (I14) credited with?

- `csv` run 1: count: expected 4, got 5
- `csv` run 2: count: expected 4, got 5
- `csv` run 3: count: expected 4, got 5
- `csv` run 5: count: expected 4, got 5

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 1: count: expected 6, got 10
- `csv` run 2: count: expected 6, got 10
- `csv` run 3: count: expected 6, got 10
- `csv` run 4: count: expected 6, got 10
- `csv` run 5: count: expected 6, got 10

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 1: counts: expected no, got depends
- `csv` run 2: counts: expected no, got depends
- `csv` run 3: counts: expected no, got depends
- `csv` run 4: counts: expected no, got depends
- `csv` run 5: counts: expected no, got yes

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 1: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 4: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 5: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6

**Q33.** Which of Kesting University's research works has the most citations?

- `csv` run 1: work: expected W20, got W22
- `csv` run 2: work: expected W20, got W22
- `csv` run 3: work: expected W20, got W22
- `csv` run 4: work: expected W20, got W22
- `csv` run 5: work: expected W20, got W22

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 1: count: expected 3, got 5
- `csv` run 2: count: expected 3, got 5
- `csv` run 3: count: expected 3, got 5
- `csv` run 4: count: expected 3, got 5
- `csv` run 5: count: expected 3, got 5

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 1: count: expected 2, got 0
- `csv` run 2: count: expected 2, got 0
- `csv` run 3: count: expected 2, got 0
- `csv` run 4: count: expected 2, got 0
- `csv` run 5: count: expected 2, got 0

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04
- `csv` run 2: institution: expected I06, got I04
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I04', 'I06', 'I03', 'I02', 'I01']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4

**Q42.** How many research works appeared in Global Marine Science Reports (S04)?

- `csv` run 1: count: expected 0, got 2
- `csv` run 2: count: expected 0, got 2
- `csv` run 3: count: expected 0, got 2
- `csv` run 4: count: expected 0, got 2
- `csv` run 5: count: expected 0, got 2

**Q43.** Is W07 research output?

- `csv` run 1: research: expected no, got yes
- `csv` run 2: research: expected no, got yes
- `csv` run 3: research: expected no, got yes
- `csv` run 4: research: expected no, got yes
- `csv` run 5: research: expected no, got yes

**Q44.** Which institutions are part of the Albury University System, at any level below it?

- `csv` run 1: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 3: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `csv` run 5: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `executed` run 2: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']
- `executed` run 4: institutions: expected ['I02', 'I03', 'I04', 'I05'], got ['I02', 'I03', 'I04', 'I05', 'I06']

**Q45.** How many research works is the Halloran Institute for Coastal Studies (I06) credited with?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4

**Q46.** What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?

- `csv` run 1: parent: expected I06, got I01
- `csv` run 2: parent: expected I06, got I01
- `csv` run 3: parent: expected I06, got I01
- `csv` run 4: parent: expected I06, got I01
- `csv` run 5: parent: expected I06, got I01
- `executed` run 1: parent: expected I06, got I01
- `executed` run 2: parent: expected I06, got I01
- `executed` run 3: parent: expected I06, got I01
- `executed` run 4: parent: expected I06, got I01
- `executed` run 5: parent: expected I06, got I01

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Gets Rostval's four 4-author works at 1/4 each, but misses that Kesting's lead comes from a single-author review (W22) plus half shares of W20 and W21; the 2.0 total and the 'half' split are not explained, and the answer's account of full counting is muddled.
- `csv` run 2: Gets Rostval's quarter-share per work right, but for Kesting it cites W22 and W21 (2 of 4) rather than W22 plus half of both W20 and W21, so the checklist's Kesting point is only partly met
- `csv` run 3: Gives the quarter-credit point for Rostval's four-author works, but only vaguely says Kesting has larger shares; omits that W22 is a single-author review and that Kesting holds half of W20 and W21.
- `csv` run 4: Gets Rostval's one-of-four authors and Kesting's larger fractional shares broadly, but doesn't name the single-author review W22 or the half-shares of W20 and W21, and it states a vague 1.75–2.0 range.
- `csv` run 5: Gets Kesting's shares right (W22 single-author, 0.5 each from W20 and W21) and Rostval's one author per work, but doesn't state four authors per work, so a quarter each (gives 1.0 total, which matches).
- `executed` run 1: Gives Kesting's larger shares (W22 single-author, W20 two authors) but never says Rostval's four works each have four authors with one from Rostval, so a quarter each.
- `executed` run 2: Gets Rostval's quarter shares (0.25 each) and Kesting's single-author W22 at full credit, but says its other two works are 0.5 each, which matches the half shares for W20 and W21 only loosely; it never names W20 and W21 explicitly. Also, the answer's 'three' works for Kesting implies shares the checklist covers, so the main gap is naming W20/W21.
- `executed` run 3: Denies the swap and doesn't mention Rostval's four-author works at a quarter each or Kesting's larger shares (single-author W22, half of W20/W21).
- `executed` run 4: Gets Rostval's four-author quarter shares right, but credits Kesting's lead only to W22, omitting the half shares of W20 and W21.
- `executed` run 5: Gets Kesting's larger shares (single-author W22 plus W20/W21), but says Kesting gets 1.0 from W20 and W21 combined (half each is consistent) while Rostval's quarter-each reasoning is present only as 'one author in four'; it never states that W21 is shared or that the order flips, and its claim that Rostval has four works including W21 is unverified against the key's 'four 2024 works'.

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise, while the key says W70 is credited only to the last-listed affiliation (Halloran Institute), which is an affiliated institute that does not roll up to Albury.
- `csv` run 2: Rejects the premise and says W70 counts for Albury, whereas the key says it is credited to the Halloran Institute (last-listed affiliation), an affiliated institute that does not roll up to Albury
- `csv` run 3: Rejects the premise and credits W70 to the University of Albury, contradicting the key: only the last-listed affiliation counts (Halloran Institute), and as an affiliated institute rather than a unit it does not roll up to Albury.
- `csv` run 4: Contradicts the checklist: it denies the premise and says W70 counts for Albury, whereas the key says only the last-listed affiliation counts and Halloran is an affiliated institute, not a unit.
- `csv` run 5: Rejects the premise; the key says only the last-listed affiliation counts, so W70 goes to Halloran, an affiliated institute that doesn't roll up to Albury.
- `executed` run 1: Says W70 is credited only to Halloran (I06) and that I06 is not an Albury unit, but never states the rule that only the last-listed affiliation counts, and doesn't call Halloran an affiliated institute.
- `executed` run 2: Says W70 is credited only to Halloran (I06) and that I06 counts only for itself, so it doesn't roll up to Albury; but it never says the last-listed affiliation rule explicitly, and it frames the premise as false rather than explaining that Halloran is an affiliated institute, not a unit.
- `executed` run 3: Correctly says W70 is credited to Halloran (last-listed affiliation), but doesn't state that Halloran is an affiliated institute, not a unit, so its works don't roll up to Albury; its stated reason concerns Tessel counting towards I02.
- `executed` run 4: Identifies that W70 is credited to Halloran (I06) rather than Albury, but omits that Halloran is an affiliated institute, not a unit, so its works don't roll up to Albury; it also doesn't state the last-listed-affiliation rule.
- `executed` run 5: Says W70 is credited to Halloran (I06) and that I06 counts only toward itself, but does not state the 'last-listed affiliation counts' rule and does not explicitly call Halloran an affiliated institute rather than a unit.

