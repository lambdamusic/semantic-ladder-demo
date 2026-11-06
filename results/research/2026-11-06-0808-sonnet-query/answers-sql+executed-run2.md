**Q1.** 2. A01, A02 and A03 are merged into person A01 (Mara Ellison), and "M. Ellison" is a separate person, A04, with a different ORCID.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all credited to A01; W03 also merges record W02.

**Q3.** No. W37 is by A05 and W38 by A06, which have different ORCIDs and institutions (W37 at I05, W38 at I12).

**Q4.** 2. A05's works are W14 and W37, both research output.

**Q5.** No. W08 is by A04 (I07) and W01 by A01 (I02), and the people table keeps them as separate people with different ORCIDs.

**Q6.** A01. For the University of Albury, units included, A01 has 5 research works (W01, W03, W06, W12, W19), ahead of A07 with 4 and A08 with 2.

**Q7.** 5. The research works are W01, W03, W06, W12 and W19; W04, W05 and W07 are not research output.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 8. The works are W01, W03, W06, W12, W13, W19, W71 and W72, credited to I02, I03 or I04.

**Q10.** 12. These are the 8 Albury works plus W14, W28, W29 and W37 from I05.

**Q11.** 6. The works are W08, W16, W20, W21, W22 and W24; W23 is excluded because it is retracted and not research output.

**Q12.** Full 3, fractional 2.0. In 2024, W20 contributes 0.5, W21 contributes 0.5 (A09 and A10 are 2 of 4 authors) and W22 contributes 1.

**Q13.** Full: I09. Fractional: I07. Rostval has 4 works (W21, W27, W28, W29) against Kesting's 3, but only 4 × 0.25 = 1.0 against Kesting's 2.0.

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W71 and W72 (1 each), plus W28 and W29 (0.5 each).

**Q15.** 4. The works are W12, W21, W28 and W51; W05 and W10 are not research output.

**Q16.** 10. The works are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded from research output because its source S04 is delisted, not because of its type.

**Q18.** 4. The works are W01, W03, W13 and W72; W05 is an erratum.

**Q19.** 7. The citing works are W12, W13, W14, W15, W16, W17 and W18, all citing W03.

**Q20.** None. W02 and W42 appear only as merged records inside W03 and W31, and no other work in the data is a preprint of a published work that is also present.

**Q21.** 4. The works are W27, W31, W39 and W50.

**Q22.** In total: W30. Within its publication year and the two years after: W31.
- W30 has 5 citations (W60–W64), only W60 (2020) inside 2019–2021.
- W31 has 4 citations (W62, W65, W66, W67), all inside 2023–2025.

**Q23.** Total 5, in window 1.

**Q24.** 3. The research works are W20, W21 and W22; W23 is retracted and not research output.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted and its research_output is "no".

**Q27.** I12, with 3 citing works (W33, W34, W35). I09 and I11 have 1 each.

**Q28.** 1. Only W32 comes from Rostval and cites Kesting work (W20).

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15). The institution count includes W13 through I03, a unit of I02.

**Q30.** 3. The Albury University System citers are W12, W13 and W14 (I05).

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, which are in turn cited by those three works.

**Q32.** 5. The works are W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations (W32, W35, W36).

**Q34.** 3. The 2025 works are W08, W16 and W24.

**Q35.** 2. The works are W21 and W24.

**Q36.** 2. The works are W17 and W24; W76 is a foreword and not research output.

**Q37.** I06, the Halloran Institute (A08).

**Q38.** I04, I03, I02, I01.

**Q39.** 3. W01, W13 and W71 appeared in S01.

**Q40.** S01.

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, so S03 is lower.

**Q42.** 0. S04 is delisted, and its only works (W07, W75) are not research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05.

**Q45.** 3. The works are W70, W73 and W74.

**Q46.** I06. It is an affiliated institution (type AFF) whose institution_units row counts only toward itself, so it has no rollup parent. Its parent_id does name I02, so if you read the raw parent chain instead, the ultimate parent would be I01.

**Q47.** Kesting has fewer works in 2024 (3 against 4) but holds larger author shares on them. Rostval appears on more works, but as one of four authors each time, so its fractional total is lower.

**Q48.** The premise is off: W70 is credited to the Halloran Institute (I06), not the Tessel Laboratory (I04). I06 is an affiliated institution whose works count only toward itself, so W70 does not roll up to the University of Albury.

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":[]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I06"}}
```