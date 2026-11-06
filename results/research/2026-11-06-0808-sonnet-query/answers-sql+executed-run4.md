**Q1.** 2. The records A01, A02 and A03 are merged into person A01, which has one ORCID. "M. Ellison" is person A04, with a different ORCID.

**Q2.** W01, W03, W04, W05, W06, W07, W12 and W19. These are all of A01's credited works, whatever their type.

**Q3.** No. The W37 Jonas Brandt is A05 (ORCID 0000-0001-6105-5008, I05) and the W38 one is A06 (ORCID 0000-0007-5475-1779, I12). They are different people.

**Q4.** 2. A05 has W14 and W37, and both are research output.

**Q5.** No. The M. Ellison of W08 is A04 (ORCID 0000-0004-8662-8360). Mara Ellison of W01 is A01, who has a different ORCID.

**Q6.** A01. Counting I02, I03 and I04, A01 has 5 research works (W01, W03, W06, W12, W19), A07 has 4 and A08 has 2. I06 does not roll up into I02.

**Q7.** 5. These are W01, W03, W06, W12 and W19. W04 and W05 are not research output by type, and W07 is not because S04 is delisted.

**Q8.** I01. The chain is I04, then I03, I02 and I01.

**Q9.** 8. They are W01, W03, W06, W12, W13, W19, W71 and W72, credited to I02, I03 or I04.

**Q10.** 12. These are the 8 above plus the I05 works W14, W28, W29 and W37.

**Q11.** 6. These are W08, W16, W20, W21, W22 (I07) and W24 (I08). W23 is excluded because it is not research output.

**Q12.** Full 3, fractional 2.0. In 2024 Kesting has W20 (1/2), W21 (I07 and I08 each hold 1 of 4 shares, so 2/4) and W22 (1), which sum to 2.0.

**Q13.** Full: I09, with 4 works (W21, W27, W28, W29) against Kesting's 3. Fractional: I07, with 2.0 against Rostval's 1.0 (a quarter of each of those four works).

**Q14.** Full 7, fractional 6.0. The GB works are W06, W12, W13, W71 and W72 (1 each), plus W28 and W29 (0.5 each).

**Q15.** 4. These are W12, W21, W28 and W51.

**Q16.** 10. These are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4. These are W01, W03, W13 and W72. W05 is an erratum, so it does not count.

**Q19.** 7. The citing works are W12, W13, W14, W15, W16, W17 and W18.

**Q20.** W02 and W42, with a caveat. They are the records merged into W03 and W31, so they no longer exist as separate works. W18 is typed as a preprint (PPR) but has no published version in the data.

**Q21.** 4. These are W27, W31, W39 and W50.

**Q22.** In total W30 has more (5 against 4). Within its publication year and the two years after, W31 has more (4 against 1).

**Q23.** Total 5 (W60 to W64). In the window 2019–2021 it has 1 (W60).

**Q24.** 3. These are W20, W21 and W22. W23 is retracted and not research output.

**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).

**Q26.** No. W23 is retracted and flagged research_output = no.

**Q27.** I12, with 3 citing works (W33, W34, W35).

**Q28.** 1. Only W32 does.

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15, all GB).

**Q30.** 3. These are W12, W13 and W14, the last via I05.

**Q31.** W50, W51 and W52. The works citing W01 are W40 and W41.

**Q32.** 5. These are W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations.

**Q34.** 3. These are W08, W16 and W24.

**Q35.** 2. These are W21 and W24.

**Q36.** 2. These are W17 and W24. W76 is an editorial.

**Q37.** I06.

**Q38.** I04, I03, I02 and I01.

**Q39.** 3. These are W01, W13 and W71, all in S01, the top tier.

**Q40.** S01.

**Q41.** No. S03 has tier rank 3 and S02 has rank 2, and rank 1 is the highest.

**Q42.** 0. S04 is delisted, so W07 and W75 are not research output.

**Q43.** No. W07 is in the delisted S04.

**Q44.** I02, I03, I04 and I05. I06 has I02 as its parent_id, but it is an affiliate (AFF) type and institution_units does not roll its works up, so I excluded it.

**Q45.** 3. These are W70, W73 and W74.

**Q46.** I06. It is an affiliate whose works count only towards itself, although its parent_id field says I02. If you read parent_id literally, the answer would be I01.

**Q47.** Rostval has more works in 2024 (4 against 3), but its shares are thin: each of its four works is split four ways, giving 1.0. Kesting has W22 sole-authored and half of W20, giving 2.0.

**Q48.** W70 is credited to the Halloran Institute (I06), an affiliate whose works do not count towards I02. Tessel (I04) appears on W71 and W72, not W70.

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I06"}}
```