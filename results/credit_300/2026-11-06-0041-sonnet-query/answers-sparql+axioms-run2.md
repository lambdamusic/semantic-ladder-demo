**Q1.** A-. Kestrel's long-term issuer rating (LTIDR) A01 was A- from 2024-03-12 to 2025-06-20.
**Q2.** No. A03 (2026-02-10) was an affirmation with a Negative outlook; the downgrade, A02, was in 2025.
**Q3.** No. The 2031 note I02 is rated BB+ (A07), below investment grade.
**Q4.** Positive. A09 on E03 (the same entity as E02) is A with a Positive outlook.
**Q5.** The credit risk of E02 (Northwind Holdings), which guarantees I03. E02/E03 is rated A.
**Q6.** Valdoria's Country Ceiling is BB (A12). Its foreign-currency rating is therefore BB (A14), below its local-currency rating of BBB- (A13).
**Q7.** The 2026 downgrades are the issuers in the JSON list, including E08, E10 and E16. This list is not merged across duplicate records of the same entity.
**Q8.** E08 (Saxby Shipping), rated RD in A22.
**Q9.** 278. There are 279 entity records with an issuer rating in force, which merge to 278 distinct entities.
**Q10.** Depends. Its foreign-currency rating is BB (non-investment grade) and its local-currency rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. Only A36 is a downgrade for E14.
**Q14.** None. Halden Foods' first rating, A30, started on 2024-02-01.
**Q15.** A- (A26, E10).
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33); the Rating Watch in between did not change the level.
**Q17.** No. A17 only placed the A- rating on Rating Watch Negative.
**Q18.** The 32 entities in the JSON list, with watch-RWN in force.
**Q19.** The 28 entities in the JSON list, with a Negative outlook in force.
**Q20.** No. A19 is a withdrawal (WD) for commercial reasons, not a default.
**Q21.** The entities in the JSON list. Each had an issuer rating that was later withdrawn, and neither it nor a linked record holds one now.
**Q22.** E08 only, rated RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 66 of the 106 rated instruments held an investment-grade rating.
**Q26.** A+ (A40, local-currency basis).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria only has a Country Ceiling of BB (A12) in the data.
**Q30.** Corvenia's ceiling is A and Valdoria's is BB. Entities rated exactly at their ceiling are in the JSON list.
**Q31.** No. No company's foreign-currency issuer rating is above its country's ceiling.
**Q32.** E09 (Halden Group plc).
**Q33.** The credit risk of E10 (Halden Bank), which guarantees I05. It is rated BBB+ (A27).
**Q34.** No. Halden Foods (E12) is its own ultimate parent, while Halden Bank's ultimate parent is E09.
**Q35.** 3 distinct legal entities: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2 distinct legal entities: E02 (the same entity as E03) and E04.
**Q37.** 344 distinct legal entities, after merging the 370 records linked by sameEntityAs.
**Q38.** No. E06 and E13 have no sameEntityAs link, and they have different LEIs and domiciles (DE and US).
**Q39.** A (A09).
**Q40.** 66 distinct GB-domiciled entities hold an issuer rating, merging duplicate records.
**Q41.** BB+ (A44). That record is not flagged as in force in the store, so this is the latest action, not a confirmed in-force rating.
**Q42.** LU.
**Q43.** 1. E10 and E17 are the same entity.
**Q44.** Yes. I07 has localCurrency = true (currency XVD).
**Q45.** No. I07 is a local-currency note, and the Country Ceiling constrains foreign-currency ratings. Its BBB- rating (A45) would sit above the BB ceiling only if the ceiling applied to it.
**Q46.** No. Halden Leasing (E11) only has a counterparty obligation rating (A46, BBB).
**Q47.** A (A47).
**Q48.** 106 instruments held a rating in force.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":278},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E1039","E1194","E15","E1028","E1101","E1126","E05","E1236"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":344},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":66},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":106}}
```