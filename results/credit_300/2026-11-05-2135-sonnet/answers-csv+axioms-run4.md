**Q1.** A-. A01 assigned E01 A- on 2024-03-12, and the next change was A02 (DG to BBB) on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook.

**Q3.** No, BB+. The 2031 note is I02, and A07 (2025-06-20) downgraded it from BBB (A23) to BB+.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed it at A with a POS outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and E02's latest rating is A09/A11 (A).

**Q6.** The foreign-currency rating is capped by the Country Ceiling. A12 sets Valdoria's ceiling at BB, so A14 (FC) is BB, while the local-currency rating in A13 (BBB-) is not capped.

**Q7.** Issuers with an issuer-rating DG dated 2026 are listed in the JSON, with 28 entities. I excluded QA test records. Where a RESEARCH duplicate was rated, I used the RATINGS-system record ID (E1160 for E1161, E1169 for E1170, E1298 for E1299).

**Q8.** E08. A22 (2026-07-08) took it to RD and nothing later supersedes it.

**Q9.** 278. This counts distinct legal entities (merged by LEI) with at least one issuer-rating series in force on 2026-10-01. Withdrawn series, credit-opinion-only entities, VD (country ceiling only) and QA records are excluded. This is a long manual tally, so treat it as approximate.

**Q10.** Depends. E05's local-currency rating is BBB- (A13, investment grade), but its foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and A35 (2025-11-20) came later.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E17 is the same entity as E10, which held A- from A26 (2023) until A27 (2026-04-15).

**Q16.** No. It was BBB+ after A36, and A35 (RW) and A33 (AF) both kept BBB+.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement with the rating unchanged at A-.

**Q18.** Issuers whose latest action on 2026-10-01 was a Rating Watch Negative are listed in the JSON, with 32 entities. E1059 qualifies on its local-currency series (A1132), and E1209 stands for E1210 (A1442).

**Q19.** Issuers whose latest action on 2026-10-01 carried a Negative outlook are listed in the JSON, with 25 entities. E1160 stands for E1161 (A1344) and E1261 for E1262 (A1558).

**Q20.** No. A19 withdrew E07's rating on 2026-05-12 for commercial reasons, and a withdrawal is not a default.

**Q21.** The 35 entities in the JSON were rated at some point but ended in withdrawal (the WD actions, e.g. A19, A1002, A1013, A1046). E1001, E1253 and E1138 appear under their RATINGS IDs, although the withdrawals are on E1002, E1254 and E1138 respectively.

**Q22.** E08 only. A22 (RD) is the only RD or D rating in the data.

**Q23.** F2, from A04 (STIDR, 2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 66. I counted instruments whose latest INST action on 2026-10-01 was BBB- or better, excluding EX-only instruments.

**Q26.** A+, from A40 (LC).

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38 (CV, LTIDR FC).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** Eight entities have an FC rating exactly at their ceiling. The VD ceiling is BB (A12) and the CV ceiling is A (A37). E05, E1028, E1101, E1126 and E1236 are at BB. E15, E1039 and E1194 are at A.

**Q31.** No. Every FC rating for VD- or CV-domiciled entities is at or below its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09, and E09 has no parent.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ (A27, 2026-04-15).

**Q34.** No. E12 has no parent link in the data and only shares the "Halden" name, so the data does not support a link.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 331. There are 370 records, of which 13 are QA test records (E16 and E1340–E1351) and 26 are RESEARCH duplicates of RATINGS records (same LEI).

**Q38.** No. E06 and E13 have different LEIs and different countries (DE and US).

**Q39.** A, from A09 (2025-09-15, applying to the E02/E03 entity).

**Q40.** 66 GB-domiciled issuers held an issuer rating on 2026-10-01. This is a manual tally and should be treated as approximate.

**Q41.** None. E16 is a QA test record, so its actions are not rating actions.

**Q42.** LU. Domicile follows the RESEARCH record (E17, LU), while E10's RATINGS record says DE; the data conflicts.

**Q43.** 1, the E10/E17 entity.

**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency.

**Q45.** No. The ceiling caps foreign-currency issuer ratings. I07 is a local-currency note rated BBB- (A45), so the BB ceiling does not apply to it.

**Q46.** No. E11 only has a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only A47, an expected rating (EX), which is not a rating in force.

**Q48.** 106. There are 115 instruments, and 9 have only EX actions (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1228","E1307","E1186","E1034","E1112","E1167","E1160","E1263","E1285","E1169","E1255","E1093","E1080","E1057","E1053","E1144","E1051","E1294","E1300","E1229","E1298","E1243"]},
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
"Q18": {"issuers": ["E06","E1006","E1297","E1066","E1059","E1098","E1266","E1238","E1314","E1267","E1088","E1013","E1037","E1061","E1323","E1317","E1264","E1260","E1209","E1194","E1181","E1146","E1133","E1132","E1126","E1109","E1099","E1168","E1203","E1242","E1019","E1039"]},
"Q19": {"issuers": ["E01","E09","E1158","E1034","E1228","E1118","E1079","E1282","E1056","E1160","E1263","E1072","E1300","E1294","E1080","E1271","E1064","E1029","E1046","E1105","E1190","E1005","E1055","E1211","E1261"]},
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