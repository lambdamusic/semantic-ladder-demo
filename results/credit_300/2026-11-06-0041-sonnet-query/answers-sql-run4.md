**Q1.** A-. E01's rating was set at A- on 2024-03-12 (A01) and not cut until 2025-06-20 (A02).
**Q2.** No. E01's only 2026 actions are affirmations at BBB (A03, A04).
**Q3.** No. Kestrel's 2031 note (I02) was cut to BB+ on 2025-06-20 (A07), which is sub-investment grade.
**Q4.** POS. E03 is a duplicate record of E02 (same LEI), and its latest action is A09 on 2025-09-15, an affirmation at A with a Positive outlook. E02's own last outlook (A08) was Stable.
**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes E02's risk (A08, A09).
**Q6.** Valdoria Telecom's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB equals Valdoria's Country Ceiling (A12), which caps the foreign-currency rating.
**Q7.** 43 issuers had a DG action on their issuer rating in 2026 (listed in the JSON). E1341's DG is dated 2026-11-09, after today, so I excluded it.
**Q8.** E08. It was rated RD from 2026-07-08 (A22).
**Q9.** 291. That is 292 entity IDs with a current non-withdrawn issuer rating, collapsed by shared LEI.
**Q10.** Depends. The foreign-currency rating is BB (sub-investment grade) and the local-currency rating is BBB- (investment grade).
**Q11.** BBB+. E14 was cut on 2024-09-30 (A36), and the next action is on 2025-11-20.
**Q12.** A-, from A34.
**Q13.** 1, from A36.
**Q14.** None. E12's first rating is dated 2024-02-01 (A30).
**Q15.** A-. E10 was only cut on 2026-04-15 (A27).
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35, A33 are a watch and an affirmation).
**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17).
**Q18.** 32 issuers, listed in the JSON. This includes E1019 and E1059, whose watch is on the local-currency rating only.
**Q19.** 37 issuers, listed in the JSON, based on foreign-currency outlooks. No local-currency rating had a Negative outlook.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not defaulted.
**Q21.** 35 entities, listed in the JSON. Their latest issuer-rating action by 1 October 2026 is a withdrawal, including E07 and the duplicate E1002.
**Q22.** E08 only (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 66 instruments.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD only has a Country Ceiling (A12, BB) and no issuer rating.
**Q30.** E05, E1028, E1101, E1126, E1236 (BB, Valdoria ceiling) and E15, E1039, E1194 (A, Corvenia ceiling).
**Q31.** Yes. Several VD-domiciled issuers hold ratings above the BB ceiling, e.g. E1096 at BBB and E1229 at BB+. I did not verify each one's country, but the query only returned CV and VD entities.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was cut to BBB+ on 2026-04-15 (A27).
**Q34.** No. E12 has no parent and no link to E09.
**Q35.** 3 (E09, E10, E11). E17 is a duplicate of E10.
**Q36.** 2 (E02, E04). E03 is a duplicate of E02.
**Q37.** 344. There are 342 distinct LEIs plus the 2 sovereigns, which have no LEI.
**Q38.** No. They have different LEIs, countries and entity IDs (E06 and E13).
**Q39.** A, from A08 and A09.
**Q40.** 74.
**Q41.** BB+ (A44).
**Q42.** DE. The LU country on E17 is a duplicate research record for the same LEI.
**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.
**Q44.** Yes. I07 is denominated in XVD, which I take to be Valdoria's currency; the data does not define XVD explicitly.
**Q45.** Yes. I07 is rated BBB- (A45), above the BB ceiling (A12).
**Q46.** No. E11 only has a Credit Opinion (A46).
**Q47.** None. I08 was expired on 2026-09-01 (A47).
**Q48.** 106.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},
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
"Q18":{"issuers":["E1037","E1242","E1317","E1088","E1194","E06","E1133","E1181","E1210","E1099","E1132","E1260","E1006","E1264","E1013","E1061","E1238","E1297","E1267","E1066","E1146","E1203","E1314","E1323","E1098","E1126","E1109","E1168","E1039","E1266","E1019","E1059"]},
"Q19":{"issuers":["E1055","E1294","E1350","E1072","E1190","E01","E1064","E1118","E1343","E1005","E1080","E1079","E1034","E1188","E1248","E1046","E1348","E1029","E1161","E1342","E1351","E1271","E1347","E09","E1060","E1211","E1262","E1056","E1282","E1340","E1300","E1228","E1263","E1345","E1105","E1158","E1344"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1021","E1166","E1062","E1316","E1244","E1205","E1121","E1076","E1218","E1234","E1233","E1225","E1200","E1084","E1048","E1124","E1172","E1032","E1159","E1308","E1057","E1007","E1155","E1254","E1002","E1206","E1320","E1219","E1277","E1063","E1140","E1138","E1107","E1041"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
"Q31":{"any":"yes"},
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
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```