**Q1.** A-. Kestrel's FC LTIDR was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. A03 (2026-02-10) is an affirmation with the outlook revised to Negative, which is not a downgrade.

**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ by A07.

**Q4.** Positive. E02 and E03 share an LEI, and the latest action is A09 (2025-09-15, Positive).

**Q5.** The credit risk is E02's, rated A. I03 is guaranteed by E02, whose LTIDR is A (A08, A09).

**Q6.** The FC rating is capped by Valdoria's Country Ceiling, which is BB (A12). Valdoria Telecom's FC rating is BB (A14) and its LC rating is BBB- (A13), and LC ratings are not capped.

**Q7.** 31 issuers had a DG action on their LTIDR in 2026, listed in the JSON. QA record E16 is excluded.

**Q8.** E08. It went to RD on 2026-07-08 (A22) after a distressed debt exchange.

**Q9.** 278. This counts distinct LEIs whose latest LTIDR on each basis on 1 Oct 2026 is not WD, with QA records excluded.

**Q10.** Depends. The FC rating is BB (speculative grade) and the LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 (2024-09-30) downgraded it from A-.

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 was in force until the downgrade A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; the Watch (A35) and the affirmation (A33) did not change the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch.

**Q18.** 32 issuers, listed in the JSON. Each has a latest action that is a Rating Watch Negative; a Watch holds until the next action.

**Q19.** 29 issuers, listed in the JSON. Each has a latest outlook of Negative. I excluded E1057 and E1172 because their ratings were withdrawn.

**Q20.** No. E07's rating was withdrawn (A19, WD), and a withdrawal is not a default.

**Q21.** 35 entities, listed in the JSON. Each had an LTIDR at some point, and its latest action on every basis is a withdrawal.

**Q22.** E08 only. It is the only non-QA record that ever reached RD or D (A22).

**Q23.** F2, from A04.

**Q24.** Yes. The issuer rating is BBB.

**Q25.** 66, counting the latest INST rating per instrument and ignoring EX actions.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities, listed in the JSON. Country Ceilings are A for CV and BB for VD, and these entities' FC ratings equal them.

**Q31.** No. No FC rating among CV or VD entities exceeds its ceiling.

**Q32.** E09, via E11 to E10 to E09.

**Q33.** The credit risk is E10's, rated BBB+. I05 is guaranteed by E10, which A27 downgraded to BBB+.

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3. The group is E09, E10 (E17 is the same LEI) and E11.

**Q36.** 2. The group is E02 (E03 is the same LEI) and E04.

**Q37.** 331 distinct entities, counting non-QA records by LEI, or by record ID where there is no LEI.

**Q38.** No. They have different LEIs.

**Q39.** A.

**Q40.** 66. This is an aggregate query for GB-domiciled issuers on 1 Oct 2026 and I did not inspect individual rows.

**Q41.** None. E16 is a QA record.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, which is E10 and is domiciled in DE per RATINGS.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. It is local-currency debt, so the ceiling does not apply.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an EX action (A47), so it is still unrated.

**Q48.** 106, counting instruments with a non-EX, non-WD INST rating on 1 Oct 2026.

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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E05","E1028","E1101","E1126","E1236"]},
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
"Q48":{"count":106}
}
```