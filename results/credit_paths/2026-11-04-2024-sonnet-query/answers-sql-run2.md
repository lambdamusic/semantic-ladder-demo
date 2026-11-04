**Q1.** A-. Kestrel's issuer rating (E01) was A- from A01 (2024-03-12) until it was downgraded on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is A03 (2026-02-10), an affirmation at BBB with the outlook moved to Negative.

**Q3.** No. The 2031 note (I02) was cut to BB+ by A07 on 2025-06-20, which is below investment grade.

**Q4.** Positive. E03 "NORTHWIND HLDGS" has the same LEI as E02, so I treat it as the same entity. Its latest action is A09 (2025-09-15), A with a Positive outlook.

**Q5.** The guarantor, E02 (Northwind Holdings), is the risk. I03 is guaranteed by E02, and its latest rating is A (A11).

**Q6.** The data does not state a reason. It is consistent with the sovereign ceiling: VD's Country Ceiling is BB (A12), which matches Valdoria Telecom's (E05) FC rating of BB (A14), while the LC rating is BBB- (A13).

**Q7.** 49 issuers had a downgrade action in 2026. They include E08, E10, E16 and E5059, and the full list is in the JSON.

**Q8.** E08 (Saxby Shipping). It was downgraded to RD on 2026-07-08 (A22) and nothing later is recorded.

**Q9.** 390. 393 entity IDs hold a current LTIDR, but duplicate records share LEIs, so I count distinct LEIs. This includes the two sovereign entries.

**Q10.** Depends. E05's FC rating is BB (not investment grade) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions were a watch (A35) and an affirmation (A33).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10's rating was A- from A26 until the downgrade to BBB+ on 2026-04-15 (A27). E17 is a duplicate record with no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after the watch (A35) and affirmation (A33).

**Q17.** No. E06 has only a Rating Watch Negative placement (A17) in 2026, with the rating still A-.

**Q18.** 32 issuers were on RWN on 1 Oct 2026, including E06, E1006 and E1266. The full list is in the JSON.

**Q19.** 57 issuers had a Negative outlook (excluding those on RWN), including E01, E09 and E1300. The full list is in the JSON.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not for default.

**Q21.** 35 entities, including E07, E1225 and E1200. These all have a withdrawn LTIDR; the full list is in the JSON.

**Q22.** E08 only, rated RD by A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 72 instruments.

**Q26.** A+, from A40.

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** 13 entities have an FC issuer rating exactly at the ceiling (A for CV, BB for VD), including E15 and E05. The full list is in the JSON.

**Q31.** No. None of the non-sovereign FC ratings exceeds the CV ceiling (A) or the VD ceiling (BB).

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10 (Halden Bank AG), is the risk. I05 is guaranteed by E10, and the note is rated BBB+ (A29).

**Q34.** No. E12 has no parent and sits outside the E09 group that contains E10.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 509. The 540 entity rows contain duplicate LEIs.

**Q38.** No. E06 and E13 have different LEIs and different countries.

**Q39.** A. E02 is A (A08) and E03 has A (A09).

**Q40.** 87 distinct LEIs among the GB issuers with a current rating (88 by entity ID).

**Q41.** BB+. E16 was downgraded to BB+ by A44.

**Q42.** DE. E10 is DE, but duplicate record E17 (same LEI, from RESEARCH) says LU. I took the RATINGS-system record.

**Q43.** 1.

**Q44.** Yes. I07 is denominated in XVD, which I read as the Valdoria local currency.

**Q45.** No. The ceiling (BB) applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a Credit Opinion (A46, BBB) and no LTIDR.

**Q47.** None. I08's latest action is EX on 2026-09-01 (A47). I read EX as the rating ending, though the data does not define it.

**Q48.** 113 instruments.

**Q49.** E5167. The chain is E5047→E5035→E5023→E5011→E5167.

**Q50.** 4.

**Q51.** 55.

**Q52.** 20.

**Q53.** No. Their roots are E5059 and E5086.

**Q54.** E5130 and E5124.

**Q55.** 23.

**Q56.** BB-, held by E5144.

**Q57.** None. E5011 (root E5167) and E5013 (root E5001) share no ancestor.

**Q58.** E5145 guarantees I5007, which was issued by E5133 in another group.

**Q59.** 11.

**Q60.** The guarantor E5145 (Geren Group SA) is the risk, and it is not in the same group as the issuer. The issuer E5133 sits under E5132, whereas E5145 is its own root.

**Q61.** 18.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E5019","E5059","E5097","E5113","E5116","E5156"]},
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
"Q18":{"issuers":["E1266","E1039","E1059","E1006","E1264","E1019","E1109","E1168","E1317","E1037","E1242","E1066","E1314","E1146","E1203","E1323","E1238","E1297","E1061","E1013","E1210","E1181","E1133","E06","E1088","E1194","E1126","E1098","E1267","E1132","E1099","E1260"]},
"Q19":{"issuers":["E1211","E1262","E5019","E09","E1060","E5131","E5113","E1064","E01","E1118","E1343","E1079","E1347","E1271","E1263","E5073","E5050","E1228","E1345","E5099","E1029","E5059","E1342","E1351","E5020","E1161","E5170","E5023","E5062","E1056","E1340","E5013","E1282","E1348","E1046","E1294","E5141","E1055","E5119","E1350","E5057","E1188","E1248","E1034","E5116","E1080","E1005","E1344","E1105","E1158","E1072","E5156","E1190","E5039","E5102","E5097","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1225","E1200","E1234","E1233","E1140","E1041","E1107","E1063","E1138","E1219","E1206","E1320","E1002","E07","E1021","E1166","E1277","E1155","E1032","E1007","E1308","E1057","E1159","E1062","E1172","E1124","E1076","E1218","E1254","E1048","E1084","E1316","E1244","E1121","E1205"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E5124","E1039","E1101","E1126","E5047","E1236","E5116","E1194","E5012","E5091","E15","E05","E1028"]},
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
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5167"},
"Q50":{"count":4},
"Q51":{"count":55},
"Q52":{"count":20},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5130","E5124"]},
"Q55":{"count":23},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"none"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":11},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":18}}
```