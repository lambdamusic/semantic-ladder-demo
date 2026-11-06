**Q1.** A-. E01's last action before 1 Jan 2025 was A01 (A-); the downgrade to BBB (A02) came on 2025-06-20.
**Q2.** No. E01's only 2026 action is A03, an affirmation with a Negative outlook, which is not a downgrade.
**Q3.** No. The 2031 note I02 is subordinated and was downgraded to BB+ by A07, which is speculative grade.
**Q4.** Positive. E02 and E03 share an LEI and are one entity; its latest action is A09 (E03, 2025-09-15), which affirmed A with a Positive outlook.
**Q5.** The holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, whose issuer rating is A, and I03 itself is rated A (A11).
**Q6.** Valdoria's Country Ceiling is BB (A12). The FC rating (A14, BB) is capped by it, while the LC rating (A13, BBB-) is not.
**Q7.** 31 issuers had a downgrade in 2026 (see JSON). I took these from DG actions on issuer ratings dated in 2026, excluding QA records. The query was cut off at 60 seconds in one round, so the list may be incomplete.
**Q8.** E08. A22 on 2026-07-08 moved it to RD, which is a default, and nothing came after.
**Q9.** 261. This counts distinct LEIs (record ID where there is no LEI) whose latest long-term issuer action on or before 2026-10-01 is not a withdrawal.
**Q10.** Depends. The FC rating is BB, which is speculative grade, but the LC rating is BBB-, which is investment grade.
**Q11.** BBB+. The downgrade A36 on 2024-09-30 set it, and it held through 2025-06-01.
**Q12.** A-. A34 assigned it on 2023-01-15.
**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 is an affirmation.
**Q14.** None. E12's first rating action is A30 on 2024-02-01.
**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). I used E10 and ignored E17, which has the same LEI.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 did not change it).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative, which is not a downgrade.
**Q18.** 32 issuers, listed in the JSON. Each has a Watch as its latest action on its currency basis, with no later action up to 2026-10-01.
**Q19.** 30 issuers, listed in the JSON. Each has a Negative outlook as the latest outlook set, with no later outlook change or withdrawal.
**Q20.** No. E07 was withdrawn on 2026-05-12 (A19), which is not a default.
**Q21.** 36 entities, listed in the JSON. Each has a withdrawal as its latest long-term action before 2026-10-01, with no later action under its own record or LEI. E1106 is excluded because only its LC rating was withdrawn.
**Q22.** E08, the only entity with an RD or D rating (A22).
**Q23.** F2, from A04.
**Q24.** Yes. E01's rating is BBB, which is investment grade.
**Q25.** 66. This counts instruments whose latest non-EX action leaves them at BBB- or higher on 2026-10-01.
**Q26.** A+, from A40.
**Q27.** A-. I06 was assigned A- by A42 and has had no later action.
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** 8 entities, listed in the JSON. Their FC ratings equal the ceiling for their domicile: A for CV and BB for VD. About 25 rows of the CV/VD query were not shown, so this list may be incomplete.
**Q31.** No. Every CV and VD entity I could see has an FC rating at or below its ceiling, though the unseen rows leave a small gap.
**Q32.** E09. E11 has E10 as parent, and E10 has E09, which has no parent.
**Q33.** The holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27; the credit opinion on E11 is not a rating.
**Q34.** No. E12 has no parent link to E09 or E10.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 331, counting distinct LEIs (record ID for the sovereigns, which have none) and excluding QA records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A, from A09.
**Q40.** 66.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile over the RATINGS record E10 (DE).
**Q43.** 1. Only E17 (LU) exists, and it is the same entity as E10.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an expected rating (A47, EX), so it stays unrated.
**Q48.** 106. This counts instruments with a non-EX, non-withdrawn latest rating on 2026-10-01.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1299","E1307","E1213","E1080","E1285","E1112","E1263","E1064","E1163","E1053","E1051","E1300","E10","E1034","E1229","E1144","E1159","E1057","E1228","E1294","E1058","E1093","E1161","E1170","E1290","E1167"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":261},
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
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236"]},
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