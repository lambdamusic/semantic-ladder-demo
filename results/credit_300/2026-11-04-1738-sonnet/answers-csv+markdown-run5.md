**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01) and not changed until A02 on 2025-06-20.

**Q2.** No. In 2026 E01 only had affirmations (A03 LTIDR BBB with NEG outlook, A04 STIDR F2), and no downgrade.

**Q3.** No, BB+. The 2031 note is I02 (subordinated), downgraded to BB+ by A07 on 2025-06-20 after being assigned BBB (A23).

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and its latest action is A09 (2025-09-15, affirmed A, POS).

**Q5.** The holder takes E02's (Northwind Holdings) credit risk, rated A. I03 is issued by the finance subsidiary E04 but guaranteed by E02, whose latest LTIDR is A (A09, via E03).

**Q6.** The Country Ceiling caps foreign-currency ratings and not local-currency ones. VD's ceiling is BB (A12), so E05's FC rating is BB (A14), while its LC rating is BBB- (A13).

**Q7.** 30 issuers had an LTIDR downgrade (DG) dated in 2026. QA records are excluded, duplicate-LEI records are mapped to the RATINGS ID, and instrument downgrades are not counted (see the JSON list).

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, and nothing later changes that.

**Q9.** 278. After mapping duplicate-LEI records to one entity and excluding QA records, 266 of the E10xx–E13xx entities still held an LTIDR on 2026-10-01. Adding the 12 older entities (E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15) gives 278. This follows the latest-action-by-date rule, which leaves E1115, E1158 and E1303 rated because an action after their WD restores a rating. E1279 and E1106 stay counted as well, since each keeps one currency basis after the other was withdrawn.

**Q10.** Depends. E05's foreign-currency rating is BB (speculative grade, A14) and its local-currency rating is BBB- (investment grade, A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and was unchanged on 2025-06-01.

**Q12.** A-, assigned on 2023-01-15 (A34).

**Q13.** 1 time, by A36. The RW (A35) and AF (A33) actions are not downgrades.

**Q14.** None. E12's first rating (A30) is dated 2024-02-01, after 2024-01-01.

**Q15.** A-. E10 and E17 share an LEI, so they are one entity, and A26 (A-) held until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; the RW and AF actions left the rating unchanged.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement with the rating unchanged. E13 (Orrin Bancorp) is a different entity.

**Q18.** 32 issuers were on RWN on 2026-10-01 (see the JSON list). I counted E1019 and E1059 because one of their currency-basis ratings is on RWN; if only the headline foreign-currency rating counts, drop those two.

**Q19.** 23 issuers had a Negative outlook on 2026-10-01 (see the JSON list). E1059 is included because its FC series (A1129) is NEG.

**Q20.** No. E07 was BB, then withdrawn on 2026-05-12 (A19, commercial reasons), and a withdrawal is not a default.

**Q21.** 35 entities had an issuer rating at some point but none on 2026-10-01, because their last action on every basis is a withdrawal (see the JSON list).

**Q22.** E08 only, through its RD downgrade (A22).

**Q23.** F2, affirmed on 2026-02-10 (A04).

**Q24.** Yes. E01's current LTIDR is BBB (A03).

**Q25.** 66. Of 106 rated instruments, 66 had a rating of BBB- or higher. EX actions do not count as ratings.

**Q26.** A+ (A40, LC).

**Q27.** A-. I06 was assigned A- (A42).

**Q28.** BBB+ (A38, CV LTIDR FC).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** Eight entities were exactly at their ceiling. In VD (ceiling BB): E05, E1028, E1101, E1126 and E1236, all BB. In CV (ceiling A): E15, E1039 and E1194, all A.

**Q31.** No. No VD or CV company has an FC rating above its ceiling (BB or A).

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's (Halden Bank) credit risk, rated BBB+. I05 is guaranteed by E10, whose LTIDR was downgraded to BBB+ by A27.

**Q34.** No. E12 has no parent link to E09, so the shared name is not evidence of a common group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 331. The 370 records minus 13 QA records (E16, E1340–E1351) and 26 duplicate-LEI records leaves 331, with the sovereigns VD and CV counted as entities.

**Q38.** No. Their LEIs differ (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A (A09, affirmed 2025-09-15).

**Q40.** 66, counting GB-domiciled entities per the RATINGS record that still held an LTIDR on 2026-10-01.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, and the LU on the RESEARCH record E17 is overridden.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose RATINGS record says DE.

**Q44.** Yes. I07 is in XVD, VD's domestic currency.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47, EX), which is not yet a rating.

**Q48.** 106 instruments held a rating. Of the 115 instruments, 9 have only EX actions (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049) and so are unrated.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1307","E1186","E1034","E1169","E1159","E1112","E1167","E1160","E1298","E1285","E1263","E1300","E1294","E1080","E1051","E1053","E1057","E1144","E1255","E1093","E1243","E1290","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1088","E1006","E1019","E1059","E1264","E1260","E1013","E1132","E1109","E1099","E1126","E1098","E1146","E1168","E1181","E1209","E1266","E1238","E1297","E1314","E1317","E1323","E1066","E1061","E1037"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1079","E1034","E1046","E1029","E1064","E1261","E1263","E1271","E1282","E1294","E1228","E1248","E1160","E1080","E1005","E1211","E1300","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1225","E1206","E1308","E1140","E1001","E1021","E1007","E1277","E1219","E1159","E1320","E1138","E1107","E1121","E1234","E1205","E1244","E1076","E1041","E1155","E1200","E1172","E1253","E1057","E1048","E1062","E1316","E1166"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
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