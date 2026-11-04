**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02); the 2026-02-10 action (A03) affirmed BBB with a Negative outlook.

**Q3.** No, BB+. The 2031 note is I02, a subordinated note, and it has been rated BB+ since the 2025-06-20 downgrade.

**Q4.** Positive. E02's current rating (A09) is A with a Positive outlook.

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 and guaranteed by E02, and credit_risk_of is E02; the rating is A on both E02 (A09) and I03 (A11).

**Q6.** The data supports an explanation, but it does not state a cause. Valdoria's country ceiling is BB from 2025-04-01. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13), so the foreign-currency rating sits at the ceiling.

**Q7.** I judged "downgraded" by an actual fall in rating level, not by the action code. Several rows are mislabelled: E1064's A- to BBB+ move on 2026-02-02 is coded AF, and E1290 and E1307 have similar cases. The list covers issuer ratings only, so I05's 2026 downgrade, which is an instrument rating, is not included. The list is in the JSON.

**Q8.** E08 only. Its rating is RD (A22) from 2026-07-08, and no other entity has an RD or D rating.

**Q9.** 277. This counts entities with a non-withdrawn issuer rating in force on 2026-10-01. It includes CV and E1279, whose only current rating is local-currency. Without the sovereign CV the count is 276.

**Q10.** Depends on the currency basis. E05's foreign-currency rating is BB (not investment grade) and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 held A- until 2024-09-30 (A34).

**Q13.** 1. The only fall in rating level for E14 was A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating (A30) began on 2024-02-01, after the date asked about.

**Q15.** A-. E10 held A- from 2023-05-01 to 2026-04-15 (A26); E17 is merged into E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), with only a watch period in between (A35).

**Q17.** No. E06's 2026 action was a move to Rating Watch Negative at A- (A17), not a downgrade.

**Q18.** 32 entities were on Rating Watch Negative; they are listed in the JSON. This uses rows with watch = RWN and no end date, including foreign-currency rows and local-currency-only cases (E1019, E1059).

**Q19.** 26 entities had a Negative outlook; they are listed in the JSON.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19), and it was never rated RD or D.

**Q21.** 35 entities had a rating that ended in withdrawal; they are listed in the JSON. E1106 and E1279 are excluded because each still holds a rating on another currency basis.

**Q22.** E08 only (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's rating is BBB (A03).

**Q25.** 66. Of the 106 instruments with a rating in force, 66 are rated BBB- or better.

**Q26.** A+ (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** E15, E1039 and E1194 (CV, ceiling A) and E05, E1028, E1101, E1126 and E1236 (VD, ceiling BB) have foreign-currency ratings exactly at their ceiling.

**Q31.** No. No foreign-currency rating exceeds the A ceiling for CV or the BB ceiling for VD.

**Q32.** E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is issued by E11 and guaranteed by E10, and credit_risk_of is E10; the rating is BBB+ on both I05 (A29) and E10 (A27).

**Q34.** No. E12 has no parent, and its ultimate_parent_id is empty, so it is not in the E09 group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 entity rows, after duplicate records were merged.

**Q38.** No. E06 (DE) and E13 (US) have different LEIs and no parent link between them.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled entities hold an issuer rating in force on 2026-10-01.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity is domiciled in LU.

**Q44.** Yes. I07 is flagged local_currency = yes and is denominated in XVD.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency obligation rated BBB- (A45).

**Q46.** No. E11 has no rating rows; I05 is rated on E10's credit.

**Q47.** None. I08 has no rating rows.

**Q48.** 106 instruments have a rating in force.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 277},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```