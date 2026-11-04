**Q1.** A-. E01 held A- (A01, 2024-03-12 to 2025-06-20) on that date.

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with the outlook moved to Negative (A03); the downgrade was in 2025 (A02).

**Q3.** No. The 2031 note is I02, rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 has been BBB-free at A with a Positive outlook since 2025-09-15 (A09).

**Q5.** The risk is E02's, which is rated A. I03 is issued by E04 and guaranteed by E02, and credit_risk_of is E02 (E02 A09, I03 A11).

**Q6.** The data gives no explicit reason. E05 has FC BB (A14) and LC BBB- (A13), and the Valdoria ceiling of BB applies from 2025-04-01. The ceiling caps foreign-currency ratings at BB, which is consistent with the gap.

**Q7.** 31 issuers had a downgrade (DG) action starting in 2026; the IDs are in the JSON block. I counted E1051, E1064, E1229 and E1290 because they have a 2026 DG row or a lower rating in 2026, even where the labels look inconsistent. I did not add E11, whose I05 note was downgraded because its guarantor E10 was.

**Q8.** E08 only. Its rating is RD (A22, from 2026-07-08).

**Q9.** 278. This counts entities with an open, non-withdrawn LTIDR on 2026-10-01, and includes the sovereign CV. Without CV the count is 277.

**Q10.** Depends. E05 is BB in foreign currency, which is not investment grade, and BBB- in local currency, which is.

**Q11.** BBB+ (E14 A36).

**Q12.** A- (E14 A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A- (E10 A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; the watch period (A35) did not change the rating.

**Q17.** No. E06 was only placed on Rating Watch Negative (A17) and stayed at A-.

**Q18.** 32 issuers had an open RWN on 2026-10-01 (listed in the JSON). E1019 and E1059 are on watch only for their local-currency ratings.

**Q19.** 26 issuers had an open Negative outlook on that date (listed in the JSON). Examples are E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), not moved to default.

**Q21.** 35 entities had a rating that was later withdrawn and not replaced (listed in the JSON). E1106 and E1279 are excluded because each keeps an open rating in the other currency basis.

**Q22.** E08 only, rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. Of the 106 instruments with an open own rating, 66 are BBB- or higher.

**Q26.** A+ (E15 A40).

**Q27.** A-. The 2032 note is I06 (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** Eight entities are exactly at their ceiling. E15, E1039 and E1194 are at A, the CV ceiling. E05, E1028, E1101, E1126 and E1236 are at BB, the VD ceiling.

**Q31.** No. No CV company is above A and no VD company is above BB.

**Q32.** E09. Both E11's ultimate_parent_id and E10's parent_id point to it.

**Q33.** The risk is E10's, which is rated BBB+. I05 is guaranteed by E10, credit_risk_of is E10, and I05 itself is rated BBB+ (A29).

**Q34.** No. E12 has no parent and no ultimate parent, so it is not in E09's group.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04). E03 is merged into E02.

**Q37.** 331 rows in entities.csv.

**Q38.** No. E06 and E13 are separate entities with different LEIs and countries.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled entities held a current, non-withdrawn issuer rating.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity is domiciled in LU.

**Q44.** Yes. I07 is flagged local_currency=yes and is denominated in XVD.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has no ratings of its own; I05 is rated through guarantor E10.

**Q47.** None. I08 has no rating row.

**Q48.** 106 instruments have an open own rating.

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
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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