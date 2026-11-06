**Q1.** A-. Kestrel's LTIDR was A- from 2024-03-12 (A01) until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on Kestrel is A03, an affirmation at BBB with the outlook moved to Negative.

**Q3.** No, BB+. I02 (the 2031 subordinated note) was cut from BBB to BB+ in A07.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity, and the latest action is A09 (2025-09-15), an affirmation at A with a Positive outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and E02's rating is A (A09 on E03, the duplicate record).

**Q6.** Valdoria's Country Ceiling (A12) is BB. The foreign-currency rating is capped at BB (A14), while the local-currency rating is BBB- (A13).

**Q7.** 43 issuers were downgraded in 2026 (IDs in the JSON, including E08, E10 and E16). Each has an LTIDR "DG" action dated 2026-01-01 to 2026-11-06.

**Q8.** E08 (Saxby Shipping). It was downgraded to RD on 2026-07-08 (A22), and there are no later actions.

**Q9.** 291. These are the distinct entities, deduplicated by LEI, whose latest LTIDR action on or before 2026-10-01 was not a withdrawal. The count includes the two sovereigns.

**Q10.** Depends. The foreign-currency rating is BB (sub-investment grade) and the local-currency rating is BBB- (investment grade).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36), and the next action is 2025-11-20.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26), and the downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+, with an A35 watch and an A33 affirmation in between.

**Q17.** No. Orrin Bank (E06) has only A16 and A17, and A17 is a Rating Watch Negative placement at A-, not a downgrade.

**Q18.** 32 issuers were on Rating Watch Negative on 1 October 2026 (IDs in the JSON). Each has a latest LTIDR action that is a watch.

**Q19.** 37 issuers had a Negative outlook on 1 October 2026 (IDs in the JSON), including E01 (A03) and E09 (A25).

**Q20.** No. Pellam (E07) was withdrawn for commercial reasons (A19), and its last rating was BB; no default rating was ever recorded.

**Q21.** 35 entities (IDs in the JSON). Each had an LTIDR before 2026-10-01 but its latest LTIDR action is a withdrawal, as with E07.

**Q22.** E08, the only entity with an RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66. Of 106 instruments rated on 1 October 2026, 66 were BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** E05, E1028, E1039, E1101, E1126, E1194, E1236 and E15. Each has a foreign-currency LTIDR equal to its country's ceiling.

**Q31.** No. No foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is issued by E11 but guaranteed by E10, and both the note (A29) and E10 (A27) are BBB+.

**Q34.** No. E12 (Halden Foods) has no parent link, so it is not in E09's group; the shared name is not evidence.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate record of E02.

**Q37.** 344. The 370 records contain 342 distinct LEIs, and the two sovereigns (CV, VD) have no LEI.

**Q38.** No. E06 and E13 have different LEIs and are a bank and a holding company, so they are separate entities.

**Q39.** A. E02 and E03 are the same entity, and the latest action (A09) is an affirmation at A.

**Q40.** 74. These are distinct GB-domiciled entities, deduplicated by LEI, with an active issuer rating on 1 October 2026.

**Q41.** BB+. E16 was downgraded on 2026-06-01. It comes from the QA source system.

**Q42.** DE. E10 is the RATINGS record; E17, the LU record, is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, is a duplicate of the German E10, so I treated it as not a separate LU entity. If you count raw records instead, the answer is 1.

**Q44.** Yes. I07 is denominated in XVD, which I read as Valdoria's local currency.

**Q45.** No. The ceiling (BB) limits foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a CO-type rating (A46, BBB), not an LTIDR.

**Q47.** None. I08's rating was expired by an EX action on 2026-09-01 (A47).

**Q48.** 106. This counts instruments whose latest INST action on or before 2026-10-01 is not an expiry or withdrawal.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 291},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1039","E1101","E1126","E1194","E1236","E15"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 344},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 74},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```