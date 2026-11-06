**Q1.** A-. E01's LTIDR (FC) was assigned A- on 2024-03-12 (A01) and not changed until the 2025-06-20 downgrade (A02).

**Q2.** No. E01's only 2026 action is the 2026-02-10 affirmation at BBB (A03); the downgrade was in 2025 (A02).

**Q3.** No, it is BB+. The 2031 note I02 (subordinated) was cut from BBB to BB+ on 2025-06-20 (A23, A07).

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action is A09 (affirmed A, POS, 2025-09-15).

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes E02's credit risk, which is A per A09 (I03 itself is also A, A11).

**Q6.** The Country Ceiling for VD is BB (A12), and E05's FC rating is capped there (A14). The LC rating is BBB- (A13), which the ceiling does not constrain.

**Q7.** Thirty entities had an issuer-rating downgrade dated 2026, listed in the JSON. The QA test records are excluded, and each duplicate cluster is named by its RATINGS record.

**Q8.** E08. It was cut to RD on 2026-07-08 (A22) and is the only RD/D rating.

**Q9.** 278. This counts distinct entities (merged by LEI) whose latest issuer-rating series is not withdrawn and which are not test records. It includes the sovereign CV.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (not, A14).

**Q11.** BBB+. E14 was downgraded on 2024-09-30 (A36), and the 2025-11-20 RW (A35) did not change the rating.

**Q12.** A-, from A34 (assigned 2023-01-15).

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating action is 2024-02-01 (A30).

**Q15.** A-. E10 and E17 share an LEI, and the A- from A26 stood until the 2026-04-15 downgrade (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33); the watch (A35) did not change the rating.

**Q17.** No. E06's only 2026 action is the Rating Watch Negative on 2026-09-03 (A17) at A-.

**Q18.** Thirty-two entities had a latest rating action that was a Rating Watch placement, listed in the JSON. Entities where a later affirmation, upgrade, downgrade or withdrawal cleared the watch are excluded.

**Q19.** Twenty-four entities had a latest action with a Negative outlook, listed in the JSON. I treated an RW action as carrying no outlook, so entities whose latest action is an RW are excluded.

**Q20.** No. The E07 rating was withdrawn on 2026-05-12 (A19) and was never RD/D.

**Q21.** Thirty-five entities, listed in the JSON, were rated but had every issuer-rating series withdrawn by 1 October 2026 (WD actions such as A19).

**Q22.** E08 only (RD, A22).

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. These are the instruments whose latest INST rating is in force and investment grade; EX (expected) ratings do not count.

**Q26.** A+. E15's LC rating was assigned on 2024-03-01 (A40).

**Q27.** A-, from A42.

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (BB, A12), which is not an issuer rating.

**Q30.** Eight entities. The VD ceiling is BB and the CV ceiling is A, and E05, E1028, E1101, E1126 and E1236 sit at BB while E15, E1039 and E1194 sit at A.

**Q31.** No. No VD or CV entity has an FC rating above its ceiling (BB and A respectively).

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No, as far as the data shows. E12 has no parent and no shared LEI with the Halden entities; only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10, so it is the same entity.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 331. I took the 370 entity rows, removed 13 QA test records and 26 RESEARCH rows that duplicate a RATINGS LEI, and kept the sovereigns.

**Q38.** No. E06 and E13 have different LEIs and countries, so only the names are similar.

**Q39.** A (A09).

**Q40.** 66, counting distinct GB-domiciled entities with a non-withdrawn issuer rating.

**Q41.** None. E16 is a QA test record, so its ratings (A43, A44) are not in force.

**Q42.** LU. The RESEARCH record E17 gives LU, which overrides the RATINGS record's DE under the domicile rule.

**Q43.** 1, the E10/E17 entity.

**Q44.** Yes. I07 is in XVD and its issuer E05 is domiciled in VD, whose domestic currency is XVD.

**Q45.** No. The ceiling applies to FC ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an expected rating (A47, EX), which is not in force.

**Q48.** 106. There are 115 instruments, and 9 have only an expected rating: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1307","E1159","E1186","E1034","E1285","E1300","E1112","E1169","E1167","E1080","E1051","E1053","E1144","E1057","E1263","E1298","E1160","E1294","E1093","E1255","E1243","E1229","E1290"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1194","E1203","E1133","E1088","E1168","E1109","E1264","E1260","E1099","E1013","E1019","E1059","E1061","E1066","E1037","E1126","E1132","E1146","E1181","E1209","E1266","E1297","E1314","E1317","E1323","E1098","E1238"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1005","E1079","E1228","E1034","E1282","E1029","E1046","E1190","E1261","E1263","E1294","E1248","E1271","E1300","E1072","E1080","E1053","E1059","E1064"]},
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