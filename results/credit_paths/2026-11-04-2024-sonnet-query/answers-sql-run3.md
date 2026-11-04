**Q1.** A-. E01's rating was A- from A01 (2024-03-12) until it was downgraded to BBB in A02 on 2025-06-20.
**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with Negative outlook.
**Q3.** No. The 2031 note I02 is subordinated and was cut to BB+ in A07, which is sub-investment grade.
**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) is an affirmation at A with Positive outlook.
**Q5.** A holder takes the credit risk of E02, the guarantor of I03, which is currently rated A (A08, affirmed in A09).
**Q6.** E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13). The BB matches the Valdoria country ceiling of BB (A12), which caps foreign-currency ratings.
**Q7.** 49 issuers had a downgrade (DG) recorded in 2026 up to today (4 Nov 2026), listed in the JSON. I excluded E1341 (2026-11-09) and E5033 (2026-11-06) because those dates are later than today.
**Q8.** E08. It was downgraded to RD in A22 on 2026-07-08 after a distressed debt exchange.
**Q9.** 390 distinct issuers held a foreign-currency issuer rating on 1 Oct 2026. Duplicate records sharing an LEI are counted once, and withdrawn ratings are excluded.
**Q10.** Depends. E05 is investment grade in local currency (BBB-) but not in foreign currency (BB).
**Q11.** BBB+. E14 was downgraded in A36 on 2024-09-30, and the later action A35 is a watch placement at the same rating.
**Q12.** A-, from A34.
**Q13.** 1. Only A36 is a downgrade for E14.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. E10's rating was A- (A26) until the downgrade in A27 on 2026-04-15.
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+; A35 and A33 only changed the watch status and affirmed it.
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative placement at A-.
**Q18.** 32 issuers were on RWN; they are listed in the JSON.
**Q19.** 57 issuers had a Negative outlook; they are listed in the JSON.
**Q20.** No. E07's rating was withdrawn (A19, WD), not set to a default grade.
**Q21.** 36 entities, listed in the JSON. Their latest foreign-currency issuer action on or before 1 Oct 2026 was a withdrawal.
**Q22.** E08 only, rated RD in A22.
**Q23.** F2, from A04.
**Q24.** Yes. E01's issuer rating is BBB.
**Q25.** 72 instruments were rated investment grade on 1 Oct 2026, excluding expired ratings.
**Q26.** A+, from A40.
**Q27.** A-. I06 has had a single rating, A42.
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a country ceiling (A12, BB) and no issuer rating.
**Q30.** Nine VD entities are at the BB ceiling and four CV entities are at the A ceiling (ceilings from A12 and A37). They are listed in the JSON.
**Q31.** No. No VD entity is above BB and no CV entity is above A.
**Q32.** E09.
**Q33.** A holder takes the risk of E10, the guarantor of I05, which is currently rated BBB+ (A27).
**Q34.** No. E12 has no parent and no link to E09.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 511 distinct legal entities after merging records that share an LEI.
**Q38.** No. E06 and E13 have different LEIs and different countries (DE and US).
**Q39.** A (A09, via E03).
**Q40.** 87 distinct GB-domiciled issuers.
**Q41.** BB+. E16 was downgraded in A44.
**Q42.** DE. E17 shows LU, but it is a RESEARCH duplicate of E10 with the same LEI.
**Q43.** 0. The only LU record, E17, duplicates E10, which is domiciled in DE.
**Q44.** Yes. I07 is denominated in XVD, the Valdoria currency.
**Q45.** No. I07 is a local-currency note rated BBB- (A45). The BB country ceiling constrains foreign-currency ratings, and I07's rating equals E05's local-currency rating.
**Q46.** No. E11 has only a credit opinion (A46, CO), not an issuer rating.
**Q47.** None. I08's latest action is A47, an expiry (EX) on 2026-09-01.
**Q48.** 113 instruments held a rating on 1 Oct 2026, excluding expired ones.
**Q49.** E5167, via the chain E5167>E5011>E5023>E5035>E5047.
**Q50.** 4 levels.
**Q51.** 55.
**Q52.** 20.
**Q53.** No. E5062 sits under E5059, while E5086 is its own top entity.
**Q54.** E5124 and E5130.
**Q55.** 23 rated entities have a VD-domiciled entity above them in their chain of parents.
**Q56.** BB-, held by E5144.
**Q57.** None. E5011 is in the E5167 group and E5013 is in the E5001 group, so they share no ancestor.
**Q58.** E5145 guarantees I5007, which is issued by E5133 in the E5132 group.
**Q59.** 11.
**Q60.** A holder takes the risk of E5145, the guarantor of I5007. It is not in the same group as the issuer E5133, whose group top is E5132.
**Q61.** 18 members hold a sub-investment-grade foreign-currency issuer rating.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E1170","E1167","E5097","E1053","E5156","E1163","E1057","E1346","E1300","E1307","E1228","E1342","E1340","E1255","E1285","E1345","E1263","E1112","E1294","E1213","E1348","E1144","E1229","E1161","E1344","E1058","E1347","E5116","E1343","E16","E1051","E1080","E5059","E1351","E1034","E1243","E1186","E5113","E1350","E5019","E1093","E1151","E10","E1290","E1299","E1064","E1159","E1349"]},
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
"Q18":{"issuers":["E06","E1133","E1006","E1264","E1019","E1297","E1238","E1013","E1061","E1037","E1317","E1242","E1039","E1266","E1059","E1109","E1168","E1194","E1088","E1099","E1260","E1132","E1066","E1146","E1323","E1203","E1314","E1181","E1210","E1098","E1126","E1267"]},
"Q19":{"issuers":["E1105","E1344","E1158","E1064","E1118","E01","E1343","E1046","E1348","E5099","E1345","E1228","E5050","E1263","E5073","E5039","E5156","E1072","E1190","E1079","E1161","E1351","E1029","E5020","E1342","E5059","E5170","E5097","E1300","E5102","E1294","E1350","E1055","E5141","E5119","E09","E1211","E5019","E1060","E1262","E5113","E5131","E1080","E5116","E1005","E5057","E1248","E1034","E1188","E1340","E5013","E1282","E5023","E5062","E1056","E1271","E1347"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1316","E1244","E1057","E1308","E1007","E1159","E1032","E1155","E1206","E1320","E1219","E1218","E1233","E1200","E1225","E1234","E1021","E1279","E07","E1166","E1084","E1048","E1062","E1121","E1205","E1107","E1041","E1140","E1138","E1063","E1002","E1076","E1277","E1254","E1172","E1124"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E5124","E1236","E5012","E1101","E05","E5091","E1028","E1126","E5047","E1039","E15","E5116","E1194"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":511},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":87},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
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
"Q54":{"entities":["E5124","E5130"]},
"Q55":{"count":23},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"none"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":11},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":18}}
```