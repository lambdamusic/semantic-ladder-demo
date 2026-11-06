**Q1.** A-. E01's rating was A- (A01, 2024-03-12) until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with a Negative outlook (A03).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action is an affirmation at A with a Positive outlook (A09, 2025-09-15). I did not run a query to re-check this against E02's own records.

**Q5.** The risk is E02, the guarantor of I03, whose issuer is E04. The note is rated A (A10, A11), and I took E02's own rating as A (A08, A09).

**Q6.** The data does not state a reason. Valdoria Telecom's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The Valdoria country ceiling of BB (A12) is consistent with the foreign-currency cap.

**Q7.** 44 entities have a downgrade action in 2026, listed in the JSON, e.g. E08, E10, E16. I did not check whether any of them are duplicate records of the same entity.

**Q8.** E08. It is rated RD (A22, 2026-07-08), and no other entity has an RD, D or SD rating.

**Q9.** 290. There are 291 entity IDs with a latest issuer action on or before 2026-10-01, but two share an LEI, so I counted them once. That count included withdrawn ratings and I did not exclude them.

**Q10.** Depends. It is BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13).

**Q11.** BBB+. E14 was downgraded from A- on 2024-09-30 (A36).

**Q12.** A-. This is the rating assigned on 2023-01-15 (A34).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A-. E10's rating was A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. The rating stayed at BBB+ (A36, A35 and A33 are a watch placement and an affirmation).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement at A- (A17).

**Q18.** 30 entities, listed in the JSON, e.g. E06, E1006.

**Q19.** 37 entities, listed in the JSON, e.g. E01, E09.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19) and there is no default rating on record.

**Q21.** 36 entities whose latest issuer action on or before 2026-10-01 was a withdrawal, e.g. E07, E1002. They are listed in the JSON.

**Q22.** E08, the only entity ever rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66. This counts instruments with a latest rating on or before 2026-10-01 that is investment grade, excluding withdrawn or expired ratings.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), and no issuer rating.

**Q30.** E15, E1039 and E1194 sit at the CV ceiling of A, and E05, E1028, E1101, E1126 and E1236 sit at the VD ceiling of BB. I compared each entity's latest foreign-currency rating with the ceiling.

**Q31.** No. No CV entity is rated above A and no VD entity above BB.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The risk is E10, the guarantor of I05 (issuer E11). E10 is currently rated BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344, counting records that share an LEI once.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A (A09).

**Q40.** 74. This is the count of distinct GB issuers by LEI, using the same latest-action basis as Q9.

**Q41.** BB+ (A44).

**Q42.** DE (E10). The LU record E17 shares E10's LEI and appears to be a duplicate.

**Q43.** 1, E17 only.

**Q44.** Yes. I07 is denominated in XVD, the Valdoria currency.

**Q45.** Yes. The note is rated BBB- (A45), above the BB ceiling (A12).

**Q46.** No. E11 only has a Credit Opinion of BBB (A46), not an issuer rating.

**Q47.** None. I08 was rated A, then its rating expired on 2026-09-01 (A47).

**Q48.** 106. This is the number of instruments with a current rating on 2026-10-01, excluding withdrawn or expired ones.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":290},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```