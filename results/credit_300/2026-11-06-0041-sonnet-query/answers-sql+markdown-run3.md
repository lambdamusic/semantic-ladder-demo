**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).
**Q2.** No. The only 2026 action on E01 is an affirmation with a Negative outlook (A03), and an affirmation or outlook change is not a downgrade.
**Q3.** No. The 2031 note (I02, subordinated) was downgraded to BB+ (A07), which is speculative grade.
**Q4.** Positive. E02 and E03 share one LEI, so they are one entity. The latest action is A09 on E03 (2025-09-15), which carries a POS outlook.
**Q5.** A holder takes the credit risk of E02, Northwind Holdings, the guarantor of I03. The note is rated A (A10 and A11), in line with E02's A.
**Q6.** Valdoria's Country Ceiling is BB (A12) and caps foreign-currency ratings. E05's FC rating is BB (A14), while its LC rating is BBB- (A13) and is not capped.
**Q7.** 31 issuers had a downgrade (DG) action in 2026, listed in the JSON, including E08 and E10. E01 is not among them.
**Q8.** E08 (Saxby Shipping) was in default. It was downgraded to RD on 2026-07-08 (A22), and RD counts as default.
**Q9.** 278. This counts distinct LEIs whose latest LTIDR (either currency basis) on 2026-10-01 is not WD, excluding QA records.
**Q10.** Depends. E05's FC rating is BB (speculative grade) and its LC rating is BBB- (investment grade).
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action is 2025-11-20.
**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34).
**Q13.** 1. The only downgrade of E14 is A36.
**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).
**Q15.** A-. E10 (Halden Bank) was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 is a RESEARCH record of the same LEI.
**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+; the 2025-11-20 Watch and the 2026-05-01 affirmation (A35, A33) did not change it.
**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement (A17), which leaves the rating unchanged.
**Q18.** 32 issuers were on Rating Watch Negative (RWN) on 2026-10-01, listed in the JSON, including E06.
**Q19.** 28 issuers had a Negative outlook, listed in the JSON, including E01 and E09.
**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19) for commercial reasons. A withdrawal is not a default, and its last rating was BB.
**Q21.** 39 records across 37 entities had an issuer rating at some point but none on 2026-10-01, listed in the JSON, including E07. Each of these has a latest LTIDR action of WD. Two of the entities (E1001/E1002 and E1021/E1022) appear under two records each.
**Q22.** E08 is the only entity ever rated RD or D.
**Q23.** F2 (A04).
**Q24.** Yes. E01's FC issuer rating is BBB (A02, affirmed in A03).
**Q25.** 66. This counts non-QA instruments whose latest INST action on or before 2026-10-01 is investment grade. EX actions are ignored.
**Q26.** A+. E15's LC rating is A+ (A40).
**Q27.** A- (A42). I06 is subordinated.
**Q28.** BBB+ (A38).
**Q29.** None. VD (Republic of Valdoria) has only a Country Ceiling (A12, BB), which is not an issuer rating.
**Q30.** 8 entities have an FC rating exactly at their country's ceiling. In CV (ceiling A) they are E15, E1039 and E1194. In VD (ceiling BB) they are E05, E1028, E1101, E1126 and E1236.
**Q31.** No. Every FC-rated entity in CV is at or below A, and every one in VD is at or below BB.
**Q32.** E09. The chain is E11, then E10, then E09.
**Q33.** A holder takes the credit risk of E10, Halden Bank, the guarantor of I05. The note is rated BBB+ (A29).
**Q34.** Yes. E10 has E09 as its parent, and E12 (Halden Foods) is not in that chain.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2. E02 and E03 are one entity, and E04 is its subsidiary.
**Q37.** 331 distinct LEIs among non-QA records. This collapses same-LEI duplicates and excludes QA test records.
**Q38.** No. They have different LEIs (E06 and E13), so they are different entities.
**Q39.** A. E02 was assigned A (A08) and later affirmed at A (A09).
**Q40.** 66. This counts distinct LEIs rated on 2026-10-01 with GB domicile, using the RESEARCH record for country where records disagree.
**Q41.** None. E16 (Brindle Capital) is a QA record, which is test data to be ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, and it says LU, not DE.
**Q43.** 1. Only the Halden Bank LEI (E10/E17) resolves to LU.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where E05 is domiciled.
**Q45.** No. It is local-currency debt, so the ceiling does not cap it; it is rated BBB- (A45) in any case.
**Q46.** No. E11 has only a Credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), so it is unrated until an AS action.
**Q48.** 106. These are non-QA instruments whose latest non-EX INST action on or before 2026-10-01 is not WD.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1151","E1294","E1053","E1144","E1299","E1159","E1243","E1057","E1167","E1058","E1080","E1285","E1290","E1034","E1170","E1051","E1093","E1064","E08","E1186","E1112","E1228","E1229","E1255","E1263","E1307","E10","E1161","E1300","E1163","E1213"]},
"Q8":{"entities":["E08"]},"Q9":{"count":278},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1109","E1181","E1019","E06","E1039","E1203","E1061","E1266","E1264","E1006","E1066","E1059","E1323","E1099","E1132","E1037","E1133","E1146","E1317","E1194","E1013","E1242","E1314","E1098","E1297","E1210","E1168","E1267","E1238","E1088","E1126","E1260"]},
"Q19":{"issuers":["E1118","E1294","E1029","E1080","E01","E1055","E1188","E1105","E1161","E1005","E1262","E1046","E1282","E1271","E1064","E1190","E1034","E1248","E1060","E1228","E1211","E1072","E1263","E09","E1056","E1158","E1079","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1218","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1002","E1277","E1244","E1316","E1048","E1084","E1076","E1254","E07","E1021","E1166","E1139","E1200","E1225","E1233","E1234","E1121","E1205","E1001","E1124","E1172","E1022","E1062","E1206","E1219","E1320","E1041","E1063","E1107","E1138","E1140"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"yes"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":331},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":66},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```