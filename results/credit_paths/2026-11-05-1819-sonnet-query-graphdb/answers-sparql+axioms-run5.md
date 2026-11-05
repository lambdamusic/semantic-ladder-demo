**Q1.** A-. A01 (A-, 2024-03-12) was in force until A02 replaced it on 2025-06-20.
**Q2.** No. The only downgrade was A02 in 2025; A03 on 2026-02-10 is an Affirmation with a Negative outlook.
**Q3.** No, BB+. The 2031 note (I02) is subordinated, and A07 downgraded it to BB+.
**Q4.** Positive. E02 and E03 are the same entity, and the latest action, A09 (2025-09-15), carries a Positive outlook.
**Q5.** The guarantor E02 (Northwind Holdings). I03 is rated A (A11).
**Q6.** The data does not state a reason, but it fits the Country Ceiling. Valdoria's ceiling is BB (A12) and E05's foreign-currency rating is BB (A14). Its local-currency rating is BBB- (A13) and is not capped.
**Q7.** The 51 entities are listed in the JSON. They are entities with a Downgraded long-term issuer action dated in 2026, including E08, E10 and E16.
**Q8.** E08. A22 moved it to RD on 2026-07-08.
**Q9.** 377 distinct issuers hold a long-term issuer rating in force.
**Q10.** Depends. Its foreign-currency rating is BB (sub-investment grade), but its local-currency rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1, from A36 on 2024-09-30.
**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.
**Q15.** A- (A26, in force until 2026-04-15).
**Q16.** No. The rating stayed BBB+ throughout; the Watch (A35) and the Affirmation (A33) are not changes.
**Q17.** No. A17 is only a Watch Negative placement.
**Q18.** The 32 entities with a Rating Watch Negative in force are in the JSON.
**Q19.** The 48 entities with a Negative outlook in force are in the JSON.
**Q20.** No. A19 is a withdrawal, which is not a default.
**Q21.** The 49 entities in the JSON had an issuer rating at some point but none in force on 1 October 2026. The query excluded records whose same-entity twin still has a rating.
**Q22.** Only E08. A22 moved it to RD, the only default-level rating in the data.
**Q23.** F2 (A04).
**Q24.** Yes. It is BBB (A03).
**Q25.** 72 instruments hold an investment-grade rating in force.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria only has a Country Ceiling (A12), which is not a rating.
**Q30.** The 13 entities in the JSON have a foreign-currency rating equal to their country's ceiling (A for CV, BB for VD).
**Q31.** No. Every foreign-currency rating at or above the ceiling was exactly at it.
**Q32.** E09.
**Q33.** E10 (Halden Bank), the guarantor of I05. I05 is rated BBB+ (A29).
**Q34.** No. E12 is its own ultimate parent, while E10 sits under E09.
**Q35.** 3 distinct legal entities: E09, E10 and E11. E17 is a duplicate record of E10.
**Q36.** 2 distinct legal entities: E02 and E04. E03 is a duplicate record of E02.
**Q37.** 511 distinct entities. There are 540 records, and the duplicates are linked by sameEntityAs.
**Q38.** No. E06 and E13 are not linked by sameEntityAs and differ in domicile (DE and US).
**Q39.** A. E03 carries A09 (A, 2025-09-15), and E02 and E03 are the same entity.
**Q40.** 79.
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1.
**Q44.** Yes. I07 has localCurrency = true.
**Q45.** No. It is rated BBB- (A45). Its flag marks it as local currency, so the ceiling does not cap it.
**Q46.** No. E11 only has a Credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 only has an Expected rating (A47), so it is unrated.
**Q48.** 113 instruments.
**Q49.** E5001.
**Q50.** 7 levels. E5047 has 7 ancestors.
**Q51.** 58 entities.
**Q52.** 19 entities. E5168 is a duplicate record of E5062, so it is not counted separately.
**Q53.** Depends. E5062 (Belir Mining) is linked to E5168, whose parent is Rotam (E5086), but both records resolve to ultimate parent E5059 (Belir Group).
**Q54.** E5106 and E5169 are domiciled in VD.
**Q55.** 31 rated entities have an ancestor domiciled in VD.
**Q56.** BB-. E5144 is the lowest current foreign-currency rating in the Vesol group.
**Q57.** E5002. It is the nearest entity in both chains (E5011 via E5005, E5013 via E5006).
**Q58.** E5145. It guarantees I5007, issued by E5133, which is in the Vesol group.
**Q59.** 10 entities sit three levels below E5001 (E5013 to E5022).
**Q60.** The risk is E5145, and no, it is not in the issuer's group. The issuer E5133 is in the Vesol group, while E5145 is its own ultimate parent.
**Q61.** 19 members hold a foreign-currency rating below investment grade; the top, E5001, has no rating.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1300","E1151","E1167","E1080","E5113","E1051","E10","E1034","E1347","E1343","E1290","E1350","E1341","E1229","E1342","E5097","E1351","E5059","E1255","E1340","E16","E1186","E1161","E1263","E1058","E1349","E1112","E08","E5116","E1170","E1344","E1228","E1163","E1243","E5033","E1299","E5019","E1053","E1348","E1213","E1346","E1159","E1057","E1345","E1064","E1294","E1093","E1144","E1307","E5156"]},
"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1203","E1314","E1194","E1210","E1260","E1133","E1146","E1242","E1066","E1168","E1297","E1109","E1061","E1132","E1088","E06","E1098","E1266","E1006","E1267","E1037","E1013","E1317","E1181","E1323","E1059","E1099","E1238","E1264","E1039","E1126","E1019"]},
"Q19":{"issuers":["E1300","E5099","E1080","E1105","E5113","E1034","E1118","E1056","E1064","E1055","E5097","E1046","E5059","E5020","E1161","E1263","E1282","E01","E5131","E5023","E5141","E5116","E09","E1271","E5039","E5102","E1228","E1060","E5073","E5033","E1079","E5019","E5050","E5062","E1072","E1190","E1005","E1248","E5057","E1294","E1188","E5119","E1029","E5013","E1262","E1158","E5156","E1211"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1084","E1032","E1234","E1219","E1107","E1244","E1172","E1347","E1062","E1343","E1350","E1345","E1341","E1349","E1155","E1166","E1342","E1200","E1351","E1277","E1124","E1340","E1076","E1138","E16","E1348","E1041","E1159","E1140","E1346","E1002","E1344","E1121","E1308","E1007","E1316","E07","E1206","E1225","E1057","E1205","E1320","E1063","E1233","E1254","E5170","E1218","E1048","E1021"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1194","E15","E5116","E1039","E5124","E1236","E1126","E05","E5047","E1028","E1101","E5091","E5012"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":7},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"depends"},"Q54":{"entities":["E5106","E5169"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":10},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```