**Q1.** A-. E01's A- (A01) was in force from 2024-03-12 to 2025-06-20, so it covers 1 Jan 2025.

**Q2.** No. E01's only 2026 action (A03, 2026-02-10) kept it at BBB and moved the outlook to Negative; the downgrade to BBB was A02 in 2025.

**Q3.** No. The 2031 note is I02 (subordinated), now rated BB+ (A07, since 2025-06-20), which is below investment grade.

**Q4.** Positive. E02's open row A09 is A with a POS outlook.

**Q5.** The guarantor E02 (Northwind Holdings), not the issuer E04. I03 names E02 as `credit_risk_of`, and I03 is rated A (A11); E02's own rating is also A.

**Q6.** The data doesn't state a reason. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB equals Valdoria's country ceiling (BB from 2025-04-01), which is consistent with the ceiling capping foreign-currency ratings.

**Q7.** 36 issuers, listed in the JSON. I counted a downgrade as a lower rating level than the prior row, not the action code. E1064 (A- to BBB+, labelled AF) is therefore included, and E5116 (A STA to A NEG, labelled DG) is excluded. E5033's cut (A5028) is dated 2026-11-06, after the 1 Oct 2026 snapshot, so I excluded it.

**Q8.** E08. Its open row A22 is RD from 2026-07-08.

**Q9.** 377. This counts entities with an open, non-WD LTIDR row, including the E08 RD row and the E5033 row dated after the snapshot. The Republic of Valdoria (VD) has no rating.

**Q10.** Depends. E05 is BB on a foreign-currency basis (A14, not investment grade) and BBB- on a local-currency basis (A13, investment grade).

**Q11.** BBB+. A36 (BBB+, valid 2024-09-30 to 2025-11-20) covers that date.

**Q12.** A-. A34 (A-, valid 2023-01-15 to 2024-09-30) covers that date.

**Q13.** 1. The only drop is A- to BBB+ on 2024-09-30 (A36); the RWN and affirmation rows are not downgrades.

**Q14.** None. E12's first rating (A30) starts on 2024-02-01.

**Q15.** A-. A26 (A-) held until 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33), with only a watch period in between.

**Q17.** No. E06's A- was unchanged; A17 on 2026-09-03 only added Rating Watch Negative.

**Q18.** 31 entities, listed in the JSON. These are entities with an open row carrying the RWN watch, including three whose open RWN row is on the local-currency basis (E1019, E1059, E1194).

**Q19.** 46 entities, listed in the JSON. These are entities with an open row carrying a Negative outlook.

**Q20.** No. E07 has WD (A19), not a default rating, and has no D or RD row.

**Q21.** 35 entities, listed in the JSON. Their latest open row is WD and they have no other open rating. E1106 and E1279 are excluded because each still holds an open rating on the other currency basis.

**Q22.** E08 only, through RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is BBB (A03).

**Q25.** 72. This counts instrument rows still open on 1 Oct 2026 at BBB- or above.

**Q26.** A+ (A40).

**Q27.** A- (A42 on I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** 13 entities, listed in the JSON. Country ceilings are CV = A and VD = BB. Five entities sit at BB in VD (E05, E1028, E1101, E1126, E1236) and three more at BB in VD-domiciled group companies (E5012, E5047, E5091, E5124 make four of these; together they are the VD set). The CV entities at A are E15, E1039, E1194 and E5116.

**Q31.** No. No entity's foreign-currency rating is above its country's ceiling.

**Q32.** E09.

**Q33.** E10 (Halden Bank), the guarantor, per I05. I05 is rated BBB+ (A29), and E10 is also BBB+.

**Q34.** No. E12 has no parent, while E10 belongs to the E09 group, and the data gives no link between them despite the shared name.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 497. This is 16 core rows, 315 E1xxx rows and 166 E5xxx rows, taking duplicates as already merged. I derived the E1xxx count by subtracting the 24 merged-away IDs from E1001–E1339.

**Q38.** No. E06 and E13 are separate entities with different LEIs, countries (DE, US) and records.

**Q39.** A (A09).

**Q40.** 79. This counts GB-domiciled entities with an open, non-WD issuer rating.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is denominated in XVD with `local_currency` = yes.

**Q45.** No. I07 is rated BBB- (A45), but it is a local-currency obligation, and the VD ceiling of BB applies to foreign-currency ratings.

**Q46.** No. E11 has no ratings of its own; its I05 note is guaranteed by E10.

**Q47.** None. I08 has no rating row.

**Q48.** 113. This counts instruments with an open rating on 1 Oct 2026.

**Q49.** E5001.

**Q50.** 6, since `ancestors.csv` has E5047 → E5001 at levels_up = 6.

**Q51.** 58 (E5001 to E5058).

**Q52.** 19 (E5086 to E5104).

**Q53.** No. E5062 belongs to the E5059 group and E5086 is the top of the Rotam group.

**Q54.** E5106, E5124 and E5130.

**Q55.** 32 rated entities have a VD-domiciled entity above them: 6 in Cerid, 2 in Rotam, 10 in Wonod and 14 in Geren. In Geren the top, E5145, is domiciled in VD.

**Q56.** BB-. E5144 (A5108) is the lowest of Vesol's current ratings.

**Q57.** E5002. It is level 2 above E5011 and level 2 above E5013.

**Q58.** E5145. It guarantees I5007, which E5133 (Vesol group) issued.

**Q59.** 12 (E5011 to E5022).

**Q60.** E5145 (Geren Group SA), the guarantor, and it is not in the same group as the issuer E5133 (Vesol). I5007 is rated BBB (A5126).

**Q61.** 19. This counts Cerid members whose current foreign-currency rating is BB+ or lower; E5001 itself has no rating row.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E5019","E5059","E5097","E5113","E5156"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 377},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5033","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
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
"Q30": {"entities": ["E15","E1039","E1194","E5116","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 497},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 79},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 113},
"Q49": {"parent": "E5001"},
"Q50": {"count": 6},
"Q51": {"count": 58},
"Q52": {"count": 19},
"Q53": {"same_group": "no"},
"Q54": {"entities": ["E5106","E5124","E5130"]},
"Q55": {"count": 32},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```