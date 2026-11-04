**Q1.** A-. Assigned A- on 2024-03-12 (A01) and downgraded to BBB only on 2025-06-20 (A02), so A- held on 1 Jan 2025.

**Q2.** No. 2026 for Kestrel Energy (E01) is only an affirmation, A03 on 2026-02-10, with the outlook moving to Negative.

**Q3.** No. I02 is subordinated and was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 on 2025-09-15, is an affirmation at A with a POS outlook.

**Q5.** The credit risk of Northwind Holdings (E02), at A. I03 is guaranteed by E02, and I03 is rated A (A10, affirmed by A11).

**Q6.** Valdoria Telecom (E05) is rated BB on FC (A14) and BBB- on LC (A13). The Valdoria Country Ceiling is BB (A12) and caps FC ratings only. The data does not state this as the reason, so it is an inference.

**Q7.** 38 issuers, listed in the JSON. These are the non-QA entities with a DG on an LTIDR in 2026.

**Q8.** Saxby Shipping (E08), which went to RD on 2026-07-08 (A22).

**Q9.** 377 distinct issuers, counting entities with a non-withdrawn LTIDR on 1 Oct 2026 and merging duplicate records by LEI. This includes the sovereign CV, which holds an LTIDR.

**Q10.** Depends. Its FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+ (DG on 2024-09-30).

**Q12.** A- (assigned 2023-01-15).

**Q13.** 1 (A-/BBB+ on 2024-09-30). The 2025-11-20 Watch was not a downgrade.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01.

**Q15.** A-. Halden Bank is E10, and E17 is the same entity by LEI. E10's DG to BBB+ came on 2026-04-15, after 1 Jan 2026.

**Q16.** No. It was BBB+ on 1 Jan 2025 and is BBB+ now.

**Q17.** No. Orrin Bank (E06) only has an RW action, A17 on 2026-09-03, with the rating unchanged at A-.

**Q18.** 32 issuers, listed in the JSON. These are entities whose latest LTIDR action on or before 1 Oct 2026 carries RWN.

**Q19.** 47 issuers, listed in the JSON. These are entities whose latest LTIDR action has a NEG outlook and no Watch.

**Q20.** No. Pellam Retail (E07) was rated BB and then withdrawn on 2026-05-12 (A19), and a withdrawal is not a default.

**Q21.** 36 entities, listed in the JSON. Each had an LTIDR and has a withdrawal as its latest action. I left out E1106 because its FC rating is still active.

**Q22.** Only Saxby Shipping (E08), at RD.

**Q23.** F2 (A04).

**Q24.** Yes, BBB.

**Q25.** 72 instruments, counting the latest non-EX action on or before 1 Oct 2026 and excluding withdrawn ones.

**Q26.** A+ (LC, from E15).

**Q27.** A- (I06).

**Q28.** BBB+.

**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling record, A12, and no issuer rating.

**Q30.** 13 company entities. CV ceiling is A and VD ceiling is BB, and each of these has an FC rating exactly equal to its ceiling.

**Q31.** No. None exceeds its ceiling.

**Q32.** E09 (Halden Group plc). The chain is E11, then E10, then E09.

**Q33.** The credit risk of Halden Bank (E10), at BBB+. I05 is guaranteed by E10, and A29 puts I05 at BBB+.

**Q34.** No. Halden Foods (E12) has no parent and is not in the E09 group.

**Q35.** 3.

**Q36.** 2.

**Q37.** 497. That is 495 distinct LEIs among non-QA records plus the two sovereigns, who have no LEI.

**Q38.** No. They have different LEIs.

**Q39.** A.

**Q40.** 79.

**Q41.** None. Brindle Capital (E16) is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 overrides the RATINGS record's DE.

**Q43.** 1 (Halden Bank).

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. The note is local-currency, so the ceiling does not cap it. It is rated BBB- (A45) against a BB ceiling, but the ceiling does not apply.

**Q46.** No. Halden Leasing (E11) has only a Credit opinion, which is not a rating.

**Q47.** None. I08 has only an EX (expected) action, so it is unrated.

**Q48.** 113 instruments (72 investment grade plus 41 speculative grade).

**Q49.** E5001 (Cerid Group plc). The chain is E5047, E5035, E5023, E5011, E5167, then E5001, because E5167 shares its LEI with E5002, whose parent is E5001.

**Q50.** 5.

**Q51.** 58 distinct LEIs, after excluding the QA record E5170.

**Q52.** 19.

**Q53.** No. The RATINGS parent link, which governs, puts Belir Mining under Belir Group (E5059) via E5060.

**Q54.** E5106, E5124, E5130. E5106 is VD per the RESEARCH record.

**Q55.** 31.

**Q56.** BB-, held by E5144.

**Q57.** E5002. Guven's parent E5167 is the same entity as E5002, and Telecom's chain goes through E5006 to E5002.

**Q58.** E5145 (Geren). It guarantees I5007, which is issued by E5133 in the Vesol group.

**Q59.** 12.

**Q60.** The credit risk of E5145, which is not in the same group as the issuer E5133.

**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1299","E1307","E1213","E1080","E5156","E1285","E1112","E1263","E1064","E1163","E5019","E1053","E1051","E1300","E10","E1034","E1229","E5116","E5059","E1144","E1159","E5113","E1057","E1228","E1294","E1058","E1093","E1161","E1170","E1290","E5097","E1167","E5033"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E1059"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E1028","E1101","E1126","E1236","E05","E5012","E5047","E5091","E5124"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":497},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":79},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":5},
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