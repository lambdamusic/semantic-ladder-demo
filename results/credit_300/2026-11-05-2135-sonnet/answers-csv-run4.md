**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02, downgrade to BBB) came on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with Negative outlook.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), downgraded to BB+ in A07 after A23 assigned BBB.

**Q4.** Positive. A09 (2025-09-15) affirmed A with Positive outlook. It sits on E03, which shares E02's LEI and is a duplicate record of Northwind Holdings.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, and A11 affirmed A in 2025.

**Q6.** The data does not state a reason. E05's foreign-currency rating is BB (A14), equal to Valdoria's country ceiling (VD, CC, A12), while its local-currency rating is BBB- (A13). That is consistent with the ceiling capping the foreign-currency rating.

**Q7.** 44 issuers had a downgrade action in 2026 (listed in the JSON). I counted issuer-level downgrades only, not instrument downgrades such as A29. I also excluded E1341's A1720, which is dated 2026-11-09, after today's date. Duplicate records are mapped to their canonical entity.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, with no later action.

**Q9.** 291. This counts canonical entities whose latest issuer-rating action as of 2026-10-01 is not a withdrawal, with duplicates merged. Three entities (E1115, E1158, E1303) have actions dated after a withdrawal, and I treated them as rated. E1279 is counted because its local-currency rating is still held after the foreign-currency withdrawal.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 (2025-11-20) came after 1 June 2025.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** Once. A36 is the only downgrade on E14.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 assigned A- in 2023, and the downgrade to BBB+ (A27) came on 2026-04-15. E17 is a duplicate record of E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35, A33), apart from a watch period.

**Q17.** No. A17 (2026-09-03) put E06 on Rating Watch Negative at A-, which is not a downgrade.

**Q18.** 31 issuers (listed in the JSON). I took each entity's latest action as of 2026-10-01 and kept those where it is a Rating Watch Negative action. E1019 and E1059 are on watch for their local-currency ratings only.

**Q19.** 35 issuers (listed in the JSON). I used the latest action's outlook, and entities whose latest action is a watch (blank outlook) are excluded. A1730, dated 2026-10-15, falls after the as-of date.

**Q20.** No. E07 was withdrawn for commercial reasons (A19), not defaulted.

**Q21.** 35 entities (listed in the JSON). Each was rated and then withdrawn by 2026-10-01.

**Q22.** E08 only. A22 is the only RD or D rating in the data.

**Q23.** F2, from A04 (STIDR).

**Q24.** Yes. The issuer rating is BBB (A03), which is investment grade.

**Q25.** 66. These are the instruments whose latest rating on 2026-10-01 was BBB- or higher. Instruments with an EX action are treated as no longer rated.

**Q26.** A+, from A40.

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a country-ceiling record (A12, BB) and no issuer rating.

**Q30.** E05, E1028, E1101, E1126, E1236, E15, E1039 and E1194. Valdoria's ceiling is BB (A12) and Corvenia's is A (A37). Each of these has a foreign-currency rating equal to its country's ceiling.

**Q31.** No. No Valdoria or Corvenia entity has a foreign-currency rating above its country's ceiling. Ceilings exist in the data only for VD and CV.

**Q32.** E09. E11 has parent E10 and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10 (downgraded to BBB+ in A27 and A29).

**Q34.** No. E12 has no parent and no link to E09, so only the name is shared.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 370 entity rows; 26 are duplicates by LEI (E03, E17 and 24 RESEARCH rows).

**Q38.** No. They have different LEIs and countries and no parent link.

**Q39.** A, from A08 and A09.

**Q40.** 74. These are canonical GB entities with an active issuer rating on 2026-10-01.

**Q41.** BB+, from A44 (2026-06-01).

**Q42.** DE. E10 in the RATINGS source says DE; the RESEARCH duplicate E17 says LU.

**Q43.** 0. The only LU row is E17, a duplicate of E10, whose authoritative record says DE.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's currency, and its BBB- rating matches E05's local-currency rating. The data does not define XVD, so this is inferred.

**Q45.** No. The BB ceiling constrains foreign-currency ratings, and I07 is a local-currency obligation, so its BBB- is not capped by it.

**Q46.** No. E11 has only a CO record (A46) and no LTIDR. Its notes are rated through the guarantor.

**Q47.** None. The only action on I08 is A47, an EX on 2026-09-01. I read EX as expired or ended, but the data does not define it.

**Q48.** 106 instruments held a rating on 2026-10-01. The 8 instruments with an EX action, whether before or after that date, are excluded.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1064","E1163","E1058","E1213","E1228","E1350","E1346","E1347","E1307","E1034","E1186","E1159","E1169","E1160","E1167","E1112","E1080","E1093","E1051","E1053","E1057","E1229","E1144","E1263","E1285","E1294","E1298","E1300","E1340","E1342","E1343","E1344","E1345","E1348","E1349","E1351","E1255","E1243","E1151","E1290"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 291},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1118","E1158","E1350","E1347","E1228","E1056","E1034","E1263","E1046","E1029","E1080","E1064","E1160","E1248","E1261","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1348","E1349","E1351","E1105","E1079","E1190","E1188","E1211","E1005"]},
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
"Q37": {"count": 344},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 74},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```