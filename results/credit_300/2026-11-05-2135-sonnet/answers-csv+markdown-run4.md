**Q1.** A-. E01's last action on or before that date is A01 (2024-03-12, A-). The downgrade to BBB (A02) came in June 2025.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook.

**Q3.** No, BB+. The 2031 note I02 is subordinated. A23 assigned BBB, then A07 downgraded it to BB+.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes E02 (Northwind Holdings) risk, rated A. I03 is guaranteed by E02, and its latest rating action (A09) affirmed A.

**Q6.** Valdoria's Country Ceiling (A12) is BB. It caps E05's foreign-currency rating at BB (A14), while the local-currency rating (A13) is BBB- because it isn't capped.

**Q7.** 30 issuers had a downgrade (DG) action in 2026. I used canonical RATINGS IDs for research duplicates, and I excluded QA records and instrument downgrades such as I05.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and no later action changes that.

**Q9.** 278 distinct issuers. This counts entities whose latest long-term issuer rating action is not a withdrawal, with duplicate records merged by LEI. Cases where a later action follows a withdrawal (E1158, E1115, E1303) count as rated, and E1279 counts because its local-currency rating survives. Credit opinions (CO), Country Ceilings (CC) and QA records are excluded. This was a long hand count, so treat it as approximate.

**Q10.** No. The foreign-currency headline rating (A14) is BB. Only the local-currency rating (A13, BBB-) is investment grade.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and nothing changed it before 1 June 2025.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came later.

**Q13.** 1. Only A36 is a DG for E14. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating (A30) is dated 2024-02-01.

**Q15.** A-. E10's A26 holds until A27 on 2026-04-15, and E17 is just the research duplicate of E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now. The Watch (A35) and the affirmation (A33) changed nothing.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch, which is not a downgrade.

**Q18.** 32 issuers were on Rating Watch Negative. Each has a Watch (RW) as its latest rating action for that basis, with no later action clearing it. The list is in the JSON block.

**Q19.** 27 issuers had a Negative outlook. Each has a latest action with a NEG outlook. Where the latest action is a Watch or withdrawal with no outlook, I carried forward the previous outlook. E1059 is counted on its foreign-currency outlook.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19, commercial reasons). A withdrawal says nothing about default.

**Q21.** 35 entities. Each had a rating and then a withdrawal as its latest action. The list is in the JSON block.

**Q22.** E08 only. A22 is the only RD or D rating in the data.

**Q23.** F2. A04 (STIDR) affirmed F2.

**Q24.** Yes. The foreign-currency issuer rating is BBB (A03), which is investment grade.

**Q25.** 66 instruments. Of the 106 rated instruments, 40 are below investment grade. Instruments with only an expected rating (EX) are unrated, and I used each instrument's own rating actions, including the guaranteed ones.

**Q26.** A+. A40 assigned E15's local-currency rating.

**Q27.** A-. A42 rated I06 (subordinated, in USD). That is below the CV ceiling of A (A37).

**Q28.** BBB+. A38 is CV's foreign-currency issuer rating. The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), and no issuer rating.

**Q30.** Eight entities sit exactly at their ceiling: E05, E1028, E1101, E1126, E1236 (VD, BB) and E15, E1039, E1194 (CV, A). E1245 is excluded because the research record puts its domicile in FR.

**Q31.** No. No foreign-currency rating exceeds BB for Valdoria entities or A for Corvenia entities.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10 (Halden Bank) risk, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ by A27.

**Q34.** No. E12 has no parent and sits outside E09's group, which contains E10.

**Q35.** 3. The group is E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2. The group is E02 (E03 is a duplicate record) and E04.

**Q37.** 331. There are 370 records, less 26 same-LEI duplicates and 13 QA records. This counts the two sovereigns.

**Q38.** No. Their LEIs differ (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A. A09 affirmed A, and E03 is the same entity as E02.

**Q40.** 66 distinct GB-domiciled issuers, after removing withdrawn ones and the QA record.

**Q41.** None. E16 is a QA test record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, and it says LU while E10 says DE.

**Q43.** 1. Only the Halden Bank entity (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 is in XVD, the Valdorian dollar, which is E05's domestic currency.

**Q45.** No. I07 is BBB- (A45) against a BB ceiling, but it is local-currency debt and the ceiling doesn't cap it.

**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which isn't an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), so it stays unrated.

**Q48.** 106. There are 115 instruments, and 9 have only an expected rating (EX).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1228","E1307","E1186","E1034","E1159","E1169","E1160","E1285","E1298","E1263","E1080","E1051","E1167","E1112","E1300","E1294","E1290","E1093","E1057","E1053","E1144","E1255","E1243","E1229"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 278},
"Q10": {"investment_grade": "no"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1088","E1194","E1203","E1133","E1099","E1168","E1019","E1059","E1264","E1209","E1126","E1260","E1266","E1238","E1013","E1037","E1061","E1066","E1098","E1109","E1132","E1146","E1181","E1297","E1317","E1323","E1314"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1034","E1146","E1228","E1282","E1261","E1263","E1294","E1271","E1132","E1190","E1029","E1056","E1046","E1053","E1072","E1079","E1064","E1160","E1248","E1059","E1055","E1005","E1188"]},
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