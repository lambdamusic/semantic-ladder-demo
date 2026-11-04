**Q1.** A-. E01's latest FC LTIDR before 2025-01-01 is A01 (A-), and the downgrade A02 came later, in June 2025.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with the outlook revised to NEG, which is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02 (SUB). A07 downgraded it to BB+, below the earlier A23 (BBB).

**Q4.** POS. E02 and E03 share an LEI, so they are one entity. Its latest action is A09 (2025-09-15), which affirmed A with a POS outlook.

**Q5.** E02, rated A. I03 is guaranteed by E02 (Northwind Holdings), whose latest LTIDR is A (A09).

**Q6.** The FC rating is capped by Valdoria's Country Ceiling of BB (A12), so E05's FC rating is BB (A14). The LC rating (A13, BBB-) is not capped.

**Q7.** 31 issuers had a DG on an issuer rating in 2026, listed in the JSON. QA records are excluded, and RESEARCH duplicates are mapped to their RATINGS record (E1170→E1169, E1161→E1160, E1299→E1298).

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, which is a default, and nothing later changes it.

**Q9.** 278. By latest action (counting an issuer if any LTIDR basis is still rated), 313 non-QA issuers were ever rated and 35 had withdrawn. Three entities have an action dated after their WD: E1115 (A1250), E1158 (A1338) and E1303 (A1649). I treated those as rated because the latest action wins.

**Q10.** Depends. E05's FC rating is BB (speculative grade, A14) and its LC rating is BBB- (investment grade, A13).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30 and nothing changed it before 2025-06-01.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36. A35 was a Watch, not a downgrade.

**Q14.** None. E12's first rating is A30 (2024-02-01), so it had no rating on 2024-01-01.

**Q15.** A-. E10 (and E17, the same LEI) was rated A- from A26, and the downgrade A27 only came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after A35 (Watch) and A33 (affirmation).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement with the rating unchanged.

**Q18.** 32 issuers have a latest action that is a Watch, listed in the JSON. E1059 and E1019 are on Watch only on their LC rating (A1132 and A1042).

**Q19.** 28 issuers, listed in the JSON. An outlook carries through a later Watch action that leaves the outlook blank (E1132, E1146).

**Q20.** No. E07 was rated BB and then withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07 plus 34 numbered entities, listed in the JSON, whose latest action is a withdrawal. E1279 and E1106 are excluded because their LC ratings are still active.

**Q22.** E08 only, rated RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The latest LTIDR (A03) is BBB.

**Q25.** 66 instruments. EX actions are not ratings, so those instruments are not counted.

**Q26.** A+, from A40.

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38.

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities. The ceilings are VD at BB (A12) and CV at A (A37). At BB are E05, E1028, E1101, E1126 and E1236. At A are E15, E1039 and E1194.

**Q31.** No. No VD entity has an FC rating above BB, and no CV entity has one above A.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose latest LTIDR is A27 (BBB+).

**Q34.** No. E12 has no parent and is not linked to E09, despite the similar name.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 331. There are 370 records. Removing 13 QA records and 26 same-LEI duplicates leaves 331; the two sovereigns have no LEI and are counted.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09.

**Q40.** 66 GB-domiciled issuers (list not itemised in the JSON).

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record (E10) takes precedence over the RESEARCH record (E17, LU).

**Q43.** 0. The only LU record is E17, and the RATINGS record for that LEI says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but a local-currency obligation is not capped.

**Q46.** No. E11 only has a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an Expected rating (A47), so it is unrated.

**Q48.** 106 instruments. Of 115 instruments, 9 have no assigned rating by 2026-10-01 (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1307","E1186","E1034","E1112","E1159","E1169","E1160","E1167","E1263","E1285","E1300","E1298","E1080","E1051","E1093","E1294","E1290","E1255","E1243","E1144","E1057","E1053","E1229","E1151"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1006","E1088","E1181","E1099","E1109","E1168","E1209","E1264","E1260","E1266","E1297","E1314","E1317","E1323","E1126","E1059","E1019","E1037","E1066","E1061","E1013","E1098","E1132","E1146","E1238"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1034","E1046","E1029","E1064","E1072","E1160","E1228","E1248","E1263","E1261","E1271","E1294","E1300","E1079","E1105","E1190","E1211","E1282","E1005","E1080","E1059","E1146","E1132"]},
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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```