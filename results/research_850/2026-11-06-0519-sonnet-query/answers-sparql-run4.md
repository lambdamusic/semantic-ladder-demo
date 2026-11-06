**Q1.** 1. A01, A02 and A03 all carry ORCID 0000-0002-9841-6229, so they are one person (A101 shares it too). A04 and A102 are different people despite the name "M. Ellison".

**Q2.** 32 works are listed in the JSON, found by pooling A01, A02, A03 and A101 (same ORCID) across all work types.

**Q3.** No. A05 (W37) and A06 (W38) have different ORCIDs.

**Q4.** 9. A05 has 7 research works, and A104 (same ORCID 0000-0001-6105-5008) adds W702 and W725. The preprint W556 is not research output.

**Q5.** No. A04 (W08) has ORCID 0000-0004-8662-8360, which differs from Mara Ellison's.

**Q6.** A01, Mara Ellison. Her ORCID has 22 Albury research works, the most of any author; A07 is next with 15.

**Q7.** 22. This counts articles and reviews that are not retracted and not staging records. It excludes the retracted W374 and the non-research types.

**Q8.** I01. The chain is I04, then I03, then I02, then I01.

**Q9.** 116, for I02 with its units.

**Q10.** 171, for I01 with all its units.

**Q11.** 65. I count only the feed records (60 articles and 5 reviews) and exclude the staging-origin records. This is an interpretation, since the data does not say outright that staging records are excluded.

**Q12.** Full counting gives 14 and fractional counting gives 12.0.

**Q13.** Under full counting, I09 has more (16 against 14). Under fractional counting, I07 has more (12.0 against 4.0).

**Q14.** Full counting gives 47 and fractional counting gives 43.

**Q15.** 25.

**Q16.** 88, excluding staging records.

**Q17.** W02, W612, W663 (preprints), W04, W271, W936 (editorials) and W05, W813, W949 (errata).

**Q18.** 15. Preprints and the erratum are excluded.

**Q19.** 30.

**Q20.** 23 preprints point to a work that is also in the data. They are listed in the JSON, and all their targets are in the data.

**Q21.** 46.

**Q22.** I cannot answer this. The citation-window query failed and I had no rounds left to rerun it.

**Q23.** I cannot answer this, for the same reason as Q22.

**Q24.** 12. A09 has 9 research works and A103 (same ORCID) adds W478, W531 and W686.

**Q25.** 41. The research works of Lena Vossberg that have citations are 7, with 41 citation records among them.

**Q26.** No. W23 is retracted.

**Q27.** I12, Université de Lorvain, with 16 citing works.

**Q28.** 4.

**Q29.** Author level 7, institution level 12 (University of Albury), country level 21 (GB).

**Q30.** 18.

**Q31.** The 14 works in the JSON are the second-hop citers, found by following citations two steps from W01.

**Q32.** 20. These are the 8 direct citers plus 12 additional works at the second hop.

**Q33.** W22, with 19 citations.

**Q34.** 6.

**Q35.** 24.

**Q36.** 26.

**Q37.** I04, the Tessel Laboratory, though the authorship rows also show I06 on W70. The data I retrieved did not settle why W70 is excluded from Albury's output (see Q48).

**Q38.** I04, I03, I02 and I01 (the Tessel Laboratory's chain), plus I06 (Halloran Institute, an affiliate of I02).

**Q39.** 21. These are Albury works in S01, the only K3 source.

**Q40.** S01.

**Q41.** No. S03 is tier K1 and S02 is tier K2.

**Q42.** 13.

**Q43.** Yes. W07 is a non-retracted article from the feed.

**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.

**Q45.** 22.

**Q46.** I01.

**Q47.** I did not query this directly. Rostval's works are co-authored with many people at other institutions, so each Rostval author carries a small share, which gives 4.0 fractionally. Kesting's authors hold larger shares, which gives 12.0.

**Q48.** The data I retrieved does not show it. W70 is a non-retracted 2023 article, and its authorships list I04 and I06, both under I02, so I could not confirm the reason.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":22},
"Q8":{"parent":"I01"},
"Q9":{"count":116},
"Q10":{"count":171},
"Q11":{"count":65},
"Q12":{"full":14,"fractional":12},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":47,"fractional":43},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W02","W04","W05","W271","W612","W663","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W226","W1049","W432","W210","W416","W506","W611","W219","W460","W663","W877","W263","W407","W42","W556","W612","W522","W728","W524","W730","W545","W322","W02"]},
"Q21":{"count":46},
"Q22":{"more_in_total":null,"more_in_window":null},
"Q23":{"total":null,"in_window":null},
"Q24":{"count":12},
"Q25":{"count":41},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":7,"institution":12,"country":21},
"Q30":{"count":18},
"Q31":{"works":["W682","W338","W396","W50","W51","W546","W895","W922","W52","W90","W1042","W337","W801","W844"]},
"Q32":{"count":20},
"Q33":{"work":"W22"},
"Q34":{"count":6},
"Q35":{"count":24},
"Q36":{"count":26},
"Q37":{"institution":"I04"},
"Q38":{"institutions":["I04","I03","I02","I01","I06"]},
"Q39":{"count":21},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":13},
"Q43":{"research":"yes"},
"Q44":{"institutions":["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45":{"count":22},
"Q46":{"parent":"I01"}}
```