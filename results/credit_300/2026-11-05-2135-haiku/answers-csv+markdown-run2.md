**Q1.** A-. Kestrel's rating set by A01 (2024-03-12) held until A02 (2025-06-20) downgraded it to BBB.

**Q2.** No. A03 (2026-02-10) affirmed BBB with a negative outlook, and the last downgrade was A02 in 2025.

**Q3.** No; BB+. I02 was assigned BBB (A23), then downgraded to BB+ by A07 (2025-06-20).

**Q4.** Positive (POS). E03 is the same LEI as E02, and its latest action is A09 (2025-09-15), an affirmation at A with a POS outlook.

**Q5.** E02 (Northwind Holdings) takes the risk, and I03 is rated A. I03 is guaranteed by E02, so it is rated in line with E02's A (A11).

**Q6.** Valdoria's country ceiling caps foreign-currency ratings. A12 sets the VD ceiling at BB, so E05's FC rating (A14, BB) sits at the ceiling. Its LC rating (A13, BBB-) is local-currency and not capped.

**Q7.** 31 issuers by DG action code (listed in JSON). Four DG actions did not lower the rating: E1064 (A1140) and E1294 (A1627) stayed level, E1051's second DG (A1104) stayed level, and E1229's second DG (A1481) raised BB to BB+. Withdrawals and Rating Watches are not counted.

**Q8.** E08 (Saxby Shipping), at RD since A22 (2026-07-08). It is the only RD or D rating in the data.

**Q9.** About 281 distinct issuers. I derived this by exclusion across all non-QA entities; treat it as approximate and verify with a script.

**Q10.** No. Its headline FC rating is BB (A14). Its LC rating is BBB- (A13), which is investment grade but local-currency only.

**Q11.** BBB+. A36 (2024-09-30) set BBB+; the later RW (A35) and AF (A33) did not change it.

**Q12.** A-. A34 (2023-01-15) assigned A-, and nothing changed it before 1 Jan 2024.

**Q13.** Once. A36 (2024-09-30) downgraded A- to BBB+. The Rating Watch in A35 is not a downgrade.

**Q14.** None. Halden Foods' first rating, A30 (BB-), is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. A26 (2023-05-01) set A-; the downgrade to BBB+ (A27) came later, in 2026.

**Q16.** No. BBB+ was set on 2024-09-30 (A36) and still held on 2026 (A33 AF, A35 RW), so it did not change after 1 Jan 2025.

**Q17.** No. A16 set A- and A17 (2026-09-03) is only a Rating Watch, not a downgrade.

**Q18.** 28 issuers, by the latest action on or before 1 Oct 2026 carrying RWN with no later action clearing it. E1209 is the RATINGS record; its RESEARCH duplicate is E1210.

**Q19.** 26 issuers, by the latest action on or before 1 Oct 2026 carrying a NEG outlook. Entities whose latest action was a Rating Watch with no outlook are excluded because their outlook is not recorded.

**Q20.** No. A19 (2026-05-12) withdrew the rating, and a withdrawal is not a default.

**Q21.** 32 entities had a rating that was withdrawn with no later rating action by 1 Oct 2026. The list was assembled by hand from the withdrawal actions.

**Q22.** E08 is the only entity ever in default (RD, A22).

**Q23.** F2. A04 (2026-02-10) affirmed the short-term rating at F2.

**Q24.** Yes. A03 (2026-02-10) rated the long-term issuer rating BBB, which is investment grade (outlook NEG).

**Q25.** About 66. I counted by hand the instruments whose latest rating on or before 1 Oct 2026 is BBB- or higher. Expected ratings (EX) are not ratings and are excluded.

**Q26.** A+. A40 (2024-03-01) assigned the LC rating A+.

**Q27.** A-. A42 (2024-03-01) assigned the instrument rating A-.

**Q28.** BBB+. A38 (FC) is BBB+. Corvenia's LC rating is A- (A39), which is a separate rating.

**Q29.** None. VD's only action is a Country Ceiling (A12, BB), which is not a sovereign issuer rating.

**Q30.** Eight entities sit exactly at their country's ceiling. VD's ceiling is BB (A12) and CV's is A (A37). The entities are E05, E1028, E1101, E1126, E1236, E15, E1039 and E1194.

**Q31.** No. No company's FC rating is above its country's ceiling on 1 Oct 2026.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank). I05 is guaranteed by E10 and is rated BBB+ (A29), in line with E10's BBB+ (A27).

**Q34.** No. Halden Foods (E12) has no parent. Halden Bank's chain ends at E09, so they are separate groups.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 distinct entities. This excludes QA records and counts LEI-duplicate RESEARCH records once, and it includes the sovereigns VD and CV.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. E02/E03's latest action is A09 (2025-09-15), an affirmation at A.

**Q40.** Not determined. This needs a full pass over the GB-domiciled entities' ratings, which I did not complete.

**Q41.** None. Brindle Capital (E16) is a QA record, and QA records must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile over the RATINGS record's DE.

**Q43.** 1: Halden Bank (E10/E17).

**Q44.** Yes. XVD is Valdoria's domestic currency, and I07 is issued by E05 (VD).

**Q45.** No. Local-currency debt is not capped by the ceiling, so the BB ceiling does not constrain I07 (BBB-, A45).

**Q46.** No. A46 is a credit opinion (CO), which is not a rating.

**Q47.** None. I08 has only an expected rating (EX, A47), which is not confirmed until an AS action.

**Q48.** 106. Of the 115 instruments, 9 have only EX actions and no rating.

Note on IDs: where an entity has a RESEARCH duplicate with the same LEI, I give the RATINGS record ID. Counts marked approximate or not completed above were derived by hand and should be checked against the CSVs.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 281},
  "Q10": {"investment_grade": "no"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06","E1194","E1203","E1126","E1132","E1133","E1146","E1181","E1209","E1238","E1242","E1260","E1266","E1267","E1297","E1314","E1317","E1323","E1013","E1037","E1061","E1059","E1098","E1099","E1109","E1088","E1168","E1019"]},
  "Q19": {"issuers": ["E01","E09","E1034","E1046","E1055","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1029","E1056","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E1160"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07","E1124","E1032","E1063","E1279","E1084","E1308","E1218","E1219","E1057","E1159","E1155","E1234","E1244","E1200","E1166","E1076","E1107","E1041","E1048","E1121","E1140","E1138","E1062","E1172","E1205","E1206","E1233","E1277","E1316","E1320","E1225"]},
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
  "Q40": {"count": null},
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