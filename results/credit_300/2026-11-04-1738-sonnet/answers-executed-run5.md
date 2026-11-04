**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01), so it held on 2025-01-01.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation with the outlook moved to Negative; the downgrade to BBB was A02, on 2025-06-20.

**Q3.** No. The 2031 note is I02 (subordinated), rated BB+ (A07), which is below investment grade.

**Q4.** Positive. A09 (2025-09-15) is the current E02 row.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, which is the credit_risk_of entity. I03 carries A (A11) and E02's issuer rating is A (A09).

**Q6.** The data does not state a reason, but it is consistent with the country ceiling. VD's ceiling is BB, and E05's foreign-currency LTIDR is BB (A14) while its local-currency rating is BBB- (A13). The ceiling is a cap on foreign-currency ratings.

**Q7.** 31 issuers had a rating-level downgrade in 2026 (listed in the JSON). I judged this from the rating moving down, not from the action label. E1064's A- to BBB+ is labelled AF, and E1051's, E1229's and E1144's later "DG" rows follow upgrades. I excluded E11, because I05 was downgraded but E11 itself has no rating.

**Q8.** E08. Its rating is RD from 2026-07-08 with no end date (A22).

**Q9.** 278. This counts entities (including the sovereign CV) with a non-withdrawn issuer rating in force on 2026-10-01, with each entity counted once.

**Q10.** Depends. E05 is BB in foreign currency (non-investment grade, A14) but BBB- in local currency (investment grade, A13).

**Q11.** BBB+ (A36, 2024-09-30 to 2025-11-20).

**Q12.** A- (A34).

**Q13.** 1. E14 was downgraded once, from A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating (A30) starts on 2024-02-01.

**Q15.** A-. A26 ran from 2023-05-01 to 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). Only the watch status changed in between (A35).

**Q17.** No. E06's only 2026 action is a move to Rating Watch Negative (A17); the rating stayed at A-.

**Q18.** 31 issuers (listed in the JSON), each with a current row showing a Rating Watch Negative status. E1019, E1059 and E1037 qualify through their local-currency rows or an old open watch.

**Q19.** 25 issuers (listed in the JSON) have a current row with a Negative outlook.

**Q20.** No. E07's rating was BB and then withdrawn (A19), and no default rating was recorded.

**Q21.** 35 entities (listed in the JSON). Each has a withdrawal as its latest row and no later reinstatement.

**Q22.** E08 only, through its RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. This counts instruments whose own current rating is BBB- or better.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** 8 entities. The CV ceiling is A and the VD ceiling is BB; E15, E1039 and E1194 sit at A, and E05, E1028, E1101, E1126 and E1236 sit at BB.

**Q31.** No. No CV entity is rated above A and no VD entity above BB in foreign currency.

**Q32.** E09 (E11 → E10 → E09).

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ (A27), and I05 itself is BBB+ (A29).

**Q34.** No. E12 has no parent, and E10 belongs to the E09 group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is merged into E02.

**Q37.** 331. This is the number of rows in entities.csv, with duplicates already merged.

**Q38.** No. They have different LEIs, countries (DE and US) and entity IDs (E06 and E13), and no record links them.

**Q39.** A (A09).

**Q40.** 66, counting GB-domiciled entities with a non-withdrawn issuer rating in force on 2026-10-01.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity has country LU.

**Q44.** Yes. I07 is flagged local_currency = yes and is denominated in XVD.

**Q45.** No. I07 is a local-currency instrument, so the foreign-currency ceiling does not apply; it is rated BBB- (A45) against the VD ceiling of BB.

**Q46.** No. E11 has no rating rows; I05 is rated through its guarantor E10.

**Q47.** None. I08 has no rating row.

**Q48.** 106. This counts every instrument with a rating row; all of them are still in force.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q30": {"entities": ["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```