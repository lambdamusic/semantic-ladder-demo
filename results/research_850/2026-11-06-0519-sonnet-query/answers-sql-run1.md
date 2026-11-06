**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229, while A04 (0000-0004-8662-8360) and A102 (0000-0008-4738-8328) are different people.
**Q2.** 32 works, listed in the JSON: all works of A01, A02, A03 and A101, including the editorials, errata and preprints.
**Q3.** No. W37 is by A05 (I05) and W38 is by A06 (I12), and their ORCIDs differ.
**Q4.** 9. These are the distinct research works (articles, reviews and preprints, with preprints collapsed into their published version) of ORCID 0000-0001-6105-5008, which covers A05 and A104.
**Q5.** No. W08 is by A04, whose ORCID differs from Mara's (A01).
**Q6.** A01. Mara (ORCID 0000-0002-9841-6229) has 23 distinct research works credited to I02 and its units, more than anyone else.
**Q7.** 23 distinct research works. I counted articles, reviews and preprints, merged preprints into their published versions, and kept retracted works.
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9.** 119.
**Q10.** 176.
**Q11.** 89.
**Q12.** Full counting gives 14 and fractional counting gives 12.
**Q13.** Under full counting Rostval Technical University (I09) has more, with 16 against 14. Under fractional counting Kesting University (I07) has more, with 12 against 4.
**Q14.** Full counting gives 48 and fractional counting gives 44.0.
**Q15.** 27.
**Q16.** 97.
**Q17.** W04, W271 and W936 are editorials, and W05, W813 and W949 are errata.
**Q18.** 15. This is A07 only; A108 has a different ORCID.
**Q19.** 30. W02 (the preprint) has 9 citing works and W03 has 26, with 5 in common.
**Q20.** 23 preprints, listed in the JSON, each pointing via `version_of` to a published work that is in the data.
**Q21.** 47.
**Q22.** W30 has more in total, with 18 against 15 for W31 and its preprint W42. W31 has more in its window, with 15 against 2 for W30.
**Q23.** W30 has 18 citations in total, and 2 within 2019–2021 (W60 and W988).
**Q24.** 18. This merges A09 and A103, which share an ORCID.
**Q25.** 42. This sums per-work citation counts and includes the retracted works W23, W693 and W1025.
**Q26.** Yes. W23 is a retracted article, but it is still an article by I07 and nothing in the data excludes retracted works.
**Q27.** I12, with 16 citing works.
**Q28.** 4.
**Q29.** 7 works are author self-citations, 12 are University of Albury self-citations, and 21 are country self-citations.
**Q30.** 18.
**Q31.** 14 works, listed in the JSON.
**Q32.** 20.
**Q33.** W22, with 19 citations.
**Q34.** 26.
**Q35.** 25.
**Q36.** 26.
**Q37.** I04. Its `affil_seq` is 1 on W70, while I06 is the second affiliation.
**Q38.** I06 (primary on W71), I04, and their ancestors I03, I02 and I01.
**Q39.** 21. S01 is the only K3 source.
**Q40.** S01.
**Q41.** No. S03 is K1 and S02 is K2.
**Q42.** 13.
**Q43.** Yes. W07 is an article.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22.
**Q46.** I01. The chain is I06 → I02 → I01.
**Q47.** I07's 14 works are mostly written by I07 authors, so they keep nearly their full share and fractional counting gives 12. I09's 16 works have many authors from other institutions, so its share drops to 4.
**Q48.** The premise doesn't hold in the data. W70's primary affiliation I04 sits under I03, I02 and I01, so W70 does count towards the University of Albury (I02), and I could not find any rule that excludes it.

```json
{"Q1":{"count":3},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":23},
"Q8":{"parent":"I01"},
"Q9":{"count":119},
"Q10":{"count":176},
"Q11":{"count":89},
"Q12":{"full":14,"fractional":12},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":48,"fractional":44},
"Q15":{"count":27},
"Q16":{"count":97},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21":{"count":47},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":18,"in_window":2},
"Q24":{"count":18},
"Q25":{"count":42},
"Q26":{"counts":"yes"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":7,"institution":12,"country":21},
"Q30":{"count":18},
"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W844","W895","W90","W922"]},
"Q32":{"count":20},
"Q33":{"work":"W22"},
"Q34":{"count":26},
"Q35":{"count":25},
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