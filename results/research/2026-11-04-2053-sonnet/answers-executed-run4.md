**Q1.** 2. A01 already merges A01, A02 and A03 (which would cover "Ellison, Mara J."), while A04 "M. Ellison" has a different ORCID and stays a separate person.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19, per the A01 credits (W03 also merges W02).

**Q3.** No. W37 is by A05 and W38 by A06, and they have different ORCIDs.

**Q4.** 2 (W14, W37).

**Q5.** No. W08 is by A04 and W01 by A01, and they have different ORCIDs.

**Q6.** A01. A01 has 5 research works credited to I02 or its units (W01, W03, W06, W12, W19), against 4 for A07.

**Q7.** 5 (W01, W03, W06, W12, W19). W04 and W05 are not research output, W07 is in a delisted source, and W08 belongs to A04.

**Q8.** I01 (I04 → I03 → I02 → I01).

**Q9.** 8 (W01, W03, W06, W12, W13, W19, W71, W72). I06 does not roll up into I02 according to institution_units.

**Q10.** 12: the 8 above plus the I05 works W14, W28, W29 and W37 (W12 is already counted).

**Q11.** 6 (W08, W16, W20, W21, W22, W24). W23 is retracted and not research output.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5) and W22 (1).

**Q13.** Full: I09 (4 works: W21, W27, W28, W29, against 3 for I07). Fractional: I07 (2.0 against 1.0 for I09).

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28, W29, W71 and W72; W28 and W29 count 0.5 each and the rest count 1 each.

**Q15.** 4 (W12, W21, W28, W51).

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74). W04 and W09 are excluded as non-research.

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded because its source is delisted, not because of its type.

**Q18.** 4 (W01, W03, W13, W72).

**Q19.** 7 (W12–W18).

**Q20.** W02 and W42, the preprint records merged into W03 and W31. W18 is a preprint but has no published version in the data.

**Q21.** 4 (W27, W31, W39, W50).

**Q22.** In total, W30 has more (5 against 4). Within publication year plus two years, W31 has more (4 against 1).

**Q23.** 5 in total (W60–W64), and 1 in the window (W60, 2020).

**Q24.** 3 (W20, W21, W22). W23 is excluded.

**Q25.** 6: W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted and not research output.

**Q27.** I12, with 3 citing works (W33, W34, W35).

**Q28.** 1 (W32).

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15).

**Q30.** 3 (W12, W13, W14, where W14 comes through I05).

**Q31.** W50, W51, W52.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20, with 3 citations.

**Q34.** 3 (W08, W16, W24).

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24). W76 is an editorial.

**Q37.** I06.

**Q38.** I04, I03, I02, I01.

**Q39.** 3 (W01, W13, W71, all in S01).

**Q40.** S01.

**Q41.** No. S03 has tier_rank 3 and S02 has rank 2, so S02 is higher.

**Q42.** 0. S04 is delisted, so its works are not research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05. I06 has I02 as its parent_id but does not count towards it in institution_units, so I left it out.

**Q45.** 3 (W70, W73, W74).

**Q46.** I06. Its parent_id is I02, but institution_units shows it counting only towards itself. If parent_id alone is followed, the answer would be I01.

**Q47.** Under full counting, I09 has 4 works to I07's 3. Under fractional counting, I09 holds only one of four authors on each of its works (1.0 in total), while I07 has the sole-authored W22 and half of W20 and W21 (2.0).

**Q48.** W70 is credited to I06, an affiliated institution that, per institution_units, counts only towards itself and not towards I02. The Tessel Laboratory (I04) is credited on W71 and W72, not W70.

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":3,"fractional":2.0},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6.0},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I06"}}
```