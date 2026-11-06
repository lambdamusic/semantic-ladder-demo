**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02). In 2026 it was affirmed at BBB with a Negative outlook (A03).

**Q3.** No, BB+. The 2031 note is I02 (subordinated), downgraded to BB+ in A07.

**Q4.** Positive. E02's open LTIDR record is A09 (A, POS).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and I03's open rating is A (A11).

**Q6.** The data points to the Country Ceiling. VD's ceiling is BB, and E05's foreign-currency rating is BB (A14) while its local-currency rating is BBB- (A13). The data does not state the rule outright.

**Q7.** 31 issuers had a downgrade in 2026, judged by actual rating-level drops. Some records are labelled AF or DG inconsistently with the rating change (e.g. E1064 A1141, E1290 A1621), so I went by the rating level. Instrument downgrades are excluded.

**Q8.** E08, which has been rated RD since 2026-07-08 (A22).

**Q9.** 278. This counts entities with an open, non-withdrawn issuer rating, including CV (the only sovereign with a rating). An FC or LC rating alone is enough to count.

**Q10.** Depends. E05 is BB in foreign currency (sub-investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts 2024-02-01 (A30).

**Q15.** A-. E10 was A- until 2026-04-15 (A26).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now; only the watch and outlook moved (A35, A33).

**Q17.** No. E06 stayed at A- and was placed on Rating Watch Negative on 2026-09-03 (A17).

**Q18.** 32 issuers carried an open RWN record. They are listed in the JSON below.

**Q19.** 27 issuers had an open Negative outlook. They are listed in the JSON below.

**Q20.** No. E07's rating was withdrawn (WD) on 2026-05-12 (A19), which is not a default.

**Q21.** 35 entities, all with an open WD record and no other open issuer rating. They are listed in the JSON below.

**Q22.** E08 only. It reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. Of the 106 open instrument ratings, 66 are BBB- or better.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** E15, E1039, E1194 (CV, ceiling A) and E05, E1028, E1101, E1126, E1236 (VD, ceiling BB), all at the ceiling in foreign currency.

**Q31.** No. No CV entity is rated above A and no VD entity is rated above BB in foreign currency.

**Q32.** E09, from the ancestors table (E11→E10→E09).

**Q33.** E10 (Halden Bank), rated BBB+. E10 guarantees I05, and I05's open rating is BBB+ (A29).

**Q34.** No. E12 has no parent and no link to E09, so the shared name does not make it part of the group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is a duplicate record merged into E02.

**Q37.** 331. This is the number of rows in entities.csv, after the duplicate records were merged.

**Q38.** No. E06 (DE, LEI 549300AMVE3VRVG7HK43) and E13 (US, LEI 815600O8X8K2F154N214) are separate entities.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled entities with an open, non-withdrawn issuer rating.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU (E10).

**Q43.** 1: E10. The merged record E17 is part of E10.

**Q44.** Yes. I07 is in XVD with local_currency = yes.

**Q45.** No. The VD ceiling is BB, but I07 is a local-currency note rated BBB- (A45). The ceiling appears to apply only to foreign-currency ratings, as E05's own LC rating is also BBB-.

**Q46.** No. E11 has no rating records of its own; I05 is rated through the E10 guarantee.

**Q47.** None. I08 has no rating record.

**Q48.** 106 instruments (I01–I07 plus 99 I1xxx) have an open rating.

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
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```