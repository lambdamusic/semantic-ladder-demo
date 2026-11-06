**Q1.** A-. E01's latest action on or before 2025-01-01 is A01 (A-); the downgrade A02 came in June 2025.

**Q2.** No. A03 (2026-02-10) is an affirmation with a negative outlook, and the outlook is not a downgrade.

**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. Northwind Holdings E02 and NORTHWIND HLDGS E03 share a LEI, so they are one entity, and A09 (2025-09-15) affirms A with a positive outlook.

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk; A09 and A11 both give A.

**Q6.** The Valdoria Country Ceiling is BB (A12) and caps foreign-currency ratings. E05's foreign-currency rating is therefore BB (A14), while its local-currency rating, which is uncapped, is BBB- (A13).

**Q7.** 31 issuers. These are the entities with a DG action on an issuer rating dated 2026. They are listed in the JSON, with duplicate research records mapped to their RATINGS ID and QA records excluded.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, a default, and nothing later changes that.

**Q9.** 278. This is 300 distinct rated entities in the E1001–E1324 range plus 12 early ones, minus the 34 in that range whose latest action is a withdrawal; the count is hand-derived. E1279 keeps its local-currency rating after its foreign-currency withdrawal.

**Q10.** Depends. E05 is BB (speculative) in foreign currency and BBB- (investment grade) in local currency.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action, A35, is only a Watch.

**Q12.** A-, from A34.

**Q13.** 1 time, by A36.

**Q14.** None. Halden Foods' first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10 and E17 share a LEI, and the downgrade A27 only came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ after A35 (Watch) and A33 (affirmed).

**Q17.** No. A17 is a Rating Watch placement, which leaves the rating unchanged.

**Q18.** 32 issuers. Their latest action on the relevant basis is a Rating Watch Negative that no later action has cleared. They are listed in the JSON.

**Q19.** 26 issuers. Their latest issuer-rating action carries a Negative outlook. Where the latest action is a Watch or withdrawal the outlook field is blank, so those are excluded.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which says nothing about default.

**Q21.** 35 entities, listed in the JSON. Each had a rating and its latest action is a withdrawal.

**Q22.** E08 only. It is the only entity ever rated RD or D (A22).

**Q23.** F2, from A04.

**Q24.** Yes. E01's long-term rating is BBB (A03), which is investment grade.

**Q25.** 66 instruments. This is a count of instruments whose latest INST rating is BBB- or higher, excluding the 9 that only have an Expected (EX) action.

**Q26.** A+, from A40. Local-currency ratings are not capped.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities, listed in the JSON. Valdoria's ceiling is BB (A12) and Corvenia's is A (A37).

**Q31.** No. No foreign-currency rating exceeds BB for VD entities or A for CV entities. Gater Holdings (E1245) is not a CV entity because its RESEARCH record E1246 gives domicile FR.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ by A27 (the instrument's own A29 agrees).

**Q34.** No. Halden Foods E12 has no parent, while Halden Bank sits under E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10, since they share a LEI.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331. There are 370 records; I removed 26 duplicate-LEI records and 13 QA records (E16 and E1340–E1351).

**Q38.** No. The LEIs differ (549300AMVE… vs 815600O8X8…).

**Q39.** A, from A09.

**Q40.** 66. This is a hand count of GB-domiciled rated entities with no final withdrawal.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding DE on E10.

**Q43.** 1 (Halden Bank).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), and the ceiling does not apply to local-currency debt.

**Q46.** No. E11 is a finance subsidiary and only has a credit opinion (A46), which is not a rating.

**Q47.** None. I08 only has an Expected action (A47), so it is still unrated.

**Q48.** 106. There are 115 instruments, of which 9 have only an Expected action or none.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1034","E1228","E1112","E1159","E1169","E1186","E1167","E1151","E1160","E1093","E1080","E1057","E1051","E1053","E1144","E1263","E1255","E1285","E1294","E1298","E1300","E1290","E1243","E1307","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1146","E1264","E1168","E1019","E1209","E1109","E1260","E1037","E1098","E1181","E1013","E1323","E1126","E1132","E1314","E1266","E1297","E1317","E1238","E1061","E1066","E1059","E1099"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1228","E1034","E1046","E1029","E1064","E1190","E1055","E1080","E1261","E1263","E1294","E1300","E1271","E1248","E1160","E1079","E1005","E1059","E1211","E1282","E1072"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1225","E1206","E1308","E1140","E1320","E1159","E1277","E1219","E1244","E1107","E1234","E1205","E1007","E1021","E1076","E1121","E1062","E1155","E1172","E1138","E1166","E1200","E1001","E1253","E1316","E1041","E1057","E1048"]},
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