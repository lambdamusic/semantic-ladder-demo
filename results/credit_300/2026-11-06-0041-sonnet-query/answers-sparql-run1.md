**Q1.** A-. Kestrel's rating on 1 Jan 2025 was still the A- from A01 (2024-03-12); the downgrade to BBB (A02) came on 2025-06-20.

**Q2.** No. A03 on 2026-02-10 was an affirmation at BBB with a Negative outlook.

**Q3.** No. The 2031 note I02 was downgraded to BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (E03, 2025-09-15), with a Positive outlook; E02's A08 was Stable.

**Q5.** E02, rated A. I03's issuer is the finance sub E04, but E02 guarantees it. I03 is rated A (A11) and E02 is rated A.

**Q6.** The data doesn't state a reason. Valdoria's Country Ceiling (A12) is BB, which equals E05's foreign-currency rating (A14), while the local-currency rating is BBB- (A13). That suggests the ceiling caps the foreign-currency rating.

**Q7.** The issuers with a downgrade (DG) action in 2026 are listed in the JSON, 44 in all. They include E08, E10 and E16.

**Q8.** E08. Saxby Shipping was rated RD on 2026-07-08 (A22).

**Q9.** 289. This is distinct issuers by LEI whose latest long-term issuer rating on 1 Oct 2026 was not WD. It includes the Republic of Corvenia (CV), the only sovereign with an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 from A-.

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' first rating (A30) is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-, from A26. The downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 and is still BBB+ (A33). Only a watch was added in A35 and then cleared.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch Negative on A-, which is not a downgrade.

**Q18.** The 32 issuers on Rating Watch Negative are in the JSON.

**Q19.** The 37 issuers with a Negative outlook are in the JSON.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), not defaulted.

**Q21.** Issuers whose latest rating is WD, excluding E1106 and E1279, are in the JSON. Those two still hold a rating on the other currency basis.

**Q22.** E08, which was downgraded to RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 69. This counts instruments whose latest rating on 1 Oct 2026 was BBB- or better, excluding expired ratings.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38 (foreign currency).

**Q29.** None. Valdoria has only a Country Ceiling (BB, A12), not an issuer rating.

**Q30.** The entities in the JSON are rated exactly at their country's ceiling: BB for VD and A for CV.

**Q31.** No. No foreign-currency issuer rating exceeded its ceiling; all were at or below it.

**Q32.** E09, Halden Group plc, through E11 → E10 → E09.

**Q33.** E10, rated BBB+. I05 is issued by E11 but guaranteed by E10, which was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent link to E09, so the data doesn't place it in the group.

**Q35.** 3: E09, E10 and E11. E17 appears to be a research-source duplicate of the bank.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 344. There are 370 entity records, which fall to 344 distinct legal entities after merging records that share an LEI.

**Q38.** No. They are different legal entities, E06 (DE) and E13 (US), with different LEIs.

**Q39.** A, affirmed in A09.

**Q40.** 74, counted by distinct LEI.

**Q41.** BB+, from A44 (downgraded 2026-06-01).

**Q42.** DE (E10). The LU record E17 is a research-source duplicate.

**Q43.** 1 (E17).

**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.

**Q45.** Yes. I07 is rated BBB- (A45), above the BB ceiling (A12).

**Q46.** No. E11 has only a credit opinion (A46, type CO), not an issuer default rating.

**Q47.** None. I08's rating of A was marked expired (EX) on 2026-09-01 (A47).

**Q48.** 112. This counts instruments with a current rating on 1 Oct 2026, excluding expired and withdrawn ones.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":289},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E06","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":69},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1039","E1101","E1126","E1194","E1236","E15"]},
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
"Q48":{"count":112}
}
```