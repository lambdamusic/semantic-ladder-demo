**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person. A04 is a different "M. Ellison" with another ORCID.
**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These come from A01 (W01, W04, W05, W06, W12), A02 (W02, W07, W19) and A03 (W03).
**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.
**Q4.** 2. A05 wrote W14 and W37.
**Q5.** No. W08 is by A04 (ORCID 0000-0004-8662-8360), not the Mara Ellison ORCID.
**Q6.** A01 (Mara Ellison), with 6 distinct research works: W01, W03 (W02 is its preprint), W06, W07, W12, W19. A08 has 4 and A07 has 4.
**Q7.** 6. The research works are W01, W03, W06, W07, W12 and W19. W02 is a preprint of W03, so it is the same work. W04 (editorial) and W05 (erratum) are not research.
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9.** 12: W01, W03 (with W02), W06, W07, W12, W13, W19, W70, W71, W72, W73, W74.
**Q10.** 16: the 12 from Q9 plus W14, W28, W29, W37 via I05.
**Q11.** 6: W08, W16, W20, W21, W22, W23. W24 is a supplement, and W90–W92 are staging (STG) records, so I excluded them. W23 is retracted but still counted.
**Q12.** Full 3 and fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5) and W22 (1).
**Q13.** Full counting: I09 (4 works, W21, W27, W28, W29). Fractional counting: I07 (2.0 vs 1.0).
**Q14.** Full 7 and fractional 6.0. The works are W06, W12, W13, W28, W29, W71, W72, with shares 1, 1, 1, 0.5, 0.5, 1, 1.
**Q15.** 4: W12, W21, W28, W51. W05 is an erratum and W10 is front matter.
**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74. W91 is staging, and W04 and W09 are not research.
**Q17.** W04 (editorial) and W05 (erratum).
**Q18.** 4: W01, W03 (with its preprint W02), W13, W72.
**Q19.** 7: W12, W13, W14, W15, W16, W17, W18. W15 cites both versions but is counted once.
**Q20.** W02 (preprint of W03) and W42 (preprint of W31). W18 has no `version_of`.
**Q21.** 4: W27, W31 (with W42), W39, W50.
**Q22.** In total W30 has more (5 vs 4). Within its publication year and the two years after, W31 has more (4 vs 1). W31 plus W42 are cited by W62, W65, W66, W67.
**Q23.** Total 5 (W60–W64). Within 2019–2021, only W60 (2020), so 1.
**Q24.** 4: W20, W21, W22, W23.
**Q25.** 10. W20 has 3 citations, W21 has 2, W22 has 4 (including the staging works W90–W92) and W23 has 1.
**Q26.** Depends. W23 is an article credited to I07, but it is flagged `is_retracted`, and the data doesn't say whether retractions are excluded.
**Q27.** I12, with 3 citing works: W33, W34, W35.
**Q28.** 1: W32.
**Q29.** Authors 2 (W12, W13), University of Albury 2 (W12, W13), countries 4 (W12, W13, W14, W15, all GB).
**Q30.** 3: W12, W13, W14.
**Q31.** W50, W51, W52, W90. W01 is cited by W40 and W41.
**Q32.** 6: W40, W41, W50, W51, W52, W90.
**Q33.** W22, with 4 citations (W20 has 3).
**Q34.** 2: W08 and W16.
**Q35.** 1: W21. W24 is a supplement.
**Q36.** 0. S06 holds W17 and W24 (supplements) and W76 (editorial).
**Q37.** I04, the first-listed affiliation. W70 also lists I06 second.
**Q38.** I06, I04, I03, I02, I01. I06 and I04 are listed directly, and I03, I02, I01 are their ancestors.
**Q39.** 4: W01, W13, W71, W74. This assumes K3 is the highest tier, which the data doesn't state.
**Q40.** S01 (K3), under the same assumption that a higher K number means a higher tier.
**Q41.** Depends. S03 is K1 and S02 is K2, and the data doesn't say whether a higher K number is better.
**Q42.** 2: W07 and W75.
**Q43.** Yes. W07 is an article (ART).
**Q44.** I02, I03, I04, I05, I06. I06 is typed AFF (affiliated) but has I02 as its parent.
**Q45.** 4: W70, W71, W73, W74.
**Q46.** I01. The chain is I06 → I02 → I01.
**Q47.** Rostval has more works in 2024 (4 vs 3), but each is one of four authors, so it gets only 0.25 per work (1.0 in total). Kesting has the sole-authored W22 and half of W20 and W21, giving 2.0.
**Q48.** The premise is wrong: W70 is one of the University of Albury's research works. I04 sits under I03, which sits under I02, and W70 is an article, so it counts. Only the first-listed affiliation (I04) gives it directly to the Tessel Laboratory.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":10},"Q26":{"counts":"depends"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52","W90"]},"Q32":{"count":6},"Q33":{"work":"W22"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"depends"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```