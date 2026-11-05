**Q1.** A-. E01's FC issuer rating was A- from 2024-03-12 to 2025-06-20 (A01).
**Q2.** No. The only 2026 action on E01 was an affirmation with a Negative outlook (A03, BBB, 2026-02-10); the downgrade was in 2025 (A02).
**Q3.** No, BB+. The 2031 note I02 has been rated BB+ since 2025-06-20.
**Q4.** Positive. E02's rating A has had a POS outlook since 2025-09-15 (A09).
**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and credit_risk_of is E02.
**Q6.** The data points to the Country Ceiling. Valdoria's ceiling is BB, and E05's FC rating is BB against a LC rating of BBB- (A14, A13). The data doesn't state this reason explicitly.
**Q7.** 37 issuers had a downgrade action in 2026 (listed in the JSON).
**Q8.** E08. Its rating moved to RD on 2026-07-08 (A22).
**Q9.** 377 distinct entities hold an issuer rating in force, excluding WD.
**Q10.** Depends. E05's FC rating is BB (not investment grade) and its LC rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. E14 was downgraded once, on 2024-09-30 (A36).
**Q14.** None. E12's first rating began on 2024-02-01.
**Q15.** A- (A26).
**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A36 to A33); only the watch status changed.
**Q17.** No. E06 was placed on Rating Watch Negative (A17) but kept A-.
**Q18.** 32 issuers were on RWN (listed in the JSON).
**Q19.** 47 issuers had a Negative outlook (listed in the JSON).
**Q20.** No. E07's rating was withdrawn (WD, A19), which is not a default.
**Q21.** 35 entities (listed in the JSON), including E07.
**Q22.** E08 is the only entity with an RD rating (A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's rating is BBB.
**Q25.** 72 instruments held an investment-grade rating.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has no rating records.
**Q30.** 13 entities had an FC rating exactly at their country's ceiling (listed in the JSON).
**Q31.** No. None of the FC ratings returned for entities in VD or CV was above its ceiling.
**Q32.** E09, as shown in the ancestors table.
**Q33.** E10 (Halden Bank), rated BBB+ (A27). I05 is guaranteed by E10.
**Q34.** No. E12 has no parent, while E10 sits under E09.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 (which includes the merged E03) and E04.
**Q37.** 497 entities.
**Q38.** No. E06 and E13 are separate entities with different LEIs and countries.
**Q39.** A.
**Q40.** 79.
**Q41.** None. No entity named Brindle Capital is in the data.
**Q42.** LU.
**Q43.** 1 (E10).
**Q44.** Yes. I07 is flagged local_currency=yes, in XVD.
**Q45.** No. I07 is a local-currency obligation, so the FC ceiling doesn't apply to it. Its BBB- is also above the BB ceiling (A45).
**Q46.** No. There is no rating record for E11.
**Q47.** None. I08 has no INST rating record.
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6 levels (ancestors table: E5047 to E5001).
**Q51.** 58, which is 57 members plus the parent.
**Q52.** 19, which is 18 members plus the parent.
**Q53.** No. E5062 belongs to the E5059 group.
**Q54.** E5106, E5124, E5130.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002. It is the nearest ancestor shared by E5011 (2 levels up) and E5013 (2 levels up).
**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the E5132 group.
**Q59.** 12.
**Q60.** E5145. It is not in the same group as the issuer E5133, whose group is E5132.
**Q61.** 19 members hold a sub-investment-grade FC rating.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1290","E1034","E5156","E1228","E1229","E1255","E1263","E1298","E1307","E1058","E1167","E1064","E1093","E10","E1160","E5059","E1080","E5116","E1151","E1294","E08","E1112","E1169","E1186","E1163","E1213","E1300","E5097","E1053","E1057","E1144","E1159","E1243","E5019","E5113","E1051"]},
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
"Q18":{"issuers":["E1039","E1059","E1266","E1099","E1132","E1260","E1006","E1019","E1264","E1066","E1146","E1203","E1314","E1323","E06","E1133","E1088","E1194","E1098","E1126","E1037","E1209","E1242","E1317","E1267","E1013","E1061","E1238","E1297","E1109","E1168","E1181"]},
"Q19":{"issuers":["E1005","E1080","E5116","E1072","E1190","E5039","E5156","E1228","E1263","E5050","E5073","E5099","E1029","E1160","E5020","E5059","E1046","E09","E1211","E5019","E5113","E5131","E01","E1064","E1118","E1261","E1300","E5097","E5102","E1271","E1079","E1055","E1294","E5119","E5141","E1105","E1158","E1034","E1188","E1248","E5057","E1056","E1059","E1282","E5013","E5023","E5062"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1048","E1084","E1200","E1225","E1233","E1234","E1062","E1244","E1316","E1121","E1205","E1206","E1219","E1320","E1277","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1001","E1124","E1172","E1218","E1041","E1063","E1107","E1138","E1140","E07","E1021","E1166","E1076"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1039","E1101","E1126","E1194","E1236","E15","E5012","E5047","E5091","E5116","E5124"]},
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