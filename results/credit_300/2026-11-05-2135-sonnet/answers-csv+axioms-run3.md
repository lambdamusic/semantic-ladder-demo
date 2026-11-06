**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB on 2026-02-10 (A03). The downgrade was in 2025 (A02).

**Q3.** No, it is BB+. The 2031 note (I02) was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity. A09 (2025-09-15, affirmed A, POS) supersedes A08 (STA).

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and E02's current rating is A via A09 on E03, the same entity.

**Q6.** The data does not state a reason. It is consistent with the Country Ceiling: VD's ceiling is BB (A12), which matches E05's FC rating of BB (A14), while the LC rating is BBB- (A13).

**Q7.** 29 issuers still hold a rating in force and have a 2026 DG on an issuer rating (list in the JSON). Duplicate research records are resolved to their RATINGS records, and QA records are excluded. E1057 and E1159 were also downgraded in 2026 but were withdrawn by 1 October (A1124, A1342), so they are not counted.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) and no later action exists. It is the only RD or D rating in the data.

**Q9.** 278. This counts distinct legal entities, merging records that share an LEI, with an LTIDR or STIDR in force on 2026-10-01: not withdrawn, not superseded, and not a QA record. In three cases (E1115, E1158, E1303) a rating was affirmed or upgraded after a withdrawal, and I counted them as in force per the rules.

**Q10.** Depends. E05's FC rating is BB (A14), which is sub-investment grade, and its LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and was still BBB+ on 2025-06-01.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34), before the 2024 downgrade.

**Q13.** Once, on 2024-09-30 (A36).

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E17 shares E10's LEI, and E10 was rated A- from 2023-05-01 (A26). It was downgraded to BBB+ only on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ from 2024-09-30 (A36), and the 2025 watch (A35) and 2026 affirmation (A33) were both at BBB+.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17). E13 (Orrin Bancorp) is a different entity.

**Q18.** 32 entities. Each has a Rating Watch Negative as the latest rating action on a rating still in force (list in the JSON).

**Q19.** 27 entities. Each has a Negative outlook on the latest rating action on a rating still in force (list in the JSON).

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19). It was last rated BB (A18), not a default rating.

**Q21.** 35 entities. They had an issuer rating that was later withdrawn and not reinstated (list in the JSON).

**Q22.** E08 only. It is the only RD or D rating in the data (A22).

**Q23.** F2, affirmed on 2026-02-10 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 66. Of the 106 instruments with a non-expected rating in force, 66 are rated BBB- or better (Q48 gives the 106).

**Q26.** A+ (A40, LC).

**Q27.** A- (A42).

**Q28.** BBB+ (A38, FC).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** 8 entities (list in the JSON). Their FC LTIDR equals the ceiling: BB for VD (A12) and A for CV (A37). E1245 is excluded because its research record puts its domicile in FR.

**Q31.** No. No entity has an FC LTIDR above its ceiling: VD entities are at BB or below, and CV entities are at A or below. E1039's LC AA- is not an FC rating.

**Q32.** E09. E11's parent is E10 and E10's parent is E09, which has no parent.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent link and a different LEI from the group, so the shared name alone does not make it part of the group.

**Q35.** 3: E09, E10 (the same entity as E17) and E11.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 331. There are 370 records. I removed 13 QA test records and 26 RESEARCH duplicates that share an LEI with a RATINGS record. The two sovereigns have no LEI and count once each.

**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214) and no link between them.

**Q39.** A (A09, affirmed on the same entity as E02).

**Q40.** 66. This is the GB-domiciled subset of the Q9 issuers, using the research country where one exists. E10 is excluded because its research record is in LU.

**Q41.** None. E16 is a QA test record, so its actions are not rating actions and it has no rating in force.

**Q42.** LU. The RESEARCH record E17 gives LU for the same LEI as E10, and research country takes precedence.

**Q43.** 1: E10, the same entity as E17.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), but the ceiling constrains only FC ratings and I07 is a local-currency note.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating in force.

**Q48.** 106. There are 115 instruments, and 9 have only an expected rating: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1228","E1307","E1034","E1186","E1160","E1169","E1285","E1263","E1255","E1167","E1151","E1112","E1093","E1080","E1051","E1300","E1294","E1290","E1298","E1144","E1229","E1243","E1053"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1088","E1194","E1203","E1133","E1181","E1099","E1098","E1146","E1168","E1019","E1037","E1013","E1066","E1061","E1059","E1109","E1126","E1132","E1264","E1260","E1266","E1297","E1314","E1317","E1323","E1209","E1238"]},
"Q19": {"issuers": ["E01","E09","E1029","E1158","E1118","E1056","E1034","E1046","E1064","E1079","E1080","E1160","E1190","E1228","E1248","E1261","E1263","E1271","E1294","E1300","E1072","E1005","E1055","E1105","E1211","E1188","E1282"]},
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