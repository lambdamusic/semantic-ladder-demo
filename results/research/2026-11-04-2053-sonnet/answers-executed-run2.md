**Q1.** 2. A01 merges A01, A02 and A03, which covers "Mara Ellison" and "Ellison, Mara J."; "M. Ellison" is the separate person A04, with a different ORCID. I couldn't see the names of A02 and A03, so this assumes "Ellison, Mara J." is one of them.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all the works with credits for A01.

**Q3.** No. W37 is credited to A05 and W38 to A06. They have different ORCIDs and are separate people.

**Q4.** 2. A05 is credited on W14 and W37, both research output.

**Q5.** No. W08 is credited to A04 and W01 to A01. They have different ORCIDs and are separate people.

**Q6.** A01. A01 has 5 research works credited to I02, I03 or I04 (W01, W03, W06, W12, W19), against 4 for A07 and 2 for A08.

**Q7.** 5. These are W01, W03, W06, W12 and W19; W04, W05 and W07 are not research output.

**Q8.** I01. The chain is I04, then I03, then I02, then I01.

**Q9.** 8. They are W01, W03, W06, W12, W13, W19, W71 and W72, credited to I02, I03 or I04.

**Q10.** 12. The 8 from Q9 plus 4 credited to I05: W14, W28, W29 and W37 (W12 is already counted).

**Q11.** 6. They are W08, W16, W20, W21, W22 and W24; W23 is excluded because it is not research output.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20 (0.5), W21 (0.5) and W22 (1).

**Q13.** Full: I09 (4 against 3). Fractional: I07 (2.0 against 1.0). I09's 2024 works are W21, W27, W28 and W29, each worth 0.25 to it.

**Q14.** Full 7, fractional 6. The GB works in 2024 are W06, W12, W13, W71 and W72 (1 each) and W28 and W29 (0.5 each).

**Q15.** 4. They are W12, W21, W28 and W51; W05 and W10 are not research output.

**Q16.** 10. They are W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 (EDT) and W05 (ERR). W07 is excluded because its source is delisted, not because of its type.

**Q18.** 4. They are W01, W03, W13 and W72.

**Q19.** 7. The citing works are W12, W13, W14, W15, W16, W17 and W18.

**Q20.** None. W18 is a preprint but is not merged into any work in the data. W02 and W42 are only records merged into W03 and W31.

**Q21.** 4. They are W27, W31, W39 and W50.

**Q22.** In total, W30 has more (5 against 4). Within its publication year and the two years after, W31 has more (4 against 1).

**Q23.** Total 5 (W60 to W64). Within 2019–2021, only W60 (2020), so 1.

**Q24.** 3. They are W20, W21 and W22; W23 is not research output.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted and so is not research output, even though it is credited to Kesting.

**Q27.** I12, with 3 citing works (W33, W34, W35). The other citing institutions are I09 (W32) and I11 (W36), one work each.

**Q28.** 1 (W32).

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15, all GB).

**Q30.** 3. W12, W13 and W14 are credited within the Albury University System; W15 is I13, which is outside it.

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and those two are in turn cited by W50, W51 and W52.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20, with 3 citations (W32, W35, W36).

**Q34.** 3 (W08, W16, W24).

**Q35.** 2 (W21, W24).

**Q36.** 2. W17 and W24 are research output; W76 is an editorial and is not.

**Q37.** I06. W70 is credited to A08 at I06.

**Q38.** I04, I03, I02, I01. These come from the institution_units rows for I04.

**Q39.** 3. The highest tier is S01, and W01, W13 and W71 appeared there.

**Q40.** S01 (tier K3, rank 1).

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, and rank 1 is the highest, so S02 is the higher tier.

**Q42.** 0. S04 is delisted, so its works are not research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05. I06 is excluded: its parent_id is I02, but institution_units has it counting only towards itself.

**Q45.** 3 (W70, W73, W74).

**Q46.** I01 by the parent_id chain (I06, then I02, then I01). However, I06 is an affiliate, and institution_units does not roll it up into I02 or I01, so for counting it stands alone.

**Q47.** Under full counting, I09 leads 4 to 3, because each work counts once. Under fractional counting, I07 leads 2.0 to 1.0, because I09's four works (W21, W27, W28, W29) each have four authors at different institutions, giving only 0.25 each. I07 holds the sole-authored W22 and half shares of W20 and W21.

**Q48.** The credit for W70 is to I06, not I04. The data does not show it listing the Tessel Laboratory. I06 is an affiliate whose only roll-up is to itself in institution_units, so its works do not count towards I02.

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