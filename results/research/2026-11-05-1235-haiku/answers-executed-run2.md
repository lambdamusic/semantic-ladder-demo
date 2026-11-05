**Q1.** 2 people: A01 (Mara Ellison, which absorbs author records A02 and A03) and A04 (M. Ellison). A04 has a different ORCID and is its own person. "Ellison, Mara J." does not appear in the data, so I cannot place it.

**Q2.** Eight works: W01, W03, W04, W05, W06, W07, W12 and W19, all credited to A01 in credits.csv.

**Q3.** No. A05 (ORCID 0001-6105-5008) wrote W37 and A06 (ORCID 0007-5475-1779) wrote W38, and they are separate people in people.csv.

**Q4.** 2. A05 is credited on W14 and W37, both research output.

**Q5.** No. A04 (M. Ellison, W08) is a separate person from A01 (Mara Ellison, W01), with a different ORCID.

**Q6.** A01, with 5 research works (W01, W03, W06, W12, W19) credited to I02, I03 or I04.

**Q7.** 5. Of A01's eight works, W04 and W05 are non-research document types and W07 is from a delisted source.

**Q8.** I01. I04 → I03 → I02 → I01 via parent_id.

**Q9.** 8: W01, W03, W06, W12, W13, W19, W71, W72 (credits to I02, I03 and I04).

**Q10.** 12: the I02/I03/I04 set above plus I05's W12, W14, W28, W29 and W37.

**Q11.** 6: W08, W16, W20, W21, W22 and W24. W23 is retracted and not research output.

**Q12.** Full 3, fractional 2.0. The 2024 works are W20, W21 and W22; W20 is one of two authors, W21 gives 2 of 4 authors to I07/I08, and W22 has one author.

**Q13.** Full: Rostval (I09) with 4 (W21, W27, W28, W29) against Kesting's 3. Fractional: Kesting with 2.0 against Rostval's 1.0 (each of Rostval's four works gives 0.25).

**Q14.** Full 7, fractional 6.0. The seven 2024 works with a GB-credited author are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 each contribute 0.5 and the other five contribute 1.0 each.

**Q15.** 4: W12, W21, W28 and W51.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71 and W74.

**Q17.** W04 (editorial) and W05 (erratum) are excluded by document type. W07 is excluded for its delisted source, not its type.

**Q18.** 4: W01, W03, W13 and W72.

**Q19.** 7: W12, W13, W14, W15, W16, W17 and W18 cite W03, the published version of the drift-aware mapping paper.

**Q20.** None. W02 (preprint) is merged into W03 and W42 into W31, but neither is a separate work in the data. W18 is a preprint with no published version in the data.

**Q21.** 4: W27, W31, W39 and W50, all with A17 credited to I14.

**Q22.** W30 has more in total (5 against W31's 4). W31 has more in its window (4 against W30's 1).

**Q23.** Total 5 (W60, W61, W62, W63, W64). Within 2019–2021, only W60 (2020) counts, so 1.

**Q24.** 3: W20, W21 and W22. W23 is not research output.

**Q25.** 6. W20 has 3 citations, W21 has 2 and W22 has 1.

**Q26.** No. W23 is retracted, so research_output is "no".

**Q27.** I12 (Université de Lorvain), with 3 citing works: W33, W34 and W35. Citations to Kesting's research works come from W32 (I09), W33/W34/W35 (I12) and W36 (I11).

**Q28.** 1: W32 cites W20.

**Q29.** Author-level 2 (W12, W13). Albury (units included) 2 (W12, W13). Country 4 (W12, W13, W14, W15, all with a GB author).

**Q30.** 3: W12, W13 and W14 have an author at an Albury System unit.

**Q31.** W50, W51 and W52. W40 and W41 cite W01, and these three cite W40 or W41.

**Q32.** 5: W40 and W41 (citing W01), plus W50, W51 and W52 (citing those).

**Q33.** W20, with 3 citations.

**Q34.** 3: W08, W16 and W24.

**Q35.** 2: W21 and W24.

**Q36.** 2: W17 and W24. W76 is an editorial.

**Q37.** I06. W70's only credit is A08 at I06.

**Q38.** I04, I03, I02, I01. W71 is credited to I04, which counts toward each parent level.

**Q39.** 3: W01, W13 and W71 appear in S01, the tier-1 source, among the Albury (units included) works.

**Q40.** S01 (Journal of Marine Autonomy, tier_rank 1).

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, so S02 is the higher tier.

**Q42.** 0. S04 is delisted, so W07 and W75 are not research output.

**Q43.** No. W07 is in S04, which is delisted.

**Q44.** I02, I03, I04 and I05 are listed in institution_units under I01. I06 has parent_id I02, so it is also below I01 in the hierarchy, but institution_units does not count its works toward I01 or I02. I have included it on the hierarchy; the works-count answer is different (Q10).

**Q45.** 3: W70, W73 and W74.

**Q46.** I01. I06 → I02 → I01.

**Q47.** They do swap. Rostval (I09) has 4 full-count works against Kesting's 3, but Kesting's fractional total (2.0) beats Rostval's (1.0). Kesting gets a full credit for W22 and half credits on W20 and W21, while each of Rostval's four works gives only a 0.25 share.

**Q48.** The premise is wrong. W70's only credit is A08 at I06 (Halloran), not the Tessel Laboratory (I04). Halloran's works count only toward I06 in institution_units, not toward Albury, so W70 is not an Albury work.

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
  "Q12": {"full": 3, "fractional": 2.0},
  "Q13": {"full": "I09", "fractional": "I07"},
  "Q14": {"full": 7, "fractional": 6.0},
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