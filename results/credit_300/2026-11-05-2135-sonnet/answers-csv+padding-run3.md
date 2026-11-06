**Q1.** A-. A01 assigned A- (2024-03-12); the next action, A02, was not until 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB (2026-02-10).

**Q3.** No, BB+. I02 (subordinated, issuer E01) was downgraded to BB+ by A07.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A10, A11).

**Q6.** The data does not state a reason. Valdoria's country ceiling is BB (A12) and E05's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13), which is consistent with the ceiling capping the foreign-currency rating.

**Q7.** 30 issuers had an issuer-rating downgrade in 2026 (listed in the JSON, duplicates merged, QA records excluded). E08 was downgraded twice (A21, A22).

**Q8.** E08 (Saxby Shipping). A22 downgraded it to RD on 2026-07-08, and nothing followed.

**Q9.** 278. Of 313 entities that ever held an issuer rating, 35 had withdrawn it by 2026-10-01. Sovereign CV counts; VD has only a country ceiling.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+.

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 assigned it in 2023, and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 RWN, A33 affirmed).

**Q17.** No. E06's only 2026 action is a Watch Negative (A17), with no rating change.

**Q18.** 32 issuers; the list is in the JSON. These are entities whose latest action is a watch with no later resolution. E1019 and E1059 are on watch for their local-currency ratings only.

**Q19.** 27 issuers; the list is in the JSON. These are entities whose latest action carries a NEG outlook.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and no default rating (D or RD) was recorded.

**Q21.** 35 entities; the list is in the JSON. All are entities whose last issuer-rating action by 2026-10-01 was a withdrawal.

**Q22.** E08, the only entity with an RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade (A03).

**Q25.** 68. This counts the latest instrument ratings at BBB- or above on 2026-10-01 (5 of I01–I07, 63 of I1001–I1107); instruments expired before that date are excluded.

**Q26.** A+ (A40).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country-ceiling record (A12, BB) and no issuer rating.

**Q30.** 8 entities (listed in the JSON). VD's ceiling is BB and CV's is A, and these have foreign-currency ratings at exactly that level.

**Q31.** No. Within the only two ceilings in the data (VD, CV), no company's foreign-currency rating is above its ceiling; other countries have no ceiling data.

**Q32.** E09 (Halden Group plc). E11 has parent E10, which has parent E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10 (downgraded by A27 and A29).

**Q34.** No. E12 has no parent link, and sharing a name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04, with E03 a duplicate of E02.

**Q37.** 344. That is 370 rows less 26 RESEARCH duplicates of the same LEI.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US), and neither is linked to the other.

**Q39.** A (A08, A09).

**Q40.** 66 GB-domiciled issuers (duplicates merged, withdrawn and QA excluded).

**Q41.** None. E16 is a QA-system record and I treated it as non-production; its only ratings are A43 (BBB-) and A44 (BB+).

**Q42.** DE. E10 says DE and the RESEARCH duplicate E17 says LU, so I took the RATINGS record.

**Q43.** 0. The only LU row is E17, a duplicate of E10 whose primary record is DE.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's own currency (inferred from the code, not defined in the data).

**Q45.** No. The ceiling caps foreign-currency ratings, and I07 is local-currency at BBB- (A45).

**Q46.** No. E11 has only a CO rating (A46), not an issuer default rating.

**Q47.** None. The only record on I08 is an EX action on 2026-09-01 (A47), so it is no longer rated.

**Q48.** 109. That is 7 seed instruments plus 102 generated, with 6 expired before 2026-10-01 excluded. I counted I1001, I1007 and I1015 as rated because their EX actions fall after 1 October; I assumed EX means the rating expired on that date.

Assumptions: I excluded QA-source records from the counts, merged same-LEI duplicates, and ordered actions by date. E1115, E1158 and E1303 have withdrawal actions dated before later rating actions, so by date they count as rated. I treated E1279 as still rated because only its foreign-currency rating was withdrawn.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1034","E1159","E1307","E1169","E1160","E1167","E1186","E1263","E1285","E1300","E1298","E1294","E1057","E1093","E1080","E1112","E1053","E1051","E1229","E1255","E1243","E1144","E1151"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1006","E1088","E1019","E1168","E1260","E1264","E1061","E1099","E1098","E1109","E1132","E1146","E1181","E1209","E1266","E1297","E1314","E1317","E1323","E1126","E1066","E1059","E1238","E1037","E1013"]},
"Q19": {"issuers": ["E01","E09","E1118","E1158","E1282","E1228","E1034","E1029","E1046","E1190","E1261","E1064","E1056","E1005","E1079","E1072","E1248","E1271","E1294","E1263","E1300","E1080","E1160","E1188","E1059","E1211","E1105"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1225","E1206","E1001","E1308","E1140","E1138","E1320","E1277","E1219","E1121","E1244","E1007","E1062","E1076","E1021","E1155","E1107","E1166","E1200","E1172","E1159","E1234","E1205","E1253","E1057","E1048","E1316","E1041"]},
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
"Q40": {"count": 66},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 109}
}
```