**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person. The other "M. Ellison" (A04) has a different ORCID.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01, A02 and A03 combined: A01 has W01, W04, W05, W06, W12; A02 has W02, W07, W19; A03 has W03.

**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.

**Q4.** 2. A05 wrote W14 and W37, both articles.

**Q5.** No. W08 is by A04, whose ORCID differs from Mara Ellison's.

**Q6.** A01, the Mara Ellison person (A01/A02/A03). She has 6 research works under I02: W01, W03, W06, W07, W12 and W19. A07 and A08 have 4 each.

**Q7.** 6. The research works are W01, W03 (with its preprint W02 merged in), W06, W07, W12 and W19. The editorial W04 and erratum W05 are excluded.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 12. The works are W01, W03 (including W02), W06, W07, W12, W13, W19, W70, W71, W72, W73 and W74.

**Q10.** 16. This is the 12 above plus W14, W28, W29 and W37 through I05.

**Q11.** 6. The works are W08, W16, W20, W21, W22 and W23. W24 is a SUP and is excluded. W90–W92 are excluded because they come from STG (staging) records.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5, with A10 at I08 and A09 at I07 out of 4 authors) and W22 (1).

**Q13.** Full counting: I09, with 4 works (W21, W27, W28, W29) against 3 for I07. Fractional counting: I07, with 2.0 against 1.0 for I09.

**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W71 and W72 (1 each) and W28 and W29 (0.5 each). W06 and W12 each have two GB authors, so their GB share is still 1.

**Q15.** 4: W12, W21, W28, W51.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4: W01, W03 (with W02 merged in), W13, W72. W05 is an erratum.

**Q19.** 7: W12, W13, W14, W15, W16, W17, W18.

**Q20.** W02 (version of W03) and W42 (version of W31).

**Q21.** 4: W27, W31 (with W42 merged in), W39, W50.

**Q22.** In total W30 has more, with 5 citations against 4 for W31 across both versions. Within the publication year plus two years, W31 has more, with 4 (W62, W65, W66, W67) against 1 (W60) for W30.

**Q23.** 5 in total (W60–W64). 1 within 2019–2021 (W60).

**Q24.** 4: W20, W21, W22, W23.

**Q25.** 7. The counts are W20 = 3, W21 = 2, W22 = 1 and W23 = 1.

**Q26.** Yes. W23 is a retracted article (`is_retracted` = true), but it is still an article credited to I07, so it counts. The retraction flag should be shown alongside it.

**Q27.** I12, with 3 citing works: W33, W34 and W35.

**Q28.** 1: W32.

**Q29.** Author level 2 (W12, W13), institution level 2 (W12, W13), country level 4 (W12, W13, W14, W15). W16 is by the other M. Ellison (A04), so it is not a self-citation.

**Q30.** 3: W12, W13, W14 (I05 is in I01).

**Q31.** W50, W51, W52, W90. W01 is cited by W40 and W41, and these four cite one or both of them.

**Q32.** 6: W40, W41, W50, W51, W52, W90.

**Q33.** W20, with 3 citations (W32, W35, W36). Citations from the STG works W90–W92 are not counted.

**Q34.** 2: W08 and W16.

**Q35.** 1: W21. W24 is a SUP.

**Q36.** 0. S06 holds only W17 and W24 (SUP) and W76 (EDT).

**Q37.** I04. W70 lists I04 first (affil_seq 1) and I06 second.

**Q38.** I04, I03, I02, I01 and I06. A08 is affiliated with I06 and I04 on W71, and I04's ancestors are I03, I02 and I01.

**Q39.** 4: W01, W13, W71, W74. The data does not define how tiers are ordered. I assumed K3 is highest.

**Q40.** S01, under the same assumption that K3 is highest.

**Q41.** Depends. The data does not say whether K1 or K2 ranks higher. If a larger number means a higher tier, S02 is higher.

**Q42.** 2: W07 and W75.

**Q43.** Yes. W07 is an article (ART).

**Q44.** I02, I03, I04, I05, I06.

**Q45.** 4: W70, W71, W73, W74.

**Q46.** I01. The chain is I06 → I02 → I01.

**Q47.** Rostval has more works in 2024 (4 against 3), but it is only one of four authors on each, so each work earns it 0.25. Kesting's works have fewer authors (W22 has one, and W20 and W21 are split fairly evenly), so it earns 2.0 in total.

**Q48.** The premise is wrong. W70 does count as a University of Albury work, because I04 → I03 → I02. W70 is excluded only from I05, which sits under I01 but not under I02.

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
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I04","I03","I02","I01","I06"]},
"Q39": {"count": 4},
"Q40": {"source": "S01"},
"Q41": {"higher": "depends"},
"Q42": {"count": 2},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06"]},
"Q45": {"count": 4},
"Q46": {"parent": "I01"}
}
```