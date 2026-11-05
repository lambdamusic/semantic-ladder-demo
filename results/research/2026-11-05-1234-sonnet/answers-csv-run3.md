**Q1.** 2. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person. The other "M. Ellison" (A04) has a different ORCID.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. Mara Ellison's records A01, A02 (W02, W07, W19) and A03 (W03) are the same person. A04's W08 and W16 are not hers.

**Q3.** No. W37 is by A05 and W38 by A06, and their ORCIDs differ.

**Q4.** 2. A05 authored W14 and W37, both articles.

**Q5.** No. W08's author is A04, whose ORCID differs from A01's.

**Q6.** A01, with 6 works: W01, W03, W06, W07, W12, W19. A07 and A08 have 4 each.

**Q7.** 6: W01, W03, W06, W07, W12, W19. I did not count W02 because it is a preprint of W03, and W04 and W05 are not research types.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 12: W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74. The units I03, I04 and I06 are included.

**Q10.** 16. This is the 12 above plus I05's W14, W28, W29 and W37.

**Q11.** 6: W08, W16, W20, W21, W22, W23. W24 is a supplement (SUP) and W90–W92 are staging (STG) records, so I excluded them.

**Q12.** Full count 3 (W20, W21, W22). Fractional count 2.0: W20 gives 0.5, W21 gives 0.5 and W22 gives 1.

**Q13.** Full counting: I09, with 4 works (W21, W27, W28, W29) against 3 for I07. Fractional counting: I07, with 2.0 against 1.0 for I09, whose four works each give 0.25.

**Q14.** Full count 7 (W06, W12, W13, W28, W29, W71, W72). Fractional count 6.0: W28 and W29 give 0.5 each and the other five give 1 each.

**Q15.** 4: W12, W21, W28, W51.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74. I excluded W04 (editorial), W09 (PTX) and W91 (STG).

**Q17.** W04 (editorial, EDT) and W05 (erratum, ERR).

**Q18.** 4: W01, W03, W13, W72. W02 is a preprint of W03, and W05 is an erratum.

**Q19.** 7: W12, W13, W14, W15, W16, W17, W18. W15 cites both versions and is counted once.

**Q20.** W02 (preprint of W03) and W42 (preprint of W31). W18 has no `version_of`, so it is not one.

**Q21.** 4: W27, W31, W39, W50. W42 is the preprint of W31 and is not counted separately.

**Q22.** Total: W30, with 5 citations against 4 for W31 and W42 combined. Within the window: W31, with 4 against 1.

**Q23.** Total 5 (W60–W64). In the window 2019–2021: 1 (W60).

**Q24.** 4: W20, W21, W22, W23.

**Q25.** 7. W20 has 3 citations, W21 has 2, W22 has 1 and W23 has 1. I ignored citations from the staging records W90–W92.

**Q26.** Depends. W23 is an article but is flagged `is_retracted=true`, and the data gives no rule on whether retracted works count. My counts above include it.

**Q27.** I12, with 3 citing works (W33, W34, W35). I09, I11 and I14 have 1 each.

**Q28.** 1 (W32, which cites W20).

**Q29.** Author level 2 (W12, W13). University of Albury level 2 (W12, W13). Country level 4 (W12, W13, W14, W15, all GB). W16's author A04 is a different person from A01.

**Q30.** 3: W12, W13 and W14. W14 comes from I05, which is also in the Albury University System.

**Q31.** W50, W51, W52. W40 and W41 cite W01; W50 and W51 cite W40, and W51 and W52 cite W41. I excluded the staging record W90.

**Q32.** 5: W40, W41, W50, W51, W52.

**Q33.** W20, with 3 citations.

**Q34.** 2: W08 and W16.

**Q35.** 1 (W21). W24 is a supplement (SUP).

**Q36.** 0 on my assumption that SUP, a type the data does not define, is not research. W17 and W24 are SUP and W76 is an editorial. If SUP counted, the answer would be 2.

**Q37.** I04. W70 lists I04 first (`affil_seq` 1) and I06 second.

**Q38.** I06, I04, I03, I02, I01. W71 is credited to I06 and I04, which roll up to I02 and I03 and then to I01.

**Q39.** 4: W01, W13, W71, W74, all in S01. This assumes K3 is the highest tier.

**Q40.** S01 (K3), assuming a higher K number means a higher tier. The data does not state the tier direction, and K0 could instead be the top.

**Q41.** Depends on the tier direction. S03 is K1 and S02 is K2, so S03 is higher only if lower K numbers rank higher.

**Q42.** 2: W07 and W75.

**Q43.** Yes. W07 is an article (ART) in S04.

**Q44.** I02, I03, I04, I05, I06. I06 is typed AFF (affiliated), but its `parent_id` is I02, so I included it.

**Q45.** 4: W70, W71, W73, W74.

**Q46.** I01. The chain is I06 → I02 → I01.

**Q47.** I09 has more works (4 against 3) but they are all four-author papers, so each gives only 0.25 (1.0 in total). Kesting's W22 is single-author and its W20 and W21 give 0.5 each, for 2.0 in total.

**Q48.** The premise is wrong. I04 is under I03, which is under I02, so W70 is counted as a University of Albury work (it is in my 12 for Q9).

```json
{"Q1":{"count":2},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":7},"Q26":{"counts":"depends"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"depends"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```