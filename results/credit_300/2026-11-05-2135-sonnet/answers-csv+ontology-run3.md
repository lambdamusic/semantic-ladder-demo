**Q1.** A-. E01's LTIDR FC was assigned A- (A01) and not cut to BBB until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB with a Negative outlook (A03).

**Q3.** No, it is BB+. The 2031 note I02 is subordinated and was downgraded to BB+ (A07).

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action is the affirmation A09 with a POS outlook.

**Q5.** The holder takes E02's risk, rated A. I03 is guaranteed by E02, whose latest issuer rating is A (A09).

**Q6.** The Country Ceiling for VD is BB (A12), and it caps foreign-currency ratings but not local-currency ones. E05's FC rating is therefore BB (A14), while its LC rating is BBB- (A13).

**Q7.** 30 issuers had a 2026 downgrade, listed in the JSON. I treated records with the same LEI as one entity and ignored QA records. Withdrawal after a downgrade doesn't undo it (E1057, E1159).

**Q8.** E08 only. Its latest action is RD on 2026-07-08 (A22).

**Q9.** 278. Of 313 distinct non-QA entities that ever had an LTIDR, 35 ended in withdrawal. E1158, E1115 and E1303 have actions dated after their WD, so by date they are still rated; E1279 (LC) and E1106 (FC) keep one basis.

**Q10.** Depends. Its FC rating is BB (non-investment grade, A14) and its LC rating is BBB- (investment grade, A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions are Watch and affirmation.

**Q12.** A-. It was assigned A- on 2023-01-15 (A34), before the downgrade.

**Q13.** 1, the downgrade A36. The Watch (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. E10/E17 was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A35 is a Watch, A33 an affirmation).

**Q17.** No. E06's only 2026 action is a Watch (A17), which is not a downgrade.

**Q18.** 32 issuers, listed in the JSON, are on RWN on 2026-10-01, taking each entity's latest action. This includes E1019 and E1059, whose Watch is on the LC rating.

**Q19.** 26 issuers, listed in the JSON, have a Negative outlook. I carried the outlook forward through Watch actions, since a Watch doesn't revise it. I used FC ratings, and E1158 depends on its dated actions.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** 35 entities, listed in the JSON (RATINGS record IDs). Their latest LTIDR action is a withdrawal.

**Q22.** E08 only. It is the only entity ever rated RD or D (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. By latest INST action on 2026-10-01, 106 instruments are rated and 40 of those are below BBB-. Expected ratings (EX) don't count as rated.

**Q26.** A+ (A40).

**Q27.** A-. I06 is subordinated and carries the instrument rating A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities, listed in the JSON, are at their ceiling. The ceilings are A for CV (A37) and BB for VD (A12). E1245 is excluded because RESEARCH puts it in FR (E1246).

**Q31.** No. Every FC rating for a CV or VD entity is at or below its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's risk, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ in 2026 (A27).

**Q34.** No. E12 has no parent, so it is outside E09's group.

**Q35.** 3: E09, E10 (with E17, same LEI) and E11.

**Q36.** 2: E02 (with E03, same LEI) and E04.

**Q37.** 331. I excluded the QA records (E16 and E1340–E1351) and merged records sharing an LEI. Sovereigns and finance subsidiaries are included.

**Q38.** No. They have different LEIs (E06 vs E13).

**Q39.** A (A09, affirmed on E03).

**Q40.** 66. That is 73 GB-domiciled issuers that ever held an issuer rating, less 7 withdrawn.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH's record (E17) holds for domicile, overriding E10's DE.

**Q43.** 1: the Halden Bank entity (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. It is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 106 of the 115 instruments. Nine have only an EX action or an action dated after 2026-10-01.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1307","E1228","E1034","E1169","E1160","E1159","E1167","E1186","E1080","E1112","E1263","E1285","E1294","E1298","E1300","E1053","E1051","E1057","E1093","E1144","E1229","E1243","E1255","E1290"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1264","E1109","E1168","E1061","E1260","E1013","E1019","E1059","E1037","E1066","E1098","E1132","E1146","E1209","E1266","E1126","E1181","E1297","E1314","E1317","E1323","E1238","E1099"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1228","E1056","E1079","E1029","E1046","E1064","E1105","E1132","E1146","E1160","E1190","E1211","E1261","E1263","E1271","E1282","E1294","E1300","E1034","E1080","E1005","E1072"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1084","E1233","E1225","E1206","E1218","E1001","E1140","E1320","E1308","E1277","E1219","E1138","E1007","E1062","E1155","E1159","E1021","E1172","E1057","E1121","E1048","E1076","E1166","E1200","E1041","E1316","E1253","E1244","E1107","E1234","E1205"]},
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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```