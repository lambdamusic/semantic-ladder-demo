**Q1.** A-. LTIDR FC was A- from A01 (2024-03-12) until A02 (2025-06-20).
**Q2.** No. The only 2026 action is A03, an affirmation at BBB.
**Q3.** No, BB+. I02 is subordinated and was cut to BB+ in A07, which supersedes A23 (BBB).
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) affirmed A with a POS outlook.
**Q5.** The guarantor, E02 (Northwind Holdings), rated A. I03 is issued by E4 but guaranteed by E02, and A10/A11 rate it A.
**Q6.** The data gives no stated reason. It only shows E05 FC BB (A14) against LC BBB- (A13), with FC equal to Valdoria's BB country ceiling (A12).
**Q7.** 43 issuers had a 2026 downgrade (DG) action. Duplicate research records are mapped to their RATINGS record, and E1341's DG is dated 2026-11-09, after today.
**Q8.** E08. A22 (2026-07-08) moved it to RD.
**Q9.** 290. This counts distinct entities (deduplicated by LEI) with a live LTIDR on 2026-10-01, excluding withdrawals. E1115, E1158 and E1303 have actions dated after their WD, so I followed the dates.
**Q10.** Depends. It is investment grade in local currency (BBB-, A13) but not in foreign currency (BB, A14).
**Q11.** BBB+. A36 downgraded E14 on 2024-09-30.
**Q12.** A-. This is the A34 assignment.
**Q13.** One. A36 is the only DG; A35 is a watch and A33 an affirmation.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. E10 (E17 is a duplicate) was assigned A- in A26, and the downgrade A27 came only on 2026-04-15.
**Q16.** No. It was BBB+ after A36 and is still BBB+ (A35 is a watch, A33 an affirmation).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-.
**Q18.** 32 issuers, listed in the JSON. Each is one whose latest action on 2026-10-01 was a watch, with no later action resolving it. E1059 and E1019 are on watch for their local-currency rating only.
**Q19.** 35 issuers, listed in the JSON. Each has NEG as the outlook on its latest action. An issuer whose latest action is a watch has a blank outlook and is excluded.
**Q20.** No. A19 is a withdrawal for commercial reasons at BB, not a default.
**Q21.** 36 entities, listed in the JSON. E07 and 35 others had their ratings withdrawn (WD) before 2026-10-01.
**Q22.** E08 only. A22 is the only RD/D action.
**Q23.** F2 (A04).
**Q24.** Yes. BBB (A03) is investment grade.
**Q25.** 66. I count the latest INST rating of each instrument and treat EX actions as expected, not final, ratings, so I exclude them.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a country ceiling (A12, CC BB), no issuer rating.
**Q30.** E05, E1028, E1101, E1126 and E1236 (FC BB, VD ceiling BB), plus E15, E1039 and E1194 (FC A, CV ceiling A).
**Q31.** No. No VD entity has an FC rating above BB and no CV entity has one above A.
**Q32.** E09. E11 has parent E10, whose parent is E09.
**Q33.** The guarantor, E10 (Halden Bank), rated BBB+. I05's guarantor is E10, and A27/A29 put it at BBB+.
**Q34.** No. E12 has no parent and no link to E09 in the data; only the name is similar.
**Q35.** Three: E09, E10 and E11. E17 is a duplicate of E10.
**Q36.** Two: E02 and E04. E03 is a duplicate of E02.
**Q37.** 344. This is 370 records minus 26 duplicates that share an LEI with another record.
**Q38.** No. They have different LEIs and different countries.
**Q39.** A (A08/A09).
**Q40.** 74 GB-domiciled issuers, deduplicated and excluding withdrawn ones.
**Q41.** BB+. A44 downgraded E16 on 2026-06-01.
**Q42.** DE (E10, RATINGS source). The research duplicate E17 says LU.
**Q43.** Zero. The only LU record, E17, duplicates E10, which is domiciled in DE.
**Q44.** Yes. I07 is in XVD, which I take to be Valdoria's currency, although the data never defines the code.
**Q45.** No. I07 is BBB- (A45) and the BB ceiling constrains foreign-currency ratings, which I07 is not.
**Q46.** No. E11 has only a CO rating (A46) and no LTIDR or STIDR; the data does not define CO.
**Q47.** None. I08 has only an EX action (A47, A), which I read as an expected, not final, rating.
**Q48.** 106 instruments, applying the same EX exclusion as Q25.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1064","E1163","E1058","E1213","E1228","E1347","E1307","E1350","E1346","E1034","E1186","E1169","E1159","E1285","E1112","E1263","E1167","E1160","E1349","E1341","E1345","E1344","E1343","E1342","E1340","E1348","E1294","E1300","E1298","E1290","E1255","E1080","E1093","E1057","E1053","E1051","E1144","E1243","E1229","E1151"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 290},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1109","E1013","E1098","E1066","E1099","E1126","E1146","E1317","E1314","E1168","E1132","E1181","E1209","E1264","E1260","E1266","E1297","E1238","E1061","E1059","E1019","E1323","E1037"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1350","E1347","E1228","E1034","E1282","E1056","E1046","E1080","E1029","E1072","E1345","E1344","E1343","E1342","E1340","E1348","E1351","E1294","E1064","E1300","E1263","E1261","E1248","E1271","E1079","E1190","E1211","E1005","E1160","E1188","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
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