**Q1.** A-. A01 assigned A- on 2024-03-12 and it stayed in force until A02 (2025-06-20).

**Q2.** No. Kestrel's only 2026 action is A03, an affirmation at BBB; the downgrade (A02) was in 2025.

**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ in A07, which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, and A09 (2025-09-15) affirmed A with a Positive outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03's guarantor is E02, so the credit risk is E02's (A09, A).

**Q6.** The Valdoria country ceiling caps it. The sovereign's ceiling is BB (A12) and the foreign-currency rating is BB (A14). The local-currency rating of BBB- (A13) is not subject to that cap.

**Q7.** 30 rated entities were downgraded in 2026 (list in the JSON). The list uses rated record IDs and includes entities withdrawn later (E1057, E1159). It excludes instrument downgrades (A29) and the QA test record E16 (A44).

**Q8.** Only Saxby Shipping (E08), which went to RD in A22 on 2026-07-08.

**Q9.** About 278 distinct issuers hold an in-force issuer rating. This counts one entity per LEI, excludes QA records and entities whose latest action is a withdrawal, and includes some with only a local-currency rating in force. It is a manual count over a very large file, so treat it as approximate.

**Q10.** Depends. Foreign currency is BB (A14), which is below investment grade; local currency is BBB- (A13), which is investment grade.

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and it was still BBB+ on 2025-06-01 (the RW in A35 came later).

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.

**Q15.** A-. A26 assigned it in 2023, and the downgrade (A27) came on 2026-04-15. E17 is just the research record for the same LEI.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 changed only the watch status and affirmed).

**Q17.** No. Orrin Bank's only 2026 action is a Rating Watch placement (A17). Orrin Bancorp (E13) is a different entity.

**Q18.** 33 rated records have a Rating Watch Negative as their latest action (list in the JSON). It includes E1019 and E1059, which are on watch only on their local-currency ratings.

**Q19.** 26 rated records have a Negative outlook on their latest action (list in the JSON).

**Q20.** No. Pellam Retail's rating was withdrawn (A19), and it was never rated RD or D.

**Q21.** 35 rated records had an issuer rating that was later withdrawn and not reinstated (list in the JSON).

**Q22.** Only Saxby Shipping (E08), via A22. No other record carries RD or D.

**Q23.** F2, from A04 (affirmed 2026-02-10).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** About 66 instruments held an investment-grade rating on 1 October 2026. Instruments with only an expected rating (EX) are not counted as rated.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. Valdoria has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** Eight entities were exactly at their ceiling: E05, E1028, E1101, E1126 and E1236 at BB (Valdoria), and E15, E1039 and E1194 at A (Corvenia). Domicile follows the RESEARCH record, so Gater (E1245) is treated as French and drops out.

**Q31.** No. Nothing sits above its ceiling, and the closest cases are exactly at it (see Q30).

**Q32.** Halden Group plc (E09). E11's parent is E10, whose parent is E09, which has none.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. Halden Foods (E12) has no parent. Halden Bank sits under E09, so the shared name alone does not make them one group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate record of E02.

**Q37.** About 331. There are 370 records, minus 26 RESEARCH duplicates (same LEI) and 13 QA test records, and the two sovereigns are counted.

**Q38.** No. Their LEIs differ (E06 and E13), and they have no parent link.

**Q39.** A, from A09.

**Q40.** About 65 GB-domiciled issuers hold an in-force issuer rating. This is a manual count and approximate.

**Q41.** None. Brindle Capital (E16) is a QA test record, so its actions are not treated as rating actions.

**Q42.** LU. The RESEARCH record E17 (LU) takes precedence over the RATINGS record E10 (DE).

**Q43.** 1. Only the Halden Bank entity (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 is in XVD and the issuer's domicile is VD, whose domestic currency is XVD.

**Q45.** No. The ceiling applies to foreign-currency issuer ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating in force.

**Q48.** 106 instruments. Of 115, nine have only expected ratings: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1186","E1228","E1285","E1263","E1307","E1159","E1170","E1161","E1167","E1112","E1093","E1080","E1051","E1053","E1144","E1034","E1057","E1290","E1294","E1299","E1300","E1255","E1243","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1088","E1126","E1013","E1133","E1323","E1132","E1061","E1006","E1019","E1066","E1276","E1264","E1260","E1238","E1098","E1297","E1314","E1317","E1146","E1168","E1109","E1099","E1181","E1194","E1203","E1210","E1037","E1266","E1059"]},
"Q19": {"issuers": ["E01","E09","E1034","E1158","E1055","E1056","E1005","E1079","E1118","E1228","E1300","E1190","E1064","E1072","E1161","E1105","E1080","E1029","E1046","E1263","E1294","E1262","E1248","E1271","E1282","E1211"]},
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