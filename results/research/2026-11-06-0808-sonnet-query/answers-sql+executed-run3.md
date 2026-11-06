**Q1.** 2. A01, A02 and A03 are merged into one person (A01), and "M. Ellison" is a separate person (A04).

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all of A01's credits; W03 is merged with W02.

**Q3.** No. W37 is by A05 and W38 by A06, who have different ORCIDs and are separate people.

**Q4.** 2. A05's research works are W14 and W37.

**Q5.** No. W08 is by A04 and W01 by A01, who have different ORCIDs and are separate people in `people`.

**Q6.** A01. A01 has 5 research works credited to I02/I03/I04 (W01, W03, W06, W12, W19), against 4 for A07 and 2 for A08.

**Q7.** 5. Mara Ellison's research works are W01, W03, W06, W12 and W19.

**Q8.** I01, via I04 → I03 → I02 → I01.

**Q9.** 8. They are W01, W03, W06, W12, W13, W19, W71 and W72; I06 does not roll up into I02 in `institution_units`.

**Q10.** 12. These are the 8 from Q9 plus the I05 works W14, W28, W29 and W37.

**Q11.** 6. They are W08, W16, W20, W21, W22 and W24; W23 is retracted and not research output.

**Q12.** Full 4, fractional 3. The 2024 works are W20, W21, W22 and W24, which score 0.5, 0.5, 1 and 1.

**Q13.** Full counting is a tie, so there is no single answer. Both institutions have 4 works: Kesting has W20, W21, W22 and W24, and Rostval has W21, W27, W28 and W29. Under fractional counting Kesting leads, 3 to 1.

**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W28, W29, W71 and W72; W28 and W29 count 0.5 each and the rest count 1.

**Q15.** 4. They are W12, W21, W28 and W51; W05 and W10 are not research output.

**Q16.** 10. They are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74; W04 and W09 are excluded.

**Q17.** W04 (editorial) and W05 (erratum). W07 is also not research output, but because its source S04 is delisted, not because of its type.

**Q18.** 4. They are W01, W03, W13 and W72; W05 is an erratum.

**Q19.** 7. They are W12, W13, W14, W15, W16, W17 and W18.

**Q20.** None. W03 and W31 are merged with W02 and W42, but those records are not separate works in the data.

**Q21.** 4. They are W27, W31, W39 and W50.

**Q22.** W30 has more in total (5 vs 4), and W31 has more within its window (4 vs 1). W30 is cited by W60–W64, with only W60 (2020) inside 2019–2021. W31 is cited by W62, W65, W66 and W67, all inside 2023–2025.

**Q23.** 5 in total and 1 within the window. W60 (2020) is the only citer in 2019–2021.

**Q24.** 3. They are W20, W21 and W22; W23 is retracted.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted and not research output.

**Q27.** I12, with 3 citing works (W33, W34, W35). I11 and I09 have 1 each.

**Q28.** 1. Only W32 cites Kesting's research works.

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15, all GB).

**Q30.** 3. They are W12, W13 and W14.

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, which are in turn cited by these three.

**Q32.** 5. They are W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations.

**Q34.** 3. They are W08, W16 and W24.

**Q35.** 2. They are W21 and W24.

**Q36.** 2. They are W17 and W24; W76 is an editorial.

**Q37.** I06. It is the only credit on W70 (author A08).

**Q38.** I04, I03, I02 and I01, from I04's chain of units.

**Q39.** 3. They are W01, W13 and W71, all in S01.

**Q40.** S01, which has tier_rank 1.

**Q41.** No. S03 has rank 3 and S02 has rank 2, so S03 is lower.

**Q42.** 0. S04 is delisted, so its works (W07, W75) are not research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04 and I05. I06 has I02 as its parent, but `institution_units` does not count it towards I02 or I01.

**Q45.** 3. They are W70, W73 and W74.

**Q46.** I01, following the `parent_id` chain I06 → I02 → I01. This is not a roll-up, since I06's works do not count towards I01.

**Q47.** The data does not show a swap. Under full counting Kesting and Rostval tie at 4 each in 2024, and Kesting leads only under fractional counting (3 vs 1). Rostval's works are shared among more outside authors, so each of its works counts for less.

**Q48.** W70 is credited to I06 (Halloran, an affiliated institution), not to the Tessel Laboratory (I04). I06 does not count towards I02 in `institution_units`, so W70 is not an Albury work. The Tessel credits are on W71 and W72.

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":4,"fractional":3},"Q13":{"full":"tie","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":[]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I01"}}
```