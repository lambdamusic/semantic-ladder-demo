**Q1.** A-. Kestrel Energy's issuer rating (E01, A01) was A- from 2024-03-12 to 2025-06-20.

**Q2.** No. The only downgrade was on 2025-06-20 (A02). The 2026-02-10 action (A03) affirmed BBB and moved the outlook to Negative.

**Q3.** No, BB+. The 2031 note (I02) was cut to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 are the same entity (same LEI). A09 (Positive outlook, A) took over from A08 on 2025-09-15.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02 and its credit risk is E02; both the note (A10/A11) and E02 are rated A.

**Q6.** Valdoria's foreign-currency rating is BB (A14) against BBB- local-currency (A13). The Country Ceiling for VD is BB (A12), which caps foreign-currency ratings but not local-currency ones.

**Q7.** Entities with a long-term downgrade dated in 2026, up to the 1 Oct 2026 reference date (list in the JSON). I used the recorded action type, so a few oddly dated or repeated records (e.g. E1051, E1229) are taken at face value.

**Q8.** E08 (Saxby Shipping). It was rated RD on 2026-07-08 (A22). Pellam's rating was withdrawn, which is not a default.

**Q9.** 278. This counts distinct entities with an issuer rating in force, merging records that share an LEI.

**Q10.** Depends. Valdoria Telecom (E05) is BBB- in local currency, which is investment grade, and BB in foreign currency, which is not.

**Q11.** BBB+. A36 was in force from 2024-09-30 to 2025-11-20.

**Q12.** A-. A34 was in force from 2023-01-15 to 2024-09-30.

**Q13.** 1. The only downgrade is A36, from A- to BBB+.

**Q14.** None. Halden Foods' first rating is dated 2024-02-01.

**Q15.** A-. A26 was in force until 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now. The Rating Watch Negative in between (A35) was resolved by an affirmation (A33).

**Q17.** No. Orrin Bank (E06) was only placed on Rating Watch Negative on 2026-09-03 (A17), still at A-.

**Q18.** The entities carrying a Negative watch in force on 1 Oct 2026 (list in the JSON).

**Q19.** The entities with a Negative outlook in force. One row of that result was truncated, so the list may be missing one entity.

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19, WD), not for default.

**Q21.** Entities whose latest rating is a withdrawal (WD), so none in force on 1 Oct 2026. I omitted E02, which is covered by its duplicate E03. I also omitted several entities with no in-force record but with actions dated in late 2026 or later.

**Q22.** Only E08, rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66 instruments held an investment-grade rating on 1 Oct 2026.

**Q26.** A+ (A40).

**Q27.** A-. This is the instrument rating for I06 (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria has only a Country Ceiling of BB (A12) and no issuer rating.

**Q30.** The entities whose foreign-currency rating equals the ceiling: CV's ceiling is A (A37) and VD's is BB (A12). I took the matches from foreign-currency ratings in force.

**Q31.** No. None of the foreign-currency ratings in CV or VD exceeds its ceiling.

**Q32.** E09 (Halden Group plc).

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded on 2026-04-15 (A27).

**Q34.** No. E12 is its own ultimate parent, separate from E09's group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 344. This counts distinct entities after merging records that share an LEI.

**Q38.** No. E06 and E13 have no sameEntityAs link and different LEIs or countries.

**Q39.** A, per A09 on E03 (the same entity as E02).

**Q40.** 66.

**Q41.** BB+, per A44 on 2026-06-01. This record did not appear in the "in force" class, so it is worth checking.

**Q42.** LU.

**Q43.** 1.

**Q44.** Yes. I07's localCurrency flag is true.

**Q45.** No. The note is local-currency (BBB-), and the ceiling (BB) applies only to foreign-currency ratings.

**Q46.** No. E11 only has a counterparty obligation rating (A46, BBB), not a long-term issuer rating.

**Q47.** A. I08 was rated A on 2026-09-01 (A47, action EX).

**Q48.** 106.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1299","E1307","E1213","E1080","E1285","E1112","E1263","E1064","E1347","E1344","E1348","E1163","E1053","E1051","E1300","E10","E1034","E1229","E16","E1144","E1159","E1057","E1340","E1228","E1294","E1058","E1342","E1093","E1161","E1343","E1170","E1290","E1350","E1167","E1345","E1351"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"BB+"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"A"},
"Q48":{"count":106}
}
```