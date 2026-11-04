**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 is a different "M. Ellison" with a different ORCID.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. I read this as the person behind A01, A02 and A03. A01's own record alone covers only W01, W04, W05, W06 and W12.

**Q3.** No. A05 and A06 have different ORCIDs.

**Q4.** 2 (W14, W37).

**Q5.** No. A04 (W08) has a different ORCID from A01.

**Q6.** A01 (Mara Ellison, via A01/A02/A03). She has 6 research works under I02 and its units: W01, W03, W06, W07, W12, W19. A07 and A08 have 4 each.

**Q7.** 6 (W01, W03, W06, W07, W12, W19). W02 is a preprint of W03 and counts once. W04 (editorial) and W05 (erratum) are not research.

**Q8.** I01 (I04 → I03 → I02 → I01).

**Q9.** 12 (W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74). This assumes I06, an AFF-type unit, rolls up into I02. Without I06 the count would be 10.

**Q10.** 16. These are the 12 above plus W14, W28, W29, W37 from I05.

**Q11.** 6 (W08, W16, W20, W21, W22, W23). I excluded W24 (SUP). I also excluded W90–92, which are STG (staging) records.

**Q12.** Full 3, fractional 2.0. The works are W20 (0.5), W21 (0.5) and W22 (1).

**Q13.** Full: I09 (4 works: W21, W27, W28, W29). Fractional: I07 (2.0 vs 1.0).

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W71, W72 (1 each) and W28, W29 (0.5 each).

**Q15.** 3 (W12, W21, W28). W05 (erratum) and W10 (front matter) are not research.

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74). I excluded W04 and W09 by type, and W91 as a staging record.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4 (W01, W03/W02, W13, W72).

**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18). W15 cites both versions.

**Q20.** W02 (of W03) and W42 (of W31).

**Q21.** 4 (W27, W31, W39, W50). W42 is a preprint of W31 and is collapsed into it.

**Q22.** Total: W30 (5 vs 4). Within the publication year and two years after: W31 (4 vs 1).

**Q23.** Total 5 (W60–W64). In the window 1 (W60, 2020).

**Q24.** 4 (W20, W21, W22, W23).

**Q25.** 7: W20 has 3, W21 has 2, W22 has 1 and W23 has 1. This excludes the staging records W90–92, which would add 3 more citations to W22.

**Q26.** Yes. W23 is flagged retracted, but it is still a research article in the record. Dropping retracted works would be a policy choice the data doesn't make.

**Q27.** I12 with 3 citing works (W33, W34, W35).

**Q28.** 1 (W32).

**Q29.** Author level 2 (W12, W13), University of Albury 2 (W12, W13), country 4 (W12, W13, W14, W15). W16 is by a different M. Ellison (A04), so it is not a self-citation.

**Q30.** 3 (W12, W13, W14, which includes I05).

**Q31.** W50, W51, W52. W90 also cites W41 but is a staging record.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20 (3 citations: W32, W35, W36).

**Q34.** 2 (W08, W16).

**Q35.** 1 (W21). W24 is SUP.

**Q36.** 0. W17 and W24 are SUP and W76 is EDT.

**Q37.** I04, listed first (affil_seq 1). I06 is a second affiliation (affil_seq 2).

**Q38.** I01, I02, I03, I04, I06. W71 lists I06 and I04, and I04 sits under I03 → I02 → I01.

**Q39.** 1 (W07), assuming K0 is the highest tier. If K3 is highest, the count is 4. The data doesn't define tier order.

**Q40.** S04, assuming K0 is the highest tier. The data doesn't define the order, so S01 (K3) is the alternative.

**Q41.** Depends. The data doesn't say whether K1 or K2 ranks higher.

**Q42.** 2 (W07, W75).

**Q43.** Yes. W07 is an article (ART).

**Q44.** I02, I03, I04, I05, I06.

**Q45.** 4 (W70, W71, W73, W74).

**Q46.** I01 (I06 → I02 → I01), following parent_id. I06 is typed AFF (affiliate), so this depends on whether an affiliate counts as part of its parent.

**Q47.** Rostval has more works in full counting (4 vs 3). In each of W21, W27, W28 and W29 it is only one of four authors, so it earns 0.25 per work (1.0 total). Kesting has W22 alone (1) plus half of W20 and W21, giving 2.0.

**Q48.** The premise is wrong. I04 sits under I03, which sits under I02, so W70 does count as a University of Albury work, and it is included in Q9.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":3},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":7},"Q26":{"counts":"yes"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I01","I02","I03","I04","I06"]},"Q39":{"count":1},"Q40":{"source":"S04"},"Q41":{"higher":"depends"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```