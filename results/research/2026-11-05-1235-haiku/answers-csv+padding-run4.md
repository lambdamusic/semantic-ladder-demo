**Working definitions (the data doesn't define these, so I've assumed them):** research output = types ART, REV, PPR. EDT, ERR, PTX and SUP are non-research. A preprint and its article count as one distinct work. "Units" means institutions below the named one via `parent_id`. Retracted works (W23) are counted by type.

**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229; A04 has a different ORCID, so it is a different person.

**Q2.** W01, W04, W05, W06, W12. These are A01's authorships; A02 and A03 are the same person by ORCID and add W02, W03, W07, W19.

**Q3.** No. W37 (A05) and W38 (A06) have different ORCIDs.

**Q4.** 2. A05 is an author of W14 and W37, both ART.

**Q5.** No. A04 (ORCID 0000-0004-8662-8360) and A01 (ORCID 0000-0002-9841-6229) differ.

**Q6.** A01 (Mara Ellison, consolidated with A02 and A03). She has 6 distinct research works at Albury units, against 4 for A07.

**Q7.** 6, across A01/A02/A03: W01, W03, W06, W07, W12, W19 (W02 is a preprint of W03). The A01 record alone gives 3.

**Q8.** I01. I04 → I03 → I02 → I01.

**Q9.** 12. W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74 sit at I02/I03/I04/I06 (W02 collapses into W03; W04 and W05 are non-research).

**Q10.** 16. The 12 above plus W14, W28, W29, W37 from I05.

**Q11.** 9. W08, W16, W20, W21, W22, W23, W90, W91, W92 (W24 is SUP; W23 is retracted but ART).

**Q12.** Full 3; fractional 2.0. The 2024 works are W20, W21, W22, and Kesting's author shares are 1/2, 2/4 and 1.

**Q13.** Full: I09 (4 vs 3). Fractional: I07 (2.0 vs 1.0). Rostval's 2024 works W21, W27, W28, W29 each give 0.25.

**Q14.** Full 7; fractional 6.0. The GB-affiliated 2024 works are W06, W12, W13, W28, W29, W71, W72. W28 and W29 each give 0.5 (two GB authors of four).

**Q15.** 4. W12, W21, W28, W51 (W05 is ERR and W10 is PTX).

**Q16.** 11. W01, W08, W13, W20, W29, W31, W32, W52, W71, W74, W91.

**Q17.** W04 (EDT) and W05 (ERR).

**Q18.** 4. W01, W03 (with its preprint W02), W13, W72; W05 is ERR.

**Q19.** 7. W12, W13, W14, W15, W16, W17, W18 cite W03 or W02.

**Q20.** W02 (preprint of W03) and W42 (preprint of W31).

**Q21.** 4. W27, W31 (with its preprint W42), W39, W50.

**Q22.** Total: W30 (5 vs 4). Window: W31 (4 vs 1). W31 counts W31 and W42 together.

**Q23.** Total 5. Within 2019–2021 only W60 (2020) falls in the window, so 1.

**Q24.** 4. W20, W21, W22, W23 (W23 is retracted but ART).

**Q25.** 10. Citations: W20 (3) + W21 (2) + W22 (4) + W23 (1).

**Q26.** Depends. W23 is ART by type but flagged `is_retracted=true`, and the data doesn't say whether retracted works count.

**Q27.** Université de Lorvain (I12), with 3 works: W33, W34, W35 cite W21, W22, W20.

**Q28.** 1. Only W32 (Rostval authors) cites a Kesting work (W20).

**Q29.** Author 2 (W12, W13); institution 2 (W12, W13); country 4 (W12, W13, W14, W15). The A04 "M. Ellison" (W16) is a different ORCID.

**Q30.** 3. W12, W13, W14 cite W02/W03 from within the I01 tree.

**Q31.** W50, W51, W52, W90. These cite W40 or W41, which cite W01.

**Q32.** 6. Hop 1: W40, W41. Hop 2: W50, W51, W52, W90.

**Q33.** W22, with 4 citations (W34, W90, W91, W92). Three of those come from Kesting's own works; W20 is the most-cited by external works (3).

**Q34.** 5. W08, W16, W90, W91, W92 (W24 is SUP).

**Q35.** 1. W21 (W24 is SUP).

**Q36.** 0. S06 holds W17 and W24 (SUP) and W76 (EDT). If SUP counted, it would be 2.

**Q37.** I04. W70 has two affiliation rows: I04 (affil_seq 1) and I06 (affil_seq 2).

**Q38.** I01, I02, I03, I04, I06. W71 is credited to I06 and I04, plus their parents.

**Q39.** 4. W01, W13, W71, W74 appear in S01.

**Q40.** S01. It is the only K3 source, the highest tier.

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 2. W07, W75.

**Q43.** Yes. W07 is ART.

**Q44.** I02, I03, I04, I05, I06.

**Q45.** 4. W70, W71, W73, W74.

**Q46.** I01 (I06 → I02 → I01).

**Q47.** Full counting favours Rostval (4 vs 3), since it has four 2024 works. Fractional counting favours Kesting (2.0 vs 1.0), because Rostval's works have four authors each (0.25 per work) while Kesting's 2024 works have fewer authors, so its authors take larger shares. This has no JSON field, so it's answered in prose only.

**Q48.** The premise doesn't hold. W70 lists the Tessel Laboratory (I04), which sits under Albury (I03 → I02 → I01), and also Halloran (I06), an Albury unit. So W70 is an Albury work and is counted in Q9 and Q10. This has no JSON field either.

```json
{
  "Q1": {"count": 1},
  "Q2": {"works": ["W01", "W04", "W05", "W06", "W12"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 2},
  "Q5": {"same": "no"},
  "Q6": {"author": "A01"},
  "Q7": {"count": 6},
  "Q8": {"parent": "I01"},
  "Q9": {"count": 12},
  "Q10": {"count": 16},
  "Q11": {"count": 9},
  "Q12": {"full": 3, "fractional": 2.0},
  "Q13": {"full": "I09", "fractional": "I07"},
  "Q14": {"full": 7, "fractional": 6.0},
  "Q15": {"count": 4},
  "Q16": {"count": 11},
  "Q17": {"works": ["W04", "W05"]},
  "Q18": {"count": 4},
  "Q19": {"count": 7},
  "Q20": {"works": ["W02", "W42"]},
  "Q21": {"count": 4},
  "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
  "Q23": {"total": 5, "in_window": 1},
  "Q24": {"count": 4},
  "Q25": {"count": 10},
  "Q26": {"counts": "depends"},
  "Q27": {"institution": "I12", "citing_works": 3},
  "Q28": {"count": 1},
  "Q29": {"author": 2, "institution": 2, "country": 4},
  "Q30": {"count": 3},
  "Q31": {"works": ["W50", "W51", "W52", "W90"]},
  "Q32": {"count": 6},
  "Q33": {"work": "W22"},
  "Q34": {"count": 5},
  "Q35": {"count": 1},
  "Q36": {"count": 0},
  "Q37": {"institution": "I04"},
  "Q38": {"institutions": ["I01", "I02", "I03", "I04", "I06"]},
  "Q39": {"count": 4},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 2},
  "Q43": {"research": "yes"},
  "Q44": {"institutions": ["I02", "I03", "I04", "I05", "I06"]},
  "Q45": {"count": 4},
  "Q46": {"parent": "I01"}
}
```