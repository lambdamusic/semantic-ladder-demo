**Q1.** A-. Kestrel Energy (E01) was rated A- from A01 (2024-03-12) until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. A03 (2026-02-10) only affirmed BBB; the downgrade was A02 in 2025.

**Q3.** No. The 2031 note (I02) is rated BB+ (A07, 2025-06-20), which is below investment grade.

**Q4.** Positive. E03 is the research duplicate of E02 (same LEI). Its latest action, A09 (2025-09-15), has a Positive outlook and is more recent than A08 (Stable).

**Q5.** A holder takes the credit risk of the guarantor Northwind Holdings (E02), rated A (A08/A09). The issuer is E04 and the guarantor is E02 on I03.

**Q6.** I can't confirm the cause from the data. FC is BB and LC is BBB- (A13/A14), and the Republic of Valdoria's country ceiling (A12) is BB. That is consistent with the ceiling capping the FC rating, but no comment states it.

**Q7.** 43 issuers have a downgrade action (DG) dated in 2026, listed in the JSON. I excluded E1341, whose DG is dated 2026-11-09, after today. I counted entities by action label and did not check each for an actual rating drop; E1051 shows A+ on both of its DG actions.

**Q8.** Saxby Shipping (E08) was in default, rated RD from A22 (2026-07-08).

**Q9.** 290. That is 288 distinct LEIs plus the two sovereigns (CV, VD), counting each issuer's latest long-term issuer rating (LTIDR) that is not WD as of 2026-10-01.

**Q10.** Depends. Valdoria Telecom (E05) is BBB- in local currency (investment grade) and BB in foreign currency (not).

**Q11.** BBB+. Marlow Utilities (E14) was downgraded by A36 on 2024-09-30 and nothing changed before 2025-06-01.

**Q12.** A-, from A34.

**Q13.** 1 time (A36).

**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.

**Q15.** A-. Halden Bank (E10) was cut to BBB+ only on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+; A35/A33 only added and then removed a watch.

**Q17.** No. Orrin Bank (E06) was placed on Rating Watch Negative (A17) with the rating unchanged at A-.

**Q18.** 32 issuers are on Rating Watch Negative, listed in the JSON. This includes watches on local-currency (LC) ratings only (E1019, E1059).

**Q19.** 37 issuers have a Negative outlook, listed in the JSON.

**Q20.** No. Pellam Retail (E07) was withdrawn (WD, A19), not defaulted.

**Q21.** 35 entities, listed in the JSON. Their latest LTIDR action is WD. I left out E1106 and E1279, which withdrew one currency basis but still hold a rating on the other.

**Q22.** Only Saxby Shipping (E08), via A22.

**Q23.** F2 (A04).

**Q24.** Yes. Kestrel's issuer rating is BBB (A03).

**Q25.** 69 instruments held an investment-grade rating on 2026-10-01, out of 112 rated. This counts I08's A (A47, action EX), whose meaning isn't defined in the data.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria has only a country ceiling (A12), BB, and no issuer rating.

**Q30.** Eight entities have an FC rating exactly at their country ceiling. The ceilings are CV = A and VD = BB: E15, E1039 and E1194 at A, and E05, E1028, E1101, E1126 and E1236 at BB.

**Q31.** No. No CV entity is above A and no VD entity is above BB.

**Q32.** Halden Group plc (E09), via E11 → E10 → E09.

**Q33.** A holder takes the guarantor's risk, Halden Bank (E10), rated BBB+ (A27). The issuer is E11 and the guarantor is E10 on I05.

**Q34.** No. Halden Foods (E12) has no parent link; only E10 and E11 link to E09, so the shared name proves nothing.

**Q35.** 3 (E09, E10, E11). E17 is a duplicate of E10 (same LEI).

**Q36.** 2 (E02, E04). E03 is a duplicate of E02.

**Q37.** 344. There are 370 entity records, with 342 distinct LEIs plus the two sovereigns that have none.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A. E02 and E03 both show A.

**Q40.** 74 distinct LEIs.

**Q41.** BB+ (A44, downgraded 2026-06-01).

**Q42.** DE (E10). The duplicate record E17 says LU, but it shares E10's LEI and comes from the RESEARCH source.

**Q43.** 0. The only LU record is E17, which is a duplicate of the DE entity E10. If you count records instead, the answer is 1.

**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency, but the data has no explicit currency-to-country mapping.

**Q45.** No. Its rating is BBB-, above the BB ceiling, but the ceiling constrains foreign-currency obligations and this is a local-currency note.

**Q46.** No. E11 has only a credit opinion (CO, A46), no issuer rating.

**Q47.** A (A47, 2026-09-01). The action code EX isn't defined in the data, so this rating may be provisional or expected.

**Q48.** 112 instruments.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":69},
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
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"A"},
"Q48":{"count":112}
}
```