**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01), which covers 1 Jan 2025.

**Q2.** No. E01 moved from A- to BBB in 2025 (A02); the 2026-02-10 record (A03) only changed the outlook to Negative, with the rating still BBB.

**Q3.** No. The 2031 note is I02, rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's open record A09 shows A with a POS outlook.

**Q5.** E02 (Northwind Holdings), rated A. I03 has E04 as issuer and E02 as guarantor and credit_risk_of, and E02's LTIDR is A (A09).

**Q6.** The data doesn't state a reason. It shows E05 at BB foreign-currency and BBB- local-currency (A14, A13), and Valdoria's country ceiling is BB (ceilings.csv). That is consistent with the ceiling capping the FC rating, but the data doesn't say so explicitly.

**Q7.** 30 issuers had a rating lowered in 2026, judged by the rating actually falling between consecutive records rather than by the action label (which is inconsistent, e.g. A1141 and A1146). Examples are E08 (A21, A22), E10 (A27) and E1034 (A1070). The full list is in the JSON.

**Q8.** E08. Its open record A22 has rating RD, and no other open record shows a default rating.

**Q9.** 278. I counted entities with an open, non-WD LTIDR on 1 Oct 2026, counting E1279 for its open LC rating.

**Q10.** Depends. E05 is BB on a foreign-currency basis (not investment grade) and BBB- on a local-currency basis (investment grade).

**Q11.** BBB+. A36 covers 2024-09-30 to 2025-11-20.

**Q12.** A-. A34 covers 2023-01-15 to 2024-09-30.

**Q13.** 1. Only A36 (A- to BBB+) is a true downgrade for E14; A35 and A33 keep the rating at BBB+.

**Q14.** None. E12's first rating (A30) starts 2024-02-01.

**Q15.** A-. A26 runs from 2023-05-01 to 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), with only a watch period in between (A35).

**Q17.** No. E06 was only placed on Rating Watch Negative on 2026-09-03 (A17), with the rating still A-.

**Q18.** 31 issuers had an open RWN record on 1 Oct 2026. The full list is in the JSON.

**Q19.** 27 issuers had an open record with a Negative outlook. The full list is in the JSON.

**Q20.** No. E07's rating was withdrawn (WD, A19), which is not a default.

**Q21.** 35 entities. Each has an open WD record and no other open issuer rating (E1279 and E1106 keep an open FC or LC rating, so they are excluded). The full list is in the JSON.

**Q22.** E08. It went to RD in A22, and no entity has a D rating.

**Q23.** F2 (STIDR, A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. Of the 106 instruments with an open rating, 40 are below BBB-.

**Q26.** A+ (E15 LC, A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV FC, A38).

**Q29.** None. VD has no rating records.

**Q30.** E05, E15, E1028, E1039, E1101, E1126, E1194, E1236. The CV ceiling is A and the VD ceiling is BB, and each of these has an open FC rating exactly at its country's ceiling.

**Q31.** No. No company's open FC rating exceeds its country's ceiling.

**Q32.** E09. E11's ultimate_parent_id is E09 (via E10).

**Q33.** E10 (Halden Bank), rated BBB+. I05 names E10 as guarantor and credit_risk_of, and E10's LTIDR is now BBB+ (A27).

**Q34.** No. E12 has no parent and sits outside the E09 chain.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04 (E03 is a duplicate record of E02).

**Q37.** 331. That is 16 entities from the E01-series plus CV and VD, plus 339 IDs in E1001–E1339 less 24 merged duplicates.

**Q38.** No. E06 (DE) and E13 (US) are separate entities with different LEIs and countries.

**Q39.** A (POS outlook, A09).

**Q40.** 66 GB-domiciled entities held an open, non-WD issuer rating.

**Q41.** None. No entity named Brindle Capital appears in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is in XVD with local_currency = yes.

**Q45.** No. I07 is a local-currency note rated BBB- (A45), and the Valdoria ceiling of BB applies to foreign-currency ratings.

**Q46.** No. E11 has no rating records of its own; I05 is rated on E10's credit.

**Q47.** None. I08 has no instrument rating record.

**Q48.** 106 instruments had an open rating on 1 Oct 2026.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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