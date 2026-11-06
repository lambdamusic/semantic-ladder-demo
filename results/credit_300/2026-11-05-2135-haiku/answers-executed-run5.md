**Q1.** A-. E01's A- rating (A01) ran from 2024-03-12 to 2025-06-20, which covers 1 Jan 2025.

**Q2.** No. The only 2026 action on E01 was an affirmation (A03, Feb 2026) that moved the outlook to Negative while the rating stayed BBB; the last downgrade was A02 (2025-06-20).

**Q3.** No, it is rated BB+. The 2031 note is I02, whose current INST rating is BB+ (DG from 2025-06-20).

**Q4.** Positive. Northwind Holdings (E02) has a current LTIDR FC rating of A with outlook POS (A09).

**Q5.** The holder takes credit risk of E02 (Northwind Holdings), rated A. I03 has credit_risk_of = E02 and E02's current rating is A (A09).

**Q6.** The foreign-currency rating is capped by Valdoria's country ceiling of BB (ceilings.csv, VD, from 2025-04-01), while the local-currency rating of BBB- (E05 LC) is not. The data gives the ceiling but does not state the mechanism explicitly, so this is an inference. (Q6 has no JSON field.)

**Q7.** E08, E10, E1034, E1051, E1053, E1057, E1058, E1064, E1080, E1093, E1112, E1144, E1151, E1159, E1160, E1163, E1167, E1169, E1186, E1213, E1228, E1229, E1243, E1255, E1263, E1285, E1290, E1294, E1298, E1300, E1307. These are rating-level drops in 2026 (e.g. E08 B→CCC, E1051 AA-→A+). Two of them carry non-DG action labels (E1064 AF, E1290 AF), so the list relies on the rating values rather than the action field.

**Q8.** E08. Its current rating is RD (A22, from 2026-07-08), the only default rating in the data.

**Q9.** 278. This counts entities with a current LTIDR rating that is not WD, including the sovereign CV, and excludes the 35 entities whose current rating is WD.

**Q10.** Depends. E05's FC rating is BB, which is not investment grade, while its LC rating is BBB-, which is.

**Q11.** BBB+. E14's rating from 2024-09-30 to 2025-11-20 was BBB+ (A36).

**Q12.** A-. E14's rating from 2023-01-15 to 2024-09-30 was A- (A34).

**Q13.** 1. The only downgrade action on E14 is A36 (DG, 2024-09-30, A- to BBB+).

**Q14.** None. E12's first rating (BB-, A-series) starts on 2024-02-01, after 1 Jan 2024.

**Q15.** A-. E10's rating from 2023-05-01 to 2026-04-15 was A- (A26).

**Q16.** No. E14 stayed at BBB+ throughout; the RWN watch (A35) and AF affirmation (A33) did not change the rating.

**Q17.** No. E06 was rated A- throughout 2026, with only a Rating Watch Negative placed on 2026-09-03 (A17).

**Q18.** E06, E1006, E1013, E1019, E1037, E1039, E1059, E1061, E1066, E1088, E1098, E1099, E1109, E1126, E1132, E1133, E1146, E1168, E1181, E1194, E1203, E1209, E1238, E1242, E1260, E1264, E1266, E1267, E1297, E1314, E1317, E1323. Each has a current watch value of RWN.

**Q19.** E01, E1005, E1029, E1034, E1046, E1055, E1056, E1059, E1064, E1072, E1079, E1080, E1105, E1118, E1158, E1160, E1188, E1190, E1211, E1228, E1248, E1261, E1263, E1271, E1282, E1294, E1300. Each has a current outlook of NEG.

**Q20.** No. E07's current rating is WD (withdrawn), not RD.

**Q21.** E07, E1001, E1007, E1021, E1032, E1041, E1048, E1057, E1062, E1063, E1076, E1084, E1107, E1121, E1124, E1138, E1140, E1155, E1159, E1166, E1172, E1200, E1205, E1206, E1218, E1219, E1225, E1233, E1234, E1244, E1253, E1277, E1308, E1316, E1320. Each has a current rating of WD.

**Q22.** E08. It is the only entity with an RD rating.

**Q23.** F2. E01's short-term rating is F2 (STIDR, A04, from 2026-02-10).

**Q24.** Yes. E01's current FC issuer rating is BBB (A03), which is investment grade.

**Q25.** 66. These are the instruments whose current INST rating is BBB- or higher, counting I01, I03, I05, I06, I07 and the I10xx instruments.

**Q26.** A+. E15's current LC rating is A+ (A40).

**Q27.** A-. I06 (the 2032 note) is rated A- (A42).

**Q28.** BBB+. CV's current FC issuer rating is BBB+ (A38).

**Q29.** None. VD (Republic of Valdoria) has no rating record in ratings.csv; only its ceiling is given.

**Q30.** E05, E15, E1028, E1101, E1126, E1194, E1236. Each has a current FC rating equal to its country's ceiling: BB for VD, A for CV.

**Q31.** No. No VD company has an FC rating above BB, and no CV company has one above A.

**Q32.** E09. E11's chain is E10 then E09, and E09 is the ultimate parent.

**Q33.** E10, rated BBB+. I05 (the 2028 note) has credit_risk_of = E10, and E10's current rating is BBB+ (A29).

**Q34.** No. E12 has no parent or ultimate parent in the data, and E10 sits under E09. The shared "Halden" name is not evidence of common ownership.

**Q35.** 3. The Halden group is E09 (parent), E10 and E11. E12 is not linked.

**Q36.** 2. The Northwind group is E02 (parent) and E04.

**Q37.** 331. That is the number of rows in entities.csv, including the two sovereigns CV and VD.

**Q38.** No. They have different IDs, LEIs and countries (DE vs US), and no parent link.

**Q39.** A. E02's current LTIDR FC rating is A (A09).

**Q40.** 65. These are GB-domiciled entities with a current non-WD LTIDR rating. E07, E1007, E1021, E1062, E1124, E1200 and E1057 are excluded because they are withdrawn.

**Q41.** None. "Brindle Capital" does not appear in the data.

**Q42.** LU. E10 is domiciled in Luxembourg.

**Q43.** 1. Only E10 is domiciled in LU.

**Q44.** Yes. I07 (the 2027 note) has local_currency = yes.

**Q45.** No. I07 is rated BBB-, which is numerically above the BB ceiling, but it is a local-currency obligation, and the ceiling applies to foreign-currency ratings.

**Q46.** No. E11 has no LTIDR record in ratings.csv.

**Q47.** None. I08 (the 2034 note) has no rating record.

**Q48.** 106. That is 7 I01–I07 instruments plus 99 I10xx instruments, all with current INST ratings.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "Positive"},
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
  "Q19": {"issuers": ["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
  "Q30": {"entities": ["E05","E15","E1028","E1101","E1126","E1194","E1236"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 331},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 65},
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