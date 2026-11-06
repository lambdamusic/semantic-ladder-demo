**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, came on 2025-06-20.
**Q2.** No. The only 2026 action is A03, an affirmation at BBB with a Negative outlook, which is not a downgrade.
**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ by A07, after being assigned BBB by A23.
**Q4.** Positive. E03 shares E02's LEI, and A09 (2025-09-15) affirmed A with a POS outlook.
**Q5.** The guarantor E02, Northwind Holdings. I03 is guaranteed by E02 and is rated A (A10, A11).
**Q6.** The Country Ceiling for Valdoria (VD) is BB (A12) and caps foreign-currency ratings, so E05's FC rating is BB (A14). Its local-currency rating is not capped and sits at BBB- (A13). No JSON field for this question.
**Q7.** 31 issuers had a downgrade (DG) on their issuer rating in 2026 (e.g. E08 A21/A22, E10 A27). QA records were ignored. Duplicate records were merged to their RATINGS ID: E1161→E1160, E1170→E1169 and E1299→E1298.
**Q8.** E08. A22 downgraded it to RD (restricted default) on 2026-07-08, and RD is a default.
**Q9.** 278. This counts distinct, non-QA entities whose latest issuer-rating action is not a withdrawal, merging records with the same LEI. Because the latest action governs, I counted E1158 and E1303 as rated even though a withdrawal precedes later actions, and E1279 as rated through its local-currency rating. Finance subsidiaries (FINSUB, only credit opinions) and VD (Country Ceiling only) are not counted. This is a hand count, so treat it as approximate.
**Q10.** Depends. E05's FC rating is BB (speculative) but its LC rating is BBB- (investment grade) (A13, A14).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the Watch in A35 came later.
**Q12.** A-. A34 assigned it on 2023-01-15.
**Q13.** One. Only A36 is a DG for E14.
**Q14.** None. E12 was first rated on 2024-02-01 (A30).
**Q15.** A-. A26 assigned it to E10; the downgrade A27 came on 2026-04-15.
**Q16.** No. It was BBB+ after A36 and is BBB+ now (A35, A33).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch.
**Q18.** 32 issuers were on Rating Watch Negative: those whose latest action was a Watch (RW). Examples are E06 (A17) and E1267 (A1570).
**Q19.** 25 issuers had a Negative outlook: those whose latest action carried NEG. Examples are E01 (A03) and E09 (A25). I treated a Watch action, which has no outlook, as replacing the earlier outlook, so for example E1146 is excluded.
**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), which is not a default.
**Q21.** 35 entities. Each has a withdrawal (WD) as its latest action on every basis and was not re-rated later.
**Q22.** Only E08. A22 set RD; no other record shows RD or D.
**Q23.** F2 (A04).
**Q24.** Yes, BBB (A03).
**Q25.** 66. Counted from each instrument's latest INST action up to 2026-10-01, with expected-rating (EX) actions treated as unrated. Hand count, so treat as approximate.
**Q26.** A+ (A40).
**Q27.** A- (A42), below the CV ceiling of A (A37).
**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the issuer rating.
**Q29.** None. VD has only a Country Ceiling (A12).
**Q30.** Eight entities: E05, E1028, E1101, E1126, E1236 (all FC BB, ceiling BB) and E15, E1039, E1194 (all FC A, ceiling A).
**Q31.** No. No VD or CV company has an FC rating above its ceiling. E1246 (the RESEARCH record for Gater Holdings) places it in FR.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The guarantor E10, Halden Bank. I05 is guaranteed by E10 and rated BBB+ (A29).
**Q34.** No. E12 has no parent link, so it is not in E09's group.
**Q35.** Three: E09, E10 and E11. E17 is E10's duplicate record.
**Q36.** Two: E02 and E04. E03 is E02's duplicate record.
**Q37.** 331. That is 370 records, less 13 QA records and 26 duplicate records.
**Q38.** No. They have different LEIs (E06 549300AMVE…, E13 815600O8X8…).
**Q39.** A (A09).
**Q40.** 65. Counted GB-domiciled distinct entities with an issuer rating that was not withdrawn.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding DE on E10.
**Q43.** One, the Halden Bank entity (E17/E10).
**Q44.** Yes. I07 is in XVD, VD's domestic currency, and E05 is domiciled in VD.
**Q45.** No. Local-currency debt is not capped by the ceiling.
**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not a rating.
**Q47.** None. A47 is only an Expected rating (EX) for I08; it is not assigned.
**Q48.** 106 instruments (7 of I01–I08 plus 99 of I1001–I1107). The 8 with only an EX action, or none by the cutoff, are excluded. Hand count.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1213","E1307","E1163","E1228","E1034","E1080","E1051","E1053","E1057","E1144","E1159","E1160","E1167","E1169","E1186","E1243","E1255","E1263","E1285","E1298","E1300","E1290","E1294","E1112","E1093","E1229","E1151"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1109","E1264","E1168","E1019","E1209","E1260","E1066","E1037","E1061","E1126","E1323","E1297","E1098","E1013","E1132","E1146","E1317","E1314","E1266","E1238","E1181","E1059","E1099"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1079","E1228","E1282","E1160","E1261","E1263","E1271","E1029","E1046","E1034","E1056","E1080","E1064","E1072","E1190","E1211","E1294","E1105","E1005","E1300","E1188"]},
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