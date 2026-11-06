**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02, DG to BBB) is dated 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations (BBB, F2).

**Q3.** No. The 2031 note (I02) was rated BBB (A23) and downgraded to BB+ (A07, 2025-06-20).

**Q4.** Positive. A09 (E03, "NORTHWIND HLDGS") is the latest action, a 2025-09-15 affirmation at A with Positive outlook. E03 shares E02's LEI, so it is the same entity as E02 (earlier outlook Stable, A08).

**Q5.** The guarantor, E02, rated A (A08/A09). I03 is issued by E04 and guaranteed by E02. The note itself is rated A (A10/A11).

**Q6.** The data does not state a reason. VD's Country Ceiling is BB (A12), and E05's foreign-currency rating is BB (A14) against local-currency BBB- (A13). That is consistent with the foreign-currency rating being capped at the ceiling.

**Q7.** 43 entities had a downgrade (DG) dated in 2026 on or before today; the IDs are in the JSON. E1341's DG (A1720, 2026-11-09) is excluded because it is dated after today (2026-11-05). Instrument-only downgrades (I05) are not counted.

**Q8.** E08, which was downgraded to RD on 2026-07-08 (A22) and had no later action.

**Q9.** 291, counting entities with a non-withdrawn long-term issuer rating on 2026-10-01. That is 293 records, with E02/E03 and E1059/E1060 each merged by shared LEI. It includes E08 (RD) and CV, but excludes VD, which has only a Country Ceiling. Several entities (e.g. E1115, E1158, E1303) have a later action after a WD, and I treated them as rated.

**Q10.** Depends. Valdoria Telecom's local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and A35 (2025-11-20) was only a Watch.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once (A36).

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.

**Q15.** A- (A26). The downgrade to BBB+ (A27) is dated 2026-04-15. E17 is a duplicate record for the same entity.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). Only a Watch came and went (A35).

**Q17.** No. E06's 2026 action is a Rating Watch Negative (A17), not a downgrade.

**Q18.** 32 entities were still on Rating Watch Negative (RWN) on 2026-10-01, meaning their latest action was a Watch and no later action cleared it. Some of these Watches are old (e.g. E1037's from 2022) and some are on the local-currency rating (E1019, E1059). The IDs are in the JSON.

**Q19.** 37 entities had a Negative outlook as their latest outlook on 2026-10-01 (IDs in the JSON). I excluded E1132 and E1146, whose Negative outlook was followed by a Watch.

**Q20.** No. E07 was withdrawn on 2026-05-12 (A19) and never had a default rating.

**Q21.** 35 entities had a long-term rating that was later withdrawn, with no rating after that (IDs in the JSON).

**Q22.** Only E08, via RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 68. This is the count of instruments whose latest rating on 2026-10-01 was BBB- or higher. Instruments whose rating had expired (EX) before that date are excluded.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). A39 is the local-currency rating, A-.

**Q29.** None. VD has only a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05, E1028, E1101, E1126 and E1236 are foreign-currency BB, equal to VD's BB ceiling. E15, E1039 and E1194 are foreign-currency A, equal to CV's A ceiling (A37).

**Q31.** No. None of the entities in ceiling countries (VD, CV) had a foreign-currency rating above the ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10, currently rated BBB+ (A27, downgraded from A-). I05 is issued by E11 and guaranteed by E10.

**Q34.** No. E12 has no parent link to E09/E10, and the data shows only a name similarity.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02 and its subsidiary E04). E03 is a duplicate of E02.

**Q37.** 344. This is 370 entity records minus 26 duplicate pairs sharing an LEI; it assumes E1001 to E1351 are all present.

**Q38.** No. E06 (DE) and E13 (US) have different LEIs.

**Q39.** A (A08/A09).

**Q40.** 74 distinct GB-domiciled issuers, counting E02/E03 as one.

**Q41.** BB+. E16 was assigned BBB- (A43) and downgraded on 2026-06-01 (A44).

**Q42.** DE (E10). The duplicate record E17 (same LEI) says LU, so there is a conflict. I used the RATINGS record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is recorded as DE.

**Q44.** Yes. I07 is denominated in XVD, which I inferred is Valdoria's currency; the data does not define XVD.

**Q45.** No. I07's rating is BBB- (A45). The BB ceiling applies to foreign-currency ratings, not to a local-currency note.

**Q46.** No. E11 has only a CO-type rating (A46, BBB), no long-term issuer rating.

**Q47.** None. I08's A rating expired (EX) on 2026-09-01 (A47).

**Q48.** 109. This counts instruments with a rating on 2026-10-01. Of the 114 rated, I08, I1008, I1012, I1021, I1046 and I1049 had already expired (I1015 expires only on 2026-12-17).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":68},
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
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":109}
}
```