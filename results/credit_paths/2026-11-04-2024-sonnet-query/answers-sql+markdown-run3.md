**Q1.** A-. The 2024-03-12 assignment (A01) stood until the downgrade on 2025-06-20 (A02).
**Q2.** No. The only 2026 action is an affirmation with a Negative outlook (A03), which is not a downgrade.
**Q3.** No, BB+. The 2031 note I02 is subordinated and was downgraded to BB+ (A07).
**Q4.** POS. E03 shares E02's LEI, so they are one entity, and E03's latest action (A09, 2025-09-15) set the outlook to Positive.
**Q5.** A holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, and its rating (A11) matches E02's A.
**Q6.** The data does not state a reason. It only shows E05 at BB (A14) for foreign currency and BBB- (A13) for local currency, and Valdoria's Country Ceiling at BB (A12).
**Q7.** There are 38 issuers downgraded in 2026, listed in the JSON.
**Q8.** E08. It went to RD on 2026-07-08 (A22).
**Q9.** 377 distinct issuers hold an LTIDR or STIDR that was not withdrawn. This merges duplicate records by LEI and excludes QA records.
**Q10.** Depends. E05 is BB on foreign currency (A14, speculative) and BBB- on local currency (A13, investment grade).
**Q11.** BBB+ (A36 stood on that date).
**Q12.** A- (A34).
**Q13.** 1, the downgrade A36.
**Q14.** None. Halden Foods' first rating is dated 2024-02-01 (A30).
**Q15.** A- (A26; the downgrade A27 came on 2026-04-15).
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+.
**Q17.** No. E06 only had a Rating Watch placed (A17).
**Q18.** 32 issuers were on Rating Watch Negative, listed in the JSON.
**Q19.** 47 issuers had a Negative outlook, listed in the JSON.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.
**Q21.** 35 entities, listed in the JSON.
**Q22.** E08 only.
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB.
**Q25.** 72.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD carries only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** 13 entities, listed in the JSON.
**Q31.** No. No foreign-currency issuer rating sits above its country's ceiling.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** A holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, and both E10 (A27) and I05 (A29) are BBB+.
**Q34.** Yes. E17 "HALDEN BANK" shares E10's LEI, so it is the same entity, and E10 is under E09.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 497 distinct entities, counting records by LEI and excluding QA.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A08, plus A09 on E03, the same entity).
**Q40.** 79.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** LU. E17 (RESEARCH) holds for domicile, overriding E10's DE.
**Q43.** 1 (the Halden Bank entity).
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** No. It is local-currency debt, so the ceiling does not cap it.
**Q46.** No. E11 only has a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is unrated.
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6 levels.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. E5062 sits under E5059. The RESEARCH duplicate E5168 pointing to E5086 is overridden by RATINGS, which holds for parent links.
**Q54.** E5106, E5124 and E5130.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002. E5011 → E5167 (the same entity as E5005) → E5002, and E5013 → E5006 → E5002.
**Q58.** E5145, which guarantees I5007 issued by E5133 in the Vesol group.
**Q59.** 12.
**Q60.** A holder takes the credit risk of E5145, which is not in the same group as the issuer E5133.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E5097","E1213","E1294","E1051","E5156","E1064","E1186","E1169","E5059","E5033","E1080","E1160","E1144","E5019","E1163","E1263","E1228","E08","E1298","E1290","E1285","E1057","E1300","E1151","E1058","E1112","E1307","E1229","E10","E5116","E1053","E1159","E1093","E1243","E1167","E1034","E5113","E1255"]},"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1297","E1264","E1266","E1132","E1181","E1323","E1317","E1066","E1314","E1013","E1061","E1126","E1133","E06","E1039","E1088","E1098","E1146","E1099","E1260","E1019","E1037","E1203","E1267","E1059","E1109","E1168","E1194","E1209","E1242","E1238"]},"Q19":{"issuers":["E1228","E1282","E1300","E5099","E1263","E1055","E1079","E1158","E1261","E5013","E5156","E01","E1211","E5023","E5102","E1005","E1271","E5097","E1029","E1188","E1294","E5062","E1064","E5057","E5073","E1034","E1118","E1190","E5039","E5113","E5119","E1056","E1072","E1080","E09","E1046","E1059","E5019","E5059","E5141","E1105","E1160","E5116","E1248","E5020","E5050","E5131"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1048","E1084","E1316","E1244","E1121","E1205","E1277","E1218","E1225","E1200","E1234","E1233","E07","E1021","E1166","E1062","E1172","E1124","E1001","E1253","E1155","E1032","E1007","E1308","E1057","E1159","E1076","E1219","E1206","E1320","E1140","E1041","E1107","E1063","E1138"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E1028","E5091","E1039","E5124","E5012","E5047","E1101","E1126","E1194","E15","E05","E1236","E5116"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"yes"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":497},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5124","E5130"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```