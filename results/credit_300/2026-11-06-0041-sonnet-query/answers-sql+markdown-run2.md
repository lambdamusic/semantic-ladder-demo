**Q1.** A-. A01 (2024-03-12) set A-, and the downgrade A02 only came on 2025-06-20.
**Q2.** No. Kestrel's only 2026 actions are A03/A04, which are affirmations.
**Q3.** No. The 2031 note (I02, subordinated) was downgraded to BB+ by A07, which is speculative grade.
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 affirmed A with a POS outlook on 2025-09-15.
**Q5.** A holder takes E02's credit risk, since I03 is guaranteed by E02. I03 is rated A (A10/A11), in line with E02's A.
**Q6.** Valdoria's Country Ceiling is BB (A12), and it caps the FC rating (A14, BB). The LC rating (A13, BBB-) is not capped.
**Q7.** 31 issuers had a downgrade in 2026, listed in the JSON. QA records are excluded and duplicate records are merged by LEI. I05 is an instrument, not an issuer.
**Q8.** E08, rated RD since A22 (2026-07-08). Pellam's withdrawal is not a default.
**Q9.** 278 distinct issuers, counted by LEI with QA excluded and withdrawn ratings dropped.
**Q10.** Depends. FC is BB (speculative) and LC is BBB- (investment grade).
**Q11.** BBB+. A36 downgraded Marlow on 2024-09-30. A35 was only a watch.
**Q12.** A-, from A34.
**Q13.** 1, from A36.
**Q14.** None. Halden Foods' first rating was A30 on 2024-02-01.
**Q15.** A-, from A26. The downgrade A27 only came on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ after A33.
**Q17.** No. A17 is a Rating Watch, not a downgrade.
**Q18.** 32 issuers are on RWN, listed in the JSON. This includes E1019 and E1059, which are on watch for LC only.
**Q19.** 28 issuers have a Negative outlook, listed in the JSON.
**Q20.** No. A19 withdrew the rating for commercial reasons, which says nothing about default.
**Q21.** 35 entities, listed in the JSON, including E07 (Pellam).
**Q22.** Only E08 (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 66 instruments, excluding the unconfirmed expected rating on I08.
**Q26.** A+ (A40).
**Q27.** A- (A42, subordinated, I06).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** Eight entities: E15, E1194 and E1039 at Corvenia's ceiling of A, and E1028, E1236, E05, E1101 and E1126 at Valdoria's ceiling of BB.
**Q31.** No. No CV or VD entity's FC rating exceeds its ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** E10 (Halden Bank AG), as the guarantor of I05. The note is rated BBB+ (A29), matching E10's BBB+ (A27).
**Q34.** No. E12 has no parent and is not linked to the Halden group.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 331 distinct entities, counting by LEI with QA excluded and the two sovereigns counted by record ID.
**Q38.** No. Their LEIs differ.
**Q39.** A.
**Q40.** 66.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for country.
**Q43.** 1.
**Q44.** Yes. I07 is in XVD, VD's domestic currency.
**Q45.** No. I07 is local-currency debt and the ceiling does not cap it.
**Q46.** No. E11 has only a Credit Opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.
**Q48.** 106.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1298","E1307","E1213","E1080","E1285","E1112","E1263","E1064","E1163","E1053","E1051","E1300","E10","E1034","E1229","E1144","E1159","E1057","E1228","E1294","E1058","E1093","E1160","E1290","E1169","E1167"]},
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
"Q18":{"issuers":["E06","E1013","E1266","E1132","E1037","E1039","E1314","E1088","E1238","E1297","E1006","E1098","E1181","E1317","E1203","E1168","E1209","E1242","E1260","E1194","E1323","E1146","E1133","E1267","E1061","E1019","E1099","E1264","E1126","E1109","E1059","E1066"]},
"Q19":{"issuers":["E1055","E1059","E09","E1211","E1105","E1072","E1158","E1261","E1300","E1228","E01","E1064","E1005","E1029","E1188","E1079","E1080","E1046","E1248","E1160","E1190","E1271","E1282","E1118","E1034","E1056","E1263","E1294"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1277","E07","E1063","E1233","E1219","E1172","E1205","E1320","E1076","E1206","E1234","E1138","E1048","E1107","E1253","E1225","E1121","E1159","E1032","E1166","E1218","E1007","E1155","E1021","E1057","E1001","E1041","E1244","E1200","E1140","E1084","E1308","E1062","E1124","E1316"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1194","E1039","E1028","E1236","E05","E1101","E1126"]},
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