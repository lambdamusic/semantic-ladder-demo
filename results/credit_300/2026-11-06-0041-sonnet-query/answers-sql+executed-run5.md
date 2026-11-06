**Q1.** A-. E01's LTIDR FC rating was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01 was affirmed at BBB with a Negative outlook on 2026-02-10 (A03), so there was no downgrade in 2026.

**Q3.** No, BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 has been rated A with a POS outlook since 2025-09-15 (A09).

**Q5.** E02 (Northwind Holdings) is the credit risk, rated A. I03 is issued by E04 but guaranteed by E02, and its credit_risk_of is E02. The instrument rating is A (A11) and E02's issuer rating is also A (A09).

**Q6.** Not in the JSON. The Valdoria country ceiling is BB (from 2025-04-01), which caps E05's foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13).

**Q7.** 31 issuers had a downgrade (DG) action in 2026, listed in the JSON. E1051 has two DG rows, both at A+, so one of them may not be a real step down.

**Q8.** E08. It was rated RD from 2026-07-08 (A22).

**Q9.** 278. This counts distinct entities with a current non-withdrawn LTIDR, after merging duplicate records, and includes the sovereign CV.

**Q10.** Depends. E05 is BB in foreign currency (sub-investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade is A36 on 2024-09-30; A35 is a watch action at the same rating.

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). The watch period in between did not change the rating.

**Q17.** No. E06 went on Rating Watch Negative at A- on 2026-09-03 (A17), which is not a downgrade.

**Q18.** 32 issuers were on RWN on 1 October 2026, listed in the JSON. This includes E1019 and E1059, whose watch is on the local-currency rating only.

**Q19.** 28 issuers had a Negative outlook, listed in the JSON, including E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (WD) on 2026-05-12 (A19), not set to a default grade.

**Q21.** 35 entities had an issuer rating at some point but none in force on 1 October 2026, listed in the JSON. They were all withdrawn, e.g. E07 (A19).

**Q22.** E08 only. It is the only entity with an RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's current issuer rating is BBB (A03).

**Q25.** 66 instruments held an investment-grade (BBB- or above) rating on 1 October 2026.

**Q26.** A+ (A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV LTIDR FC, A38).

**Q29.** None. The data has no ratings for VD; it only appears as a country with a ceiling of BB.

**Q30.** 8 entities were exactly at their country's ceiling: E05 (BB/BB), E1028, E1101, E1126, E1236 (all BB/BB), E1039, E1194 and E15 (all A/A).

**Q31.** No. Every foreign-currency issuer rating in VD or CV country was at or below its ceiling.

**Q32.** E09. E11's ultimate_parent_id is E09.

**Q33.** E10 (Halden Bank) is the credit risk, rated BBB+. I05 is issued by E11 but guaranteed by E10, and the instrument is BBB+ (A29), as is E10 (A27).

**Q34.** No. E12 (Halden Foods) has no parent, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 entities, after duplicate records are merged.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) are separate entities.

**Q39.** A (A09).

**Q40.** 66 distinct GB-domiciled entities held a non-withdrawn issuer rating.

**Q41.** None. No entity named Brindle Capital was found in the entities table.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is flagged local_currency = yes and is denominated in XVD.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has no ratings of its own; only its notes (I05) are rated.

**Q47.** None. I08 has no rating record.

**Q48.** 106 instruments held a non-withdrawn rating on 1 October 2026.

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
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E1244","E1316","E1007","E1032","E1057","E1155","E1159","E1308","E1138","E1206","E1219","E1320","E1218","E1001","E1200","E1225","E1233","E1234","E07","E1166","E1021","E1048","E1084","E1062","E1121","E1205","E1041","E1063","E1107","E1140","E1076","E1277","E1124","E1172","E1253"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1039","E1101","E1126","E1194","E1236","E15"]},
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