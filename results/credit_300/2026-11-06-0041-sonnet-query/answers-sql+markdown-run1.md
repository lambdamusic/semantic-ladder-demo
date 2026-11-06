**Q1.** A-. E01's LTIDR was set at A- by A01 (2024-03-12) and not changed until the A02 downgrade on 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations. A03 moved the outlook to NEG but kept the rating at BBB.

**Q3.** No. I02 is subordinated and was cut to BB+ by A07, which is speculative grade.

**Q4.** POS. E03 has the same LEI as E02, so it is the same entity. A09 (2025-09-15, E03) is the latest action and sets the outlook to POS.

**Q5.** The holder takes E02's (Northwind Holdings) credit risk. I03 is guaranteed by E02 and is rated A (A10, A11).

**Q6.** The data does not state the reason. E05's FC rating is BB and its LC rating is BBB- (A14, A13). The VD Country Ceiling is BB (A12), which fits a ceiling cap on FC ratings, but no comment says so.

**Q7.** 31 issuers had a DG on an issuer rating in 2026, listed in the JSON. They include E08 (A21, A22) and E10 (A27). After merging same-LEI records and excluding QA records, no other issuer qualifies.

**Q8.** E08. A22 on 2026-07-08 took it to RD, which is a default.

**Q9.** 278. This counts distinct LEIs with a latest LTIDR other than WD on 2026-10-01. Same-LEI duplicates are merged and QA records are excluded.

**Q10.** Depends. E05 is BB on FC (speculative) and BBB- on LC (investment grade).

**Q11.** BBB+. A36 (2024-09-30) set it, and the later RW (A35) left the rating unchanged.

**Q12.** A-. A34 assigned it on 2023-01-15.

**Q13.** 1. A36 is the only DG for E14.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 is the same entity as E17, and the downgrade to BBB+ came on 2026-04-15, after this date.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now. The RW and the later AF did not change the rating.

**Q17.** No. E06's only 2026 action is an RW (A17), which is not a downgrade.

**Q18.** 32 issuers were on RWN, listed in the JSON. This includes E06 and LC-only watches.

**Q19.** 28 issuers had a NEG outlook, listed in the JSON. This includes E01 and E09.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, which is not a default.

**Q21.** 35 entities, listed in the JSON, have a latest LTIDR of WD and no other current LTIDR. This includes E07.

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's FC rating is BBB, which is investment grade.

**Q25.** 66. This counts instruments whose latest INST rating on 2026-10-01 is BBB- or higher. EX actions are excluded.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The CC of A is a cap, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** Eight entities: E05, E1028, E1101, E1126 and E1236 at BB (VD ceiling), and E15, E1039 and E1194 at A (CV ceiling).

**Q31.** No. No entity's FC rating is above its country ceiling.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** The holder takes E10's (Halden Bank) credit risk. I05 is guaranteed by E10 and is rated BBB+ after A29.

**Q34.** Yes. E12 (Halden Foods) has no parent and is not part of the E09 group. The question is ambiguous on which Halden Foods is meant, so this assumes Halden Bank (E10) is the intended Halden entity and the answer is "no" for Foods. Correction: E12 has no parent link to E09, so they are not in the same group.

**Q35.** 3. The group is E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2. The group is E02 and E04. E03 duplicates E02.

**Q37.** 331. This is the count of distinct LEIs plus the two sovereigns, with QA excluded.

**Q38.** No. They have different LEIs.

**Q39.** A. Both E02 (A08) and E03 (A09) are A.

**Q40.** 66. This is distinct GB-domiciled issuers with a current LTIDR on 2026-10-01, using the RESEARCH country where records disagree.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. RESEARCH holds for domicile, and E17 says LU while E10 says DE.

**Q43.** 1. Only the Halden Bank entity (E10/E17) is in LU after applying the RESEARCH country.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, the country of E05.

**Q45.** No. I07 is rated BBB- and is local-currency debt, so the BB ceiling does not apply.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an EX action (A47), so it is not yet rated.

**Q48.** 106. This counts instruments whose latest INST action on or before 2026-10-01 is not EX, and none of them is WD.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18":{"issuers":["E1037","E1317","E1209","E1242","E1264","E1019","E1006","E1203","E1146","E1066","E1314","E1323","E1133","E06","E1194","E1088","E1181","E1266","E1059","E1039","E1238","E1061","E1013","E1297","E1132","E1099","E1260","E1267","E1126","E1098","E1109","E1168"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1032","E1155","E1159","E1007","E1057","E1253","E1308","E1121","E1205","E1076","E1244","E1316","E1166","E1021","E07","E1041","E1138","E1063","E1140","E1107","E1277","E1062","E1124","E1001","E1172","E1084","E1048","E1218","E1219","E1320","E1206","E1200","E1225","E1233","E1234"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1126","E1236","E1194","E15","E1039","E1028","E1101"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":331},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```