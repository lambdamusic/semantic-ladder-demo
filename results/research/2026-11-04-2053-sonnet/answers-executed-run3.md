**Q1.** 2. A01 (merging A01, A02 and A03) is one person. A04 "M. Ellison" has a different ORCID and is a separate person in people.csv. I can't see the name of A02 or A03, so I'm assuming "Ellison, Mara J." is one of them.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all the credits for A01 (W03 also merges W02).

**Q3.** No. W37 is by A05 and W38 is by A06, two different people with different ORCIDs.

**Q4.** 2 (W14, W37).

**Q5.** No. W08 is credited to A04 and W01 to A01, which are separate people with different ORCIDs.

**Q6.** A01. A01 has 5 research works credited to I02 or I03 (W01, W03, W06, W12, W19), against 4 for A07 and 2 for A08.

**Q7.** 5 (W01, W03, W06, W12, W19). W04, W05 and W07 are not research output.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 8 (W01, W03, W06, W12, W13, W19, W71, W72), counting credits to I02, I03 and I04.

**Q10.** 12. These are the 8 above plus 4 from I05 (W14, W28, W29, W37). I06 is not rolled up into I01.

**Q11.** 6 (W08, W16, W20, W21, W22, W24). W23 is excluded because it is not research output.

**Q12.** Full 4, fractional 3.0. The 2024 works are W20 (0.5), W21 (0.5), W22 (1) and W24 (1).

**Q13.** Full: tie, with both at 4. Fractional: I07 (3.0 against 1.0 for I09). I09's 2024 works are W21, W27, W28 and W29, each worth 0.25.

**Q14.** Full 7, fractional 6.0. The works are W06 (1), W12 (1), W13 (1), W28 (0.5), W29 (0.5), W71 (1) and W72 (1).

**Q15.** 4 (W12, W21, W28, W51).

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74). W04 and W09 are not research output.

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded for a different reason: its source is delisted.

**Q18.** 4 (W01, W03, W13, W72).

**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18).

**Q20.** None. W18 is typed as a preprint but isn't merged into any work in the data. W02 and W42 were merged into W03 and W31 and no longer appear as separate works.

**Q21.** 4 (W27, W31, W39, W50).

**Q22.** In total W30 has more (5 against 4). Within its publication year and the two years after, W31 has more (4 against 1).

**Q23.** Total 5 (W60–W64). Within 2019–2021 only 1 (W60).

**Q24.** 3 (W20, W21, W22). W23 is retracted and not research output.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12, with 3 citing works (W33, W34, W35). I09 and I11 have 1 each.

**Q28.** 1 (W32).

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15). W16's A04 is a different person from A01.

**Q30.** 3 (W12, W13, W14). W14 counts because I05 sits under I01.

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and those are in turn cited by W50, W51 and W52.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20, with 3 citations (W32, W35, W36).

**Q34.** 2 (W08, W16).

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24). W76 is an editorial and does not count.

**Q37.** I06.

**Q38.** I04, I03, I02, I01.

**Q39.** 3 (W01, W13, W71), all in S01.

**Q40.** S01, which has tier_rank 1.

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, and rank 1 is the highest, so S03 is lower.

**Q42.** 0. S04 is delisted, so none of its works count as research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05.

**Q45.** 3 (W70, W73, W74).

**Q46.** I06. Its parent_id points to I02, but it is an affiliate (AFF) and institution_units counts it only towards itself, so it doesn't roll up to I02 or I01. Read purely from parent_id, the answer would be I01.

**Q47.** The premise is slightly off, because under full counting they tie at 4 each in 2024. Kesting leads under fractional counting (3.0 against 1.0) because W22 and W24 are sole-author Kesting works. Each of Rostval's four works (W21, W27, W28, W29) has only one Rostval author among four, so each is worth 0.25.

**Q48.** W70's only credit is to I06, which counts only towards itself and not towards I02. The credit for A08 is to I06 (Halloran Institute), not I04. A08 is credited to I04 only on W71 and W72.

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