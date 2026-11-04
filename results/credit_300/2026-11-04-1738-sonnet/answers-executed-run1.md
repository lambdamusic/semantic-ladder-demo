**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02), and the 2026-02-10 action (A03) was an affirmation with a Negative outlook.

**Q3.** No. The 2031 note is I02 (BB+, SUB, after the 2025-06-20 downgrade), which is below investment grade.

**Q4.** Positive. E02's rating A has had a POS outlook since 2025-09-15 (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 and guaranteed by E02, and credit_risk_of is E02. The I03 rating is A, and E02's LTIDR is A (A09).

**Q6.** Valdoria's country ceiling for VD is BB from 2025-04-01. E05's foreign-currency rating is therefore capped at BB (A14), while its local-currency rating is BBB- (A13).

**Q7.** 31 issuers had a downgrade in 2026 (listed in the JSON). Some downgrades are labelled AF (E1064 on 2026-02-02, E1290 on 2026-01-01), so I used the actual rating drop rather than the action label.

**Q8.** E08. Its rating was RD from 2026-07-08 (A22), the only default-level rating.

**Q9.** 278. This counts entities, including the sovereign CV, with a non-withdrawn issuer (LTIDR) rating still open on 1 Oct 2026. The count is hand-tallied from a long list, so it carries some risk of error.

**Q10.** Depends. E05 is BB in foreign currency (below investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+ (E14, A36 from 2024-09-30).

**Q12.** A- (E14, A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now (A33). Only the watch status and outlook moved in between.

**Q17.** No. E06 only went on Rating Watch Negative on 2026-09-03 (A17), with the rating still A-.

**Q18.** 31 issuers were on RWN on 1 Oct 2026 (listed in the JSON). E1019, E1059, E1039, E1126 and E1194 are included because they carry open RWN rows on one rating type.

**Q19.** 27 issuers had a Negative outlook on 1 Oct 2026 (listed in the JSON), based on open rows with outlook NEG.

**Q20.** No. E07 was rated WD (withdrawn) from 2026-05-12 (A19), and withdrawal is not default.

**Q21.** 35 entities, all of them withdrawn with no later rating (WD rows still open).

**Q22.** E08 only (RD, A22).

**Q23.** F2 (E01, A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. Counting instruments with an open INST rating of BBB- or better: 5 among I01–I07 and 61 among the I1xxx series. Instruments with no INST row are not counted.

**Q26.** A+ (E15 LC, A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV FC, A38).

**Q29.** None. VD has no rating records, only a ceiling of BB.

**Q30.** Eight entities. CV's ceiling is A: E15, E1039 and E1194 are at A. VD's ceiling is BB: E05, E1028, E1101, E1126 and E1236 are at BB.

**Q31.** No. No CV entity is above A and no VD entity is above BB.

**Q32.** E09. E11's parent is E10, whose parent is E09 (the ultimate_parent_id).

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10 and credit_risk_of is E10. I05 and E10 are both BBB+ since 2026-04-15 (A29, A27).

**Q34.** No. E12 has no parent and no ultimate parent, so it is not in E09's group.

**Q35.** 3: E09, E10, E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 rows in entities.csv. Duplicate records were already merged into single entities, so each row is one distinct legal entity.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) have different LEIs and countries, and neither lists the other as a record.

**Q39.** A (E02, A09).

**Q40.** 66 GB-domiciled entities held a non-withdrawn issuer rating. GB-domiciled entities with no rating (the FINSUBs) are excluded, as are those whose latest row is WD.

**Q41.** None. No Brindle Capital appears in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity is domiciled in LU.

**Q44.** Yes. I07 is flagged local_currency=yes and denominated in XVD.

**Q45.** No. I07 is rated BBB-, above the BB ceiling, but the ceiling applies to foreign-currency ratings and I07 is a local-currency note.

**Q46.** No. E11 has no rows in ratings.csv. Only I05 is rated, and it takes E10's credit risk.

**Q47.** None. I08 has no INST rating record, and the data does not state that an unrated senior note takes its issuer's rating (E15 is A).

**Q48.** 106: 7 among I01–I07 and 99 among the I1xxx series. All have open ratings and all mature after 1 Oct 2026.

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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q30": {"entities": ["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
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