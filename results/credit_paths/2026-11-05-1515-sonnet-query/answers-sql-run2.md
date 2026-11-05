**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).
**Q2.** No. E01's only 2026 action was an affirmation at BBB with a Negative outlook (A03).
**Q3.** No. The 2031 note I02 was downgraded to BB+ on 2025-06-20 (A07), which is sub-investment grade.
**Q4.** Positive. E02 (STA, A08) and E03 (POS, A09, 2025-09-15) share one LEI, so I treated them as one entity and took the latest action.
**Q5.** The guarantor, Northwind Holdings (E02). I03 is issued by E04 and guaranteed by E02, and is rated A (A10/A11).
**Q6.** The data does not say why. It shows only FC BB (A14) against LC BBB- (A13), and the Republic of Valdoria's Country Ceiling is BB (A12).
**Q7.** The issuers with a 2026 issuer-level downgrade are listed in the JSON, excluding the future-dated E5033 and E1341. I05 is an instrument downgrade, so it is not counted.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) and has had no later action.
**Q9.** 390. This is the count of distinct LEIs with a non-withdrawn FC issuer rating on 2026-10-01.
**Q10.** Depends. E05 is BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13).
**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36).
**Q12.** A-, from A34.
**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement.
**Q14.** None. E12's first rating was on 2024-02-01 (A30).
**Q15.** A-. E10's downgrade to BBB+ came on 2026-04-15 (A27).
**Q16.** No. E14 stayed at BBB+ through the watch (A35) and the affirmation (A33).
**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement at A- (A17).
**Q18.** The issuers on Rating Watch Negative are in the JSON.
**Q19.** The issuers with a Negative outlook are in the JSON.
**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19), and it was never rated in default.
**Q21.** The entities whose latest FC action is a withdrawal on or before 2026-10-01 are in the JSON. E1002 is a duplicate of E1001 and E1106 withdrew only its LC rating, so I left both out.
**Q22.** E08 is the only entity with a default-grade rating (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 72. This counts each instrument's latest rating at BBB- or better and excludes the matured (EX) ones.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling of BB (A12) and no issuer rating.
**Q30.** E05 (BB, A14) and E15 (A, A41) sit at their country ceilings (VD BB, CV A). I did not check the other entities domiciled in those countries.
**Q31.** No, based on the entities I checked. I did not check every VD and CV entity.
**Q32.** E09. E11 sits under E10, which sits under E09.
**Q33.** The guarantor, Halden Bank (E10). I05 is guaranteed by E10 and rated BBB+ (A29).
**Q34.** No. E12 has no parent and a different LEI from the Halden Group entities.
**Q35.** 3 (E09, E10, E11). E17 has the same LEI as E10, so it is not counted separately.
**Q36.** 2 (E02, E04). E03 duplicates E02.
**Q37.** 511 distinct LEIs or entities across the 540 rows.
**Q38.** No. They have different LEIs and are different entity records (E06 and E13).
**Q39.** A (A08/A09).
**Q40.** 87. This counts distinct GB-domiciled LEIs with an active FC issuer rating.
**Q41.** BB+ (A44).
**Q42.** DE (E10). The LU record E17 is a RESEARCH duplicate with the same LEI.
**Q43.** 0. The only LU record, E17, duplicates the DE-domiciled Halden Bank.
**Q44.** Yes. I07 is denominated in XVD, the Valdoria currency.
**Q45.** Yes. I07 is rated BBB- (A45), above the Valdoria ceiling of BB (A12).
**Q46.** No. E11 has only a CO record (A46), not an LTIDR.
**Q47.** None. I08's latest record is an expiry (EX, A47), so it no longer holds a rating.
**Q48.** 113 instruments held a non-expired rating on 2026-10-01.
**Q49.** E5001. The chain runs E5047, E5035, E5023, E5011, then E5167, which is a duplicate of E5005, then E5002 and E5001.
**Q50.** 6.
**Q51.** 59.
**Q52.** 19.
**Q53.** No. Belir Mining sits in the Belir Group (E5059) and Rotam Group Inc is its own root.
**Q54.** Not determined; I did not query this.
**Q55.** Not determined; I did not query this.
**Q56.** Not determined; I did not query this.
**Q57.** E5002, Cerid Energy plc. It is the first parent in both chains.
**Q58.** E5145. It guarantees I5007, issued by E5133 in the Vesol group. I did not check the other guaranteed notes.
**Q59.** 12.
**Q60.** Geren Group SA (E5145), the guarantor. It is not in the same group as the issuer E5133, which belongs to Vesol (E5132).
**Q61.** Not determined; I did not query this.

For Q54 to Q56 and Q61, the JSON holds placeholder values (empty list, "none", 0) that are not data-backed. Q55 and Q58 are partial.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16","E1170","E1051","E1080","E1307","E1167","E1345","E1350","E1229","E5156","E5116","E5059","E1340","E1299","E5097","E1161","E1351","E1290","E1263","E1255","E1064","E1053","E1285","E1034","E1163","E1348","E1144","E1344","E1186","E5019","E1058","E1213","E1294","E1159","E1346","E1343","E1057","E1228","E1347","E1300","E1112","E1349","E1093","E1342","E1243","E5113","E1151"]},"Q8":{"entities":["E08"]},"Q9":{"count":390},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1264","E1267","E1013","E1061","E1238","E1297","E06","E1133","E1039","E1266","E1098","E1126","E1066","E1146","E1203","E1314","E1323","E1037","E1242","E1317","E1088","E1194","E1109","E1168","E1099","E1132","E1260","E1181","E1210"]},"Q19":{"issuers":["E1079","E1228","E1263","E1345","E5050","E5073","E5099","E1034","E1188","E1248","E5057","E1105","E1158","E1344","E01","E1064","E1118","E1343","E1271","E1347","E1055","E1294","E1350","E5119","E5141","E1029","E1161","E1342","E1351","E5020","E5059","E5170","E1005","E1080","E5116","E09","E1060","E1211","E1262","E5019","E5113","E5131","E1056","E1282","E1340","E5013","E5023","E5062","E1300","E5097","E5102","E1072","E1190","E5039","E5156","E1046","E1348"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07","E1048","E1166","E1320","E1200","E1041","E1244","E1076","E1124","E1316","E1107","E1121","E1279","E1138","E1063","E1233","E1062","E1225","E1308","E1115","E1084","E1254","E1140","E1021","E1205","E1206","E1277","E1172","E1155","E1303","E1219","E1218","E1007","E1032","E1057","E1234","E1159"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":87},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":59},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":[]},"Q55":{"count":0},"Q56":{"rating":"none"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":0}}
```