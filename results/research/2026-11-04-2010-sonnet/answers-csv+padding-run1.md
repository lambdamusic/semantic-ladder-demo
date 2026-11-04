Assumptions, since the data doesn't define these terms:
- "Research works" means ART, REV and PPR. A preprint is merged with its published version through `version_of`, so W02 and W03 count once. EDT, ERR, PTX and SUP are excluded.
- W23 is retracted but still counted. The data doesn't say how retractions are treated.
- STG records (W90–92) are treated as unpublished staging and left out of research counts. They are kept where a question is about citations in general, as in Q31–32.
- Institution roll-ups follow `parent_id`, so I06 counts as part of I02 and I01 even though its type is AFF.
- Tier order isn't defined. I read K3 as the highest, but K0 could be the top tier.

**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 has a different ORCID, so it is a different person.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01, A02 and A03.

**Q3.** No. A05 (W37) and A06 (W38) have different ORCIDs.

**Q4.** 2. A05 wrote W14 and W37.

**Q5.** No. W08 is by A04, whose ORCID differs from A01's.

**Q6.** A01. Ellison has 6 University of Albury works (W01, W03, W06, W07, W12, W19). A07 and A08 have 4 each.

**Q7.** 6. These are W01, W03 (merged with its preprint W02), W06, W07, W12 and W19. W04 and W05 are excluded.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 12. These are W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73 and W74.

**Q10.** 16. These are the 12 above plus W14, W28, W29 and W37 from I05.

**Q11.** 6. These are W08, W16, W20, W21, W22 and W23. W24 is SUP and W90–92 are STG.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5) and W22 (1).

**Q13.** Full: I09, with 4 works (W21, W27, W28, W29) against 3 for Kesting. Fractional: I07, with 2.0 against 1.0 for Rostval.

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W71 and W72 (1 each), plus W28 and W29 (0.5 each).

**Q15.** 4. These are W12, W21, W28 and W51.

**Q16.** 10. These are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74. W04 is EDT, W09 is PTX and W91 is STG.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4. These are W01, W03 (with W02), W13 and W72. W05 is an erratum.

**Q19.** 7. These are W12, W13, W14, W15, W16, W17 and W18.

**Q20.** W02 (of W03) and W42 (of W31).

**Q21.** 4. These are W27, W31 (with W42), W39 and W50.

**Q22.** W30 has more in total (5 against 4). W31 has more within its window (4 against 1). W30 is cited by W60–W64, and the 2019–2021 window catches only W60. W31 plus W42 are cited by W62, W65, W66 and W67, all in 2023–2025.

**Q23.** Total 5, in window 1.

**Q24.** 4. These are W20, W21, W22 and W23.

**Q25.** 7. W20 has 3 citations, W21 has 2, W22 has 1 (W34) and W23 has 1. This excludes the staged W90–92 citations of W22.

**Q26.** Depends. W23 is an ART from Kesting, but it is flagged retracted and the data gives no policy on retractions.

**Q27.** I12, with 3 citing works: W33, W34 and W35.

**Q28.** 1. Only W32 does.

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15).

**Q30.** 3. These are W12, W13 and W14.

**Q31.** W50, W51, W52, W90. W01 is cited by W40 and W41, and these four cite one of them.

**Q32.** 6. These are W40, W41, W50, W51, W52 and W90.

**Q33.** W20, with 3 citations.

**Q34.** 2. These are W08 and W16.

**Q35.** 1. Only W21 counts, because W24 is SUP.

**Q36.** 0. S06 holds only W17 and W24 (SUP) and W76 (EDT).

**Q37.** I04. It is listed first (affil_seq 1) and I06 second.

**Q38.** I06, I04, I03, I02, I01. I06 and I04 are listed directly, and I04 rolls up to I03, I02 and I01.

**Q39.** 4. These are W01, W13, W71 and W74 in S01 (K3), taking K3 as highest.

**Q40.** S01 (K3). If K0 is the top tier, it would be S04.

**Q41.** Depends. The tier order isn't defined: K1 is higher than K2 only if K0 is the top tier.

**Q42.** 2. These are W07 and W75.

**Q43.** Yes. W07 is an ART.

**Q44.** I02, I03, I04, I05, I06.

**Q45.** 4. These are W70, W71, W73 and W74.

**Q46.** I01. The chain is I06 → I02 → I01. Its type is AFF (affiliate), so it is only a parent by the `parent_id` link.

**Q47.** Rostval has more works (4 against 3), but each is shared among four authors, so each earns only 0.25 (1.0 in total). Kesting's W22 is single-authored and W20 and W21 give 0.5 each, for 2.0.

**Q48.** The premise doesn't hold. W70 lists I04 (Tessel) first, and I04 rolls up through I03 to I02, so it is a University of Albury work (counted in Q9).

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2.0},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6.0},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":7},"Q26":{"counts":"depends"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52","W90"]},"Q32":{"count":6},"Q33":{"work":"W20"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"depends"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```