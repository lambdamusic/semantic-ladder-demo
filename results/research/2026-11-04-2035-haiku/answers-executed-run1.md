**Q1.** 2 people (A01 and A04). "Mara Ellison" is person A01, which merges A01, A02 and A03; "M. Ellison" is A04 alone. The name "Ellison, Mara J." does not appear in people.csv, so I can't confirm which record it is.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19 (8 works). These are all credits to person A01. W08 is credited to A04, a different person.

**Q3.** No. W37 is by A05 and W38 is by A06, which are separate people with different ORCIDs.

**Q4.** 2. A05 is credited on W14 and W37 (both at I05), and both are research output.

**Q5.** No. W08 is by A04 and W01 is by A01, which are separate people with different ORCIDs.

**Q6.** A01, with 5 research works. Albury units are I02, I03 and I04, and A01's research credits there are W01, W03, W06, W12 and W19.

**Q7.** 5 (W01, W03, W06, W12, W19). W04, W05 and W07 are not research output.

**Q8.** I01. I04 → I03 → I02 → I01 (levels_up 3).

**Q9.** 8 (W01, W03, W06, W12, W13, W19, W71, W72). Units I02, I03 and I04; W04, W05 and W07 are excluded.

**Q10.** 12. Units are I01–I05 (I05 counts towards I01), which adds W14, W28, W29 and W37 to the Q9 set.

**Q11.** 6 (W08, W16, W20, W21, W22, W24). Units are I07 and I08; W23 is not research output.

**Q12.** Full 3; fractional 2.0. The 2024 works are W20, W21 and W22; Kesting's shares are 0.5 + 0.5 + 1.0.

**Q13.** Full: Rostval (I09), 4 vs 3. Fractional: Kesting (I07), 2.0 vs 1.0. Rostval's 2024 works are W21, W27, W28 and W29, each with one of its authors.

**Q14.** Full 7; fractional 6.0. The GB works are W06, W12, W13, W28, W29, W71 and W72; W28 and W29 each give GB 0.5.

**Q15.** 4 (W12, W21, W28, W51).

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).

**Q17.** W04 and W05 (editorial and erratum types). W07 is excluded because its source S04 is delisted, not because of its type.

**Q18.** 4 (W01, W03, W13, W72). W05 is not research output.

**Q19.** 7. The citing works are W12–W18, which cite the merged record W03 (W02 is merged into it).

**Q20.** None. The only preprint-type work, W18, has no published version in the data, and W02, which merged into W03, is not a work in the table.

**Q21.** 4 (W27, W31, W39, W50). All are credited to I14 and are research output.

**Q22.** Total: W30 (5 citations vs 4). Within window: W31 (4 vs 1). W30's window is 2019–2021, which contains only W60; W31's window is 2023–2025, which contains all four of its citing works.

**Q23.** Total 5; in window 1. The citing works are W60–W64, and only W60 (2020) falls in 2019–2021.

**Q24.** 3 (W20, W21, W22). W23 is not research output.

**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36) and W22 has 1 (W34).

**Q26.** No. W23 is retracted and its research_output is no.

**Q27.** I12 (Université de Lorvain), with 3 citing works. W33, W34 and W35 cite Kesting's W21, W22 and W20 respectively.

**Q28.** 1 (W32). W32 is credited to I09 and cites W20; no other I09 work cites a Kesting work.

**Q29.** Author level 2, institution level 2, country level 4. The citing works are W12–W18, which share authors A01 or A07 (W12, W13), the Albury units I02/I03 (W12, W13), and the GB country (W12–W15).

**Q30.** 3 (W12, W13, W14). These are the citing works with an institution in the Albury System (I01, with I05 included).

**Q31.** W50, W51, W52. These are the works citing W40 or W41, which are the works that cite W01.

**Q32.** 5 (W40, W41, W50, W51, W52). Two are direct citers of W01 and three are second-hop citers.

**Q33.** W20, with 3 citations. The other Kesting research works have 0–2 citations.

**Q34.** 3 (W08, W16, W24).

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24). W76 is an editorial and is not research output.

**Q37.** I06 (Halloran Institute for Coastal Studies). The only W70 credit is A08 at I06.

**Q38.** I04, I03, I02, I01. W71's only credit is A08 at I04, which rolls up through the chain.

**Q39.** 3 (W01, W13, W71). S01 is the only tier-1 source, and Albury's works in S01 are these three.

**Q40.** S01 (Journal of Marine Autonomy), tier_rank 1.

**Q41.** No. S03 is tier_rank 3 (K1), and S02 is tier_rank 2 (K2), so S02 is higher.

**Q42.** 0. S04 is delisted, so its works W07 and W75 are not research output.

**Q43.** No. W07's research_output is no because its source S04 is delisted.

**Q44.** I02, I03, I04 and I05, per the institution_units roll-up. Caveat: institutions.csv lists I06 as a child of I02, but I06 has no roll-up row, so the data is inconsistent about whether I06 is included.

**Q45.** 3 (W70, W73, W74). I06 has no sub-units.

**Q46.** I01, per the parent_id chain I06 → I02 → I01. Caveat: institution_units does not roll I06 up to I02 or I01, so the data is inconsistent here too.

**Q47.** Kesting has the most under fractional counting but not under full counting. Under full counting each work counts once, so Rostval's four 2024 works beat Kesting's three. Under fractional counting, Kesting's works have fewer co-authors (W22 is a single-author Kesting work, W20 has two authors), so its shares are larger (2.0 vs 1.0 for Rostval).

**Q48.** W70's only credit is A08 at I06 (Halloran), not at I04 (Tessel). I06 is not in the Albury units (institution_units lists I06 only under itself), so W70 does not count. Even though I04 is an Albury unit, the premise doesn't hold because that credit is not on W70.

Q47 and Q48 have no field in the schema, so they are not in the JSON block.

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
  "Q44": {"institutions": ["I02", "I03", "I04", "I05"]},
  "Q45": {"count": 3},
  "Q46": {"parent": "I01"}
}
```