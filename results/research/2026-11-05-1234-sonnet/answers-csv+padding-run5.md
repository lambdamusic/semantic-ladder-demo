**Q1.** 2. A01, A02 and A03 share ORCID 0000-0002-9841-6229. The other "M. Ellison" record, A04, has a different ORCID (0000-0004-8662-8360).

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01, A02 and A03, who are one person.

**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.

**Q4.** 2 (W14 and W37, both ART).

**Q5.** No. W08 is by A04, whose ORCID differs from A01's.

**Q6.** A01 (Mara Ellison) has 6 works (W01, W03, W06, W07, W12, W19). A07 and A08 each have 4.

**Q7.** 6. W02 is a preprint version of W03, so the two count once.

**Q8.** I01, via I04 → I03 → I02 → I01.

**Q9.** 12: W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74. This includes the affiliated I06 through its parent link to I02, and counts W02/W03 once.

**Q10.** 16. These are the 12 above plus W14, W28, W29 and W37 from I05.

**Q11.** 6: W08, W16, W20, W21, W22, W23.

**Q12.** Full 3 (W20, W21, W22). Fractional 2.0 (W20 gives 0.5, W21 gives 0.5, W22 gives 1).

**Q13.** Full: I09, with 4 works (W21, W27, W28, W29) against Kesting's 3. Fractional: I07, with 2.0 against Rostval's 1.0.

**Q14.** Full 7 (W06, W12, W13, W28, W29, W71, W72). Fractional 6.0.

**Q15.** 4 (W12, W21, W28, W51). The erratum W05 and the front matter W10 are not research.

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4 (W01, W03/W02, W13, W72). W05 is an erratum.

**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18). W15 cites both versions and is counted once.

**Q20.** W02 (version of W03) and W42 (version of W31).

**Q21.** 4 (W27, W31/W42, W39, W50).

**Q22.** In total W30 has more (5 citations against 4). Within its publication year and the two years after, W31 has more (4 against 1).

**Q23.** Total 5. Within 2019–2021, 1 (W60).

**Q24.** 4 (W20, W21, W22, W23).

**Q25.** 7 (W20 has 3, W21 has 2, W22 has 1, W23 has 1). This leaves out citations from the staging records W90–W92.

**Q26.** Yes. W23 is a published article, though it is flagged `is_retracted`. A policy that excludes retracted works would change this.

**Q27.** I12, with 3 citing works (W33, W34, W35).

**Q28.** 1 (W32).

**Q29.** Author 2 (W12, W13). Institution 2 (W12, W13). Country 4 (W12, W13, W14, W15). A04 is a different person from A01, so W16 is not an author self-citation.

**Q30.** 3 (W12, W13, W14, the last via I05).

**Q31.** W50, W51, W52, W90. These cite W40 or W41, which are the works that cite W01.

**Q32.** 6 (W40, W41, W50, W51, W52, W90).

**Q33.** W20, with 3 citations.

**Q34.** 2 (W08, W16). W24 is a supplement, and W90–W92 are staging records that I excluded.

**Q35.** 1 (W21).

**Q36.** 0. W17 and W24 are supplements and W76 is an editorial.

**Q37.** I04 is the first-listed affiliation (affil_seq 1) for W70. I06 is also listed, as seq 2.

**Q38.** I06, I04, I03, I02, I01 (the two listed institutions plus their ancestors).

**Q39.** 4 (W01, W13, W71, W74). This assumes K3 is the highest tier.

**Q40.** S01, assuming a larger number means a higher tier. The data does not define the order. If K0 were the top tier, it would be S04.

**Q41.** Depends. The tier order is not defined: S03 is K1 and S02 is K2.

**Q42.** 2 (W07, W75).

**Q43.** Yes. W07 is an ART.

**Q44.** I02, I03, I04, I05, I06. I06 is typed AFF but has a parent link to I02.

**Q45.** 4 (W70, W71, W73, W74).

**Q46.** I01, via I06 → I02 → I01.

**Q47.** Rostval's 2024 works each have 4 authors with only one at Rostval, so each adds just 0.25 (1.0 in total). Kesting's three works have fewer co-authors and concentrate its authors, so it gets 2.0.

**Q48.** The premise is wrong. I04 → I03 → I02, so W70 is one of the University of Albury's works through the Tessel Laboratory, and it is included in the count of 12 above.

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
"Q31": {"works": ["W50","W51","W52","W90"]},
"Q32": {"count": 6},
"Q33": {"work": "W20"},
"Q34": {"count": 2},
"Q35": {"count": 1},
"Q36": {"count": 0},
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I06","I04","I03","I02","I01"]},
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