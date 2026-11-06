**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01) and not changed until A02 on 2025-06-20.
**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04.
**Q3.** No, BB+. The 2031 note is I02, which A07 downgraded to BB+ on 2025-06-20.
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and A09 (2025-09-15) is the latest action, giving POS.
**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest LTIDR FC is A (A08, A09).
**Q6.** The Country Ceiling for VD (A12) is BB. It caps E05's foreign-currency rating (A14, BB), while the local-currency rating (A13, BBB-) is not capped.
**Q7.** Entities with a DG on their issuer rating in 2026, QA records excluded and duplicate records mapped to the RATINGS record. The list is in the JSON.
**Q8.** E08. A22 on 2026-07-08 set RD, which is a default.
**Q9.** 277. This counts distinct entities (by LEI) whose latest LTIDR action on or before 2026-10-01 is not a withdrawal. I followed the latest action literally, so E1158, E1303 and E1115 count as rated even though they had WD records earlier. E1279 counts because its LC rating remains.
**Q10.** Depends. E05's FC rating is BB (A14), which is not investment grade, while its LC rating is BBB- (A13), which is.
**Q11.** BBB+. A36 downgraded E14 to BBB+ in 2024 and nothing changed it before 2025-06-01.
**Q12.** A-, from A34.
**Q13.** One time (A36).
**Q14.** None. E12's first action is on 2024-02-01 (A30).
**Q15.** A-. E10 and E17 are one entity, and A26 holds until the downgrade on 2026-04-15 (A27).
**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35 and A33 did not change it).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch.
**Q18.** The list is in the JSON. It includes E1019 and E1059, whose local-currency ratings are on watch.
**Q19.** The list is in the JSON. I took the latest stated outlook and carried it through RW rows, which have a blank outlook. That adds E1146 and E1132.
**Q20.** No. E07's rating was withdrawn (A19), which is not a default.
**Q21.** The list is in the JSON. These are the entities whose last issuer rating action before 2026-10-01 was a withdrawal.
**Q22.** E08 only.
**Q23.** F2 (A04).
**Q24.** Yes. E01's LTIDR is BBB.
**Q25.** 66. This counts instruments whose latest INST action on or before 2026-10-01 is BBB- or better; expected-rating (EX) rows are ignored.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.
**Q30.** E05, E1028, E1101, E1126 and E1236 are at the VD ceiling of BB. E15, E1039 and E1194 are at the CV ceiling of A. E1245 is excluded because its RESEARCH record places it in FR.
**Q31.** No. No entity's FC rating exceeds its country's ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The holder takes E10's credit risk, rated BBB+ (A27). I05 is guaranteed by E10.
**Q34.** No. E12 has no parent, so it is not in the E09 group.
**Q35.** 3 entities: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2 entities: E02 and E04. E03 is the same entity as E02.
**Q37.** 331. There are 370 records, of which 13 are QA, leaving 357. Of those, 26 are duplicates of the same LEI, which leaves 331, including the two sovereigns.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A09).
**Q40.** 65. This counts GB-domiciled entities with an active issuer rating on 2026-10-01.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding DE on E10.
**Q43.** 1, the Halden Bank entity (E10/E17).
**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.
**Q45.** No. It is local-currency debt, so the ceiling does not apply, and it is rated BBB- (A45).
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating, and its debt is guaranteed by E10.
**Q47.** None. I08 has only an expected rating (A47), which is not a rating.
**Q48.** 106. Nine instruments have no rating: I08 and the eight with only an EX action (I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1307","E1034","E1186","E1159","E1167","E1169","E1160","E1112","E1093","E1080","E1057","E1051","E1263","E1285","E1290","E1298","E1300","E1294","E1255","E1243","E1144","E1053","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1146","E1099","E1168","E1019","E1181","E1209","E1260","E1297","E1098","E1264","E1109","E1266","E1037","E1013","E1061","E1314","E1317","E1126","E1059","E1066","E1238","E1323","E1132"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1079","E1228","E1056","E1034","E1029","E1046","E1263","E1271","E1248","E1261","E1190","E1294","E1300","E1005","E1080","E1160","E1211","E1072","E1064","E1146","E1132"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1076","E1084","E1234","E1233","E1225","E1206","E1121","E1007","E1172","E1155","E1159","E1166","E1200","E1205","E1219","E1244","E1253","E1277","E1308","E1316","E1320","E1138","E1140","E1107","E1048","E1057","E1062","E1041","E1021","E1001"]},
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