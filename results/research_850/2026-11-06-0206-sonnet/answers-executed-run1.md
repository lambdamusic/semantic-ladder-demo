**Q1.** 3 people. "Mara Ellison" is A01, and "M. Ellison" is two separate people (A04, A102, different ORCIDs). The data has no author-record names, so I assumed "Ellison, Mara J." is a variant of A01.

**Q2.** A01 is credited on W01, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048 and W1050 (credits.csv).

**Q3.** No. W37 credits A05 and W38 credits A06, who are separate people with different ORCIDs.

**Q4.** 9 (W14, W37, W554, W565, W702, W725, W785, W792, W1038).

**Q5.** No. W08 credits A04 and W01 credits A01, and people.csv keeps them as different people.

**Q6.** A01, with 19 research works credited to I02.

**Q7.** 19. Mara Ellison's other works are excluded because of type (editorials, errata) or because of retraction or a delisted source.

**Q8.** I01 (I04 → I03 → I02 → I01).

**Q9.** 93, counting I02, I03, I04 and I19 via institution_units. This was a long manual scan, so treat it as approximate.

**Q10.** 138, which is the 93 plus 45 further works credited to I05 or I20. Same manual-scan caveat.

**Q11.** 59, counting credits to I07 and I08.

**Q12.** Full counting gives 13 and fractional gives 11. The 13 works from 2024 are W20, W21, W22, W203, W333, W419, W504, W528, W595, W624, W675, W705 and W1027.

**Q13.** Under full counting Rostval (I09) has more: 15 against 13. Under fractional counting Kesting (I07) has more: 11 against 4.5.

**Q14.** Full counting gives 42 works. Fractional counting gives about 38.83.

**Q15.** 23.

**Q16.** 84.

**Q17.** W04, W05, W271, W813, W936 and W949. These are editorials and errata. Her other non-research works (W07, W374, W449, W763) are excluded for other reasons (delisted source or retraction).

**Q18.** 15 (W01, W03, W13, W72, W251, W262, W292, W293, W435, W553, W598, W758, W787, W833, W969).

**Q19.** 26 works cite W03, which already merges W02.

**Q20.** None. The unmerged PPR works (W18, W221, W306, W336, W566, W745, W747, W780, W781, W824, W1054) have no published counterpart in the data.

**Q21.** 45.

**Q22.** W30 has more citations in total (16 against 11). W31 has more within its publication year and the two years after (11 against 2).

**Q23.** W30 has 16 citations in total and 2 in the window of 2019–2021 (W60, W988).

**Q24.** 12.

**Q25.** 20, from W20 (13), W21 (2), W22 (1), W366 (1), W417 (2) and W531 (1). The other six works have no citations.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12 (Université de Lorvain), with 12 citing works.

**Q28.** 4 (W32, W586, W777, W357).

**Q29.** Author level 7, University of Albury level 10, country level 20, out of 26 citing works.

**Q30.** 14.

**Q31.** W50, W51, W52, W337, W338, W396, W546, W682, W801, W895 and W1042.

**Q32.** 17.

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 25.

**Q36.** 36.

**Q37.** I06 (Halloran Institute). Its only credit, for A08, is to I06.

**Q38.** I04, I03, I02 and I01.

**Q39.** 19.

**Q40.** S01 (tier K3, rank 1).

**Q41.** No. S03 has rank 3 and S02 has rank 2, so S02 is the higher tier.

**Q42.** 0. S04 is delisted, so none of its works are research output.

**Q43.** No. W07 is in S04, which is delisted.

**Q44.** I02, I03, I04, I05, I19 and I20. I06 and I21 have a parent_id but are not listed in institution_units.

**Q45.** 16.

**Q46.** I01. The direct parent is I02, whose parent is I01.

**Q47.** Rostval's works are mostly multi-institution papers, so each earns about 0.25 of a work. Kesting's works are mostly credited to Kesting alone. Rostval therefore leads on full counting (15 against 13) but trails on fractional counting (4.5 against 11).

**Q48.** W70's author A08 is credited to I06 (Halloran Institute, an affiliate), not to the Tessel Laboratory. I06 is not in the University of Albury's unit roll-up in institution_units, despite its parent_id of I02.

```json
{"Q1":{"count":3},
"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":19},
"Q8":{"parent":"I01"},
"Q9":{"count":93},
"Q10":{"count":138},
"Q11":{"count":59},
"Q12":{"full":13,"fractional":11},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":42,"fractional":38.83},
"Q15":{"count":23},
"Q16":{"count":84},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":26},
"Q20":{"works":[]},
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
"Q31":{"works":["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W1042"]},
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
"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I01"}}
```