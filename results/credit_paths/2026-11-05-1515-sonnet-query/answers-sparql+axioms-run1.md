**Q1.** A-. Kestrel's long-term FC issuer rating A01 held until 2025-06-20.
**Q2.** No. The only 2026 action, A03 (2026-02-10), affirmed BBB with a Negative outlook.
**Q3.** No. The 2031 note (I02) has been rated BB+ since 2025-06-20 (A07).
**Q4.** Positive. A09 on E03 (the same entity as E02) is in force with a Positive outlook.
**Q5.** E02, rated A. I03 is guaranteed by E02, whose in-force rating is A (A09).
**Q6.** The data doesn't state a reason. The FC rating A14 is BB and the LC rating A13 is BBB-, and Valdoria's Country Ceiling A12 is BB, which would cap the FC rating.
**Q7.** 47 entities had an LTIDR downgraded in 2026 (listed in the JSON). I excluded two with actions dated after today (E1341 and E5033) and three where the rating did not change (E1064, E1051's second action, E5116).
**Q8.** E08. A22 (RD, 2026-07-08) is in force.
**Q9.** 377 distinct issuers hold an in-force LTIDR other than WD, merging sameEntityAs duplicates.
**Q10.** Depends. Its FC rating is BB (not investment grade) and its LC rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. Only A36 is a downgrade (2024-09-30).
**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.
**Q15.** A- (A26).
**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now; only the watch and outlook changed.
**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative with A- unchanged.
**Q18.** 32 issuers are on RWN (listed in the JSON).
**Q19.** 48 issuers had a Negative outlook (listed in the JSON).
**Q20.** No. A19 is a withdrawal (WD, "commercial reasons"), not a default.
**Q21.** 51 entities, taken from the query result (listed in the JSON). I couldn't verify why it includes some entities that have 2026 downgrades, so treat it with caution.
**Q22.** E08 only (RD).
**Q23.** F2 (A04).
**Q24.** Yes. BBB (A03).
**Q25.** 72 of the 113 rated instruments.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. Valdoria has only a Country Ceiling (A12, BB), not an issuer rating.
**Q30.** 13 entities (listed in the JSON).
**Q31.** No. No FC rating exceeds its country's ceiling.
**Q32.** E09.
**Q33.** E10, rated BBB+ (A27). E10 guarantees I05.
**Q34.** No. E12 has no parent link to E09.
**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.
**Q36.** 2: E02 and E04. E03 is a duplicate record of E02.
**Q37.** 511 distinct legal entities, after merging sameEntityAs duplicates.
**Q38.** No. E06 and E13 have no sameEntityAs link and different domiciles (DE and US).
**Q39.** A (A09).
**Q40.** 79.
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1. E10 and E17 are the same entity.
**Q44.** Yes. I07 is flagged local currency and is denominated in XVD.
**Q45.** No. The ceiling applies to FC ratings, and I07 is local-currency.
**Q46.** No. E11 has only a counterparty-obligation rating (A46, type CO).
**Q47.** A (A47).
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6. The chain is E5047, E5035, E5023, E5011, E5005 (E5167 is a duplicate record of E5005), E5002, E5001.
**Q51.** 58. The group has 59 records, one of which (E5167) is a duplicate of E5005.
**Q52.** 19.
**Q53.** No. E5062 sits under E5059, while Rotam's top is E5086.
**Q54.** E5106, E5124 and E5130. E5169 is a duplicate of E5106.
**Q55.** 31.
**Q56.** BB-. E5144 is the lowest FC rating in the Vesol group.
**Q57.** E5002.
**Q58.** E5145. It guarantees I5007, issued by E5133 in a different group.
**Q59.** 12 (E5011 to E5022).
**Q60.** E5145, and no. E5145 is its own ultimate parent, while the issuer E5133 sits under E5132.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16","E5019","E5059","E5097","E5113","E5156"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09","E5013","E5019","E5020","E5023","E5033","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E5170","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16","E07","E1032","E1062","E1076","E1124","E1140","E1200","E1316","E1001","E1121","E1138","E1159","E1233","E1048","E1057","E1155","E1172","E1205","E1206","E1218","E1219","E1225","E1253","E1277","E1320","E1041","E1308","E1107","E1007","E1084","E1166","E1234","E1244","E1063","E1021"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1028","E1039","E1101","E1126","E05","E1194","E1236","E15","E5012","E5047","E5091","E5116","E5124"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":511},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":79},
"Q41":{"rating":"BB+"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"A"},
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