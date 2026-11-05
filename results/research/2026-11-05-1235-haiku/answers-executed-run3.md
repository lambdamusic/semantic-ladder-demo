**Q1.** Two: A01 (Mara Ellison) and A04 (M. Ellison). The third name, "Ellison, Mara J.", does not appear in people.csv, so I can't place it; if it is A02 or A03 (merged into A01, names not shown), it is still A01.

**Q2.** Eight works: W01, W03, W04, W05, W06, W07, W12, W19, all credited to A01.

**Q3.** No. W37 credits A05 and W38 credits A06, and people.csv keeps A05 and A06 as separate people with different ORCIDs.

**Q4.** Two: W14 and W37 are both credited to A05 at I05, and both are research output.

**Q5.** No. W08 credits A04 and W01 credits A01, and people.csv keeps A04 ("M. Ellison", ORCID 0000-0004-8662-8360) separate from A01 (ORCID 0000-0002-9841-6229).

**Q6.** A01. Under I02 with units I03 and I04, A01 has five research works (W01, W03, W06, W12, W19), ahead of A07 (four) and A08 (two).

**Q7.** Five: W01, W03, W06, W12, W19 are research output. W04, W05 and W07 are not.

**Q8.** I01. The parent chain is I04 → I03 → I02 → I01, and I01 has no parent.

**Q9.** Eight distinct works: W01, W03, W06, W12, W19 (I02), W13 and W72 (I03), and W71 and W72 (I04). W72 is counted once.

**Q10.** Twelve distinct works, from I02, I03, I04 and I05 (the units counting towards I01). I06 is excluded because institution_units lists only I06 for it.

**Q11.** Six: W08, W16, W20, W21, W22, W24 (I07 and I08). W23 is retracted and not research output.

**Q12.** Full 3 (W20, W21, W22). Fractional 2.0, from W20 (1 of 2 authors = 0.5), W21 (2 of 4 = 0.5) and W22 (1 of 1 = 1).

**Q13.** Full: I09 (4 works in 2024: W21, W27, W28, W29, against 3 for I07). Fractional: I07 (2.0, against 1.0 for I09).

**Q14.** Full 7 (W06, W12, W13, W28, W29, W71, W72). Fractional 6.0, because W28 and W29 each give 0.5 and the other five give 1 each.

**Q15.** Four: W12, W21, W28, W51. W05 and W10 are not research output.

**Q16.** Ten: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74. W04 and W09 are not research output.

**Q17.** W04 (editorial) and W05 (erratum), both excluded by document type. W07 is excluded because its source S04 is delisted, not for its type.

**Q18.** Four: W01, W03, W13, W72. W05 is not research output.

**Q19.** Seven: W12, W13, W14, W15, W16, W17, W18 cite W03, and all are research output.

**Q20.** None. W02 and W42 are preprint records merged into W03 and W31, but they are not rows in works.csv, and W18 (a preprint) has no published version in the data.

**Q21.** Four: W27, W31, W39, W50, all credited to A17 at I14.

**Q22.** W30 has more in total (5 against 4). W31 has more within its window (4 against 1). W31 (2023) has citations from W62, W65, W66 and W67 (all within 2023–2025); W30 (2019) has one, W60 (2020), within 2019–2021.

**Q23.** Total 5 (W60, W61, W62, W63, W64). Within 2019–2021: 1 (W60).

**Q24.** Three: W20, W21, W22. W23 is not research output.

**Q25.** Six. W20 is cited three times (W32, W35, W36), W21 twice (W33, W36) and W22 once (W34).

**Q26.** No. W23 has research_output "no" because it is retracted.

**Q27.** I12 (Université de Lorvain), with three citing works: W33, W34 and W35. The other citing institutions are I09 (W32) and I11 (W36), with one each.

**Q28.** One: W32, the only I09-credited work that cites a Kesting research work (W20).

**Q29.** Author self-citations: 2 (W12 and W13 share A01 or A07 with W03). Institution (University of Albury units): 2 (W12 via I02, W13 via I03). Country (GB): 4 (W12, W13, W14 via I05, W15 via I13).

**Q30.** Three: W12, W13 and W14 have an author at an institution under I01 (I02, I03 or I05), matching W03's institutions.

**Q31.** W50, W51 and W52. They cite W40 or W41, which cite W01.

**Q32.** Five: W40 and W41 (citing W01), then W50, W51 and W52 (citing W40 or W41).

**Q33.** W20, with three citations (from W32, W35 and W36), the most of Kesting's research works.

**Q34.** Three: W08, W16 and W24 (all 2025).

**Q35.** Two: W21 and W24, both credited to A10 at I08.

**Q36.** Two: W17 and W24 are research output in S06. W76 is an editorial.

**Q37.** I06 (Halloran Institute for Coastal Studies), per the single credit A08 on W70.

**Q38.** I04, I03, I02 and I01. W71 is credited to I04, whose chain of parents runs through I03, I02 and I01.

**Q39.** Three: W01, W13 and W71 are in S01, the tier-1 source. The other Albury works are in S02 or S03.

**Q40.** S01 (Journal of Marine Autonomy), tier_rank 1.

**Q41.** No. S03 is tier_rank 3, and S02 is tier_rank 2, so S02 is the higher tier.

**Q42.** Zero. S04 is delisted, so its works are not research output (W07).

**Q43.** No. W07 is from delisted source S04 and has research_output "no".

**Q44.** I02, I03, I04 and I05. I06 has parent I02 but its works do not roll up to I01 per institution_units, so I have left it out.

**Q45.** Three: W70, W73 and W74, all credited to I06.

**Q46.** I01. I06 → I02 → I01.

**Q47.** Full counting gives each work to every institution with an author on it, so the count of works decides. Rostval has four 2024 works against Kesting's three, so it wins full counting. Fractional counting divides each work among all its authors, and Rostval has one of four authors on each of its four works (1.0 total). Kesting's shares are larger: W22 is single-authored and W21 has two of four authors (2.0 total).

**Q48.** The premise is wrong. W70's only credit is A08 at I06 (Halloran), not I04 (Tessel), and I06's works roll up only to I06 in institution_units, so W70 is not counted for the University of Albury. A08 is credited to I04 on W71 and W72, not W70.

```json
{
  "Q1": {"count": 2},
  "Q2": {"works": ["W01", "W03", "W04", "W05", "W06", "W07", "W12", "W19"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 2},
  "Q5": {"same": "no"},
  "Q6": {"author": "A01"},
  "Q7": {"count": 5},
  "Q8": {"parent": "I01"},
  "Q9": {"count": 8},
  "Q10": {"count": 12},
  "Q11": {"count": 6},
  "Q12": {"full": 3, "fractional": 2},
  "Q13": {"full": "I09", "fractional": "I07"},
  "Q14": {"full": 7, "fractional": 6},
  "Q15": {"count": 4},
  "Q16": {"count": 10},
  "Q17": {"works": ["W04", "W05"]},
  "Q18": {"count": 4},
  "Q19": {"count": 7},
  "Q20": {"works": []},
  "Q21": {"count": 4},
  "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
  "Q23": {"total": 5, "in_window": 1},
  "Q24": {"count": 3},
  "Q25": {"count": 6},
  "Q26": {"counts": "no"},
  "Q27": {"institution": "I12", "citing_works": 3},
  "Q28": {"count": 1},
  "Q29": {"author": 2, "institution": 2, "country": 4},
  "Q30": {"count": 3},
  "Q31": {"works": ["W50", "W51", "W52"]},
  "Q32": {"count": 5},
  "Q33": {"work": "W20"},
  "Q34": {"count": 3},
  "Q35": {"count": 2},
  "Q36": {"count": 2},
  "Q37": {"institution": "I06"},
  "Q38": {"institutions": ["I04", "I03", "I02", "I01"]},
  "Q39": {"count": 3},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 0},
  "Q43": {"research": "no"},
  "Q44": {"institutions": ["I02", "I03", "I04", "I05"]},
  "Q45": {"count": 3},
  "Q46": {"parent": "I01"}
}
```