**Q1.** A-. A01 (2024-03-12) assigned A-, and the next action, A02, is dated 2025-06-20.

**Q2.** No. The only 2026 actions are A03/A04, which affirmed BBB and F2.

**Q3.** No. The 2031 note is I02, rated BBB in A23 and cut to BB+ in A07 (2025-06-20).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02, whose latest action is A09.

**Q6.** The data points to the country ceiling. The Valdoria country ceiling (A12) is BB. Valdoria Telecom's foreign-currency rating (A14) is BB, while its local-currency rating (A13) is BBB-. The data gives no explicit reason beyond that.

**Q7.** Downgraded in 2026 (DG actions dated in 2026, up to today): E08, E10, E16 and 38 others, listed in the JSON. E1341's DG (A1720, 2026-11-09) is dated in the future and is excluded. Duplicate RESEARCH records are mapped to their RATINGS record, for example E1170 to E1169.

**Q8.** E08. A22 (2026-07-08) moved it to RD, and it is the only default rating in the data.

**Q9.** About 289, an estimate I did not verify record by record. It counts distinct issuers (deduplicated by LEI) whose latest LTIDR is not a withdrawal. CO ratings and the country-ceiling record are not issuer ratings.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) cut it from A- to BBB+, and A35 (2025-11-20) only put it on watch.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once. A36 is the only DG action for E14.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 (2023-05-01) assigned it, and the downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33, 2026-05-01). The 2025-11 RWN (A35) was not a rating change.

**Q17.** No. The only 2026 Orrin Bank action is A17 (RW, A- unchanged).

**Q18.** On Rating Watch Negative on 1 October 2026: E06 and 30 others, listed in the JSON, where the latest watch was never resolved or withdrawn. Several of these watches date from 2022–2025, so they may be stale.

**Q19.** Negative outlook on 1 October 2026: E01, E09 and 30 others, listed in the JSON. Each entity's latest outlook on or before that date was NEG. E1346 and E1349 are excluded because their NEG actions came after 1 October.

**Q20.** No. A19 is a withdrawal for commercial reasons, not a default. Its last rating was BB.

**Q21.** Entities that had an issuer rating but whose latest action by 1 October 2026 was a withdrawal: E07 and 35 others, listed in the JSON. This includes E07 (A19).

**Q22.** E08 only, via RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** About 68 instruments, counted from the latest INST rating of each instrument rated on 1 October 2026 (BBB- or higher).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country-ceiling record (A12, BB), not an issuer rating.

**Q30.** Foreign-currency issuer rating exactly at the ceiling (VD ceiling BB, CV ceiling A): E05, E1028, E1101, E1126, E1236, E15, E1039 and E1194.

**Q31.** No. No Valdoria or Corvenia company has a foreign-currency rating above its ceiling. E1039's AA- is a local-currency rating (A81), and its foreign-currency rating is A.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent link and E10 sits under E09. The shared "Halden" name is not evidence of a group.

**Q35.** 3 (E09, E10, E11). E17 duplicates E10 by LEI.

**Q36.** 2 (E02, E04). E03 duplicates E02 by LEI.

**Q37.** 344. That is 370 records minus 26 duplicates sharing a LEI, and it includes the two sovereigns.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A (A09 on E03, the same entity as E02).

**Q40.** About 74, an estimate I did not verify record by record. It counts GB-domiciled non-duplicate issuers with an active LTIDR.

**Q41.** BB+ (A44). E16 comes from the QA source system, so treat it with caution.

**Q42.** DE. E10 (RATINGS) says DE, while the duplicate E17 (RESEARCH) says LU. I preferred the RATINGS record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose RATINGS record says DE. If E17's country is taken at face value, the answer would be 1.

**Q44.** Yes, inferred. I07 is in XVD, which appears to be Valdoria's currency (VD), though the data does not define it.

**Q45.** No. The ceiling constrains foreign-currency obligations, and I07 is local-currency. Its BBB- is above the BB ceiling numerically, but the ceiling does not apply to it.

**Q46.** No. E11 only has a CO rating (A46), not an LTIDR.

**Q47.** None. A47 (2026-09-01) expired the rating on I08, so there is no current rating. It was A.

**Q48.** 109. That is all 7 notes among I01–I07, plus 102 of the 107 instruments I1001–I1107; I1008, I1012, I1021, I1046 and I1049 had expired by 1 October. I08 had also expired.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1064","E1058","E1213","E1163","E1228","E1347","E1350","E1346","E1307","E1112","E1169","E1159","E1285","E1349","E1343","E1344","E1348","E1342","E1340","E1345","E1351","E1294","E1263","E1255","E1243","E1167","E1160","E1144","E1080","E1093","E1057","E1053","E1051","E1298","E1290","E1300","E1186","E1229"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 289},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1194","E1203","E1133","E1088","E1099","E1264","E1066","E1109","E1181","E1146","E1168","E1132","E1260","E1098","E1317","E1314","E1126","E1013","E1266","E1297","E1323","E1061","E1238","E1037","E1059","E1019"]},
"Q19": {"issuers": ["E01","E09","E1158","E1348","E1347","E1350","E1344","E1343","E1342","E1340","E1345","E1351","E1294","E1263","E1080","E1300","E1160","E1228","E1056","E1118","E1029","E1046","E1190","E1079","E1072","E1034","E1064","E1055","E1211","E1271","E1261","E1005"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1233","E1218","E1084","E1001","E1225","E1140","E1316","E1320","E1206","E1277","E1021","E1155","E1048","E1007","E1219","E1159","E1253","E1308","E1244","E1107","E1076","E1121","E1200","E1138","E1172","E1041","E1166","E1057","E1234","E1205","E1062","E1279"]},
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