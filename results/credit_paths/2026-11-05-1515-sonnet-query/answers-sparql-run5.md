**Q1.** A-. E01's rating from A01 (2024-03-12) was A- until the downgrade A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), with the outlook moved to Negative.

**Q3.** No. The 2031 note I02 was cut to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity, and the later record A09 (2025-09-15) shows a Positive outlook.

**Q5.** A holder takes the credit risk of E02 (Northwind Holdings), the guarantor of I03. I03 is rated A (A11).

**Q6.** The data doesn't state a reason. It only shows E05 at BBB- on a local-currency basis (A13) and BB on a foreign-currency basis (A14), with a BB Country Ceiling (A12).

**Q7.** The issuers with a downgrade action in 2026 are listed in the JSON below.

**Q8.** E08. It was rated RD on 2026-07-08 (A22).

**Q9.** 390. This is the count of distinct LEIs with a current issuer rating that is not withdrawn.

**Q10.** Depends. E05 is BBB- (investment grade) in local currency and BB (not investment grade) in foreign currency.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-. E14 was rated A- from 2023-01-15 (A34).

**Q13.** 1, the downgrade A36.

**Q14.** None. E12's first rating is dated 2024-02-01.

**Q15.** A-. E10 held A- (A26) until the 2026-04-15 downgrade. E17 shares E10's LEI and carries no ratings.

**Q16.** No. E14's rating stayed BBB+, with only a watch and an outlook change since then.

**Q17.** No. E06 was placed on Rating Watch Negative on 2026-09-03 at an unchanged A- (A17).

**Q18.** The issuers on Rating Watch Negative on 1 October 2026 are in the JSON below.

**Q19.** The issuers with a Negative outlook on 1 October 2026 are in the JSON below.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** The entities whose issuer rating was withdrawn, with no later rating, are in the JSON below.

**Q22.** E08 only. It is the only entity with an RD, D or SD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The BBB issuer rating (A03) is investment grade.

**Q25.** 72. Of 113 instruments rated on 1 October 2026, 72 were investment grade.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. The data holds only a BB Country Ceiling for VD (A12), with no sovereign issuer rating.

**Q30.** The entities whose foreign-currency rating equals their country's ceiling are in the JSON below.

**Q31.** No. No foreign-currency issuer rating exceeds its country's ceiling.

**Q32.** E09.

**Q33.** A holder takes the credit risk of E10, the guarantor of I05. E10 is rated BBB+ (A27).

**Q34.** No. E12 has no parent, so it is not in E09's group.

**Q35.** 3.

**Q36.** 2.

**Q37.** 509. This counts distinct LEIs, which collapses the duplicate records.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A. E02 and E03 are the same entity, and the latest rating is A.

**Q40.** 87.

**Q41.** BB+ (A44).

**Q42.** DE (E10). The duplicate record E17 has the same LEI and lists LU, so the data is inconsistent here.

**Q43.** 1.

**Q44.** Yes. I07 is denominated in XVD, the local currency.

**Q45.** Yes. I07 is rated BBB- against a BB ceiling (A45, A12).

**Q46.** No. E11 has only a BBB counterparty-type rating (A46), not an issuer rating.

**Q47.** None. I08's rating was expired (EX) on 2026-09-01 (A47).

**Q48.** 113.

**Q49.** E5167.

**Q50.** 4. The chain is E5047, E5035, E5023, E5011, E5167.

**Q51.** 55.

**Q52.** 20.

**Q53.** Depends. E5062 is in the Belir group, but the upper-case record E5168 "BELIR MINING SA" sits under the Rotam group.

**Q54.** E5124 and E5130.

**Q55.** 23.

**Q56.** BB-. E5144 is the lowest current foreign-currency issuer rating in the Vesol group.

**Q57.** None. E5011's chain ends at E5167, while E5013's chain runs through E5006, E5002 and E5001, so there is no common ancestor.

**Q58.** E5145. It guarantees I5007, which is issued by E5133 in a different group.

**Q59.** 11.

**Q60.** A holder takes the credit risk of E5145. It is not in the same group as the issuer E5133, which sits under E5132.

**Q61.** 18.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":390},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5170"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1028","E1101","E1126","E05","E1236","E5012","E5047","E5091","E5124","E1039","E1194","E15","E5116"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":509},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":87},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5167"},
"Q50":{"count":4},
"Q51":{"count":55},
"Q52":{"count":20},
"Q53":{"same_group":"depends"},
"Q54":{"entities":["E5124","E5130"]},
"Q55":{"count":23},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"none"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":11},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":18}
}
```