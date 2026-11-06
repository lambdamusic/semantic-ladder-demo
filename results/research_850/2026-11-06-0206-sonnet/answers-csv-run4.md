Assumptions I applied, because the data does not define them:
- Research works are ART, REV and PPR records. EDT, ERR, PTX and SUP records, retracted works and STG (staging) records are excluded.
- A preprint is merged into the work named in its `version_of`.
- Authors are merged by ORCID.
- Institutions roll up through `parent_id`, including AFF units.
- A higher K number means a higher tier.

The counts come from long manual scans, so the larger ones (Q9, Q10, Q11, Q16, Q21) may be off by a few.

**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229. The "M. Ellison" records A04 and A102 carry different ORCIDs.
**Q2.** 32 works, listed in the JSON. They cover A01, A02, A03 and A101 and include editorials, errata and the retracted W374.
**Q3.** No. W37 is by A05 and W38 by A06, which have different ORCIDs.
**Q4.** 9. A05 and A104 share an ORCID; the works are W14, W37, W554, W565, W785, W792, W1038, W702 and W725. The preprint W556 is merged into W1038.
**Q5.** No. W08 is by A04 (ORCID …8360); W01 is by A01 (ORCID …6229).
**Q6.** A01, meaning Mara Ellison, with 22 UoA research works. The next highest is A110 with about 15.
**Q7.** 22. The excluded items are the editorials, errata, the retracted W374, and the preprints W02 and W663.
**Q8.** I01, via I04→I03→I02→I01.
**Q9.** 117 (I02, I03, I04, I06 and I19).
**Q10.** 174. That is the 117 above plus 57 from I05, I20 and I21.
**Q11.** 64 (I07, I08 and I22).
**Q12.** Full 14, fractional 12.0. The 2024 works are W20, W21, W22, W203, W333, W1027, W419, W421, W504, W528, W624, W675, W705 and W595.
**Q13.** Full counting favours I09 (15 vs 14). Fractional counting favours I07 (12.0 vs 3.75).
**Q14.** Full 45, fractional 41.5.
**Q15.** 24.
**Q16.** 88.
**Q17.** W04, W05, W271, W813, W936 and W949. These are editorials and errata.
**Q18.** 15. W02 and W219 are merged into W03 and W251.
**Q19.** 29 distinct citing works, from the citations of W02 and W03.
**Q20.** 23 preprints with an existing parent, listed in the JSON. PPR records without `version_of` are excluded.
**Q21.** 47.
**Q22.** W30 has more in total (18 vs 13 distinct citing works for W31 and its preprint W42). W31 has more in its window (13 vs 2).
**Q23.** 18 in total and 2 within 2019–2021 (W60 and W988).
**Q24.** 12. A09 and A103 share an ORCID.
**Q25.** 41. The per-work counts are W20 14, W21 3, W22 19, W366 1, W417 2, W967 1 and W531 1.
**Q26.** No. W23 is retracted, so it is excluded under the assumption above.
**Q27.** I12, with 16 citing works. W806 is a Kesting work that also lists I12.
**Q28.** 4 (W32, W586, W777 and W357).
**Q29.** Author 7, institution 12, country 21.
**Q30.** 18.
**Q31.** 14 works, listed in the JSON.
**Q32.** 20, excluding W01 itself.
**Q33.** W22, with 19 citations.
**Q34.** 6 (W08, W16, W260, W603, W850 and W956).
**Q35.** 24.
**Q36.** 26.
**Q37.** I04, its first-listed affiliation. I06 is listed second.
**Q38.** I06 and I04, plus their ancestors I03, I02 and I01.
**Q39.** 20. This assumes S01 (K3) is the highest tier.
**Q40.** S01. The tier scale direction is not documented.
**Q41.** No. S03 is K1 and S02 is K2.
**Q42.** 13.
**Q43.** Yes. W07 is a non-retracted ART.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22.
**Q46.** I01, via I06→I02→I01.
**Q47.** The Rostval Technical University (I09) works are mostly four-author papers with one Rostval author each, so each is worth 0.25 under fractional counting (15 works, 3.75). Kesting's works are mostly by Kesting authors, so it scores 12.0 fractionally while trailing 14 to 15 under full counting.
**Q48.** It is one of the University of Albury's works. A08's first-listed affiliation on W70 is I04, and I04→I03→I02, so the work counts; the premise is false.

```json
{
"Q1": {"count": 3},
"Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3": {"same": "no"},
"Q4": {"count": 9},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 22},
"Q8": {"parent": "I01"},
"Q9": {"count": 117},
"Q10": {"count": 174},
"Q11": {"count": 64},
"Q12": {"full": 14, "fractional": 12.0},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 45, "fractional": 41.5},
"Q15": {"count": 24},
"Q16": {"count": 88},
"Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
"Q18": {"count": 15},
"Q19": {"count": 29},
"Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21": {"count": 47},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 18, "in_window": 2},
"Q24": {"count": 12},
"Q25": {"count": 41},
"Q26": {"counts": "no"},
"Q27": {"institution": "I12", "citing_works": 16},
"Q28": {"count": 4},
"Q29": {"author": 7, "institution": 12, "country": 21},
"Q30": {"count": 18},
"Q31": {"works": ["W50","W51","W52","W90","W337","W338","W396","W546","W682","W801","W844","W895","W922","W1042"]},
"Q32": {"count": 20},
"Q33": {"work": "W22"},
"Q34": {"count": 6},
"Q35": {"count": 24},
"Q36": {"count": 26},
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I06","I04","I03","I02","I01"]},
"Q39": {"count": 20},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 13},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45": {"count": 22},
"Q46": {"parent": "I01"}
}
```