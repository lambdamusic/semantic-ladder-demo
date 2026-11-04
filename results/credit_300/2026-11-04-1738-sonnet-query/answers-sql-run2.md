**Q1.** A-. E01's last action before 1 Jan 2025 was A01 (A-); the downgrade to BBB (A02) came on 2025-06-20.

**Q2.** No. E01 had only affirmations in 2026 (A03 and A04, 2026-02-10), where the outlook moved to Negative; the one downgrade, A02, was in 2025.

**Q3.** No. I02 (the 2031 note) was cut to BB+ by A07, which is sub-investment grade.

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** A holder takes the credit risk of E02, the guarantor of I03, which is rated A (A08 and A09).

**Q6.** It is capped by the country ceiling. VD's Country Ceiling (A12) is BB, so E05's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13).

**Q7.** 44 entities had a long-term rating downgrade dated 2026, listed in the JSON. Duplicate records were merged by LEI and some actions are dated after today, so this is a best reading.

**Q8.** E08. A22 (2026-07-08) rated it RD, a default rating, and nothing later changes that.

**Q9.** 291. This counts distinct LEI-deduplicated entities whose latest long-term rating action on or before 2026-10-01 is not a withdrawal, and it includes the sovereign CV.

**Q10.** Depends. E05 is BBB- in local currency (investment grade) but BB in foreign currency (not).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30.

**Q12.** A-. A34 is E14's rating from 2023-01-15.

**Q13.** 1. A36 is the only downgrade of E14.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 set E10 at A-, and the downgrade A27 came only on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; A35 and A33 were a watch and an affirmation.

**Q17.** No. E06 has only a Rating Watch action (A17, 2026-09-03), with no rating change.

**Q18.** 32 entities were on Rating Watch Negative, listed in the JSON.

**Q19.** 37 entities had a Negative outlook, listed in the JSON.

**Q20.** No. A19 withdrew E07's rating on 2026-05-12 for commercial reasons, which is not a default.

**Q21.** 35 entities, listed in the JSON, whose latest action is a withdrawal (WD) and who held a rating earlier.

**Q22.** Only E08. Its RD rating (A22) is the only default-grade rating in the data.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB.

**Q25.** 66. Of the 106 instruments rated on 2026-10-01 (latest action not EX), 66 were investment grade.

**Q26.** A+ (A40).

**Q27.** A- (A42 on I06).

**Q28.** BBB+ (A38 on CV).

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** 8 entities: E15, E1039 and E1194 sit at the CV ceiling of A, and E05, E1028, E1236, E1126 and E1101 sit at the VD ceiling of BB.

**Q31.** No. Every CV entity is at or below A and every VD entity is at or below BB.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** A holder takes the credit risk of E10, the guarantor of I05, which is rated BBB+ after A27.

**Q34.** No. E12 has no parent and no link to E09 or E10; the shared name is only a coincidence.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. This is the number of distinct LEIs, with the two sovereigns without an LEI counted by their own ID.

**Q38.** No. Their LEIs differ (E06 vs E13).

**Q39.** A. E02 was rated A (A08) and E03 affirmed A (A09).

**Q40.** 74. Counted as in Q9, restricted to LEI-deduplicated entities whose country is GB.

**Q41.** BB+ (A44).

**Q42.** DE. E10 is domiciled in DE; the LU in E17 is a conflicting RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, is a duplicate of the DE entity E10.

**Q44.** Yes. I07 is denominated in XVD, which I take to be Valdoria's currency.

**Q45.** No. The Country Ceiling (BB, A12) limits foreign-currency ratings, and I07 is local-currency, so its BBB- (A45) is not constrained by it.

**Q46.** No. E11 has only a CO record (A46), not a long-term issuer rating.

**Q47.** None. I08 has only an EX action (A47, 2026-09-01), which looks like an expiry or exchange, so I read it as no longer rated. That reading is an assumption about EX.

**Q48.** 106. These are instruments whose latest action on or before 2026-10-01 was not an EX.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1151","E1350","E1294","E1341","E1167","E1058","E1285","E1290","E16","E1340","E1346","E1344","E1169","E1112","E08","E1348","E1186","E1342","E10","E1351","E1160","E1144","E1053","E1057","E1243","E1159","E1080","E1034","E1347","E1051","E1093","E1064","E1343","E1263","E1345","E1349","E1307","E1229","E1228","E1298","E1255","E1213","E1163","E1300"]},
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
"Q18":{"issuers":["E1133","E06","E1061","E1013","E1238","E1297","E1266","E1039","E1059","E1194","E1088","E1203","E1314","E1146","E1323","E1066","E1098","E1126","E1019","E1264","E1006","E1317","E1037","E1209","E1242","E1168","E1109","E1260","E1132","E1099","E1181","E1267"]},
"Q19":{"issuers":["E1350","E1055","E1294","E1188","E1248","E1034","E1347","E1271","E1261","E1118","E1064","E01","E1343","E1345","E1228","E1263","E1029","E1342","E1351","E1160","E09","E1211","E1080","E1005","E1340","E1056","E1059","E1282","E1105","E1344","E1158","E1046","E1348","E1072","E1190","E1079","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1057","E1308","E1007","E1032","E1155","E1159","E1253","E1107","E1140","E1138","E1063","E1041","E1218","E1316","E1244","E1121","E1205","E1021","E1166","E07","E1084","E1048","E1277","E1225","E1234","E1233","E1200","E1001","E1172","E1124","E1206","E1219","E1320","E1076","E1062"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1236","E1126","E1101"]},
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