**Q1.** A-. Kestrel's FC LTIDR was A- from 2024-03-12 to 2025-06-20 (E01, A01).
**Q2.** No. The only downgrade was on 2025-06-20 (A02); the 2026-02-10 action (A03) was an affirmation with the outlook moved to Negative.
**Q3.** No. The 2031 note I02 has been BB+ since 2025-06-20, which is below investment grade.
**Q4.** Positive. Northwind Holdings (E02, merged with E03) has an A rating with POS outlook since 2025-09-15 (A09).
**Q5.** E02, rated A. I03 is guaranteed by E02, and I03 itself is rated A (A11).
**Q6.** Not asked in the JSON. The VD ceiling is BB (from 2025-04-01) and E05's FC rating is BB, while its LC rating is BBB-.
**Q7.** 38 issuers had an LTIDR downgrade (DG) starting in 2026; they are listed in the JSON.
**Q8.** E08, whose RD rating has been in force since 2026-07-08 (A22).
**Q9.** 376 distinct rated entities hold a current FC LTIDR (WD excluded). This count includes the sovereign CV.
**Q10.** Depends. E05 is BB on FC (A14) and BBB- on LC (A13), so only the LC rating is investment grade.
**Q11.** BBB+ (E14, A36).
**Q12.** A- (E14, A34).
**Q13.** Once, on 2024-09-30 (A36). The A- to BBB+ move is the only DG on E14.
**Q14.** BB- (E12, A30).
**Q15.** A- (E10, A26).
**Q16.** No. E14 has been BBB+ throughout, and only the watch and outlook changed (A35, A33).
**Q17.** No. E06 stayed at A- and was only placed on Rating Watch Negative on 2026-09-03 (A17).
**Q18.** 32 issuers are on RWN; they are listed in the JSON.
**Q19.** 48 issuers have a NEG outlook; they are listed in the JSON.
**Q20.** No. E07's rating was withdrawn (WD, A19), which is not a default; the only defaulted entity is E08.
**Q21.** 36 entities had an FC LTIDR before but have none in force now (withdrawn or ended); they are listed in the JSON.
**Q22.** E08 only (RD, A22).
**Q23.** F2 (E01, A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 72 instruments.
**Q26.** A+ (E15, A40).
**Q27.** A- (I06, A42).
**Q28.** BBB+ (CV, A38).
**Q29.** None. VD has no rating records.
**Q30.** 13 entities have an FC rating equal to their ceiling; they are listed in the JSON.
**Q31.** No. None of the current FC ratings exceed their ceiling.
**Q32.** E09. E11's parent is E10, and its ultimate parent is E09.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and I05 is rated BBB+ (A29).
**Q34.** No. E12 has no parent, while E10 belongs to the E09 group.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 497, since the entities table is already deduplicated.
**Q38.** No. E06 and E13 are separate entities.
**Q39.** A (E02, A09).
**Q40.** 79.
**Q41.** None. No entity named Brindle exists in the data.
**Q42.** LU (E10).
**Q43.** 1.
**Q44.** Yes. I07 is denominated in XVD with local_currency = yes.
**Q45.** Yes. I07 is rated BBB- (A45) and the VD ceiling is BB.
**Q46.** No. E11 has no rating records.
**Q47.** None. I08 has no rating records.
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6 levels (ancestors table, E5047 to E5001).
**Q51.** 58.
**Q52.** 19.
**Q53.** No. E5062 is in the Belir group (E5059) and E5086 is a separate top entity.
**Q54.** E5106, E5124 and E5130.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002. It is 2 levels above both E5011 and E5013.
**Q58.** E5145, which guarantees I5007 issued by E5133 in the Vesol group.
**Q59.** 12.
**Q60.** E5145 (Geren Group SA). It is not in the same group as the issuer E5133, which is in the E5132 group.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1290","E1058","E1167","E08","E1112","E1169","E1186","E1053","E1057","E1144","E1159","E1243","E5019","E5113","E1064","E1093","E1080","E5116","E1151","E1294","E1051","E1163","E1213","E1300","E5097","E10","E1160","E5059","E1034","E1228","E1229","E1255","E1263","E1298","E1307","E5033","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":376},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"BB-"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1013","E1061","E1238","E1297","E1109","E1168","E1099","E1132","E1260","E1006","E1019","E1264","E06","E1133","E1088","E1194","E1066","E1146","E1203","E1314","E1323","E1037","E1209","E1242","E1317","E1181","E1098","E1126","E1267","E1039","E1059","E1266"]},
"Q19":{"issuers":["E1005","E1080","E5116","E1105","E1158","E1046","E1055","E1294","E5119","E5141","E1034","E1188","E1248","E5057","E1079","E1056","E1059","E1282","E5013","E5023","E5062","E1300","E5097","E5102","E1072","E1190","E5039","E5156","E01","E1064","E1118","E1261","E09","E1211","E5019","E5113","E5131","E1029","E1160","E5020","E5059","E1271","E1228","E1263","E5033","E5050","E5073","E5099"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1121","E1205","E1206","E1219","E1320","E1244","E1316","E1062","E1277","E1218","E07","E1021","E1166","E1279","E1001","E1124","E1172","E1048","E1084","E1041","E1063","E1107","E1138","E1140","E1200","E1225","E1233","E1234","E1076"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236","E5012","E5047","E5091","E5116","E5124"]},
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
"Q45":{"above_ceiling":"yes"},
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