**Q1.** 1. A01, A02, A03 (and A101) share ORCID 0000-0002-9841-6229 and are linked by samePersonAs.
**Q2.** 32 works (19 research works and 13 other records), listed in the JSON. These cover all of Mara's linked author records (A01, A02, A03, A101).
**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.
**Q4.** 9. A05 has research works W1038, W14, W37, W554, W565, W785, W792, W702 and W725.
**Q5.** No. W08's author is A04, whose ORCID differs from Mara's.
**Q6.** A01 (the person Mara Ellison). I did not count at person level in the query, so this is an inference: she has 19 research works against 15 for A07, the best single record.
**Q7.** 19.
**Q8.** I01 (I04 is a unit of I03, which is a unit of I02, which is a unit of I01).
**Q9.** 95 (sum of the yearly counts for I02).
**Q10.** 140.
**Q11.** 59.
**Q12.** Full counting gives 13. I could not compute the fractional figure, because the query returned nothing.
**Q13.** Under full counting, I09 has 16 and I07 has 13, so I09 has more. I could not compute fractional counts. Q47 implies the order swaps, so I07 is my inference.
**Q14.** I could not compute either figure, because the queries returned nothing.
**Q15.** 25.
**Q16.** 88.
**Q17.** W04, W05, W271, W813, W936, W949. These are editorials and errata, so they are excluded by document type. The preprints are excluded as superseded by their published versions, and W374 is retracted.
**Q18.** 15.
**Q19.** 30 distinct citing works (cites of W02 and W03 combined).
**Q20.** 23 preprints, each linked by versionOf to a published version in the data. They are listed in the JSON.
**Q21.** 45.
**Q22.** W30 has more in total (18 against 13). W31 has more within its publication year and the two years after (13 against 2).
**Q23.** W30 has 18 citations in total and 2 in the window 2019–2021 (W60 and W988).
**Q24.** 12.
**Q25.** 20.
**Q26.** No. W23 is retracted, so it is not a ResearchWork.
**Q27.** I12, with 12 citing works.
**Q28.** 4.
**Q29.** 7 at author level, 11 at the University of Albury level, and 21 at country level.
**Q30.** 15.
**Q31.** The 11 works listed in the JSON.
**Q32.** 17.
**Q33.** W20, with 13 citations.
**Q34.** 7.
**Q35.** 25.
**Q36.** 36.
**Q37.** I06.
**Q38.** I01, I02, I03, I04.
**Q39.** I could not determine this, because the tier-rank join returned nothing. The highest tier is K3 (S01).
**Q40.** S01.
**Q41.** No. S03 is tier K1 (rank 3) and S02 is tier K2 (rank 2), so S02 is higher.
**Q42.** 0. S04 is tier K0 and has no ResearchWork records.
**Q43.** No. W07 is not a ResearchWork.
**Q44.** I02, I03, I04, I05, I19, I20. I06 is excluded: its parent is I02, but its derived ultimate parent is itself.
**Q45.** 16.
**Q46.** I06. The data lists I02 as its parent, but its derived ultimate parent is I06 itself.
**Q47/Q48.** I did not get enough data to explain these.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W06","W1005","W12","W238","W464","W676","W1048","W1050","W19","W869","W972","W03","W206","W817","W555","W843","W905","W984","W04","W05","W271","W374","W813","W949","W02","W07","W449","W663","W763","W612","W936"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":19},
"Q8":{"parent":"I01"},
"Q9":{"count":95},
"Q10":{"count":140},
"Q11":{"count":59},
"Q12":{"full":13,"fractional":null},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":null,"fractional":null},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W226","W1049","W432","W210","W416","W506","W611","W219","W460","W663","W877","W263","W407","W42","W556","W612","W522","W728","W524","W730","W545","W322","W02"]},
"Q21":{"count":45},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":18,"in_window":2},
"Q24":{"count":12},
"Q25":{"count":20},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":12},
"Q28":{"count":4},
"Q29":{"author":7,"institution":11,"country":21},
"Q30":{"count":15},
"Q31":{"works":["W682","W1042","W338","W52","W51","W895","W337","W546","W801","W50","W396"]},
"Q32":{"count":17},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":25},
"Q36":{"count":36},
"Q37":{"institution":"I06"},
"Q38":{"institutions":["I01","I02","I03","I04"]},
"Q39":{"count":null},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":0},
"Q43":{"research":"no"},
"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I06"}}
```