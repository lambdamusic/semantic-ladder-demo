**Q1.** 2. "Mara Ellison" and "Ellison, Mara J." resolve to A01 (author_ids A01 A02 A03), and "M. Ellison" is a separate person, A04, with a different ORCID.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19 (A01's credits).

**Q3.** No. W37 credits A05 and W38 credits A06, who are separate people with different ORCIDs.

**Q4.** 2. A05 is credited on W14 and W37, both research output.

**Q5.** No. W08 credits A04 and W01 credits A01, who are kept as distinct people with different ORCIDs.

**Q6.** A01. A01 has 5 research works credited to I02, I03 or I04 (W01, W03, W06, W12, W19), against 4 for A07.

**Q7.** 5. These are W01, W03, W06, W12 and W19. W04 and W05 are not research output by type, and W07 is not because its source S04 is delisted.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 8: W01, W03, W06, W12, W13, W19, W71, W72.

**Q10.** 12. These are the 8 above plus W14, W28, W29 and W37 through I05. I06 is not a unit of I01.

**Q11.** 6: W08, W16, W20, W21, W22, W24. W23 is excluded because it is retracted and not research output.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (share 0.5), W21 (0.5) and W22 (1).

**Q13.** Full counting: I09 (4 works: W21, W27, W28, W29, vs 3 for I07). Fractional counting: I07 (2.0 vs 1.0 for I09).

**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W71 and W72 (1 each) plus W28 and W29 (0.5 each).

**Q15.** 4: W12, W21, W28, W51.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.

**Q17.** W04 (EDT) and W05 (ERR).

**Q18.** 4: W01, W03, W13, W72. W05 is an erratum and not research output.

**Q19.** 7: W12, W13, W14, W15, W16, W17, W18 all cite W03.

**Q20.** None. The merged records W02 and W42 sit inside W03 and W31 rather than as separate works, and W18 is a preprint without a matching published work in the data.

**Q21.** 4: W27, W31, W39, W50.

**Q22.** W30 has more in total (5 vs 4), and W31 has more within the window (4 vs 1). W30's citers are W60–W64, and only W60 (2020) falls in 2019–2021. W31's citers W62, W65, W66 and W67 all fall in 2023–2025.

**Q23.** Total 5, in window 1 (W60 only).

**Q24.** 3: W20, W21, W22. W23 is retracted and not research output.

**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).

**Q26.** No. W23 is retracted, so research_output is "no".

**Q27.** I12, with 3 citing works (W33, W34, W35). The works citing Kesting's research are W32 (I09), W33, W34 and W35 (I12), and W36 (I11).

**Q28.** 1 (W32).

**Q29.** Author 2 (W12, W13), institution 2 (W12 via I02, W13 via I03), country 4 (W12, W13, W14, W15, all GB).

**Q30.** 3 (W12, W13, W14, via I02, I03 and I05, all within I01).

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and these three works cite W40 or W41.

**Q32.** 5: W40, W41, W50, W51, W52.

**Q33.** W20, with 3 citations.

**Q34.** 3: W08, W16, W24.

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24). W76 is an editorial and not research output.

**Q37.** I06. W70's only credit is A08 at I06.

**Q38.** I04, I03, I02, I01. W71 is credited to I04, which counts towards I03, I02 and I01.

**Q39.** 3 (W01, W13, W71, all in S01, tier_rank 1).

**Q40.** S01 (K3, rank 1).

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, and a lower rank number is higher.

**Q42.** 0. S04 is delisted, so its works (W07, W75) are not research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05.

**Q45.** 3 (W70, W73, W74).

**Q46.** I06. It is listed with parent I02, but its type is AFF (affiliate) and institution_units counts its works only towards itself, so I treat it as having no parent in the hierarchy. If you read parent_id literally, the chain would give I01.

**Q47.** Under full counting every credited work counts once, so I09 leads with 4 works against 3. Under fractional counting I07 leads, 2.0 against 1.0, because it is the sole author of W22 and holds half of W20 and W21. I09 holds only a quarter of each of its four multi-author works.

**Q48.** On W70 the author (A08) is credited to I06, not to the Tessel Laboratory (I04, which is credited on W71 and W72). I06 is an affiliate whose works count only towards itself in institution_units, not towards I02.

```json
{
"Q1": {"count": 2},
"Q2": {"works": ["W01","W03","W04","W05","W06","W07","W12","W19"]},
"Q3": {"same": "no"},
"Q4": {"count": 2},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 5},
"Q8": {"parent": "I01"},
"Q9": {"count": 8},
"Q10": {"count": 12},
"Q11": {"count": 6},
"Q12": {"full": 3, "fractional": 2},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 7, "fractional": 6},
"Q15": {"count": 4},
"Q16": {"count": 10},
"Q17": {"works": ["W04","W05"]},
"Q18": {"count": 4},
"Q19": {"count": 7},
"Q20": {"works": []},
"Q21": {"count": 4},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 5, "in_window": 1},
"Q24": {"count": 3},
"Q25": {"count": 6},
"Q26": {"counts": "no"},
"Q27": {"institution": "I12", "citing_works": 3},
"Q28": {"count": 1},
"Q29": {"author": 2, "institution": 2, "country": 4},
"Q30": {"count": 3},
"Q31": {"works": ["W50","W51","W52"]},
"Q32": {"count": 5},
"Q33": {"work": "W20"},
"Q34": {"count": 3},
"Q35": {"count": 2},
"Q36": {"count": 2},
"Q37": {"institution": "I06"},
"Q38": {"institutions": ["I04","I03","I02","I01"]},
"Q39": {"count": 3},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 0},
"Q43": {"research": "no"},
"Q44": {"institutions": ["I02","I03","I04","I05"]},
"Q45": {"count": 3},
"Q46": {"parent": "I06"}
}
```