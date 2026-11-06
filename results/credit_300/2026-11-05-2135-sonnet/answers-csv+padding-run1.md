**Q1.** A-. A01 (E01, 2024-03-12) set A-; the downgrade A02 came on 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03 (2026-02-10), which affirmed BBB with a Negative outlook.
**Q3.** No, BB+. The 2031 note is I02 (subordinated), downgraded to BB+ by A07, below the BBB- cut-off.
**Q4.** POS. E03 is a RESEARCH duplicate of E02 (same LEI), and A09 (2025-09-15) affirmed A with a Positive outlook.
**Q5.** E02, the guarantor of I03, rated A (A08/A09; the note I03 is also A per A11).
**Q6.** The data doesn't state the reason. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The FC rating equals the Valdoria country ceiling of BB (VD, A12), which is consistent with the FC rating being capped by the ceiling.
**Q7.** 44 issuers have a DG action dated 2026 (listed in the JSON). I mapped RESEARCH duplicates to their RATINGS record and excluded A1720 (E1341, dated 2026-11-09, after today).
**Q8.** E08. A22 (2026-07-08) took it to RD with no later action.
**Q9.** 290 by my count, with duplicates merged and withdrawn issuers excluded. VD (country-ceiling rating only) and CO-only entities are not counted. Treat this as approximate.
**Q10.** Depends. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (not investment grade, A14).
**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action is A35 on 2025-11-20.
**Q12.** A-. A34 (2023-01-15) is the only action before that date.
**Q13.** 1. Only A36 is a downgrade on E14.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. A26 (E10, 2023) set A-, and the downgrade A27 came on 2026-04-15. E17 is a duplicate record with no actions.
**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). The 2025-11-20 Rating Watch Negative (A35) did not change the rating.
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with A- unchanged.
**Q18.** 32 issuers (listed in the JSON). The latest action on each is a Rating Watch Negative. E1019 and E1059 are included only on LC-rating watches (A1041/A1042, A1132).
**Q19.** 37 issuers (listed in the JSON), based on the latest FC outlook being Negative. E1158 is included even though its latest action follows a withdrawal.
**Q20.** No. E07 was withdrawn for commercial reasons (A19), and nothing shows a default rating.
**Q21.** 36 entities had a rating that was later withdrawn with no later rating action (listed in the JSON).
**Q22.** E08 only, via the RD rating in A22.
**Q23.** F2 (A04, E01 STIDR).
**Q24.** Yes. E01's LTIDR is BBB (A03).
**Q25.** 66. Of the 106 instruments rated on 2026-10-01, 40 are BB+ or lower.
**Q26.** A+ (A40, E15 LC).
**Q27.** A- (A42, I06).
**Q28.** BBB+ (A38, CV FC).
**Q29.** None. VD has only a country-ceiling rating of BB (A12) and no issuer rating.
**Q30.** E05, E1028, E1101, E1126, E1236 (VD ceiling BB) and E15, E1039, E1194 (CV ceiling A).
**Q31.** No. No VD or CV company has an FC rating above its ceiling.
**Q32.** E09. E11's parent is E10, and E10's parent is E09.
**Q33.** E10, the guarantor of I05, rated BBB+ (A27; I05 is also BBB+ per A29).
**Q34.** No. E12 has no parent, while E10 sits under E09.
**Q35.** 3: E09, E10, E11. E17 duplicates E10.
**Q36.** 2: E02 and E04. E03 duplicates E02.
**Q37.** 344. The file has 370 rows, and 26 are duplicates sharing an LEI with another row.
**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).
**Q39.** A (A09, via the duplicate E03 of E02).
**Q40.** 74 by my count.
**Q41.** BB+ (A44, 2026-06-01).
**Q42.** DE (E10). E17 is a RESEARCH duplicate (same LEI) that conflicts by showing LU.
**Q43.** 0. The only LU row is E17, a duplicate of E10, whose RATINGS record says DE.
**Q44.** Yes. I07 is in XVD, Valdoria's currency (an inference from the code), and its BBB- matches E05's LC rating.
**Q45.** No. The ceiling limits FC ratings, and this note is an LC obligation (A45 BBB-).
**Q46.** No. E11 only has a CO rating (A46).
**Q47.** None. I08 has only an EX action (A47, 2026-09-01), and the data doesn't define EX. I read it as not a final rating, but it carries A.
**Q48.** 106 instruments (7 from I01–I07 and 99 from the I1xxx range). The 8 with only EX actions are excluded.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16","E1064","E1058","E1163","E1213","E1228","E1350","E1346","E1347","E1307","E1034","E1112","E1159","E1349","E1160","E1186","E1285","E1348","E1263","E1344","E1343","E1340","E1342","E1345","E1300","E1290","E1298","E1294","E1243","E1255","E1167","E1093","E1080","E1057","E1053","E1144","E1051","E1169","E1229","E1151","E1351","E1052"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":290},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1019","E1037","E1039","E1059","E1061","E1066","E1006","E1013","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1055","E1064","E1005","E1029","E1034","E1046","E1056","E1059","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
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
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```