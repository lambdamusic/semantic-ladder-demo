**Q1.** A-. A01 assigned A- on 2024-03-12 and the downgrade to BBB (A02) came only on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with a Negative outlook.

**Q3.** No. The 2031 note is I02, rated BBB (A23) and then cut to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 is a duplicate of E02 (same LEI), and its latest action A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02 (A09, A11).

**Q6.** The foreign-currency rating is held to Valdoria's Country Ceiling of BB (A12). E05's FC rating is BB (A14) against an LC rating of BBB- (A13).

**Q7.** 43 issuers had a downgrade (DG) dated in 2026 up to today, listed in the JSON. I merged duplicate records onto the primary ID, counted issuer-level actions only, and left out E1341's DG, which is dated 2026-11-09, after today.

**Q8.** E08. A22 moved it to RD on 2026-07-08 after a distressed debt exchange.

**Q9.** 291. This counts distinct entities (duplicates merged) whose latest FC or LC issuer rating was not withdrawn by 2026-10-01. It treats the 13 early-sample entities plus CV as rated. The assumptions are in the notes below.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade) but its foreign-currency rating is BB (not), per A13 and A14.

**Q11.** BBB+. E14 was cut from A- to BBB+ on 2024-09-30 (A36), and the later watch (A35) did not change the rating.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once, in A36. A35 is a watch placement and A33 an affirmation.

**Q14.** None. E12's first rating (A30) is dated 2024-02-01, after 2024-01-01.

**Q15.** A-. A26 assigned A- on 2023-05-01 and the downgrade (A27) came on 2026-04-15. E17 is a duplicate record of E10 (same LEI).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-.

**Q18.** 32 issuers, listed in the JSON, where the latest action was a Rating Watch Negative (RW) not later resolved by another action. This includes E06 (A17).

**Q19.** 35 issuers, listed in the JSON, whose latest outlook on 2026-10-01 was NEG. E1346, E1349 and E1341 are excluded because their NEG downgrades come after that date.

**Q20.** No. E07 is not in default. Its rating was withdrawn for commercial reasons (A19).

**Q21.** 35 entities, listed in the JSON, whose issuer rating was withdrawn (WD) on or before 2026-10-01, for example E07 (A19) and E1032 (A1067).

**Q22.** Only E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB after A03, which is investment grade.

**Q25.** 66. I counted instruments whose latest own INST rating on 2026-10-01 is BBB- or better.

**Q26.** A+, from A40.

**Q27.** A-, from A42 for I06.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling record (A12, BB) and no issuer rating.

**Q30.** 8 entities, listed in the JSON. Only VD (ceiling BB) and CV (ceiling A) have ceilings in the data, and these entities' FC ratings sit exactly on them.

**Q31.** No. No VD or CV company has an FC rating above BB or A respectively. Local-currency ratings above the ceiling, such as E1039's AA- (A1081), are not a breach.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank AG (E10), rated BBB+ after A27. I05 is guaranteed by E10.

**Q34.** No. E12 has no parent_id and no recorded link to E09 or E10, and a shared name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 344. There are 370 rows, and 26 are RESEARCH duplicates of the same LEI.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A, from A09 (on E03, the duplicate of E02).

**Q40.** 74. This counts GB-domiciled issuers with an active issuer rating on 2026-10-01.

**Q41.** BB+, from A44. E16's source_system is QA.

**Q42.** DE (E10, from the RATINGS source). The duplicate record E17 says LU, which conflicts.

**Q43.** 0. The only LU record, E17, duplicates E10, whose primary record says DE.

**Q44.** Yes, probably. I07 is in XVD, which is not defined in the data and is assumed to be Valdoria's currency. Its BBB- (A45) matches E05's local-currency rating.

**Q45.** No. The ceiling limits foreign-currency ratings, and I07 is in the (assumed) local currency.

**Q46.** No. E11 has no LTIDR, only a CO record (A46, BBB), which the data does not define as an issuer rating.

**Q47.** None. I08 has only an EX action (A47). EX is not defined in the data, and there is no assignment (AS) record for I08.

**Q48.** 106. Of 115 instruments, 9 have only an EX action (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049) and no assigned rating.

Notes and assumptions:
- **Withdrawals:** a withdrawal (WD) dated before later actions on the same entity (E1115, E1158, E1303) was overridden by the later action, on a latest-dated basis.
- **E1279:** its withdrawal covered only the FC rating, so the LC rating still counts.
- **Q9 and Q40:** both counts depend on these assumptions, and Q9 is the least certain figure.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1163","E1167","E1169","E1160","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1056","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
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
"Q48": {"count": 106}
}
```