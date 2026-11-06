**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person. A101 ("M. Ellison") also carries that ORCID, while A04 and A102 are different people.

**Q2.** 32 works. Mara Ellison's records A01, A02, A03 and A101 all share one ORCID, and I included every document type, retracted ones too. The list is in the JSON.

**Q3.** No. W37 is by A05 (ORCID …6105-5008, I05) and W38 is by A06 (ORCID …5475-1779, I12).

**Q4.** 9. A05's ORCID covers W1038, W14, W37, W554, W565, W702, W725, W785 and W792; W556 is a preprint of W1038 and is not counted separately. I counted only ART and REV works that are not retracted.

**Q5.** No. W08's M. Ellison is A04 (ORCID …8662-8360), which differs from Mara Ellison's ORCID.

**Q6.** A01, the Mara Ellison person (A01/A02/A03/A101), with 23 ART/REV works credited to I02 or its units. The next is A07 with 15.

**Q7.** 22. This is her ART and REV works, excluding the retracted W374 and counting the preprints W02, W612 and W663 with their published versions.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 116, from 103 ART and 13 REV that are not retracted. Preprints are assumed to merge with their published versions.

**Q10.** 171, from 151 ART and 20 REV.

**Q11.** 84, from 76 ART and 8 REV. SUP, EDT and PPR are excluded and retracted works are not counted.

**Q12.** Full counting gives 14 and fractional counting gives 12.0.

**Q13.** Full counting: I09 (16 against 14). Fractional counting: I07 (12.0 against about 4.42).

**Q14.** Full counting gives 46 and fractional counting gives about 42.67. These are ART/REV works from 2024 that are not retracted.

**Q15.** 25, from 24 ART and 1 REV that are not retracted.

**Q16.** 95, from 85 ART and 10 REV that are not retracted.

**Q17.** W04, W05, W271, W813, W936 and W949. They are editorials (EDT) and errata (ERR).

**Q18.** 15.

**Q19.** 30 distinct works cite W02 or W03.

**Q20.** W02, W42, W556, W612 and W663. These are the ones I saw in the data; I did not run a full listing, so the list may be incomplete.

**Q21.** 46, from 43 ART and 3 REV.

**Q22.** W31, counting its preprint W42, has more citations in both cases. In total W31 has 13 against 18 for W30... that is wrong on that count: W30 has more in total (18 against 13). Within the publication year and the next two years W31 leads (13 against 2).

**Q23.** W30 has 18 citations in total and 2 within the window (2019–2021).

**Q24.** 15, excluding the retracted W1025, W23 and W693.

**Q25.** 41, from W20 (14), W21 (3), W22 (19), W366 (1), W417 (2), W531 (1) and W967 (1).

**Q26.** No. W23 is retracted.

**Q27.** I12 (Université de Lorvain), with 16 citing works.

**Q28.** 4.

**Q29.** Among the 30 citing works, 7 are self-citations at the author level, 12 at the University of Albury level (units included) and 21 at the country level.

**Q30.** 18.

**Q31.** 14 works: W682, W338, W396, W50, W51, W546, W895, W922, W52, W90, W1042, W337, W801 and W844.

**Q32.** 20. That is 8 works citing W01 directly plus 14 at two hops, with W895 and W844 in both.

**Q33.** W22, with 19 citations.

**Q34.** 25.

**Q35.** 24, from 23 ART and 1 REV.

**Q36.** 26, from 24 ART and 2 REV.

**Q37.** I04, though W70 is also credited to I06 on a second authorship line, so the data does not give a single answer.

**Q38.** I04, I03, I02, I01 and I06. W71's authorship lists I04 and I06, and I04's ancestors are I03, I02 and I01.

**Q39.** 21.

**Q40.** S01, which is tier K3.

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 13, from 11 ART and 2 REV.

**Q43.** Yes. W07 is a non-retracted article.

**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.

**Q45.** 22, from 19 ART and 3 REV.

**Q46.** I01. I06 → I02 → I01.

**Q47.** Kesting has fewer 2024 works than Rostval (14 against 16). Its works have few co-authors, so its fractional share (12.0) is far larger than Rostval's (about 4.4), which comes from works with many authors from elsewhere.

**Q48.** The data does not show that W70 is excluded. I04 sits under I03, which sits under I02, and W70 is a non-retracted 2023 article, so it should count for the University of Albury. If it is excluded, the data I queried does not say why.

```json
{
"Q1":{"count":1},
"Q2":{"works":["W03","W206","W763","W817","W555","W612","W843","W905","W936","W984","W02","W07","W1048","W1050","W19","W449","W663","W869","W972","W01","W04","W05","W06","W1005","W12","W238","W271","W374","W464","W676","W813","W949"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":22},
"Q8":{"parent":"I01"},
"Q9":{"count":116},
"Q10":{"count":171},
"Q11":{"count":84},
"Q12":{"full":14,"fractional":12},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":46,"fractional":42.67},
"Q15":{"count":25},
"Q16":{"count":95},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W02","W42","W556","W612","W663"]},
"Q21":{"count":46},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":18,"in_window":2},
"Q24":{"count":15},
"Q25":{"count":41},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":7,"institution":12,"country":21},
"Q30":{"count":18},
"Q31":{"works":["W682","W338","W396","W50","W51","W546","W895","W922","W52","W90","W1042","W337","W801","W844"]},
"Q32":{"count":20},
"Q33":{"work":"W22"},
"Q34":{"count":25},
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
"Q46":{"parent":"I01"}
}
```