**Q1.** A-. E01's LTIDR FC was set to A- by A01 (2024-03-12) and not changed until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook, which is not a downgrade.

**Q3.** No. The 2031 note is I02, a subordinated note, and A07 downgraded it to BB+ on 2025-06-20, which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15, affirmed at A, Positive).

**Q5.** Northwind Holdings (E02). I03 is guaranteed by E02, whose current rating is A (A09).

**Q6.** Valdoria's Country Ceiling is BB (A12, on VD). Valdoria Telecom's FC rating (A14, BB) is capped at that level, while its LC rating (A13, BBB-) is not capped.

**Q7.** 31 issuers had an LTIDR downgrade in 2026. Records E1170, E1161 and E1299 are RESEARCH duplicates, so they are reported under E1169, E1160 and E1298. QA records are ignored. E10 is included because A27 downgraded its LTIDR.

**Q8.** E08 only. A22 (2026-07-08) moved it to RD, which is a default.

**Q9.** 277. This counts distinct entities (LEI-merged, QA excluded) whose latest LTIDR, or an LTIDR on at least one currency basis, is not WD on 2026-10-01. Entities with a withdrawal as their latest action are excluded. E1158 and E1115 have a rating action dated after an earlier WD, and I counted them as rated by the latest-action rule.

**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and nothing changed it before 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1. The only downgrade is A36. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 and E17 share an LEI. A26 set A- in 2023, and the downgrade A27 came only on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement, which is not a downgrade.

**Q18.** 32 issuers have a latest action that is a Rating Watch Negative placement. Where two bases exist, I counted the issuer if the latest FC or LC action is on Watch. E1210 is reported as E1209, its RATINGS record.

**Q19.** 21 issuers had a Negative outlook on their latest action. Issuers whose latest action is a Watch placement have no outlook on that row, so they are excluded.

**Q20.** No. E07's rating was withdrawn (A19, WD), and a withdrawal is not a default.

**Q21.** 35 entities. Each had an issuer rating whose latest action is a withdrawal. E1279 and E1106 are excluded because they still have an LC rating.

**Q22.** E08 only. A22 is the only RD or D rating in the data.

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. E01's current LTIDR is BBB (A03).

**Q25.** 66. This counts instruments whose latest INST action is an AS, AF, UG or DG at BBB- or above. Instruments with only an EX action are unrated.

**Q26.** A+ (A40, E15 LC).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38, CV FC).

**Q29.** None. VD carries only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities. The ceilings are BB for VD (A12) and A for CV (A37). The matches are E05, E1028, E1101, E1126 and E1236 for VD, and E15, E1039 and E1194 for CV.

**Q31.** No. No VD or CV company has a latest FC rating above its ceiling; E1039 and E1194 sit exactly at A, and E1039's AA- is local-currency, which is not capped.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** Halden Bank (E10), the guarantor of I05. It is rated BBB+ (A27).

**Q34.** No. E12 has no parent link, and the shared name does not make it part of the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 331. The file has 370 records. I removed 13 QA records (E16 and E1340–E1351) and 26 same-LEI RESEARCH duplicates.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09 on E03, the same entity as E02).

**Q40.** 66. These are the active GB-domiciled entities from the Q9 count, using the RATINGS country.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** DE. The RATINGS record E10 holds, and the RESEARCH record E17 saying LU is overridden.

**Q43.** 0. LU appears only on the RESEARCH duplicate E17, and the RATINGS record says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, and it is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), so it is unrated.

**Q48.** 106. There are 115 instruments, and 9 have only an EX action: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1186","E1034","E1228","E1159","E1112","E1169","E1160","E1167","E1298","E1285","E1294","E1300","E1263","E1080","E1051","E1053","E1057","E1093","E1144","E1255","E1290","E1307","E1243","E1151","E1229"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 277},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1088","E1194","E1203","E1133","E1006","E1264","E1099","E1168","E1019","E1209","E1109","E1260","E1181","E1146","E1013","E1037","E1066","E1061","E1059","E1098","E1126","E1238","E1266","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1228","E1034","E1046","E1056","E1029","E1059","E1079","E1160","E1261","E1263","E1271","E1248","E1282","E1294","E1300","E1080","E1190"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1225","E1308","E1206","E1140","E1001","E1138","E1320","E1277","E1219","E1159","E1244","E1107","E1121","E1316","E1155","E1172","E1007","E1021","E1076","E1062","E1048","E1253","E1205","E1234","E1041","E1057","E1166","E1200"]},
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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```