**Q1.** 2. A01 (which merges A01, A02 and A03) is one person and A04 "M. Ellison" is another. I'm assuming "Ellison, Mara J." is one of the merged records A02/A03, since their names aren't shown.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19, from the A01 credits.

**Q3.** No. W37 credits A05 and W38 credits A06, which are separate people with different ORCIDs.

**Q4.** 2. A05 authored W14 and W37, both research output.

**Q5.** No. A04 and A01 are separate people with different ORCIDs.

**Q6.** A01. A01 has 5 research works credited to I02 and its units (W01, W03, W06, W12, W19), against 4 for A07.

**Q7.** 5. These are W01, W03, W06, W12 and W19. W04 and W05 are not research, W07 is in a delisted source, and W08 belongs to A04.

**Q8.** I01, via the chain I04 → I03 → I02 → I01.

**Q9.** 8: W01, W03, W06, W12, W13, W19, W71, W72. I06 does not roll up into I02.

**Q10.** 12. These are the 8 from Q9 plus the I05 works W14, W28, W29 and W37.

**Q11.** 6: W08, W16, W20, W21, W22, W24. W23 is excluded because it is not research output.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5, since A09 and A10 are both I07 units) and W22 (1).

**Q13.** Full counting: Rostval (I09), with 4 works (W21, W27, W28, W29) against 3 for I07. Fractional counting: Kesting (I07), with 2.0 against 1.0.

**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 each give GB only 0.5, since two of their four authors are non-GB.

**Q15.** 4: W12, W21, W28, W51.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded because its source is delisted, not because of its type.

**Q18.** 4: W01, W03, W13, W72. W05 is an erratum and does not count.

**Q19.** 7: W12, W13, W14, W15, W16, W17, W18.

**Q20.** W02 and W42. They are the merged preprint records inside W03 and W31. W18 is typed PPR but is not merged into any other work.

**Q21.** 4: W27, W31, W39, W50.

**Q22.** In total W30 has more citations, 5 against 4 for W31. Within its publication year and the two years after, W31 has more, 4 against 1.

**Q23.** Total 5 (W60–W64). In the window 2019–2021 it has 1 (W60).

**Q24.** 3: W20, W21, W22. W23 is retracted and not research output.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted and not research output, and it is the only Kesting work with that status.

**Q27.** I12, with 3 citing works (W33, W34, W35). I11 and I09 each have 1.

**Q28.** 1, which is W32.

**Q29.** Author 2 (W12, W13), institution 2 (W12 in I02, W13 in I03), country 4 (W12, W13, W14, W15, all GB). W16 is credited to A04, who is a different person from A01.

**Q30.** 3: W12, W13 and W14, whose I05 credit sits under I01.

**Q31.** W50, W51, W52. W40 and W41 cite W01, and these three cite them.

**Q32.** 5: W40, W41, W50, W51, W52.

**Q33.** W20, with 3 citations.

**Q34.** 3: W08, W16, W24.

**Q35.** 2: W21 and W24.

**Q36.** 2: W17 and W24. W76 is an editorial.

**Q37.** I06.

**Q38.** I04, I03, I02, I01.

**Q39.** 3: W01, W13, W71, all in S01.

**Q40.** S01, which has tier_rank 1.

**Q41.** No. S03 has rank 3 and S02 has rank 2, so S02 is higher.

**Q42.** 0. S04 is delisted, so none of its works count.

**Q43.** No. W07 is in S04, a delisted source.

**Q44.** I02, I03, I04, I05. I06 has I02 as its parent_id but is not part of I02's rollup in institution_units.

**Q45.** 3: W70, W73, W74.

**Q46.** I01, following parent_id from I06 to I02 to I01. I06's works still count only toward I06 itself.

**Q47.** Under full counting, I09 has 4 works (W21, W27, W28, W29) against 3 for I07, so I09 leads. Under fractional counting, I07 gets 0.5, 0.5 and 1 from W20, W21 and W22. I09 gets only 0.25 from each of its four co-authored works, so I07 leads.

**Q48.** W70's only credit (A08) is to I06, the Halloran Institute, not the Tessel Laboratory. Per institution_units, I06 counts only toward itself and not toward I02. The Tessel credit (I04) is on W71 and W72 instead.

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
"Q46": {"parent": "I01"}
}
```