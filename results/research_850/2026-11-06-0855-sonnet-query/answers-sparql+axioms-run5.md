**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229 and are linked by samePersonAs.

**Q2.** 30 works: W01, W02, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050. W02 is included through Authorship AS-W02-A02-1 (A02), although it has no hasPerson link.

**Q3.** No. W37's Jonas Brandt is A05 and W38's is A06, with different ORCIDs and no samePersonAs link.

**Q4.** 9 research works, counting A05 together with its linked record A104.

**Q5.** No. The M. Ellison on W08 is A04, whose ORCID differs from A01's and who has no samePersonAs link.

**Q6.** A07, with 15 research works credited to I02 and its units.

**Q7.** 19.

**Q8.** I01.

**Q9.** 95.

**Q10.** 140.

**Q11.** 59.

**Q12.** Full counting gives 13 and fractional counting gives 11.

**Q13.** Full counting favours I09 (16 against 13). Fractional counting favours I07 (11 against 4).

**Q14.** Full counting gives 46 and fractional counting gives 42.

**Q15.** 25.

**Q16.** 88.

**Q17.** W04, W271 and W936 are editorials. W05, W813 and W949 are errata.

**Q18.** 15.

**Q19.** 30 distinct citing works, across W02 and W03.

**Q20.** The 23 preprints with a published version in the data are listed in the JSON below.

**Q21.** 45.

**Q22.** W30 has more in total, while W31 has more within its publication year and the two years after (W31 counted 11 against 2 using res:cites).

**Q23.** W30 has 16 citations in total and 2 in the window. The raw Citation records show 18, so the two counts differ. I used the derived res:cites links, which are the citations that count.

**Q24.** 12.

**Q25.** 20.

**Q26.** No. W23 is retracted, so it is not a research work.

**Q27.** I12, with 12 citing works.

**Q28.** 4.

**Q29.** Author level 7, institution level 10, country level 20.

**Q30.** 14.

**Q31.** Ten works: W50, W51, W52, W337, W338, W396, W546, W682, W801, W1042.

**Q32.** 17 (7 direct citers and 10 second-hop citers).

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 25.

**Q36.** 36.

**Q37.** I06. Only AS-W70-A08-2 is credited on W70, and it names I06.

**Q38.** I01, I02, I03 and I04, through W71's credited authorship at I04.

**Q39.** 19.

**Q40.** S01, which is in tier K3 (rank 1).

**Q41.** No. S03 is in K1 (rank 3) and S02 is in K2 (rank 2), so S03 is lower.

**Q42.** 0. No work in the K0-tier S04 is a research work.

**Q43.** No. W07 is not in the ResearchWork class; it appeared in the K0-tier S04, which I infer is why it does not count.

**Q44.** I02, I03, I04, I05, I19 and I20. I06 and I21 are not included, since their ultimate parent is themselves and they do not count towards I01.

**Q45.** 16.

**Q46.** I06 is its own ultimate parent, even though its parent is listed as I02.

**Q47.** I09 has more works, but its authors are mostly at other institutions, so its fractional share is small (4). I07's works are mostly authored by its own people (11).

**Q48.** W70's credited authorship is only the I06 line. The I04 line is an Authorship record that was not carried into the credited institutions, and I06 does not count towards I02.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A07"},
"Q7":{"count":19},
"Q8":{"parent":"I01"},
"Q9":{"count":95},
"Q10":{"count":140},
"Q11":{"count":59},
"Q12":{"full":13,"fractional":11},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":46,"fractional":42},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21":{"count":45},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":16,"in_window":2},
"Q24":{"count":12},
"Q25":{"count":20},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":12},
"Q28":{"count":4},
"Q29":{"author":7,"institution":10,"country":20},
"Q30":{"count":14},
"Q31":{"works":["W50","W51","W52","W337","W338","W396","W546","W682","W801","W1042"]},
"Q32":{"count":17},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":25},
"Q36":{"count":36},
"Q37":{"institution":"I06"},
"Q38":{"institutions":["I01","I02","I03","I04"]},
"Q39":{"count":19},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":0},
"Q43":{"research":"no"},
"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I06"}}
```