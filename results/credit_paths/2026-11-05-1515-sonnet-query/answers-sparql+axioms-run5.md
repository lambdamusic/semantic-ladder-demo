**Q1.** A-. Kestrel's long-term foreign-currency rating was A- on 1 Jan 2025 (A01, in force 2024-03-12 to 2025-06-20).
**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03).
**Q3.** No. The 2031 note I02 is rated BB+ (A07).
**Q4.** Positive. E02 and E03 are the same entity, and A09 is in force with a Positive outlook.
**Q5.** E02, the guarantor, rated A (A11 on I03).
**Q6.** Valdoria Telecom's foreign-currency rating is BB (A14), capped at the Country Ceiling of BB (A12). Its local-currency rating is BBB- (A13).
**Q7.** E08, E10 and E16 (A21/A22, A27, A44). The E1xxx/E5xxx records could not be checked, so this list may be incomplete.
**Q8.** E08, rated RD in A22.
**Q9.** 376 distinct LEIs hold an in-force long-term issuer rating, counting LEIs so that duplicate records of one entity count once.
**Q10.** Depends. Valdoria Telecom is BBB- in local currency (A13, investment grade) and BB in foreign currency (A14, not).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** Once (A36). A35 is a watch action, not a downgrade.
**Q14.** None. Halden Foods' first rating, A30, dates from 2024-02-01.
**Q15.** A- (A26).
**Q16.** No. It was BBB+ on 1 Jan 2025 and is still BBB+ (A33).
**Q17.** No. A17 is a Rating Watch Negative action, and the rating stayed A-.
**Q18.** The list is in the JSON. The query output was noisy, so treat it as best effort.
**Q19.** The list is in the JSON. The query output was noisy, so treat it as best effort.
**Q20.** No. Pellam Retail (E07) has a withdrawal (A19), not a default.
**Q21.** The list is in the JSON. It includes E07 and E16, but E16 is uncertain.
**Q22.** E08 is the only entity ever rated RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 72 instruments held an investment-grade rating.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. Only a Country Ceiling (A12) is recorded for Valdoria.
**Q30.** The list is in the JSON; it includes E05 and E15.
**Q31.** No. My ceiling query found no foreign-currency rating above its ceiling.
**Q32.** E09.
**Q33.** E10, the guarantor, rated BBB+ (A29 on I05).
**Q34.** No. E12 is its own ultimate parent.
**Q35.** 3 (E09, E10 and E11, where E17 is the same entity as E10).
**Q36.** 2 (E02 and E04, where E03 is the same entity as E02).
**Q37.** 509 distinct LEIs across 538 records. The sovereign records (e.g. VD, CV) have no LEI and are not counted.
**Q38.** No. E06 and E13 have different LEIs and no sameEntityAs link.
**Q39.** A (A09).
**Q40.** 79.
**Q41.** BB+ (A44). Its in-force status is uncertain.
**Q42.** LU.
**Q43.** 1. Records E10 and E17 share one LEI.
**Q44.** Yes (I07 has localCurrency true).
**Q45.** No. I07 is a local-currency note, and the ceiling applies to foreign-currency ratings.
**Q46.** No. E11 only has a CO-type rating (A46), which is not in force.
**Q47.** None. A47 is an EX action and is not in force.
**Q48.** 113 instruments held an in-force rating.
**Q49.** E5001.
**Q50.** 6 levels.
**Q51.** 59, uncertain.
**Q52.** 19, from the ultimateParent count.
**Q53.** No. E5062's ultimate parent is E5059, while E5086 is its own.
**Q54.** E5106, E5124, E5130 and E5169. E5169 appears to be a duplicate record of E5106.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002.
**Q58.** E1021 and E5145 (I1098 and I5007), plus E02 for I03.
**Q59.** 11, uncertain.
**Q60.** E5145, and no. The issuer E5133 has ultimate parent E5132, while the guarantor E5145 is its own ultimate parent.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":376},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5033","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E07","E16","E5170"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1028","E1039","E1101","E1126","E05","E1194","E1236","E15","E5012","E5047","E5091","E5116","E5124"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":509},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":59},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5124","E5130","E5169"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E02","E1021","E5145"]},"Q59":{"count":11},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```