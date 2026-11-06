**Q1.** A-. E01's rating was A- (A01, 2024-03-12) until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation (A03/A04, 2026-02-10).

**Q3.** No. I02 is rated BB+ (A07 downgrade, 2025-06-20), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action is A09 (2025-09-15), an affirmation at A with a POS outlook.

**Q5.** E02's credit risk, rated A. I03 is guaranteed by E02, and E02/E03's current LTIDR is A.

**Q6.** Not a JSON field. The FC rating is BB (A14) because it is capped by Valdoria's Country Ceiling of BB (A12). The LC rating (A13) is BBB- and is not capped.

**Q7.** 31 issuers were downgraded in 2026 (QA records excluded, research duplicates mapped to the RATINGS record); they are listed in the JSON below.

**Q8.** E08 only. A22 (2026-07-08) downgraded it to RD, which is a default.

**Q9.** 278. This is my count of distinct non-QA entities with an issuer rating (LTIDR or STIDR) in force on 2026-10-01, with same-LEI records merged and withdrawn ratings excluded. It is a long manual tally.

**Q10.** No. E05's headline FC rating is BB (A14), though its LC rating is BBB- (A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36); the RW on 2025-11-20 came later.

**Q12.** A- (A34).

**Q13.** 1, the downgrade A36.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 and E17 are the same entity, and the A- from A26 held until the downgrade on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33 affirmation); the only downgrade, A36, came before 2025.

**Q17.** No. E06's only 2026 action is a Rating Watch placement (A17), which is not a downgrade.

**Q18.** 32 issuers had their latest action as a Rating Watch Negative. E1019 and E1059 are included on the strength of their LC series only.

**Q19.** 25 issuers. I used each issuer's latest action; actions that carry no outlook, such as RW, count as having no Negative outlook.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19), which is not a default.

**Q21.** 35 entities. Each has a withdrawal as its last action on every basis and no later rating.

**Q22.** E08 only (A22, RD).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is BBB (A03).

**Q25.** 66 instruments held an investment-grade rating on 2026-10-01: 5 among I01–I07 and 61 among I1001–I1107.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities have an FC rating exactly at their country's ceiling. The ceilings are VD BB and CV A.

**Q31.** No. No FC rating of a company domiciled in VD or CV is above its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ (A27).

**Q34.** No. E12 has no parent, while E10 belongs to E09's group.

**Q35.** 3: E09, E10 (E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 330. That is 369 records, less 13 QA records and 26 same-LEI duplicates.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A08, A09).

**Q40.** 66 GB-domiciled issuers hold an issuer rating, using research domicile where it differs.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding DE on E10.

**Q43.** 1 (the Halden Bank entity, E10/E17).

**Q44.** Yes. I07 is in XVD, VD's domestic currency, and its issuer E05 is domiciled in VD.

**Q45.** No. I07 is local-currency debt (BBB-, A45), so the ceiling does not cap it.

**Q46.** No. E11 only has a Credit opinion (A46), which is not a rating.

**Q47.** None. I08 only has an Expected rating (A47) and no Assigned action.

**Q48.** 106 instruments held a rating. That is 115 instruments less 8 with only an EX action (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049 less I08 counted already, so 9 unrated in total). Treat this count as approximate.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 278},
"Q10": {"investment_grade": "no"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1118","E1158","E1228","E1282","E1248","E1271","E1029","E1046","E1056","E1079","E1034","E1064","E1080","E1190","E1261","E1263","E1294","E1300","E1005","E1160","E1072","E1059","E1105"]},
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
"Q37": {"count": 330},
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