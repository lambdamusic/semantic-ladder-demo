**Q1.** A-. E01's rating was A- (A01, 2024-03-12) until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), and the downgrade to BBB came in 2025 (A02).

**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI). Its latest action, A09 (2025-09-15), is an affirmation with a POS outlook, later than E02's STA in A08.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, whose rating is A (A08), and I03 is rated A (A10, A11).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating of Valdoria Telecom (E05) at BB (A14). Its local-currency rating is BBB- (A13).

**Q7.** 42 issuers had a real downgrade in 2026 (listed in the JSON). I counted a "DG" action only when the rating actually fell, which excludes E1064, E1051 on 2026-06-01, and E1229 on 2026-06-02. This includes QA-sourced entities, since the data doesn't say to exclude them, and actions up to today (2026-11-06).

**Q8.** E08 (Saxby Shipping). It was downgraded to RD on 2026-07-08 (A22), after a distressed debt exchange.

**Q9.** 291. This counts distinct LEIs, or entity IDs where there is no LEI, whose latest LTIDR on 1 Oct 2026 was not a withdrawal. It includes the sovereign CV, and the count is 290 without it.

**Q10.** Depends. Valdoria Telecom (E05) is BB in foreign currency (A14), which is not investment grade, and BBB- in local currency (A13), which is.

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36).

**Q12.** A-. This is E14's initial rating (A34, 2023-01-15).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was rated A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and still is. A35 only placed it on Rating Watch Negative, and A33 affirmed BBB+.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement (A17), with the rating unchanged at A-.

**Q18.** 30 issuers (see the JSON), each with a foreign-currency Rating Watch Negative as their latest action on 1 Oct 2026.

**Q19.** 37 issuers (see the JSON), each with a NEG outlook on their latest rating action as of 1 Oct 2026.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 "for commercial reasons" (A19), which is not a default.

**Q21.** 37 entities (see the JSON), each of which had an issuer rating that was later withdrawn (WD) before 1 Oct 2026.

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. These are instruments whose latest rating on 1 Oct 2026 was BBB- or better and had not expired (EX).

**Q26.** A+ (A40).

**Q27.** A-. I06 is a subordinated note issued by E15 (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB) and no issuer rating.

**Q30.** Eight entities. Corvenia's ceiling is A (A37), and E15, E1039 and E1194 are rated A. Valdoria's ceiling is BB (A12), and E05, E1028, E1101, E1126 and E1236 are rated BB.

**Q31.** No. Every CV- and VD-domiciled issuer is at or below its ceiling.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is issued by E11 but guaranteed by E10, whose rating was cut to BBB+ (A27), and I05 itself is also BBB+ (A29).

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3 (E09, E10, E11). E17 is a duplicate record of E10.

**Q36.** 2 (E02, E04). E03 is a duplicate record of E02.

**Q37.** 344. This is the number of distinct LEIs among the 370 entity rows, with the LEI-less sovereigns CV and VD counted by their IDs.

**Q38.** No. They have different LEIs and no parent link between them (E06 and E13).

**Q39.** A (A08).

**Q40.** 66. This counts distinct GB-domiciled LEIs with a non-withdrawn issuer rating on 1 Oct 2026, and includes QA-sourced entities.

**Q41.** BB+ (A44). E16 is a QA-sourced record.

**Q42.** DE. E10 is domiciled in DE, and the LU record E17 is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency, and is rated at the local-currency level (A45, BBB-).

**Q45.** No. The ceiling limits foreign-currency ratings, and I07 is a local-currency note. It is rated BBB-, above the BB ceiling, but that ceiling doesn't apply to it.

**Q46.** No. E11 has only a counterparty obligation rating (A46, CO BBB) and no LTIDR.

**Q47.** None. I08's rating expired (EX) on 2026-09-01 (A47).

**Q48.** 106. These are instruments whose latest rating on 1 Oct 2026 had not expired.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1299","E1307","E1213","E1080","E1285","E1112","E1263","E1347","E1348","E1344","E1163","E1053","E1051","E1300","E10","E1034","E1229","E16","E1144","E1159","E1057","E1340","E1228","E1294","E1058","E1342","E1093","E1161","E1343","E1290","E1170","E1350","E1167","E1345","E1351","E1349","E1346"]},
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
"Q18":{"issuers":["E1039","E1242","E1109","E1037","E1088","E1194","E1013","E1146","E1181","E1238","E1210","E1264","E1267","E1314","E1099","E1061","E1323","E1126","E1132","E1168","E1066","E1098","E1266","E1006","E1133","E1203","E1260","E1317","E06","E1297"]},
"Q19":{"issuers":["E1080","E1118","E1158","E1345","E09","E1079","E1105","E1161","E1228","E1262","E1060","E01","E1188","E1190","E1344","E1347","E1056","E1343","E1348","E1034","E1350","E1351","E1211","E1282","E1072","E1271","E1055","E1263","E1340","E1005","E1300","E1029","E1046","E1064","E1248","E1294","E1342"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1057","E1063","E1155","E1107","E1007","E1254","E1308","E1032","E1062","E1138","E1159","E1279","E1106","E07","E1084","E1200","E1218","E1277","E1172","E1124","E1320","E1121","E1225","E1233","E1002","E1021","E1041","E1140","E1219","E1244","E1076","E1206","E1166","E1205","E1234","E1316","E1048"]},
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
"Q40":{"count":66},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}}
```