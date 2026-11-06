**Q1.** A-. E01's rating A1 (A-) ran 2024-03-12 to 2025-06-20, so it held on 1 Jan 2025.

**Q2.** No. The 2026-02-10 record (A03) is an affirmation that only moved the outlook to Negative, and the downgrade to BBB was on 2025-06-20 (A02).

**Q3.** No. Kestrel has two notes, I01 (2030) and I02 (2031). I02 is subordinated and rated BB+, which is below investment grade.

**Q4.** Positive (E02, A09).

**Q5.** E02, the guarantor, at A. I03 names E02 as `credit_risk_of`, and I03 itself is rated A (A11).

**Q6.** The data doesn't state a reason. It does show a Valdoria ceiling of BB from 2025-04-01. E05's foreign-currency rating is BB (A14), which sits at that ceiling, while its local-currency rating is BBB- (A13).

**Q7.** Many issuers had a downgrade (DG) action or a lower rating in 2026, listed in the JSON. E1064 is included because it fell from A- to BBB+ on 2026-02-02 (A1141), although that record is labelled AF. E1290 is included for the same reason (A1621).

**Q8.** E08. It was rated RD from 2026-07-08 (A22) and no later record replaces that.

**Q9.** 278. This counts entities with an open, non-WD long-term issuer rating on 1 Oct 2026, including the sovereign CV and entities rated only in local currency (E1279).

**Q10.** Depends. E05 is BB in foreign currency (A14, sub-investment grade) and BBB- in local currency (A13, investment grade).

**Q11.** BBB+ (E14, A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36). The 2025 watch (A35) and the 2026 affirmation (A33) left the rating at BBB+.

**Q14.** None. E12's first rating starts 2024-02-01 (A30).

**Q15.** A- until 2026-04-15, when it moved to BBB+ (A26/A27).

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now. Only the watch and outlook changed in between.

**Q17.** No. E06's 2026 record (A17) is a Rating Watch Negative, and the rating stays A-.

**Q18.** 32 issuers have an open Rating Watch Negative (RWN) record, listed in the JSON.

**Q19.** 26 issuers have an open Negative outlook, listed in the JSON.

**Q20.** No. E07's rating was withdrawn (WD, A19), which is not a default.

**Q21.** 35 entities have an open WD record, listed in the JSON. E1279 and E1106 still hold a rating in one currency basis, so they are excluded.

**Q22.** E08 only. It is the only entity ever rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade (A03).

**Q25.** 66 instruments held a rating of BBB- or higher on 1 Oct 2026.

**Q26.** A+ (E15, A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV, A38).

**Q29.** None. VD has no rating records.

**Q30.** Eight entities sit exactly at their country's ceiling. For CV (ceiling A): E15, E1039 and E1194. For VD (ceiling BB): E05, E1028, E1101, E1126 and E1236.

**Q31.** No. No CV company is above A, and no VD company is above BB.

**Q32.** E09 (`ultimate_parent_id` for E11).

**Q33.** E10, the guarantor, at BBB+. I05 names E10 as `credit_risk_of`, and I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent, and E09's group contains only E09, E10 and E11.

**Q35.** 3: E09, E10 and E11. E17 is merged into E10.

**Q36.** 2: E02 and E04. E03 is merged into E02.

**Q37.** 331 entity rows in `entities.csv`. Merged duplicates are already collapsed into these rows.

**Q38.** No. E06 is Orrin Bank AG (DE) and E13 is Orrin Bancorp Inc (US), with different LEIs and no parent link.

**Q39.** A (E02, A09).

**Q40.** 65 GB-domiciled entities hold an open, non-WD issuer rating.

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** LU (E10).

**Q43.** 1. Only E10 is domiciled in LU.

**Q44.** Yes. I07 is in XVD with `local_currency` = yes.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has no rating record of its own. I05 is rated on the guarantor E10's credit.

**Q47.** None. I08 has no rating record.

**Q48.** 106 instruments held an open rating on 1 Oct 2026.

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
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q40": {"count": 65},
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