**Q1.** A-. E01's A- (A01, 2024-03-12) was still in force until the downgrade to BBB (A02) on 2025-06-20.
**Q2.** No. The only 2026 action on E01 was an affirmation at BBB with a Negative outlook (A03, 2026-02-10).
**Q3.** No, BB+. I02 was downgraded from BBB to BB+ on 2025-06-20 (A07), which is sub-investment grade.
**Q4.** Positive. E03 is the same entity as E02 (same LEI) and carries the later action, A09 (2025-09-15, A, Positive), which supersedes A08 (Stable).
**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes E02's credit risk (A08/A09, I03 rated A).
**Q6.** Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings. E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13).
**Q7.** 44 issuers had a downgrade action in 2026, listed in the JSON, including E08, E10 and E16. This includes duplicate records such as E1170, which is a research copy of E1169.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and E07's withdrawal (A19) is not a default.
**Q9.** 289. This counts distinct LEIs with a latest long-term issuer rating that is not a withdrawal, as of 2026-10-01, so duplicate records are merged. The count includes the two sovereigns, CV and VD, and it is sensitive to that choice.
**Q10.** Depends. E05 is BBB- (investment grade) in local currency but BB (not investment grade) in foreign currency (A13/A14).
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the 2025-11-20 action (A35) was only a watch.
**Q12.** A-. E14 held A- from A34 (2023-01-15) until A36.
**Q13.** 1. The only downgrade of E14 is A36.
**Q14.** None. E12's first rating (A30) is dated 2024-02-01, after the requested date.
**Q15.** A-. E10 was A- (A26) until the downgrade to BBB+ on 2026-04-15 (A27). E17 is a research duplicate of E10, since it shares E10's LEI.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A36, A35, A33).
**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17), not a downgrade.
**Q18.** 32 issuers, listed in the JSON, including E06.
**Q19.** 37 issuers, listed in the JSON, including E01 and E09.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.
**Q21.** 37 entities, listed in the JSON, including E07. Their latest rating before 2026-10-01 is a withdrawal, or they had no valid rating by that date.
**Q22.** E08 only. It was downgraded to CCC (A21) and then to RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 66. This counts instruments whose latest rating is investment grade, excluding expired or withdrawn ratings.
**Q26.** A+ (A40, local-currency basis).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling of BB (A12), not an issuer rating.
**Q30.** E15 and E1039 and E1194 at the CV ceiling of A, plus E05, E1028, E1101, E1126 and E1236 at the VD ceiling of BB.
**Q31.** No. No company in CV or VD has a foreign-currency rating above its country's ceiling of A and BB respectively.
**Q32.** E09. E11's parent is E10, and E10's parent is E09.
**Q33.** E10, rated BBB+. I05 is issued by E11 but guaranteed by E10, whose issuer rating (A27) and I05's rating (A29) are both BBB+.
**Q34.** No. E12 has no parent link, whereas E10 sits under E09.
**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.
**Q36.** 2: E02 and E04. E03 is a duplicate of E02.
**Q37.** 344. There are 370 entity records with 342 distinct LEIs, and the two sovereigns have no LEI.
**Q38.** No. They have different LEIs, countries (E06 DE, E13 US) and entity records.
**Q39.** A. E02 and E03 are the same entity, and the latest action (A09) affirmed A.
**Q40.** 74. This counts distinct LEIs among GB-domiciled entities with a valid issuer rating as of 2026-10-01.
**Q41.** BB+. E16 was downgraded from BBB- on 2026-06-01 (A44).
**Q42.** DE. E10 is domiciled in Germany; E17's LU record is a research duplicate with the same LEI.
**Q43.** 1. Only the record E17 is LU, and it appears to duplicate E10, so this depends on whether duplicates count.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.
**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but the ceiling applies to foreign-currency ratings and I07 is a local-currency obligation.
**Q46.** No. E11 has only a Corporate Obligation rating of BBB (A46), not an issuer rating.
**Q47.** None. I08's A rating was expired on 2026-09-01 (A47).
**Q48.** 106. This counts instruments with a current, non-expired and non-withdrawn rating on 2026-10-01.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":289},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```