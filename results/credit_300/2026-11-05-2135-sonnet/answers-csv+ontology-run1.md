**Q1.** A-. Assigned A- (A01, 2024-03-12); the downgrade to BBB came later (A02, 2025-06-20).
**Q2.** No. The only 2026 actions on E01 are affirmations (A03 LTIDR, A04 STIDR).
**Q3.** No, BB+. The 2031 note is I02 (subordinated); it was downgraded to BB+ (A07, 2025-06-20).
**Q4.** Positive. Northwind's records E02 and E03 share an LEI, so they are one entity; its latest action is A09 (2025-09-15, affirmed A, POS).
**Q5.** The holder takes E02's risk (Northwind Holdings), rated A. I03 is guaranteed by E02, and E02's latest rating is A (A09).
**Q6.** Valdoria's Country Ceiling is BB (A12) and caps foreign-currency ratings. E05's FC rating is BB (A14), while its local-currency rating is BBB- (A13) and is not capped.
**Q7.** 31 issuers were downgraded in 2026, listed in the JSON. QA records are excluded, and RESEARCH records are folded into their RATINGS record (E1161→E1160, E1170→E1169, E1299→E1298).
**Q8.** E08. It was downgraded to RD (A22, 2026-07-08), which is a default.
**Q9.** 278. This counts distinct entities (merged by LEI, QA excluded) whose latest LTIDR action is not a withdrawal, and it includes the sovereign CV. I treated E1279 as still rated, since its local-currency rating was never withdrawn (A1594 withdrew only the FC basis).
**Q10.** Depends. E05's local-currency rating is BBB- (investment grade) but its foreign-currency rating is BB (speculative).
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).
**Q12.** A-. This is the 2023-01-15 assignment (A34).
**Q13.** One downgrade (A36). The watch (A35) and affirmation (A33) are not downgrades.
**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).
**Q15.** A-. E10 was assigned A- (A26) and downgraded to BBB+ only on 2026-04-15 (A27).
**Q16.** No. It has been BBB+ since A36 (2024-09-30); A35 (watch) and A33 (affirmation) left it unchanged.
**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.
**Q18.** 32 entities, listed in the JSON. Each one's latest action on its rating is a Watch Negative. E1059 and E1019 are on watch on the LC basis only, and E1209 is the entity behind record E1210.
**Q19.** 28 entities, listed in the JSON. Each one's latest action carries a Negative outlook. An RW action carries no outlook, so I counted none for entities whose latest action was a Watch.
**Q20.** No. E07 was assigned BB and later withdrawn (A19, "commercial reasons"); a withdrawal is not a default.
**Q21.** 35 entities, listed in the JSON. Each has a withdrawal as its latest action. E1158, E1115 and E1303 are not included because later actions re-established a rating.
**Q22.** E08 only. It reached RD in A22; no other action in the data is RD or D.
**Q23.** F2 (A04, affirmed 2026-02-10).
**Q24.** Yes. BBB is investment grade (A03).
**Q25.** 66 instruments held an investment-grade rating. Expected (EX) actions do not count as ratings.
**Q26.** A+ (A40).
**Q27.** A-. I06 is rated A- (A42).
**Q28.** BBB+ (A38). This is not the Country Ceiling, which is A (A37).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** Eight entities were exactly at their country's ceiling: E05, E1028, E1101, E1126, E1236 at VD's BB, and E15, E1039, E1194 at CV's A. E1279's FC rating is withdrawn, and E1245 is domiciled in FR per RESEARCH record E1246.
**Q31.** No. Every FC rating in VD and CV is at or below its ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The holder takes E10's risk (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).
**Q34.** No. E12 has no parent, while E10 sits in the E09 group.
**Q35.** 3 entities: E09, E10 and E11. E17 is a second record of E10.
**Q36.** 2 entities: E02 (with its duplicate record E03) and E04.
**Q37.** 331. There are 370 records, less 13 QA records and 26 duplicate records sharing an LEI.
**Q38.** No. They have different LEIs (E06 and E13).
**Q39.** A (A09).
**Q40.** 66 GB-domiciled issuers held an issuer rating, using the same rated-issuer rule as Q9.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile and says LU, overriding the RATINGS record's DE.
**Q43.** 1 entity: E10, through E17.
**Q44.** Yes. I07 is in XVD, the domestic currency of E05's country, VD.
**Q45.** No. The ceiling applies only to foreign-currency debt, and I07 is local-currency.
**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected action (A47), so it remains unrated.
**Q48.** 106 instruments held a rating. Nine have only an EX action and no assignment: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1228","E1034","E1307","E1159","E1160","E1167","E1186","E1169","E1263","E1298","E1300","E1285","E1255","E1243","E1290","E1093","E1080","E1057","E1053","E1144","E1294","E1112","E1051","E1229","E1151"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1109","E1264","E1168","E1006","E1209","E1260","E1133","E1088","E1013","E1037","E1061","E1066","E1098","E1099","E1126","E1132","E1146","E1181","E1194","E1203","E1238","E1266","E1297","E1314","E1317","E1323","E1059","E1019"]},
"Q19": {"issuers": ["E01","E09","E1034","E1046","E1056","E1029","E1079","E1118","E1158","E1228","E1261","E1263","E1271","E1294","E1300","E1080","E1053","E1055","E1059","E1064","E1160","E1105","E1190","E1282","E1248","E1072","E1005","E1211"]},
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