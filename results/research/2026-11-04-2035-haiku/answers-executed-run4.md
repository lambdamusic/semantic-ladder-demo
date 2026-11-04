**Q1.** Two people: A01 (Mara Ellison, merging A01–A03) and A04 (M. Ellison). They have different ORCIDs, and "Ellison, Mara J." does not appear in the data, so I can't place it. (people.csv)

**Q2.** Eight works: W01, W03, W04, W05, W06, W07, W12, W19. These are the works credited to A01 in credits.csv.

**Q3.** No. The W37 author is A05 (ORCID 0001-6105-5008) and the W38 author is A06 (ORCID 0007-5475-1779), which are separate people.

**Q4.** Two. A05 is credited on W14 and W37, both research output, and both at I05.

**Q5.** No. A04 (ORCID 0000-0004-8662-8360) and A01 (ORCID 0000-0002-9841-6229) are separate people.

**Q6.** A01, with five research works (W01, W03, W06, W12, W19) under I02, I03 or I04. A07 has four and A08 has two.

**Q7.** Five: W01, W03, W06, W12, W19. W04 and W05 are not research output, and W07 is excluded because its source S04 is delisted.

**Q8.** I01. The chain is I04 → I03 → I02 → I01 (institution_units, institutions.csv).

**Q9.** Eight: W01, W03, W06, W12, W13, W19, W71, W72. These are the research works credited to I02, I03 or I04.

**Q10.** Twelve. This adds I05's research works (W12, W14, W28, W29, W37) to the eight from Q9. I06 is not counted towards I01 in institution_units.

**Q11.** Six: W08, W16, W20, W21, W22, W24. These are credited to I07 or I08, and W23 is excluded because it is not research output.

**Q12.** Full: 3. Fractional: 2.0. The 2024 works are W20, W21 and W22; their Kesting shares are 1/2, 2/4 and 1 respectively.

**Q13.** Full: I09 (Rostval, 4 vs 3). Fractional: I07 (Kesting, 2.0 vs 1.0). Rostval's four 2024 works (W21, W27, W28, W29) each give a 1/4 share.

**Q14.** Full: 7. Fractional: 6.0. GB-credited 2024 research works are W06, W12, W13, W28, W29, W71, W72 (GB includes I13 and I05). Fractional shares are 1, 1, 1, 0.5, 0.5, 1, 1.

**Q15.** Four: W12, W21, W28, W51.

**Q16.** Ten: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.

**Q17.** W04 (EDT, editorial) and W05 (ERR, erratum). W07 is excluded for source reasons, not type.

**Q18.** Four: W01, W03, W13, W72. W05 is not research output.

**Q19.** Seven: W12, W13, W14, W15, W16, W17, W18. These all cite W03, since no work cites W05.

**Q20.** None. The preprint records W02 and W42 are merged into W03 and W31, and W18 (PPR) has no published version in the data.

**Q21.** Four: W27, W31, W39, W50. All are credited to I14 through A17.

**Q22.** Total: W30 (5 vs 4). Within the window: W31 (4 vs 1). W30 is cited by W60–W64. W31 is cited by W62, W65, W66 and W67, all within 2023–2025. W30's window (2019–2021) only includes W60.

**Q23.** Total: 5. Within 2019–2021: 1 (W60).

**Q24.** Three: W20, W21, W22. W23 is not research output.

**Q25.** Six. W20 is cited three times (W32, W35, W36), W21 twice (W33, W36), and W22 once (W34).

**Q26.** No. W23 has research_output "no" because it is retracted.

**Q27.** I12 (Université de Lorvain), with three citing works: W33, W34 and W35. I09 has one (W32) and I11 has one (W36).

**Q28.** One: W32, which cites W20.

**Q29.** Authors: 2 (W12 and W13 share A01 or A07 with W03). University of Albury: 2 (W12 and W13). Countries (GB): 4 (W12, W13, W14, W15).

**Q30.** Three: W12, W13, W14. Each has a credit within I01's units (I02, I03, I05).

**Q31.** W50, W51 and W52. These cite W40 or W41, which are the two works citing W01.

**Q32.** Five: W40, W41, W50, W51, W52. This excludes W01 itself.

**Q33.** W20. It has three citations, more than W21 (two) or W22 (one).

**Q34.** Three: W08, W16, W24.

**Q35.** Two: W21 and W24, both credited to A10 at I08.

**Q36.** Two: W17 and W24. W76 is an editorial and not research output.

**Q37.** I06 (Halloran Institute for Coastal Studies), via A08 in credits.csv.

**Q38.** I04, I03, I02, I01. W71 is credited to I04, which counts towards each of these levels.

**Q39.** Three: W01, W13 and W71. These are the Albury research works in S01, the only tier-1 source.

**Q40.** S01 (Journal of Marine Autonomy), tier_rank 1.

**Q41.** No. S03 is tier_rank 3 and S02 is tier_rank 2, and 1 is the highest.

**Q42.** Zero. S04 is delisted, so its works (W07, W75) are not research output.

**Q43.** No. W07's source S04 is delisted.

**Q44.** I02, I03, I04 and I05 by counting towards I01. I06 is a child of I02 in institutions.csv, but its works do not count towards I02 or I01 in institution_units. If "part of" means the parent_id hierarchy only, I06 is also included.

**Q45.** Three: W70, W73, W74.

**Q46.** I01. The chain is I06 → I02 → I01.

**Q47.** Full counting favours Rostval (4 vs 3) because Kesting has a single-author work (W22) that counts in full. Fractional counting favours Kesting (2.0 vs 1.0) because Rostval's four works each have four authors, so each Rostval share is only 1/4. This is an interpretation: the JSON has no field for Q47.

**Q48.** The premise doesn't match the data. credits.csv records one institution per person per work, and A08 on W70 is credited to I06 (Halloran), not I04. A08 is credited to I04 on W71 and W72 instead. This is an interpretation: the JSON has no field for Q48.

```json
{
  "Q1": {"count": 2},
  "Q2": {"works": ["W01", "W03", "W04", "W05", "W06", "W07", "W12", "W19"]},
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
  "Q17": {"works": ["W04", "W05"]},
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
  "Q31": {"works": ["W50", "W51", "W52"]},
  "Q32": {"count": 5},
  "Q33": {"work": "W20"},
  "Q34": {"count": 3},
  "Q35": {"count": 2},
  "Q36": {"count": 2},
  "Q37": {"institution": "I06"},
  "Q38": {"institutions": ["I04", "I03", "I02", "I01"]},
  "Q39": {"count": 3},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 0},
  "Q43": {"research": "no"},
  "Q44": {"institutions": ["I02", "I03", "I04", "I05", "I06"]},
  "Q45": {"count": 3},
  "Q46": {"parent": "I01"}
}
```