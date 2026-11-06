**Q1.** A-. Kestrel's LTIDR (FC) was A- from A01 (2024-03-12) until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. The only 2026 action on E01 is A03 (2026-02-10), an affirmation at BBB with a Negative outlook.

**Q3.** No, it is BB+. The 2031 note is I02, and A07 (2025-06-20) downgraded it from BBB (A23) to BB+.

**Q4.** Positive. E03 is a duplicate of E02 (same LEI), and A09 (2025-09-15) affirmed A with a POS outlook, superseding A08 (STA).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A08, A09).

**Q6.** The data does not state a reason. It is consistent with a country-ceiling cap: A12 sets Valdoria's CC at BB, and A14 gives E05 FC BB against LC BBB- (A13).

**Q7.** 42 issuers had a downgrade (DG) dated in 2026; they are listed in the JSON. Duplicate research records are mapped to the RATINGS record (E1170→E1169, E1161→E1160, E1299→E1298). I excluded E1341, whose DG (A1720) is dated 2026-11-09, after today. E1057, E1159, E1243 and E1229 are also included.

**Q8.** E08 (Saxby Shipping). A22 (2026-07-08) took it to RD, and there is no later action.

**Q9.** 290. This counts distinct entities whose latest LTIDR action on or before 2026-10-01 is not a withdrawal, merging duplicates by LEI. It includes the QA-source records, and I treated E1158, E1303 and E1115 as rated because later actions follow their withdrawals.

**Q10.** Depends. FC is BB (A14, sub-investment grade) but LC is BBB- (A13, investment grade).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 from A- to BBB+, and the later actions A35 and A33 keep BBB+.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade; A35 is a watch action and A33 an affirmation.

**Q14.** None. Halden Foods' first action, A30, is dated 2024-02-01.

**Q15.** A-. E10 had A- from A26 until A27 (2026-04-15). E17 is a duplicate of E10 and has no actions.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A35 only adds a watch, and A33 affirms).

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch Negative at A-, with no rating change.

**Q18.** 32 issuers were on Rating Watch Negative: their latest action on or before 2026-10-01 is an RW with RWN and nothing later cleared it. The list is in the JSON. E1019 and E1059 are included on the strength of local-currency watches only.

**Q19.** 34 issuers had a Negative outlook. Watch actions carry no outlook, so I did not carry an earlier NEG through them. I excluded E1346, E1349 and E1341, whose NEG actions (A1730, A1736, A1720) come after 1 Oct.

**Q20.** No. E07's last action is A19, a withdrawal for commercial reasons, not a default.

**Q21.** 36 entities, all of whose latest LTIDR action on or before 2026-10-01 is a withdrawal (WD). They are listed in the JSON; E1001 is carried by E1002's actions, E1021 by E1022's, E1138 by E1139's, and E1253 by E1254's.

**Q22.** E08 only. It is the only entity with an RD or D rating (A22).

**Q23.** F2. A04 (2026-02-10) affirmed E01's STIDR at F2.

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 66 instruments. This counts instruments whose latest INST action on or before 2026-10-01 is BBB- or better and is not an EX. Instruments whose only action is an EX are treated as not rated at that date.

**Q26.** A+ (A40, LC).

**Q27.** A-. The 2032 note is I06, rated by A42.

**Q28.** BBB+. A38 sets Corvenia's FC LTIDR.

**Q29.** None. VD has only a Country Ceiling record (A12, BB) and no LTIDR.

**Q30.** 8 entities have an FC rating exactly at their country's ceiling. Valdoria's ceiling is BB (A12) and Corvenia's is A (A37). The at-ceiling entities are E05, E1028, E1101, E1126 and E1236 (all BB) and E15, E1039 and E1194 (all A).

**Q31.** No. Every FC rating for a Valdoria or Corvenia company is at or below its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27 (2026-04-15).

**Q34.** No. E12 has no parent and no link to E09, E10 or E11.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. entities.csv has 370 rows, and 26 are RESEARCH duplicates sharing a LEI with another row.

**Q38.** No. They have different LEIs, countries (DE vs US) and no parent link.

**Q39.** A (A08, affirmed in A09).

**Q40.** 74 GB-domiciled issuers, including 7 QA-source records.

**Q41.** BB+ (A44, 2026-06-01). Note that E16 comes from the QA source system.

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU, so the sources conflict.

**Q43.** 0. The only LU row is E17, a duplicate of E10, whose RATINGS record places it in DE. Counted as its own entity, it would be 1.

**Q44.** Yes, by inference. I07 is in XVD, which appears to be Valdoria's local currency, but the data has no currency-to-country table.

**Q45.** No. I07 is BBB- (A45), above the BB ceiling, but the ceiling applies to foreign-currency ratings and I07 is a local-currency note.

**Q46.** No. E11 has only a CO rating (A46, BBB) and no LTIDR.

**Q47.** None. I08's only action, A47, is an EX on 2026-09-01 (last rating A), so it has no current rating.

**Q48.** 106 instruments. 115 instruments exist, and 9 have no active rating: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049, whose only action is an EX.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1064","E1163","E1058","E1213","E1307","E1228","E1350","E1346","E1347","E1169","E1034","E1160","E1186","E1112","E1167","E1285","E1263","E1349","E1159","E1300","E1080","E1051","E1053","E1144","E1057","E1340","E1342","E1343","E1344","E1345","E1351","E1348","E1294","E1298","E1255","E1093","E1243","E1290","E1229"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 290},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1006","E1088","E1168","E1099","E1037","E1066","E1061","E1264","E1260","E1266","E1098","E1297","E1323","E1314","E1317","E1209","E1181","E1126","E1146","E1132","E1013","E1109","E1238","E1019","E1059"]},
"Q19": {"issuers": ["E01","E09","E1350","E1347","E1343","E1342","E1344","E1345","E1348","E1351","E1340","E1158","E1118","E1034","E1072","E1282","E1263","E1228","E1029","E1046","E1056","E1261","E1160","E1190","E1271","E1248","E1294","E1300","E1005","E1080","E1079","E1059","E1188","E1105"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
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