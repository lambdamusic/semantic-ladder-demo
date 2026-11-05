**Q1.** A-. E01's LTIDR was A- (A01) until the downgrade to BBB on 2025-06-20 (A02), so A- applied on 1 Jan 2025.
**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), with BBB and a negative outlook.
**Q3.** No, BB+. I02 is subordinated and was cut from BBB to BB+ on 2025-06-20 (A07).
**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI). Its latest action is A09 (2025-09-15), an affirmation at A with a POS outlook, which is newer than A08 (STA).
**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes the guarantor's risk. E02's A comes from A08, and A09 on its duplicate E03 also shows A.
**Q6.** Not in the JSON. Valdoria's Country Ceiling (VD CC, A12) is BB, which caps the foreign-currency rating (A14: BB) below the local-currency rating (A13: BBB-).
**Q7.** 50 entities, listed in the JSON, after merging duplicate records by LEI. I excluded E5033, whose downgrade is dated 2026-11-06, after today. Other future-dated actions may exist that I did not check.
**Q8.** E08 only. A22 on 2026-07-08 moved it to RD after a distressed debt exchange.
**Q9.** 391. This counts distinct issuers by LEI whose latest LTIDR is not a withdrawal.
**Q10.** Depends. The foreign-currency rating is BB (A14, not investment grade) and the local-currency rating is BBB- (A13, investment grade).
**Q11.** BBB+. A36 downgraded E14 from A- on 2024-09-30.
**Q12.** A- (A34).
**Q13.** 1, from A36.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. The downgrade to BBB+ (A27) came on 2026-04-15, after the date asked.
**Q16.** No. It was BBB+ on 1 Jan 2025 and is still BBB+ (A35 watch, A33 affirmed).
**Q17.** No. E06 only has a Rating Watch Negative placement (A17) and no downgrade.
**Q18.** 30 entities, listed in the JSON.
**Q19.** 57 entities with a Negative outlook, listed in the JSON.
**Q20.** No. E07 had its rating withdrawn for commercial reasons (A19), not a default.
**Q21.** 36 entities, listed in the JSON. Their latest LTIDR action is a withdrawal, and they have no foreign-currency rating in force on 1 Oct 2026.
**Q22.** E08 only (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 72. This counts instruments whose latest INST rating is BBB- or better and has not expired (EX).
**Q26.** A+ (A40).
**Q27.** A- (A42). I06 is the 2032 note.
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.
**Q30.** 13 entities, listed in the JSON. The ceiling is BB for VD and A for CV.
**Q31.** No. No company's foreign-currency rating exceeds its country ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, which A27 downgraded to BBB+ on 2026-04-15.
**Q34.** No. E12 has no parent, while E10 sits under E09.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 511. That is 540 records minus duplicate LEI records (RESEARCH/QA copies).
**Q38.** No. E06 and E13 have different LEIs and countries (DE vs US), and E06 has no parent.
**Q39.** A, with a positive outlook.
**Q40.** 87.
**Q41.** BB+. A44 downgraded E16 from BBB- on 2026-06-01.
**Q42.** DE. E17 (LU) is a RESEARCH duplicate of E10 with the same LEI.
**Q43.** 0. The only LU record, E17, duplicates the German E10, so no distinct entity is domiciled in LU.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency.
**Q45.** No. The BB ceiling caps foreign-currency ratings, and I07 is local-currency, rated BBB- (A45).
**Q46.** No. E11 only has a CO rating (A46).
**Q47.** None. I08's rating expired (EX, A47, 2026-09-01).
**Q48.** 113. This counts instruments whose latest INST action is not an expiry.
**Q49.** E5001. E5047's chain runs E5035, E5023, E5011, then E5167, which is a duplicate record of E5005 (same LEI), then E5002 and E5001.
**Q50.** 6 levels (E5035, E5023, E5011, E5005, E5002, E5001).
**Q51.** 58. The recursion returned 59 because it counts the duplicate record E5167 separately.
**Q52.** 20.
**Q53.** No. Belir Mining's top parent is E5059 (Belir Group) and Rotam's is E5086.
**Q54.** E5124 and E5130.
**Q55.** 23.
**Q56.** BB- (E5144).
**Q57.** E5002 (Cerid Energy plc). E5011 reaches it through E5167/E5005, and E5013 through E5006.
**Q58.** E5145, which guarantees I5007 issued by E5133 in the Vesol group.
**Q59.** 12.
**Q60.** E5145 (Geren Group SA), which is not in the same group as the issuer. The issuer E5133 sits under E5132 (Vesol).
**Q61.** 20. This count merges E5167 into E5005.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1058","E1167","E1341","E1064","E1093","E1343","E1151","E1294","E1350","E1344","E1034","E1051","E1347","E1080","E5116","E5156","E1285","E1290","E10","E1160","E5059","E1342","E1351","E1053","E1057","E1144","E1159","E1243","E5019","E5113","E16","E1340","E1346","E1163","E1213","E1300","E5097","E08","E1112","E1169","E1186","E1348","E1228","E1229","E1255","E1263","E1298","E1307","E1345","E1349"]},"Q8":{"entities":["E08"]},"Q9":{"count":391},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1126","E1132","E1168","E1066","E1098","E1266","E1109","E1006","E1133","E1203","E1260","E1317","E1099","E1037","E1209","E1013","E1146","E1181","E1238","E06","E1297","E1039","E1242","E1314","E1264","E1267","E1061","E1323","E1088","E1194"]},"Q19":{"issuers":["E1072","E09","E1079","E1105","E1228","E1059","E1211","E1282","E5057","E1056","E1160","E1343","E1348","E5119","E5170","E5013","E01","E1188","E1190","E1261","E1344","E1347","E5020","E5059","E5102","E5073","E5099","E5156","E1080","E1118","E1158","E1345","E5062","E1350","E1351","E1055","E1263","E1340","E5097","E5113","E5116","E1005","E1300","E5019","E5023","E5039","E1029","E1046","E1064","E1248","E1294","E1342","E5131","E1034","E5141","E1271","E5050"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1225","E1233","E1200","E1234","E1218","E1084","E1048","E1316","E1244","E1121","E1205","E1277","E1062","E1320","E1206","E1219","E1076","E1279","E07","E1166","E1021","E1124","E1172","E1001","E1253","E1032","E1007","E1308","E1159","E1155","E1057","E1138","E1107","E1063","E1041","E1140"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E1101","E1126","E5124","E5047","E5012","E5091","E1236","E1028","E05","E5116","E15","E1194","E1039"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":87},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":20},"Q53":{"same_group":"no"},"Q54":{"entities":["E5124","E5130"]},"Q55":{"count":23},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":20}}
```