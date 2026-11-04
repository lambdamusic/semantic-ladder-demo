**Q1.** A-. A01 (2024-03-12) assigned A-, and the downgrade A02 only came on 2025-06-20.
**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook.
**Q3.** No. The 2031 note is I02, a subordinated note, and A07 (2025-06-20) downgraded it to BB+, which supersedes A23's BBB.
**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and A09 (2025-09-15) affirmed A with a Positive outlook.
**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 and guaranteed by E02, and A09 affirmed E02 at A.
**Q6.** The Country Ceiling caps it. VD's ceiling is BB (A12), and E05's foreign-currency rating is BB (A14) while its local-currency rating is BBB- (A13).
**Q7.** 43 entities were downgraded in 2026, listed in the JSON, e.g. E10 (A27), E16 (A44) and E08 (A21, A22). I counted DG actions dated 2026-01-01 to 2026-11-04 and excluded A1720 (E1341), which is dated 2026-11-09, after today.
**Q8.** E08. A22 (2026-07-08) moved it to RD and nothing followed.
**Q9.** 290. This counts distinct entities, with duplicates merged by LEI, whose latest issuer-rating action on or before 2026-10-01 is not a withdrawal. Three cases are judgement calls: E1115, E1158 and E1303 have actions dated after their withdrawal, and I went by dates. E1106 (only its local-currency rating was withdrawn) and E1279 (only its foreign-currency rating was withdrawn) were counted because one rating remains.
**Q10.** Depends. E05's foreign-currency rating is BB (non-investment grade, A14) and its local-currency rating is BBB- (investment grade, A13).
**Q11.** BBB+. A36 (2024-09-30) downgraded E14 from A- (A34) to BBB+.
**Q12.** A-. A34 (2023-01-15) is the only action before that date.
**Q13.** 1. Only A36 is a downgrade; the others are an assignment, a watch and an affirmation.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. A26 assigned it on 2023-05-01, and the downgrade A27 came on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01, after A36, and it is still BBB+ (A35 and A33 are watch and affirmation only).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-.
**Q18.** 32 entities were on Rating Watch Negative, listed in the JSON. This includes E1019 and E1059, where only the local-currency rating is on watch, and excludes entities whose watch was later resolved (e.g. E14 by A33).
**Q19.** 36 entities had a Negative outlook, listed in the JSON. I excluded entities whose latest action was a Rating Watch, since no outlook is shown, and actions dated after 2026-10-01 (A1730, A1736). E1158 is included on the date-based reading (A1338).
**Q20.** No. A19 withdrew E07's rating for commercial reasons, which is not a default.
**Q21.** 35 entities, listed in the JSON, whose latest action is a withdrawal (WD) dated on or before the cutoff, e.g. E07 (A19) and E1001 (A1002 on duplicate E1002).
**Q22.** E08 only (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. A03 affirmed BBB, which is investment grade.
**Q25.** 68. This counts the latest instrument ratings as of 2026-10-01 at BBB- or above. Expired (EX) ratings are excluded, but three EX actions dated after the cutoff (I1007, I1001, I1015) still counted as rated.
**Q26.** A+ (A40).
**Q27.** A- (A42 on I06).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling of BB (A12), which is not an issuer rating.
**Q30.** E05, E1028, E1101, E1126 and E1236 sit at VD's BB ceiling, and E15, E1039 and E1194 sit at CV's A ceiling.
**Q31.** No. No foreign-currency rating exceeds the VD (BB) or CV (A) ceiling, and the data gives no ceilings for other countries.
**Q32.** E09. E11 has parent E10, and E10 has parent E09.
**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.
**Q34.** No. E12 has no parent link to the Halden group, and the shared name is not evidence.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 and E04, with E03 a duplicate of E02.
**Q37.** 344. There are 370 rows, and 26 are RESEARCH duplicates sharing a LEI with another row.
**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).
**Q39.** A, per A09 (the affirmation was booked on E03, the duplicate of E02).
**Q40.** 74 GB-domiciled entities held an issuer rating.
**Q41.** BB+. A44 downgraded E16 from BBB- (A43) on 2026-06-01.
**Q42.** DE per E10 (RATINGS), but the RESEARCH duplicate E17 says LU, so the sources conflict.
**Q43.** 0, since E17 is a duplicate of E10, which is DE. If the LU record is counted, the answer would be 1.
**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency, and its BBB- matches E05's local-currency rating. The data does not define the code explicitly.
**Q45.** No. The ceiling applies to foreign-currency obligations, and I07 is a local-currency note, so the BB cap doesn't constrain its BBB- (A45).
**Q46.** No. E11 has only a CO rating (A46) and no LTIDR.
**Q47.** None. A47 (2026-09-01) expired the I08 rating.
**Q48.** 109. There are 115 instruments, minus six with no rating at the cutoff: I08, I1008, I1012, I1021, I1046 and I1049, all of which have EX actions on or before 2026-10-01.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E10","E16","E1064","E1058","E1163","E1213","E1034","E1228","E1346","E1350","E1307","E1347","E1169","E1160","E1186","E1112","E1298","E1167","E1159","E1151","E1263","E1300","E1343","E1344","E1345","E1348","E1349","E1351","E1340","E1342","E1294","E1285","E1290","E1080","E1051","E1093","E1057","E1053","E1144","E1243","E1255","E08","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1194","E1203","E1133","E1088","E1181","E1264","E1168","E1019","E1260","E1037","E1013","E1099","E1098","E1109","E1066","E1132","E1146","E1209","E1266","E1297","E1314","E1317","E1323","E1126","E1061","E1238","E1059"]},
"Q19": {"issuers": ["E01","E09","E1158","E1282","E1034","E1228","E1350","E1347","E1029","E1160","E1263","E1118","E1079","E1046","E1056","E1343","E1344","E1345","E1348","E1351","E1340","E1342","E1294","E1271","E1248","E1080","E1064","E1261","E1190","E1005","E1059","E1300","E1072","E1211","E1055","E1105"]},
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