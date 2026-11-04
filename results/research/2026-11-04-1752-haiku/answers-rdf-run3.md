**Assumptions:** The data doesn't define the `wtype` codes. I treat ART, REV and PPR as research output, and EDT, ERR, PTX and SUP as not. "Units included" means all descendants via `res:parent`. Retraction is not treated as a document-type exclusion.

**Q1.** Two people. A01, A02 and A03 share ORCID 0000-0002-9841-6229, while A04 ("M. Ellison") has ORCID 0000-0004-8662-8360.

**Q2.** W01, W04, W05, W06, W12. These are the works with `AS-…-A01` authorship records.

**Q3.** No. A05 (W37) has ORCID 0000-0001-6105-5008, and A06 (W38) has 0000-0007-5475-1779.

**Q4.** 2. A05 authored W14 and W37, both articles credited to I05.

**Q5.** No. A04 (W08) has ORCID …8360, and A01 (W01) has …6229.

**Q6.** Mara Ellison (the person behind A01, A02 and A03), with 7 research works in the Albury subtree (I02, I03, I04, I06). The top single record is A07 with 5 (W01, W02, W03, W13, W72). The JSON uses A01 to stand for that merged person.

**Q7.** 7, counting the merged person (A01, A02, A03): W01, W02, W03, W06, W07, W12, W19. A01 alone has 3, since W04 (EDT) and W05 (ERR) are excluded.

**Q8.** I01. I04 → I03 → I02 → I01, and I01 has no parent.

**Q9.** 13. Albury subtree authorships (I02, I03, I04, I06) cover W01, W02, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73 and W74. W04 and W05 are excluded.

**Q10.** 17. The 13 from Q9 plus W14, W28, W29 and W37, which are credited to I05 under I01.

**Q11.** 9. The works credited to I07 or I08 are W08, W16, W20, W21, W22, W23, W90, W91 and W92. W24 (SUP) is excluded.

**Q12.** Full 3; fractional 2.0. The 2024 works are W20, W21 and W22. Kesting's shares are 1/2 on W20, 2/4 on W21 (A09 at I07 plus A10 at I08) and 1 on W22.

**Q13.** Full: I09 (4 vs 3). Fractional: I07 (2.0 vs 1.0). Rostval's 2024 works are W21, W27, W28 and W29, each with four authors, so it gets 1/4 on each.

**Q14.** Full 7; fractional 5.0. The 2024 research works with GB-affiliated authors are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 each have 2 of 4 authors in GB.

**Q15.** 4. Ocean Sensing Letters 2024 research works are W12, W21, W28 and W51. W05 (ERR) and W10 (PTX) are excluded.

**Q16.** 11. S01 works minus W04 (EDT) and W09 (PTX) are W01, W08, W13, W20, W29, W31, W32, W52, W71, W74 and W91.

**Q17.** W04 (editorial) and W05 (erratum), because of their EDT and ERR types.

**Q18.** 5. A07's research works are W01, W02, W03, W13 and W72, with W05 (ERR) excluded. If the W02 and W03 versions are merged into one work, the count is 4.

**Q19.** 7. The distinct citers are W12, W13, W14, W15, W16, W17 and W18 (citing W03 or W02).

**Q20.** W02 (versionOf W03) and W42 (versionOf W31). These are the only PPR works with a `versionOf` link.

**Q21.** 5. A17 at I14 authored W27, W31, W39, W42 and W50. W42 is a preprint, counted as research here.

**Q22.** W30 has more total citations (5 vs 4, where W31's count includes its W42 version). W31 has more within-window citations (4 vs 1). The windows are 2019–2021 for W30 and 2023–2025 for W31.

**Q23.** Total 5; in window 1. The citers are W60–W64, and only W60 (2020) falls within 2019–2021.

**Q24.** 4. A09 authored W20, W21, W22 and W23. W23 is retracted, but its document type is ART.

**Q25.** 10. W20 is cited 3 times, W21 2, W22 4 and W23 1.

**Q26.** Yes. W23 is an ART credited to I07, and the data's research-output rule is based on document type, not the retraction flag. If retracted works were excluded, it would drop out.

**Q27.** I12 (Université de Lorvain), with 3 citing works. W33, W34 and W35 are all I12 works, and they cite W21 and W22 (W33, W34) or W20 (W35). Note that these citations come from I12, not from the Kesting-affiliated W90, W91 and W92.

**Q28.** 1. The only Rostval work citing a Kesting work is W32, which cites W20.

**Q29.** Author 2 (W12 and W13), institution 2 (W12 and W13), country 4 (W12, W13, W14 and W15). W12 and W13 share an author or institution, W14 and W15 share the GB country, and W16 to W18 share none.

**Q30.** 3. W12, W13 and W14 are all in the Albury System (I01) subtree, which shares institutions with W03 and W02.

**Q31.** W50, W51, W52 and W90. These cite W40 or W41, which are the two works that cite W01.

**Q32.** 6. Within two hops of W01 are W40 and W41 (one hop), and W50, W51, W52 and W90 (two hops).

**Q33.** W22, which is cited 4 times (by W34, W90, W91 and W92).

**Q34.** 5. The 2025 Kesting research works are W08, W16, W90, W91 and W92. W24 (SUP) is excluded.

**Q35.** 0. The only work credited to I08 is W24, which is SUP.

**Q36.** 0. S06 contains only W17 (SUP), W24 (SUP) and W76 (EDT).

**Q37.** I04 (affiliationSeq 1). W70 is also credited to I06 (affiliationSeq 2).

**Q38.** I04 and I06, plus their ancestors I03, I02 and I01. Both affiliations of W71 are listed at every level.

**Q39.** 4. Albury-subtree works in S01 are W01, W13, W71 and W74. S01 is tier K3, the highest tier.

**Q40.** S01 (Journal of Marine Autonomy), tier K3.

**Q41.** No. S03 is tier K1, which is lower than S02's K2.

**Q42.** 2. The S04 works are W07 and W75, both ART.

**Q43.** Yes. W07 is an ART.

**Q44.** I02, I03, I04, I05 and I06. These are the child and grandchild institutions of I01.

**Q45.** 4. I06 is credited on W70, W71, W73 and W74, all research works.

**Q46.** I01. I06 → I02 → I01.

**Q47.** Full counting ranks Rostval higher because it has 4 works in 2024 versus Kesting's 3. Under fractional counting, Kesting's works have fewer co-authors (W22 has one author, W20 has two), so its authors take larger shares (2.0 vs 1.0). Rostval's four works each have four authors, giving only 1/4 per work.

**Q48.** The premise is wrong. W70 is credited to I06 (Halloran, a unit of I02) as well as to I04 (Tessel → I03 → I02), so it is counted in Albury's totals (Q9).

```json
{
  "Q1": {"count": 2},
  "Q2": {"works": ["W01", "W04", "W05", "W06", "W12"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 2},
  "Q5": {"same": "no"},
  "Q6": {"author": "A01"},
  "Q7": {"count": 7},
  "Q8": {"parent": "I01"},
  "Q9": {"count": 13},
  "Q10": {"count": 17},
  "Q11": {"count": 9},
  "Q12": {"full": 3, "fractional": 2.0},
  "Q13": {"full": "I09", "fractional": "I07"},
  "Q14": {"full": 7, "fractional": 5.0},
  "Q15": {"count": 4},
  "Q16": {"count": 11},
  "Q17": {"works": ["W04", "W05"]},
  "Q18": {"count": 5},
  "Q19": {"count": 7},
  "Q20": {"works": ["W02", "W42"]},
  "Q21": {"count": 5},
  "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
  "Q23": {"total": 5, "in_window": 1},
  "Q24": {"count": 4},
  "Q25": {"count": 10},
  "Q26": {"counts": "yes"},
  "Q27": {"institution": "I12", "citing_works": 3},
  "Q28": {"count": 1},
  "Q29": {"author": 2, "institution": 2, "country": 4},
  "Q30": {"count": 3},
  "Q31": {"works": ["W50", "W51", "W52", "W90"]},
  "Q32": {"count": 6},
  "Q33": {"work": "W22"},
  "Q34": {"count": 5},
  "Q35": {"count": 0},
  "Q36": {"count": 0},
  "Q37": {"institution": "I04"},
  "Q38": {"institutions": ["I04", "I06", "I03", "I02", "I01"]},
  "Q39": {"count": 4},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 2},
  "Q43": {"research": "yes"},
  "Q44": {"institutions": ["I02", "I03", "I04", "I05", "I06"]},
  "Q45": {"count": 4},
  "Q46": {"parent": "I01"}
}
```