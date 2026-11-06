**Q1.** A-. E01 was assigned A- (A01) and not downgraded to BBB until A02 on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03 (affirmed BBB, outlook moved to Negative). The downgrade (A02) was in 2025.

**Q3.** No, BB+. The 2031 note is I02, a subordinated note. A07 downgraded it to BB+ on 2025-06-20, after A23 had assigned BBB.

**Q4.** Positive. E03 shares E02's LEI, so it is the same company. A09 (2025-09-15) affirmed A with a Positive outlook and supersedes A08 (Stable).

**Q5.** The guarantor, E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and A08/A09 give E02 an A rating.

**Q6.** Valdoria's country ceiling (A12, sovereign Country Ceiling BB) caps foreign-currency ratings at BB. E05's FC rating is BB (A14), while its LC rating is BBB- (A13).

**Q7.** 31 issuers had a downgrade (DG) action in 2026. E1169, E1160 and E1298 are the canonical IDs for duplicate records E1170, E1161 and E1299. I excluded QA-source test records (E16, E1340–E1351) and actions dated after today (e.g. A1720).

**Q8.** E08. A22 moved it to RD on 2026-07-08, and no later action changes that.

**Q9.** 269. This counts distinct issuers (duplicate records merged by LEI) whose latest LTIDR action on or before 2026-10-01 is not WD. QA records are excluded. The count includes E08, which is at RD.

**Q10.** Depends. E05 is BBB- in local currency (investment grade, A13) but BB in foreign currency (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ by A36 on 2024-09-30. The 2025-11-20 action (A35) is only a watch.

**Q12.** A-. This is from A34, assigned 2023-01-15 and before A36.

**Q13.** 1. The only downgrade of E14 is A36.

**Q14.** None. E12's first rating (A30, BB-) is dated 2024-02-01, after the question date.

**Q15.** A-. E10 was assigned A- (A26) and downgraded to BBB+ only on 2026-04-15 (A27). E17 is a duplicate record of E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). The RWN watch in A35 was resolved without a rating change.

**Q17.** No. E06's only 2026 action (A17) is a Rating Watch Negative placement with the rating still A-.

**Q18.** 32 issuers were on Rating Watch Negative, because their last action was a watch placement and no later action cleared it. E1019 and E1059 are on watch for their local-currency rating only.

**Q19.** 26 issuers had a Negative outlook, taken from each entity's latest LTIDR action on or before 2026-10-01. Entities whose latest action is a watch (RW), a withdrawal (WD) or a later Stable/Positive outlook are excluded.

**Q20.** No. E07 has a rating withdrawal (A19, "commercial reasons"), not a default.

**Q21.** 36 entities. Each had an LTIDR rating but its latest action is a withdrawal (WD) on or before 2026-10-01. Entities withdrawn and later re-rated (E1115, E1158, E1303) are not included.

**Q22.** E08 only. It is the only entity with an RD rating (A22).

**Q23.** F2. This is the short-term rating (STIDR) affirmed in A04.

**Q24.** Yes. E01's long-term rating is BBB (A03), which is investment grade.

**Q25.** 66. This is the number of instruments rated BBB- or higher on 2026-10-01. Instruments with only an EX action are not counted, because EX looks like an expected or provisional rating that the data does not define.

**Q26.** A+. This is E15's local-currency rating from A40.

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. This is CV's foreign-currency LTIDR (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** 8 entities have an FC rating exactly at the ceiling. VD's ceiling is BB (A12) and CV's is A (A37). Their FC ratings are: E05 BB, E1028 BB, E1101 BB, E1126 BB, E1236 BB, E15 A, E1039 A and E1194 A.

**Q31.** No. No VD or CV company has an FC rating above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10 (Halden Bank AG), rated BBB+. I05 is issued by E11 but guaranteed by E10. E10 was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent link, and only the name suggests a connection. E10 sits under E09.

**Q35.** 3. The group is E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2. The group is E02 and E04. E03 is a duplicate record of E02.

**Q37.** 331. This is 370 records, less 26 RESEARCH duplicates (same LEI as a RATINGS record), less 13 QA-source records. If QA records count as real entities, the figure is 344.

**Q38.** No. They have different LEIs, countries and names.

**Q39.** A, as described in Q4.

**Q40.** 66 distinct GB-domiciled issuers hold an issuer rating.

**Q41.** None. E16 exists only as a QA-source record. Its last QA action (A44) was BB+, but I treat it as non-production data.

**Q42.** DE. The RATINGS record E10 says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of the DE-domiciled E10.

**Q44.** Yes. I07 is in XVD, which looks like Valdoria's currency. Its BBB- rating (A45) matches E05's LC rating (A13).

**Q45.** No. The ceiling limits foreign-currency ratings, and I07 is a local-currency instrument. It is not above the ceiling.

**Q46.** No. E11 has only a credit opinion (A46, CO). Its notes (I05) are rated through the guarantee.

**Q47.** None. I08 has only an EX action (A47, A). I read EX as an expected rating, not a rating in force.

**Q48.** 106. This is I01–I07 plus 99 of the I10xx instruments. Eight instruments with only an EX action are excluded: I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1034","E1228","E1186","E1167","E1169","E1160","E1159","E1307","E1263","E1285","E1229","E1300","E1290","E1144","E1112","E1093","E1080","E1057","E1053","E1051","E1151","E1243","E1255","E1298","E1294"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 269},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1133","E1194","E1203","E1006","E1099","E1088","E1109","E1264","E1059","E1181","E1209","E1132","E1146","E1168","E1098","E1066","E1061","E1260","E1266","E1126","E1037","E1013","E1297","E1314","E1317","E1323","E1238","E1019"]},
"Q19": {"issuers": ["E01","E09","E1118","E1158","E1079","E1056","E1034","E1228","E1282","E1046","E1029","E1190","E1263","E1294","E1300","E1160","E1271","E1053","E1080","E1064","E1261","E1059","E1072","E1211","E1005","E1105"]},
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
"Q30": {"entities": ["E05","E15","E1028","E1101","E1126","E1236","E1039","E1194"]},
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