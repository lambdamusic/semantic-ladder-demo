**Q1.** A-. E01's rating was A- (A01) until the downgrade to BBB on 2025-06-20 (A02).
**Q2.** No. The only 2026 action for E01 is an affirmation (A03).
**Q3.** No. The 2031 note I02 was cut to BB+ (A07), which is sub-investment grade.
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (POS).
**Q5.** The holder takes the credit risk of E02, the guarantor of I03, which is rated A (A10, A11).
**Q7.** The issuers with a 2026 LTIDR downgrade are listed in the JSON, after merging duplicate records that share an LEI.
**Q8.** E08. A22 puts it at RD on 2026-07-08.
**Q9.** 391 distinct issuers hold a non-withdrawn LTIDR as of 2026-10-01, with duplicate records merged.
**Q10.** Depends. E05 is BB in foreign currency (A14) but BBB- in local currency (A13).
**Q11.** BBB+. E14 was cut to BBB+ on 2024-09-30 (A36), and the 2025-11-20 action (A35) was only a watch.
**Q12.** A- (A34).
**Q13.** 1, for E14 (A36).
**Q14.** None. E12's first rating is dated 2024-02-01 (A30).
**Q15.** A-. E10 was A- (A26) until the downgrade on 2026-04-15 (A27).
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after A33.
**Q17.** No. E06 has only a Rating Watch Negative (A17).
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not for default.
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 72 of the 113 rated instruments are investment grade as of 2026-10-01.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling of BB (A12), no issuer rating.
**Q32.** E09.
**Q33.** The holder takes the credit risk of E10, the guarantor of I05, currently rated BBB+ (A27).
**Q34.** No. E12 has no parent and is not in the Halden group.
**Q35–Q36.** The Halden group has 3 entities and the Northwind group has 2.
**Q37.** 511 distinct legal entities after merging records with the same LEI.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A. E02 is still at A with no later change.
**Q40.** 87.
**Q41.** BB+ (A44).
**Q42.** DE. E10 is the RATINGS record, and E17 is a RESEARCH duplicate showing LU.
**Q43.** 1.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency.
**Q45.** Yes. I07 is rated BBB- (A45), above VD's ceiling of BB (A12).
**Q46.** No. E11 has only a Country Ceiling-style CO rating (A46), no LTIDR.
**Q47.** None. I08's rating was marked EX (expired) on 2026-09-01 (A47).
**Q48.** 113, counting instruments whose latest INST action is not EX or WD.
**Q49.** E5001. The chain runs E5047 → E5035 → E5023 → E5011 → E5167 (a duplicate of E5005) → E5002 → E5001.
**Q50.** 6 levels.
**Q51–Q52.** The Cerid group has 59 entities and the Rotam group has 19.
**Q53.** No. E5062 sits under E5059 and E5086 is its own root.
**Q54.** E5124 and E5130.
**Q55.** 23.
**Q56.** BB-. The lowest current FC issuer rating in the Vesol group is BB- (E5144).
**Q57.** E5002. Both entities sit three levels below E5001, and E5002 is the nearest shared ancestor.
**Q58.** E5145. It guarantees I5007, issued by E5133, which is in the Vesol group.
**Q59.** 12.
**Q60.** The holder takes the credit risk of E5145, the guarantor of I5007, which is not in the same group as the issuer E5133.
**Q61.** 20.

Q6 has no JSON field, so I did not answer it. It would be explained by the E05 ratings above, but the data gives no stated reason.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1290","E1151","E1294","E1350","E08","E1112","E1169","E1186","E1348","E1058","E1167","E1341","E5156","E1053","E1057","E1144","E1159","E1243","E5019","E5113","E1051","E1347","E1163","E1213","E1300","E5097","E1344","E16","E1340","E1346","E1080","E5116","E1228","E1229","E1255","E1263","E1298","E1307","E1345","E1349","E5033","E1034","E10","E1160","E1342","E1351","E5059","E1064","E1093","E1343"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":391},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1109","E1168","E1037","E1209","E1242","E1317","E1099","E1260","E1132","E1019","E1264","E1006","E1194","E1088","E1181","E1238","E1061","E1013","E1297","E1203","E1066","E1314","E1323","E1146","E1267","E1133","E06","E1126","E1098","E1059","E1266","E1039"]},
"Q19":{"issuers":["E1294","E5119","E1055","E5141","E1350","E1118","E1343","E1261","E1064","E01","E1271","E1347","E1188","E1034","E5057","E1248","E1348","E1046","E5062","E1340","E5013","E5023","E1059","E1056","E1282","E5073","E1263","E5050","E1228","E1345","E5099","E5116","E1005","E1080","E1029","E1160","E1342","E5170","E5059","E1351","E5020","E1079","E5113","E1211","E09","E5019","E5131","E1190","E5039","E5156","E1072","E1105","E1158","E1344","E5102","E5097","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1048","E1084","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1277","E1244","E1316","E1062","E1076","E1206","E1219","E1320","E1218","E1001","E1124","E1172","E07","E1021","E1166","E1121","E1205","E1041","E1063","E1107","E1138","E1140","E1200","E1225","E1233","E1234"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1101","E5012","E5047","E5091","E5116","E5124","E15","E1236","E1039","E05","E1028","E1126","E1194"]},
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
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":59},
"Q52":{"count":19},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5124","E5130"]},
"Q55":{"count":23},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":20}
}
```