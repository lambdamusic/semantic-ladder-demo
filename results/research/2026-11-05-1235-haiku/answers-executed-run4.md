**Q1.** 2 (A01 and A04). The data has no record named "Ellison, Mara J."; A02 and A03 are merged into A01, and A04 has a different ORCID from A01.

**Q2.** W01, W03, W04, W05, W06, W07, W12, W19. These are all works credited to A01 in credits.csv.

**Q3.** No. The W37 Jonas Brandt is A05 and the W38 one is A06, which are separate people with different ORCIDs.

**Q4.** 2 (W14, W37). A05 is credited on these two research works, both at I05.

**Q5.** No. W08's M. Ellison is A04 and W01's Mara Ellison is A01, which are separate people with different ORCIDs.

**Q6.** A01 (5 works). Among I02, I03 and I04 units, A01 has W01, W03, W06, W12 and W19; A07 has four (W01, W03, W13, W72).

**Q7.** 5 (W01, W03, W06, W12, W19). W04, W05 and W07 are not research output.

**Q8.** I01. I04 → I03 → I02 → I01 by parent_id, and I01 has no parent.

**Q9.** 8 (W01, W03, W06, W12, W13, W19, W71, W72). These are the research works credited to I02, I03 or I04.

**Q10.** 12. This adds W14, W28, W29 and W37 (credited to I05) to the Q9 set.

**Q11.** 6 (W08, W16, W20, W21, W22, W24). W23 is retracted and not research output.

**Q12.** Full 3, fractional 2. The 2024 works are W20, W21 and W22; fractionally W20 gives 0.5, W21 gives 0.5 (A09 and A10 at 1/4 each) and W22 gives 1.

**Q13.** Full: tie (3 each). Fractional: I07 (2.0 against 0.75 for I09). I09's 2024 works are W21, W27 and W29.

**Q14.** Full 7; fractional 6. The GB-credited works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 each give GB 0.5 because two of their four authors are at GB institutions.

**Q15.** 4 (W12, W21, W28, W51).

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).

**Q17.** W04 (editorial) and W05 (erratum). W07 is excluded because its source is delisted, not because of its type.

**Q18.** 4 (W01, W03, W13, W72). W05 is not research output.

**Q19.** 7. W12–W18 cite W03, and no citation links to W02 or W05.

**Q20.** None. W18 is the only preprint-type work, and no other work in the data is its published version. W02 and W42 are merged into W03 and W31, but they are not separate works in the table.

**Q21.** 4 (W27, W31, W39, W50).

**Q22.** W30 has more citations in total (5 against 4). W31 has more within its window (4 against 1).

**Q23.** Total 5 (W60–W64). In window 1 (W60, 2020 falls inside 2019–2021).

**Q24.** 3 (W20, W21, W22). W23 is not research output.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 has research_output "no" because it is retracted.

**Q27.** Université de Lorvain (I12), 3 works (W33, W34, W35). These cite Kesting's W20, W21 and W22.

**Q28.** 1 (W32).

**Q29.** Authors 2 (W12, W13), institutions 2 (W12, W13), countries 4 (W12, W13, W14, W15).

**Q30.** 3 (W12, W13, W14).

**Q31.** W50, W51, W52. These cite W40 or W41, which cite W01.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20 (3 citations).

**Q34.** 3 (W08, W16, W24).

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24).

**Q37.** I06. W70 is credited to A08 at I06.

**Q38.** I04, I03, I02, I01. W71 is credited to I04, which counts towards I03, I02 and I01 in institution_units.

**Q39.** 3 (W01, W13, W71). These are the Albury-units research works in S01, the tier-1 source.

**Q40.** S01 (Journal of Marine Autonomy, tier K3, rank 1).

**Q41.** No. S03 is rank 3 and S02 is rank 2, so S02 is the higher tier.

**Q42.** 0. S04 is delisted, so W07 and W75 are not research output.

**Q43.** No. W07 is in a delisted source (S04).

**Q44.** I02, I03, I04, I05, per institution_units. The data conflicts on I06: institutions.csv gives its parent as I02, but institution_units does not roll its works up to I02 or I01. I have followed institution_units.

**Q45.** 3 (W70, W73, W74).

**Q46.** I01, by the parent_id chain I06 → I02 → I01. This conflicts with institution_units, which does not roll I06 up to I01.

**Q47.** They don't swap. In full counting they tie at 3 each (I07: W20, W21, W22; I09: W21, W27, W29). In fractional counting I07 leads (2.0 against 0.75), because fractions shrink with the number of authors and I09's works have four authors each.

**Q48.** The premise is wrong. W70 is credited to I06 (Halloran), not to Tessel (I04), which is credited on W71 and W72. Also, I06's works do not roll up to I02 in institution_units, so W70 is excluded from Albury's count for that reason.

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
  "Q13": {"full": "tie", "fractional": "I07"},
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