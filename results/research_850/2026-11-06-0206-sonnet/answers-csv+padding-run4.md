Assumptions, since the data doesn't define them:
- "Research work" means type ART or REV. A preprint (PPR) is merged into the work named in its `version_of`.
- EDT, ERR, PTX and SUP records are not research.
- Retracted works still count.
- STG records are treated as unvalidated staging and excluded.
- Authors are merged by shared ORCID.
- Institutions roll up through `parent_id`, including AFF units.

**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229. A04 (…8662-8360) and A102 (…4738-8328) are different people.

**Q2.** 32 works, listed in the JSON. They are every authorship of A01, A02, A03 and A101 (the same person).

**Q3.** No. W37 has A05 and W38 has A06, with different ORCIDs.

**Q4.** 9. A05 and A104 share an ORCID; the works are W14, W37, W554, W565, W785, W792, W1038 (with its preprint W556), W702 and W725.

**Q5.** No. W08 has A04 (ORCID …8662-8360), while Mara is …9841-6229.

**Q6.** Mara Ellison (A01). She has 23 research works, all credited to I02. The next highest is A07 with 15.

**Q7.** 23. This counts W02/W03, W612/W869 and W663/W464 once each, and includes the retracted W374.

**Q8.** I01. The chain is I04, then I03, then I02, then I01.

**Q9.** 119, for I02 plus I03, I04, I19 and I06.

**Q10.** 175. That is the 119 for I02 plus 56 more from I05, I20 and I21.

**Q11.** 70, covering I07, I08 and I22.

**Q12.** Full 14, fractional 12.0. The fractional figure is the sum of Kesting's share of each 2024 work, e.g. W20 = ½, W203 = 5/6, W419 = ⅔, W21 = ½, W675 = ½.

**Q13.** Full: I09 (16 works against 14). Fractional: I07 (12.0 against 4.0).

**Q14.** Full 49, fractional ≈44.67. The 49 comes from 29 works with an I02-unit author, 12 with an I05-unit author (W28 and W29 among them) and 8 more with an I13-only author.

**Q15.** 27. These are the ART and REV records in S02 for 2024; W520 and W922 are retracted but counted.

**Q16.** 90 research works in S01, STG records excluded, including the retracted W693 and W852.

**Q17.** W04, W05, W271, W813, W936 and W949. W04, W271 and W936 are editorials; W05, W813 and W949 are errata.

**Q18.** 15. This counts W02/W03 and W219/W251 once each.

**Q19.** 27. W03 and W02 are cited by 29 works between them, and W397 and W569 are STG.

**Q20.** 23 preprints, listed in the JSON. Each has a `version_of` target that is present in works.csv.

**Q21.** 46 for Oskel Polytechnic. W780 is a standalone preprint and is counted.

**Q22.** In total, W30 has more (17 against 12). Within its publication year and the two after, W31 has more (12 against 2).

**Q23.** W30 has 17 citations in total and 2 in the window: W60 (2020) and W988 (2021). W878 is an STG citer and is excluded.

**Q24.** 15. A09 and A103 share an ORCID; W268, W714 and W802 are STG and excluded.

**Q25.** 23: W20 14, W21 3, W22 1, W23 1, W366 1, W417 2, W531 1. The other eight works have no citations from non-STG works.

**Q26.** Yes. W23 is a retracted ART at I07 that is still a published record, so it counts. Excluding retractions would change that.

**Q27.** I12 (Université de Lorvain), with 15 citing works, e.g. W20 is cited by W35, W282 and W300. The next highest is I09 with 4 (W357, W586, W32, W777).

**Q28.** 4: W32, W357, W586 and W777.

**Q29.** Author 7, institution 12, country 21. The author-level figure treats A102's W1056 as a different person.

**Q30.** 18, adding W14, W214, W349, W544, W748 and W812 to the 12 from the University of Albury.

**Q31.** 12 works, listed in the JSON. STG records are excluded.

**Q32.** 18 distinct works: 7 direct citers of W01 plus 11 further works that cite those citers.

**Q33.** W20, with 14 citations. W22 only looks higher (19) if the STG citers are counted.

**Q34.** 7: W08, W16, W260, W603, W693, W850 and W956.

**Q35.** 25.

**Q36.** 26.

**Q37.** I04. A08's first affiliation on W70 is the Tessel Laboratory, with I06 listed second.

**Q38.** I06, I04, I03, I02 and I01 (W71 lists I06 first, then I04).

**Q39.** 21 of the University of Albury's works are in S01, the only K3 source.

**Q40.** S01, the only K3 source.

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 13.

**Q43.** Yes. W07 is an ART, and the K0 tier of S04 doesn't change its type.

**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.

**Q45.** 22.

**Q46.** I01. The chain is I06, then I02, then I01.

**Q47.** Rostval has more 2024 works (16 against 14), but it is usually one of 4 authors with only one from I09, so each work gives it about ¼ (16 × ¼ = 4.0). Kesting's 2024 works are mostly written by its own people, so its fractional total is 12.0 and it moves ahead.

**Q48.** The premise is wrong: W70 is one of the University of Albury's works. Its author A08 lists I04 (Tessel), which rolls up through I03 to I02, and I06 (Halloran), which has I02 as its parent.

```json
{
"Q1": {"count": 3},
"Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3": {"same": "no"},
"Q4": {"count": 9},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 23},
"Q8": {"parent": "I01"},
"Q9": {"count": 119},
"Q10": {"count": 175},
"Q11": {"count": 70},
"Q12": {"full": 14, "fractional": 12},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 49, "fractional": 44.67},
"Q15": {"count": 27},
"Q16": {"count": 90},
"Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
"Q18": {"count": 15},
"Q19": {"count": 27},
"Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21": {"count": 46},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 17, "in_window": 2},
"Q24": {"count": 15},
"Q25": {"count": 23},
"Q26": {"counts": "yes"},
"Q27": {"institution": "I12", "citing_works": 15},
"Q28": {"count": 4},
"Q29": {"author": 7, "institution": 12, "country": 21},
"Q30": {"count": 18},
"Q31": {"works": ["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W922","W1042"]},
"Q32": {"count": 18},
"Q33": {"work": "W20"},
"Q34": {"count": 7},
"Q35": {"count": 25},
"Q36": {"count": 26},
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I06","I04","I03","I02","I01"]},
"Q39": {"count": 21},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 13},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45": {"count": 22},
"Q46": {"parent": "I01"}
}
```