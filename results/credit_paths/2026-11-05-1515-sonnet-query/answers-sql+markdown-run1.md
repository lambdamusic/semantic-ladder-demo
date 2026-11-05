**Q1.** A-. Kestrel's rating from A01 (assigned 2024-03-12) held until A02 on 2025-06-20.

**Q2.** No. The only 2026 Kestrel action, A03, is an affirmation with the outlook revised to Negative.

**Q3.** No. The 2031 note (I02) is subordinated and was cut to BB+ by A07, which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (2025-09-15, outlook POS).

**Q5.** Northwind Holdings (E02). I03 is guaranteed by E02, and its instrument rating is A (A10/A11), in line with E02's issuer rating of A.

**Q6.** Valdoria Telecom's FC rating is BB against BBB- for LC (A14, A13). The FC rating is held to Valdoria's Country Ceiling of BB (A12), and LC ratings are not capped.

**Q7.** 38 issuers had a downgrade action in 2026; the full list is in the JSON. It includes E08 and E10.

**Q8.** E08. Saxby Shipping went to RD on 2026-07-08 (A22).

**Q9.** 377 distinct issuers held an issuer rating on 1 Oct 2026, with duplicate records merged by LEI and QA records excluded.

**Q10.** Depends. Valdoria Telecom's LC rating is BBB- (investment grade) and its FC rating is BB (speculative grade).

**Q11.** BBB+. Marlow was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-, from A34 (assigned 2023-01-15).

**Q13.** 1, the downgrade A36.

**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 and E17 share an LEI, and the downgrade to BBB+ came only on 2026-04-15 (A27).

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now; the later actions are a watch (A35) and an affirmation (A33).

**Q17.** No. Orrin Bank's only 2026 action is the Rating Watch Negative A17, which is not a downgrade.

**Q18.** 32 issuers were on RWN on 1 Oct 2026, including E06; the list is in the JSON.

**Q19.** 47 issuers had a Negative outlook, including E01 and E09; the list is in the JSON.

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and the rating before that was BB.

**Q21.** 35 entities had their issuer rating withdrawn and held no issuer rating on 1 Oct 2026, including E07; the list is in the JSON.

**Q22.** E08 is the only entity ever at RD or D.

**Q23.** F2 (A04).

**Q24.** Yes. Kestrel's issuer rating is BBB.

**Q25.** 72 instruments held an investment-grade rating on 1 Oct 2026. EX actions are excluded.

**Q26.** A+ (A40).

**Q27.** A- (A42). The note is subordinated.

**Q28.** BBB+ (A38).

**Q29.** None. The Republic of Valdoria has only a Country Ceiling (A12), which is not a rating.

**Q30.** 13 entities had an FC rating exactly at their country's ceiling (BB for VD, A for CV); the list is in the JSON.

**Q31.** No. No company in CV or VD has an FC rating above its ceiling.

**Q32.** E09. The chain is E11, E10, E09.

**Q33.** Halden Bank (E10). It guarantees I05, which is rated BBB+ after A29, in line with E10's own BBB+.

**Q34.** No. Halden Bank (E10) sits under E09, while Halden Foods (E12) has no parent.

**Q35.** 3.

**Q36.** 2. E03 is the same entity as E02.

**Q37.** 497. There are 495 distinct LEIs plus 2 records with no LEI, with QA excluded.

**Q38.** No. They have different LEIs.

**Q39.** A.

**Q40.** 79.

**Q41.** None. Brindle Capital (E16) is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for country.

**Q43.** 1, which is Halden Bank (E10).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer is domiciled.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47, EX).

**Q48.** 113 instruments held a rating.

**Q49.** E5001.

**Q50.** 6.

**Q51.** 58.

**Q52.** 19.

**Q53.** No. The RATINGS parent link puts E5062 under E5059 (via E5060). The RESEARCH record E5168 pointing to Rotam does not override it.

**Q54.** E5106, E5124 and E5130. E5106's country is VD per the RESEARCH record E5169.

**Q55.** 31.

**Q56.** BB- (E5144).

**Q57.** E5002. E5011 goes via E5005 to E5002, and E5013 goes via E5006 to E5002.

**Q58.** E5145 (Geren Group SA) guarantees I5007, which is issued by E5133 in the Vesol group.

**Q59.** 12.

**Q60.** Geren Group (E5145). It is not in the same group as the issuer E5133, which is in Vesol (E5132).

**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1167","E1058","E1053","E1144","E5019","E1159","E1057","E1243","E5113","E08","E1169","E1186","E1112","E1080","E5116","E5156","E1294","E1151","E1064","E1093","E1051","E1290","E1285","E5097","E1163","E1213","E1300","E1307","E1229","E1298","E1263","E1255","E5033","E1228","E10","E5059","E1160"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":377},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1109","E1168","E1061","E1238","E1297","E1013","E1098","E1126","E06","E1133","E1088","E1194","E1267","E1181","E1099","E1260","E1132","E1019","E1006","E1264","E1039","E1266","E1059","E1203","E1146","E1323","E1066","E1314","E1317","E1037","E1209","E1242"]},
"Q19":{"issuers":["E1211","E5023","E1046","E5019","E5059","E5020","E5119","E1158","E1055","E5039","E1105","E1034","E5097","E1263","E1188","E1294","E1059","E1228","E5099","E1029","E1271","E1079","E5073","E5116","E09","E1190","E1282","E1261","E5062","E5141","E1072","E5013","E5156","E5050","E1248","E1064","E1118","E5102","E5057","E01","E5131","E1056","E1160","E1080","E5113","E1300","E1005"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1244","E1316","E1021","E07","E1166","E1140","E1063","E1138","E1041","E1107","E1062","E1277","E1206","E1320","E1219","E1205","E1121","E1225","E1200","E1234","E1233","E1048","E1084","E1001","E1124","E1172","E1032","E1253","E1308","E1159","E1155","E1057","E1007","E1076","E1218"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E5012","E5047","E1126","E1101","E1028","E5091","E05","E5124","E1236","E1039","E5116","E1194","E15"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":497},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":79},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":58},
"Q52":{"count":19},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106","E5124","E5130"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":19}
}
```