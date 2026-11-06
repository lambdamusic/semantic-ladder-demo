**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01), and the downgrade to BBB only came on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with the outlook moved to NEG, and an outlook change is not a downgrade.

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are the same entity, and the latest action is A09 (2025-09-15) with outlook POS.

**Q5.** A holder takes the credit risk of E02 (Northwind Holdings), the guarantor of I03. The note is rated A (A10, A11).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating of BBB- (A13) is not capped.

**Q7.** 31 issuers had an LTIDR or STIDR downgrade in 2026 (listed in the JSON). They include E10 (A29's issuer, downgraded in A27) and E08 (A21, A22), but not E01 or E14.

**Q8.** E08 only. It was downgraded to RD on 2026-07-08 (A22).

**Q9.** 278 distinct issuers hold an issuer rating as of 2026-10-01, counted by LEI, excluding QA records and withdrawn ratings.

**Q10.** Depends. Valdoria Telecom (E05) is BB on foreign currency (speculative) and BBB- on local currency (investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions (A35, A33) leave it at BBB+.

**Q12.** A-, from A34 (assigned 2023-01-15).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. The downgrade to BBB+ (A27) came on 2026-04-15, after that date.

**Q16.** No. Marlow Utilities was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 did not change the rating).

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch Negative, which is not a downgrade.

**Q18.** 32 issuers were on Rating Watch Negative on 2026-10-01 (listed in the JSON), including E06.

**Q19.** 28 issuers had a Negative outlook on 2026-10-01 (listed in the JSON), including E01 and E09.

**Q20.** No. Pellam Retail (E07) was BB and then withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** 35 entities (listed in the JSON) had a rating that was later withdrawn, including E07 (A19).

**Q22.** E08 only (RD in A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66 instruments, counting each instrument's latest non-EX action, excluding QA issuers and withdrawals.

**Q26.** A+ (A40).

**Q27.** A- (A42, instrument I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not its issuer rating.

**Q30.** Eight entities (listed in the JSON) had a foreign-currency rating exactly at their country's ceiling. They are E05, E15 and others in VD (ceiling BB) and CV (ceiling A).

**Q31.** No. None of the foreign-currency ratings exceeds its ceiling.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** A holder takes the credit risk of E10 (Halden Bank), the guarantor of I05. The note is rated BBB+ (A29).

**Q34.** Yes in the sense that matters for the question only if Halden Foods has a parent link. E12 has none, so it is not in E09's group. The answer is no.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10, since they share an LEI.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331 distinct legal entities, counted by LEI with QA records excluded.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A. The latest action is A09 for the same entity (E03), an affirmation at A.

**Q40.** 66 distinct GB issuers, using the RESEARCH country where records disagree.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding DE on E10.

**Q43.** 1. Only the Halden Bank entity (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. The ceiling applies only to foreign-currency debt, and I07 is local-currency, so its BBB- (A45) is not capped.

**Q46.** No. E11 has only a Credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.

**Q48.** 106 instruments held a rating on 2026-10-01, excluding I08 (EX only).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1159","E1057","E1053","E1144","E1243","E1294","E1151","E1064","E1093","E1034","E1285","E1290","E1058","E1167","E10","E1160","E1080","E1213","E1300","E1163","E1186","E1112","E1169","E08","E1051","E1229","E1307","E1255","E1263","E1228","E1298"]},
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
"Q18":{"issuers":["E1168","E1109","E1146","E1203","E1066","E1314","E1323","E1059","E1266","E1039","E1126","E1098","E06","E1133","E1238","E1013","E1297","E1061","E1132","E1260","E1099","E1267","E1194","E1088","E1019","E1264","E1006","E1317","E1037","E1209","E1242","E1181"]},
"Q19":{"issuers":["E1271","E1079","E1064","E1261","E01","E1118","E1211","E09","E1059","E1056","E1282","E1263","E1228","E1029","E1160","E1055","E1294","E1080","E1005","E1034","E1188","E1248","E1046","E1190","E1072","E1158","E1105","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1244","E1316","E1233","E1234","E1200","E1225","E1076","E1219","E1206","E1320","E1205","E1121","E1166","E07","E1021","E1048","E1084","E1277","E1218","E1172","E1001","E1124","E1007","E1253","E1032","E1159","E1057","E1155","E1308","E1062","E1107","E1140","E1063","E1138","E1041"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1101","E05","E1236","E1126","E1028","E15","E1194","E1039"]},
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