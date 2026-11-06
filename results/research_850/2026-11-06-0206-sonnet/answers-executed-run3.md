**Q1.** 3. The people table has Mara Ellison (A01, which merges A01–A03 and A101), M. Ellison (A04) and M. Ellison (A102), each with a different ORCID. "Ellison, Mara J." is not a person record, so I took it to be one of the author records merged into A01.

**Q2.** 30 works: W01, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W608, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050. These are all the works credited to A01 in credits.csv.

**Q3.** No. The W37 author is A05 and the W38 author is A06, which are separate people with different ORCIDs.

**Q4.** 9. A05 is credited on W14, W37, W554, W565, W702, W725, W785, W792 and W1038, and all nine are research output.

**Q5.** No. W08 is credited to A04 and W01 to A01, which are different people with different ORCIDs.

**Q6.** A01. She has 20 research works at I02, against 15 for A07 and fewer for the others I checked.

**Q7.** 20. Of her 30 works, W04, W05, W07, W271, W374, W449, W763, W813, W936 and W949 are not research output.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 94 research works, counting credits at I02, I03, I04 and I19.

**Q10.** 139. This is the 94 above plus 45 more from I05 and I20, which also count towards I01.

**Q11.** 59 research works, counting I07 and I08.

**Q12.** Full 13, fractional 11. The 2024 works are W20, W21, W22, W203, W333, W419, W504, W528, W595, W624, W675, W705 and W1027. Their shares are W20 0.5, W21 0.5, W203 5/6, W419 2/3, W675 0.5 and 1 for each of the other seven.

**Q13.** Full: I09, fractional: I07. Rostval has 16 research works in 2024 (full count 16), each with one Rostval author out of four, so fractional is 4. Kesting has 13 and 11.

**Q14.** Full 47, fractional 43. The GB institutions are I02, I03, I04, I05, I06, I13, I19, I20 and I21.

**Q15.** 25 research works.

**Q16.** 85 research works.

**Q17.** W04, W05, W271, W813, W936 and W949. These are editorials and errata. W07, W374, W449 and W763 are excluded for other reasons (delisted source or retraction), not document type.

**Q18.** 15. These are W01, W03, W13, W72, W251, W262, W292, W293, W435, W553, W598, W758, W787, W833 and W969. A108, also named Priya Ramanathan, is a different person.

**Q19.** 26 works cite W03 or its preprint W02.

**Q20.** None. Preprints are merged into their published versions, and none of the standalone PPR records matches another work in the data.

**Q21.** 44 research works.

**Q22.** W30 has more in total (16 against 11). W31 has more in its window (11 against 2).

**Q23.** W30 has 16 citations in total. In 2019–2021 it has 2, from W60 and W988.

**Q24.** 12. These are W20, W21, W22, W203, W232, W366, W417, W478, W531, W686, W738 and W967.

**Q25.** 20. W20 has 13 citations, W21 has 2, W417 has 2, and W22, W366 and W531 have 1 each.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12 (Université de Lorvain), with 12 citing works.

**Q28.** 4 works: W32, W357, W586 and W777.

**Q29.** Author 7, institution 10, country 20. This is out of the 26 works citing W03.

**Q30.** 14. This is the 10 University of Albury self-citations plus W14, W349, W544 and W748, which come from I05 or I20.

**Q31.** W50, W51, W52, W337, W338, W396, W546, W682, W801, W895 and W1042.

**Q32.** 17 works. 7 cite W01 directly and 11 cite one of those, with W895 in both groups.

**Q33.** W20, with 13 citations.

**Q34.** 7 research works: W08, W16, W24, W260, W603, W850 and W956.

**Q35.** 25 research works.

**Q36.** 36 research works.

**Q37.** I06. W70 is credited to the Halloran Institute (A08 at I06).

**Q38.** I04, I03, I02 and I01.

**Q39.** 19. These are the University of Albury works in S01, the only source in the top tier (K3, rank 1).

**Q40.** S01.

**Q41.** No. S03 has tier_rank 3 and S02 has rank 2, and a lower rank number means a higher tier, so S02 is higher.

**Q42.** 0. S04 is delisted, so none of its works are research output.

**Q43.** No. W07 is in S04, which is delisted.

**Q44.** I02, I03, I04, I05, I19 and I20. I06 and I21 have parents in institutions.csv but are not listed as counting towards the system.

**Q45.** 16 research works.

**Q46.** I01. I06's parent is I02, whose parent is I01, although I06's works count only towards I06 itself.

**Q47.** Kesting has fewer 2024 works (13 against 16), but they are mostly written by Kesting authors alone or in small teams, so it keeps most of each work (11 in total). Rostval's 16 works each have one Rostval author among four, so fractional counting gives it only 4.

**Q48.** W70 is credited to I06, an affiliated institute, not to the Tessel Laboratory (I04). institution_units lists I06 as counting only towards itself, so its works do not roll up to the University of Albury.

```json
{
"Q1": {"count": 3},
"Q2": {"works": ["W01","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W608","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3": {"same": "no"},
"Q4": {"count": 9},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 20},
"Q8": {"parent": "I01"},
"Q9": {"count": 94},
"Q10": {"count": 139},
"Q11": {"count": 59},
"Q12": {"full": 13, "fractional": 11},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 47, "fractional": 43},
"Q15": {"count": 25},
"Q16": {"count": 85},
"Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
"Q18": {"count": 15},
"Q19": {"count": 26},
"Q20": {"works": []},
"Q21": {"count": 44},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 16, "in_window": 2},
"Q24": {"count": 12},
"Q25": {"count": 20},
"Q26": {"counts": "no"},
"Q27": {"institution": "I12", "citing_works": 12},
"Q28": {"count": 4},
"Q29": {"author": 7, "institution": 10, "country": 20},
"Q30": {"count": 14},
"Q31": {"works": ["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W1042"]},
"Q32": {"count": 17},
"Q33": {"work": "W20"},
"Q34": {"count": 7},
"Q35": {"count": 25},
"Q36": {"count": 36},
"Q37": {"institution": "I06"},
"Q38": {"institutions": ["I04","I03","I02","I01"]},
"Q39": {"count": 19},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 0},
"Q43": {"research": "no"},
"Q44": {"institutions": ["I02","I03","I04","I05","I19","I20"]},
"Q45": {"count": 16},
"Q46": {"parent": "I01"}
}
```