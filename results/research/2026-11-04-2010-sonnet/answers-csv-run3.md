**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. The other "M. Ellison" (A04) has a different ORCID.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01, A02 and A03 (same person); W08 and W16 belong to A04, a different person.

**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.

**Q4.** 2. A05 wrote W14 and W37, both ART.

**Q5.** No. W08 is by A04, whose ORCID differs from Mara Ellison's.

**Q6.** A01 (Mara Ellison), with 6 works: W01, W03 (W02 is its preprint), W06, W07, W12, W19. A08 has 4 and A07 has 4.

**Q7.** 6. They are W01, W03 (with W02 as its preprint), W06, W07, W12 and W19. W04 (EDT) and W05 (ERR) are not research.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 12. These are W01, W03 (with W02), W06, W07, W12, W13, W19, W70, W71, W72, W73 and W74.

**Q10.** 16. This is the 12 from Q9 plus I05's W14, W28, W29 and W37.

**Q11.** 6. These are W08, W16, W20, W21, W22 and W23. W24 (SUP) is excluded, and so are the staging records W90–W92.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5) and W22 (1).

**Q13.** Full: I09 (4 vs 3). Fractional: I07 (2.0 vs 1.0). I09 has W21, W27, W28 and W29 at 0.25 each.

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28 (0.5), W29 (0.5), W71 and W72. W71's author A08 has two GB affiliations, which count once.

**Q15.** 4: W12, W21, W28 and W51. W05 (ERR) and W10 (PTX) are excluded.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74. W04 and W09 are non-research, and W91 is staging.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4: W01, W03 (W02 is its preprint), W13 and W72. W05 is an erratum.

**Q19.** 7: W12, W13, W14, W15, W16, W17 and W18.

**Q20.** W02 (of W03) and W42 (of W31).

**Q21.** 4: W27, W31, W39 and W50. W42 is a preprint of W31, so it is not counted separately.

**Q22.** In total, W30 has more citations (5 vs 4). Within its publication year and the two years after, W31 has more (4 vs 1).

**Q23.** Total 5. In window 1: only W60 (2020) falls in 2019–2021.

**Q24.** 4: W20, W21, W22 and W23.

**Q25.** 7. W20 has 3, W21 has 2, W22 has 1 and W23 has 1. W90–W92 are staging records, so their citations to W22 are not counted.

**Q26.** Yes. W23 is a retracted ART but is still a published record, flagged `is_retracted`. Excluding retractions would be a policy choice the data does not make.

**Q27.** I12, with 3 citing works: W33, W34 and W35.

**Q28.** 1: W32 cites W20.

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15). W16's author A04 is a different Ellison.

**Q30.** 3: W12, W13 and W14, since I05 is within the system. W15 is Dunmore (I13), which is outside it.

**Q31.** W50, W51 and W52. W01 is cited by W40 and W41, and W90 (staging) is excluded.

**Q32.** 5: W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations. W22 would have 4 only if the staging records W90–W92 counted.

**Q34.** 2: W08 and W16.

**Q35.** 1: W21. W24 is a SUP.

**Q36.** 0. W17 and W24 are SUP, and W76 is EDT.

**Q37.** I04, the first affiliation (affil_seq 1). W70 also lists I06 as a second affiliation.

**Q38.** I04, I03, I06, I02 and I01. They are the two listed units plus their ancestors.

**Q39.** 4: W01, W13, W71 and W74. This assumes K3 is the highest tier, which the data does not state.

**Q40.** S01 (K3), assuming a higher number means a higher tier. The data does not define the tier ordering, so K0 could equally be the top.

**Q41.** Depends. The data does not say whether K1 outranks K2.

**Q42.** 2: W07 and W75.

**Q43.** Yes. W07 is an ART.

**Q44.** I02, I03, I04, I05 and I06.

**Q45.** 4: W70, W71, W73 and W74.

**Q46.** I01. The chain is I06 → I02 → I01.

**Q47.** Rostval appears on more works (4 vs 3 in 2024), but on each it is one of four co-authors (0.25 share each). Kesting has the sole-author W22 (1) and half-shares of W20 and W21, giving 2.0 vs 1.0.

**Q48.** The premise is wrong: W70 is one of the University of Albury's works. I04 rolls up to I03 and then to I02, and I06 is also under I02. W70 counts once for Albury even though it has two affiliations.

Assumptions: research types are ART, REV and PPR, with preprints deduplicated against their published version. Staging (STG) records are excluded.

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
"Q12": {"full": 3, "fractional": 2.0},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 7, "fractional": 6.0},
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
"Q38": {"institutions": ["I04","I03","I06","I02","I01"]},
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