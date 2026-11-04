**Q1.** A-. Kestrel Energy (E01) held A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.
**Q2.** No. E01's only 2026 action is A03 (2026-02-10), an affirmation with the outlook revised to Negative.
**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ by A07 on 2025-06-20, which is speculative grade.
**Q4.** Positive. E03 is the RESEARCH record of the same LEI as E02, so both are one entity, and its latest action is A09 (2025-09-15), an affirmation at A with a Positive outlook.
**Q5.** The holder takes the credit risk of E02 (Northwind Holdings), the guarantor of I03 (issuer E04). The note is rated A, per A10 and A11, in line with E02's A.
**Q6.** Valdoria's Country Ceiling (VD, BB, A12) caps foreign-currency ratings, so E05's FC rating is BB (A14). Its LC rating is BBB- (A13) because local-currency ratings are not capped.
**Q7.** 31 issuers had a downgrade action dated in 2026; they are listed in the JSON.
**Q8.** E08 (Saxby Shipping). A22 on 2026-07-08 downgraded it to RD, a default, and no later action changes that.
**Q9.** 278. This counts distinct LEIs whose latest long-term issuer rating on 2026-10-01 is not a withdrawal and excludes QA records.
**Q10.** Depends. E05 is BB on a foreign-currency basis (speculative grade) and BBB- on a local-currency basis (investment grade).
**Q11.** BBB+. Marlow Utilities (E14) was downgraded to BBB+ by A36 on 2024-09-30, and the next action (A35) is dated 2025-11-20.
**Q12.** A-, from A34 (2023-01-15).
**Q13.** 1. Only A36 is a downgrade for E14, since the Watch and the affirmation are not.
**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30), after that date.
**Q15.** A-. E10's rating was A- from A26 until the downgrade A27 on 2026-04-15.
**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now; the Watch and affirmation did not change it.
**Q17.** No. Orrin Bank (E06) has only A16 (assigned) and A17 (Watch Negative, rating unchanged).
**Q18.** 32 issuers were on Rating Watch Negative, listed in the JSON.
**Q19.** 30 issuers had a Negative outlook, listed in the JSON. I excluded E1172 and E1057 because they were withdrawn.
**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19, commercial reasons), and a withdrawal is not a default.
**Q21.** 35 entities had an issuer rating that was later withdrawn and had none on 2026-10-01; they are listed in the JSON.
**Q22.** Only E08, the one entity with an RD or D rating.
**Q23.** F2, from A04.
**Q24.** Yes. E01's long-term rating is BBB, which is investment grade.
**Q25.** 66. This counts instruments whose latest non-Expected rating on 2026-10-01 is investment grade.
**Q26.** A+, from A40 (LC basis).
**Q27.** A-, from A42. I06 is subordinated.
**Q28.** BBB+, from A38.
**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling (A12), which is not its issuer rating.
**Q30.** 8 entities. The CV ceiling is A and E15, E1039 and E1194 are at A. The VD ceiling is BB and E05, E1028, E1101, E1126 and E1236 are at BB.
**Q31.** No. No CV entity is above A and no VD entity is above BB.
**Q32.** E09 (Halden Group). The chain is E11 to E10 to E09.
**Q33.** The holder takes the credit risk of E10 (Halden Bank), the guarantor. I05 is rated BBB+ after A29 on 2026-04-15.
**Q34.** No. E12 (Halden Foods) has no parent link to E09 or E10.
**Q35.** 3: E09, E10 and E11. E17 is the RESEARCH record of E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 331, counting distinct LEIs (sovereigns by record ID) and excluding QA records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A. E02 and E03 are the same entity, and its latest action is A09, an affirmation at A.
**Q40.** 66 distinct GB-domiciled issuers.
**Q41.** None. E16 (Brindle Capital) is a QA test record, so it and its actions are ignored.
**Q42.** DE. The RATINGS record E10 holds, over the RESEARCH record E17 that says LU.
**Q43.** 0. The only LU record is E17, and the RATINGS record for the same LEI (E10) says DE.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** No. I07 is a local-currency obligation, rated BBB- (A45), and the Country Ceiling (BB) does not cap it.
**Q46.** No. E11 (Halden Leasing) is a finance subsidiary whose only action is a credit opinion (A46), which is not a rating.
**Q47.** None. I08's only action is an Expected rating (A47), so the note is still unrated.
**Q48.** 106 instruments held a rating on 2026-10-01, excluding Expected ratings.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1080","E1093","E1151","E1161","E1228","E1285","E1294","E1299","E08","E1053","E1058","E1112","E1159","E1167","E1170","E1186","E1263","E10","E1051","E1057","E1064","E1163","E1290","E1300","E1307","E1144","E1213","E1255","E1243","E1229"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1032","E1062","E1076","E1124","E1138","E1140","E1200","E1316","E1048","E1121","E1155","E1159","E1205","E1206","E1218","E1219","E1225","E1233","E1254","E1277","E1320","E1007","E1041","E1057","E1063","E1084","E1107","E1166","E1172","E1234","E1244","E1308","E1021"]},
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
"Q48":{"count":106}}
```