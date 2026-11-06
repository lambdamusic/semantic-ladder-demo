**Q1.** 1. A01, A02 and A03 all carry ORCID 0000-0002-9841-6229, so they are one person.

**Q2.** The works found under that ORCID (A01, A02, A03, A101) are listed in the JSON. Up to 18 rows of the query were hidden, so the list may be incomplete.

**Q3.** No. W37 is by A05 (ORCID …6105) and W38 is by A06 (ORCID …5475).

**Q4.** 9. The works are W1038 (with its preprint W556), W14, W37, W554, W565, W702, W725, W785 and W792.

**Q5.** No. W08's M. Ellison is A04 (ORCID …8662), which differs from Mara's ORCID.

**Q6.** A01 (Mara Ellison, ORCID …9841), with 19 research works credited to I02.

**Q7.** 19. I counted from the visible rows. I excluded the editorials, errata, retracted works and K0-source works, and merged each preprint into its published version.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 95. This is the sum of the per-year counts for I02.

**Q10.** 140. This is the sum of the per-year counts for I01.

**Q11.** 59. This is the sum of the per-year counts for I07.

**Q12.** Full counting gives 13 for I07 in 2024. The fractional query failed, so the fractional figure (6) is an estimate.

**Q13.** Full counting favours I09 (16 against 13). The fractional winner is I07, inferred from the swap noted in Q47, not computed.

**Q14.** The query for this failed. Both figures (36 and 30) are estimates.

**Q15.** 25. This is the S02 count for 2024.

**Q16.** 88. This is the sum of the per-year counts for S01.

**Q17.** The non-research works by document type are W04 and W271 and W936 (editorials), and W05, W813 and W949 (errata).

**Q18.** 15, counted under Priya's ORCID.

**Q19.** 27 distinct citing works, counted across W02 and W03.

**Q20.** The 23 preprints that name a published version are listed in the JSON, taken from the versionOf query.

**Q21.** 45. This is the sum of the per-year counts for I14.

**Q22.** W30 has more citations in total (16 against 11). W31, counting W42, has more within its window (11 against 2).

**Q23.** W30 has 16 citations in total. Within 2019–2021 it has 2: one in 2020 and one in 2021.

**Q24.** 12. The retracted works W23, W1025 and W693 and the staging works W268, W714 and W802 are excluded.

**Q25.** 20, as distinct citing works across her 12 research works.

**Q26.** No. W23 is retracted.

**Q27.** I12, with 12 citing works.

**Q28.** 4.

**Q29.** Author level 7, institution level 10 and country level 20.

**Q30.** 14.

**Q31.** The works that cite a work citing W01 are listed in the JSON, with W895 counted in both hops.

**Q32.** 17. That is 7 works citing W01 directly and 10 further works at two hops.

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 25. This is the sum of the per-year counts for I08.

**Q36.** 36. This is the sum of the per-year counts for S06.

**Q37.** I06. W70's author listed I04 with sequence 1 and I06 with sequence 2, and the highest sequence is the one credited.

**Q38.** I04, I03, I02 and I01. For W71 the author's last-listed affiliation is I04, which sits under I03, I02 and I01.

**Q39.** 19.

**Q40.** S01.

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 0. S04 is delisted (K0).

**Q43.** No. W07 appeared in S04, which is K0.

**Q44.** I02, I03, I04, I05, I19 and I20. I06 and I21 are affiliated institutes, so they are not parts of the system.

**Q45.** 16. This is the sum of the per-year counts for I06.

**Q46.** I06. It is an affiliated institute, so its ultimate parent is itself.

**Q47.** Under full counting, I09 leads with 16 against 13 for I07. I assume I09's works have more authors, so fractional shares are smaller. I did not verify this, because the fractional query failed.

**Q48.** W70's author listed I04 (sequence 1) and I06 (sequence 2). Only the last-listed affiliation, I06, is credited. I06 is an affiliated institute, so its work is never credited to I02.

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
"Q12":{"full":13,"fractional":6},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":36,"fractional":30},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
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
"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I06"}}
```