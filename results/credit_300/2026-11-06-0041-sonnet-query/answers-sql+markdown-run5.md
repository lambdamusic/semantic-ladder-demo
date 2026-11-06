**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).

**Q2.** No. E01 has only an affirmation on 2026-02-10 (A03, outlook moved to Negative), and an outlook change is not a downgrade.

**Q3.** No, BB+. The 2031 note I02 is subordinated and was cut to BB+ on 2025-06-20 (A07).

**Q4.** Positive (POS). E02 and E03 share an LEI, so they are one entity, and the latest action is A09 on E03 (2025-09-15, POS).

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so it is rated on the guarantor (A08/A09, and A11 on I03).

**Q6.** The Country Ceiling for VD is BB (A12) and caps foreign-currency ratings. E05's FC rating is BB (A14), while its local-currency rating is BBB- (A13) and is not capped.

**Q7.** 31 issuers had an LTIDR downgrade in 2026 (listed in the JSON, including E08 and E10). Records sharing an LEI are counted once.

**Q8.** E08 (Saxby Shipping) was in default. A22 downgraded it to RD on 2026-07-08.

**Q9.** 278 distinct issuers held a non-withdrawn LTIDR on 2026-10-01, with records matched by LEI and QA records excluded.

**Q10.** Depends. E05 is BB on foreign currency (A14, speculative grade) and BBB- on local currency (A13, investment grade).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30. The 2025-11-20 Watch (A35) came later.

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. Halden Bank (E10) was downgraded to BBB+ only on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). The Watch and its affirmation did not change it.

**Q17.** No. E06 only had a Watch Negative placed on 2026-09-03 (A17).

**Q18.** 32 issuers were on Rating Watch Negative on 2026-10-01 (listed in the JSON, including E06).

**Q19.** 30 issuers had a Negative outlook on 2026-10-01 (listed in the JSON, including E01 and E09).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** 35 entities (listed in the JSON, including E07) had an LTIDR at some point but had it withdrawn by 2026-10-01.

**Q22.** Only E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66 instruments were rated investment grade on 2026-10-01. This counts each instrument's latest non-Expected rating, excluding QA issuers.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), which is not a rating.

**Q30.** Eight entities were exactly at their country's ceiling (BB for VD, A for CV): E05, E1028, E1101, E1126, E1236, E1039, E15 and E1194. E1279 is excluded because its rating was withdrawn.

**Q31.** No. Every VD entity's FC rating is at or below BB, and every CV entity's is at or below A.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the credit risk of Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A29 and A27 both show BBB+.

**Q34.** No. Halden Foods (E12) has no parent and no link to E09.

**Q35.** 3 entities: E09, E10 and E11. E17 is the same entity as E10, since they share an LEI.

**Q36.** 2 entities: E02 and E04. E03 is the same entity as E02.

**Q37.** 331 distinct legal entities, matched by LEI with QA records excluded.

**Q38.** No. They have different LEIs and are separate entities.

**Q39.** A, from A08 and A09.

**Q40.** 66 distinct GB-domiciled issuers, with RESEARCH records deciding the country.

**Q41.** None. E16 is a QA record, so it and its ratings are ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.

**Q43.** 1 entity, Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB- (A45), but the ceiling does not apply to local-currency debt.

**Q46.** No. E11 only has a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an Expected rating (A47), so it is unrated.

**Q48.** 106 instruments held a rating on 2026-10-01.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1159","E1057","E1243","E1053","E1144","E1080","E1064","E1093","E1151","E1294","E1051","E08","E1112","E1169","E1186","E1058","E1167","E1307","E1228","E1263","E1298","E1255","E1229","E1034","E1163","E1213","E1300","E1285","E1290","E10","E1160"]},
"Q8":{"entities":["E08"]},"Q9":{"count":278},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1059","E1266","E1039","E1098","E1126","E1133","E06","E1181","E1013","E1297","E1238","E1061","E1146","E1203","E1066","E1314","E1323","E1168","E1109","E1099","E1132","E1260","E1019","E1006","E1264","E1194","E1088","E1267","E1317","E1242","E1037","E1209"]},
"Q19":{"issuers":["E1055","E1294","E1059","E1056","E1282","E1190","E1072","E1132","E1046","E1034","E1188","E1248","E1211","E09","E1029","E1160","E1080","E1005","E1079","E1271","E1300","E1158","E1105","E1064","E1261","E01","E1118","E1146","E1263","E1228"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1032","E1159","E1057","E1155","E1253","E1007","E1308","E1206","E1320","E1219","E1048","E1084","E1076","E1021","E07","E1166","E1138","E1041","E1063","E1107","E1140","E1205","E1121","E1225","E1233","E1234","E1200","E1277","E1218","E1062","E1001","E1172","E1124","E1316","E1244"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E1039","E15","E1194"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":331},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":66},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```