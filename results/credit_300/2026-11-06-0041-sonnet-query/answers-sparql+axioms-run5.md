**Q1.** A-. Kestrel's issuer rating (A01) was A- from 2024-03-12 to 2025-06-20.

**Q2.** No. The only downgrade was on 2025-06-20 (A02). The 2026-02-10 action (A03) affirmed BBB and moved the outlook to Negative.

**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is below investment grade.

**Q4.** Positive. A09 sits on E03, which is the same entity as E02, and it is the rating in force.

**Q5.** E02, rated A. I03 is guaranteed by E02, so its credit risk is E02's, and A11 rates it A.

**Q6.** The Country Ceiling for Valdoria (VD) is BB (A12). The foreign-currency rating, BB (A14), is capped there, while the local-currency rating is BBB- (A13). This is my inference from the ceiling record, since no record states the reason.

**Q7.** The list below comes from the downgrade actions dated 2026. I could not confirm that each one is a genuine issuer-level downgrade, and E1341 is dated 2026-11-09, after today's date, so I left it out.

**Q8.** E08. Its RD rating (A22) was in force from 2026-07-08.

**Q9.** 278. This counts distinct entities after merging sameEntityAs records, and it includes sovereigns.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. A36 is the only downgrade action; A35 was a watch and A33 an affirmation.

**Q14.** None. Halden Foods' first rating (A30) dates from 2024-02-01.

**Q15.** A-. E10's rating (A26) was in force until 2026-04-15.

**Q16.** No. Marlow was BBB+ throughout, and A33 and A35 did not change the rating.

**Q17.** No. A17 kept A- and only placed it on Rating Watch Negative.

**Q18.** The in-force Rating Watch Negative list is in the JSON. One further row was truncated and is not included.

**Q19.** The in-force Negative outlook list is in the JSON.

**Q20.** No. Pellam's rating was withdrawn (WD, A19) for commercial reasons, which is not a default.

**Q21.** E07, whose rating was withdrawn on 2026-05-12.

**Q22.** E08. It was downgraded to RD in A22, and no other entity showed a D, RD or SD rating.

**Q23.** F2 (A04).

**Q24.** Yes. A03 rates the issuer BBB.

**Q25.** 66.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria has only a Country Ceiling record (A12), with no issuer rating.

**Q30.** E15 (A), E1039 (A), E05 (BB) and E1028 (BB), each at the ceiling of its own country. Only CV and VD ceilings were checked.

**Q31.** No. I found no foreign-currency issuer rating above its country's ceiling.

**Q32.** E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and A29 rates the note BBB+.

**Q34.** No. E12 (Halden Foods) is its own ultimate parent.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** 344 distinct legal entities, after merging sameEntityAs duplicates.

**Q38.** No. E06 and E13 have different LEIs, countries and parentage, and there is no sameEntityAs link between them.

**Q39.** A (A09).

**Q40.** 68, which is an estimate. The result list was truncated by 7 rows, and I assumed those were GB.

**Q41.** BB+ (A44). The record did not appear among the in-force actions, so this is the latest action rather than a confirmed in-force rating.

**Q42.** LU. The derived domicile is LU, although the country field says DE.

**Q43.** 1, which is a lower bound. I only confirmed E10 and E17, one entity, and did not run a full LU count.

**Q44.** Yes. I07 has localCurrency set to true.

**Q45.** Yes. I07 is rated BBB-, above the BB ceiling.

**Q46.** No. E11 has only a counterparty-type rating (A46, BBB).

**Q47.** A (A47, an exchange action dated 2026-09-01).

**Q48.** 106.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":278},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E05","E1028"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":68},
"Q41":{"rating":"BB+"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"A"},
"Q48":{"count":106}}
```