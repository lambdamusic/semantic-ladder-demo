**Q1.** A-. A01 set Kestrel Energy (E01) at A- on 2024-03-12, and the next action (A02) came on 2025-06-20, so A- held on 1 Jan 2025.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the downgrade (A02) was in 2025.

**Q3.** No, BB+. I02 was cut to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is a duplicate record of Northwind Holdings. Its latest action, A09 (2025-09-15), is A with a Positive outlook.

**Q5.** The risk is the guarantor's, E02 (Northwind Holdings), rated A. I03 is issued by E04 and guaranteed by E02.

**Q6.** Valdoria's Country Ceiling is BB (A12). Valdoria Telecom's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13). The data does not state the reason explicitly; the ceiling is the likely cause.

**Q7.** 44 issuers had a downgrade action recorded in 2026, listed in the JSON. This counts both foreign-currency and local-currency downgrades and includes some later withdrawn.

**Q8.** E08. Saxby Shipping was rated RD on 2026-07-08 (A22).

**Q9.** 290. 291 rated entity records de-duplicate to 290: 288 distinct LEIs, plus the two sovereigns, which have no LEI. This includes the sovereigns and excludes withdrawn ratings.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-. A34 set E14 at A- on 2023-01-15, before the 2024 downgrade.

**Q13.** 1. Only A36 is a downgrade of E14.

**Q14.** None. E12's first rating (A30) is dated 2024-02-01.

**Q15.** A-. E10 was A- (A26) until the downgrade to BBB+ on 2026-04-15 (A27). E17 is a duplicate record of E10 and has no ratings.

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+ (A35 and A33 are a watch and an affirmation).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17).

**Q18.** 30 issuers, listed in the JSON, were on Rating Watch Negative on 1 October 2026. This uses the latest foreign-currency action, and includes E06.

**Q19.** 37 issuers, listed in the JSON, had a Negative outlook as of their latest foreign-currency action on 1 October 2026.

**Q20.** No. E07's latest action is a withdrawal "for commercial reasons" (A19), not a default.

**Q21.** 36 entities, listed in the JSON, whose latest issuer-rating action by 1 October 2026 was a withdrawal. This includes E07.

**Q22.** E08 is the only entity that has ever been rated RD, D or SD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 69. Of 112 instruments carrying a rating on 1 Oct 2026, 69 were BBB- or better.

**Q26.** A+ (A40, local-currency basis).

**Q27.** A- (A42 on I06).

**Q28.** BBB+ (A38, foreign-currency basis).

**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling of BB (A12), with no issuer rating.

**Q30.** Corvenia's ceiling is A and Valdoria's is BB. At the ceiling: E1039, E1194 and E15 (A, CV); E1028, E1101, E1126, E05 and E1236 (BB, VD).

**Q31.** No. No Corvenia company is rated above A and no Valdoria company is above BB.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The risk is the guarantor's, E10 (Halden Bank), rated BBB+ (A27). I05 is issued by E11 and guaranteed by E10.

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 (same LEI).

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 344. There are 370 entity records but 342 distinct LEIs, plus the 2 records with no LEI.

**Q38.** No. They have different LEIs, countries (DE vs US) and no parent link.

**Q39.** A, from the E02/E03 records (A08 and A09).

**Q40.** 74. This counts distinct LEIs among GB-domiciled entities with a current issuer rating.

**Q41.** BB+. E16 was downgraded from BBB- on 2026-06-01 (A44).

**Q42.** DE (E10). E17 is a duplicate record of E10 that carries LU.

**Q43.** 0. The only LU record, E17, shares its LEI with E10, which is domiciled in DE. Counted by record, it would be 1.

**Q44.** Yes. I07 is denominated in XVD, which is Valdoria's currency.

**Q45.** No. The ceiling constrains foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion of BBB (A46), not an issuer rating.

**Q47.** A (A47, action EX).

**Q48.** 112 instruments.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":290},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":69},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E1039","E1194","E15","E1028","E1101","E1126","E05","E1236"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":344},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":74},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":112}}
```