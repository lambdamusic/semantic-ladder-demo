**Q1.** A-. The A01 rating (A-, assigned 2024-03-12) held until the A02 downgrade on 2025-06-20.

**Q2.** No. The only 2026 action on Kestrel Energy (E01) is A03, an affirmation at BBB with the outlook moved to Negative.

**Q3.** No, it is BB+. The 2031 note (I02) is subordinated and was downgraded to BB+ by A07.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (2025-09-15, POS).

**Q5.** A holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and both I03 (A11) and E02 (A08) are rated A.

**Q6.** Not answerable from the data. The records show Valdoria Telecom (E05) at BB foreign-currency (A14) and BBB- local-currency (A13). The Valdoria Country Ceiling is BB (A12), which is consistent with a cap on the FC rating, but no comment gives the reason.

**Q7.** Thirty-one issuers had a downgrade in 2026 (listed in the JSON). RESEARCH records are mapped to the RATINGS record of the same LEI.

**Q8.** E08. A22 set it to RD on 2026-07-08, and no later action followed.

**Q9.** 278. This counts distinct entities (by LEI) with a current, non-withdrawn LTIDR or STIDR, QA records excluded.

**Q10.** Depends. Its FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. The DG on 2024-09-30 (A36) set it, and the later actions did not change the rating.

**Q12.** A-. A34 set it on 2023-01-15, before the A36 downgrade.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10's downgrade to BBB+ (A27) is dated 2026-04-15, after that date.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 and A33 did not change the rating.

**Q17.** No. Orrin Bank's only 2026 action is A17, a Rating Watch Negative at A-, which is not a downgrade.

**Q18.** Thirty-two issuers were on Rating Watch Negative on 1 October 2026 (listed in the JSON).

**Q19.** Twenty-eight issuers had a Negative outlook on 1 October 2026 (listed in the JSON), including E01 and E09.

**Q20.** No. Pellam Retail (E07) was rated BB, and A19 withdrew the rating for commercial reasons, which is not a default.

**Q21.** Thirty-five entities (listed in the JSON), all with a withdrawal as their latest action and no later rating.

**Q22.** E08, which went CCC to RD. No other record carries RD or D.

**Q23.** F2, from A04.

**Q24.** Yes. Its LTIDR is BBB (A03).

**Q25.** 66. These are instruments whose latest non-EX action by 1 October 2026 is investment grade.

**Q26.** A+, from A40.

**Q27.** A-. I06 was assigned A- by A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12, BB) and no issuer rating.

**Q30.** Eight entities were at their ceiling: five in VD at BB and three in CV at A (listed in the JSON).

**Q31.** No. No FC rating of a VD or CV entity is above its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** A holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and both I05 (A29) and E10 (A27) were cut to BBB+ in 2026.

**Q34.** No. Halden Foods (E12) has no parent and no link to the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 331 distinct LEI-based entities, with QA records excluded.

**Q38.** No. E06 and E13 have different LEIs and no shared parent.

**Q39.** A, from A08 and A09.

**Q40.** 66.

**Q41.** None. Brindle Capital (E16) is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds; the RESEARCH duplicate E17 says LU.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, domiciled in DE per RATINGS.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB- and is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47), so it remains unrated.

**Q48.** 106.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1159","E1057","E1298","E1243","E1053","E1144","E1058","E1167","E1285","E1290","E1080","E1307","E1228","E1263","E1255","E1229","E1034","E1169","E1163","E1213","E1300","E1151","E1294","E10","E1160","E1051","E1064","E1093","E08","E1112","E1186"]},
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
"Q18":{"issuers":["E1037","E1317","E1242","E1209","E1238","E1297","E1061","E1013","E1266","E1039","E1059","E1194","E1088","E1314","E1066","E1146","E1323","E1203","E1132","E1260","E1099","E1133","E06","E1181","E1109","E1168","E1264","E1006","E1019","E1267","E1126","E1098"]},
"Q19":{"issuers":["E1005","E1080","E01","E1118","E1064","E1261","E1271","E1046","E1059","E1282","E1056","E1263","E1228","E1211","E09","E1105","E1158","E1079","E1160","E1029","E1248","E1034","E1188","E1300","E1055","E1294","E1072","E1190"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1320","E1206","E1219","E1316","E1244","E1205","E1121","E1048","E1084","E1166","E07","E1021","E1277","E1234","E1225","E1233","E1200","E1218","E1063","E1138","E1107","E1041","E1140","E1062","E1007","E1032","E1159","E1253","E1308","E1057","E1155","E1172","E1124","E1001","E1076"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1039","E1028","E1236","E1126","E1101","E15","E1194"]},
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
"Q48":{"count":106}}
```