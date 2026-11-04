**Assumptions:** Research works are types ART, REV and PPR. EDT, ERR, PTX and SUP are excluded. A preprint counts once with its published version (W02 with W03, W42 with W31). STG records (W90–W92) are treated as unpublished staging and excluded. The retracted W23 still counts. Institution units follow `parent_id`. The data does not define how the tier codes rank, so the tier answers are conditional.

**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 has a different ORCID, so it is someone else.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These come from A01 plus her variants A02 and A03. W08 and W16 belong to A04, a different person.

**Q3.** No. A05 and A06 have different ORCIDs.

**Q4.** 2. A05 wrote W14 and W37.

**Q5.** No. W08 is by A04, who has a different ORCID from A01.

**Q6.** A01 (Mara Ellison). Her research works credited to I02 or its units are W01, W03/W02, W06, W07, W12 and W19, which is 6. A07 and A08 have 4 each.

**Q7.** 6. W02 is a preprint of W03 and counts once, so the works are W01, W03, W06, W07, W12 and W19.

**Q8.** I01. The chain is I04, then I03, then I02, then I01.

**Q9.** 12: W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74. I02, I03, I04 and I06 are included.

**Q10.** 16. This adds W14, W28, W29 and W37 from I05 to the 12 above.

**Q11.** 6: W08, W16, W20, W21, W22, W23. W24 is SUP and W90–W92 are STG.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20, W21 and W22, with I07 shares of 0.5, 0.5 and 1.

**Q13.** Full counting favours I09 (4 works: W21, W27, W28, W29). Fractional counting favours I07 (2.0 against 1.0).

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 give GB half each, and the other five give GB a full share.

**Q15.** 4: W12, W21, W28, W51. W05 is ERR and W10 is PTX.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.

**Q17.** W04 (EDT) and W05 (ERR).

**Q18.** 4: W01, W03 (with W02), W13, W72. W05 is ERR.

**Q19.** 7: W12, W13, W14, W15, W16, W17, W18.

**Q20.** W02 (of W03) and W42 (of W31).

**Q21.** 4: W27, W31, W39, W50. W42 duplicates W31.

**Q22.** W30 has more in total (5 against 4). W31 has more within its window (4 against 1). The W31 count includes W42's citer W67.

**Q23.** Total 5 (W60–W64). In the 2019–2021 window, 1 (W60).

**Q24.** 4: W20, W21, W22, W23.

**Q25.** 7. W20 has 3 citations, W21 has 2, W22 has 1 (W34) and W23 has 1 (W39).

**Q26.** Yes. It is a retracted research article by I07, and the data has no rule removing retracted works. Its `is_retracted` flag is still available if you want to exclude it.

**Q27.** I12, with 3 citing works (W33, W34, W35). I11, I09 and I14 have 1 each.

**Q28.** 1. Only W32 cites Kesting work, namely W20.

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15). W16's author A04 is a different Ellison.

**Q30.** 3: W12, W13, W14. W14 is from I05, which sits under I01.

**Q31.** W50, W51, W52, W90.

**Q32.** 6: W40, W41, W50, W51, W52, W90.

**Q33.** W20, with 3 citations. W90–W92 are STG and not counted. Counting them would give W22 four.

**Q34.** 2: W08 and W16.

**Q35.** 1. Only W21. W24 is SUP.

**Q36.** 0. W17 and W24 are SUP and W76 is EDT.

**Q37.** I02. W70's single author lists I04 and I06 (both under I02), so it is credited once to the University of Albury.

**Q38.** I06, I04, I03, I02, I01. I04 and I06 are the direct credits, and the rest are the ancestors of I04.

**Q39.** 1 (W07 in S04). This assumes K0 is the top tier. If K3 were the top, the count would be 4.

**Q40.** S04. This is only valid if K0 is the top tier. The data does not state the ordering.

**Q41.** Depends. The ordering of K1 and K2 is not defined in the data.

**Q42.** 2: W07 and W75.

**Q43.** Yes. W07 is an ART.

**Q44.** I02, I03, I04, I05, I06.

**Q45.** 4: W70, W71, W73, W74.

**Q46.** I01. The chain is I06, then I02, then I01.

**Q47.** I09 has more 2024 works (4 against 3), but it is one of four authors on each. I07 has fewer works but larger shares, with sole authorship of W22 and half of W20 and W21.

**Q48.** The premise is wrong: W70 is one of the University of Albury's works. I04 rolls up through I03 to I02, so W70 counts for I02 along with I06.

```json
{
"Q1": {"count": 1},
"Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},
"Q3": {"same": "no"},
"Q4": {"count": 2},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 6},
"Q8": {"parent": "I01"},
"Q9": {"count": 12},
"Q10": {"count": 16},
"Q11": {"count": 6},
"Q12": {"full": 3, "fractional": 2},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 7, "fractional": 6},
"Q15": {"count": 4},
"Q16": {"count": 10},
"Q17": {"works": ["W04","W05"]},
"Q18": {"count": 4},
"Q19": {"count": 7},
"Q20": {"works": ["W02","W42"]},
"Q21": {"count": 4},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 5, "in_window": 1},
"Q24": {"count": 4},
"Q25": {"count": 7},
"Q26": {"counts": "yes"},
"Q27": {"institution": "I12", "citing_works": 3},
"Q28": {"count": 1},
"Q29": {"author": 2, "institution": 2, "country": 4},
"Q30": {"count": 3},
"Q31": {"works": ["W50","W51","W52","W90"]},
"Q32": {"count": 6},
"Q33": {"work": "W20"},
"Q34": {"count": 2},
"Q35": {"count": 1},
"Q36": {"count": 0},
"Q37": {"institution": "I02"},
"Q38": {"institutions": ["I06","I04","I03","I02","I01"]},
"Q39": {"count": 1},
"Q40": {"source": "S04"},
"Q41": {"higher": "depends"},
"Q42": {"count": 2},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06"]},
"Q45": {"count": 4},
"Q46": {"parent": "I01"}
}
```