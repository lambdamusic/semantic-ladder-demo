**Q1.** A-. Kestrel's last action before 1 Jan 2025 was the A-/STA assignment (A01); the downgrade to BBB came later (A02, 2025-06-20).

**Q2.** No. The only 2026 action on Kestrel (E01) is an affirmation at BBB with Negative outlook (A03).

**Q3.** No, it is BB+. The 2031 note is I02, assigned BBB (A23) and downgraded to BB+ (A07).

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its latest action is A09 (2025-09-15, A/POS), which supersedes A08 (STA).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02 (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating. Valdoria Telecom's FC rating is therefore BB (A14), while its LC rating is BBB- (A13).

**Q7.** I counted 48 issuers with a downgrade action dated 2026, listed in the JSON with duplicates merged to the RATINGS record. I excluded E1341 and E5033, whose downgrades are dated after today (A1720, A5028).

**Q8.** E08. Saxby Shipping was downgraded to RD on 2026-07-08 (A22).

**Q9.** 391. This is my count of distinct issuers whose latest LTIDR action on 1 Oct 2026 is not a withdrawal, with duplicates merged. It is a long manual count and could be off by a few. E1115, E1158 and E1303 have later actions after a withdrawal (A1250, A1337/A1338, A1649), so I counted them as rated.

**Q10.** Depends. The FC rating is BB, which is not investment grade (A14), but the LC rating is BBB-, which is (A13).

**Q11.** BBB+. Marlow Utilities (E14) was downgraded to BBB+ on 2024-09-30 (A36) and was not changed until later.

**Q12.** A-. This is the rating assigned on 2023-01-15 (A34).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. Halden Bank (E10; E17 is a duplicate record) held A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. It was BBB+ on 1 Jan 2025 and is BBB+ now. A35 is a watch and A33 an affirmation, neither of which changes the rating.

**Q17.** No. Orrin Bank's only 2026 action is a Rating Watch Negative at A- (A17).

**Q18.** 32 issuers have a Rating Watch Negative as their latest action, listed in the JSON. For E1059 and E1019 the watch is on the LC rating (A1132, A1042).

**Q19.** 55 issuers have a Negative outlook as their latest action, listed in the JSON. I did not count entities whose latest action was a Rating Watch, since it carries no outlook. I excluded actions dated after 1 Oct 2026, such as A1730 and A1736.

**Q20.** No. Pellam Retail's rating was withdrawn for commercial reasons (A19), and it was never rated D or RD.

**Q21.** 35 entities had a rating that was later withdrawn, listed in the JSON, with E1001 and E1253 standing for their duplicates E1002 and E1254. I left out E1279 and E1106 because each still holds a rating on one currency basis.

**Q22.** E08. Its RD (A22) is the only default-grade rating in the data.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 72. This counts instruments whose latest INST rating is BBB- or higher. I treated EX as the rating having ended, so I08, I1046 and similar are not counted.

**Q26.** A+ (A40).

**Q27.** A- (A42, on I06).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has only a Country Ceiling of BB (A12) and no LTIDR.

**Q30.** 13 entities have an FC rating equal to the ceiling. Valdoria's ceiling is BB (A12) and Corvenia's is A (A37), and the 13 are the VD entities at BB and the CV entities at A, listed in the JSON.

**Q31.** No. No VD entity has an FC rating above BB, and no CV entity has one above A.

**Q32.** E09 (Halden Group plc). The chain is E11 to E10 to E09.

**Q33.** The guarantor Halden Bank (E10), rated BBB+ (A27). I05 is issued by E11 and guaranteed by E10.

**Q34.** No. E12 has no parent and so sits outside the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 511. There are 540 entity rows, and 29 are RESEARCH duplicates sharing an LEI with another row.

**Q38.** No. They have different LEIs, countries and types.

**Q39.** A (A08, A09).

**Q40.** 87, counted manually by GB domicile among the rated issuers.

**Q41.** BB+ (A44).

**Q42.** DE (E10). The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of the DE-domiciled E10.

**Q44.** Yes. I07 is denominated in XVD, which I infer is Valdoria's currency.

**Q45.** No. The ceiling applies to foreign-currency obligations, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a CO rating (A46) and no issuer rating.

**Q47.** None. I08 has only an EX action (A47, 2026-09-01) and no other rating.

**Q48.** 113. That is the 122 instruments less 9 with no rating in force: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

**Q49.** E5001. E5011's parent is E5167, a duplicate of E5005, which sits under E5002 and E5001.

**Q50.** 6 levels: E5047, E5035, E5023, E5011, E5005, E5002, E5001.

**Q51.** 59. This is E5001 to E5058 plus the QA record E5170, which names E5001 as its parent. E5011 is included via the E5167 and E5005 duplicate.

**Q52.** 19, E5086 to E5104. E5168 is a duplicate of E5062.

**Q53.** No. E5062 sits under Belir Group, and only the RESEARCH duplicate E5168 names Rotam (E5086) as parent.

**Q54.** E5124 and E5130. E5169 is a duplicate of the NL-domiciled E5106.

**Q55.** 23. The count is the rated descendants of VD-domiciled entities: 6 under E5005/E5167, 2 under E5091, 1 under E5124 and 14 under E5145.

**Q56.** BB-, held by E5144.

**Q57.** E5002. E5011 reaches it through E5167, the duplicate of E5005, and E5013 reaches it through E5006.

**Q58.** E5145. It guarantees I5007, issued by E5133 in the Vesol group. All other guarantees are within the guarantor's own group.

**Q59.** 12: E5011 to E5022.

**Q60.** The guarantor Geren Group SA (E5145). It is not in the same group as the issuer E5133, which sits under E5132.

**Q61.** 20. These are 19 sub-investment-grade members plus the QA record E5170 (B-, A5127). Without E5170 the count is 19.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1169","E1051","E1080","E1307","E1298","E1167","E1160","E1285","E1263","E1255","E1243","E1228","E1213","E1229","E1294","E1290","E1300","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E1064","E1112","E1093","E1053","E1057","E1058","E1159","E1163","E1186","E1144","E1151","E5116","E5113","E5059","E5097","E5019","E5156"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 391},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1059","E1006","E1013","E1019","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1209","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E1238","E1203"]},
"Q19": {"issuers": ["E01","E09","E1046","E1056","E1079","E1080","E1105","E1118","E1190","E1211","E1228","E1271","E1282","E1300","E1294","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E1072","E1158","E1248","E1029","E1059","E1005","E1034","E1064","E1188","E1261","E1263","E1055"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 72},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124","E15","E1039","E1194","E5116"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 511},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 87},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 113},
"Q49": {"parent": "E5001"},
"Q50": {"count": 6},
"Q51": {"count": 59},
"Q52": {"count": 19},
"Q53": {"same_group": "no"},
"Q54": {"entities": ["E5124","E5130"]},
"Q55": {"count": 23},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 20}
}
```