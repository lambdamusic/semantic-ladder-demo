**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01), and the downgrade to BBB came later, on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 was an affirmation at BBB with a Negative outlook (A03, 2026-02-10).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15), which affirmed A with a Positive outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 was issued by E04 and guaranteed by E02, and its rating of A (A11) matches E02's.

**Q6.** The data gives no explicit reason. The Valdoria country ceiling is BB (A12), and Valdoria Telecom's foreign-currency rating is BB (A14), against BBB- in local currency (A13). That fits the ceiling capping the foreign-currency rating.

**Q7.** I found 44 issuers with a downgrade of a long-term issuer rating dated in 2026 (listed in the JSON). I did not check whether any of these IDs are duplicate records of one entity.

**Q8.** Saxby Shipping (E08). It was rated RD on 2026-07-08 (A22).

**Q9.** 290. This is the count of distinct LEIs whose latest long-term issuer rating on 2026-10-01 is not WD.

**Q10.** Depends. Local currency is BBB- (investment grade) and foreign currency is BB (not).

**Q11.** BBB+. A36 downgraded Marlow Utilities (E14) from A- to BBB+ on 2024-09-30.

**Q12.** A- (A34).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. Halden Foods' (E12) first rating is dated 2024-02-01 (A30).

**Q15.** A-. Halden Bank (E10) was rated A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+, with only a watch and an affirmation in between (A35, A33).

**Q17.** No. Orrin Bank (E06) only went on Rating Watch Negative (A17).

**Q18.** 32 issuers (IDs in the JSON).

**Q19.** 37 issuers (IDs in the JSON).

**Q20.** No. Pellam Retail's (E07) rating was withdrawn (A19), which is not a default.

**Q21.** 35 entities (IDs in the JSON). These are entities with a rating history whose last long-term issuer rating on 2026-10-01 is a withdrawal or nothing, shown by LEI.

**Q22.** Only E08 (A22, RD).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB.

**Q25.** 66 instruments, counting those whose latest rating on 2026-10-01 is BBB- or better.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has only a Country Ceiling of BB (A12) and no issuer rating.

**Q30.** 8 entities (IDs in the JSON). The ceilings are A for Corvenia and BB for Valdoria, and these entities are rated exactly at them.

**Q31.** No. No Corvenia (CV) or Valdoria (VD) company's foreign-currency issuer rating exceeds its ceiling.

**Q32.** Halden Group (E09). E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 was guaranteed by E10 (A29 rates the note BBB+, and E10's current rating is also BBB+).

**Q34.** No. E12 has no parent link to the Halden group in the data.

**Q35.** 3 (E09, E10, E11). E17 is a duplicate of E10 by LEI.

**Q36.** 2 (E02, E04). E03 duplicates E02.

**Q37.** 344. There are 342 distinct LEIs, plus the two sovereigns (CV, VD), which have no LEI.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A08 and A09).

**Q40.** 74.

**Q41.** BB+ (A44). Brindle Capital (E16) was downgraded on 2026-06-01.

**Q42.** DE. The LU record E17 is a duplicate of E10 by LEI.

**Q43.** 1, counting distinct LEIs.

**Q44.** Yes. Its currency is XVD, which appears to be Valdoria's local currency, though the data never defines it.

**Q45.** Yes. The note is rated BBB- (A45), above the BB ceiling.

**Q46.** No. E11 has only a CO-type rating (A46), not an issuer rating.

**Q47.** None. The only action on I08 is EX (A47, 2026-09-01), which looks like an exit, so there is no current rating. The data does not define EX.

**Q48.** 106. This is the count of instruments with a latest rating on 2026-10-01 that is neither WD nor an EX action.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":290},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E1039","E1194","E15","E05","E1028","E1101","E1126","E1236"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":344},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":74},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```