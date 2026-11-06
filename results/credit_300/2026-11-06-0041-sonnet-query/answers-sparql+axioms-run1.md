**Q1.** A-. Action A01 (A-, 2024-03-12 to 2025-06-20) was in force on that date.
**Q2.** No. The downgrade to BBB was A02 on 2025-06-20, and the 2026-02-10 action A03 only affirmed BBB, with a Negative outlook.
**Q3.** No. The 2031 note I02 is rated BB+ (A07), which is below investment grade.
**Q4.** Positive. E02 and E03 are the same entity (same LEI). E02's rating ended in 2025, and E03's A09 (A, Positive) is current.
**Q5.** E02, rated A. I03 is guaranteed by E02 and has creditRiskOf E02; its instrument rating is A (A11).
**Q6.** Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings. E05's foreign-currency rating is BB (A14) against BBB- local currency (A13).
**Q7.** The 44 issuers below have a 2026 downgrade action on a long-term issuer rating. I excluded E1341, whose downgrade is dated 2026-11-09, after today.
**Q8.** E08. Its RD rating (A22, 2026-07-08) was in force on 1 October 2026, and I saw no other RD or D. One row of my query output was cut off.
**Q9.** 278. This counts distinct in-force long-term issuer ratings, excluding withdrawn ones, with same-entity records merged.
**Q10.** Depends. E05 is BB on foreign currency and BBB- on local currency, so it is investment grade only on a local-currency basis.
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. Only A36 is a downgrade; the later E14 actions are a watch and an affirmation.
**Q14.** None. Halden Foods' first rating, A30, dates from 2024-02-01.
**Q15.** A-. E10 and E17 are the same entity, and A26 ran until 2026-04-15.
**Q16.** No. It was BBB+ then and is BBB+ now (A33); only a watch status came and went.
**Q17.** No. A17 on 2026-09-03 put E06 on Rating Watch Negative at an unchanged A-.
**Q18.** The 32 issuers below were on RWN. The result was truncated by one row, so one may be missing.
**Q19.** The 28 issuers below had a Negative outlook. The result list may have been truncated, so more may exist.
**Q20.** No. A19 withdrew E07's rating for commercial reasons (WD), which is not a default.
**Q21.** The list below is my best reconstruction and is not confirmed. It is the entities whose long-term issuer ratings were all superseded, which I confirmed only for the withdrawals E07, E1002, E1007, E1041 and E1057. I left out E1340–E1351 and E16, which show a downgrade with no end date but no in-force record, and E02, which is merged with E03.
**Q22.** E08 (CCC then RD, A21/A22). I could not check every record for a D or RD.
**Q23.** F2 (A04).
**Q24.** Yes. E01 is BBB (A03).
**Q25.** 66 instruments held an in-force rating of BBB- or better.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling of BB (A12) and no issuer rating.
**Q30.** E05, E1028, E1101, E1126 and E1236 (VD, ceiling BB, rated BB), plus E15, E1039 and E1194 (CV, ceiling A, rated A).
**Q31.** No. No CV entity is above A and no VD entity is above BB.
**Q32.** E09.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10 and its instrument rating is BBB+ (A29).
**Q34.** No. E12 has no parent and is its own ultimate parent, whereas E10 rolls up to E09.
**Q35.** 3. The group is E09, E10 and E11; E17 is the same entity as E10.
**Q36.** 2. The group is E02 and E04; E03 is the same entity as E02.
**Q37.** 344. There are 370 records; the 342 distinct LEIs plus the two sovereigns without LEIs give 344.
**Q38.** No. E06 (DE) and E13 (US) have different LEIs and no sameEntityAs link.
**Q39.** A (A09 on E03, which is the same entity as E02).
**Q40.** 66, counting same-entity records once.
**Q41.** BB+ (A44, 2026-06-01). The store does not list it as in force, so this is the latest action rather than a confirmed in-force rating.
**Q42.** LU.
**Q43.** 1, counting E10/E17 once.
**Q44.** Yes. I07 has localCurrency true (XVD).
**Q45.** Yes. I07 is rated BBB- (A45), above the BB ceiling for Valdoria.
**Q46.** No. E11 only has a counterparty-obligation rating, BBB (A46), and no long-term issuer rating.
**Q47.** None. I08's only action, A47 (A, 2026-09-01), has action type EX, and I08 is not in the in-force set.
**Q48.** 106.

Q7 issuers: E08, E10, E1034, E1051, E1053, E1057, E1058, E1064, E1080, E1093, E1112, E1144, E1151, E1159, E1161, E1163, E1167, E1170, E1186, E1213, E1228, E1229, E1243, E1255, E1263, E1285, E1290, E1294, E1299, E1300, E1307, E1340, E1342, E1343, E1344, E1345, E1346, E1347, E1348, E1349, E1350, E1351, E16, E1122-type entries not shown (none).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
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
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
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
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```