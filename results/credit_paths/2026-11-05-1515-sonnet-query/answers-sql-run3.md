**Q1.** A-. Kestrel's rating was A- from A01 (2024-03-12). The downgrade to BBB came later, in A02 (2025-06-20).

**Q2.** No. A03 (2026-02-10) only affirmed BBB and changed the outlook to Negative.

**Q3.** No. Instrument I02 (the 2031 note) is rated BB+ since A07, below investment grade.

**Q4.** Positive. E02 and E03 share an LEI, so I treated them as one entity. The latest action, A09 (2025-09-15), is Positive.

**Q5.** The risk is Northwind Holdings (E02), rated A. Instrument I03 is issued by E04 and guaranteed by E02, and A09/A11 affirm A.

**Q6.** The data doesn't state a reason. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The country ceiling for VD is BB (A12), which is consistent with the gap, but no record says it is the cause.

**Q7.** The list is in the JSON; it counts issuers with a 2026 downgrade (DG) action dated on or before today (2026-11-05). I excluded E1341, whose downgrade is dated 2026-11-09. Inclusion of any other future-dated downgrades hasn't been checked.

**Q8.** E08 (Saxby Shipping). It was downgraded to RD on 2026-07-08 (A22) after a distressed debt exchange.

**Q9.** 391. This counts distinct de-duplicated entities (same LEI) whose latest long-term issuer rating on 1 Oct 2026 was not a withdrawal.

**Q10.** Depends. Valdoria Telecom (E05) is BB in foreign currency (A14, sub-investment grade) and BBB- in local currency (A13, investment grade).

**Q11.** BBB+. E14 was downgraded in A36 (2024-09-30), and the Rating Watch Negative in A35 only came on 2025-11-20.

**Q12.** A-. This is from A34 (2023-01-15).

**Q13.** 1. The only downgrade of E14 is A36.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. A27 (downgrade to BBB+) came only on 2026-04-15.

**Q16.** No. The rating stayed BBB+ (A36 through A33). A35 was a watch and A33 an affirmation.

**Q17.** No. A17 (2026-09-03) only placed E06 on Rating Watch Negative at A-.

**Q18.** The list is in the JSON (32 issuers whose latest issuer rating was a Rating Watch Negative action).

**Q19.** The list is in the JSON; it includes E01 and E09.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and it was never rated in default.

**Q21.** The list is in the JSON (35 entities, including E07). Each had an issuer rating that was later withdrawn.

**Q22.** E08 only. It is the only entity with an RD, D or C rating (A22).

**Q23.** F2, from A04.

**Q24.** Yes. The BBB issuer rating (A03) is investment grade.

**Q25.** 72. This is the number of instruments whose latest rating on 1 Oct 2026 was investment grade and not an expiry (EX).

**Q26.** A+, from A40.

**Q27.** A-, from A42 for I06.

**Q28.** BBB+, from A38.

**Q29.** None. The entity VD has only a Country Ceiling (BB, A12) and no issuer rating.

**Q30.** The list is in the JSON. The ceilings are CV = A (A37) and VD = BB (A12); the list is entities in each country whose foreign-currency rating equals it.

**Q31.** No. No CV entity is above A and no VD entity is above BB.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The risk is Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 (Halden Foods) has no parent, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 511. This is 540 rows with duplicates of the same LEI merged.

**Q38.** No. They have different LEIs and are separate entities, E06 and E13.

**Q39.** A. A09 affirmed A on 2025-09-15, after A08 assigned A.

**Q40.** 87. This counts distinct GB-domiciled de-duplicated issuers with an issuer rating on 1 Oct 2026.

**Q41.** BB+. A44 (2026-06-01) downgraded E16 from BBB-. Note E16's source system is QA.

**Q42.** DE (E10). E17 is a duplicate record with the same LEI that shows LU.

**Q43.** 0. The only LU record, E17, is a duplicate of E10, which is DE.

**Q44.** Yes. I07 is denominated in XVD, the Valdoria currency.

**Q45.** No. The BB ceiling (A12) applies to foreign currency, and I07 is a local-currency obligation rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (CO, A46) and no long-term issuer rating.

**Q47.** None. I08's latest action, A47 (2026-09-01), is an expiry, so it has no current rating.

**Q48.** 113. This is the number of instruments with a live rating on 1 Oct 2026.

**Q49.** E5001. The chain is E5047 to E5035, E5023, E5011, E5005, E5002, then E5001.

**Q50.** 6. E5047 sits at depth 6 below E5001.

**Q51.** 59, counting E5001 and de-duplicating E5167 (the same LEI as E5005).

**Q52.** 20, counting Rotam Group Inc (E5086) and every descendant.

**Q53.** No. E5062 sits under E5059 (Belir Group AG), and E5086 is a separate root.

**Q54.** E5124 and E5130.

**Q55.** 23.

**Q56.** BB-. This is E5144; the other members hold higher ratings (E5133 BBB-, E5141 BB, E5132 BB+).

**Q57.** E5002. It is the nearest common ancestor, two levels above both E5011 and E5013.

**Q58.** E5145. It guarantees I5007, issued by E5133 in the Vesol group.

**Q59.** 12.

**Q60.** The risk is Geren Group SA (E5145). It is not in the same group as the issuer E5133, which is in Vesol.

**Q61.** 20.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1034","E1080","E5116","E1064","E1343","E1093","E1167","E1058","E1344","E10","E5059","E1160","E1351","E1342","E1053","E1144","E5019","E1159","E1057","E1243","E5113","E1051","E1347","E5097","E1163","E1213","E1300","E1290","E1285","E1307","E1345","E1229","E1298","E1263","E1255","E5033","E1228","E1349","E1350","E1294","E1151","E16","E1340","E1346","E08","E1169","E1348","E1186","E1112","E5156"]},"Q8":{"entities":["E08"]},"Q9":{"count":391},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1099","E1260","E1006","E1297","E1132","E1181","E1323","E1266","E1019","E1037","E1203","E1267","E06","E1039","E1088","E1098","E1146","E1066","E1314","E1061","E1126","E1133","E1059","E1109","E1168","E1194","E1209","E1242","E1264","E1238","E1317","E1013"]},"Q19":{"issuers":["E1034","E1118","E1190","E1343","E5039","E5113","E5119","E1105","E1160","E5116","E1228","E1282","E1300","E1345","E1350","E5099","E01","E1055","E1079","E1158","E1261","E1340","E1342","E5013","E5156","E1059","E5019","E5059","E5141","E1056","E1072","E1080","E1347","E1005","E1271","E5097","E5170","E1064","E5057","E5073","E1248","E09","E1046","E1263","E1344","E1348","E1351","E5020","E5050","E5131","E1211","E5023","E5102","E1029","E1188","E1294","E5062"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1062","E1225","E1200","E1234","E1233","E1253","E1155","E1032","E1007","E1308","E1057","E1159","E1121","E1205","E1316","E1244","E1048","E1084","E1277","E1219","E1206","E1320","E1076","E07","E1021","E1166","E1172","E1124","E1001","E1218","E1140","E1041","E1107","E1063","E1138"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E15","E1039","E1194","E5116","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":87},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":59},"Q52":{"count":20},"Q53":{"same_group":"no"},"Q54":{"entities":["E5124","E5130"]},"Q55":{"count":23},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":20}}
```