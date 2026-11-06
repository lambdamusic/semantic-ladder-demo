**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB (A03, A04); the downgrade was in 2025 (A02).

**Q3.** No, BB+. The 2031 note is I02 (subordinated), cut from BBB to BB+ on 2025-06-20 (A23, A07).

**Q4.** POS (Positive). E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (2025-09-15, A, POS), which supersedes A08 (STA).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and I03 is rated A (A10, A11).

**Q6.** Likely the sovereign Country Ceiling. VD's CC is BB (A12), and E05's foreign-currency rating is BB (A14) while its local-currency rating is BBB- (A13). The data does not state the rule explicitly, so this is an inference.

**Q7.** 42 entities had a downgrade (DG) in 2026, listed in the JSON.
- I counted LTIDR actions only, mapping research duplicates to the RATINGS record (E1161→E1160, E1170→E1169, E1299→E1298).
- I excluded E1341, whose downgrade (A1720) is dated 2026-11-09, after today.

**Q8.** E08. It was downgraded to RD ("distressed debt exchange completed") on 2026-07-08 (A22).

**Q9.** 290, though this is uncertain.
- This counts distinct entities (duplicates merged by LEI) with a non-withdrawn LTIDR on 2026-10-01.
- E1115, E1158 and E1303 have rating actions dated after their withdrawal (A1251/A1250, A1339/A1338, A1650/A1649). I treated the latest dated action as current. If withdrawal is final, the count is 287.

**Q10.** Depends. E05 is BBB- in local currency (investment grade, A13) but BB in foreign currency (not, A14).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36), and nothing changed before 2025-06-01.

**Q12.** A- (A34, assigned 2023-01-15).

**Q13.** 1. The only DG on E14 is A36.

**Q14.** None. E12's first action is 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in 2023 (A26); the downgrade to BBB+ came on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35 is a watch, A33 an affirmation).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17), not a downgrade.

**Q18.** 32 entities, listed in the JSON. I took each entity whose latest action on or before 2026-10-01 is an RW action, which carries RWN. Some watches are old (e.g. E1267, from 2023) with no later action in the data. E1019 and E1059 are on watch in local currency only.

**Q19.** 33 entities, listed in the JSON. Each has a NEG outlook on its latest action on or before 2026-10-01. E1059's NEG is its foreign-currency outlook (A1129, filed under duplicate E1060). Downgrades dated after 2026-10-01 (E1341, E1346, E1349) are excluded.

**Q20.** No. E07's rating was withdrawn for "commercial reasons" (A19), not for default; its last rating was BB.

**Q21.** 36 entities, listed in the JSON. All had a rating and then a WD action on or before 2026-10-01. E1106 is excluded because only its local-currency rating was withdrawn (A1230). E1115, E1158 and E1303 are excluded because of the post-withdrawal anomaly noted under Q9.

**Q22.** E08, the only entity ever rated RD (A22).

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66 instruments. Of the 106 rated instruments on 2026-10-01, 66 are rated BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38, CV foreign-currency LTIDR).

**Q29.** None. VD has only a Country Ceiling record (A12, BB) and no issuer rating (LTIDR).

**Q30.** 8 entities: E05, E1028, E1101, E1126, E1236 (ceiling BB, VD) and E15, E1039, E1194 (ceiling A, CV).
- Ceilings exist only for VD (BB, A12) and CV (A, A37).
- E1307 is excluded because its latest rating is BB-.

**Q31.** No. No VD or CV company has a foreign-currency rating above its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is issued by E11 but guaranteed by E10 (instruments.csv), and it was downgraded to BBB+ along with E10 (A27, A29).

**Q34.** No. E12 has no parent_id and no link to E09 or E10, so the data shows only a shared name.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 370 records, and 26 are RESEARCH-source duplicates sharing an LEI with another record.

**Q38.** No. E06 and E13 have different LEIs and countries (DE vs US).

**Q39.** A (A08, A09).

**Q40.** 73 distinct GB-domiciled entities held an issuer rating on 2026-10-01 (72 if withdrawal is final, as in Q9).

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE. E10 (RATINGS source) says DE, while the duplicate E17 (RESEARCH source) says LU; I used the RATINGS record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record says DE.

**Q44.** Yes, probably. I07 is denominated in XVD, which is not a standard code and looks like Valdoria's local currency (VD). Its BBB- rating matches E05's local-currency rating (A45, A13).

**Q45.** No. The BB ceiling constrains foreign-currency ratings, and I07 appears to be a local-currency obligation.

**Q46.** No. E11 has only a CO-type rating (A46) and no LTIDR.

**Q47.** None. I08 has only an EX action (A47, A, 2026-09-01). The data does not define EX (expired or expected), so no standing rating can be confirmed.

**Q48.** 106 instruments. I counted those with an assignment (AS) on or before 2026-10-01. Eight instruments (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046) and I1049 have only an EX action and are excluded.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 290},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1109","E1006","E1088","E1264","E1168","E1019","E1209","E1099","E1146","E1013","E1181","E1037","E1061","E1059","E1066","E1266","E1260","E1126","E1132","E1238","E1098","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1351","E1347","E1350","E1348","E1344","E1343","E1342","E1340","E1345","E1300","E1046","E1034","E1029","E1056","E1059","E1064","E1079","E1160","E1190","E1228","E1263","E1261","E1271","E1248","E1294","E1005","E1282","E1211","E1072"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
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
"Q37": {"count": 344},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 73},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```