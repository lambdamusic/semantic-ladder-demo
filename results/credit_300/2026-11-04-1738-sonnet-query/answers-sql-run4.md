**Q1.** A-. Kestrel Energy (E01) was rated A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. The only 2026 action, A03, is an affirmation at BBB with a Negative outlook.

**Q3.** No. The 2031 note I02 is subordinated and was cut to BB+ by A07, which is below investment grade.

**Q4.** Positive. E03 shares Northwind Holdings' LEI (213800PHEIYNJMHTDV74) with E02, so it is a duplicate record of the same entity. Its latest action, A09 (2025-09-15), has a POS outlook and supersedes E02's STA from A08.

**Q5.** The guarantor, Northwind Holdings (E02). I03 is issued by E04 and guaranteed by E02, and the note is rated A.

**Q6.** Valdoria Telecom's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB equals the Republic of Valdoria's Country Ceiling of BB (A12), which caps foreign-currency ratings.

**Q7.** The 43 issuers listed in the JSON had a downgrade of their issuer rating (action DG) dated between 2026-01-01 and today (2026-11-04). This includes E08, whose downgrade took it to RD. Actions dated after today are excluded.

**Q8.** E08 (Saxby Shipping). A22 downgraded it to RD on 2026-07-08 after a distressed debt exchange.

**Q9.** 291. These are the distinct issuers whose latest long-term issuer rating on 2026-10-01 was not a withdrawal, deduplicated by LEI.

**Q10.** Depends. The foreign-currency rating is BB (not investment grade) and the local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 cut Marlow Utilities from A- on 2024-09-30.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. The downgrade A27 only came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ after A35 (watch) and A33 (affirmation).

**Q17.** No. Orrin Bank's only 2026 action, A17, is a Rating Watch Negative at an unchanged A-.

**Q18.** The 30 issuers listed in the JSON. This uses the latest foreign-currency rating on 2026-10-01 being on Rating Watch Negative.

**Q19.** The 37 issuers listed in the JSON. This uses the latest foreign-currency rating on 2026-10-01 carrying a Negative outlook.

**Q20.** No. Pellam Retail (E07) has a withdrawal (A19, "commercial reasons"), not a default rating.

**Q21.** The 35 entities listed in the JSON, whose latest issuer rating by 2026-10-01 was a withdrawal. E1279 is excluded because it still had a local-currency rating.

**Q22.** E08 is the only entity ever rated RD or D.

**Q23.** F2, from A04.

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66. These are instruments whose latest rating on 2026-10-01 was BBB- or better and had not expired.

**Q26.** A+, from A40.

**Q27.** A-. I06 is a subordinated note with rating A42.

**Q28.** BBB+, from A38.

**Q29.** None. Valdoria (VD) only has a Country Ceiling (A12, BB) and no issuer rating.

**Q30.** E1039, E1194, E15 (Corvenia, ceiling A) and E05, E1028, E1101, E1126, E1236 (Valdoria, ceiling BB). The ceilings are taken from the Country Ceiling records A37 and A12.

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09 (Halden Group). E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10). I05 is guaranteed by E10 and is rated BBB+ after A29.

**Q34.** No. Halden Foods (E12) has no parent and is not linked to the E09 group.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 344. There are 370 records, 26 of which are duplicate LEIs (342 distinct LEIs), plus the two sovereigns that have no LEI.

**Q38.** No. They have different LEIs, countries and no link.

**Q39.** A, from A09 (applied to E02 through the shared LEI).

**Q40.** 74. These are GB-domiciled issuers with a non-withdrawn issuer rating on 2026-10-01, deduplicated by LEI.

**Q41.** BB+, from A44.

**Q42.** DE. E10 is the RATINGS record, while E17 (LU) is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, duplicates E10, which is domiciled in DE. This is a judgement call, since counting E17 would give 1.

**Q44.** Yes. The note I07 is denominated in XVD, which appears to be Valdoria's own currency. The data does not define this code, so this is an inference.

**Q45.** No. The Country Ceiling (BB) caps foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. Halden Leasing (E11) only has a CO rating (A46), no issuer rating.

**Q47.** None. I08's only action, A47, is an EX on 2026-09-01, so it has no current rating.

**Q48.** 106. These are instruments with an INST rating on 2026-10-01 that had not been marked EX.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1170","E1159","E1057","E1299","E1243","E1053","E1144","E1064","E1343","E1093","E1350","E1151","E1294","E1347","E1051","E1307","E1228","E1349","E1263","E1255","E1229","E1345","E1344","E1080","E08","E1112","E1186","E1348","E16","E1346","E1340","E10","E1351","E1161","E1342","E1163","E1213","E1300","E1285","E1290","E1058","E1167"]},
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
"Q18":{"issuers":["E1037","E1126","E1132","E1168","E1006","E1133","E1203","E1260","E1317","E1210","E1264","E1267","E1109","E1061","E1323","E1066","E1098","E1266","E1314","E06","E1297","E1013","E1146","E1181","E1238","E1099","E1088","E1194","E1039","E1242"]},
"Q19":{"issuers":["E1055","E1263","E1340","E09","E1079","E1105","E1161","E1228","E1262","E1005","E1300","E1072","E1211","E1282","E01","E1188","E1190","E1344","E1347","E1029","E1046","E1064","E1248","E1294","E1342","E1060","E1350","E1351","E1056","E1343","E1348","E1034","E1080","E1118","E1158","E1345","E1271"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1007","E1254","E1308","E1124","E1320","E1002","E1021","E1041","E1140","E1219","E1244","E1172","E1048","E1107","E1032","E1062","E1138","E1159","E1166","E1205","E1234","E1316","E1057","E1063","E1155","E07","E1084","E1200","E1218","E1277","E1121","E1225","E1233","E1076","E1206"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E05","E1028","E1101","E1126","E1236"]},
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