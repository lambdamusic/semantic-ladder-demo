**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. 2026 has only A03, an affirmation at BBB (NEG) on 2026-02-10. The downgrade (A02) was in 2025.

**Q3.** No, it is BB+. The 2031 note is I02; A07 (2025-06-20) cut it from BBB (A23) to BB+.

**Q4.** POS. E03 is a duplicate record of E02 (same LEI), and A09 (2025-09-15) affirmed A with a Positive outlook.

**Q5.** The holder takes E02 (Northwind Holdings) risk, rated A. I03 is issued by E04 and guaranteed by E02, whose latest action is A09 (A).

**Q6.** The data doesn't state a reason. E05's FC rating is BB (A14), the same as Valdoria's Country Ceiling BB (A12), while LC is BBB- (A13). That is consistent with the ceiling capping FC only.

**Q7.** 48 issuers had 2026 downgrades (list in JSON). The RESEARCH duplicates are mapped to their RATINGS records. QA-source entities are included because the data doesn't say to exclude them. The E1341 (A1720) and E5033 (A5028) downgrades are dated after today and are excluded.

**Q8.** E08. A22 (2026-07-08) took it to RD after a distressed debt exchange, and nothing later changes that.

**Q9.** 389. This counts distinct (LEI-deduplicated) entities whose latest LTIDR action on 2026-10-01 is not WD, including CV. Where a WD is followed by a later dated action (E1115, E1303), I counted the entity as rated. It is a long manual count, so treat it as approximate.

**Q10.** Depends. E05 is BB on FC (A14, not investment grade) but BBB- on LC (A13, investment grade).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the later actions (A35, A33) kept BBB+.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a DG for E14.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was A- (A26) until A27 on 2026-04-15, and E17 is a duplicate record with no actions.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 is a watch and A33 an affirmation).

**Q17.** No. E06's only 2026 action is A17, Rating Watch Negative at A-.

**Q18.** 32 issuers were on RWN on 2026-10-01 (list in JSON). Each had RW as its latest action, with no later resolving action. E1059 is on RWN for its LC rating only (A1132).

**Q19.** 54 issuers had a Negative outlook (list in JSON). These are entities whose latest action by date carries NEG. Under the same QA treatment as Q7, E1341 is excluded.

**Q20.** No. E07's LTIDR was withdrawn (A19, commercial reasons), not defaulted.

**Q21.** 37 entities (list in JSON). Each had an LTIDR and then a WD before 2026-10-01 with no later re-rating. E1279 is counted because its FC rating was withdrawn (A1594).

**Q22.** E08, the only entity with a default-grade (RD) rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's IDR is BBB (A03).

**Q25.** 72. I count instruments whose latest INST action on 2026-10-01 is BBB- or higher. EX actions are treated as expected ratings and excluded.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42).

**Q28.** BBB+. CV's LTIDR FC is A38; A37 (A) is the Country Ceiling, not the issuer rating.

**Q29.** None. VD has only a Country Ceiling record (A12, BB) and no LTIDR.

**Q30.** 11 entities (list in JSON). Only VD (BB) and CV (A) ceilings are in the data, and these are the FC ratings equal to them.

**Q31.** No. None of the VD or CV entities has an FC rating above BB or A respectively.

**Q32.** E09 (Halden Group plc). E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10 (Halden Bank AG) risk, rated BBB+. E10 is the guarantor of I05, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent, while E10 sits under E09; only the name is shared.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 511. There are 540 rows, minus 29 RESEARCH duplicates sharing an LEI with another row.

**Q38.** No. They have different LEIs, countries and types, and no relationship in the data.

**Q39.** A (A08, then A09).

**Q40.** 86. This counts GB-domiciled rated issuers (deduplicated, with withdrawals excluded) and includes the QA entities.

**Q41.** BB+ (A44, 2026-06-01). E16 comes from the QA source system.

**Q42.** DE per the RATINGS record E10. The RESEARCH duplicate E17 says LU, so the data conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose authoritative record says DE.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's currency, though the data doesn't define the code.

**Q45.** No. I07 is BBB- (A45), but the BB ceiling constrains FC obligations and I07 is LC.

**Q46.** No. E11 has only a CO rating (A46), not an LTIDR.

**Q47.** None. I08's only action is A47, an EX (expected) rating at A, so no final rating is in force.

**Q48.** 113. That is every instrument with a non-EX action.

**Q49.** E5001 (Cerid Group plc). E5047's chain runs E5035, E5023, E5011, E5167, which is the duplicate of E5005, then E5002 and E5001.

**Q50.** 6 levels: E5035, E5023, E5011, E5005, E5002, E5001.

**Q51.** 59. That is E5001–E5058 plus E5170 (QA), with E5167 merged into E5005.

**Q52.** 19, E5086–E5104.

**Q53.** Depends. E5062's RATINGS parent is E5060 (Belir), but its duplicate E5168 names E5086 (Rotam) as parent.

**Q54.** E5124 and E5130. E5169 (VD) is a duplicate of E5106, which is NL.

**Q55.** 23. The count is Cerid 6, Wonod 1, Geren 14 and Rotam 2.

**Q56.** BB-, E5144 (A5108).

**Q57.** E5002 (Cerid Energy plc). E5011 reaches it via E5167/E5005 and E5013 via E5006.

**Q58.** E5145. It guarantees I5007, issued by E5133 in the Vesol group.

**Q59.** 12.

**Q60.** The holder takes E5145 (Geren Group SA) risk, and it is not in the same group as the issuer E5133 (Vesol).

**Q61.** 20. This is 19 Cerid entities plus QA entity E5170.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1169","E1051","E1080","E1307","E1345","E1350","E1167","E1160","E5156","E5116","E5059","E1351","E1344","E1346","E1343","E1342","E1347","E1348","E1349","E1340","E1213","E1228","E1229","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1112","E1093","E1064","E1163","E1159","E1186","E1243","E1034","E1053","E1057","E1058","E1144","E5019","E5113","E5097"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 389},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1264","E1098","E1061","E1209","E1181","E1059","E1006","E1013","E1019","E1037","E1088","E1099","E1109","E1132","E1133","E1126","E1146","E1168","E1194","E1203","E1242","E1260","E1266","E1267","E1297","E1314","E1317","E1323","E1238","E1039","E1066"]},
"Q19": {"issuers": ["E01","E09","E1190","E1056","E1079","E1046","E1029","E5050","E5039","E5059","E5062","E5020","E5013","E5023","E5057","E5073","E5097","E5099","E5102","E5113","E5119","E5131","E5156","E5170","E5116","E5019","E1211","E1248","E1282","E1261","E1263","E1300","E1294","E1228","E1118","E1105","E1080","E1072","E1034","E1064","E1160","E1188","E1005","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1158","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 72},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5124","E15","E1039","E1194"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 511},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 86},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 113},
"Q49": {"parent": "E5001"},
"Q50": {"count": 6},
"Q51": {"count": 59},
"Q52": {"count": 19},
"Q53": {"same_group": "depends"},
"Q54": {"entities": ["E5124","E5130"]},
"Q55": {"count": 23},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 20}
}
```