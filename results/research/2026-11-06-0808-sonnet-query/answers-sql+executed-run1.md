**Q1.** 2. A01 merges the author records A01, A02 and A03 (Mara Ellison and "Ellison, Mara J."). "M. Ellison" is a separate person, A04, with a different ORCID.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all A01's credited works (W03 also covers W02).

**Q3.** No. W37 is by A05 (I05) and W38 by A06 (I12), who are separate people with different ORCIDs.

**Q4.** 2. A05 authored W14 and W37, both research works.

**Q5.** No. W08 is by A04 and W01 by A01, who are separate people with different ORCIDs, so the data gives no basis to merge them.

**Q6.** A01. She has 5 research works at the University of Albury (W01, W03, W06, W12, W19), against 4 each for A07 and A08.

**Q7.** 5. A01's research works are W01, W03, W06, W12 and W19.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 8. They are W01, W03, W06, W12, W13, W19, W71 and W72, credited to I02, I03 or I04.

**Q10.** 12. These are the 8 Albury works plus W14, W28, W29 and W37 from I05.

**Q11.** 6. They are W08, W16, W20, W21, W22 and W24, credited to I07 or I08. W23 is excluded because it is retracted.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5) and W22 (1).

**Q13.** Full counting: I09 (4 works against 3). Fractional counting: I07 (2.0 against 1.0).

**Q14.** Full 7, fractional 5.5. The works are W06 (0.5), W12 (1), W13 (1), W28 (0.5), W29 (0.5), W71 (1) and W72 (1).

**Q15.** 4. They are W12, W21, W28 and W51.

**Q16.** 10. They are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 (editorial) and W05 (erratum). W07 is an article that fails because its source is delisted, not because of its type.

**Q18.** 4. A07's research works are W01, W03, W13 and W72; W05 is an erratum.

**Q19.** 7. The citing works are W12, W13, W14, W15, W16, W17 and W18.

**Q20.** W02 and W42. The record_ids show W02 merged into W03 and W42 merged into W31. W18 is typed as a preprint, but it is not merged into any work in the data.

**Q21.** 4. They are W27, W31, W39 and W50.

**Q22.** In total W30 has more citations (5 against 4). Within its publication year and the two years after, W31 has more (4 against 1).

**Q23.** Total 5 (W60–W64); within the window only 1 (W60, 2020).

**Q24.** 3. A09's research works are W20, W21 and W22; W23 is retracted.

**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).

**Q26.** No. W23 is retracted and not research output.

**Q27.** I12, with 3 citing works (W33, W34, W35). I11 has 1 (W36) and I09 has 1 (W32).

**Q28.** 1. Only W32 does.

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15).

**Q30.** 3. They are W12, W13 and W14 (I05 sits in the Albury University System).

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and these three cite those.

**Q32.** 5. They are W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations.

**Q34.** 3. They are W08, W16 and W24.

**Q35.** 2. They are W21 and W24.

**Q36.** 2. They are W17 and W24; W76 is a foreword and not research output.

**Q37.** I06. W70's author A08 is credited to the Halloran Institute, not the Tessel Laboratory.

**Q38.** I04, I03, I02, I01 (I04 and the three levels above it).

**Q39.** 3. They are W01, W13 and W71, all in S01.

**Q40.** S01, with tier_rank 1.

**Q41.** No. S03 has tier_rank 3 and S02 has rank 2, so S03 is lower.

**Q42.** 0. S04 is delisted, so none of its works count as research output.

**Q43.** No. W07 is in S04, which is delisted.

**Q44.** I02, I03, I04, I05. I06 is only an affiliate and does not roll up to I01.

**Q45.** 3. They are W70, W73 and W74.

**Q46.** I01, going by the parent_id chain I06 → I02 → I01. Caveat: I06 is typed AFF and institution_units gives it no roll-up, so it is not truly part of that hierarchy.

**Q47.** Under full counting Rostval has 4 works (W21, W27, W28, W29) against Kesting's 3. Kesting's authors take larger shares of its works, so fractionally it leads, 2.0 to 1.0.

**Q48.** W70's only credit is I06, the Halloran Institute, which is an affiliate (AFF). Affiliates don't count toward I02, and W70 is not credited to the Tessel Laboratory (I04).

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":5.5},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I01"}}
```