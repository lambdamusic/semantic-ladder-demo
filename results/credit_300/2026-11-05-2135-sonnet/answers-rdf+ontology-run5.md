**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01); the next action was the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only E01 long-term action in 2026 is an affirmation at BBB (A03, 2026-02-10).

**Q3.** No, BB+. The 2031 note is I02, rated BBB (A23) and then downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E02 and E03 share one LEI, so they are one entity. The latest action is E03's affirmation with a POS outlook on 2025-09-15 (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and I03's own rating is A (A10, A11).

**Q6.** E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The foreign-currency rating is held down by Valdoria's Country Ceiling of BB (A12); the local-currency rating is not capped.

**Q7.** 31 issuers had a downgrade (DG) in 2026. I used the RATINGS record ID where an entity has duplicate records, and ignored QA records (E16 and E1340–E1351). See the JSON for the list.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) and has had no action since.

**Q9.** 278. I counted distinct entities (merging duplicate records by LEI) whose latest issuer-rating action by 2026-10-01 is not a withdrawal. This includes the Republic of Corvenia and excludes QA and credit-opinion-only records. Several entities have withdrawal actions dated before later non-withdrawal actions, and I followed the dates. Treat this count as approximate.

**Q10.** Depends. E05 is BB on foreign currency (A14) and BBB- on local currency (A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions are a Watch and an affirmation.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34).

**Q13.** 1. The only downgrade is A36; the Watch (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26) and downgraded to BBB+ on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. E06's 2026 action is a Rating Watch on 2026-09-03 (A17), which is not a downgrade.

**Q18.** 32 issuers were on Rating Watch Negative. In each case their latest action by 2026-10-01 is a Watch (for example A17 for E06 and A1010 for E1006). See the JSON for the list.

**Q19.** 28 issuers had a Negative outlook. I used each entity's latest outlook-bearing action. I excluded entities whose latest action is a Rating Watch, which carries no outlook (E1132, E1146). I also excluded entities that were later revised to a non-negative outlook or withdrawn. See the JSON for the list.

**Q20.** No. E07 was withdrawn on 2026-05-12 (A19); a withdrawal is not a default, and it was never rated below BB.

**Q21.** 35 entities. Each had an issuer rating that ended in a withdrawal (WD) action with no later rating action. See the JSON for the list.

**Q22.** E08 only. It reached RD (a default) on 2026-07-08 (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The current issuer rating is BBB (A03), which is investment grade.

**Q25.** 66. Of 106 instruments with a rating, 40 are below BBB-. Instruments with only an Expected (EX) rating are unrated.

**Q26.** A+. E15's local-currency rating is A+ (A40).

**Q27.** A-. The 2032 note is I06, rated A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), and a ceiling is not an issuer rating.

**Q30.** 8 entities: E05, E1028, E1101, E1126, E1236 (VD, ceiling BB) and E15, E1039, E1194 (CV, ceiling A). Each has a foreign-currency rating exactly at its ceiling.

**Q31.** No. No foreign-currency rating exceeds the BB ceiling for VD or the A ceiling for CV.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10 (Halden Bank), rated BBB+. The note I05 is guaranteed by E10, whose rating was cut to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent link and shares nothing but a name prefix with E09's group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10, so it is not counted separately.

**Q36.** 2: E02 and E04. E03 is a duplicate record of E02.

**Q37.** 344. There are 370 entity records, and 26 of them are duplicate records of an entity that already has a record.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09 for E03, the same entity as E02).

**Q40.** 66. I counted distinct rated issuers domiciled in GB, using the RESEARCH record where country records disagree.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. E17 is the RESEARCH record of E10, and the RESEARCH record holds for country.

**Q43.** 1. E17 is the only LU record, and it is the same entity as E10.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB- (A45), but local-currency debt is not capped by the Country Ceiling.

**Q46.** No. E11 has only a Credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47).

**Q48.** 106. There are 115 instruments, and 9 have only an Expected action.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1051","E1053","E1057","E1058","E1064","E1080","E1186","E1112","E1093","E1034","E1213","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1294","E1300","E1282","E1105"]},
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
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
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