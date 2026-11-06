**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 ("M. Ellison") has a different ORCID.
**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01 (W01, W04, W05, W06, W12), A02 (W02, W07, W19) and A03 (W03).
**Q3.** No. A05 and A06 have different ORCIDs.
**Q4.** 2 (W14, W37).
**Q5.** No. W08's M. Ellison is A04, whose ORCID differs from Mara's.
**Q6.** A01 (Mara, via A01/A02/A03) has 6 research works: W01, W03, W06, W07, W12, W19. A07 and A08 have 4 each.
**Q7.** 6. W02 is a preprint of W03 and counted once; W04 and W05 are not research types.
**Q8.** I01 (I04 → I03 → I02 → I01).
**Q9.** 12: W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74.
**Q10.** 16. These are the 12 above plus W14, W28, W29, W37 via I05.
**Q11.** 9: W08, W16, W20, W21, W22, W23, W90, W91, W92. This includes retracted W23 and the STG-sourced W90–W92.
**Q12.** Full 3, fractional 2.0. W20 gives 0.5, W21 gives 0.5 (I07 + I08) and W22 gives 1.
**Q13.** Full: I09 (4 works against 3). Fractional: I07 (2.0 against 1.0).
**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W71 and W72 (1 each), plus W28 and W29 (0.5 each).
**Q15.** 4 (W12, W21, W28, W51).
**Q16.** 11 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74, W91). W04 and W09 are excluded by type, and W42 is merged into W31.
**Q17.** W04 (editorial) and W05 (erratum).
**Q18.** 4 (W01, W03/W02, W13, W72). W05 is an erratum.
**Q19.** 7: W12, W13, W14, W15, W16, W17, W18.
**Q20.** W02 (of W03) and W42 (of W31).
**Q21.** 4 (W27, W31, W39, W50). W42 is merged into W31.
**Q22.** Total: W30 (5 against 4). Within the window: W31 (4 against 1).
**Q23.** Total 5 (W60–W64). Within 2019–2021, 1 (W60).
**Q24.** 4 (W20, W21, W22, W23).
**Q25.** 10. The counts are W20 = 3, W21 = 2, W22 = 4, W23 = 1.
**Q26.** Yes. W23 is a research article that is flagged retracted; excluding retracted works would be a policy choice the data doesn't state.
**Q27.** I12, with 3 works (W33, W34, W35). The other citing institutions have one each: I09, I11, I14.
**Q28.** 1 (W32).
**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15, all GB).
**Q30.** 3 (W12, W13, W14).
**Q31.** W50, W51, W52, W90. W01 is cited by W40 and W41.
**Q32.** 6 (W40, W41, W50, W51, W52, W90).
**Q33.** W22, with 4 citations (W34, W90, W91, W92). W20 has 3.
**Q34.** 5 (W08, W16, W90, W91, W92).
**Q35.** 1 (W21). W24 is a supplementary item, not research.
**Q36.** 0. W17 and W24 are SUP and W76 is EDT.
**Q37.** I04, its first-listed affiliation. I06 is also listed, second.
**Q38.** I06, I04, I03, I02, I01.
**Q39.** 4 (W01, W13, W71, W74), assuming K3 is the top tier.
**Q40.** S01 (K3). This assumes a higher K number means a higher tier, which the data doesn't state.
**Q41.** No. Under that same assumption K1 is below K2.
**Q42.** 2 (W07, W75).
**Q43.** Yes. W07 is an article (ART), though its source S04 sits in the K0 tier.
**Q44.** I02, I03, I04, I05, I06.
**Q45.** 4 (W70, W71, W73, W74).
**Q46.** I01 (I06 → I02 → I01).
**Q47.** Rostval has more 2024 works (4 against 3), but only as one co-author among several on each. Kesting has fewer works but larger author shares (W22 is sole-authored, and W20 and W21 are shared with other institutions), so it leads on fractional counting.
**Q48.** The premise is wrong: W70 is one of the University of Albury's works. Its first affiliation I04 rolls up through I03 to I02, and the data would only exclude it if the hierarchy were ignored.

Assumptions: STG-sourced W90–W92 are counted, preprints are merged into their published version, and retracted W23 still counts.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":9},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":11},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":10},"Q26":{"counts":"yes"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52","W90"]},"Q32":{"count":6},"Q33":{"work":"W22"},"Q34":{"count":5},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```