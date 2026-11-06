**Q1.** A-. Kestrel Energy (E01) was set at A- by A01 on 2024-03-12. The downgrade to BBB (A02) came on 2025-06-20, after the date asked about.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation (AF) that moved the outlook to Negative; the rating stayed at BBB.

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ by A07 on 2025-06-20, which is speculative grade.

**Q4.** Positive. E03 (NORTHWIND HLDGS) shares a LEI with E02, so they are one entity. Its latest action, A09 on 2025-09-15, is an affirmation at A with a Positive outlook.

**Q5.** The holder takes the credit risk of E02 (Northwind Holdings), which guarantees the note issued by the finance subsidiary E04. The note I03 is rated A.

**Q6.** Not a field question, but from the data: Valdoria's Country Ceiling (A12) is BB. That caps Valdoria Telecom's foreign-currency rating (A14) at BB, while its local-currency rating (A13) is BBB- and is not capped.

**Q7.** 35 issuers had a downgrade (DG) in 2026. I excluded QA records and instrument-only downgrades (I05). The research-record IDs E1170 and E1299 are mapped to E1169 and E1298 by an adjacent-ID pattern I inferred rather than confirmed by LEI.

**Q8.** E08 (Saxby Shipping) was in default, having been cut to RD by A22 on 2026-07-08.

**Q9.** 281 distinct issuers, counted by LEI (the two sovereigns by record ID), excluding QA and withdrawn ratings.

**Q10.** Depends. Its foreign-currency rating is BB (speculative) and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ by A36 on 2024-09-30, and the later actions A35 and A33 kept BBB+.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating action (A30) is dated 2024-02-01, after 1 January 2024.

**Q15.** A-. E10's downgrade to BBB+ (A27) came on 2026-04-15, after the date asked about.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; the Watch and the affirmation did not change the rating.

**Q17.** No. E06 had only a Rating Watch Negative (A17) in 2026, which is not a downgrade.

**Q18.** 32 issuers.

**Q19.** 28 issuers.

**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.

**Q21.** 35 entities.

**Q22.** E08 only, via the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The BBB rating is investment grade.

**Q25.** 66 instruments, excluding the unconfirmed expected rating (EX) on I08.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). Note this is not the Country Ceiling of A.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E1039, E1194 and E15 sit at Corvenia's A ceiling. E05, E1028, E1101, E1126 and E1236 sit at Valdoria's BB ceiling.

**Q31.** No. No foreign-currency rating among CV or VD entities exceeds A or BB respectively.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** The holder takes the credit risk of E10 (Halden Bank), the guarantor. The note I05 is rated BBB+ after the A29 downgrade.

**Q34.** No. E12 (Halden Foods) has no parent link to E09 or E10.

**Q35.** 3 entities: E09, E10 and E11. E17 is a second record of E10.

**Q36.** 2 entities: E02 and E04. E03 is a duplicate record of E02.

**Q37.** 329 distinct entities, counted by LEI (sovereigns by ID), excluding QA.

**Q38.** No. Their LEIs differ.

**Q39.** A.

**Q40.** 67.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. RESEARCH record E17 holds for domicile, overriding DE.

**Q43.** 1.

**Q44.** Yes. The note I07 is in XVD, the domestic currency of VD.

**Q45.** No. The ceiling applies only to foreign-currency debt, and I07 is local-currency.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. A47 is only an expected rating (EX), so the note stays unrated.

**Q48.** 106.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":281},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E09"]},
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
"Q30":{"entities":["E1039","E1194","E15","E05","E1028","E1101","E1126","E1236"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":329},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":67},
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