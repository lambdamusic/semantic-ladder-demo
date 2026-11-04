**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with the outlook moved to Negative, which is not a downgrade.
**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.
**Q4.** Positive (POS). E02 and E03 share an LEI, so they are the same entity, and the latest action is A09 (2025-09-15, A, POS).
**Q5.** The holder takes the credit risk of Northwind Holdings (E02), rated A. The notes (I03) are issued by the finance subsidiary E04 but guaranteed by E02, and I03 is rated A (A10, A11).
**Q6.** Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings. E05's FC rating is BB (A14), while its LC rating is BBB- (A13) because local-currency ratings are not capped.
**Q7.** The list is in the JSON; it covers issuers with a DG action on a LTIDR or STIDR in 2026.
**Q8.** Saxby Shipping (E08) was in default on 2026-10-01. It was downgraded to RD on 2026-07-08 (A22).
**Q9.** 278 distinct issuers hold an LTIDR or STIDR, counting RESEARCH duplicates once by LEI and excluding QA and withdrawn ratings. This count includes the two sovereigns, which hold LTIDRs.
**Q10.** Depends. E05's foreign-currency rating is BB (speculative) and its local-currency rating is BBB- (investment grade).
**Q11.** BBB+. Marlow (E14) was downgraded to BBB+ on 2024-09-30 (A36), and the later actions A35 and A33 kept it there.
**Q12.** A-. This is the rating from A34 (2023-01-15), before the downgrade.
**Q13.** One downgrade (A36).
**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).
**Q15.** A-. Halden Bank (E10) was downgraded to BBB+ only on 2026-04-15 (A27).
**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A35 was a watch and A33 an affirmation).
**Q17.** No. Orrin Bank (E06) only had a Rating Watch Negative placed on 2026-09-03 (A17), which is not a downgrade.
**Q18.** The list is in the JSON.
**Q19.** The list is in the JSON; it covers LTIDRs with a NEG outlook on that date.
**Q20.** No. Pellam Retail (E07) was withdrawn on 2026-05-12 (A19) for commercial reasons, which is not a default.
**Q21.** The list is in the JSON.
**Q22.** Only E08.
**Q23.** F2 (A04).
**Q24.** Yes. Kestrel's LTIDR is BBB (A03).
**Q25.** 66 instruments, excluding EX-only instruments and those of QA issuers.
**Q26.** A+ (A40).
**Q27.** A-. The 2032 note (I06) is rated A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria (VD) only has a Country Ceiling (A12), which is not an issuer rating.
**Q30.** The list is in the JSON.
**Q31.** No. No company's FC rating exceeds its country's ceiling.
**Q32.** Halden Group plc (E09), via E11 to E10 to E09.
**Q33.** The holder takes the credit risk of Halden Bank (E10), the guarantor of I05. I05 is rated BBB+ (A29), in line with E10's BBB+ (A27).
**Q34.** Yes only if E12 belongs to the group, and the data does not say so. E12 has no parent, so on the data E12 is not in the Halden group.
**Q35.** 4. These are E09, E10, E11 and E12, counting E12 only as the question's own premise.
**Q36.** 2. E02 and E03 are the same entity (same LEI), plus E04.
**Q37.** 331 distinct legal entities, deduplicated by LEI and excluding QA records.
**Q38.** No. They have different LEIs (E06 and E13).
**Q39.** A (A09 via E03, same entity as E02).
**Q40.** 66.
**Q41.** None. E16 is a QA record, so it and its actions are ignored.
**Q42.** DE. The RATINGS record E10 holds; the RESEARCH record E17 says LU.
**Q43.** 0. The only LU record is E17, which is the same entity as E10, and the RATINGS record puts E10 in DE.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** Yes. I07 is rated BBB- (A45) against a ceiling of BB (A12), though a local-currency obligation isn't capped by the ceiling.
**Q46.** No. E11 only has a Credit opinion (A46), which is not a rating.
**Q47.** None. I08 only has an Expected rating (A47), so it is unrated.
**Q48.** 106 instruments.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1051","E1167","E1058","E1151","E1294","E1053","E1144","E1159","E1243","E1057","E1285","E1290","E1298","E1228","E1229","E1255","E1263","E1307","E1034","E10","E1160","E1080","E08","E1169","E1186","E1112","E1300","E1163","E1213","E1093","E1064"]},
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
"Q18":{"issuers":["E1039","E1059","E1266","E1317","E1209","E1242","E1037","E1006","E1264","E1019","E1323","E1066","E1314","E1146","E1203","E1181","E1133","E06","E1126","E1098","E1132","E1099","E1260","E1267","E1088","E1194","E1061","E1297","E1238","E1013","E1109","E1168"]},
"Q19":{"issuers":["E1228","E1263","E1271","E1034","E1188","E1248","E1282","E1056","E1059","E1079","E1294","E1055","E1105","E1158","E1160","E1029","E01","E1118","E1064","E1261","E1046","E1211","E09","E1005","E1080","E1190","E1072","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1048","E1084","E1206","E1219","E1320","E1062","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E07","E1021","E1166","E1041","E1063","E1107","E1138","E1140","E1218","E1277","E1244","E1316","E1200","E1225","E1233","E1234","E1121","E1205","E1001","E1124","E1172","E1076"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1126","E1101","E1236","E1028","E05","E1194","E1039","E15"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":4},
"Q36":{"count":2},
"Q37":{"count":331},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"none"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}}
```