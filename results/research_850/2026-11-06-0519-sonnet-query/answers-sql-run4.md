**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person (A101 shares it too).
**Q2.** 32 works (listed in the JSON), found by pooling the author records that share that ORCID (A01, A02, A03, A101). The list includes editorials, errata, preprints and the retracted W374.
**Q3.** No. A05 and A06 have different ORCIDs.
**Q4.** 9. These are A05's works plus those under A104, which shares its ORCID, minus the preprint W556 of W1038.
**Q5.** No. A04 has a different ORCID from Mara Ellison.
**Q6.** A01 (Mara Ellison), with 22 research works; the next author has 15.
**Q7.** 22. This is her 32 works minus the 6 editorials/errata, the retracted W374, the preprints W612 and W663 (versions of W869 and W464), and W02 (version of W03).
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9.** 117.
**Q10.** 174.
**Q11.** 65.
**Q12.** Full counting gives 14; fractional counting gives 12.0.
**Q13.** Full counting favours I09 (16 vs 14); fractional counting favours I07 (12.0 vs 4.0).
**Q14.** Full counting gives 47; fractional counting gives 43.0.
**Q15.** 25.
**Q16.** 88.
**Q17.** W04, W271 and W936 are editorials; W05, W813 and W949 are errata.
**Q18.** 15, after excluding W05 (erratum) and the preprints W02 and W219.
**Q19.** 30.
**Q20.** 23 preprints point to a work that is also in the data (listed in the JSON).
**Q21.** 47.
**Q22.** W30 has more citations in total (18 vs 13). W31 has more within its publication year and the two years after (13 vs 2).
**Q23.** 18 in total and 2 within the window.
**Q24.** 12, counting A09 and A103 as one person (same ORCID) and excluding retracted works.
**Q25.** 41.
**Q26.** No. W23 is retracted.
**Q27.** I12 (Université de Lorvain), with 16 citing works.
**Q28.** 4.
**Q29.** Author level 7, University of Albury 12, country 21, out of 30 citing works.
**Q30.** 18.
**Q31.** 14 works, listed in the JSON. They cite the 8 direct citers of W01.
**Q32.** 20.
**Q33.** W22, with 19 citations.
**Q34.** 6.
**Q35.** 24.
**Q36.** 26.
**Q37.** I04 (Tessel Laboratory), listed first on W70. The data also credits W70 to I06, so one institution does not fully settle this.
**Q38.** I06 and I04 directly. Through the hierarchy, W71 is also credited to I03, I02 and I01.
**Q39.** 21. The highest tier is K3, which is S01.
**Q40.** S01.
**Q41.** No. S03 is K1 and S02 is K2, so S03 is lower.
**Q42.** 13.
**Q43.** Yes. W07 is a non-retracted article.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22.
**Q46.** I01.
**Q47.** Rostval's 2024 works have many authors, so each work's credit is split into small shares (4.0 in total). Kesting's works have fewer authors, so it keeps 12.0 and moves ahead.
**Q48.** The premise doesn't hold in this data. W70 is credited to I04, which sits under I03 and I02, so it counts as a University of Albury work.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":22},
"Q8":{"parent":"I01"},
"Q9":{"count":117},
"Q10":{"count":174},
"Q11":{"count":65},
"Q12":{"full":14,"fractional":12.0},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":47,"fractional":43.0},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21":{"count":47},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":18,"in_window":2},
"Q24":{"count":12},
"Q25":{"count":41},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":7,"institution":12,"country":21},
"Q30":{"count":18},
"Q31":{"works":["W337","W546","W51","W682","W801","W844","W50","W396","W1042","W895","W338","W52","W90","W922"]},
"Q32":{"count":20},
"Q33":{"work":"W22"},
"Q34":{"count":6},
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