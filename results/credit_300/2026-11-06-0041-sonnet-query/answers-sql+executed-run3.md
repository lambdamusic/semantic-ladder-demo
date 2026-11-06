**Q1.** A-. E01's FC issuer rating was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01 was downgraded in 2025 (A02). On 2026-02-10 it was affirmed at BBB with a Negative outlook (A03).

**Q3.** No. I02 is rated BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E02, merged with E03, has been A/POS since 2025-09-15 (A09).

**Q5.** The holder takes E02's credit risk (Northwind Holdings, the guarantor), which is rated A. I03 has guarantor E02 and is rated A (A11).

**Q6.** Valdoria's Country Ceiling of BB (VD, from 2025-04-01) caps the foreign-currency rating. E05's FC rating is BB (A14) and its LC rating is BBB- (A13).

**Q7.** 31 issuers had a downgrade effective in 2026; they are listed in the JSON. This counts LTIDR downgrades on the rating scale, including E08 and E10, and excludes withdrawals.

**Q8.** E08. Its rating has been RD since 2026-07-08 (A22).

**Q9.** 278. This is the number of distinct entities with a current LTIDR that is not WD. It includes the sovereign CV, and E1279, whose LC rating is still active.

**Q10.** Depends. E05 is BB in foreign currency (investment grade is BBB- or higher, so sub-investment grade) but BBB- in local currency (investment grade).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30. The RWN period and the later affirmation are not downgrades.

**Q14.** None. E12's first rating began on 2024-02-01 (A30).

**Q15.** A-. E10 was A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+/Stable on 2025-01-01 and is BBB+/Stable now. The watch in between did not change the rating.

**Q17.** No. E06's rating is still A-; on 2026-09-03 it was only placed on Rating Watch Negative (A17).

**Q18.** 32 issuers were on RWN on 2026-10-01; they are listed in the JSON.

**Q19.** 28 issuers had a Negative outlook (with no RWN) on 2026-10-01; they are listed in the JSON.

**Q20.** No. E07's rating was withdrawn (WD, A19), not set to a default rating.

**Q21.** 35 entities had an issuer rating before but only WD on 2026-10-01; they are listed in the JSON.

**Q22.** E08. It is the only entity with an RD or D rating in the data (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. This is the number of instruments with a current INST rating of BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. The data holds no rating for VD.

**Q30.** E15, E1039 and E1194 are at the CV ceiling of A. E05, E1236, E1101, E1126 and E1028 are at the VD ceiling of BB.

**Q31.** No. No non-sovereign with a CV or VD FC rating is above the ceiling of A or BB respectively.

**Q32.** E09.

**Q33.** The holder takes E10's credit risk (Halden Bank, the guarantor), which is rated BBB+ (A27, A29).

**Q34.** No. E12 has no parent and is not in E09's group.

**Q35.** 3: E09, E10 and E11. E17 is merged into E10.

**Q36.** 2: E02 and E04.

**Q37.** 331. The entities table has 331 distinct entity_ids, after merging.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) are separate entities with different LEIs.

**Q39.** A (A09).

**Q40.** 66. This counts GB-domiciled entities with a current non-WD LTIDR.

**Q41.** None. No entity or record named Brindle Capital exists in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is flagged local_currency=yes and is denominated in XVD.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency obligation rated BBB- (A45).

**Q46.** No. E11 has no ratings of its own; only its instrument I05 is rated.

**Q47.** None. I08 has no rating record.

**Q48.** 106. This is the number of instruments with a current INST rating that is not WD.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1058","E1167","E1080","E1151","E1294","E1064","E1093","E1228","E1229","E1255","E1263","E1298","E1307","E1163","E1213","E1300","E1053","E1057","E1144","E1159","E1243","E08","E1112","E1169","E1186","E10","E1160","E1034","E1285","E1290","E1051"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":278},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1109","E1168","E1181","E06","E1133","E1088","E1194","E1066","E1146","E1203","E1314","E1323","E1006","E1019","E1264","E1013","E1061","E1238","E1297","E1099","E1132","E1260","E1039","E1059","E1266","E1098","E1126","E1267","E1037","E1209","E1242","E1317"]},
"Q19":{"issuers":["E09","E1211","E1228","E1263","E1034","E1188","E1248","E1005","E1080","E1072","E1190","E1105","E1158","E1079","E1271","E01","E1064","E1118","E1261","E1029","E1160","E1055","E1294","E1046","E1056","E1059","E1282","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1076","E1062","E1244","E1316","E1121","E1205","E1277","E1218","E1001","E1124","E1172","E1200","E1225","E1233","E1234","E07","E1021","E1166","E1206","E1219","E1320","E1041","E1063","E1107","E1138","E1140","E1048","E1084"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1236","E1101","E1126","E1028"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":331},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```