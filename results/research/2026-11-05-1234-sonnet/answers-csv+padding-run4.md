**Q1.** 2. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person. A04 ("M. Ellison") has a different ORCID, so it is a second person.
**Q2.** Nine works: W01, W02, W03, W04, W05, W06, W07, W12, W19. A01, A02 and A03 are one person, and W02, W07 and W19 sit under A02 and W03 under A03.
**Q3.** No. A05 wrote W37 and A06 wrote W38, and their ORCIDs differ.
**Q4.** 2 (W14, W37).
**Q5.** No. W08 is by A04, whose ORCID differs from Mara Ellison's.
**Q6.** A01 (Mara Ellison, via A01/A02/A03) has 6 Albury works: W01, W03 (merged with W02), W06, W07, W12, W19. A08 and A07 each have 4.
**Q7.** 6. W04 (editorial) and W05 (erratum) are not research, and W02 is the preprint version of W03.
**Q8.** I01. I04 sits under I03, which sits under I02, which sits under I01.
**Q9.** 12: W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74.
**Q10.** 16. Those 12 plus the I05 works W14, W28, W29 and W37.
**Q11.** 6: W08, W16, W20, W21, W22, W23.
**Q12.** Full 3, fractional 2.0. The works are W20 (0.5), W21 (0.5) and W22 (1).
**Q13.** Full counting: I09, with 4 works (W21, W27, W28, W29) against 3. Fractional counting: I07, with 2.0 against 1.0.
**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28 (0.5), W29 (0.5), W71 and W72.
**Q15.** 4 (W12, W21, W28, W51).
**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).
**Q17.** W04 (EDT) and W05 (ERR).
**Q18.** 4 (W01, W03/W02, W13, W72). W05 is an erratum.
**Q19.** 7 (W12–W18).
**Q20.** W02 (of W03) and W42 (of W31).
**Q21.** 4 (W27, W31 with W42 as its preprint, W39, W50).
**Q22.** In total W30 has more, 5 against 4. Within its publication year and the two years after, W31 has more, 4 against 1.
**Q23.** Total 5 (W60–W64). In window 1 (W60, 2020).
**Q24.** 4 (W20, W21, W22, W23).
**Q25.** 7. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36), W22 has 1 (W34) and W23 has 1 (W39).
**Q26.** Yes. W23 is a retracted article, but nothing in the data excludes retracted works from the count.
**Q27.** I12, with 3 citing works (W33, W34, W35).
**Q28.** 1 (W32).
**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15, all GB).
**Q30.** 3 (W12, W13, W14).
**Q31.** W50, W51, W52.
**Q32.** 5 (W40, W41, W50, W51, W52).
**Q33.** W20, with 3 citations.
**Q34.** 2 (W08, W16).
**Q35.** 1 (W21). W24 is a supplement.
**Q36.** 0. W17 and W24 are SUP and W76 is EDT.
**Q37.** I04, listed first for A08 on W70 (affil_seq 1). I06 is also listed, at affil_seq 2.
**Q38.** I06 and I04, plus their parents I03, I02 and I01.
**Q39.** 1 (W07), if K0 is the top tier.
**Q40.** The data doesn't say whether K0 or K3 is the top tier. I give S04 (K0) provisionally. If K3 is the top, it is S01.
**Q41.** Depends on the tier ordering: K1 outranks K2 only if lower numbers are better.
**Q42.** 2 (W07, W75).
**Q43.** Yes. W07 is an ART.
**Q44.** I02, I03, I04, I05, I06. I06 is typed AFF but has parent I02.
**Q45.** 4 (W70, W71, W73, W74).
**Q46.** I01.
**Q47.** Under full counting, Rostval has 4 works against Kesting's 3. Under fractional counting, each Rostval work has four authors with only one at Rostval (4 × 0.25 = 1.0). Kesting's W22 is single-authored, so it scores 2.0.
**Q48.** The premise is wrong. W70 is a University of Albury work, because I04 sits under I03, which sits under I02, and its other listed affiliation, I06, is also under I02.

I excluded EDT, ERR, PTX and SUP types as non-research. I counted W02/W03 and W31/W42 once each. I also excluded the STG-sourced records W90–W92, because I read STG as staging, which the data does not define. Counting them would change Q11 (to 9), Q16, Q25, Q31, Q32 and Q34.

```json
{
"Q1": {"count": 2},
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
"Q31": {"works": ["W50","W51","W52"]},
"Q32": {"count": 5},
"Q33": {"work": "W20"},
"Q34": {"count": 2},
"Q35": {"count": 1},
"Q36": {"count": 0},
"Q37": {"institution": "I04"},
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