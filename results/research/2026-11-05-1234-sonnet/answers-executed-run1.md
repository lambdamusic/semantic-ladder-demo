**Q1.** 2. A01 merges A01, A02 and A03 (the "Mara Ellison" and "Ellison, Mara J." forms), and A04 "M. Ellison" has a different ORCID and stays separate. The data doesn't show which name form belongs to A02 or A03.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are A01's credits, and W03 includes the merged record W02.

**Q3.** No. W37 is by A05 and W38 is by A06, who have different ORCIDs and are kept as separate people.

**Q4.** 2. A05 is credited on W14 and W37, both research output.

**Q5.** No. W08 is by A04 and W01 by A01, with different ORCIDs and no merge.

**Q6.** A01. A01 has 5 research works (W01, W03, W06, W12, W19) at I02, against 4 for A07 (W01, W03, W13, W72), using I02, I03 and I04.

**Q7.** 5. These are W01, W03, W06, W12 and W19. W04 and W05 are not research output, and W07 is excluded because S04 is delisted.

**Q8.** I01. I04 → I03 → I02 → I01.

**Q9.** 8. These are W01, W03, W06, W12, W13, W19, W71 and W72, credited to I02, I03 or I04.

**Q10.** 12. These are the 8 from Q9 plus W14, W28, W29 and W37 from I05. W12 is also credited to I05 but already counted.

**Q11.** 6. These are W08, W16, W20, W21, W22 and W24, credited to I07 or I08. W23 is excluded because it is retracted and not research output.

**Q12.** Full 4, fractional 3. The 2024 works are W20 (I07 holds 1 of 2 author credits, so 0.5), W21 (2 of 4, so 0.5), W22 (1) and W24 (1).

**Q13.** Full: tie at 4 each. Fractional: I07. Rostval's 2024 works are W21, W27, W28 and W29, with 1/4 each, so 1.0, against 3.0 for Kesting.

**Q14.** Full 7, fractional 6. The GB works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 are half GB (0.5 each) and the other five are fully GB.

**Q15.** 4. These are W12, W21, W28 and W51.

**Q16.** 10. These are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74. W04 and W09 are not research output.

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded for a different reason, its delisted source.

**Q18.** 4. These are W01, W03, W13 and W72.

**Q19.** 7. These are W12 to W18, which cite the merged work W03 (including W02).

**Q20.** W02 (merged into W03) and W42 (merged into W31). The data doesn't label them as preprints. I infer it from the merges, since they are listed only in record_ids, and W18 (type PPR) is not merged with anything.

**Q21.** 4. These are W27, W31, W39 and W50.

**Q22.** In total, W30 has more (5 against 4: W60 to W64 versus W62, W65, W66, W67). In the window, W31 has more (4 against 1). For W30 only W60 (2020) falls in 2019–2021, and for W31 W62, W65, W66 and W67 all fall in 2023–2025.

**Q23.** Total 5, in window 1.

**Q24.** 3. These are W20, W21 and W22. W23 is retracted.

**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).

**Q26.** No. W23 is retracted and not research output. Its citing work W39 isn't counted either.

**Q27.** I12, with 3 citing works (W33, W34, W35). I09 (W32) and I11 (W36) have 1 each.

**Q28.** 1. Only W32 comes from I09.

**Q29.** Author 2, institution 2, country 4. At author level W12 and W13 share an author. At institution level they credit I02 or I03. At country level W12, W13, W14 and W15 are all GB.

**Q30.** 3. W12, W13 and W14 are credited to I02, I03 or I05, all within I01.

**Q31.** W50, W51, W52. The works citing W01 are W40 and W41.

**Q32.** 5. These are W40, W41, W50, W51 and W52.

**Q33.** W20, with 3 citations.

**Q34.** 2. These are W08 and W16.

**Q35.** 2. These are W21 and W24.

**Q36.** 2. These are W17 and W24. W76 is an editorial.

**Q37.** I06.

**Q38.** I04, I03, I02, I01.

**Q39.** 3. These are W01, W13 and W71, all in S01.

**Q40.** S01 (tier_rank 1).

**Q41.** No. S03 has tier_rank 3 and S02 has rank 2, so S02 is higher.

**Q42.** 0. S04 is delisted, so none of its works are research output.

**Q43.** No. W07 is in delisted S04.

**Q44.** I02, I03, I04, I05. I06 lists I02 as parent_id, but institution_units does not roll it up.

**Q45.** 3. These are W70, W73 and W74.

**Q46.** I06. It is an affiliate (AFF) that counts only towards itself in institution_units, even though parent_id says I02. If you follow parent_id alone, the answer would be I01.

**Q47.** They don't swap. In 2024 both have 4 works under full counting (tie), and under fractional counting Kesting leads 3.0 to 1.0, because Rostval is one of four co-institutions on each of its works.

**Q48.** W70's only credit is to I06, which is an affiliate and does not count towards I02 in institution_units. The Tessel (I04) credits are on W71 and W72, not W70.

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
"Q12": {"full": 4, "fractional": 3},
"Q13": {"full": null, "fractional": "I07"},
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
"Q34": {"count": 2},
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