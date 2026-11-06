**Q1.** A-. A01 assigned A- on 2024-03-12, and A02 did not downgrade it until 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation (BBB, outlook Negative), and a Negative outlook is not a downgrade.
**Q3.** No. I02 is subordinated and was downgraded to BB+ by A07 on 2025-06-20, so it is speculative grade.
**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and its latest action is A09 (2025-09-15, affirmed A, POS).
**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and E02's latest rating is A09 (A).
**Q6.** The Country Ceiling caps foreign-currency ratings but not local-currency ones. VD's ceiling is BB (A12), which matches E05's FC rating (A14), while its LC rating of BBB- (A13) is uncapped.
**Q7.** 31 entities had a downgrade (DG) recorded in 2026, listed in the JSON. Test records are excluded, and each duplicate is shown under its RATINGS record ID.
**Q8.** E08. A22 downgraded it to RD on 2026-07-08, and RD is a default.
**Q9.** 278 (my count). This counts entities whose LTIDR is in force on 2026-10-01, merging same-LEI records and excluding withdrawn and test records. E1279 is included because its LC rating is still in force after the FC withdrawal.
**Q10.** Depends. E05 is BBB- on a local-currency basis (investment grade) and BB on a foreign-currency basis (not).
**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the next action is not until 2025-11-20.
**Q12.** A-. A34 assigned A- on 2023-01-15, before the downgrade.
**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.
**Q14.** None. E12's first action, A30, is dated 2024-02-01.
**Q15.** A-. A26 set E10 at A- in 2023, and the downgrade (A27) is not until 2026-04-15.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after A35 (Watch) and A33 (affirmation).
**Q17.** No. E06's only 2026 action, A17, is a Rating Watch placement with the rating unchanged at A-.
**Q18.** 31 entities were on RWN, listed in the JSON. Each is an entity whose latest action was a Watch placement and had not been followed by a later action.
**Q19.** 24 entities had a Negative outlook, listed in the JSON. This uses each entity's latest action; where that action was a Watch placement with no outlook, I excluded the entity.
**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.
**Q21.** 35 entities, listed in the JSON, whose latest action on their foreign-currency rating is a withdrawal.
**Q22.** E08 only. It is the only entity with an RD or D rating (A22).
**Q23.** F2. A04 affirmed the short-term rating on 2026-02-10.
**Q24.** Yes. E01's LTIDR is BBB (A03).
**Q25.** 66 instruments. This counts the instruments whose latest non-EX action leaves a rating of BBB- or better.
**Q26.** A+. A40 assigned E15's LC rating.
**Q27.** A-. A42 rated I06, which is subordinated.
**Q28.** BBB+. A38 assigned CV's FC LTIDR.
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** 8 entities, listed in the JSON, whose FC rating equals the ceiling. Five are in VD (ceiling BB) and three in CV (ceiling A).
**Q31.** No. Every FC rating in VD and CV is at or below its ceiling, and E1245's country is FR once the RESEARCH record is applied.
**Q32.** E09. E11's parent is E10, whose parent is E09, which has no parent.
**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose latest rating is A27 (BBB+).
**Q34.** No. E12 has no parent link to E09 or E10.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 331. Of the 370 records, I removed the 26 RESEARCH duplicates (same LEI) and the 13 QA test records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A09 on E03, the same entity as E02).
**Q40.** 65 (my count). This uses GB domicile after the RESEARCH override and requires an issuer rating in force.
**Q41.** None. E16 is a QA test record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding the RATINGS record's DE.
**Q43.** 1. Only the E10/E17 entity (Halden Bank) is domiciled in Luxembourg.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where E05 is domiciled.
**Q45.** No. I07 is rated BBB- (A45), but local-currency debt is not capped by the ceiling.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47) and no assignment.
**Q48.** 106. There are 115 instruments, and 9 have only an Expected rating (EX) and no assignment.

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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1088","E1194","E1203","E1133","E1006","E1099","E1109","E1168","E1181","E1019","E1264","E1209","E1126","E1132","E1098","E1260","E1266","E1297","E1066","E1061","E1037","E1013","E1059","E1317","E1323","E1238","E1314"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1034","E1228","E1079","E1072","E1282","E1046","E1029","E1056","E1059","E1064","E1160","E1190","E1261","E1263","E1271","E1294","E1300","E1080","E1005","E1105"]},
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