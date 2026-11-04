**Q1.** A-. E01's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. The only 2026 action for E01 is an affirmation at BBB with Negative outlook (A03); the downgrade to BBB was in 2025 (A02).

**Q3.** No. The 2031 note is I02 (subordinated), rated BB+ since 2025-06-20 (A07).

**Q4.** Positive. E02 has been A/POS since 2025-09-15 (A09).

**Q5.** E02, rated A. I03's credit_risk_of is the guarantor E02, and I03 is rated A (A11).

**Q6.** The data does not state a reason. E05 is BB in foreign currency (A14) and BBB- in local currency (A13), and the VD Country Ceiling is BB from 2025-04-01. That is consistent with the ceiling capping the foreign-currency rating, but this is an inference.

**Q7.** 37 entities had a downgrade in 2026 (listed in the JSON below). I counted any entity with a DG action in 2026 or a drop in rating level. E5116 is included only because its DG (A5088) moved the outlook, not the rating. E5033's downgrade starts 2026-11-06, after 1 October, so it is excluded.

**Q8.** E08. It has been RD since 2026-07-08 (A22).

**Q9.** 377. This counts entities with an LTIDR in force on 1 October 2026 that is not WD. It includes the sovereign CV and entities rated only in local currency, such as E1279. Without CV it is 376.

**Q10.** Depends. E05 is BB in foreign currency (not investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+ (A36, 2024-09-30 to 2025-11-20).

**Q12.** A- (A34).

**Q13.** Once. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts 2024-02-01 (A30).

**Q15.** A- (A26, to 2026-04-15). E10 merges E17.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), with only a watch period in between (A35).

**Q17.** No. E06's 2026 action is Rating Watch Negative at an unchanged A- (A17).

**Q18.** 32 entities (listed in the JSON), counting a watch on either the foreign- or local-currency rating.

**Q19.** 46 entities (listed in the JSON), based on the outlook in force on 1 October 2026.

**Q20.** No. E07's rating was withdrawn (A19). WD says nothing about default, and no default rating is recorded for E07.

**Q21.** 35 entities whose issuer ratings ended in WD (listed in the JSON). E1106 and E1279 still have a foreign- or local-currency rating in force, so they are excluded.

**Q22.** E08, the only entity ever rated RD or D (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 72. Of the 113 instrument ratings in force, 72 are BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A-. The 2032 note is I06 (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** E15, E1039 and E1194 are at the CV ceiling of A. E05, E1028, E1101, E1126, E1236, E5012, E5047, E5091 and E5124 are at the VD ceiling of BB.

**Q31.** No. No CV entity is above A and no VD entity is above BB in foreign currency.

**Q32.** E09.

**Q33.** E10, rated BBB+. I05's credit_risk_of is the guarantor E10, and I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent and no link to E09 in the data; the shared "Halden" name is not evidence of a group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 497 rows in entities.csv, where duplicates are already merged.

**Q38.** No. E06 and E13 have different IDs, LEIs and countries, and neither merges the other's records.

**Q39.** A, with Positive outlook (A09).

**Q40.** 79 GB-domiciled entities with an issuer rating in force.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU.

**Q43.** 1, which is E10.

**Q44.** Yes. I07 is flagged local_currency = yes (XVD).

**Q45.** No. I07 is a local-currency note, and the VD ceiling of BB applies to foreign-currency ratings. It is rated BBB-, matching E05's local-currency rating.

**Q46.** No. E11 has no rating rows; I05 is rated through its guarantor.

**Q47.** None. I08 has no rating rows.

**Q48.** 113 instruments have a rating in force.

**Q49.** E5001.

**Q50.** 6 levels (ancestors.csv).

**Q51.** 58, E5001 to E5058.

**Q52.** 19, E5086 to E5104.

**Q53.** No. Their ultimate parents are E5059 and E5086.

**Q54.** E5106, E5124 and E5130.

**Q55.** 31 rated entities have a VD entity above them in their chain: 6 in Cerid, 2 in Rotam, 9 in Wonod and 14 in Geren (E5145 is VD).

**Q56.** BB-, held by E5144.

**Q57.** E5002, the nearest shared ancestor of E5011 and E5013.

**Q58.** E5145. It guarantees I5007, which was issued by E5133 in the Vesol group.

**Q59.** 12, from E5011 to E5022.

**Q60.** E5145, and no. The issuer E5133 is in the Vesol group, E5145 is the top of Geren, and I5007 is rated BBB.

**Q61.** 19 Cerid members have a foreign-currency issuer rating below investment grade.

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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},
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