**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 is also "M. Ellison" but has a different ORCID.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. A01 authored W01, W04, W05, W06 and W12, A02 authored W02, W07 and W19, and A03 authored W03.

**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.

**Q4.** 2. A05 authored W14 and W37, both ART.

**Q5.** No. W08 is by A04, whose ORCID differs from Mara Ellison's.

**Q6.** A01 (Mara Ellison), with 6 works: W01, W03, W06, W07, W12, W19. A07 and A08 have 4 each.

**Q7.** 6. These are W01, W03, W06, W07, W12 and W19, counting the preprint W02 together with its published version W03.

**Q8.** I01. I04 sits under I03, then I02, then I01.

**Q9.** 12. These are W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73 and W74.

**Q10.** 16. This is the 12 above plus W14, W28, W29 and W37 from I05.

**Q11.** 6. These are W08, W16, W20, W21, W22 and W23.

**Q12.** Full 3, fractional 2. W20, W21 and W22 are the 2024 works. W20 and W21 give Kesting 0.5 each and W22 gives it 1.

**Q13.** Full: I09. Fractional: I07. In 2024 Rostval has 4 works (W21, W27, W28, W29) at 0.25 each, totalling 1.0. Kesting has 3 works totalling 2.0.

**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W71 and W72 (1 each), plus W28 and W29 (0.5 each).

**Q15.** 4. These are W12, W21, W28 and W51.

**Q16.** 10. These are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4. These are W01, W03 (with its preprint W02), W13 and W72.

**Q19.** 7. These are W12, W13, W14, W15, W16, W17 and W18.

**Q20.** W02 (preprint of W03) and W42 (preprint of W31).

**Q21.** 4. These are W27, W31 (with its preprint W42), W39 and W50.

**Q22.** W30 has more in total (5 against 4). W31 has more in the window (4 against 1).

**Q23.** W30 has 5 citations in total, from W60 to W64. Only W60 (2020) falls within 2019–2021, so 1 is in the window.

**Q24.** 4. These are W20, W21, W22 and W23.

**Q25.** 7. W20 has 3, W21 has 2, W22 has 1 and W23 has 1.

**Q26.** Yes. W23 is flagged `is_retracted`, but the data gives no rule that excludes retracted works from output. I counted it.

**Q27.** I12, with 3 citing works: W33, W34 and W35.

**Q28.** 1. Only W32 does.

**Q29.** Author 2, institution 2, country 4. Authors: W12 and W13. Institutions: W12 (I02) and W13 (I03). Countries: W12, W13, W14 and W15 are all GB.

**Q30.** 3. These are W12, W13 and W14 (I05).

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and these three cite them.

**Q32.** 5. These are W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations (W32, W35, W36).

**Q34.** 2. These are W08 and W16. W24 is SUP.

**Q35.** 1. Only W21 counts, because W24 is SUP.

**Q36.** 0. W17 and W24 are SUP and W76 is an editorial.

**Q37.** I04, which is listed first for W70's only author (A08). The second listed affiliation is I06.

**Q38.** I06, I04, I03, I02, I01.

**Q39.** Cannot be settled. The data does not say whether K0 or K3 is the top tier. If K3, the answer is 4 (W01, W13, W71, W74). If K0, it is 1 (W07).

**Q40.** Cannot be settled. It is S01 if K3 is the top tier and S04 if K0 is.

**Q41.** Depends. S03 is K1 and S02 is K2, and the tier direction is not defined.

**Q42.** 2. These are W07 and W75.

**Q43.** Yes. W07 is an ART.

**Q44.** I02, I03, I04, I05, I06. I06 is typed AFF (affiliated) but has parent I02, so I included it.

**Q45.** 4. These are W70, W71, W73 and W74.

**Q46.** I01. I06 goes to I02 and then to I01.

**Q47.** Rostval's 2024 works are four multi-author papers, each giving it only a 0.25 share. Kesting has the sole-authored W22 worth a full 1, plus 0.5 each from W20 and W21.

**Q48.** The premise is wrong, because W70 is one of the University of Albury's works. Its Tessel affiliation (I04) rolls up through I03 to I02, and its I06 affiliation also has parent I02.

**Assumptions:**
- "Research" means ART and REV. A preprint is merged into its published version.
- I excluded the staging records W90–W92 (`record_source` STG), which also drops their citations.

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
"Q31": {"works": ["W50","W51","W52"]},
"Q32": {"count": 5},
"Q33": {"work": "W20"},
"Q34": {"count": 2},
"Q35": {"count": 1},
"Q36": {"count": 0},
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I06","I04","I03","I02","I01"]},
"Q39": {"count": null},
"Q40": {"source": null},
"Q41": {"higher": "depends"},
"Q42": {"count": 2},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06"]},
"Q45": {"count": 4},
"Q46": {"parent": "I01"}
}
```