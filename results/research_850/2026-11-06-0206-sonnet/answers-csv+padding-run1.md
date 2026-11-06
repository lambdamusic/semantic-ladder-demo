Conventions I assumed, because the data does not define them:
- **Research works:** types ART, REV and standalone PPR count. EDT, ERR, PTX and SUP do not.
- **Excluded records:** retracted works and `STG` (staging) records are left out, and so are citations coming from STG records.
- **Merged versions:** a preprint is merged into the work it is a version of.
- **Authors:** people are matched by ORCID.
- **Units:** institutions include everything below them via `parent_id`.

I counted by hand, so the larger counts (Q9–Q11, Q14, Q16, Q21) may be off by a few.

**Q1.** 3. The ORCID 0000-0002-9841-6229 covers A01, A02, A03 and A101, and A04 and A102 are different ORCIDs.

**Q2.** 32 works: W01–W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W612, W663, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050. These come from the Mara records A01, A02, A03 and A101.

**Q3.** No. A05 (W37) and A06 (W38) have different ORCIDs.

**Q4.** 9. A05 and A104 share an ORCID; the preprint W556 merges into W1038, giving W14, W37, W554, W565, W785, W792, W1038, W702 and W725.

**Q5.** No. A04 (W08) has ORCID 0000-0004-8662-8360, which differs from Mara's.

**Q6.** A01. Mara has 22 research works credited to I02, ahead of A07, A110 and A118 at 13–15.

**Q7.** 22. Of her 32 works, 6 are non-research types, W374 is retracted, and the preprints W02 and W663 and W612 merge into W03, W464 and W869.

**Q8.** I01. I04 → I03 → I02 → I01.

**Q9.** 117.

**Q10.** 174. That is the 117 above plus 57 works from I05, I20 and I21.

**Q11.** 65. This covers I07, I08 and I22 after removing retracted, STG, SUP and ERR records (for example W23, W444, W693, W852, W1025 and W90–W92).

**Q12.** Full 14, fractional 12. The 2024 works are W20, W21, W22, W203, W333, W419, W421, W504, W528, W595, W624, W675, W705 and W1027.

**Q13.** Full: I09 (16 vs 14). Fractional: I07 (12 vs 4). Each of Rostval's 16 works has four authors from different institutions, so each contributes 0.25.

**Q14.** Full 49, fractional 44.75.

**Q15.** 25.

**Q16.** 84.

**Q17.** W04, W05, W271, W813, W936, W949. W04, W271 and W936 are editorials, and W05, W813 and W949 are errata.

**Q18.** 15. This is A07's works after merging the preprints W02 into W03 and W219 into W251, and dropping the erratum W05.

**Q19.** 27. The 29 citing works of W02 or W03 include W397 and W569, which are STG and so excluded.

**Q20.** W02, W42, W210, W219, W226, W263, W322, W407, W416, W432, W460, W506, W522, W524, W545, W556, W611, W612, W663, W728, W730, W877, W1049.

**Q21.** 47.

**Q22.** In total W30 has more citations (17 vs 12). Within the window W31 has more (12 vs 2).

**Q23.** W30 has 17 citations in total and 2 in the window 2019–2021 (W60 and W988).

**Q24.** 12. A09 and A103 share an ORCID, and the retracted W23, W693 and W1025 and the STG W268, W714 and W802 are excluded.

**Q25.** 23. W20 has 14, W21 has 3, W22 has 1, W366 has 1, W417 has 2, W531 has 1 and W967 has 1; the other six have none. Her W22 is cited mostly by STG records, which I excluded.

**Q26.** No. W23 is flagged `is_retracted` = true.

**Q27.** I12 (Université de Lorvain), with 15 citing works. I09 and I11 follow with 4 each.

**Q28.** 4. These are W32, W357, W586 and W777.

**Q29.** Author 7, institution 12, country 21. A102 (W1056) is a different M. Ellison, so it does not count as an author self-citation.

**Q30.** 18.

**Q31.** W50, W51, W52, W337, W338, W396, W546, W682, W801, W895, W922, W1042.

**Q32.** 18. Seven works cite W01 directly and 12 more cite those, with W895 in both groups.

**Q33.** W20, with 14 citations. W22 would have 19, but 18 of those come from STG records.

**Q34.** 6: W08, W16, W260, W603, W850 and W956. Including STG records would add many more.

**Q35.** 24.

**Q36.** 26.

**Q37.** I04. Its `affil_seq` is 1 for W70, with I06 second.

**Q38.** I06, I04, I03, I02 and I01.

**Q39.** 21.

**Q40.** S01 (tier K3).

**Q41.** No. S03 is K1 and S02 is K2, assuming a higher K number means a higher tier.

**Q42.** 13.

**Q43.** Yes. W07 is an ART, so it counts regardless of its source's tier (S04 is K0).

**Q44.** I02, I03, I04, I05, I06, I19, I20, I21.

**Q45.** 22.

**Q46.** I01. I06 → I02 → I01.

**Q47.** In 2024 Rostval has more works (16 vs 14), but they are mostly shared across four institutions at 0.25 each, which gives a fractional total of 4. Kesting's 14 works are largely written by its own authors, giving 12.

**Q48.** The premise does not hold in this data. W70 is credited to the University of Albury (I02): A08 lists I04 → I03 → I02, and I06 also sits under I02, so the work counts once for I02.

```json
{
"Q1": {"count": 3},
"Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3": {"same": "no"},
"Q4": {"count": 9},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 22},
"Q8": {"parent": "I01"},
"Q9": {"count": 117},
"Q10": {"count": 174},
"Q11": {"count": 65},
"Q12": {"full": 14, "fractional": 12},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 49, "fractional": 44.75},
"Q15": {"count": 25},
"Q16": {"count": 84},
"Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
"Q18": {"count": 15},
"Q19": {"count": 27},
"Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21": {"count": 47},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 17, "in_window": 2},
"Q24": {"count": 12},
"Q25": {"count": 23},
"Q26": {"counts": "no"},
"Q27": {"institution": "I12", "citing_works": 15},
"Q28": {"count": 4},
"Q29": {"author": 7, "institution": 12, "country": 21},
"Q30": {"count": 18},
"Q31": {"works": ["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W922","W1042"]},
"Q32": {"count": 18},
"Q33": {"work": "W20"},
"Q34": {"count": 6},
"Q35": {"count": 24},
"Q36": {"count": 26},
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I06","I04","I03","I02","I01"]},
"Q39": {"count": 21},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 13},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45": {"count": 22},
"Q46": {"parent": "I01"}
}
```