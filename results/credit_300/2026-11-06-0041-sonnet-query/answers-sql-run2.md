**Q1.** A-. Kestrel's LTIDR (FC) was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.
**Q2.** No. The only 2026 actions are A03 and A04 (2026-02-10), which affirm BBB with a Negative outlook and F2.
**Q3.** No. The 2031 note is I02, rated BB+ since A07, which is sub-investment grade.
**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its latest action A09 (2025-09-15) is A with a Positive outlook. E02's own record still shows Stable (A08). I treated the later one as current, but the two records conflict.
**Q5.** The holder takes the guarantor's risk: E02 (Northwind Holdings), rated A. I03 was issued by E04 and guaranteed by E02.
**Q6.** The data does not state a reason. It shows FC BB (A14) against LC BBB- (A13), and the Valdoria Country Ceiling is BB (A12), which fits a ceiling effect on the foreign-currency rating, but that is an inference.
**Q7.** 44 issuers had an LTIDR downgrade in 2026. The IDs are in the JSON and include RESEARCH and QA records.
**Q8.** E08. A22 on 2026-07-08 moved it to RD.
**Q9.** 291. This counts distinct LEIs with a non-withdrawn latest LTIDR on either currency basis as of 1 October 2026, QA records included. It is 278 if QA records are excluded.
**Q10.** Depends. Valdoria Telecom's LC rating is BBB- (investment grade), but its FC rating is BB (not investment grade), per A13 and A14.
**Q11.** BBB+. A36 was a downgrade to BBB+ on 2024-09-30, and A35 on 2025-11-20 only put it on watch.
**Q12.** A-, from A34 (2023-01-15).
**Q13.** 1. The only downgrade is A36.
**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.
**Q15.** A-, from A26. The downgrade to BBB+ (A27) came on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A36, A35, A33).
**Q17.** No. Orrin Bank (E06) has only A16 (A-) and A17, a watch action at A-.
**Q18.** 30 issuers were on Rating Watch Negative on 1 October 2026 (see the JSON list).
**Q19.** 37 issuers had a Negative outlook on 1 October 2026 (see the JSON list).
**Q20.** No. Pellam Retail (E07) was withdrawn for commercial reasons (A19), not defaulted.
**Q21.** 37 entities had their rating withdrawn (WD) by 1 October 2026 (see the JSON list).
**Q22.** E08 only (A22, RD).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 66. This counts instruments whose latest INST action by 1 October 2026 is not an expiry (EX) and whose rating is BBB- or better.
**Q26.** A+ (A40).
**Q27.** A- (A42), for I06.
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling record (A12), no issuer rating.
**Q30.** E05, E1028, E1236, E1101 and E1126 at VD's BB ceiling, and E1039, E1194 and E15 at CV's A ceiling.
**Q31.** No. No Corvenia or Valdoria entity rates above its ceiling in the 1 October 2026 FC list.
**Q32.** E09 (Halden Group plc), via E11 → E10 → E09.
**Q33.** E10 (Halden Bank), the guarantor of I05, currently rated BBB+ (A27).
**Q34.** No. E12 has no parent link, so the data does not tie it to the Halden group.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 and E04. E03 is a duplicate record of E02.
**Q37.** 344. This is the number of distinct LEIs, with RESEARCH duplicates collapsed.
**Q38.** No. Their LEIs differ (E06 vs E13).
**Q39.** A (A08, A09).
**Q40.** 74. This is the same basis as Q9, restricted to GB; it is 66 with QA records excluded.
**Q41.** BB+ (A44). E16 comes from the QA source system, so this may not be a production rating.
**Q42.** DE (E10). E17 is a RESEARCH duplicate of E10 that shows LU.
**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.
**Q44.** Yes, if XVD is Valdoria's currency. I07 is denominated in XVD.
**Q45.** Yes. I07 is rated BBB- (A45) against a Valdoria ceiling of BB (A12).
**Q46.** No. E11 has only a Counterparty rating (CO, A46), no LTIDR.
**Q47.** None. I08's latest action is an expiry (EX) on 2026-09-01 (A47).
**Q48.** 106. This counts instruments rated as of 1 October 2026 whose latest action is not an expiry.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1343","E1344","E1349","E08","E1167","E1263","E1347","E1161","E1170","E1342","E1186","E1159","E1093","E1229","E1053","E1112","E1151","E10","E1057","E1064","E1299","E1348","E1034","E1213","E1307","E1345","E1144","E1163","E1294","E1341","E1228","E1351","E1080","E1051","E1243","E1285","E1290","E1300","E1340","E1346","E16","E1058","E1255","E1350"]},"Q8":{"entities":["E08"]},"Q9":{"count":291},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1037","E1242","E1317","E1109","E1168","E1066","E1146","E1203","E1314","E1323","E1088","E1194","E1013","E1061","E1238","E1297","E1006","E1264","E1181","E1210","E1039","E1266","E06","E1133","E1267","E1099","E1132","E1260","E1098","E1126"]},"Q19":{"issuers":["E1034","E1188","E1248","E1228","E1263","E1345","E1105","E1158","E1344","E09","E1060","E1211","E1262","E1056","E1282","E1340","E01","E1064","E1118","E1343","E1029","E1161","E1342","E1351","E1055","E1294","E1350","E1005","E1080","E1271","E1347","E1300","E1079","E1072","E1190","E1046","E1348"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1244","E1316","E1076","E07","E1021","E1166","E1279","E1048","E1084","E1200","E1225","E1233","E1234","E1254","E1041","E1063","E1107","E1138","E1140","E1218","E1106","E1121","E1205","E1277","E1206","E1219","E1320","E1002","E1124","E1172","E1007","E1032","E1057","E1155","E1159","E1308","E1062"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E1028","E1236","E1101","E1126","E1039","E1194","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":344},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":74},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```