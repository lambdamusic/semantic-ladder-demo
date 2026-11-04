**Q1.** 2. A01 (Mara Ellison, with A02 and A03 merged in) and A04 (M. Ellison) are separate people. "Ellison, Mara J." appears nowhere in people.csv, so the data cannot confirm it belongs to A01.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are every work credited to A01 in credits.csv.

**Q3.** No. A05 and A06 are two different people with different ORCIDs (0000-0001-6105-5008 and 0000-0007-5475-1779).

**Q4.** 2. A05 is credited on W14 and W37, both research output.

**Q5.** No. A04 (ORCID 0000-0004-8662-8360) and A01 (ORCID 0000-0002-9841-6229) are different people.

**Q6.** A01. Its research works credited to I02, I03 or I04 are W01, W03, W06, W12 and W19 (5), ahead of A07 (4).

**Q7.** 5. Of A01's eight works, research output is W01, W03, W06, W12 and W19 (W04, W05 and W07 are not).

**Q8.** I01. I04 → I03 → I02 → I01 via parent_id, matching levels_up 3 in institution_units.

**Q9.** 8. I02 units are I02, I03 and I04; research works are W01, W03, W06, W12, W13, W19, W71 and W72.

**Q10.** 12. Adds I05's research works (W12, W14, W28, W29, W37) to the eight from Q9, with W12 overlapping.

**Q11.** 6. I07 and I08 give W08, W16, W20, W21, W22 and W24 (W23 is not research output).

**Q12.** Full 3, fractional 2. The 2024 works are W20, W21 and W22; Kesting holds 1/2 of W20, 1/2 of W21 (A09 and A10 out of four authors) and all of W22.

**Q13.** Full: I09 (4 vs 3). Fractional: I07 (2.0 vs 1.0). In 2024 Rostval has W21, W27, W28 and W29, each with a 1/4 share, totalling 1.0.

**Q14.** Full 7, fractional 6. Seven 2024 research works have a GB-credited author (W06, W12, W13, W28, W29, W71, W72); W28 and W29 each give 0.5, the rest 1.

**Q15.** 4. These are W12, W21, W28 and W51. W05 and W10 are 2024 but not research output.

**Q16.** 10. S01 research works are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 and W05. These are the editorial and the erratum. W07 is excluded for its delisted source, not its type.

**Q18.** 4. A07's research works are W01, W03, W13 and W72 (W05 is not research output).

**Q19.** 7. The citing works of W03 (the merged W02/W03 record) are W12 to W18. W05, the erratum with the same title, has no citations.

**Q20.** None. The preprints W02 and W42 are merged into W03 and W31, and W18 has no matching published version in the data.

**Q21.** 4. I14 is credited on W27, W31, W39 and W50, all research output.

**Q22.** More total: W30 (5 vs 4). More within window: W31 (4 vs 1). W30's window is 2019–2021, which holds only W60. W31's window is 2023–2025, which holds W62, W65, W66 and W67.

**Q23.** Total 5 (W60–W64). Within 2019–2021, 1 (W60, 2020).

**Q24.** 3. A09's research works are W20, W21 and W22 (W23 is retracted).

**Q25.** 6. Citations are W20 (3: W32, W35, W36), W21 (2: W33, W36) and W22 (1: W34).

**Q26.** No. W23 is retracted and marked research_output "no".

**Q27.** I12, 3 citing works (W33, W34, W35). Kesting's cited works are cited by W32 (I09), W33, W34, W35 (I12) and W36 (I11).

**Q28.** 1. Only W32 (I09) cites a Kesting work (W20).

**Q29.** Author 2, institution 2, country 4. The citing works of W03 are W12 to W18. Shared author: W12 and W13. Albury (I02/I03/I04): W12 and W13. GB-credited: W12, W13, W14 and W15.

**Q30.** 3. Citing works with an Albury System (I01 units) credit are W12, W13 and W14.

**Q31.** W50, W51 and W52. W40 and W41 are the works citing W01, and these three cite them.

**Q32.** 5. Hop 1 is W40 and W41, and hop 2 is W50, W51 and W52.

**Q33.** W20, with 3 citations.

**Q34.** 3. Kesting's 2025 research works are W08, W16 and W24.

**Q35.** 2. I08 is credited on W21 and W24.

**Q36.** 2. S06 research works are W17 and W24 (W76 is an editorial).

**Q37.** I06. W70's only credit is A08 at I06.

**Q38.** I04, I03, I02 and I01. W71 is credited to I04, which rolls up through I03, I02 and I01 per institution_units.

**Q39.** 3. The Albury research works in S01 (rank 1) are W01, W13 and W71.

**Q40.** S01. It is the only source with tier_rank 1.

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, so S03 is lower.

**Q42.** 0. Both S04 works (W07, W75) are not research output, since S04 is delisted.

**Q43.** No. W07's research_output is "no" (S04 is delisted).

**Q44.** I02, I03, I04 and I05. These are the institutions whose institution_units rows include I01 at a level above 0. I06 has parent_id I02 in institutions.csv but no institution_units row linking it to I01, so the data is inconsistent on whether it is part of the system.

**Q45.** 3. I06 is credited on W70, W73 and W74, all research output.

**Q46.** I01, following parent_id from I06 → I02 → I01. This conflicts with institution_units, which lists I06 as counting only towards itself.

**Q47.** Full counting gives each work once per institution, so Rostval's four works (W21, W27, W28, W29) beat Kesting's three (W20, W21, W22). Fractional counting weights by author share: Kesting gets 1.0 from W20 and W21 combined plus 1.0 from single-author W22, giving 2.0. Rostval gets only one author in four on each of its four works, giving 1.0.

**Q48.** The premise doesn't match the data. W70's author A08 is credited to I06 (Halloran), not the Tessel Laboratory (I04). Tessel appears only on W71 and W72, and I06 counts only towards itself in institution_units, so W70 is not an Albury work.

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