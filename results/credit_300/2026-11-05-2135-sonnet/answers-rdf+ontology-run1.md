**Q1.** A-. E01's FC LTIDR was A- from A01 (2024-03-12) until the downgrade A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is the affirmation A03/A04 (2026-02-10), which is not a downgrade.

**Q3.** No, BB+. The 2031 note is I02, subordinated; A23 assigned BBB and A07 (2025-06-20) downgraded it to BB+.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity; the latest action is A09 (AF A, POS, 2025-09-15).

**Q5.** E02, the guarantor, rated A. I03 is guaranteed by E02 (issuer E04), and E02's latest rating is A (A09).

**Q6.** The FC rating is capped by Valdoria's Country Ceiling of BB (A12). E05's FC rating is BB (A14), while its LC rating is BBB- (A13), which is not capped.

**Q7.** 31 entities had a downgrade (DG) dated in 2026; the full list is in the JSON. I excluded QA records (E16, E1340–E1351) and instrument-only downgrades (I05). Where a RESEARCH record carried the action, I used its RATINGS twin (E1161→E1160, E1299→E1298, E1170→E1169).

**Q8.** E08. It is the only entity with an RD or D rating (A22, RD, 2026-07-08).

**Q9.** 278. I counted entities, merged by LEI and excluding QA, whose latest LTIDR or STIDR action on any basis is not a withdrawal. This includes three whose latest action follows an earlier WD (E1115, E1158, E1303).

**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade). The headline FC rating is BB.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions are a Watch (A35) and an affirmation (A33).

**Q12.** A-. A34 assigned A- on 2023-01-15, and no change followed until 2024-09-30.

**Q13.** 1. Only A36 is a DG for E14.

**Q14.** None. E12's first rating was assigned 2024-02-01 (A30), after the date.

**Q15.** A-. E10 held A- (A26) until the downgrade on 2026-04-15 (A27). E17 is the same entity by LEI.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33); A35 is a Watch.

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.

**Q18.** 32 entities were on RWN, meaning their latest action on that basis is an RW. Entities later upgraded, downgraded, affirmed or withdrawn are excluded (e.g. E1012, E1213, E1158, E1276, E1303). Where the Watch is on one basis only (E1019, E1039, E1059, E1126, E1194), I counted the entity.

**Q19.** 27 entities had a NEG outlook, meaning the latest outlook-bearing LTIDR action was NEG. I excluded entities whose latest action is a Watch or withdrawal, because RW carries no outlook; this is a judgement call. E1105 counts because A1226 (2024-01-13) is later than A1227 (2024-01-04).

**Q20.** No. E07 was withdrawn (A19), which is not a default and leaves it with no rating.

**Q21.** 35 entities. Their LTIDR was withdrawn with no later rating action and no remaining LC or FC rating on the other basis. RESEARCH twins are mapped to their RATINGS records (E1002→E1001, E1254→E1253).

**Q22.** E08 only (RD, A22).

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. E01's FC LTIDR is BBB (A03).

**Q25.** 66. This counts instruments whose latest INST action rates BBB- or better; EX-only instruments are unrated.

**Q26.** A+ (A40, LC basis).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+ (A38, FC LTIDR). A37's "A" is the Country Ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 8 entities. In CV (ceiling A), E15, E1039 and E1194 have FC rating A. In VD (ceiling BB), E05, E1101, E1028, E1126 and E1236 have FC rating BB.

**Q31.** No. No CV entity is rated above A and no VD entity above BB.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** E10, the guarantor of I05, rated BBB+ (A27 downgrade of 2026-04-15).

**Q34.** No. E12 has no parent link, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331. From 370 records I removed 13 QA records (E16, E1340–E1351) and 26 RESEARCH duplicates sharing an LEI. This assumes every ID from E1001 to E1351 exists as a record, which I did not verify one by one.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09, E02/E03).

**Q40.** 66 GB-domiciled entities held an issuer rating on that date, using the same basis as Q9.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. E17 (RESEARCH) says LU, and RESEARCH holds on domicile over E10's DE.

**Q43.** 1: E10/E17.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. The ceiling does not apply to local-currency debt, and the note is rated BBB- (A45).

**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an EX action (A47), so it is unrated.

**Q48.** 106. Of 115 instruments, 9 have only EX actions and are unrated.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1051","E1053","E1057","E1058","E1064","E1080","E1186","E1093","E1112","E1213","E1034","E1151","E1159","E1160","E1163","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1144","E1169","E1167"]},
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
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1294","E1300"]},
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
"Q30": {"entities": ["E15","E1039","E1194","E05","E1101","E1028","E1126","E1236"]},
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