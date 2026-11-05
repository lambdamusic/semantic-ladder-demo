**Q1.** 2. A01 merges A01, A02 and A03, which covers "Mara Ellison" and, presumably, "Ellison, Mara J.". A04 "M. Ellison" has a different ORCID and stays separate. The data does not show the names on A02 and A03, so the "Ellison, Mara J." match is inferred.
**Q2.** W01, W03, W04, W05, W06, W07, W12, W19 (credits for A01).
**Q3.** No. W37 credits A05 and W38 credits A06, and they have different ORCIDs.
**Q4.** 2 (W14, W37).
**Q5.** No. W08 credits A04 and W01 credits A01, and they have different ORCIDs.
**Q6.** A01. A01 has 5 research works at I02 (W01, W03, W06, W12, W19). A07 has 4, and A08 has 2.
**Q7.** 5 (W01, W03, W06, W12, W19). W04 and W05 are not research by type, and W07 is not because its source is delisted.
**Q8.** I01 (I04 → I03 → I02 → I01).
**Q9.** 8 (W01, W03, W06, W12, W13, W19, W71, W72).
**Q10.** 12. These are the 8 from Q9 plus W14, W28, W29 and W37 from I05.
**Q11.** 6 (W08, W16, W20, W21, W22, W24). W23 is excluded because it is retracted and not research output.
**Q12.** Full 3, fractional 2.0. The 2024 works are W20, W21 and W22, worth 0.5, 0.5 and 1.
**Q13.** Full: I09, with 4 works (W21, W27, W28, W29) against 3 for I07. Fractional: I07, with 2.0 against 1.0 for I09.
**Q14.** Full 7 (W06, W12, W13, W28, W29, W71, W72). Fractional 6.0, where W28 and W29 give 0.5 each and the other five give 1 each.
**Q15.** 4 (W12, W21, W28, W51). W03 is dated 2023.
**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).
**Q17.** W04 (EDT) and W05 (ERR).
**Q18.** 4 (W01, W03, W13, W72).
**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18).
**Q20.** None. W02 and W42 are merged into W03 and W31 and do not appear as separate works. W18 is a preprint, but it is not merged into any work in the data.
**Q21.** 4 (W27, W31, W39, W50).
**Q22.** W30 has more in total, with 5 against 4. W31 has more within its window, with 4 against 1. W30's window is 2019–2021 and only W60 falls in it. W31's window is 2023–2025 and W62, W65, W66 and W67 all fall in it.
**Q23.** Total 5 (W60–W64). In the window, 1 (W60).
**Q24.** 3 (W20, W21, W22).
**Q25.** 6, from W20 with 3, W21 with 2 and W22 with 1.
**Q26.** No. W23 is retracted and is not research output.
**Q27.** I12, with 3 citing works (W33, W34, W35). I09 and I11 have 1 each.
**Q28.** 1 (W32).
**Q29.** Author level 2 (W12, W13). University of Albury level 2 (W12, W13). Country level 4 (W12, W13, W14, W15, all GB).
**Q30.** 3 (W12, W13, W14).
**Q31.** W50, W51, W52 (via W40 and W41).
**Q32.** 5 (W40, W41, W50, W51, W52).
**Q33.** W20, with 3 citations.
**Q34.** 3 (W08, W16, W24).
**Q35.** 2 (W21, W24).
**Q36.** 2 (W17, W24). W76 is an editorial and does not count.
**Q37.** I06.
**Q38.** I04, I03, I02, I01.
**Q39.** 3 (W01, W13, W71). S01 is the top tier.
**Q40.** S01 (rank 1).
**Q41.** No. S03 has rank 3 and S02 has rank 2, so S03 is lower.
**Q42.** 0. S04 is delisted, so its works are not research output.
**Q43.** No. W07 is in the delisted S04.
**Q44.** I02, I03, I04, I05. I06 has I02 as its parent_id, but institution_units does not roll it up into I02 or I01.
**Q45.** 3 (W70, W73, W74).
**Q46.** I06. Its parent_id is I02, but institution_units counts it only towards itself, so it does not roll up to I01.
**Q47.** Rostval has more works under full counting (4 against 3) because W27, W28 and W29 each have I09 credited. Those works have four authors from different institutions, so Rostval gets only 0.25 each, giving 1.0 in total. Kesting's solo-authored W22 gives it a full 1, and it totals 2.0.
**Q48.** I06 is an affiliate (AFF), not a unit of I02. institution_units lists it as counting only towards itself, so W70 does not roll up to the University of Albury.

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":3,"fractional":2.0},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6.0},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":[]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I06"}}
```