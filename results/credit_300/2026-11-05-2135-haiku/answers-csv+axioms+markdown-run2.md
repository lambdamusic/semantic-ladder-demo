**Caveat:** I worked these by hand from the records and did not run the SHACL/SPARQL rules. Counts over the whole book (Q9, Q19, Q25, Q40, Q48) are not settled by my pass, so I've left them null. Lists in Q7, Q18, and Q21 come from a manual scan and may have omissions. Some actions are dated after today (2026-11-06), but none of them changes an answer.

**Q1.** A-
A01 (2024-03-12, AS, FC) is the latest FC long-term rating on or before 2025-01-01; the next action, A02, is dated 2025-06-20.

**Q2.** No.
The 2026 actions on E01 are A03 and A04, both affirmations (AF), not downgrades.

**Q3.** No; BB+.
I02 (2031 note) was rated BBB in A23 and cut to BB+ in A07 (2025-06-20), its latest instrument action.

**Q4.** Positive.
E02 and its duplicate E03 are the same LEI, so the latest action (A09, 2025-09-15, AF, outlook POS) governs.

**Q5.** E02; A.
I03 is guaranteed by E02, so the holder takes E02's credit risk, and its latest instrument rating is A (A11).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling (VD, BB, A12). The local-currency rating (A13, BBB-) is not capped. Q6 has no JSON field in the spec, so it is answered here only.

**Q7.** E08, E10, E1034, E1051, E1053, E1057, E1058, E1064, E1080, E1093, E1112, E1144, E1151, E1159, E1161, E1163, E1167, E1170, E1186, E1213, E1228, E1229, E1243, E1255, E1263, E1285, E1290, E1294, E1299, E1300, E1307 (31 issuers; instrument I05 was also downgraded but is not an issuer).
These are DG actions dated 2026 on non-QA issuer records.

**Q8.** E08.
A22 (2026-07-08, DG, RD) is a default rating, and no later action reverses it.

**Q9.** Not settled. Counting every entity's rating state at 2026-10-01 needs the full rule run.

**Q10.** No.
The headline FC rating is BB (A14); the LC rating BBB- (A13) is not the headline.

**Q11.** BBB+.
A36 (2024-09-30, DG to BBB+) is the latest rating on or before 2025-06-01.

**Q12.** A-.
A34 (2023-01-15, AS, A-) is the latest rating on or before 2024-01-01.

**Q13.** 1.
E14 has one DG action (A36, 2024); A35 is a Rating Watch, which is not a downgrade.

**Q14.** None.
E12's first rating (A30) is dated 2024-02-01, after 2024-01-01.

**Q15.** A-.
A26 (A-) is the latest E10 action on or before 2026-01-01; A27 (DG to BBB+) is dated 2026-04-15.

**Q16.** No.
The last rating change before 2025-01-01 is A36 (BBB+); later actions A35 (RW) and A33 (AF) leave it at BBB+.

**Q17.** No.
E06 (Orrin Bank AG) had no downgrade in 2026; A17 is a Rating Watch. E13 (Orrin Bancorp) is a different LEI.

**Q18.** E06, E059 is LC-only, so: E1059, E06, E1013, E1019, E1037, E1039, E1061, E1066, E1088, E1098, E1099, E1109, E1126, E1132, E1133, E1146, E1181, E1194, E1203, E1210, E1238, E1242, E1260, E1264, E1266, E1267, E1297, E1314, E1317, E1323.
Each is a latest RW (RWN) action with no later action clearing it. This is a manual scan and may have omissions.

**Q19.** Not settled. Latest outlooks for about 300 entities need the full rule run.

**Q20.** No.
E07's last action is a withdrawal (A19, 2026-05-12), which is not a default.

**Q21.** E07, E1002, E1007, E1021, E1032, E1041, E1048, E1057, E1062, E1063, E1076, E1084, E1107, E1121, E1124, E1138, E1140, E1155, E1159, E1166, E1172, E1200, E1205, E1206, E1218, E1219, E1225, E1233, E1234, E1244, E1254, E1277, E1308, E1316, E1320.
Each had a rating earlier and its latest LTIDR action is a withdrawal (WD), with no later FC or LC rating. E1279 and E1106 are excluded because they still hold an LC or FC rating.

**Q22.** E08.
E08 is the only entity with an RD or D rating, which is A22.

**Q23.** F2.
A04 (STIDR, 2026-02-10, AF) is Kestrel's short-term rating.

**Q24.** Yes.
Kestrel's latest FC long-term rating is BBB (A03, 2026-02-10), which is investment grade.

**Q25.** Not settled. Counting instrument ratings at 2026-10-01 needs the full rule run.

**Q26.** A+.
A40 (LC, AS, 2024-03-01) is Corvenia Power's only local-currency rating.

**Q27.** A-.
I06 (2032 note) was assigned A- in A42 (2024-03-01) and has no later action.

**Q28.** BBB+.
A38 (CV, LTIDR, FC, 2024-01-01) is the sovereign's FC issuer rating; the A ceiling in A37 is not a rating of the sovereign.

**Q29.** None.
VD has only a Country Ceiling (A12, CC, BB), which is not the sovereign's issuer rating.

**Q30.** E05, E1028, E1101, E1126, E1236, E15, E1039, E1194.
Each is domiciled in VD (ceiling BB) or CV (ceiling A) and has an FC rating equal to its ceiling on 2026-10-01.

**Q31.** No.
No VD or CV entity's FC issuer rating is above its ceiling; the highest is E15, E1039 and E1194 at A.

**Q32.** E09.
E11 → E10 → E09, and E09 has no parent.

**Q33.** E10; BBB+.
I05 (2028 note) is guaranteed by E10, so E10's credit risk applies; its latest instrument rating is BBB+ (A29).

**Q34.** No.
E12 has no parent link and no shared LEI with E10.

**Q35.** 3.
The Halden group is E09 (parent), E10 (with duplicate E17), and E11.

**Q36.** 2.
The Northwind group is E02 (with duplicate E03) and E04.

**Q37.** 331.
The data has 370 records; I removed 13 QA records (E16, E1340–E1351) and 26 RESEARCH duplicates that share an LEI with a RATINGS record. This assumes no unflagged LEI collisions.

**Q38.** No.
Orrin Bank AG (549300AMVE3VRVG7HK43) and Orrin Bancorp Inc (815600O8X8K2F154N214) have different LEIs.

**Q39.** A.
E03 (RESEARCH, same LEI as E02) has the latest rating action, A09 (AF, A, POS).

**Q40.** Not settled. This needs a full rule run over GB entities.

**Q41.** None.
E16 is a QA record, and QA actions must be ignored.

**Q42.** LU.
The RATINGS record says DE, but the RESEARCH record E17 (same LEI) says LU, and RESEARCH holds for domicile.

**Q43.** 1.
Only E10 (via E17) is domiciled in LU.

**Q44.** Yes.
I07 is denominated in XVD, Valdoria's domestic currency.

**Q45.** No.
Local-currency debt is not subject to the Country Ceiling, so the BBB- rating on I07 (A45) is not an ceiling breach.

**Q46.** No.
E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None.
I08 has only an expected rating (A47, EX), which is not yet a rating.

**Q48.** Not settled. Counting instrument ratings at 2026-10-01 needs the full rule run.

```json
{"Q1": {"rating": "A-"},
 "Q2": {"downgraded": "no"},
 "Q3": {"investment_grade": "no", "rating": "BB+"},
 "Q4": {"outlook": "Positive"},
 "Q5": {"risk_of": "E02", "rating": "A"},
 "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307"]},
 "Q8": {"entities": ["E08"]},
 "Q9": {"count": null},
 "Q10": {"investment_grade": "no"},
 "Q11": {"rating": "BBB+"},
 "Q12": {"rating": "A-"},
 "Q13": {"count": 1},
 "Q14": {"rating": "none"},
 "Q15": {"rating": "A-"},
 "Q16": {"changed": "no"},
 "Q17": {"downgraded": "no"},
 "Q18": {"issuers": ["E06","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
 "Q19": {"issuers": null},
 "Q20": {"in_default": "no"},
 "Q21": {"entities": ["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
 "Q22": {"entities": ["E08"]},
 "Q23": {"rating": "F2"},
 "Q24": {"investment_grade": "yes"},
 "Q25": {"count": null},
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
 "Q40": {"count": null},
 "Q41": {"rating": "none"},
 "Q42": {"country": "LU"},
 "Q43": {"count": 1},
 "Q44": {"local_currency": "yes"},
 "Q45": {"above_ceiling": "no"},
 "Q46": {"issuer_rating": "no"},
 "Q47": {"rating": "none"},
 "Q48": {"count": null}}
```