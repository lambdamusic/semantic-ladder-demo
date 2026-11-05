**Q1.** 2. The three records A01, A02 and A03 are merged into one person (A01), and M. Ellison (A04) is a separate person with a different ORCID. The data doesn't show which record is named "Ellison, Mara J.", so I assume it is one of A02/A03.
**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are the works credited to A01. W03 also merges W02.
**Q3.** No. W37 is by A05 and W38 is by A06, who have different ORCIDs and are separate people.
**Q4.** 2. A05 authored W14 and W37, and both are research output.
**Q5.** No. W08 is by A04 and W01 is by A01, who are separate people with different ORCIDs.
**Q6.** A01. A01 has 5 research works (W01, W03, W06, W12, W19) credited to I02, I03 or I04. A07 has 4.
**Q7.** 5. These are W01, W03, W06, W12 and W19. W04, W05 and W07 are not research output.
**Q8.** I01. I04 counts towards I03, I02 and I01, with I01 three levels up.
**Q9.** 7. These are W01, W03, W06, W12, W13, W19 and W72, credited to I02, I03 or I04.
**Q10.** 11. These are the 7 from Q9 plus W14, W28, W29 and W37 from I05.
**Q11.** 6. These are W08, W16, W20, W21, W22 and W24. W23 is excluded because it is retracted and not research output.
**Q12.** Full 4, fractional 3.0. The 2024 works are W20, W21, W22 and W24. Their I07 shares are 0.5, 0.5, 1 and 1.
**Q13.** Under full counting they tie at 4 each, so there is no winner. Under fractional counting Kesting (I07) leads, 3.0 to 1.0. Rostval's 2024 works are W21, W27, W28 and W29, each worth 0.25.
**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 are worth 0.5 each to GB, and the others are worth 1 each.
**Q15.** 4. These are W12, W21, W28 and W51.
**Q16.** 10. These are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.
**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded because its source is delisted, not because of its type.
**Q18.** 4. These are W01, W03, W13 and W72.
**Q19.** 7. These are W12, W13, W14, W15, W16, W17 and W18.
**Q20.** W02 and W42. They are merged into W03 and W31 respectively. W18 has a preprint type but no published version in the data.
**Q21.** 4. These are W27, W31, W39 and W50.
**Q22.** W30 has more in total (5 vs 4). W31 has more in the window (4 vs 1). W30's window is 2019–2021, and only W60 (2020) falls in it. W31's window is 2023–2025 and holds W62, W65, W66 and W67.
**Q23.** Total 5 (W60–W64), and 1 in the window (W60).
**Q24.** 3. These are W20, W21 and W22. W23 is excluded.
**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).
**Q26.** No. W23 is retracted and not research output.
**Q27.** I12, with 3 citing works (W33, W34, W35). I09 and I11 have 1 each.
**Q28.** 1. Only W32 is credited to I09 and cites Kesting's works (W20).
**Q29.** Author 2, institution 2, country 4.
- Author level: W12 (A01) and W13 (A07). W16's A04 is a different person.
- Institution level (University of Albury): W12 and W13.
- Country level (GB): W12, W13, W14 and W15.

**Q30.** 3. These are W12, W13 and W14. W14 is credited to I05, which sits under I01.
**Q31.** W50, W51 and W52. W01 is cited by W40 and W41, and those are cited by W50, W51 and W52.
**Q32.** 5. These are W40, W41, W50, W51 and W52.
**Q33.** W20, with 3 citations.
**Q34.** 3. These are W08, W16 and W24.
**Q35.** 2. These are W21 and W24.
**Q36.** 2. These are W17 and W24. W76 is an editorial.
**Q37.** I06.
**Q38.** I04, I03, I02 and I01.
**Q39.** 2. These are W01 and W13, both in S01.
**Q40.** S01, which has tier rank 1.
**Q41.** No. S03 has rank 3 and S02 has rank 2, and rank 1 is the highest.
**Q42.** 0. S04 is delisted, so its works are not research output.
**Q43.** No. W07 is in S04, which is delisted.
**Q44.** I02, I03, I04 and I05. I06 is only an affiliate: its parent_id is I02, but institution_units does not count it towards I02.
**Q45.** 3. These are W70, W73 and W74.
**Q46.** I06. Its parent_id says I02, but I06 is an affiliate and counts only towards itself in institution_units. If you read parent_id as the hierarchy, the answer would be I01.
**Q47.** They don't swap. In 2024 they tie at 4 under full counting, and Kesting leads under fractional counting, 3.0 to 1.0. Kesting's works have fewer co-authors from other institutions, so fractional counting keeps more of each work.
**Q48.** W70 is credited to I06 (Halloran), not to the Tessel Laboratory. I06 does not count towards I02 in institution_units. Tessel (I04) is credited on W71 and W72, not W70.

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
"Q9": {"count": 7},
"Q10": {"count": 11},
"Q11": {"count": 6},
"Q12": {"full": 4, "fractional": 3.0},
"Q13": {"full": null, "fractional": "I07"},
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
"Q39": {"count": 2},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 0},
"Q43": {"research": "no"},
"Q44": {"institutions": ["I02","I03","I04","I05"]},
"Q45": {"count": 3},
"Q46": {"parent": "I06"}
}
```