**Q1.** A-. A01 assigned A- on 2024-03-12, and A02 did not downgrade it until 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation with a Negative outlook.
**Q3.** No, BB+. The 2031 note I02 is subordinated, and A07 downgraded it to BB+ on 2025-06-20, overriding the earlier A23 (BBB).
**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action, with a POS outlook.
**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, whose latest rating is A (A09).
**Q6.** Valdoria Telecom (E05) is domiciled in VD, and its foreign-currency rating is capped at the Country Ceiling of BB (A12, A14). Its local-currency rating is not capped, so it sits higher at BBB- (A13).
**Q7.** 30 issuers had a downgrade action dated 2026 (QA records ignored); the IDs are in the JSON. Examples are E08 (A21, A22) and E10 (A27).
**Q8.** E08. A22 set RD on 2026-07-08 with nothing after it.
**Q9.** 278. There are 313 distinct non-QA entities with an issuer rating, and 35 of them have a withdrawal as their last action.
**Q10.** Depends. The foreign-currency rating is BB (A14, speculative) and the local-currency rating is BBB- (A13, investment grade).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later watch (A35) did not change the rating.
**Q12.** A-, from A34.
**Q13.** 1, which is A36.
**Q14.** None. E12's first action (A30) is dated 2024-02-01.
**Q15.** A-. A26 set it, and the downgrade A27 only came on 2026-04-15.
**Q16.** No. BBB+ held from 2024-09-30; A35 was a watch and A33 an affirmation.
**Q17.** No. A17 is only a watch (RW).
**Q18.** 32 issuers were on RWN on 1 October 2026 (IDs in the JSON). Example: E06 (A17).
**Q19.** 25 issuers had a Negative outlook; E1146 is excluded because its latest action (A1317) is a watch with no outlook. Example: E01 (A03).
**Q20.** No. E07's rating was withdrawn (A19), and its last rating was BB, not a default.
**Q21.** 35 entities; the IDs are in the JSON. Examples are E07 (A19) and E1001 (A1002, via E1002).
**Q22.** E08 only. A22 is the only RD or D rating in the data.
**Q23.** F2 (A04).
**Q24.** Yes. BBB is investment grade (A03).
**Q25.** 66. This counts instruments whose latest INST action is an assignment at BBB- or better, with expected ratings (EX) not counted.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** 8 entities. VD's ceiling is BB (A12) and CV's is A (A37). Eight non-sovereign entities domiciled in those countries sit exactly at the ceiling; the IDs are in the JSON.
**Q31.** No. No entity domiciled in VD or CV has a foreign-currency rating above its ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09, which has none.
**Q33.** Halden Bank (E10), and the note is rated BBB+. I05 is guaranteed by E10, and A29 and A27 both give BBB+.
**Q34.** No. E12 has no parent link, while E10's parent chain ends at E09.
**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.
**Q36.** 2: E02 (same entity as E03) and E04.
**Q37.** 331. Records are collapsed by LEI and QA test records are excluded; the sovereigns count as distinct entities.
**Q38.** No. The two records have different LEIs.
**Q39.** A (A09).
**Q40.** 66. This counts GB-domiciled entities holding an issuer rating in force on 1 October 2026.
**Q41.** None. E16 is a QA test record, so its actions are ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.
**Q43.** 1, which is Halden Bank (E10/E17).
**Q44.** Yes. I07 is in XVD, which is VD's domestic currency, and E05 is domiciled in VD.
**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, and it is rated BBB- (A45).
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an expected rating (A47, EX), so it is not yet rated.
**Q48.** 106 of the 115 instruments, with 9 unrated because they have only an EX action.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1228","E1307","E1034","E1112","E1159","E1186","E1169","E1167","E1160","E1285","E1263","E1255","E1298","E1300","E1294","E1093","E1080","E1057","E1053","E1144","E1290","E1243","E1229","E1051"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 278},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1099","E1109","E1264","E1209","E1168","E1126","E1260","E1323","E1061","E1066","E1098","E1314","E1266","E1297","E1317","E1181","E1013","E1019","E1037","E1059","E1132","E1146","E1238"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1079","E1056","E1271","E1282","E1046","E1029","E1034","E1064","E1072","E1228","E1261","E1263","E1294","E1300","E1160","E1080","E1105","E1055","E1190","E1005","E1059"]},
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
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 331},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 66},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```