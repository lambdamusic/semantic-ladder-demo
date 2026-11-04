**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01), and the next action, the downgrade A02, is dated 2025-06-20.

**Q2.** No. The only 2026 action on E01 is an affirmation (A03, A04), so no downgrade.

**Q3.** No. The 2031 note is I02, a subordinated note, downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. E03 shares its LEI with E02, so they are one entity, and A09 (2025-09-15) is the latest action: affirmed A, POS.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes E02's risk. E02's latest rating is A (A09, affirmed).

**Q6.** The Valdoria Country Ceiling is BB (A12) and caps foreign-currency ratings. E05's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13), which is not capped.

**Q7.** 31 issuers had a downgrade (DG) in 2026. Duplicate research records are mapped to the RATINGS record and QA records are excluded. The IDs are in the JSON.

**Q8.** E08. It was downgraded to RD (default) on 2026-07-08 (A22) and nothing followed.

**Q9.** 278. This counts distinct LEIs whose latest long-term issuer rating action on 2026-10-01 was not a withdrawal. Several entities had a withdrawal that was followed by a later action (E1158, E1115, E1303), and I treated those as rated. E1279 and E1106 kept a local-currency or foreign-currency rating after the other was withdrawn. This count was done by hand across a very large table, so treat it as less certain.

**Q10.** Depends. E05 is BB in foreign currency (A14, speculative) and BBB- in local currency (A13, investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and had no change before 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came later.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 an affirmation.

**Q14.** None. E12's first rating action is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 is a research duplicate of E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. E06 has only a Rating Watch Negative (RW) action in 2026 (A17), which is not a downgrade.

**Q18.** 32 issuers. This takes each issuer's latest long-term action on or before 2026-10-01 where it was a Rating Watch Negative placement. I included E1019 and E1059, whose local-currency rating is the one on watch. The IDs are in the JSON.

**Q19.** 26 issuers. This takes the latest outlook, carrying it forward through a watch action that has a blank outlook (E1146, E1132). The IDs are in the JSON.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19), which is not a default.

**Q21.** 35 entities. Each was assigned a long-term rating and ended with a withdrawal as its last action. The IDs are in the JSON; E1001 stands in for the E1002 research record.

**Q22.** E08, the only entity ever rated RD or D (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's current rating is BBB (A03).

**Q25.** 66. These are instruments whose latest rating on 2026-10-01 was BBB- or higher. Expected-rating (EX) records do not count.

**Q26.** A+ (A40).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38, CV foreign-currency issuer rating). The Country Ceiling of A (A37) is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05, E1028, E1101, E1126 and E1236 are at the Valdoria ceiling of BB. E15, E1039 and E1194 are at the Corvenia ceiling of A.

**Q31.** No. Every foreign-currency rating in VD or CV is at or below its ceiling.

**Q32.** E09 (E11 → E10 → E09).

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent and no link to E09 in the data; only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 331. That is 370 records, less 13 QA records and 26 duplicate research records.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled issuers, counting the RATINGS record's country.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 says DE and takes precedence over the research record E17 (LU).

**Q43.** 0. Only the research record E17 says LU, and it is overridden by the RATINGS record.

**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency.

**Q45.** No. I07 is BBB- (A45) against a ceiling of BB, but local-currency debt is not capped.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an expected rating (A47, EX), so it is unrated.

**Q48.** 106 instruments held a rating on 2026-10-01 (66 investment grade, 40 not).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1186","E1228","E1169","E1307","E1160","E1298","E1263","E1167","E1151","E1080","E1051","E1053","E1057","E1112","E1144","E1243","E1255","E1093","E1285","E1290","E1294","E1300","E1034","E1159","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1088","E1133","E1194","E1203","E1013","E1019","E1059","E1099","E1061","E1109","E1066","E1098","E1132","E1126","E1181","E1260","E1264","E1266","E1297","E1314","E1317","E1323","E1168","E1238","E1037","E1209","E1146"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1146","E1034","E1079","E1190","E1046","E1029","E1080","E1228","E1263","E1294","E1300","E1160","E1271","E1261","E1211","E1248","E1132","E1059","E1064","E1005","E1105"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1225","E1206","E1308","E1140","E1277","E1219","E1159","E1244","E1138","E1320","E1007","E1001","E1107","E1021","E1316","E1076","E1121","E1155","E1253","E1234","E1205","E1172","E1062","E1048","E1041","E1057","E1166","E1200"]},
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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```