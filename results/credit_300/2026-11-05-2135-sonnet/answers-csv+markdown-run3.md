**Q1.** A-. E01's latest action on or before 1 Jan 2025 is A01 (2024-03-12, A-); the downgrade A02 came in June 2025.
**Q2.** No. E01's only 2026 actions, A03 and A04, are affirmations.
**Q3.** No. I02 is rated BB+ after the downgrade A07, and BB+ is speculative grade.
**Q4.** Positive. E03 has the same LEI as E02, and A09 (2025-09-15) is the latest action, affirming A with a POS outlook.
**Q5.** E02, rated A. I03 is guaranteed by E02 (instruments.csv), and A09 is E02's latest rating action.
**Q6.** The Country Ceiling caps it. A12 sets the Valdoria ceiling at BB, so E05's foreign-currency rating is BB (A14), while its uncapped local-currency rating is BBB- (A13).
**Q7.** 30 issuers had a downgrade (DG) dated in 2026, on any basis, listed in the JSON. Research-system records are mapped to their RATINGS record (E1161→E1160, E1170→E1169, E1299→E1298). QA records are ignored.
**Q8.** E08 only. A22 (2026-07-08) puts it at RD, which counts as default.
**Q9.** 278. There are 313 distinct non-QA entities that ever held a long-term issuer rating, and 35 of them were withdrawn by 1 Oct 2026. For E1158 I used the latest action by date (A1338, an affirmation), which comes after the withdrawal A1339. E1279 (local currency) and E1106 (foreign currency) keep a rating on the other basis. This is a manual tally and could be off by a few.
**Q10.** Depends. E05's foreign-currency rating is BB (speculative), while its local-currency rating is BBB- (investment grade).
**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and nothing changed it before 1 Jun 2025.
**Q12.** A-. A34 assigned A- in 2023, before the A36 downgrade.
**Q13.** One. Only A36 is a downgrade; A35 is a watch and A33 an affirmation.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. E10's A26 holds until the downgrade A27 on 2026-04-15.
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now, since the watch A35 changed nothing.
**Q17.** No. E06's only 2026 action, A17, places it on Rating Watch, which is not a downgrade.
**Q18.** 32 issuers, listed in the JSON. Each one's latest action, on either currency basis, is a Rating Watch placement.
**Q19.** 23 issuers, listed in the JSON. I read the outlook from each entity's latest action only. A blank outlook (after an RW action) counts as not negative, which excludes E1132 and E1146.
**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal says nothing about default.
**Q21.** 35 entities, listed in the JSON. Each held a long-term issuer rating that was later withdrawn, with no later action.
**Q22.** E08 only, rated RD by A22.
**Q23.** F2, from A04.
**Q24.** Yes. E01's BBB is investment grade.
**Q25.** 66 instruments. This counts instruments whose latest INST rating on 1 Oct 2026 is BBB- or higher. EX actions are not ratings.
**Q26.** A+, from A40.
**Q27.** A-, from A42 (I06).
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** Eight entities. At the VD ceiling of BB: E05, E1028, E1101, E1126 and E1236. At the CV ceiling of A: E15, E1039 and E1194.
**Q31.** No. No foreign-currency rating exceeds BB in VD or A in CV.
**Q32.** E09. E11 has parent E10 (E11 → E10), and E10 has parent E09, which has none.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).
**Q34.** No. E12 has no parent, so it is outside the E09 group that contains E10.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 (same entity as E03) and E04.
**Q37.** 331. There are 370 records, minus 26 duplicate records of the same LEI, minus 13 QA records.
**Q38.** No. They have different LEIs.
**Q39.** A, from A09.
**Q40.** 66. This is a manual tally of GB-domiciled entities with a live issuer rating. No RESEARCH-record country override affects GB.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, and it says LU, not DE.
**Q43.** 1: E10 (Halden Bank), via E17.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's domestic currency.
**Q45.** No. The note is local-currency debt, so the ceiling does not cap it.
**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an expected rating (A47, EX), so it remains unrated.
**Q48.** 106 instruments. Of 115 instruments, 9 have no assigned INST rating: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":278},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1099","E1019","E1006","E1109","E1264","E1260","E1168","E1181","E1209","E1132","E1323","E1126","E1146","E1037","E1066","E1098","E1013","E1297","E1266","E1238","E1317","E1314","E1061","E1059"]},
"Q19":{"issuers":["E01","E09","E1029","E1034","E1046","E1056","E1059","E1064","E1072","E1079","E1080","E1118","E1158","E1160","E1190","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":331},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```