**Q1.** A-. E01's rating of A- (A01) ran from 2024-03-12 to 2025-06-20, so it covered 1 January 2025.
**Q2.** No. E01's only 2026 action was an affirmation at BBB with the outlook moved to Negative (A03).
**Q3.** No. I02 (Kestrel 2031 note) is rated BB+ after a downgrade on 2025-06-20 (A07), which is below investment grade.
**Q4.** Positive. E02's current rating is A with a POS outlook (A09).
**Q5.** E02 (Northwind Holdings) is the guarantor and the credit risk of I03. Its rating is A (A09).
**Q6.** The data does not state a reason. The likely cause is the VD Country Ceiling of BB (from 2025-04-01), which matches E05's foreign-currency rating of BB (A14). The local-currency rating is BBB- (A13).
**Q7.** 37 issuers had a downgrade (DG) dated in 2026. They are listed in the JSON. I excluded E5033, whose DG is dated 2026-11-06, after the 1 October 2026 data date.
**Q8.** E08 only. It holds RD from 2026-07-08 (A22), and no other record shows D or RD.
**Q9.** 377. This is the count of distinct entities with an LTIDR or STIDR in force on 1 October 2026, excluding withdrawn (WD) ratings. It includes entities that hold only a local-currency rating.
**Q10.** Depends. E05 is BB in foreign currency, which is not investment grade, and BBB- in local currency, which is.
**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).
**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).
**Q13.** 1. E14 was downgraded once, from A- to BBB+ (A36).
**Q14.** None. E12's first rating (A30) starts on 2024-02-01.
**Q15.** A-. E10 (merged with E17) held A- until 2026-04-15 (A26).
**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). Only the watch and outlook changed in between.
**Q17.** No. E06's 2026 action was a Rating Watch Negative on an A- rating (A17), not a downgrade.
**Q18.** 32 issuers, listed in the JSON, including E06.
**Q19.** 47 issuers, listed in the JSON, including E01 and E09.
**Q20.** No. E07's rating was withdrawn (A19, WD), which is not a default. I found no D or RD for it.
**Q21.** 35 entities, listed in the JSON, including E07. Each had a non-WD issuer rating at some point but none in force on 1 October 2026.
**Q22.** E08 only, which is at RD (A22). Its earlier CCC rating is not a default.
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 72. This is the number of instruments with a non-WD rating of BBB- or higher in force on 1 October 2026.
**Q26.** A+ (A40).
**Q27.** A- (A42, I06).
**Q28.** BBB+ (A38).
**Q29.** None. No rating record exists for VD.
**Q30.** 14 entities have a foreign-currency issuer rating exactly at their country's ceiling. They are listed in the JSON and include E05 (BB, VD ceiling BB) and E15 (A, CV ceiling A).
**Q31.** No. In the ceiling query output, no foreign-currency rating exceeds its country's ceiling.
**Q32.** E09.
**Q33.** E10 (Halden Bank) is the guarantor and the credit risk of I05. Its rating is BBB+ (A27).
**Q34.** No. E12 has no parent, so it is not in E10's group, whose top is E09.
**Q35.** 3.
**Q36.** 2.
**Q37.** 497. The entities table is already deduplicated, with duplicate records merged.
**Q38.** No. E06 and E13 are separate entities with different LEIs and countries (DE and US).
**Q39.** A (A09).
**Q40.** 79.
**Q41.** None. No entity named Brindle Capital appears in the data.
**Q42.** LU.
**Q43.** 1, which is E10.
**Q44.** Yes. I07 has local_currency = yes (XVD).
**Q45.** No. I07 is a local-currency note rated BBB- (A45), and the VD ceiling (BB) applies to foreign-currency ratings.
**Q46.** No. E11 has no rating records.
**Q47.** None. I08 has no rating record.
**Q48.** 113. This is the number of instruments with a non-WD rating in force on 1 October 2026.
**Q49.** E5001.
**Q50.** 6. The ancestors table puts E5001 at levels_up = 6 from E5047.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. E5062's ultimate parent is E5059, while Rotam Group Inc (E5086) is itself a top entity.
**Q54.** E5106, E5124 and E5130. The top entity E5105 is domiciled in FR.
**Q55.** 31.
**Q56.** BB-, held by E5144.
**Q57.** E5002. It is the nearest common ancestor: E5011 reaches it via E5005, and E5013 via E5006.
**Q58.** E5145. It guarantees I5007, issued by E5133, which belongs to the E5132 group.
**Q59.** 12.
**Q60.** E5145 (Geren Group SA) is the guarantor and the credit risk. It is not in the same group as the issuer E5133, which is in the E5132 group.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E5019","E5059","E5097","E5113","E5116","E5156"]},
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
"Q18":{"issuers":["E06","E1133","E1109","E1168","E1006","E1019","E1264","E1037","E1209","E1242","E1317","E1039","E1059","E1266","E1098","E1126","E1181","E1013","E1061","E1238","E1297","E1267","E1088","E1194","E1066","E1146","E1203","E1314","E1323","E1099","E1132","E1260"]},
"Q19":{"issuers":["E1056","E1059","E1282","E5013","E5023","E5062","E09","E1211","E5019","E5113","E5131","E1228","E1263","E5050","E5073","E5099","E1005","E1080","E5116","E1055","E1294","E5119","E5141","E1046","E1072","E1190","E5039","E5156","E1105","E1158","E1079","E1271","E1034","E1188","E1248","E5057","E1300","E5097","E5102","E01","E1064","E1118","E1261","E1029","E1160","E5020","E5059"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1233","E07","E1124","E1063","E1140","E1277","E1007","E1121","E1166","E1253","E1308","E1057","E1172","E1159","E1200","E1206","E1234","E1001","E1244","E1316","E1219","E1320","E1155","E1032","E1225","E1076","E1205","E1218","E1084","E1041","E1048","E1107","E1021","E1062","E1138"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1039","E1101","E1126","E1194","E1236","E15","E5012","E5047","E5091","E5116","E5124","E1019x"]},
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

Correction to the Q30 entry in the JSON block: it contains a stray "E1019x" by mistake. E1019 is BB+ against an A ceiling, so it is not at its ceiling. I also left out E1307, which is BB- against BB. The correct Q30 list has 13 entities: E05, E1028, E1039, E1101, E1126, E1194, E1236, E15, E5012, E5047, E5091, E5116, E5124. That corrects the count of 14 stated in the Q30 answer above.