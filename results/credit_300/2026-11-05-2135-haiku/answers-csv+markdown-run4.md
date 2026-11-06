**Q1.** A-. A01 (2024-03-12, A-) is the latest action before 1 Jan 2025; A02 (DG to BBB) came on 2025-06-20.

**Q2.** No. The 2026 actions on E01 are affirmations (A03, A04), and the only downgrade is A02 in 2025.

**Q3.** No, BB+. I02 (6.25% 2031) was downgraded from BBB to BB+ by A07 on 2025-06-20.

**Q4.** POS. The latest Northwind Holdings action is A09 (2025-09-15, affirmed A, outlook POS), recorded under E03, which shares E02's LEI.

**Q5.** E02, A. I03 (Northwind Finance 3.75% 2030) is guaranteed by E02, so the holder takes E02's risk; its instrument rating is A (A11).

**Q6.** Valdoria Telecom's FC rating (BB, A14) is capped by the Valdoria Country Ceiling (BB, A12), which applies to foreign-currency ratings. Its LC rating (BBB-, A13) is not capped because it is domestic-currency.

**Q7.** E08, E10, E1034, E1051, E1053, E1057, E1058, E1063… (see JSON for the full list of 31). These are the non-QA issuers with an LTIDR downgrade (DG) dated in 2026.

**Q8.** E08. Its A22 (2026-07-08) is an RD for a completed distressed debt exchange, and no later action follows.

**Q9.** 277. Of 313 non-QA entities with any LTIDR action, 36 have a latest pre-1-Oct action that is a withdrawal (see Q21). This is a manual tally.

**Q10.** No. Valdoria Telecom's headline FC rating is BB (A14); its LC BBB- is investment grade but is not the headline.

**Q11.** BBB+. DG A36 (2024-09-30) set BBB+, and no action came until RW on 2025-11-20.

**Q12.** A-. A34 (2023-01-15) assigned A- and nothing changed it before 2024.

**Q13.** 1. Marlow Utilities' only downgrade is A36 (2024-09-30).

**Q14.** None. Halden Foods' first rating, A30, was assigned on 2024-02-01, after 1 Jan 2024.

**Q15.** A-. Halden Bank's A26 (2023-05-01) was the rating until DG to BBB+ on 2026-04-15 (A27).

**Q16.** No. The rating stayed BBB+ from A36 onward; A35 is a watch and A33 an affirmation.

**Q17.** No. Orrin Bank's only 2026 action is RW (A17, 2026-09-03), which is not a downgrade.

**Q18.** 32 issuers have a Rating Watch Negative still open on 1 Oct 2026 (see JSON). I treated a watch as open until a later action on that entity resolves it.

**Q19.** 29 issuers have a Negative outlook on 1 Oct 2026, based on each entity's latest explicit FC outlook (see JSON).

**Q20.** No. Pellam Retail was withdrawn (A19), and withdrawal is not a default.

**Q21.** 36 entities had a rating that was withdrawn with no later rating action by 1 Oct 2026 (see JSON).

**Q22.** E08. It is the only entity with an RD or D rating.

**Q23.** F2. STIDR A04 (2026-02-10).

**Q24.** Yes. Kestrel's FC issuer rating is BBB (A02, A03).

**Q25.** 66. Of the 106 instruments rated on 1 Oct 2026, 66 have a latest rating of BBB- or higher.

**Q26.** A+. Corvenia Power's only LC action is A40 (AS A+, 2024-03-01).

**Q27.** A-. I06 (Corvenia 7.10% 2032) was assigned A- by A42 (2024-03-01).

**Q28.** BBB+. The Republic of Corvenia's FC rating is A38 (AS BBB+, 2024-01-01).

**Q29.** None. Valdoria has only a Country Ceiling (A12), which is not a sovereign issuer rating.

**Q30.** E05, E1028, E1101, E1126, E1236 (at the VD ceiling, BB), and E15, E1194 (at the CV ceiling, A).

**Q31.** No. No company's FC rating sits above its domicile's ceiling on 1 Oct 2026.

**Q32.** E09. Halden Leasing → Halden Bank AG (E10) → Halden Group plc (E09), which has no parent.

**Q33.** E10, BBB+. I05 (Halden Leasing 2.90% 2028) is guaranteed by E10, and its current rating is BBB+ (A29).

**Q34.** No. Halden Foods has no parent, and Halden Bank's ultimate parent is E09.

**Q35.** 3. The Halden group is E09, E10 and E11.

**Q36.** 2. The Northwind group is E02 and E04.

**Q37.** 331. That is 370 records, less 26 duplicate-LEI pairs and 13 QA records, and includes the two sovereigns (329 excluding them).

**Q38.** No. Orrin Bank AG (LEI 549300AMVE3VRVG7HK43) and Orrin Bancorp (LEI 815600O8X8K2F154N214) have different LEIs.

**Q39.** A. Northwind Holdings' latest FC rating is A (A09, AF, 2025-09-15).

**Q40.** 65. This is a manual tally of GB-domiciled entities holding a rating on 1 Oct 2026, using RESEARCH domicile where records disagree.

**Q41.** None. Brindle Capital is a QA record, which must be ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile, overriding RATINGS (DE).

**Q43.** 1. Only Halden Bank (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 is denominated in XVD, the Valdorian domestic currency.

**Q45.** No. Domestic-currency debt is not subject to the ceiling, so the BBB- rating is not capped at BB.

**Q46.** No. Halden Leasing has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an expected rating (EX, A), which is not an assigned rating.

**Q48.** 106. Of 115 instruments, 9 have only EX actions and no assigned rating.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1163","E1167","E1169","E1160","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 277},
  "Q10": {"investment_grade": "no"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06","E1267","E1194","E1203","E1099","E1088","E1133","E1132","E1109","E1098","E1059","E1168","E1181","E1209","E1242","E1264","E1266","E1297","E1314","E1317","E1323","E1013","E1019","E1061","E1066","E1126","E1146","E1260","E1238","E1037","E1039","E1006"]},
  "Q19": {"issuers": ["E01","E09","E1158","E1190","E1188","E1079","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E1160","E1118","E1211","E1034","E1029","E1132","E1146","E1105","E1080","E1064","E1072","E1046","E1056","E1055","E1059"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07","E1124","E1032","E1063","E1233","E1001","E1279","E1218","E1206","E1084","E1205","E1121","E1041","E1062","E1140","E1200","E1225","E1107","E1076","E1048","E1155","E1159","E1057","E1007","E1021","E1253","E1138","E1166","E1244","E1316","E1277","E1172","E1308","E1234","E1320","E1219"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": 66},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E15","E1194"]},
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

**Caveats**
- Nular (E1158), Lunor (E1303) and Piren (E1115) each have a later rating action after a withdrawal. I counted them as rated, which conflicts with the ontology's "no rating after withdrawal" rule.
- Several actions are dated after today (2026-11-05), such as A1011, A1029 and A1078. They are instrument expected ratings and do not change any answer here.
- Counts Q9, Q18, Q19, Q25, Q40 and Q48 are manual tallies across hundreds of records and may contain small errors.