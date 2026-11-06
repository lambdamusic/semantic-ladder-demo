**Q1.** A-. A01 (E01, long-term IDR A-, assigned 2024-03-12) was still in force on that date, because the downgrade in A02 came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook; the downgrade (A02) was in 2025.

**Q3.** No, it is BB+. The 2031 note is I02, a subordinated note, and A07 downgraded it to BB+ on 2025-06-20.

**Q4.** Positive. E03 is a duplicate record of E02 (same LEI), and its latest action is A09 (2025-09-15, affirmed A, Positive outlook).

**Q5.** The holder takes the risk of E02 (Northwind Holdings), the guarantor of I03, whose issuer is the finance subsidiary E04. E02 is rated A (A08, A09), and the note itself is A (A10, A11).

**Q6.** The data does not state a reason. It shows only A14 (foreign-currency BB) and A13 (local-currency BBB-), and the Valdoria country ceiling in A12 is BB. That fits a ceiling cap on foreign-currency ratings, but this is an inference.

**Q7.** 43 issuers had a downgrade of their issuer rating dated in 2026 (listed in the JSON).
- I excluded E1341 because its downgrade (A1720) is dated 2026-11-09, after today.
- I left out instrument-only downgrades such as I05.

**Q8.** E08 only. A22 downgraded it to RD on 2026-07-08, and nothing later cures it.

**Q9.** 289. I counted entities whose latest long-term IDR action by 2026-10-01 was not a withdrawal.
- Duplicate records sharing a LEI count once.
- E1115's later upgrade (A1250) is treated as overriding its earlier withdrawal (A1251), which may be a data anomaly.

**Q10.** Depends. Valdoria Telecom (E05) is BBB- on local currency (A13), which is investment grade, but BB on foreign currency (A14), which is not.

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-. A34 (2023-01-15) was the only rating in force before A36.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30, assigned 2024-02-01.

**Q15.** A-. E17 is a duplicate record of E10, and A26 (A-) was in force until the downgrade in A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35 is only a watch, and A33 affirms BBB+).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating unchanged at A-.

**Q18.** 31 entities were on Rating Watch Negative on 2026-10-01. Their watch was not resolved by a later affirmation, upgrade, downgrade or withdrawal. Some of these watches are old (for example A1076, 2022), but nothing in the data clears them.

**Q19.** 35 entities had a Negative outlook on 2026-10-01. I treated a Rating Watch as replacing the outlook, and I ignored actions dated after 2026-10-01.
- E1059 is included on the foreign-currency Negative outlook in A1129, which sits on its duplicate record E1060.
- E1261 is included via A1558 on its duplicate record E1262.

**Q20.** No. E07 was rated BB (A18) and then withdrawn for "commercial reasons" (A19). Withdrawal is not a default.

**Q21.** 37 entities, listed in the JSON. Each had a rating and its latest action by 2026-10-01 is a withdrawal. I used the canonical RATINGS IDs for E1001 (A1002 sits on duplicate E1002) and E1253 (A1540 sits on duplicate E1254).

**Q22.** E08 only (A22, RD).

**Q23.** F2 (A04, 2026-02-10).

**Q24.** Yes. E01 is BBB (A03).

**Q25.** 66 instruments. I excluded instruments whose only action is EX, because the data does not define EX and an expected or expired rating is not a held rating.

**Q26.** A+ (A40, local currency).

**Q27.** A- (A42 on I06, a subordinated note).

**Q28.** BBB+ (A38, foreign currency).

**Q29.** None. The only rating on VD is the Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** Eight entities: E05, E1028, E1101, E1126 and E1236 (Valdoria, ceiling BB) and E15, E1039 and E1194 (Corvenia, ceiling A). Each has a foreign-currency rating equal to the ceiling. These are the only two ceilings the data gives.

**Q31.** No. No foreign-currency rating exceeds the VD ceiling (BB) or the CV ceiling (A). A few local-currency ratings are higher, for example E1039 at AA-, but the ceiling applies to foreign currency.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes the risk of E10 (Halden Bank), the guarantor of I05. E10 is currently BBB+ (A27, 2026-04-15), and I05 is also BBB+ (A29).

**Q34.** Depends. E12 has no parent or ownership link in the data, and only the shared name "Halden" suggests a connection.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 370 entity records, of which 26 are duplicates sharing a LEI. This assumes every ID from E1001 to E1351 exists.

**Q38.** No. E06 and E13 have different LEIs and different countries (DE and US).

**Q39.** A (A08, and A09 on duplicate E03).

**Q40.** 74 issuers (listed in my count, not in the JSON). I counted GB-domiciled entities with a live long-term IDR on 2026-10-01, with duplicates merged.

**Q41.** BB+ (A44 downgraded E16 on 2026-06-01).

**Q42.** DE (E10). The duplicate record E17 says LU, which conflicts, so I used the RATINGS record.

**Q43.** 0. The only LU record is E17, which duplicates E10 (domiciled in DE); counted by record it would be 1.

**Q44.** Yes. I07 is denominated in XVD, which looks like Valdoria's currency, but the data does not define the code.

**Q45.** No. I07 is rated BBB- (A45), but a country ceiling caps foreign-currency obligations and this note is in local currency.

**Q46.** No. E11 has only a CO-type rating (A46, BBB) and no long-term IDR. The data does not define CO, so I read it as not an issuer rating.

**Q47.** None. I08's only record is A47, an EX action (A, 2026-09-01), which I read as an expected rather than a final rating. The data does not define EX.

**Q48.** 106 instruments, excluding the nine whose only action is EX.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 289},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320","E07"]},
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
"Q34": {"same_group": "depends"},
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
"Q48": {"count": 106}
}
```