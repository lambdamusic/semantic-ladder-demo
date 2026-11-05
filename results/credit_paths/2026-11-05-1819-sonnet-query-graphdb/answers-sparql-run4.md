**Q1.** A-. Kestrel Energy (E01) was rated A- from A01 (2024-03-12) until it was downgraded to BBB on 2025-06-20 (A02).
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with a Negative outlook.
**Q3.** No. The 2031 note (I02) was cut to BB+ by A07, which is below investment grade.
**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15), which affirmed A with a Positive outlook.
**Q5.** The guarantor, Northwind Holdings (E02), rated A. The issuer is E04, but I03 is guaranteed by E02 and carries an A rating (A10, A11).
**Q6.** Valdoria Telecom's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The Valdoria Country Ceiling is BB (A12), which plausibly explains the cap, though the data gives no explicit reason.
**Q7.** These are the entities with a downgrade action dated in 2026 up to today. I excluded E1341 and E5033, whose actions are dated after 2026-11-05. I did not filter by rating type or currency basis, so the list may include non-issuer-rating downgrades.
**Q8.** E08, rated RD on 2026-07-08 (A22).
**Q9.** 393. This counts rated entities whose latest issuer rating is not WD as of 2026-10-01. Duplicate records sharing an LEI could make the true count slightly lower.
**Q10.** Depends. The local-currency rating is BBB- (investment grade) and the foreign-currency rating is BB (not).
**Q11.** BBB+, from the 2024-09-30 downgrade (A36).
**Q12.** A- (A34).
**Q13.** 1 (A36).
**Q14.** None. Halden Foods' first rating is dated 2024-02-01 (A30).
**Q15.** A- (A26). Halden Bank AG is E10; E17 is a duplicate record with the same LEI. The downgrade to BBB+ came on 2026-04-15.
**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now (A35 put it on watch; A33 affirmed it).
**Q17.** No. The only 2026 action on Orrin Bank (E06) is A17, a Rating Watch Negative at A-.
**Q18.** The entities whose latest rating on 1 October 2026 carried Rating Watch Negative are listed in the JSON, including E06.
**Q19.** The entities whose latest rating had a Negative outlook are listed in the JSON, including E01 and E09.
**Q20.** No. Pellam Retail (E07) was BB and then withdrawn (WD, A19); it was never in default.
**Q21.** The entities whose latest issuer rating is a withdrawal are listed in the JSON (35 entities, including E07).
**Q22.** E08 only, rated RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 75. This is the number of instruments with a latest non-WD rating of BBB- or better on 2026-10-01.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The only Valdoria rating is a Country Ceiling of BB (A12); there is no issuer rating.
**Q30.** These are the Corvenia entities rated A (the ceiling is A, A37) and the Valdoria entities rated BB (the ceiling is BB, A12).
**Q31.** No. No foreign-currency issuer rating exceeds A for Corvenia or BB for Valdoria.
**Q32.** E09. Halden Leasing (E11) has parent E10, which has parent E09.
**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is issued by E11 and guaranteed by E10, whose rating was cut to BBB+ on 2026-04-15 (A27).
**Q34.** No. Halden Foods (E12) has no parent and sits outside the E09 group.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 511. There are 540 entity records, and I merged 29 records that share an LEI with another record. Two records have no LEI and were kept as separate entities.
**Q38.** No. They are different records, in DE and US.
**Q39.** A (A09 and A08).
**Q40.** 88. This is a count of GB-domiciled entities with a latest non-WD issuer rating on 2026-10-01. It was not deduplicated by LEI.
**Q41.** BB+ (A44). The record for Brindle Capital (E16) comes from the QA source system.
**Q42.** DE. E17 shows LU, but it is a RESEARCH duplicate of E10, which has the same LEI.
**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.
**Q45.** Yes. I07 is rated BBB- (A45), above the BB ceiling.
**Q46.** No. E11 has only a counterparty-obligation rating, BBB (A46), not an issuer rating.
**Q47.** A. A47 is an "EX" action on I08, and the data does not say what EX means, so the rating may no longer be live.
**Q48.** 119. This counts instruments with a latest non-WD rating on 2026-10-01, and it includes I08 per A47.
**Q49.** E5167. The chain is E5047, E5035, E5023, E5011, E5167.
**Q50.** 4 levels.
**Q51.** 55.
**Q52.** 20.
**Q53.** No. Belir Mining sits under E5059 and Rotam under E5086.
**Q54.** E5124 and E5130.
**Q55.** 23. This counts entities with a VD-domiciled ancestor and a latest non-WD issuer rating as of today.
**Q56.** BB-.
**Q57.** E5002. E5011's parent E5167 shares an LEI with E5005, which sits under E5002, and E5013's chain runs E5006, E5002, E5001. That reading depends on treating E5167 and E5005 as the same entity.
**Q58.** E5145. It guarantees I5007, which E5133 issues, and the two are in different groups.
**Q59.** 11.
**Q60.** Credit risk is taken on the guarantor E5145, and it is not in the same group as the issuer E5133.
**Q61.** 18. This counts group members whose latest foreign-currency issuer rating is BB+ or below.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16","E5019","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":393},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1203","E1314","E1194","E1210","E1260","E1133","E1146","E1242","E1066","E1168","E1297","E1109","E1061","E1132","E1088","E06","E1098","E1266","E1006","E1267","E1037","E1013","E1317","E1181","E1323","E1059","E1099","E1238","E1264","E1039","E1126","E1019"]},
"Q19":{"issuers":["E1300","E5099","E1080","E1105","E5113","E1034","E1347","E1343","E1118","E1056","E1064","E1350","E1342","E1055","E5097","E1351","E1046","E5059","E5020","E1340","E1161","E1263","E1282","E01","E5131","E5023","E5141","E5116","E09","E1271","E5039","E5102","E1344","E1228","E1060","E5073","E1079","E5019","E5050","E5062","E1348","E1072","E1190","E1005","E1345","E1248","E5057","E1294","E1188","E5119","E5170","E1029","E5013","E1262","E1158","E5156","E1211"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1084","E1032","E1234","E1219","E1206","E1107","E1244","E1172","E1159","E1057","E1041","E07","E1062","E1277","E1155","E1254","E1121","E1063","E1166","E1021","E1200","E1048","E1124","E1076","E1138","E1140","E1316","E1308","E1007","E1218","E1225","E1205","E1320","E1233"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":75},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":511},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":88},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"A"},
"Q48":{"count":119},
"Q49":{"parent":"E5167"},
"Q50":{"count":4},
"Q51":{"count":55},
"Q52":{"count":20},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5124","E5130"]},
"Q55":{"count":23},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":11},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":18}
}
```