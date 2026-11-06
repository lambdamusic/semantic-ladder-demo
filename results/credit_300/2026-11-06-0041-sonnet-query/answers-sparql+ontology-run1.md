**Q1.** A-. E01's only rating before 2025-06-20 was the A- assigned in A01 (2024-03-12).
**Q2.** No. E01's only 2026 action is the affirmation A03, which kept BBB and changed the outlook to Negative.
**Q3.** No, BB+. Instrument I02 is subordinated, and A07 cut it to BB+ on 2025-06-20.
**Q4.** Positive. E02 and E03 share one LEI, so they are one entity. The latest action is A09 (E03, 2025-09-15), which affirmed A with a Positive outlook.
**Q5.** E02, rated A. Instrument I03 is guaranteed by E02, and E02's current issuer rating is A.
**Q6.** Not in the JSON. VD's Country Ceiling is BB (A12) and caps E05's foreign-currency rating at BB. Its local-currency rating (A13) is BBB- and is not capped.
**Q7.** 31 issuers had long-term issuer downgrades in 2026, excluding QA records. E1051 appears twice with DG to A+ both times, so its second action did not change the rating; I counted it anyway because the action is DG.
**Q8.** E08. Its rating became RD on 2026-07-08 (A22), and no other issuer was at RD or D.
**Q9.** 278. This counts distinct LEIs (record ID for sovereigns) whose latest long-term issuer rating on 2026-10-01 was not WD, ignoring QA.
**Q10.** Depends. E05 is BB on foreign currency (speculative) and BBB- on local currency (investment grade).
**Q11.** BBB+. The downgrade A36 (2024-09-30) was the latest action before 2025-06-01.
**Q12.** A-. A34 assigned A- in January 2023, and nothing changed until September 2024.
**Q13.** 1. Only A36 is a DG; the Watch (A35) is not a downgrade.
**Q14.** None. E12 was first rated on 2024-02-01 (A30).
**Q15.** A-. E10 was downgraded to BBB+ only on 2026-04-15 (A27).
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now, and the Watch and affirmation in between did not change it.
**Q17.** No. E06 had only the Rating Watch A17, which is not a downgrade.
**Q18.** 32 issuers were on Rating Watch Negative on 2026-10-01, listed in the JSON. They include E1019 and E1059, whose local-currency ratings are on Watch.
**Q19.** 28 issuers had a Negative outlook on 2026-10-01, listed in the JSON.
**Q20.** No. E07's rating was withdrawn (A19), which is not a default.
**Q21.** 35 entities, listed in the JSON, were rated at some point but had their latest rating withdrawn by 2026-10-01 (E07 among them).
**Q22.** E08 only. It is the only issuer with an RD or D rating.
**Q23.** F2, from A04.
**Q24.** Yes. E01's rating is BBB.
**Q25.** 66. These are instruments of non-QA issuers whose latest rating on 2026-10-01 is BBB- or better, ignoring Expected ratings (EX).
**Q26.** A+, from A40.
**Q27.** A-, from A42.
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** 8 entities, listed in the JSON. Their foreign-currency ratings equal the ceiling: CV's A (E1039, E1194, E15) or VD's BB (E1028, E1101, E1126, E05, E1236).
**Q31.** No. No foreign-currency rating in CV or VD is above its ceiling (A for CV, BB for VD).
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** E10, rated BBB+. Instrument I05 is guaranteed by E10, and A27 set E10 to BBB+.
**Q34.** No. E12 has no parent and is not in E09's group.
**Q35.** 3: E09, E10 (E17 is the same entity) and E11.
**Q36.** 2: E02 (E03 is the same entity) and E04.
**Q37.** 331. This counts non-QA records by LEI (record ID for sovereigns, which have none).
**Q38.** No. They have different LEIs.
**Q39.** A. The latest action on E02/E03 is A09.
**Q40.** 66, using the RESEARCH record's country where there is one. This matches the Q25 count by coincidence.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** LU. RESEARCH record E17 holds for country, over RATINGS' DE.
**Q43.** 1: E17/E10 is the only LU-domiciled entity.
**Q44.** Yes. I07 pays in XVD, VD's domestic currency.
**Q45.** No. It is BBB- against a BB ceiling, but the ceiling does not apply to local-currency debt.
**Q46.** No. E11 has only a Credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), so it is unrated.
**Q48.** 106 instruments of non-QA issuers held a non-WD, non-EX rating on 2026-10-01.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1243","E1057","E1144","E1263","E1159","E1064","E1285","E10","E1294","E1300","E1167","E1053","E1290","E1213","E1229","E1186","E1163","E1151","E1169","E1255","E1228","E1051","E1034","E1298","E1080","E1307","E1093","E08","E1160","E1112","E1058"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E06","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E1028","E1101","E1126","E05","E1236"]},
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