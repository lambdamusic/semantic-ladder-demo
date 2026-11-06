**Q1.** 1. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229, so they are one person. A04 and A102 are also named M. Ellison but have different ORCIDs.

**Q2.** 32 works: W01, W02, W03, W04, W05, W06, W07, W1005, W1048, W1050, W12, W19, W206, W238, W271, W374, W449, W464, W555, W612, W663, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984. These are the works on any of her four author records, including editorials, errata, a retracted work and works in delisted sources.

**Q3.** No. A05 and A06 have different ORCIDs (…6105-5008 and …5475-1779), so they are different people.

**Q4.** 9. This counts research works on A05 and A104, which share ORCID 0000-0001-6105-5008.

**Q5.** No. W08's author A04 has ORCID …8662-8360, while W01's author A01 has …9841-6229.

**Q6.** A01, with 19 research works credited to I02 and its units. The next highest is A07 with 15.

**Q7.** 19.

**Q8.** I01. I04's parent is I03, then I02, then I01, which has no parent.

**Q9.** 95.

**Q10.** 140.

**Q11.** 59.

**Q12.** Full counting gives 13 and fractional counting gives 11.0.

**Q13.** Under full counting Rostval Technical University (I09) had more, 16 against 13. Under fractional counting Kesting University (I07) had more, 11.0 against 4.0.

**Q14.** Full counting gives 46 and fractional counting gives 42.0.

**Q15.** 25.

**Q16.** 88.

**Q17.** W04, W271 and W936 are editorials, and W05, W813 and W949 are errata. W07, W449 and W763 are also not research output, but because they appeared in delisted sources, not because of their type.

**Q18.** 15.

**Q19.** 27. These are the distinct works citing W03 or its preprint W02, counted once.

**Q20.** W02, W1049, W210, W219, W226, W263, W322, W407, W416, W42, W432, W460, W506, W522, W524, W545, W556, W611, W612, W663, W728, W730, W877. These all have `version_of` set. I did not separately check that each named published version exists in `works`.

**Q21.** 45.

**Q22.** W30 has more in total (16 against 11), and W31 has more within its window (11 against 2).

**Q23.** W30 has 16 citations in total and 2 within its publication year plus two years.

**Q24.** 12.

**Q25.** 20.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12, with 12 citing works. The next highest is I01 with 5.

**Q28.** 4.

**Q29.** Of the 27 citing works, 7 are author self-citations, 10 are University of Albury self-citations and 20 are country self-citations.

**Q30.** 14.

**Q31.** W1042, W337, W338, W396, W50, W51, W52, W546, W682, W801, W895. W01 has 7 direct citers, and these 11 works cite at least one of them.

**Q32.** 17. This is the 7 direct citers plus the second-hop citers, counted once and excluding W01.

**Q33.** W20, with 13 citations. The next highest has 2.

**Q34.** 7.

**Q35.** 25.

**Q36.** 36.

**Q37.** I06. The author of W70 (A08) listed I04 first and I06 last, and only the last-listed affiliation counts.

**Q38.** I04, I03, I02 and I01. On W71 the last-listed affiliation is I04, and credit passes up its chain of parents.

**Q39.** 19.

**Q40.** S01 is the only K3 source.

**Q41.** No. S03 is K1 and S02 is K2, so S03 is lower.

**Q42.** 0. S04 is delisted (K0).

**Q43.** No. W07 appeared in S04, a delisted source.

**Q44.** I02, I03, I04, I19, I05 and I20. The affiliated institutes I06 and I21 are not units of their parents.

**Q45.** 16.

**Q46.** I06. It is an affiliated institute, so its parent link is not followed and it is its own ultimate parent.

**Q47.** Full counting gives each institution one count per work, so Rostval (16) beats Kesting (13). Fractional counting splits each work among its authors, and Rostval's works have many authors credited elsewhere, so its share drops to 4.0 while Kesting keeps 11.0.

**Q48.** W70's credited affiliation is the last one listed, I06, the Halloran Institute. It is an affiliated institute (AFF), so it is not a unit of I02, and the Tessel Laboratory (I04) listed first is ignored.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
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
"Q17":{"works":["W04","W271","W936","W05","W813","W949"]},
"Q18":{"count":15},
"Q19":{"count":27},
"Q20":{"works":["W02","W1049","W210","W219","W226","W263","W322","W407","W416","W42","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877"]},
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
"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W895"]},
"Q32":{"count":17},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":25},
"Q36":{"count":36},
"Q37":{"institution":"I06"},
"Q38":{"institutions":["I04","I03","I02","I01"]},
"Q39":{"count":19},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":0},
"Q43":{"research":"no"},
"Q44":{"institutions":["I02","I03","I04","I19","I05","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I06"}}
```