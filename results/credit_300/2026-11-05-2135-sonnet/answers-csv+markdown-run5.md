**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12) until A02 (2025-06-20).
**Q2.** No. E01's only 2026 action is A03, an affirmation (BBB, outlook NEG).
**Q3.** No, BB+. I02 is rated BB+ after A07, a downgrade from BBB in A23.
**Q4.** Positive. A09 (2025-09-15) is on E03, which has the same LEI as E02, so both records are one entity.
**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest rating is A (A09).
**Q6.** Valdoria's Country Ceiling (A12) is BB, and it caps FC ratings only. E05's FC rating is BB (A14) and its LC rating is BBB- (A13).
**Q7.** 30 issuers had a 2026 downgrade (DG); the list is in the JSON. I used the RATINGS-record ID and ignored QA records.
**Q8.** E08. A22 (2026-07-08) moved it to RD.
**Q9.** 278. 313 distinct entities ever held an LTIDR; 35 of them had withdrawn it by 1 Oct 2026.
**Q10.** Depends. E05's LC rating is BBB- (investment grade) but its FC rating is BB (not).
**Q11.** BBB+. A36 (2024-09-30) lowered E14 to BBB+, and A35 (2025-11-20) only placed it on Watch.
**Q12.** A-, from A34.
**Q13.** 1, which is A36.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. E10 and E17 share an LEI, so they are one entity, and its downgrade to BBB+ (A27) came on 2026-04-15.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).
**Q17.** No. E06 has only a Watch (A17), and Orrin Bancorp (E13) is a different entity.
**Q18.** 32 issuers; the list is in the JSON. These are entities whose latest LTIDR action is a Rating Watch, including LC-only Watches on E1019 and E1059.
**Q19.** 26 issuers; the list is in the JSON. An issuer counts if its latest LTIDR action carries a NEG outlook.
**Q20.** No. A19 is a withdrawal for commercial reasons, not a default.
**Q21.** 35 entities; the list is in the JSON. All had an LTIDR withdrawn (WD) before 1 Oct 2026 with no FC or LC rating left.
**Q22.** E08 only, via RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. BBB is investment grade.
**Q25.** 66. Of the 106 rated instruments, 40 are speculative grade.
**Q26.** A+ (A40).
**Q27.** A- (A42). This is below the CV ceiling of A.
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** E05, E1028, E1101, E1126, E1236 (all FC BB, ceiling BB), and E15, E1039, E1194 (all FC A, ceiling A).
**Q31.** No. No VD or CV entity has an FC rating above its ceiling.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** The holder takes E10's credit risk (I05 is guaranteed by E10), rated BBB+ (A27).
**Q34.** No. E12 has no parent and is not in E09's group.
**Q35.** 3: E09, E10 (same entity as E17) and E11.
**Q36.** 2: E02 (same entity as E03) and E04.
**Q37.** 331. That is 16 core entities plus 315 from E1001–E1339, after merging same-LEI records and excluding QA.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A08 and A09).
**Q40.** 66 GB issuers. No country conflicts affect GB records.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 overrides E10's DE.
**Q43.** 1, which is E10/E17.
**Q44.** Yes. I07 is in XVD, VD's domestic currency.
**Q45.** No. I07 is a local-currency instrument, so the ceiling does not apply.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is unrated.
**Q48.** 106. Nine instruments have only an Expected rating or none: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049.

Three entities (E1115, E1158, E1303) have a withdrawal dated before later actions. I treated them as rated because the latest action holds.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1064","E1058","E1163","E1213","E1186","E1228","E1307","E1112","E1169","E1159","E1263","E1285","E1160","E1167","E1080","E1034","E1051","E1053","E1057","E1093","E1144","E1298","E1294","E1300","E1290","E1255","E1229","E1243"]},
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
"Q18":{"issuers":["E06","E1267","E1242","E1039","E1088","E1133","E1194","E1203","E1006","E1109","E1264","E1099","E1168","E1019","E1059","E1132","E1126","E1146","E1181","E1209","E1037","E1061","E1066","E1098","E1013","E1238","E1260","E1266","E1297","E1317","E1314","E1323"]},
"Q19":{"issuers":["E01","E09","E1158","E1118","E1056","E1228","E1079","E1282","E1263","E1261","E1248","E1271","E1046","E1034","E1029","E1053","E1072","E1294","E1300","E1080","E1190","E1059","E1105","E1188","E1064","E1005"]},
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