**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12). The downgrade to BBB (A02) came on 2025-06-20, after that date.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04). A03 moved the outlook to NEG without changing the rating.

**Q3.** No. The 2031 note I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive (POS). E02 and E03 share an LEI, so they are one entity. The latest action is A09 (E03, 2025-09-15), which gives outlook POS.

**Q5.** The holder takes Northwind Holdings' credit risk (E02, the guarantor of I03). E02's rating is A (A08, A09), and I03 itself is rated A.

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling, which is BB (A12). E05's FC rating is BB (A14) and its LC rating is BBB- (A13), which is not capped.

**Q7.** 31 issuers had a downgrade (DG) on a long-term issuer rating in 2026, listed in the JSON below. QA records are excluded and same-LEI records are merged. Instrument-only downgrades such as I05 are not counted.

**Q8.** E08. Its latest action is a downgrade to RD on 2026-07-08 (A22), and no later action exists.

**Q9.** 278 distinct issuers held a non-withdrawn long-term issuer rating on 2026-10-01. QA records are excluded and same-LEI records are merged.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade), but its foreign-currency rating is BB (speculative grade).

**Q11.** BBB+. This is the DG of A36 (2024-09-30). The Rating Watch on A35 came later and did not change the rating.

**Q12.** A-. This is A34 (2023-01-15), before any later action.

**Q13.** 1. Only A36 is a downgrade for E14. The watch (A35) and affirmation (A33) are not downgrades.

**Q14.** None. E12's first action is A30 on 2024-02-01, after the date asked.

**Q15.** A-. E10 was A- (A26) until the downgrade to BBB+ on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). The watch and the affirmation did not change the rating.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative (A17), which is not a downgrade.

**Q18.** 32 issuers were on RWN on 2026-10-01, listed in the JSON below. This includes E1059 and E1019, whose RWN is on the local-currency rating.

**Q19.** 28 issuers had a Negative outlook on 2026-10-01 on their latest long-term issuer rating, listed in the JSON below. Withdrawn ratings are excluded.

**Q20.** No. E07 was withdrawn for commercial reasons (A19), and a withdrawal is not a default. Its rating before that was BB.

**Q21.** 35 entities had an issuer rating that was later withdrawn, listed in the JSON below. Each had a withdrawn latest rating on 2026-10-01 and no active issuer rating of any basis.

**Q22.** E08. It is the only entity with RD or D (A22).

**Q23.** F2. E01's STIDR was affirmed at F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 66. Of the 106 instruments with a live rating (EX actions are ignored), 66 are rated BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** 8 entities had an FC rating exactly at the ceiling. At CV's ceiling of A: E1194, E1039, E15. At VD's ceiling of BB: E1028, E1101, E1126, E1236, E05.

**Q31.** No. No company in CV rates above A or in VD above BB.

**Q32.** E09, Halden Group plc. E11's parent is E10 (RATINGS record), and E10's parent is E09.

**Q33.** The holder takes Halden Bank's credit risk (E10, the guarantor of I05). E10's current rating is BBB+ (A27).

**Q34.** No. E12 has no parent and no link to E09, so it is not in the E09 group.

**Q35.** 3. The group is E09, E10 and E11. E17 shares E10's LEI and is the same entity.

**Q36.** 2. The group is E02 and E04. E03 is a duplicate record of E02.

**Q37.** 331. This counts distinct LEIs (sovereigns by their own ID) and excludes QA records.

**Q38.** No. E06 and E13 have different LEIs and different countries, so they are different entities.

**Q39.** A (A08, A09, same entity).

**Q40.** 66 distinct GB-domiciled issuers had a live issuer rating on 2026-10-01.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** DE. The RATINGS record E10 holds, over RESEARCH record E17 (LU).

**Q43.** 0. The only LU record is E17, which is a duplicate of E10, and RATINGS says E10 is in DE.

**Q44.** Yes. I07 pays in XVD, VD's domestic currency.

**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but a local-currency obligation is not capped by the ceiling.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not a rating, and it has no LTIDR.

**Q47.** None. I08 has only an Expected rating (A47), so it stays unrated.

**Q48.** 106 instruments held a live rating on 2026-10-01 (EX actions ignored).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1151","E1294","E1159","E1057","E1243","E1053","E1144","E1058","E1167","E1080","E1285","E1290","E1034","E1051","E1064","E1093","E08","E1112","E1169","E1186","E1307","E1228","E1263","E1298","E1255","E1229","E10","E1160","E1163","E1213","E1300"]},
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
"Q18":{"issuers":["E1194","E1314","E1264","E1146","E1317","E1238","E1297","E1059","E1039","E1061","E1019","E1099","E1203","E1242","E1066","E1126","E1088","E1098","E1132","E1168","E1006","E1260","E1109","E1323","E1266","E1037","E06","E1013","E1267","E1181","E1209","E1133"]},
"Q19":{"issuers":["E1005","E1055","E1072","E1160","E1211","E1263","E1282","E1271","E1294","E1118","E1080","E01","E1064","E1190","E1158","E1228","E1029","E1248","E1188","E1059","E1034","E1079","E1105","E1046","E1261","E1300","E09","E1056"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1206","E1320","E1219","E1218","E1225","E1233","E1200","E1234","E1076","E1121","E1205","E1062","E1244","E1316","E1063","E1138","E1140","E1041","E1107","E1277","E1166","E07","E1021","E1172","E1124","E1001","E1048","E1084","E1007","E1253","E1032","E1308","E1155","E1057","E1159"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1194","E1039","E15","E1028","E1101","E1126","E1236","E05"]},
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
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```