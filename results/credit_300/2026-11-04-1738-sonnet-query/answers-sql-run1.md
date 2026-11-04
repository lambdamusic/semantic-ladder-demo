**Q1.** A-. E01's last action before 1 Jan 2025 was A01 (A-, 2024-03-12); the downgrade A02 came on 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with a Negative outlook.
**Q3.** No. I02 (the 2031 note) was cut to BB+ by A07 on 2025-06-20, which is sub-investment grade.
**Q4.** Positive. E03 (NORTHWIND HLDGS) shares E02's LEI, so it is the same entity, and its latest action A09 (2025-09-15) has outlook POS.
**Q5.** The credit risk is E02's, rated A. I03 is issued by E04 and guaranteed by E02, and its rating (A10/A11) matches E02's A.
**Q6.** The data doesn't state a reason. It only shows E05's local-currency rating at BBB- (A13) and foreign-currency at BB (A14), with the Valdoria country ceiling at BB (VD, A12).
**Q7.** The 44 issuers are in the JSON, found from LTIDR downgrade actions dated 2026, with duplicate records merged by LEI. This list has no upper date bound, so it may include actions after today.
**Q8.** E08. A22 moved it to RD on 2026-07-08 and nothing later reverses that.
**Q9.** 291. This counts distinct LEIs whose latest issuer-rating action by 1 Oct 2026 is not a withdrawal.
**Q10.** Depends. E05 is BBB- in local currency (investment grade) but BB in foreign currency (not investment grade).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action was A35 on 2025-11-20.
**Q12.** A-, from A34, the initial rating on 2023-01-15.
**Q13.** 1. Only A36 is a downgrade for E14.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. E10 was A- (A26) until the downgrade A27 on 2026-04-15.
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+ after A35 (watch) and A33 (affirmation).
**Q17.** No. E06's only 2026 action, A17, is a Rating Watch Negative at A-.
**Q18.** The 32 issuers are in the JSON. Each one's latest issuer-rating action by 1 Oct 2026 carries RWN; for E1059, only the local-currency (LC) rating is on watch, which is why it also appears in Q19.
**Q19.** The 37 issuers are in the JSON. Each one's latest issuer-rating action by 1 Oct 2026 carries a Negative outlook.
**Q20.** No. A19 withdrew E07's rating on 2026-05-12 for commercial reasons, which is not a default.
**Q21.** The 35 entities are in the JSON. They had an issuer rating at some point, but their latest action by 1 Oct 2026 is a withdrawal (WD).
**Q22.** E08 only. It is the only entity with an RD/D rating (A22).
**Q23.** F2, from A04.
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 66. This counts instruments with BBB- or better in their latest INST action, excluding expired ones.
**Q26.** A+, from A40.
**Q27.** A-, from A42.
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling (A12, BB) and no LTIDR.
**Q30.** The 8 entities are in the JSON. The ceilings are A for CV and BB for VD, and these entities' FC ratings equal them exactly.
**Q31.** No. Every corporate with CV or VD domicile is at or below its ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The credit risk is E10's (the guarantor), with I05 rated BBB+. A29 downgraded I05 to BBB+ on 2026-04-15, in line with E10's own BBB+.
**Q34.** No. E12 (Halden Foods) has no parent link to E09/E10.
**Q35.** 3: E09, E10 and E11. E17 is a RESEARCH duplicate of E10, with the same LEI.
**Q36.** 2: E02 and E04. E03 is a duplicate of E02.
**Q37.** 344. This counts distinct LEIs, using entity_id for the sovereigns, which have no LEI.
**Q38.** No. They have different LEIs (E06 vs E13) and are separate records with separate rating histories.
**Q39.** A. E02's rating is A (A08), reaffirmed at A by E03/A09.
**Q40.** 74. This counts distinct GB-domiciled LEIs whose latest issuer-rating action by 1 Oct 2026 is not a withdrawal.
**Q41.** BB+. A44 downgraded E16 from BBB- on 2026-06-01. E16 comes from the QA source system.
**Q42.** DE, from E10. E17's LU is a RESEARCH-source duplicate with the same LEI.
**Q43.** 0. The only LU record, E17, is the same legal entity as E10, which is DE-domiciled.
**Q44.** Yes. I07 is denominated in XVD, apparently Valdoria's currency; the data doesn't define XVD explicitly.
**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but the ceiling applies to foreign-currency obligations and I07 is local-currency.
**Q46.** No. E11 has only a Country/Counterparty-type rating (A46, CO) and no LTIDR.
**Q47.** None. I08 has an EX action (A47, 2026-09-01), so it holds no active rating as of now. Its last rating was A.
**Q48.** 106. This counts instruments with rating history on 1 Oct 2026, excluding those with EX actions.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1167","E1058","E1341","E1344","E1080","E1263","E1345","E1349","E1307","E1228","E1298","E1255","E1229","E1340","E1346","E16","E1034","E1342","E1160","E10","E1351","E1294","E1350","E1151","E1290","E1285","E1343","E1064","E1093","E1144","E1053","E1057","E1159","E1243","E1347","E1051","E1300","E1213","E1163","E1169","E1186","E1348","E1112","E08"]},
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
"Q18":{"issuers":["E1317","E1037","E1209","E1242","E1146","E1323","E1203","E1066","E1314","E1109","E1168","E1181","E1019","E1006","E1264","E06","E1133","E1266","E1039","E1059","E1260","E1099","E1132","E1267","E1126","E1098","E1088","E1194","E1297","E1061","E1013","E1238"]},
"Q19":{"issuers":["E1005","E1080","E1055","E1350","E1294","E1188","E1248","E1034","E1351","E1029","E1342","E1160","E1228","E1345","E1263","E1211","E09","E1046","E1348","E1158","E1344","E1105","E1059","E1282","E1056","E1340","E1300","E1347","E1271","E1261","E1343","E01","E1118","E1064","E1072","E1190","E1079"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1244","E1316","E1205","E1121","E1253","E1032","E1159","E1007","E1308","E1057","E1155","E1277","E07","E1166","E1021","E1218","E1076","E1048","E1084","E1233","E1225","E1234","E1200","E1320","E1206","E1219","E1138","E1107","E1063","E1140","E1041","E1062","E1124","E1172","E1001"]},
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