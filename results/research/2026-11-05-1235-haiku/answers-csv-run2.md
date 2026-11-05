**Working assumptions:** The data doesn't define the type codes or `record_source`, so I treat EDT, ERR and PTX as non-research and count ART, REV, PPR and SUP as research. Counts are work records unless a question says "distinct". Author identity is resolved by ORCID. W23 is counted by type despite its retraction flag.

**Q1.** 1 person: A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 has a different ORCID.
*Reasoning:* A01–A03 have the same ORCID, while A04 ("M. Ellison") has 0000-0004-8662-8360.

**Q2.** W01, W04, W05, W06, W12.
*Reasoning:* These are the authorship rows with A01 (W02, W03 and W07 are A02/A03, so they are excluded by ID).

**Q3.** No.
*Reasoning:* W37 is by A05 (ORCID 0000-0001-6105-5008) and W38 by A06 (ORCID 0000-0007-5475-1779).

**Q4.** 2.
*Reasoning:* A05 authored W14 (ART) and W37 (ART).

**Q5.** No.
*Reasoning:* W08's "M. Ellison" is A04 (ORCID 0000-0004-8662-8360), not A01's ORCID 0000-0002-9841-6229.

**Q6.** A01 (Mara Ellison, including A02 and A03), with 7 research records.
*Reasoning:* W01, W06 and W12 (A01), W02, W07 and W19 (A02) and W03 (A03) are all UoA-credited. The next-highest is A07 with 5 records (4 distinct).

**Q7.** 7.
*Reasoning:* Across A01, A02 and A03 the research records are W01, W02, W03, W06, W07, W12 and W19. W02 and W03 are versions of one work, so there are 6 distinct works.

**Q8.** I01.
*Reasoning:* I04 → I03 → I02 → I01.

**Q9.** 13.
*Reasoning:* Via I02, I03, I04 and I06 the research records are W01, W02, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73 and W74. This is 12 distinct works if W02 is folded into W03.

**Q10.** 17.
*Reasoning:* The 13 UoA works plus W14, W28, W29 and W37 (via I05). This is 16 distinct works.

**Q11.** 10.
*Reasoning:* I07 authored W08, W16, W20, W21, W22, W23, W90, W91 and W92, and I08 (a child of I07) adds W24.

**Q12.** Full 3; fractional 2.0.
*Reasoning:* The 2024 works are W20 (2 authors, 1 from I07 → 0.5), W21 (4 authors, 2 in the I07 tree → 0.5) and W22 (1 author → 1.0).

**Q13.** Full: Rostval (I09) with 4 vs 3. Fractional: Kesting (I07) with 2.0 vs 1.0.
*Reasoning:* I09 has 4 works in 2024 (W21, W27, W28, W29), each with one of four authors (0.25 each). Kesting has 3 works, but its single-author W22 gives it more fractional credit.

**Q14.** Full 7; fractional 6.0.
*Reasoning:* Seven 2024 works have a GB-affiliated author: W06, W12, W13, W71 and W72 fully, and W28 and W29 at 2 of 4 authors each (0.5 each).

**Q15.** 4.
*Reasoning:* S02 2024 research records are W12, W21, W28 and W51 (W05 is an erratum and W10 is front matter).

**Q16.** 11.
*Reasoning:* S01 has 13 records, minus the editorial W04 and the front matter W09.

**Q17.** W04 and W05.
*Reasoning:* W04 is EDT (editorial) and W05 is ERR (erratum); W01 and W06 are ART and W12 is ART.

**Q18.** 4.
*Reasoning:* A07 has 5 research records (W01, W02, W03, W13, W72), and W02 and W03 are one work.

**Q19.** 7.
*Reasoning:* W02 is cited by W15 and W18; W03 is cited by W12, W13, W14, W15, W16 and W17. W15 is counted once.

**Q20.** W02 and W42.
*Reasoning:* These are the PPR records with `version_of` set (to W03 and W31).

**Q21.** 5.
*Reasoning:* I14 authored W27, W31, W39, W42 and W50 (all via A17). This is 4 distinct works if W42 is folded into W31.

**Q22.** More in total: W30 (5 citations vs 4). More in window: W31 (4 vs 1).
*Reasoning:* W30 is cited by W60–W64 (window 2019–2021 contains only W60). W31 and its preprint W42 are cited by W62, W65, W66 and W67, all in its 2023–2025 window.

**Q23.** Total 5; in window 1.
*Reasoning:* Citations to W30 come from W60, W61, W62, W63 and W64. Only W60 (2020) falls in 2019–2021.

**Q24.** 4.
*Reasoning:* A09 authored W20, W21, W22 and W23. This is 3 if the retracted W23 is excluded.

**Q25.** 10.
*Reasoning:* Citations are W20 (W32, W35, W36) = 3, W21 (W33, W36) = 2, W22 (W34, W90, W91, W92) = 4, and W23 (W39) = 1.

**Q26.** Depends.
*Reasoning:* W23 is ART and credited to I07 via A09, so it counts by type. However, it is flagged `is_retracted=true`, and the data gives no rule for whether retractions are excluded.

**Q27.** I12, citing 3 works.
*Reasoning:* I12 authors W33, W34 and W35, which cite Kesting works W21 and W22 and W20. The other institutions have one each (I09 via W32, I11 via W36, I14 via W39).

**Q28.** 1.
*Reasoning:* Only W32 (all I09 authors) cites a Kesting work (W20).

**Q29.** Author-level 2; institution-level 2; country-level 4.
*Reasoning:* Author self-citations are W12 and W13 (A01 and A07 match the cited authors, and A01 = A02 = A03 by ORCID, while A04 is not Mara). Country-level GB self-citations are W12, W13, W14 and W15.

**Q30.** 3.
*Reasoning:* Citing works with a UoA-tree author in the I01 system are W12 (I02), W13 (I03) and W14 (I05).

**Q31.** W50, W51, W52 and W90.
*Reasoning:* W01 is cited by W40 and W41. W50 and W51 cite W40, W51 and W52 cite W41, and W90 cites W41.

**Q32.** 6.
*Reasoning:* One hop gives W40 and W41; two hops add W50, W51, W52 and W90.

**Q33.** W22.
*Reasoning:* W22 has 4 citations (W34, W90, W91, W92), more than W20 (3) and W21 (2).

**Q34.** 6.
*Reasoning:* The 2025 works are W08, W16, W90, W91 and W92 (I07) plus W24 (I08).

**Q35.** 2.
*Reasoning:* I08 authored W21 (ART) and W24 (SUP).

**Q36.** 2.
*Reasoning:* S06 has W17 and W24 (both SUP); W76 is an editorial. This is 0 if SUP is excluded.

**Q37.** I04 (affil_seq 1), with I06 also listed (affil_seq 2).
*Reasoning:* W70 has two affiliation rows for A08, one for I04 and one for I06.

**Q38.** I01, I02, I03, I04 and I06.
*Reasoning:* W71 is credited to I06 and I04, whose ancestors are I02 and I03, and then I01.

**Q39.** 4.
*Reasoning:* S01 (K3) is the source of W01, W13, W71 and W74 among the UoA works.

**Q40.** S01.
*Reasoning:* S01 is the only K3 source.

**Q41.** No.
*Reasoning:* S03 is K1 and S02 is K2, so S03 is lower.

**Q42.** 2.
*Reasoning:* S04 has W07 and W75, both ART.

**Q43.** Yes.
*Reasoning:* W07 is ART, not retracted, and in the FEED feed.

**Q44.** I02, I03, I04, I05 and I06.
*Reasoning:* These are the descendants of I01 (I02 and I05 directly, then I03 and I06 under I02, then I04 under I03).

**Q45.** 4.
*Reasoning:* I06 is credited with W70, W71, W73 and W74.

**Q46.** I01.
*Reasoning:* I06 → I02 → I01.

**Q47.** Rostval has more 2024 works (4 vs 3), so it leads on full counting. Its four works each have four authors, giving it only 0.25 per work. Kesting's W22 has a single author (1.0) and W20 has only two, so Kesting leads on fractional counting (2.0 vs 1.0).

**Q48.** The premise is wrong. W70 is credited to I04 (Tessel Laboratory), which sits under I03 and then I02 (University of Albury). W70 is therefore one of the 13 UoA research works counted in Q9.

```json
{"Q1": {"count": 1},
 "Q2": {"works": ["W01", "W04", "W05", "W06", "W12"]},
 "Q3": {"same": "no"},
 "Q4": {"count": 2},
 "Q5": {"same": "no"},
 "Q6": {"author": "A01"},
 "Q7": {"count": 7},
 "Q8": {"parent": "I01"},
 "Q9": {"count": 13},
 "Q10": {"count": 17},
 "Q11": {"count": 10},
 "Q12": {"full": 3, "fractional": 2.0},
 "Q13": {"full": "I09", "fractional": "I07"},
 "Q14": {"full": 7, "fractional": 6.0},
 "Q15": {"count": 4},
 "Q16": {"count": 11},
 "Q17": {"works": ["W04", "W05"]},
 "Q18": {"count": 4},
 "Q19": {"count": 7},
 "Q20": {"works": ["W02", "W42"]},
 "Q21": {"count": 5},
 "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
 "Q23": {"total": 5, "in_window": 1},
 "Q24": {"count": 4},
 "Q25": {"count": 10},
 "Q26": {"counts": "depends"},
 "Q27": {"institution": "I12", "citing_works": 3},
 "Q28": {"count": 1},
 "Q29": {"author": 2, "institution": 2, "country": 4},
 "Q30": {"count": 3},
 "Q31": {"works": ["W50", "W51", "W52", "W90"]},
 "Q32": {"count": 6},
 "Q33": {"work": "W22"},
 "Q34": {"count": 6},
 "Q35": {"count": 2},
 "Q36": {"count": 2},
 "Q37": {"institution": "I04"},
 "Q38": {"institutions": ["I01", "I02", "I03", "I04", "I06"]},
 "Q39": {"count": 4},
 "Q40": {"source": "S01"},
 "Q41": {"higher": "no"},
 "Q42": {"count": 2},
 "Q43": {"research": "yes"},
 "Q44": {"institutions": ["I02", "I03", "I04", "I05", "I06"]},
 "Q45": {"count": 4},
 "Q46": {"parent": "I01"}}
```