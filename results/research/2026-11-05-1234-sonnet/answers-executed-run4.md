**Q1.** 2. People A01 (which merges A01, A02 and A03) and A04 are distinct (different ORCIDs). I take "Ellison, Mara J." to be one of the merged A02/A03 records, but the author-level names aren't shown.
**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all the credits to A01 (W03 also merges W02).
**Q3.** No. W37 is by A05 and W38 by A06, with different ORCIDs, so they are separate people.
**Q4.** 2. A05 has W14 and W37, both research output.
**Q5.** No. W08 is by A04 and W01 by A01, with different ORCIDs, so the data treats them as separate people.
**Q6.** A01. A01 has 5 research works credited to I02, I03 or I04 (W01, W03, W06, W12, W19), against 4 for A07 and 2 for A08.
**Q7.** 5. These are W01, W03, W06, W12 and W19. W04 and W05 are not research by type, and W07 is not because its source is delisted.
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9.** 8. These are W01, W03, W06, W12, W13, W19, W71 and W72, credited via I02, I03 or I04.
**Q10.** 12. These are the 8 from Q9 plus W14, W28, W29 and W37 via I05.
**Q11.** 6. These are W08, W16, W20, W21, W22 and W24 via I07 and I08. W23 is excluded because it is retracted and not research output.
**Q12.** Full 3, fractional 2. The 2024 works are W20, W21 and W22 (W24 is 2025). W20 gives 0.5, W21 gives 0.5 (I07 and I08 both roll up to I07) and W22 gives 1.
**Q13.** Full: I09. Fractional: I07. I09 has W21, W27, W28 and W29 (4 works, 0.25 each, so 1.0), against I07's 3 works (2.0).
**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 give GB 0.5 each (two of four authors), and the other five give 1 each.
**Q15.** 4. These are W12, W21, W28 and W51.
**Q16.** 10. These are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.
**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded for its delisted source, not its type.
**Q18.** 4. These are W01, W03, W13 and W72. W05 is not research output.
**Q19.** 7. These are W12, W13, W14, W15, W16, W17 and W18, all citing the merged W03.
**Q20.** W02 and W42, the preprint records merged into W03 and W31. W18 is a preprint but has no published version in the data.
**Q21.** 4. These are W27, W31, W39 and W50.
**Q22.** More in total: W30 (5 against 4). More within the window: W31 (4 against 1). W30's window is 2019–2021, so only W60 counts. W31's is 2023–2025, so W62, W65, W66 and W67 count.
**Q23.** Total 5, in window 1. The citing works are W60 (2020), W61, W62, W63 and W64, and only W60 falls in 2019–2021.
**Q24.** 3. These are W20, W21 and W22. W23 is not research output.
**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).
**Q26.** No. W23 is retracted and not research output.
**Q27.** I12, with 3 citing works (W33, W34, W35). I11 has 1 (W36) and I09 has 1 (W32).
**Q28.** 1. Only W32 does.
**Q29.** Author 2, institution 2, country 4. At author level, W12 (A01) and W13 (A07) share an author with W03. At institution level, the same two have I02/I03 credits. At country level, W12, W13, W14 and W15 have GB credits.
**Q30.** 3. These are W12, W13 and W14 (via I05, which rolls up to I01).
**Q31.** W50, W51, W52. W01 is cited by W40 and W41, which are cited by these three.
**Q32.** 5. These are W40, W41, W50, W51 and W52.
**Q33.** W20, with 3 citations.
**Q34.** 3. These are W08, W16 and W24.
**Q35.** 2. These are W21 and W24.
**Q36.** 2. These are W17 and W24. W76 is an editorial and not research output.
**Q37.** I06.
**Q38.** I04, I03, I02, I01.
**Q39.** 3. These are W01, W13 and W71, all in S01.
**Q40.** S01, which has tier_rank 1.
**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, so S02 is the higher tier.
**Q42.** 0. S04 is delisted, so none of its works are research output.
**Q43.** No. W07 is in S04, which is delisted.
**Q44.** I02, I03, I04, I05, taken from institution_units. I06 is affiliated only and does not roll up.
**Q45.** 3. These are W70, W73 and W74.
**Q46.** I06. It is an affiliate (type AFF) that counts only towards itself in institution_units, even though parent_id names I02. If the raw parent_id chain were followed instead, it would be I01.
**Q47.** Under full counting, I09 has 4 works against I07's 3. Under fractional counting, I09 gets only 0.25 from each of its four works because they have four authors each (1.0 in total). I07 gets 2.0, mainly from W22, which is single-author (1) and W20 and W21 (0.5 each).
**Q48.** W70's credit for A08 is to I06 (Halloran Institute), not Tessel (I04). I06 is an affiliate and counts only towards itself in institution_units, so it does not roll up to I02. A08's I04 credits are on W71 and W72 only.

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