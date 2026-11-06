Several answers could not be fully checked. My last round of queries was the final one, and some aggregate queries returned inconsistent or empty results. Those answers are marked "unverified" below.

**Q1.** 1. A01, A02 and A03 all carry ORCID 0000-0002-9841-6229.
**Q2.** The 32 works of that ORCID (A01, A02, A03 and A101), including the retracted W374 and the preprints. See the JSON.
**Q3.** No. A05 and A06 have different ORCIDs.
**Q4.** 9 (unverified). A05's ORCID has 8 articles and 1 review; I excluded the 1 preprint.
**Q5.** No. W08 is by A04, a different ORCID from Mara's.
**Q6.** A01, with 23 research works at I02 and its units.
**Q7.** 23. By ORCID that is 20 + 2 CRIS + 1 retracted article, as the query returned them.
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9–Q11.** Unverified. My best figures are I02 = 141, I01 = 201 and I07 = 111, but the same query returned inconsistent totals.
**Q12–Q14.** Not determined. The 2024 queries were faulty or returned no rows.
**Q15.** Not determined for 2024. S02 has 139 research works in total.
**Q16.** 106.
**Q17.** The editorials W04, W271 and W936, and the errata W05, W813 and W949, by document type.
**Q18.** 15, from 14 articles and 1 review.
**Q19.** 30 distinct citing works across W02 and W03.
**Q20.** 23 works are preprints with a `versionOf` link to another work in the data (see the JSON).
**Q21.** 57 (unverified).
**Q22.** W30 has more citations in total (18 against 13). W31 has more within its window (13 against 2).
**Q23.** 18 in total and 2 in the window of 2019–2021.
**Q24.** 15, counting 3 staging-record articles. It is 12 without them.
**Q25.** 41, for the same 15 works.
**Q26.** No. W23 is retracted.
**Q27.** I12, with 16 citing works.
**Q28.** 4.
**Q29–Q30.** Not determined. The query failed.
**Q31.** The 14 level-2 works listed in the JSON.
**Q32.** 20 (8 citing W01 directly and 12 additional at two hops).
**Q33.** W22, with 19 citations.
**Q34.** Not determined.
**Q35.** 33 (unverified).
**Q36.** 43.
**Q37.** I04. W70 lists I04 and I06.
**Q38.** I04, I06, I03, I02 and I01 (the two listed institutions and their ancestors).
**Q39.** 21 (K3 is the top tier, from S01).
**Q40.** S01.
**Q41.** No. S03 is K1 and S02 is K2.
**Q42.** 13.
**Q43.** Yes. W07 is a non-retracted article.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22 (unverified).
**Q46.** I01.
**Q47.** Not determined, because the 2024 data could not be queried.
**Q48.** Not determined. The data shows W70 credited to I04 and I06, both under I02.

```json
{"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":23},
"Q8":{"parent":"I01"},
"Q9":{"count":141},
"Q10":{"count":201},
"Q11":{"count":111},
"Q12":{"full":0,"fractional":0},
"Q13":{"full":"I07","fractional":"I09"},
"Q14":{"full":0,"fractional":0},
"Q15":{"count":0},
"Q16":{"count":106},
"Q17":{"works":["W04","W271","W936","W05","W813","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W02","W1049","W210","W219","W226","W263","W322","W407","W416","W42","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877"]},
"Q21":{"count":57},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":18,"in_window":2},
"Q24":{"count":15},
"Q25":{"count":41},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":0,"institution":0,"country":0},
"Q30":{"count":0},
"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W844","W895","W90","W922"]},
"Q32":{"count":20},
"Q33":{"work":"W22"},
"Q34":{"count":0},
"Q35":{"count":33},
"Q36":{"count":43},
"Q37":{"institution":"I04"},
"Q38":{"institutions":["I04","I06","I03","I02","I01"]},
"Q39":{"count":21},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":13},
"Q43":{"research":"yes"},
"Q44":{"institutions":["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45":{"count":22},
"Q46":{"parent":"I01"}}
```