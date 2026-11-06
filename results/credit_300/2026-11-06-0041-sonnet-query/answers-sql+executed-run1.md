**Q1.** A-. E01's LTIDR FC rating was A- from 2024-03-12 to 2025-06-20 (A01), so it covers 1 Jan 2025.

**Q2.** No. E01 moved from BBB to BBB with a Negative outlook on 2026-02-10 (A03, action AF, affirmed), so the rating itself did not change in 2026. Its only downgrade was in 2025 (A02).

**Q3.** No. The 2031 note I02 has been rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's current rating is A with a POS outlook (A09).

**Q5.** Credit risk of E02 (Northwind Holdings), via its guarantee of I03, which is rated A (A11).

**Q6.** The data doesn't state a reason. The likely cause is the VD Country Ceiling of BB (from 2025-04-01). E05's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13).

**Q7.** The issuers with downgrade (DG) actions on their issuer ratings in 2026 are listed in the JSON. Downgrades to WD are excluded.

**Q8.** E08, which moved to RD on 2026-07-08 (A22) and is still there.

**Q9.** 278 distinct issuers had a non-withdrawn LTIDR in force on 1 October 2026.

**Q10.** Depends. E05 is BB on a foreign-currency basis (non-investment grade) and BBB- on a local-currency basis (investment grade).

**Q11.** BBB+. This is A36, valid from 2024-09-30 to 2025-11-20, and the later watch period A35 keeps BBB+.

**Q12.** A- (A34, valid 2023-01-15 to 2024-09-30).

**Q13.** 1. The only DG action for E14 is A36; the others are a watch action and an affirmation.

**Q14.** None. E12's first rating (A30) only starts on 2024-02-01.

**Q15.** A-. E10 held A- (A26) until 2026-04-15.

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now, although its watch and outlook status changed (A35, A33).

**Q17.** No. E06 is A- on Rating Watch Negative since 2026-09-03 (A17), with no rating change.

**Q18.** 32 issuers were on RWN on 1 October 2026; they are in the JSON.

**Q19.** 28 issuers had a Negative outlook on 1 October 2026; they are in the JSON.

**Q20.** No. E07's rating was withdrawn (WD, A19) and it has no default rating.

**Q21.** 35 entities had an issuer rating that was later withdrawn (WD), leaving no rating in force on 1 October 2026. They are in the JSON and include E07.

**Q22.** Only E08 has an RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66 instruments held an investment-grade rating.

**Q26.** A+ (A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV, FC, valid from 2024-01-01).

**Q29.** None. No ratings exist for VD.

**Q30.** Eight entities had a foreign-currency rating exactly at their country's ceiling (the CV ceiling is A, the VD ceiling is BB). They are listed in the JSON.

**Q31.** No. No foreign-currency issuer rating was above its country's ceiling.

**Q32.** E09.

**Q33.** Credit risk of E10 (Halden Bank), the guarantor of I05, which is rated BBB+ (A29).

**Q34.** Yes. E12 (Halden Foods) has no parent and appears in no ancestors rows, so it does not sit in E09's chain, where E10 sits. I answered "no" below, so I am correcting that: the data does not link them, so the answer is **no**.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 331. Duplicate records are already merged into the 331 entity rows.

**Q38.** No. E06 and E13 have different LEIs and countries (DE and US), so they are separate entities.

**Q39.** A (A09).

**Q40.** 66 distinct GB-domiciled issuers held an issuer rating on 1 October 2026.

**Q41.** None. No entity named Brindle Capital exists in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is flagged local_currency = yes (currency XVD).

**Q45.** No. I07 is rated BBB-, and the BB ceiling applies to foreign-currency ratings, not to a local-currency note.

**Q46.** No. The data holds no ratings for E11 itself, only for its notes I05.

**Q47.** None. No rating record exists for I08.

**Q48.** 106 instruments held a rating.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18":{"issuers":["E1037","E1209","E1242","E1317","E1099","E1132","E1260","E1013","E1061","E1238","E1297","E1181","E06","E1133","E1066","E1146","E1203","E1314","E1323","E1098","E1126","E1088","E1194","E1109","E1168","E1006","E1019","E1264","E1267","E1039","E1059","E1266"]},
"Q19":{"issuers":["E09","E1211","E01","E1064","E1118","E1261","E1034","E1188","E1248","E1228","E1263","E1005","E1080","E1271","E1079","E1055","E1294","E1046","E1105","E1158","E1056","E1059","E1282","E1300","E1072","E1190","E1029","E1160"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1021","E1166","E1121","E1205","E1200","E1225","E1233","E1234","E1206","E1219","E1320","E1244","E1316","E1062","E1277","E1218","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1041","E1063","E1107","E1138","E1140","E1001","E1124","E1172","E1048","E1084","E1076"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1039","E1236","E1028","E1194","E1101","E1126","E15"]},
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