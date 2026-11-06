**Q1.** 2. A01 merges "Mara Ellison" and "Ellison, Mara J." (author_ids A01 A02 A03), and "M. Ellison" is A04 with a different ORCID.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are the credits for A01. W03 also stands for the merged record W02.

**Q3.** No. W37 is by A05 and W38 by A06, and their ORCIDs differ.

**Q4.** 2 (W14, W37).

**Q5.** No. W08 is by A04 and W01 by A01, who are separate people with different ORCIDs.

**Q6.** A01. A01 has 5 research works credited to I02 or its units (W01, W03, W06, W12, W19), against 4 for A07 and 2 for A08.

**Q7.** 5 (W01, W03, W06, W12, W19).

**Q8.** I01 (I04 → I03 → I02 → I01).

**Q9.** 8 (W01, W03, W06, W12, W13, W19, W71, W72), counting I02, I03 and I04.

**Q10.** 12. These are the 8 from Q9 plus W14, W28, W29 and W37 via I05.

**Q11.** 6 (W08, W16, W20, W21, W22, W24). W23 is excluded because it is retracted and not research output.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20, W21 and W22. W20 gives 0.5, W21 gives 0.25 + 0.25 because both A09 (I07) and A10 (I08) count towards I07, and W22 gives 1.

**Q13.** Full: I09, with 4 works (W21, W27, W28, W29) against 3 for I07. Fractional: I07, with 2.0 against 1.0 for I09.

**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 each contribute 0.5 and the other five contribute 1 each.

**Q15.** 4 (W12, W21, W28, W51).

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded only because its source is delisted, not because of its type.

**Q18.** 4 (W01, W03, W13, W72).

**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18), citing the merged work W03/W02.

**Q20.** None. W18 has the preprint type, but no published version of it is in the data. The merged preprints W02 and W42 are already folded into W03 and W31.

**Q21.** 4 (W27, W31, W39, W50).

**Q22.** In total, W30 has 5 citations against 4 for W31. Within the window, W31 has 4 against 1 for W30.

**Q23.** 5 in total, and 1 in the window (W60 in 2020).

**Q24.** 3 (W20, W21, W22).

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted and is not research output.

**Q27.** I12, with 3 citing works (W33, W34, W35).

**Q28.** 1 (W32).

**Q29.** Author 2, institution 2, country 4. At author and institution level the self-citing works are W12 and W13. At country level (GB) they are W12, W13, W14 and W15.

**Q30.** 3 (W12, W13, W14).

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and those two are cited by W50, W51 and W52.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20, with 3 citations.

**Q34.** 3 (W08, W16, W24).

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24). W76 is an editorial and does not count.

**Q37.** I06.

**Q38.** I04, I03, I02, I01.

**Q39.** 3 (W01, W13, W71), all in S01.

**Q40.** S01.

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, so S03 is lower.

**Q42.** 0. S04 is delisted, and its only works (W07, W75) are not research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05. I06 counts only towards itself.

**Q45.** 3 (W70, W73, W74).

**Q46.** I06. It is an affiliated institution whose institution_units row counts only towards itself. Its parent_id lists I02, but that is an affiliation and not a roll-up. If you read parent_id literally, the answer would be I01.

**Q47.** Rostval has more works in full counting (4 against 3), but each of its works is shared among 4 authors, so it gets 1.0 in fractional counting. Kesting has the sole-author W22 and half of W20, which gives it 2.0.

**Q48.** A08 is credited on W70 to I06, the Halloran Institute, not to the Tessel Laboratory (I04, which appears on W71 and W72). I06 is an affiliated institution that counts only towards itself, so W70 does not roll up to I02.

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":5},"Q8":{"parent":"I01"},"Q9":{"count":8},"Q10":{"count":12},"Q11":{"count":6},"Q12":{"full":3,"fractional":2.0},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":[]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":3},"Q25":{"count":6},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":3},"Q35":{"count":2},"Q36":{"count":2},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":3},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05"]},"Q45":{"count":3},"Q46":{"parent":"I06"}}
```