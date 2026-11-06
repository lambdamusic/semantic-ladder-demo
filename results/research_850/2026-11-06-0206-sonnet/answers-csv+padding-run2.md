Assumptions: "research works" are ART, REV and PPR records. A preprint is merged into the work it is a version of. EDT, ERR, PTX and SUP records are not research works. STG (staging) records are excluded, together with the citations they make. Retracted works are kept. Tier K3 is read as the highest, though the data does not define the scale. Counts were done by hand over a large dataset, so slips are possible.

**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229.
**Q2.** 32 works, listed in the JSON. They come from A01 and its same-ORCID records A02, A03 and A101.
**Q3.** No. W37 has A05 (ORCID 0001-6105-5008) and W38 has A06 (ORCID 0007-5475-1779).
**Q4.** 9. A05 and A104 share an ORCID and together have W14, W37, W554, W565, W702, W725, W785, W792 and W1038. W556 is a preprint of W1038.
**Q5.** No. W08 has A04 (ORCID 0004-8662-8360) and W01 has A01 (ORCID 0002-9841-6229).
**Q6.** A01. Mara Ellison has 23 research works credited to I02, more than A07 and A110, who each have 15.
**Q7.** 23. Of her 32 works, W04, W05, W271, W813, W936 and W949 are not research, and the preprints W02, W612 and W663 merge into W03, W869 and W464.
**Q8.** I01, via I04 → I03 → I02 → I01.
**Q9.** 119.
**Q10.** 176. This is the 119 Albury works plus 57 more from I05, I20 and I21.
**Q11.** 70, covering I07, I08 and I22.
**Q12.** Full 14, fractional 12.
**Q13.** Full: I09 (15 works vs 14). Fractional: I07 (12 vs 3.75).
**Q14.** Full 48, fractional 44.
**Q15.** 27, including the retracted W520 and W922.
**Q16.** 88.
**Q17.** W04, W05, W271, W813, W936 and W949 (editorials and errata).
**Q18.** 15. A108 is a different Priya Ramanathan, with a different ORCID.
**Q19.** 28 works cite W03 or W02 (STG citers excluded).
**Q20.** 23 preprints, listed in the JSON.
**Q21.** 46.
**Q22.** W30 has more in total (17 vs 12). W31 has more in its window (12 vs 2).
**Q23.** W30 has 17 citations in total and 2 in 2019–2021 (W60 and W988).
**Q24.** 15. A09 and A103 share an ORCID.
**Q25.** 23. The citation counts are W20: 14, W21: 3, W22: 1, W23: 1, W366: 1, W417: 2, W531: 1.
**Q26.** Yes. W23 is retracted but remains a flagged article in the data. Whether to exclude it is a policy choice the data does not settle.
**Q27.** I12, with 16 citing works.
**Q28.** 4 (W32, W357, W586, W777).
**Q29.** Author level 7, University of Albury level 12, country level 21.
**Q30.** 18 at Albury University System level.
**Q31.** 12 works.
**Q32.** 18 works.
**Q33.** W20, with 14 citations. W22's other citers are all STG.
**Q34.** 7.
**Q35.** 24.
**Q36.** 26.
**Q37.** I04, the first-listed affiliation (affil_seq 1) of A08. I06 is listed second.
**Q38.** I06 and I04, plus their parents I03, I02 and I01.
**Q39.** 21 works in S01.
**Q40.** S01 (K3), assuming K3 is the highest tier.
**Q41.** No, on the same assumption that a larger K number means a higher tier.
**Q42.** 13.
**Q43.** Yes. W07 is an article (ART).
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22.
**Q46.** I01, via I06 → I02 → I01.

**Q47.** Under full counting Rostval has more 2024 works (15 vs 14). Each of its 15 works carries only one Rostval author out of four (0.25 each, 3.75 in total). Kesting's works are mostly written by its own authors (12 in total), so Kesting leads under fractional counting.

**Q48.** The premise is wrong: W70 is one of the University of Albury's works. Its author A08 lists I04, and I04 → I03 → I02 rolls up to the University of Albury. The second affiliation I06 also sits under I02.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":23},
"Q8":{"parent":"I01"},
"Q9":{"count":119},
"Q10":{"count":176},
"Q11":{"count":70},
"Q12":{"full":14,"fractional":12},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":48,"fractional":44},
"Q15":{"count":27},
"Q16":{"count":88},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":28},
"Q20":{"works":["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21":{"count":46},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":17,"in_window":2},
"Q24":{"count":15},
"Q25":{"count":23},
"Q26":{"counts":"yes"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":7,"institution":12,"country":21},
"Q30":{"count":18},
"Q31":{"works":["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W922","W1042"]},
"Q32":{"count":18},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":24},
"Q36":{"count":26},
"Q37":{"institution":"I04"},
"Q38":{"institutions":["I06","I04","I03","I02","I01"]},
"Q39":{"count":21},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":13},
"Q43":{"research":"yes"},
"Q44":{"institutions":["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45":{"count":22},
"Q46":{"parent":"I01"}}
```