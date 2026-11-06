**Q1.** A-. E01's long-term foreign-currency rating was set by A01 (A-, 2024-03-12) and unchanged until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB, and the 2026 short-term action A04 is also an affirmation. Its only downgrade, A02, was in 2025.

**Q3.** No. The 2031 note is I02 (subordinated), rated BB+ after the downgrade A07, which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15), an affirmation with a Positive outlook.

**Q5.** A holder takes E02's credit risk, since I03 is guaranteed by E02. E02 is rated A (A08, A09).

**Q6.** Valdoria Telecom (E05, domiciled in VD) has a foreign-currency rating of BB (A14) against a local-currency rating of BBB- (A13). Foreign-currency ratings are capped by the Valdoria Country Ceiling of BB (A12). Local-currency ratings are not capped.

**Q7.** 30 issuers had downgrades (DG) on their issuer ratings in 2026, listed in the JSON. Records from the QA system (E1340–E1351, E16) are excluded, and duplicate records are folded to the RATINGS record. A duplicate pair is two records with the same LEI, for example E1161 into E1160 and E1170 into E1169.

**Q8.** E08. It is the only issuer rated RD or D, from A22 (RD, 2026-07-08).

**Q9.** 278. About 313 distinct entities have ever held a long-term issuer rating, including the sovereign CV via A38/A39. I subtracted 35 whose latest action is a withdrawal. This is a long count over many records, so it could be off by a few.

**Q10.** Depends. Its foreign-currency rating is BB (speculative grade, A14), but its local-currency rating is BBB- (investment grade, A13).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and there is no later change before 1 June 2025.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12 was first assigned a rating in A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26 and was not downgraded until A27 on 2026-04-15. E17 is the same entity and has no actions.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). A35 (a Rating Watch) and A33 (an affirmation) are not changes.

**Q17.** No. E06's actions are A16 (assignment) and A17 (Rating Watch), and neither is a downgrade.

**Q18.** 32 issuers were on Rating Watch Negative, listed in the JSON. Each has a Watch action (RW) as its latest action on that basis. I excluded issuers whose Watch was followed by a later action, such as E1213, E1276 and E1158.

**Q19.** 26 issuers had a Negative outlook, listed in the JSON. I excluded issuers whose latest action is a Watch, because that action carries no outlook (for example E1132 and E1146).

**Q20.** No. E07's only actions are an assignment of BB (A18) and a withdrawal (A19), and a withdrawal is not a default.

**Q21.** 35 entities had their rating withdrawn before 1 October 2026 and had no later rating action, listed in the JSON. I excluded E1106, E1115, E1158, E1279 and E1303 because each still holds a rating on another basis or has a later rating action.

**Q22.** E08. It was downgraded to RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's current foreign-currency rating is BBB (A03).

**Q25.** 66. Of the 106 instruments with an assigned rating, 40 are speculative grade. EX-only instruments are unrated.

**Q26.** A+. A40 is the local-currency assignment for E15.

**Q27.** A-. I06 is rated A- in A42.

**Q28.** BBB+, from A38. The Country Ceiling of A (A37) is not the sovereign's rating.

**Q29.** None. VD only has a Country Ceiling (A12).

**Q30.** E05, E1101, E1236, E1126, E1028, E15, E1039 and E1194. The VD ceiling is BB and the CV ceiling is A (A12, A37). E1307 is at BB- after A1661, and E1245 is domiciled in FR per the RESEARCH record.

**Q31.** No. No VD or CV entity has a foreign-currency rating above BB or A respectively.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** A holder takes E10's credit risk, because I05 is guaranteed by E10. E10 is rated BBB+ after A27.

**Q34.** No. E12 has no parent link, so it is not in the group of E09, E10 and E11.

**Q35.** 3: E09, E10 (the same entity as E17) and E11.

**Q36.** 2: E02 (the same entity as E03) and its subsidiary E04.

**Q37.** 331. The data has 370 records, which I count as 351 numbered E1001–E1351, 17 numbered E01–E17, and 2 sovereigns (VD and CV). Removing 13 QA records leaves 357, and merging 26 LEI-duplicate pairs gives 331. This relies on the E1001–E1351 range being contiguous.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, from A09 and A08.

**Q40.** 66. This is a long count over GB-domiciled entities, so it could be off by a few.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. E10 says DE, but the RESEARCH record E17 holds for domicile and says LU.

**Q43.** 1. Only E10/E17 is domiciled in LU.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD, so it is local-currency debt.

**Q45.** No. I07 is rated BBB- (A45), but local-currency debt is not capped by the ceiling.

**Q46.** No. E11 is a finance subsidiary with no issuer-rating actions.

**Q47.** None. I08 has only an Expected action (A47, EX), so it stays unrated.

**Q48.** 106. There are 115 instruments, and 9 have only an Expected action: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1151","E1160","E1163","E1167","E1169","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1300","E1307","E1034","E1144","E1186"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 278},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1029","E1034","E1046","E1005","E1055","E1056","E1059","E1064","E1072","E1079","E1105","E1118","E1158","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1101","E1236","E1126","E1028","E15","E1039","E1194"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 331},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 66},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```