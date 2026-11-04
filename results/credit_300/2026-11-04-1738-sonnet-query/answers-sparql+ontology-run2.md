**Q1.** A-. E01's rating was set by A01 (A-, 2024-03-12) and stayed until the downgrade A02 on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation (BBB, outlook moved to Negative).

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ by A07 on 2025-06-20, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 on 2025-09-15, gives outlook POS.

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, rated A. I03 is guaranteed by E02, and I03 is itself rated A (A10 and A11).

**Q6.** Not answered; no field is requested for it in the JSON.

**Q7.** The 31 issuers are listed in the JSON, which includes E08 and E10 (E17 shares E10's LEI). They are the non-QA entities with a Downgraded (DG) long-term issuer rating action dated 2026. E16, a QA record, is excluded.

**Q8.** E08 (Saxby Shipping). A22 (2026-07-08) set RD, and no later action exists.

**Q9.** 278. This counts distinct LEIs (277) plus the sovereign CV, each with a non-withdrawn latest long-term issuer rating on 2026-10-01. QA records are excluded and duplicate records are merged by LEI.

**Q10.** Depends. E05's foreign-currency rating is BB (speculative) and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and nothing changed it before 2025-06-01.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. A36 is the only DG action on E14.

**Q14.** None. E12's first rating, A30, came on 2024-02-01.

**Q15.** A-. E10's rating was A- from A26 until the downgrade A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 was a Watch and A33 an affirmation).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch (RW) with the rating unchanged at A-.

**Q18.** The 34 issuers are in the JSON. Each has a Rating Watch Negative as its latest action on 2026-10-01. E1019 and E1059 are on Watch only on their local-currency ratings.

**Q19.** The 29 issuers are in the JSON; each has a Negative outlook on its latest action as of that date. E1059 stands for E1060, the RESEARCH record with the same LEI.

**Q20.** No. E07's latest action, A19, is a withdrawal for commercial reasons, which is not a default.

**Q21.** The 36 entities are in the JSON, with E1001 standing for its RESEARCH duplicate E1002. Each has a withdrawal as its latest issuer-rating action by 2026-10-01. E08 is excluded because RD is a default, not a withdrawal.

**Q22.** E08 only. A22 gave it RD, and no other non-QA record has RD or D.

**Q23.** F2, from A04.

**Q24.** Yes. E01's long-term issuer rating is BBB.

**Q25.** 66. Of the 106 instruments rated on 2026-10-01, 66 were BBB- or higher. The expected-rating action EX on I08 does not count.

**Q26.** A+, E15's local-currency rating (A40).

**Q27.** A-. The 2032 note (I06) is rated by A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (BB), which is not a rating of the sovereign.

**Q30.** The 8 entities are in the JSON. Five VD-domiciled entities are at the BB ceiling and three CV-domiciled entities are at the A ceiling.

**Q31.** No. Every CV-domiciled company is at or below A and every VD-domiciled company is at or below BB.

**Q32.** E09. The chain is E11 → E10 → E09 (Halden Group plc).

**Q33.** The holder takes the credit risk of E10, Halden Bank, rated BBB+. I05 is guaranteed by E10, and A29 gives I05 BBB+.

**Q34.** No. E12 (Halden Foods) has no parent link to E09, E10 or E11.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331. There are 329 distinct LEIs among non-QA records, plus the two sovereigns (CV and VD).

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, from A09 on E03, which is the same entity as E02.

**Q40.** 66 distinct GB-domiciled issuers hold a rating (counted by LEI).

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds, over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, and the RATINGS record for that entity says DE.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. It is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), and it stays unrated until an AS action.

**Q48.** 106. This is the count of rated instruments on 2026-10-01, excluding I08.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1243","E1057","E1144","E1263","E1159","E1064","E1285","E10","E1294","E1300","E1167","E1053","E1290","E1213","E1229","E1186","E1163","E1151","E1170","E1255","E1228","E1051","E1034","E1299","E1080","E1307","E1093","E08","E1161","E1112","E1058"]},
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
"Q18":{"issuers":["E1126","E1242","E1066","E1006","E1099","E1181","E1019","E1037","E1317","E1061","E1238","E06","E1059","E1088","E1264","E1210","E1168","E1133","E1132","E1297","E1146","E1266","E1098","E1203","E1109","E1267","E1194","E1314","E1323","E1260","E1039","E1013"]},
"Q19":{"issuers":["E1211","E1271","E1263","E1248","E1064","E1105","E1294","E1300","E1079","E1059","E1190","E1262","E1046","E01","E1282","E1228","E1055","E1029","E09","E1005","E1034","E1188","E1080","E1158","E1056","E1161","E1072","E1118"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1316","E1032","E1057","E1159","E1233","E1107","E1001","E1155","E1277","E1205","E1140","E1021","E1084","E1172","E1308","E1041","E1320","E1062","E1225","E1138","E1200","E1076","E1279","E1166","E1234","E1206","E1121","E1007","E1124","E1219","E1048","E1218","E1063","E07","E1254","E1244"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E05","E1028","E1101","E1126","E1236"]},
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
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```