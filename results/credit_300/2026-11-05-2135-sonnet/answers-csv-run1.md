**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, is dated 2025-06-20.

**Q2.** No. The only 2026 action is A03, an affirmation at BBB with the outlook moved to Negative.

**Q3.** No. I02 (SUB, 2031) was cut to BB+ in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The guarantor, E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and the latest rating on E02/E03 is A (A09).

**Q6.** The data doesn't state a reason. A14 sets FC at BB, equal to the Valdoria Country Ceiling (A12, BB), while LC is BBB- (A13), which is consistent with the ceiling capping FC.

**Q7.** 42 issuers have a DG on their issuer rating dated in 2026. They are listed in the JSON. A DG on E1341 is dated 2026-11-09, which is after today, so I excluded it. The RESEARCH duplicates E1170, E1161 and E1299 are folded into E1169, E1160 and E1298.

**Q8.** E08. A22 (2026-07-08) took it to RD and there is no later action.

**Q9.** 291. This is distinct entities with a non-withdrawn issuer rating on 2026-10-01, with duplicates merged. It is a manual count, so treat it as approximate.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13) but its FC rating is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) took E14 down to BBB+, and the next action is dated 2025-11-20.

**Q12.** A-. A34 set A- on 2023-01-15 and A36 is dated 2024-09-30.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement and A33 is an affirmation.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 (2023-05-01) set A- and the downgrade A27 is dated 2026-04-15. E17 is a duplicate record of E10.

**Q16.** No. BBB+ applied on 2025-01-01 (after A36) and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative placement at A-, which is not a downgrade.

**Q18.** 32 issuers have a last action that is an RW placement with no later clearing action. They are listed in the JSON, including E1019 and E1059, which are on watch only on their LC ratings.

**Q19.** 35 issuers had a latest outlook of NEG on 2026-10-01. Where the latest action was a watch placement with a blank outlook, I carried the prior outlook forward. Actions dated after 2026-10-01 were ignored.

**Q20.** No. E07 was never rated D or RD; A19 withdrew it for commercial reasons.

**Q21.** 35 entities. Each has a WD (withdrawal) as its latest action and no later rating action. E1279 is not listed because its LC rating (A1596) was never withdrawn.

**Q22.** E08, which went to RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66 instruments held an investment-grade rating. I counted the latest INST rating per instrument and excluded EX-only rows (see Q47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB) and no issuer rating.

**Q30.** E05, E15, E1028, E1039, E1101, E1126, E1194 and E1236. The ceilings are VD = BB (A12) and CV = A (A37), and each of these has an FC rating exactly equal to its country's ceiling.

**Q31.** No. No VD-domiciled entity is rated above BB FC and no CV-domiciled entity is rated above A FC.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest rating is A27 (BBB+).

**Q34.** No. E12 has no parent and no link to E09/E10; only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 370 records, and 26 are duplicate records sharing an LEI with another record (E03, E17 and 24 in the E10xx–E13xx range).

**Q38.** No. They have different LEIs and countries (DE and US), so they are separate entities.

**Q39.** A (A09, 2025-09-15, recorded on duplicate E03).

**Q40.** 73. This is a manual count of GB-domiciled entities with a non-withdrawn issuer rating on 2026-10-01.

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE. E10 (RATINGS source) says DE, while its duplicate E17 (RESEARCH) says LU, so the data conflicts.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE).

**Q44.** Yes. I07's currency is XVD, and its BBB- matches E05's LC rating (A13, A45).

**Q45.** No. I07 is a local-currency instrument, and the ceiling applies to FC ratings.

**Q46.** No. E11 has only a CO (counterparty) rating, A46, and no LTIDR.

**Q47.** None. I08 has only an EX-type row (A47, A), and I'm treating EX as an expected or non-final rating. The data doesn't define EX, so this is ambiguous.

**Q48.** 106 instruments. Eight instruments have only EX rows and are excluded.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1064","E1163","E1058","E1213","E1228","E1350","E1346","E1307","E1347","E1034","E1112","E1169","E1159","E1160","E1167","E1186","E1080","E1093","E1051","E1057","E1053","E1144","E1263","E1285","E1298","E1300","E1294","E1340","E1342","E1343","E1344","E1345","E1348","E1349","E1351","E1290","E1229","E1243","E1255"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1066","E1168","E1109","E1264","E1098","E1006","E1260","E1013","E1126","E1132","E1146","E1181","E1209","E1266","E1297","E1037","E1061","E1238","E1317","E1314","E1323","E1099","E1019","E1059"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1350","E1347","E1228","E1146","E1034","E1056","E1046","E1282","E1248","E1263","E1271","E1132","E1343","E1344","E1348","E1351","E1340","E1342","E1345","E1294","E1300","E1080","E1029","E1261","E1064","E1190","E1079","E1188","E1005","E1059","E1160"]},
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
"Q30": {"entities": ["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 344},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 73},
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