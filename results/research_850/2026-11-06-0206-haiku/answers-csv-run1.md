Counts are hand tallies across the CSVs, so the larger totals (Q9, Q10, Q14, Q16, Q21, Q36, Q39) may be off by a few.

**Assumptions:** Research output means ART and REV records. I excluded EDT, ERR, PTX, SUP and PPR records, and retracted works (`is_retracted = true`). Author-level questions treat records sharing an ORCID as one person, so A01, A02, A03 and A101 are Mara Ellison. Institution "units included" means descendants of the named institution in `parent_id`.

**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229, while A04 (0000-0004-8662-8360) and A102 (0000-0008-4738-8328) have different ORCIDs.

**Q2.** W01, W04, W05, W06, W12, W238, W271, W374, W676, W813, W949, W1005 (12 works, all types). These are the authorship rows for A01.

**Q3.** No. The Jonas Brandt of W37 (A05) has ORCID 0000-0001-6105-5008; the one of W38 (A06) has 0000-0007-5475-1779.

**Q4.** 7. A05 is credited to W14, W37, W554, W565, W785 (REV), W792 and W1038, all at I05 and none retracted.

**Q5.** No. W08's author A04 has ORCID 0000-0004-8662-8360, while A01 has 0000-0002-9841-6229.

**Q6.** A01 (Mara Ellison, person level across A01/A02/A03/A101), with 21 research works credited to the University of Albury family. The best single record is A07 with 15.

**Q7.** 21. Person level: A01 has 6 (W374 is retracted), A02 has 7, A03 has 4 and A101 has 4.

**Q8.** I01. I04 → I03 → I02 → I01.

**Q9.** 114. Hand-tallied across I02, I03, I04, I06 and I19.

**Q10.** 166. Hand-tallied, adding I05, I20 and I21 to the Q9 set.

**Q11.** 81. Hand-tallied across I07, I08 and I22.

**Q12.** Full 14; fractional 12. The 14 works are W20, W21, W22, W203, W333, W419, W421, W504, W528, W595, W624, W675, W705 and W1027.

**Q13.** Kesting (I07) under both counts. Full: 14 vs 11 for I09; fractional: about 12 vs 2.75.

**Q14.** Full 44; fractional 41. Hand-tallied from GB-affiliated 2024 research records.

**Q15.** 24. These are S02 ART/REV records dated 2024, excluding the retracted W922 and the editorial W418.

**Q16.** 91. Hand-tallied S01 ART/REV records across all years.

**Q17.** W04, W05, W271, W813, W949. These are EDT or ERR records.

**Q18.** 15. A07's ART records; W02 (PPR) and W05 (ERR) are excluded.

**Q19.** 30. The distinct citing works of W02 and W03; W05 is an erratum, not a version.

**Q20.** 23. These are PPR records whose `version_of` points to another record in the data (W02, W42, W210, W219, W226, W263, W322, W407, W416, W432, W460, W506, W522, W524, W545, W556, W611, W612, W663, W728, W730, W877, W1049).

**Q21.** 39. Hand-tallied I14 ART/REV records.

**Q22.** W30 has more citations in total (18 vs 14). W31 has more within its window (14 vs 2), since W31's window is 2023–2025 and all its citations fall in it.

**Q23.** 18 total, 2 in the 2019–2021 window (W60 and W988).

**Q24.** 12. A09's non-retracted ART/REV records; W23 and W1025 are retracted.

**Q25.** 40. Incoming citations to the 12 works from Q24, computed from `citations.csv`.

**Q26.** No. W23 is flagged `is_retracted = true`, so it is excluded from output.

**Q27.** I12 (Rostval-independent unit of I09's neighbour, Université de Lorvain), with 15 citing works. Each is counted once per institution.

**Q28.** 3. W32, W357 and W586 are I09 works that cite Kesting research works.

**Q29.** Author 7; institution 12; country 21. Counted over the 30 distinct works citing W02 or W03.

**Q30.** 18. Citing works with an author affiliation under I01.

**Q31.** W50, W51, W52, W90, W337, W338, W396, W546, W682, W801, W844, W895, W922, W1042 (14 works). These cite W40, W41, W229, W602, W657, W660, W844 or W895, all of which cite W01.

**Q32.** 20. The 8 direct citers of W01 plus 12 further distinct works two hops out.

**Q33.** W22, with 19 citations. Most come from Kesting's own works, so only one is external.

**Q34.** 24. Hand-tallied Kesting ART/REV records dated 2025.

**Q35.** 24. ART/REV records credited to I08 alone (the units W24 and W1027 are not excluded, but W24 is SUP).

**Q36.** 26. Hand-tallied S06 ART/REV records.

**Q37.** I04. W70's author A08 is affiliated with I04 (first) and I06 (second).

**Q38.** I04, I06, I03, I02, I01. W71's author A08 is at I06 and I04, and I04 sits under I03 → I02 → I01.

**Q39.** 21. The University of Albury family's research records in S01, which is the only K3 source.

**Q40.** S01 (Journal of Marine Autonomy, tier K3).

**Q41.** No. S03 is K1 and S02 is K2, so S03 is lower.

**Q42.** 13. ART/REV records in S04.

**Q43.** Yes. W07 is an ART record.

**Q44.** I02, I03, I04, I05, I06, I19, I20, I21.

**Q45.** 22. ART/REV records credited to I06 alone.

**Q46.** I01. I06 → I02 → I01.

**Q47.** The premise is wrong. Kesting stays ahead of Rostval in 2024 under both counting methods, so nothing swaps.

**Q48.** The premise is wrong. W70 is credited to the University of Albury through the Tessel Laboratory (I04 → I03 → I02) and the Halloran Institute (I06 → I02).

```json
{"Q1": {"count": 3},
 "Q2": {"works": ["W01","W04","W05","W06","W12","W238","W271","W374","W676","W813","W949","W1005"]},
 "Q3": {"same": "no"},
 "Q4": {"count": 7},
 "Q5": {"same": "no"},
 "Q6": {"author": "A01"},
 "Q7": {"count": 21},
 "Q8": {"parent": "I01"},
 "Q9": {"count": 114},
 "Q10": {"count": 166},
 "Q11": {"count": 81},
 "Q12": {"full": 14, "fractional": 12},
 "Q13": {"full": "I07", "fractional": "I07"},
 "Q14": {"full": 44, "fractional": 41},
 "Q15": {"count": 24},
 "Q16": {"count": 91},
 "Q17": {"works": ["W04","W05","W271","W813","W949"]},
 "Q18": {"count": 15},
 "Q19": {"count": 30},
 "Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
 "Q21": {"count": 39},
 "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
 "Q23": {"total": 18, "in_window": 2},
 "Q24": {"count": 12},
 "Q25": {"count": 40},
 "Q26": {"counts": "no"},
 "Q27": {"institution": "I12", "citing_works": 15},
 "Q28": {"count": 3},
 "Q29": {"author": 7, "institution": 12, "country": 21},
 "Q30": {"count": 18},
 "Q31": {"works": ["W50","W51","W52","W90","W337","W338","W396","W546","W682","W801","W844","W895","W922","W1042"]},
 "Q32": {"count": 20},
 "Q33": {"work": "W22"},
 "Q34": {"count": 24},
 "Q35": {"count": 24},
 "Q36": {"count": 26},
 "Q37": {"institution": "I04"},
 "Q38": {"institutions": ["I04","I06","I03","I02","I01"]},
 "Q39": {"count": 21},
 "Q40": {"source": "S01"},
 "Q41": {"higher": "no"},
 "Q42": {"count": 13},
 "Q43": {"research": "yes"},
 "Q44": {"institutions": ["I02","I03","I04","I05","I06","I19","I20","I21"]},
 "Q45": {"count": 22},
 "Q46": {"parent": "I01"}}
```