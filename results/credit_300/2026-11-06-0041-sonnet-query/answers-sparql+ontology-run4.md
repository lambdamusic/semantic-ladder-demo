**Q1.** A-. E01's last action before 1 Jan 2025 was the assignment A01 (A-, 2024-03-12). The downgrade A02 came later, on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation that moved the outlook to Negative. The rating stayed BBB.

**Q3.** No. I02 is subordinated and was downgraded by A07 to BB+, which is speculative grade.

**Q4.** Positive. E03 is the RESEARCH record of the same LEI as E02, so they are one entity. Its latest action is A09 (2025-09-15, A, POS).

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, so it is rated in line with E02's A, and its own rating A (A10, A11) is the same.

**Q6.** The data doesn't state a reason, but the likely cause is the Country Ceiling. VD's ceiling is BB (A12). E05's FC rating is BB (A14), while its LC rating is BBB- (A13), which is not capped.

**Q7.** 31 issuers had a Downgrade action in 2026 (list in the JSON). E1051 counts because its actions are labelled DG, although the rating shown after each is A+.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and RD is a default. No other non-QA issuer has an RD or D rating.

**Q9.** 278. That is 277 distinct LEIs with a non-withdrawn LTIDR on 1 Oct 2026, plus the sovereign CV, which has no LEI but has LTIDR actions (A38, A39). CO and CC ratings are excluded. The sovereign VD has only a Country Ceiling, no LTIDR.

**Q10.** Depends. E05 is BB on the FC basis (A14) but BBB- on the LC basis (A13).

**Q11.** BBB+. A36 (2024-09-30) is the latest E14 action on or before that date.

**Q12.** A-. A34 (2023-01-15) was the only E14 action before then.

**Q13.** 1. Only A36 is a DG for E14. A35 is a Watch and A33 an affirmation.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. A26 (A-, 2023-05-01) held until A27 on 2026-04-15, and E17 (same LEI) has no actions.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after the Watch (A35) and the affirmation (A33).

**Q17.** No. E06's 2026 action A17 is a Rating Watch, not a downgrade. The rating stays A-.

**Q18.** 31 issuers, listed in the JSON, were on RWN on 1 Oct 2026. Their latest action on the same LEI and basis carries a Watch. Two of them are LC-basis watches, E1019 and E1059.

**Q19.** 30 issuers, listed in the JSON, had a Negative outlook on 1 Oct 2026. In each case the latest outlook-bearing action is NEG, with no later withdrawal.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default. Its last rating before that was BB.

**Q21.** 35 entities, listed in the JSON, had a rating at some point but no non-withdrawn LTIDR on 1 Oct 2026. E07 is one of them (A19).

**Q22.** E08, the only non-QA issuer ever rated RD or D (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is BBB (A03).

**Q25.** 66. Of 106 instruments with a rating on that date, 66 were at BBB- or better. The expected rating on I08 is excluded.

**Q26.** A+ (A40).

**Q27.** A-. I06 is rated A- (A42), at or below the CV ceiling of A (A37).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** Eight entities were at their ceiling. The CV ceiling is A and the VD ceiling is BB, and the ones at exactly that level are listed in the JSON.

**Q31.** No. No FC rating among CV- or VD-domiciled entities is above its ceiling.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose FC rating is BBB+ (A27). The instrument's own rating is also BBB+ (A29).

**Q34.** No. E12 has no parent link and is not in E09's chain.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331. There are 329 distinct LEIs among non-QA records, plus the two sovereigns (CV, VD), which have none.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 66.

**Q41.** None. E16 is a QA record, which must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.

**Q43.** 1. Only E17 is domiciled in LU, and it is the same entity as E10.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected-rating action (A47), so it stays unrated.

**Q48.** 106.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E1101","E1236","E1126","E05","E1028"]},
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