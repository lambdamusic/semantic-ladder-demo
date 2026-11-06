I tallied these by hand from the CSVs, so the simple lookups are reliable but the larger counts (Q6–Q11, Q14–Q16, Q21, Q25, Q36) may be off by a few. I did not finish the fractional GB count in Q14.

**Q1.** 3 people. Records A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229; A04 and A102 have their own ORCIDs.

**Q2.** 32 works, covering the same-ORCID records A01, A02, A03 and A101 (A04 and A102 are different people).

**Q3.** No. W37 is by A05 (ORCID 0000-0001-6105-5008) and W38 by A06 (ORCID 0000-0007-5475-1779), which are different people.

**Q4.** 8 research works. A05 and A104 share an ORCID, giving W14, W37, W554, W565, W785, W792, W1038, W702 (W556 is a preprint of W1038).

**Q5.** No. M. Ellison on W08 is A04 (ORCID 0000-0004-8662-8360), and Mara Ellison on W01 is A01 (ORCID 0000-0002-9841-6229).

**Q6.** A01 (Mara Ellison, same person as A02, A03, A101), with 19 research works credited to the Albury subtree. Priya Ramanathan (A07) is next with 15.

**Q7.** 19 research works, all of them within the Albury subtree.

**Q8.** I01. I04 → I03 → I02 → I01.

**Q9.** 94 research works. This counts works credited to I02, I03, I04 and I19, excluding the affiliated institute I06, retracted works, STG records, K0 sources, editorials and errata, with preprints merged into their published versions.

**Q10.** 136 research works. This is the Albury subtree (Q9) plus the I05/I20 subtree, with I21 excluded as affiliated.

**Q11.** 56 research works. This counts I07 and I08 (I22 is affiliated and excluded).

**Q12.** Full 13; fractional 11. These are the 2024 research works of I07 and I08.

**Q13.** Kesting (I07) under both. Full: 13 vs 11 for Rostval (I09, with I23). Fractional: about 11 vs 2.75.

**Q14.** Full 196 research works with a GB-credited institution. I did not complete the fractional count.

**Q15.** 24 research works in S02 in 2024.

**Q16.** About 75 research works in S01. This is the least reliable count in the set.

**Q17.** W04 and W271 (editorials), W05, W813 and W949 (errata), and W936 (editorial).

**Q18.** 15 research works for Priya Ramanathan (A07). A108 has a different ORCID and is a different person.

**Q19.** 22 distinct works. These are the non-STG, non-retracted citers of W02 or W03, excluding W397, W569 and W973.

**Q20.** 23 works, each a preprint with `versionOf` pointing to a published work in the data.

**Q21.** 37 research works credited to I14.

**Q22.** W30 has more citations in total (16 vs 11). W31 has more within its window (11 vs 2), since its window of 2023–2025 contains all of its citers.

**Q23.** W30 has 16 citations in total and 2 within 2019–2021 (W60 and W988).

**Q24.** 12 research works between A09 and A103 (same ORCID).

**Q25.** 20 citations in total. W20 accounts for 13 of them.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12 (Université de Lorvain), with 12 citing works.

**Q28.** 4 works from I09: W32, W357, W586, W777.

**Q29.** 5 author self-citations (W12, W13, W598, W676, W843), 8 Albury-level (W12, W13, W273, W315, W598, W676, W843, W931), and 17 country-level (GB).

**Q30.** 11 citing works share an Albury University System credit with W02/W03.

**Q31.** 12 works. They cite W40, W41, W229, W602, W660 or W895, which are themselves citers of W01.

**Q32.** 18 works within two hops of W01, excluding STG and retracted records.

**Q33.** W20, with 13 citations.

**Q34.** 7 research works credited to Kesting in 2025.

**Q35.** 24 research works credited to I08.

**Q36.** 33 research works in S06.

**Q37.** I06, because A08's last-listed affiliation on W70 is I06.

**Q38.** I04, I03, I02, I01. The last-listed affiliation on W71 is I04.

**Q39.** 18 of the Albury subtree's research works are in S01, the only K3 source.

**Q40.** S01 (Journal of Marine Autonomy, tier K3).

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 0. S04 is a K0 (delisted) source, so its works are not research output.

**Q43.** No. W07 is in S04, which is delisted.

**Q44.** I02, I03, I04, I05, I19, I20. I06 and I21 are affiliated institutes and do not count as units.

**Q45.** 16 research works credited to I06.

**Q46.** I06. It is an affiliated institute, so its parent link is not followed and it is its own ultimate parent.

**Q47.** The premise is wrong. Kesting does not fall behind under either method; it leads under both (13 vs 11 full, and about 11 vs 2.75 fractional).

**Q48.** W70's author A08 gave two affiliations: I04 (seq 1) and I06 (seq 2). The house rule credits only the last-listed one, I06, which is an affiliated institute and so not a unit of I02.

```json
{
  "Q1": {"count": 3},
  "Q2": {"works": ["W01","W04","W05","W06","W12","W238","W271","W374","W464","W676","W813","W949","W1005","W02","W07","W19","W449","W663","W869","W972","W1048","W1050","W03","W206","W763","W817","W555","W612","W843","W905","W936","W984"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 8},
  "Q5": {"same": "no"},
  "Q6": {"author": "A01"},
  "Q7": {"count": 19},
  "Q8": {"parent": "I01"},
  "Q9": {"count": 94},
  "Q10": {"count": 136},
  "Q11": {"count": 56},
  "Q12": {"full": 13, "fractional": 11},
  "Q13": {"full": "I07", "fractional": "I07"},
  "Q14": {"full": 196, "fractional": null},
  "Q15": {"count": 24},
  "Q16": {"count": 75},
  "Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
  "Q18": {"count": 15},
  "Q19": {"count": 22},
  "Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
  "Q21": {"count": 37},
  "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
  "Q23": {"total": 16, "in_window": 2},
  "Q24": {"count": 12},
  "Q25": {"count": 20},
  "Q26": {"counts": "no"},
  "Q27": {"institution": "I12", "citing_works": 12},
  "Q28": {"count": 4},
  "Q29": {"author": 5, "institution": 8, "country": 17},
  "Q30": {"count": 11},
  "Q31": {"works": ["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W1039","W1042"]},
  "Q32": {"count": 18},
  "Q33": {"work": "W20"},
  "Q34": {"count": 7},
  "Q35": {"count": 24},
  "Q36": {"count": 33},
  "Q37": {"institution": "I06"},
  "Q38": {"institutions": ["I04","I03","I02","I01"]},
  "Q39": {"count": 18},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 0},
  "Q43": {"research": "no"},
  "Q44": {"institutions": ["I02","I03","I04","I05","I19","I20"]},
  "Q45": {"count": 16},
  "Q46": {"parent": "I06"}
}
```