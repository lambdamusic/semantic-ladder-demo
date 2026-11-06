**Q1.** A-. A01 (E01 AS A- 2024-03-12) is the latest foreign-currency issuer rating before that date; the next change is A02 on 2025-06-20.
**Q2.** No. E01's 2026 actions are affirmations (A03 BBB, A04 F2); the downgrade to BBB was A02 in 2025.
**Q3.** No. The 2031 note is I02 (subordinated), last rated BB+ by A07 on 2025-06-20, which is below investment grade.
**Q4.** Positive. E03 is the same legal entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with a Positive outlook.
**Q5.** Northwind Holdings (E02). I03 is issued by E04 but guaranteed by E02, whose rating is A (A09, same entity as E03).
**Q6.** The data does not state a reason. It is consistent with a Country Ceiling: A12 sets Valdoria's CC at BB, which matches E05's FC rating of BB (A14), while the LC rating is BBB- (A13).
**Q7.** 42 issuers have a DG action dated in 2026 (list in JSON). E1341's downgrade (A1720) is dated 2026-11-09, after today's date; I included it.
**Q8.** E08. A22 is a DG to RD on 2026-07-08, with no later action.
**Q9.** 291. This counts entities with an LTIDR whose latest action by date is not a withdrawal, merging records that share a LEI. Where an action follows a WD (E1115, E1158, E1303), I treated the entity as rated.
**Q10.** Depends. The foreign-currency rating is BB (A14, not investment grade), and the local-currency rating is BBB- (A13, investment grade).
**Q11.** BBB+. A36 downgraded E14 on 2024-09-30; A35 is only a watch.
**Q12.** A-. A34 (2023-01-15) was still in force on 2024-01-01.
**Q13.** 1. The only DG is A36.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. E10 was A- (A26) until the A27 downgrade on 2026-04-15; E17 is a duplicate record with the same LEI.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 is a watch, A33 an affirmation).
**Q17.** No. E06's 2026 action is A17, a Rating Watch Negative at A-, not a downgrade. E13 (Orrin Bancorp) is a different entity.
**Q18.** 32 issuers have a Rating Watch Negative as their latest action on 1 Oct 2026 (list in JSON). Watches have no expiry in the data, so older ones such as E1037 (2022) are included.
**Q19.** 37 issuers, based on the latest outlook-bearing action on or before 1 Oct 2026 (list in JSON). E1346 (A1730) and E1349 (A1736) have Negative-outlook downgrades dated 14–15 Oct, which fall after the date.
**Q20.** No. E07 was withdrawn for "commercial reasons" (A19), not rated default.
**Q21.** 35 entities (list in JSON). Their latest LTIDR action is a withdrawal (WD) dated before 1 Oct 2026. E1106 and E1279 are not listed because withdrawals applied to only one currency basis and the other basis remains.
**Q22.** E08 only. A22 is a DG to RD.
**Q23.** F2 (A04, E01 short-term IDR).
**Q24.** Yes. E01's long-term IDR is BBB (A03).
**Q25.** 68. This counts instruments whose latest rating is BBB- or higher on 1 Oct 2026. I excluded the six already expired (I08, I1008, I1012, I1021, I1046, I1049) and kept three whose EX dates are after 1 Oct (I1001, I1007, I1015).
**Q26.** A+ (A40, E15 local currency).
**Q27.** A-. I06 is rated by A42.
**Q28.** BBB+ (A38, CV foreign-currency IDR).
**Q29.** None. VD has only a Country Ceiling rating of BB (A12), which is not an issuer rating.
**Q30.** E05, E1028, E1101, E1126 and E1236 sit at the Valdoria ceiling of BB; E15, E1039 and E1194 sit at the Corvenia ceiling of A. These are entities in countries whose Country Ceiling (CC) is set by A12 (VD, BB) and A37 (CV, A).
**Q31.** No. No company's foreign-currency rating exceeds BB in VD or A in CV.
**Q32.** E09. E11 has parent E10, and E10 has parent E09.
**Q33.** Halden Bank (E10). I05 is guaranteed by E10, whose rating is BBB+ after A27.
**Q34.** No. E12 has no parent link to E09, E10 or E11; the shared name is not evidence of a group.
**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.
**Q36.** 2: E02 and its subsidiary E04. E03 is the same entity as E02.
**Q37.** 344. There are 370 entity records and 26 duplicate pairs sharing a LEI.
**Q38.** No. E06 and E13 have different LEIs and countries.
**Q39.** A (A09).
**Q40.** 73. This counts distinct GB-domiciled entities with an active LTIDR on 1 Oct 2026, merging duplicate-LEI records.
**Q41.** BB+. E16 was downgraded by A44 on 2026-06-01.
**Q42.** DE. E10 says DE, but the duplicate research record E17 says LU, so the data conflicts and I used the RATINGS record.
**Q43.** 0. The only LU record is E17, which duplicates E10 (DE).
**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency.
**Q45.** No. The BB ceiling caps foreign-currency ratings and does not apply to this local-currency note rated BBB- (A45).
**Q46.** No. E11 has only a CO-type rating (A46), not a long-term issuer rating.
**Q47.** None. I08's only rating record is A47, an EX (expiry) on 2026-09-01 at A, so it no longer carries a rating.
**Q48.** 109. That is 115 instruments less the six already expired.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
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
"Q40":{"count":73},
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