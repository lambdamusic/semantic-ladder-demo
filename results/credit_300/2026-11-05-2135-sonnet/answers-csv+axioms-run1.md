**Q1.** A-. A01 assigned A- on 2024-03-12 and A02 (downgrade to BBB) came only on 2025-06-20.

**Q2.** No. Kestrel's only 2026 action is A03, an affirmation at BBB; the downgrade (A02) was in 2025.

**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ by A07, which is below investment grade.

**Q4.** Positive. A09 affirmed A with a POS outlook on E03, which shares E02's LEI, so it is the same entity and supersedes A08 (STA).

**Q5.** The holder takes the risk of E02, the guarantor of I03, whose rating is A (A08, affirmed by A09 via E03).

**Q6.** The data doesn't state a reason. It shows only E05's foreign-currency BB (A14) against its local-currency BBB- (A13), with the Valdoria Country Ceiling at BB (A12), so the foreign-currency rating matches the ceiling.

**Q7.** 28 issuers, listed in the JSON. These are issuers with a 2026 DG action on an issuer rating (LTIDR/STIDR) who still hold a rating in force. I excluded QA test records and E1159, which was downgraded by A1341 but withdrawn by A1342. I used the rated record ID, so research-record IDs such as E1161, E1170 and E1299 appear as themselves.

**Q8.** E08. A22 moved it to RD on 2026-07-08 and nothing later supersedes it.

**Q9.** 278. This counts distinct LEIs with an LTIDR/STIDR action in force on 2026-10-01 (not withdrawn, not superseded), excluding QA records. A series withdrawn and later re-rated (E1158, E1115, E1303) counts as active, and E1279 counts through its local-currency series. The count is hand-tallied, so treat it as approximate.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+; A35 (watch) and A33 (affirmation) did not change it.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once, by A36.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10 was assigned A- by A26 and downgraded only on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+; A35 and A33 are a watch and an affirmation.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative placement at A-.

**Q18.** 32 issuers, listed in the JSON. Each has a watch action (RW) still current on 2026-10-01. Watches later superseded, such as E14's A35 by A33, are excluded.

**Q19.** 27 issuers, listed in the JSON. Each has a NEG outlook on the action still in force on 2026-10-01.

**Q20.** No. E07 was withdrawn on 2026-05-12 (A19, commercial reasons) and never rated D or RD.

**Q21.** 35 entities, listed in the JSON. Each had an issuer rating that was later withdrawn (WD) and not reinstated by 2026-10-01.

**Q22.** E08 only. A22 is the only RD or D rating in the data.

**Q23.** F2 (A04, STIDR, 2026-02-10).

**Q24.** Yes. E01's long-term rating is BBB (A03).

**Q25.** 66. This counts instruments whose current non-EX rating is BBB- or better.

**Q26.** A+ (A40, local-currency rating for E15).

**Q27.** A- (A42 on I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05, E1028, E1101, E1126 and E1236 sit at the Valdoria ceiling of BB. E15, E1039 and E1194 sit at the Corvenia ceiling of A.

**Q31.** No. No foreign-currency issuer rating from a VD- or CV-domiciled company exceeds its ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09, which has no parent.

**Q33.** The holder takes the risk of E10, the guarantor of I05, whose rating is BBB+ (A27).

**Q34.** No. E12 has no parent and E10's parent is E09, so they only share a name prefix.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).

**Q36.** 2: E02 and E04 (E03 is a duplicate record of E02).

**Q37.** 331. That is 370 records, less 13 QA test records, less 26 same-LEI research duplicates.

**Q38.** No. They have different LEIs (E06 549300AMVE…, E13 815600O8X8…) and different countries.

**Q39.** A (A09, affirmed 2025-09-15).

**Q40.** 65, counting GB-domiciled distinct issuers with a rating in force on 2026-10-01 (hand-tallied).

**Q41.** None. E16 is a QA test record, so its action isn't a rating in force.

**Q42.** LU. The research record E17 shares E10's LEI and gives LU.

**Q43.** 1. The only LU-domiciled entity is the one behind E10/E17.

**Q44.** Yes. I07 is in XVD, which is the VD domestic currency, and E05 is domiciled in VD.

**Q45.** No. The ceiling constrains foreign-currency issuer ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46, CO).

**Q47.** None. I08's only action is A47, an expected rating (EX) dated 2026-09-01, and it was never finalised.

**Q48.** 106. Of 115 instruments, 9 have no rating in force: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049 (only EX actions).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1058","E1064","E1080","E1093","E1112","E1144","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1034","E1046","E1029","E1072","E1228","E1190","E1271","E1161","E1262","E1263","E1294","E1300","E1105","E1080","E1079","E1282","E1005","E1211","E1248","E1188","E1060","E1064"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
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
"Q40": {"count": 65},
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