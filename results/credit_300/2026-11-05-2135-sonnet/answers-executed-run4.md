**Q1.** A-. E01's A- (A01) was in force 2024-03-12 to 2025-06-20.

**Q2.** No. The only 2026 action (A03, 2026-02-10) kept the rating at BBB and moved the outlook to Negative. The downgrade to BBB was in 2025 (A02).

**Q3.** No. The 2031 note is I02 (Kestrel Energy 6.25% due 2031, subordinated), rated BB+ after A07.

**Q4.** Positive (E02, A09).

**Q5.** It takes E02's credit risk, rated A. I03 is issued by E04 but guaranteed by E02, so credit_risk_of is E02, whose LTIDR is A (A09). I03 itself is also rated A.

**Q6.** Not stated outright, but the data is consistent with the country ceiling. Valdoria's ceiling is BB (VD, from 2025-04-01), and E05's foreign-currency rating is BB (A14). Its local-currency rating is BBB- (A13), which suggests the ceiling caps only foreign currency.

**Q7.** 31 issuers had a rating lower than before, or a downgrade, in 2026 (listed in the JSON). I judged by actual rating change, not the action label. E1064 and E1290 dropped under an "AF" label, and E1229's later "DG" was actually an upgrade, though E1229 was downgraded earlier in 2026.

**Q8.** E08, rated RD since 2026-07-08 (A22).

**Q9.** 278. This is every entity with an open, non-withdrawn issuer rating row on 2026-10-01, including E08 (RD) and the sovereign CV. VD has no rating.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+ (A36, valid 2024-09-30 to 2025-11-20).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36). The other records are watch or affirmation actions.

**Q14.** None. E12's first rating (A30) starts 2024-02-01.

**Q15.** A- (A26, valid to 2026-04-15).

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33). Only the watch and outlook changed in between.

**Q17.** No. E06 stayed A-, and the 2026-09-03 action (A17) only placed it on Rating Watch Negative.

**Q18.** 31 issuers had an open watch of RWN (listed in the JSON).

**Q19.** 27 issuers had an open Negative outlook (listed in the JSON).

**Q20.** No. E07 was withdrawn (WD, A19), not rated D or RD.

**Q21.** 35 entities have a WD as their latest issuer rating (listed in the JSON). Entities re-rated after a withdrawal, such as E1115 and E1303, are excluded.

**Q22.** E08 only (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade (A03).

**Q25.** 66 instruments, counting open instrument ratings of BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (A42). I06 is the 2032 note.

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** The CV ceiling is A and the VD ceiling is BB. E15 (A), E1039 (A) and E1194 (A) sit at the CV ceiling. E05, E1028, E1101, E1126 and E1236 (all BB) sit at the VD ceiling.

**Q31.** No. No CV or VD entity has a foreign-currency rating above its ceiling. The higher ratings, such as E1039's AA- (A1081), are local currency.

**Q32.** E09.

**Q33.** It takes E10's credit risk, rated BBB+. I05 is issued by E11 and guaranteed by E10 (A27); I05 is also rated BBB+ (A29).

**Q34.** No. E12 has no parent and is not in E09's chain, whereas E10 is a subsidiary of E09.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 331. This is 331 rows in entities.csv, which already have duplicates merged. The count assumes the only gaps in the E1001 to E1339 numbering are the 24 merged records, so I did not check each remaining ID individually.

**Q38.** No. E06 (DE) and E13 (US) have different LEIs, countries and records, with no parent link.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled entities hold an open non-withdrawn issuer rating.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is in XVD with local_currency set to yes.

**Q45.** No. I07 is rated BBB-, above the BB ceiling numerically, but the ceiling constrains foreign-currency obligations, and I07 is local-currency.

**Q46.** No. E11 has no rating rows. Only the guaranteed note I05 is linked to E10's rating.

**Q47.** None. I08 has no rating rows.

**Q48.** 106 instruments have an open rating. I08 is the only unrated instrument, and none had matured by 2026-10-01.

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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```