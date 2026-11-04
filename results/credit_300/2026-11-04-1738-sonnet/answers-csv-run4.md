**Q1.** A-. A01 (2024-03-12) assigned A- and the next action, A02, is dated 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB.
**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ by A07 (A23 had it at BBB), which is sub-investment grade.
**Q4.** Positive. A09 affirmed A with a POS outlook, and it sits on E03, which shares E02's LEI and is the same entity.
**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and A09 affirmed A.
**Q6.** The data states no reason. Valdoria's country ceiling (VD, CC) is BB, which equals E05's foreign-currency rating BB (A14), while A13 gives the local-currency rating BBB-.
**Q7.** 43 issuers had a downgrade (DG) dated in 2026 (list in the JSON). E1341's DG (A1720, 2026-11-09) is future-dated relative to today, so I excluded it.
**Q8.** E08. A22 (2026-07-08) took it to RD, and no other entity carries an RD or D rating.
**Q9.** 290. Duplicate records are merged by LEI, and each entity's latest action on or before 2026-10-01 is not a withdrawal. This includes E1115, E1158 and E1303, whose WD is dated before a later action. It excludes VD, which has only a country-ceiling record, and counterparty-only entities.
**Q10.** Depends on currency basis. A13 gives local currency BBB- (investment grade) and A14 gives foreign currency BB (not).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 on 2025-11-20 is later.
**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.
**Q13.** 1. Only A36 is a downgrade.
**Q14.** None. E12's first action, A30, is dated 2024-02-01.
**Q15.** A-. E10 was assigned A- (A26) and downgraded only on 2026-04-15 (A27). E17 is a duplicate record with no actions.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ after A35 (RWN) and A33 (affirmed).
**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch Negative at A-, which is not a downgrade.
**Q18.** 32 issuers have a Rating Watch Negative as their latest action (list in the JSON). E1019 and E1059 are on watch on their local-currency ratings only.
**Q19.** 35 issuers have a Negative outlook as of 2026-10-01 (list in the JSON). E1346 (A1730) and E1349 (A1736) are excluded because their NEG downgrades fall after 1 October. E1059's negative outlook is on its foreign-currency rating, while its local-currency rating is on watch.
**Q20.** No. E07 was withdrawn for commercial reasons (A19), not defaulted.
**Q21.** 36 entities had an issuer rating that was later withdrawn (list in the JSON).
**Q22.** Only E08, via A22 (RD).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 68. Counting instruments rated BBB- or better and not expired by 1 October gives 5 among I01–I08 and 63 among I1001–I1107.
**Q26.** A+ (A40).
**Q27.** A- (A42, I06).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a country-ceiling record (A12, BB) and no issuer rating.
**Q30.** Eight entities: E05, E1028, E1101, E1126 and E1236 at the Valdoria ceiling BB, and E15, E1039 and E1194 at the Corvenia ceiling A.
**Q31.** No. No Valdoria or Corvenia company has a foreign-currency rating above BB or A respectively.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded it to BBB+.
**Q34.** No. E12 has no parent_id and a different LEI, so the data does not link it to the Halden group (E09). Only the name is similar.
**Q35.** 3: E09, E10 and E11. E17 duplicates E10.
**Q36.** 2: E02 and E04. E03 duplicates E02.
**Q37.** 344. There are 370 rows, and 26 RESEARCH rows duplicate an LEI already present.
**Q38.** No. They have different LEIs, countries (DE vs US) and ids (E06, E13).
**Q39.** A (A09).
**Q40.** 74. These are the GB-domiciled entities whose latest issuer-rating action by 2026-10-01 is not a withdrawal.
**Q41.** BB+ (A44). E16 comes from the QA source system.
**Q42.** DE (E10). The research duplicate E17 says LU.
**Q43.** 0. E17 is the only LU record and duplicates E10, which is DE in the RATINGS record.
**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's local currency (E05 is in VD, and the note's BBB- matches the local-currency rating). The data does not define XVD explicitly.
**Q45.** No. The ceiling (BB) caps foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).
**Q46.** No. E11 has only a counterparty rating (A46, CO, BBB), not an issuer rating.
**Q47.** None. A47 marked I08 expired (EX) on 2026-09-01, when it was rated A.
**Q48.** 109. There are 115 instruments, and six had expired by 1 October: I08, I1008, I1012, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1064","E1163","E1058","E1213","E1228","E1347","E1350","E1346","E1307","E1034","E1186","E1159","E1169","E1167","E1160","E1112","E1093","E1080","E1051","E1057","E1151","E1144","E1285","E1263","E1255","E1294","E1298","E1300","E1340","E1343","E1344","E1342","E1345","E1348","E1349","E1351","E1290","E1229","E1243","E1053"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1019","E1088","E1099","E1109","E1132","E1264","E1260","E1168","E1209","E1098","E1181","E1066","E1006","E1037","E1061","E1126","E1238","E1266","E1297","E1314","E1317","E1323","E1146","E1013","E1059"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1079","E1228","E1347","E1350","E1351","E1343","E1344","E1342","E1348","E1340","E1345","E1300","E1263","E1056","E1034","E1080","E1072","E1046","E1064","E1029","E1160","E1190","E1211","E1261","E1294","E1005","E1105","E1055","E1248","E1271","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 68},
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
"Q48": {"count": 109}
}
```