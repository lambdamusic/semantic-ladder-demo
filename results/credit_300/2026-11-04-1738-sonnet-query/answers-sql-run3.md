**Q1.** A-. Kestrel Energy plc (E01) was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).
**Q2.** No. E01's only 2026 action is an affirmation at BBB with a Negative outlook (A03, 2026-02-10).
**Q3.** No, it is BB+. Note I02 was cut from BBB to BB+ on 2025-06-20 (A07), which is below investment grade.
**Q4.** Positive. Northwind Holdings has two records, E02 and E03, with the same LEI. The latest action is A09 (E03, 2025-09-15), an affirmation at A with a Positive outlook.
**Q5.** The guarantor, Northwind Holdings (E02). I03 is issued by E04 and guaranteed by E02, whose latest rating is A (A09).
**Q6.** Valdoria's Country Ceiling is BB (VD, A12) and it caps the foreign-currency rating. E05's foreign-currency rating is therefore BB (A14), while its local-currency rating is BBB- (A13). The data records the ceiling but not an explicit explanation.
**Q7.** 44 issuers have a 2026 downgrade (DG) action up to today, 2026-11-04; the full list is in the JSON. Duplicate research records are mapped to their RATINGS record by shared LEI. E1341's downgrade is dated 2026-11-09, after today, so it is excluded.
**Q8.** Saxby Shipping (E08) was in default. It was downgraded to RD on 2026-07-08 (A22) with no later action.
**Q9.** 291. These are distinct LEIs whose latest issuer rating on 1 October 2026 is not a withdrawal.
**Q10.** Depends. E05 is BBB- (investment grade) on a local-currency basis (A13) but BB (not investment grade) on a foreign-currency basis (A14).
**Q11.** BBB+. Marlow Utilities (E14) was downgraded from A- to BBB+ on 2024-09-30 (A36).
**Q12.** A-, from A34.
**Q13.** 1, which is A36.
**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).
**Q15.** A-. Halden Bank (E10) was cut to BBB+ only on 2026-04-15 (A27).
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+; the watch in A35 ended with the affirmation in A33.
**Q17.** No. Orrin Bank (E06) was placed on Rating Watch Negative at A- on 2026-09-03 (A17), which is not a downgrade.
**Q18.** 32 issuers, listed in the JSON. Their latest issuer action on or before 2026-10-01 carries a Rating Watch Negative flag.
**Q19.** 37 records with a Negative outlook as their latest action, listed in the JSON as 37 issuers after mapping duplicates (E1060 to E1059, E1161 to E1160).
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not for default; the only default-level rating in the data is E08's RD.
**Q21.** 34 entities, listed in the JSON. Each had an issuer rating that was later withdrawn, and no rating on any currency basis remains on 1 October 2026. I excluded E1106 and E1279, which still hold a rating on the other currency basis, and E08, which holds RD.
**Q22.** Only Saxby Shipping (E08), through its RD rating (A22).
**Q23.** F2, from A04.
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 66. These are instruments whose latest action on or before 2026-10-01 is not an expiry (EX) and whose rating is BBB- or better.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling of BB (A12) and no issuer rating.
**Q30.** Eight entities. Corvenia's ceiling is A (A37) and Valdoria's is BB (A12). The foreign-currency issuer ratings at those levels are A for E15, E1039 and E1194, and BB for E05, E1236, E1101, E1126 and E1028.
**Q31.** No. No Corvenian foreign-currency issuer rating is above A and no Valdorian one is above BB.
**Q32.** Halden Group plc (E09). The chain is E11 to E10 to E09.
**Q33.** The guarantor, Halden Bank (E10). I05 is issued by E11 and guaranteed by E10, whose current rating is BBB+ (A27).
**Q34.** No. Halden Foods (E12) has no parent link to E09, so it is not in the group that contains Halden Bank.
**Q35.** 3: E09, E10 and E11. E17 is a research duplicate of E10, sharing its LEI.
**Q36.** 2: E02 and E04. E03 is a duplicate of E02.
**Q37.** 344. This counts distinct LEIs, with an entity ID standing in where there is no LEI (the sovereigns).
**Q38.** No. They have different LEIs and different countries (E06 is in DE, E13 in US).
**Q39.** A. The ratings of E02 and E03 are both A (A08, A09), and E03 has the same LEI as E02.
**Q40.** 74. These are distinct GB-domiciled LEIs with a non-withdrawn issuer rating on 1 October 2026.
**Q41.** BB+. Brindle Capital (E16) was downgraded on 2026-06-01 (A44); the record comes from the QA source system.
**Q42.** DE. The RATINGS record E10 says DE, and the research duplicate E17 says LU. I took the RATINGS record as authoritative.
**Q43.** 0. The only LU record is E17, which duplicates E10 (LEI 391200QYPVFF2O9K2039); that entity is domiciled in DE per E10.
**Q44.** Yes, probably. I07 is denominated in XVD, which fits Valdoria's local currency. The data does not define XVD, so this is inferred from the code.
**Q45.** No. The Country Ceiling (BB) applies to foreign-currency ratings, and I07 is a local-currency obligation. I07 is rated BBB- (A45), equal to E05's local-currency rating.
**Q46.** No. E11 has only a Credit Opinion (CO, A46) and no long-term issuer rating.
**Q47.** None. I08's only action is an expiry (EX, A47, 2026-09-01), so it holds no current rating. Its last rating was A.
**Q48.** 106. These are instruments whose latest action on or before 2026-10-01 is not an expiry or a withdrawal.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1298","E1307","E1213","E1080","E1285","E1112","E1263","E1064","E1347","E1348","E1344","E1163","E1053","E1051","E1300","E10","E1034","E1229","E16","E1144","E1159","E1057","E1340","E1228","E1294","E1058","E1342","E1093","E1160","E1343","E1290","E1169","E1350","E1167","E1345","E1351","E1349","E1346"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":291},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1126","E1242","E1066","E1006","E1099","E1181","E1019","E1037","E1317","E1061","E1238","E06","E1059","E1088","E1264","E1210","E1168","E1133","E1132","E1297","E1146","E1266","E1098","E1013","E1039","E1109","E1194","E1203","E1260","E1267","E1314","E1323"]},
"Q19":{"issuers":["E1211","E1340","E1350","E1271","E1263","E1248","E1064","E1105","E1345","E1294","E1300","E1079","E1059","E1190","E1262","E1046","E1342","E01","E1347","E1282","E1348","E1228","E1344","E1055","E1029","E09","E1005","E1034","E1188","E1080","E1158","E1056","E1343","E1351","E1160","E1072","E1118"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
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
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```