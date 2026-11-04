**Q1.** A-. E01's rating was A- from A01 (2024-03-12) until it was downgraded to BBB on 2025-06-20 (A02).
**Q2.** No. E01's only 2026 action on its long-term rating is A03, an affirmation (BBB, outlook to Negative).
**Q3.** No, BB+. Note I02 is subordinated and was cut to BB+ by A07 on 2025-06-20.
**Q4.** Positive. E03 (NORTHWIND HLDGS) has the same LEI as E02, so they are one entity. The latest action is A09 (2025-09-15), which gave a POS outlook.
**Q5.** The holder takes the credit risk of E02, the guarantor of I03, and the note is rated A. The issuer E04 is a finance subsidiary, and I03's latest rating is A (A10/A11).
**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling, which is BB (A12). E05's FC rating is BB (A14) and its LC rating is BBB- (A13), because local-currency ratings are not capped.
**Q7.** 31 issuers had an issuer-rating downgrade (DG) in 2026, listed in the JSON. RESEARCH duplicates are mapped to their RATINGS records and QA records are excluded.
**Q8.** E08. A22 (2026-07-08) cut it to RD after a distressed debt exchange.
**Q9.** 278. This counts distinct LEIs whose latest long-term issuer rating on 1 October 2026 is not a withdrawal (WD). Duplicate records and QA records are excluded.
**Q10.** Depends. E05's LC rating is BBB- (investment grade) but its FC rating is BB (speculative).
**Q11.** BBB+. E14 was downgraded to BBB+ by A36 on 2024-09-30. The watch placed by A35 on 2025-11-20 falls after 1 June 2025.
**Q12.** A-, from A34 (2023-01-15).
**Q13.** 1. Only A36 is a downgrade; A35 is a Rating Watch and A33 is an affirmation.
**Q14.** None. E12's first rating, A30, is dated 2024-02-01, after the question date.
**Q15.** A-. E10's downgrade to BBB+ (A27) came on 2026-04-15, after 1 January 2026.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).
**Q17.** No. E06's only 2026 action, A17, is a Rating Watch Negative and the rating stayed A-.
**Q18.** 32 issuers were on Rating Watch Negative on 1 October 2026 (E06 among them), listed in the JSON.
**Q19.** 28 issuers had a Negative outlook on 1 October 2026 (E01 and E09 among them), listed in the JSON.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.
**Q21.** 35 entities had an issuer rating that was later withdrawn and not replaced, listed in the JSON (E07 among them).
**Q22.** Only E08, which reached RD (A22).
**Q23.** F2, from A04.
**Q24.** Yes. E01's FC rating is BBB.
**Q25.** 66. This counts instruments whose latest rating on 1 October 2026 is BBB- or better. The expected rating (EX) on I08 is excluded.
**Q26.** A+, from A40.
**Q27.** A-. I06's rating comes from A42.
**Q28.** BBB+, from A38.
**Q29.** None. VD only carries a Country Ceiling (A12), which is not its issuer rating.
**Q30.** Eight entities: E1101, E1236, E05, E1028 and E1126 sit at VD's ceiling of BB, and E1039, E1194 and E15 sit at CV's ceiling of A.
**Q31.** No. Every foreign-currency issuer rating on that date is at or below its country's ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The holder takes the credit risk of E10, the guarantor of I05, and the note is rated BBB+. This follows I05's rating after A29.
**Q34.** No. E12 has no parent, and E10's group is headed by E09.
**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.
**Q36.** 2: E02 and E04. E03 is a duplicate record of E02.
**Q37.** 331 distinct entities, counting non-QA records by LEI (and by record ID for the two sovereigns, which have no LEI).
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A, from A08 and A09.
**Q40.** 66 distinct GB-domiciled issuers.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** DE. The RATINGS record E10 holds, over the LU in E17.
**Q43.** 1. Only E17, which is the RESEARCH duplicate of E10, is in LU, and the RATINGS record holds DE.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** No. I07 is local-currency debt, so the ceiling does not apply.
**Q46.** No. E11 only has a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an expected rating (A47, EX) and no assigned rating yet.
**Q48.** 106 instruments held a rating on 1 October 2026, with none withdrawn.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1053","E1144","E1298","E1159","E1243","E1057","E1080","E1034","E1169","E1093","E1064","E10","E1160","E1151","E1294","E1167","E1058","E1285","E1290","E1051","E08","E1186","E1112","E1300","E1163","E1213","E1228","E1229","E1255","E1263","E1307"]},
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
"Q18":{"issuers":["E1194","E1088","E1266","E1059","E1039","E1126","E1098","E1238","E1297","E1013","E1061","E1242","E1317","E1037","E1066","E1314","E1323","E1146","E1203","E1006","E1264","E1019","E1181","E1209","E1168","E1109","E06","E1133","E1260","E1132","E1099","E1267"]},
"Q19":{"issuers":["E1271","E1294","E1055","E1188","E1034","E1248","E01","E1118","E1064","E1263","E1228","E1261","E1059","E1211","E09","E1190","E1072","E1158","E1105","E1046","E1282","E1056","E1029","E1160","E1005","E1080","E1300","E1079"]},
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
"Q30":{"entities":["E1101","E1236","E05","E1028","E1126","E1039","E1194","E15"]},
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
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```