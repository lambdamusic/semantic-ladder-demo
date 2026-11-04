# research: claude:sonnet, 2026-11-04 20:53

48 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **58%** | 46% to 70% | 14 of 48 |
| `executed` | **93%** | 87% to 98% | 6 of 48 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `executed` | +35 points | +21 to +48 |

## By question

| Question | Graded by | `csv` | `executed` |
|---|---|---|---|
| Q1 | code | ❌ ❌ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | code | ✅ ✅ ✅ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ 🟡 ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q15 | code | ❌ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q19 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ❌ ✅ ❌ |
| Q21 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q31 | code | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ❌ ✅ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ |
| Q35 | code | ✅ ❌ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ❌ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q38 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ✅ ❌ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q41 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q46 | code | ❌ ❌ ❌ ❌ ❌ | ❌ ❌ ✅ ✅ ✅ |
| Q47 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 ✅ 🟡 🟡 🟡 |
| Q48 | llm | ❌ ❌ ❌ ❌ ❌ | 🟡 🟡 🟡 🟡 🟡 |

## Lists, with partial credit

The 6 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `csv` | 60% | 95% |
| `executed` | 73% | 89% |

**The checklist grader agreed with itself** on 18 of 20 answers graded twice.

## Why each miss was marked

**Q1.** How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?

- `csv` run 1: count: expected 2, got 1
- `csv` run 2: count: expected 2, got 1
- `csv` run 3: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1

**Q2.** List every work, of any type, that Mara Ellison (A01) is an author of.

- `executed` run 1: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 2: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 3: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 4: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']
- `executed` run 5: works: expected ['W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19'], got ['W01', 'W03', 'W04', 'W05', 'W06', 'W07', 'W12', 'W19']

**Q6.** Which author has the most research works credited to the University of Albury, its units included?

- `csv` run 4: author: expected A01, got A08

**Q7.** How many research works has Mara Ellison authored?

- `csv` run 1: count: expected 5, got 6
- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6
- `csv` run 4: count: expected 5, got 6
- `csv` run 5: count: expected 5, got 6

**Q9.** How many research works is the University of Albury (I02) credited with, its units included?

- `csv` run 1: count: expected 8, got 12
- `csv` run 2: count: expected 8, got 12
- `csv` run 3: count: expected 8, got 12
- `csv` run 4: count: expected 8, got 12
- `csv` run 5: count: expected 8, got 12

**Q10.** How many research works is the Albury University System (I01) credited with, all its units included?

- `csv` run 1: count: expected 12, got 16
- `csv` run 2: count: expected 12, got 16
- `csv` run 3: count: expected 12, got 16
- `csv` run 4: count: expected 12, got 16
- `csv` run 5: count: expected 12, got 16

**Q11.** How many research works is Kesting University (I07) credited with, its units included?

- `csv` run 3: count: expected 6, got 7

**Q12.** How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?

- `executed` run 3: full: expected 3, got 4; fractional: expected 2, got 3

**Q13.** In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?

- `executed` run 3: full: expected I09, got None

**Q15.** How many research works appeared in Ocean Sensing Letters (S02) in 2024?

- `csv` run 1: count: expected 4, got 3

**Q20.** Which works in the data are preprints of another work that is also in the data?

- `executed` run 2: works: expected ['W02', 'W42'], got []
- `executed` run 3: works: expected ['W02', 'W42'], got []
- `executed` run 5: works: expected ['W02', 'W42'], got []

**Q24.** How many research works has Lena Vossberg (A09) authored?

- `csv` run 2: count: expected 3, got 4
- `csv` run 3: count: expected 3, got 4
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4

**Q25.** What is the total of the citation counts of Lena Vossberg's research works?

- `csv` run 2: count: expected 6, got 7
- `csv` run 3: count: expected 6, got 7
- `csv` run 4: count: expected 6, got 7
- `csv` run 5: count: expected 6, got 7

**Q26.** Does W23 count towards Kesting University's research output?

- `csv` run 2: counts: expected no, got yes
- `csv` run 3: counts: expected no, got yes
- `csv` run 4: counts: expected no, got yes
- `csv` run 5: counts: expected no, got yes

**Q31.** Which works cite at least one of the works that cite W01?

- `csv` run 2: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']
- `csv` run 3: works: expected ['W50', 'W51', 'W52'], got ['W50', 'W51', 'W52', 'W90']

**Q32.** How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?

- `csv` run 2: count: expected 5, got 6
- `csv` run 3: count: expected 5, got 6

**Q34.** How many research works was Kesting University (units included) credited with in 2025?

- `csv` run 2: count: expected 3, got 2
- `csv` run 4: count: expected 3, got 2
- `csv` run 5: count: expected 3, got 2
- `executed` run 3: count: expected 3, got 2

**Q35.** How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?

- `csv` run 2: count: expected 2, got 1
- `csv` run 4: count: expected 2, got 1
- `csv` run 5: count: expected 2, got 1

**Q36.** How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?

- `csv` run 2: count: expected 2, got 0
- `csv` run 4: count: expected 2, got 0
- `csv` run 5: count: expected 2, got 0

**Q37.** Which institution is W70 credited to?

- `csv` run 1: institution: expected I06, got I04
- `csv` run 2: institution: expected I06, got I02
- `csv` run 3: institution: expected I06, got I04
- `csv` run 4: institution: expected I06, got I04
- `csv` run 5: institution: expected I06, got I04

**Q38.** Which institutions is W71 credited to, at every level?

- `csv` run 1: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I01', 'I02', 'I03', 'I04', 'I06']
- `csv` run 2: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 3: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 4: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']
- `csv` run 5: institutions: expected ['I01', 'I02', 'I03', 'I04'], got ['I06', 'I04', 'I03', 'I02', 'I01']

**Q39.** How many of the University of Albury's research works (units included) appeared in a source of the highest tier?

- `csv` run 1: count: expected 3, got 4
- `csv` run 2: count: expected 3, got 1
- `csv` run 3: count: expected 3, got None
- `csv` run 4: count: expected 3, got 4
- `csv` run 5: count: expected 3, got 4

**Q40.** Which source is in the highest tier?

- `csv` run 2: source: expected S01, got S04
- `csv` run 3: source: expected S01, got None

**Q41.** Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?

- `csv` run 1: higher: expected no, got depends
- `csv` run 2: higher: expected no, got depends
- `csv` run 3: higher: expected no, got depends
- `csv` run 4: higher: expected no, got depends

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

**Q47.** Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?

- `csv` run 1: Gets Kesting's shares (W22 single-author, half of W20 and W21) but says W21 is in Rostval's four works and doesn't state each has four authors with a quarter share; it gives 1.0 rather than a quarter each and doesn't explicitly say they swap places.
- `csv` run 2: Gets Kesting's larger shares (sole W22, half of W20/W21) but omits that each Rostval work has four authors, one from Rostval, so a quarter each; only roughly implies it.
- `csv` run 3: Gives Kesting's shares (0.5, 0.5, 1) correctly, and Rostval's quarter-shares with four authors, but doesn't say only one author per work is from Rostval, and uses I09 instead of naming the institution; the Rostval point is mostly met, Kesting's W22 single-author review not identified as such.
- `csv` run 4: Gets Rostval's 0.25 shares across four-author works and Kesting's larger shares (W22 whole, 0.5 on W20/W21), but never states that Rostval has one author on each of its four works, which is implied only loosely.
- `csv` run 5: Rostval's quarter-share per work is covered (1.0 total), but Kesting's shares are not specified (W22 single-author review, half of W20 and W21); it only gives a total of 2.0 and mentions W21 as Rostval's, not clearly identifying Kesting's works.
- `executed` run 1: Says Rostval's four works give each 0.25 (first point), but doesn't mention four authors with one from Rostval, and Kesting's shares are given only as 0.5/0.5/1 without identifying W22 as a single-author review; roughly meets the shares point, though the full-counting framing differs
- `executed` run 3: Correctly gives Rostval's four works at 0.25 each, but credits Kesting with sole-author W22 and W24 rather than W22 plus half of W20 and W21, and denies the swap by claiming a tie under full counting.
- `executed` run 4: Gets Kesting's shares (W22 sole, half of W20/W21) and Rostval's one-of-four authors per work, but never says each Rostval work is a quarter share; also the identifiers I09/I07 are not named as the institutions.
- `executed` run 5: Gives Kesting's larger shares (sole author of W22, half of W20/W21) but says Rostval holds a quarter of each of its four works without noting each has four authors with one from Rostval; mostly meets point 2, point 1 only loosely

**Q48.** Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?

- `csv` run 1: Rejects the premise, whereas the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, an affiliated institute that doesn't roll up to Albury.
- `csv` run 2: Rejects the premise and says W70 counts for the University of Albury; checklist says only the last-listed affiliation counts (Halloran Institute), an affiliated institute that doesn't roll up.
- `csv` run 3: Asserts the opposite: claims W70 does count for Albury, whereas the key says only the last-listed affiliation counts (Halloran Institute, an affiliated institute that doesn't roll up).
- `csv` run 4: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, so W70 goes to the Halloran Institute, which is affiliated and does not roll up to Albury.
- `csv` run 5: Rejects the premise and says W70 counts for Albury; the key says only the last-listed affiliation counts, crediting the Halloran Institute, which is an affiliated institute and does not roll up to Albury.
- `executed` run 1: Says W70 is credited to the Halloran Institute (last-listed affiliation) and that I06 counts only toward itself, not the University of Albury; but doesn't state that it's an affiliated institute rather than a unit, nor the 'last listed affiliation' rule explicitly
- `executed` run 2: Correctly says the affiliate doesn't roll up to the University, and credits W70 to I06. But it never gives the last-listed-affiliation rule and wrongly denies that the author lists the Tessel Laboratory.
- `executed` run 3: Says W70 is credited only to I06 (Halloran Institute), matching the last-listed affiliation point, but never says that the Halloran Institute is an affiliated institute rather than a unit, so its works don't roll up to Albury; it only says I06 counts towards itself, not I02.
- `executed` run 4: Says W70 is credited to I06, an affiliated institution not rolling up to I02, but omits that only the last-listed affiliation counts.
- `executed` run 5: Says W70 is credited to I06 (Halloran) and that I06 is an affiliate not rolling up to I02, but never states the 'last-listed affiliation counts' rule

