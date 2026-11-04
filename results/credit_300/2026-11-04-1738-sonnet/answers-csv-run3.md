**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until the downgrade on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with a Negative outlook (A03).

**Q3.** No, BB+. The 2031 note is I02 (subordinated), downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its A09 affirmation of A on 2025-09-15 supersedes the Stable outlook in A08.

**Q5.** E02, Northwind Holdings, rated A. I03 is issued by E04 but guaranteed by E02, and is rated A (A11).

**Q6.** The data points to the country ceiling. The Valdoria country ceiling is BB (A12), and E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13).

**Q7.** 43 issuers had a DG action dated in 2026 (list in the JSON). I counted DG actions up to today (2026-11-04), so E1349 (A1736) and E1346 (A1730) are in, and E1341 (A1720, dated 2026-11-09) is out. Duplicates are mapped to their canonical record, e.g. E1299 to E1298.

**Q8.** E08. Its last action is a downgrade to RD on 2026-07-08 (A22).

**Q9.** 291 by my count, so treat it as approximate. This is distinct canonical entities with a non-withdrawn issuer rating (LTIDR, either currency basis) on 2026-10-01. CV, QA-source records and E08 (RD) are included. VD is not, because it has only a country ceiling.

**Q10.** Depends. Local currency is BBB- (investment grade, A13) and foreign currency is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and was still BBB+ in June 2025.

**Q12.** A-. This is the rating assigned on 2023-01-15 (A34).

**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement and A33 an affirmation.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in 2023 (A26) and not downgraded to BBB+ until 2026-04-15 (A27). E17 is just a duplicate record.

**Q16.** No. E14 was BBB+ on 2025-01-01 and BBB+ now; the RWN (A35) was resolved by the affirmation on 2026-05-01 (A33).

**Q17.** No. E06 was only placed on Rating Watch Negative on 2026-09-03 (A17), with the rating still A-.

**Q18.** 32 issuers were on Rating Watch Negative on 2026-10-01 (list in the JSON). E1019 and E1059 are included on the strength of their local-currency watches.

**Q19.** 37 issuers had a Negative outlook on 2026-10-01 (list in the JSON). E1059 is included on its foreign-currency outlook. E1346 and E1349 are not, because their Negative outlooks start after 1 October (A1730, A1736).

**Q20.** No. E07's rating was withdrawn for commercial reasons on 2026-05-12 (A19), which is not a default.

**Q21.** 35 entities, listed in the JSON. Their last action by 2026-10-01 is a withdrawal. E1279 is excluded because it still has a local-currency rating.

**Q22.** E08, which reached RD on 2026-07-08 (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 68 instruments held an investment-grade rating on 2026-10-01. Instruments whose rating had ended by EX before that date (I08, I1008, I1012, I1021, I1046, I1049) are excluded. I1001, I1007 and I1015 have EX dates after 1 October, so I counted them as rated.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling of BB (A12) and no issuer rating.

**Q30.** E05, E15, E1028, E1039, E1101, E1126, E1194 and E1236. VD's ceiling is BB and CV's is A (A12, A37), and each of these has a foreign-currency rating exactly at it.

**Q31.** No. No foreign-currency rating exceeds BB for VD or A for CV; E1039's local-currency AA- (A81) is not a foreign-currency rating.

**Q32.** E09. E11 sits under E10, which sits under E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and both the note and E10 are BBB+ (A27, A29).

**Q34.** No. E12 has no parent link and is not under E09; only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 370 rows, less 26 duplicate rows that share an LEI with another row.

**Q38.** No. They have different LEIs, countries (DE vs US) and ratings records.

**Q39.** A (A08, A09).

**Q40.** 74 canonical GB-domiciled entities held an issuer rating on 2026-10-01.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE; the RESEARCH duplicate E17 says LU.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is DE.

**Q44.** Yes. I07 is denominated in XVD, which I take to be Valdoria's currency; the data does not define it.

**Q45.** No. The ceiling applies to foreign-currency ratings, and the note is local-currency at BBB- (A45).

**Q46.** No. E11 has only a counterparty rating (A46, CO).

**Q47.** None. I08 has a single action, EX on 2026-09-01 (A47, last rating A), which I read as ending the rating. The data doesn't define EX.

**Q48.** 109. That is 115 instruments less the 6 whose rating ended by EX before 2026-10-01.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 291},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1126","E1088","E1146","E1266","E1013","E1317","E1099","E1006","E1264","E1203","E1133","E1132","E1323","E1260","E1168","E1109","E1238","E1209","E1037","E1061","E1066","E1098","E1297","E1181","E1314","E1194","E1019","E1059"]},
"Q19": {"issuers": ["E01","E09","E1350","E1118","E1055","E1064","E1300","E1079","E1080","E1034","E1056","E1072","E1282","E1347","E1348","E1345","E1344","E1343","E1342","E1340","E1351","E1005","E1228","E1263","E1261","E1160","E1248","E1271","E1211","E1190","E1188","E1046","E1105","E1029","E1294","E1158","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 68},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 344},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 74},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 109}
}
```