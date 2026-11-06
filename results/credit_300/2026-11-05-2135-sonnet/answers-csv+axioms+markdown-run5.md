**Q1.** A-. E01's LTIDR (FC) was assigned A- on 2024-03-12 (A01), and the downgrade to BBB came on 2025-06-20 (A02).
**Q2.** No. E01's only 2026 action is an affirmation (A03/A04), and only DG counts as a downgrade.
**Q3.** No, it is BB+. I02 is subordinated and was downgraded to BB+ on 2025-06-20 (A07).
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (AF, POS, 2025-09-15).
**Q5.** E02, rated A. I03 is guaranteed by E02, and E02/E03's current LTIDR is A (A08, A09).
**Q6.** Valdoria's Country Ceiling is BB (A12), and it caps E05's foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13) and is not capped.
**Q7.** 30 entities had a DG on an issuer rating in 2026, including E08, E10 and E1160. They are listed in the JSON. QA records are excluded. Instrument downgrades such as A29 are not counted.
**Q8.** E08. It went to RD on 2026-07-08 (A22), which is a default.
**Q9.** 278. This counts distinct entities (merged by LEI, QA excluded) whose latest LTIDR/STIDR action on some basis is not a withdrawal. I tallied it by hand from the action list, so it could be off by a few. E1279 still counts because only its FC rating was withdrawn (A1594) and its LC rating stands.
**Q10.** Depends. E05 is BBB- in local currency (A13), which is investment grade, but BB in foreign currency (A14), which is not.
**Q11.** BBB+. It was set by the downgrade on 2024-09-30 (A36), and the Watch on 2025-11-20 came later.
**Q12.** A-, from A34.
**Q13.** 1. Only A36 is a DG, and the Watch (A35) and affirmation (A33) are not downgrades.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01, after that date.
**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26) and downgraded on 2026-04-15 (A27).
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33).
**Q17.** No. E06's only 2026 action is a Watch (A17), and the rating is unchanged.
**Q18.** 32 entities had a latest action that was a Watch Negative, including E06, E1006 and E1109. They are listed in the JSON. I included E1019 and E1059, whose watch is on the LC rating.
**Q19.** 27 entities had a latest action with a Negative outlook (E01, E09, E1158 and others, listed in the JSON). Entities whose latest action was a Watch, an upgrade, an affirmation to Stable, or a withdrawal are excluded.
**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.
**Q21.** 35 entities. E07 and 34 E1xxx entities had every issuer rating withdrawn before 2026-10-01 and no later re-rating. They are listed in the JSON.
**Q22.** E08 only. It is the only RD or D rating in the data (A22).
**Q23.** F2, from A04.
**Q24.** Yes. E01's LTIDR is BBB (A03).
**Q25.** 66. Of the 115 instruments, 66 had an INST rating of BBB- or better in force. This is a hand count.
**Q26.** A+, from A40.
**Q27.** A- (A42).
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.
**Q30.** E05, E1028, E1101, E1126 and E1236 at the VD ceiling of BB. E15, E1039 and E1194 at the CV ceiling of A. E1245 is excluded because its RESEARCH record puts it in FR.
**Q31.** No. Every FC rating for VD- and CV-domiciled companies is at or below the ceiling (BB for VD, A for CV).
**Q32.** E09. The chain is E11 to E10 to E09, and E09 has no parent.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose LTIDR became BBB+ on 2026-04-15 (A27).
**Q34.** No. E12 has no parent link to E09.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 (the same entity as E03) and E04.
**Q37.** 331. There are 370 records, of which 13 are QA test data and 26 are RESEARCH duplicates sharing an LEI. The 2 sovereigns, which have no LEI, are counted as entities.
**Q38.** No. Their LEIs differ.
**Q39.** A (A09).
**Q40.** 66. This counts GB-domiciled entities with an issuer rating still in force. It is a hand count.
**Q41.** None. E16 is a QA record, so it and its actions are ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, and E10 and E17 share an LEI.
**Q43.** 1. Only the E10/E17 entity is domiciled in LU.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where E05 is domiciled.
**Q45.** No. I07 is rated BBB- (A45), but it is local-currency debt, which the ceiling does not cap.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is unrated until an AS action confirms it.
**Q48.** 106. Of the 115 instruments, 9 have only an EX action and are unrated: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1307","E1228","E1285","E1034","E1186","E1167","E1160","E1159","E1263","E1255","E1300","E1290","E1294","E1298","E1080","E1112","E1093","E1057","E1053","E1144","E1243","E1229","E1051","E1169"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1133","E1088","E1168","E1194","E1203","E1006","E1109","E1264","E1099","E1126","E1019","E1059","E1013","E1037","E1061","E1066","E1098","E1146","E1181","E1209","E1238","E1266","E1297","E1314","E1317","E1323","E1260","E1132"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1079","E1064","E1029","E1046","E1034","E1072","E1190","E1248","E1271","E1228","E1261","E1263","E1160","E1294","E1300","E1080","E1282","E1105","E1005","E1055","E1059","E1188"]},
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
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
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