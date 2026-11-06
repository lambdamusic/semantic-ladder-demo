**Q1.** A-. Kestrel (E01) was rated A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. In 2026 Kestrel's only actions were affirmations (A03, A04, 2026-02-10), one with the outlook moved to Negative.

**Q3.** No, BB+. The 2031 note (I02) was downgraded to BB+ by A07.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity, and the latest action is A09 (2025-09-15) with a Positive outlook.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 and guaranteed by E02, and I03 itself is rated A (A11).

**Q6.** Valdoria's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The data gives no stated reason; the likely cause is the Valdoria country ceiling, which looks like BB (A12), but A12's rating type and basis are not shown.

**Q7.** These are the issuers with a downgrade action on a long-term issuer rating in 2026 (list in the JSON). It includes E08, E10 and E16.

**Q8.** E08. Its latest rating is RD (A22, 2026-07-08).

**Q9.** 291, counting entities that share a LEI once. Some other entities may also be duplicates, so this is approximate.

**Q10.** Depends. Foreign currency is BB (A14), below investment grade; local currency is BBB- (A13), which is investment grade.

**Q11.** BBB+ (A36, 2024-09-30).

**Q12.** A- (A34, 2023-01-15).

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. Halden Foods' first rating is dated 2024-02-01 (A30).

**Q15.** A-. E10 held A- (A26) until the downgrade on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33, 2026-05-01); a Rating Watch Negative in between (A35) was resolved by affirmation.

**Q17.** No. E06 was only placed on Rating Watch Negative (A17), with the rating held at A-.

**Q18.** The issuers whose latest action carries Rating Watch Negative (list in the JSON). It includes E06.

**Q19.** The issuers whose latest rating action carries a Negative outlook (list in the JSON). It includes E01 and E09.

**Q20.** No. Pellam's rating was withdrawn (A19, WD), which is not a default.

**Q21.** These 37 entities have a withdrawn long-term issuer rating as their latest, and E08 is not among them (it is in default, not withdrawn). The list includes E07.

**Q22.** E08, the only entity ever rated RD/D/SD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 106. The query returned 106 both for rated instruments and for investment-grade ones, which looks inconsistent: I02 (BB+) and I04 (BB) are not investment grade. Treat this figure as unreliable.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** BB (A12 on VD). The data does not show whether that is a foreign-currency or local-currency rating.

**Q30.** E15 and E05. I read A12 (BB) as Valdoria's ceiling, which matches E05's FC BB. Corvenia's ceiling is A (A37), which matches E15's FC A (A41).

**Q31.** No. I found no foreign-currency rating above its country's ceiling.

**Q32.** E09. Halden Leasing (E11) has parent E10, whose parent is E09.

**Q33.** The guarantor, E10, rated BBB+. I05 is issued by E11 and guaranteed by E10.

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 shares E10's LEI, so I counted it as the same entity.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 344. There are 370 entity records and 26 LEIs shared by two records each.

**Q38.** No. They have different countries, different LEIs and different types (E06 is a bank in DE; E13 is a bank holding company in the US).

**Q39.** A, assuming the latest action is the E03 affirmation (A09, 2025-09-15).

**Q40.** 308, but this is low confidence. The same query returned a lower total of 291, so it is internally inconsistent.

**Q41.** BB+ (A44).

**Q42.** DE (E10). E17 has the same LEI and says LU, so the data conflicts on this.

**Q43.** 1. Only E17 is in LU, and it duplicates E10.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's currency.

**Q45.** No. The note's BBB- is a local-currency rating, and the ceiling (BB) constrains foreign-currency ratings.

**Q46.** No. E11 has only a support-based "CO" rating (A46), not an issuer rating.

**Q47.** None. I08's rating A was expired by action EX on 2026-09-01 (A47).

**Q48.** 106 (see the caveat in Q25).

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":291},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":106},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"BB"},"Q30":{"entities":["E15","E05"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":344},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":308},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```