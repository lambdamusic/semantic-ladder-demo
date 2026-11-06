**Q1.** A-. Kestrel's long-term foreign-currency rating was A- under A01 (2024-03-12 to 2025-06-20).
**Q2.** No. On 2026-02-10 (A03) the rating stayed at BBB and only the outlook changed to Negative.
**Q3.** No. The 2031 note (I02) has been rated BB+ since the 2025-06-20 downgrade (A07), which is below investment grade.
**Q4.** Positive, from E02's rating A09 (the E02/E03 merged entity).
**Q5.** E02 (Northwind Holdings) is the guarantor, so a holder takes its credit risk (I03). It is rated A (A09).
**Q6.** Not asked in the JSON. The data shows Valdoria Telecom (E05) at BB foreign-currency and BBB- local-currency, and Valdoria's ceiling is BB. The data does not state the reason explicitly.
**Q7.** 30 issuers had a downgrade (DG) action on a long-term rating starting in 2026, listed in the JSON. I excluded E1064, whose 2026 DG shows no change in rating. I counted E1051 once, on its first DG (AA- to A+).
**Q8.** E08. Its rating has been RD since 2026-07-08 (A22).
**Q9.** 278 distinct entities held a non-withdrawn long-term issuer rating on 1 October 2026.
**Q10.** Depends. E05 is BB on foreign currency (A14) but BBB- on local currency (A13).
**Q11.** BBB+ (A36, valid 2024-09-30 to 2025-11-20).
**Q12.** A- (A34).
**Q13.** Once, A- to BBB+ on 2024-09-30 (A36). The Rating Watch Negative action (A35) is not a downgrade.
**Q14.** None. Halden Foods' first rating (A30) starts on 2024-02-01.
**Q15.** A- (A26, valid to 2026-04-15).
**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now (A33).
**Q17.** No. Orrin Bank (E06) only went on Rating Watch Negative (A17) in 2026, with the rating still A-.
**Q18.** 32 issuers carry an open Rating Watch Negative, listed in the JSON, including E06.
**Q19.** 28 issuers have an open Negative outlook, listed in the JSON, including E01 and E09.
**Q20.** No. Pellam's (E07) rating was withdrawn (WD, A19), which is not a default.
**Q21.** 35 entities, listed in the JSON. They had a non-withdrawn issuer rating at some point but none open on 1 October 2026, including E07.
**Q22.** Only E08, which was rated RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 66 distinct instruments held an investment-grade rating (BBB- or higher) on 1 October 2026.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. There are no ratings for VD (Republic of Valdoria).
**Q30.** Eight entities were exactly at their country's ceiling: E05, E1028, E1101, E1126, E1236 (VD, BB) and E15, E1039, E1194 (CV, A).
**Q31.** No. No non-sovereign foreign-currency rating was above its ceiling (VD and CV checked).
**Q32.** E09 (Halden Group plc).
**Q33.** E10 (Halden Bank) is the guarantor of I05, so a holder takes its credit risk. It is rated BBB+ (A27), the same as the note (A29).
**Q34.** No. Halden Foods (E12) has no parent, so it is not in E09's group, while Halden Bank (E10) is.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 and E04.
**Q37.** 331 entities, with duplicate records already merged.
**Q38.** No. They are separate entities, E06 (DE) and E13 (US), with different LEIs.
**Q39.** A (A09).
**Q40.** 66 distinct GB-domiciled entities held a non-withdrawn issuer rating on 1 October 2026.
**Q41.** None. There is no entity named Brindle Capital.
**Q42.** LU (E10).
**Q43.** 1 entity is domiciled in LU.
**Q44.** Yes. I07 is flagged local_currency = yes (currency XVD).
**Q45.** No. The ceiling limits foreign-currency ratings, and I07 is a local-currency obligation rated BBB- (A45).
**Q46.** No. E11 has no ratings.
**Q47.** None. I08 has no rating records.
**Q48.** 106 distinct instruments had an open rating on 1 October 2026.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1206","E1219","E1320","E1121","E1205","E1244","E1316","E1048","E1084","E1076","E1200","E1225","E1233","E1234","E1001","E1124","E1172","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1062","E1277","E1218","E1041","E1063","E1107","E1138","E1140","E07","E1021","E1166"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236"]},
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