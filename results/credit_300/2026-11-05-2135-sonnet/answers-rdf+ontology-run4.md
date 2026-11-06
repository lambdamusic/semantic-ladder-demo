**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01), and the next action, a downgrade to BBB, only came on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04).

**Q3.** No, BB+. The 2031 note is I02, and its latest rating is BB+ (A07, 2025-06-20).

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (2025-09-15, POS).

**Q5.** The credit risk of E02, rated A. I03 is issued by E04 but guaranteed by E02 (A09: A).

**Q6.** Valdoria Telecom's foreign-currency rating is BB (A14), capped at Valdoria's Country Ceiling of BB (A12). Its local-currency rating is BBB- (A13), which the ceiling does not cap.

**Q7.** Thirty-one issuers were downgraded in 2026 (DG actions). I excluded QA records (E16, E1340–E1351) and instrument-only downgrades.

**Q8.** E08 was in default (RD, A22, 2026-07-08).

**Q9.** 277 by my count, deduplicated by LEI. It counts entities whose latest action is not a withdrawal and excludes QA records and credit opinions. The sovereign CV is included.

**Q10.** No. The headline foreign-currency rating is BB (A14); only the local-currency rating, BBB- (A13), is investment grade.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and nothing changed it until later.

**Q12.** A- (A34).

**Q13.** 1, from A36. The Watch (A35) and affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was A- from A26, and the downgrade (A27) only came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.

**Q18.** Thirty-two issuers were on Rating Watch Negative, being those whose latest action on a given basis was an RW.

**Q19.** Twenty-five issuers had a Negative outlook. I treated an entity whose latest action was a Watch as having no outlook.

**Q20.** No. E07 was rated BB and then withdrawn (A19), and a withdrawal is not a default.

**Q21.** Thirty-five entities had a rating that was later withdrawn, so none was held on 2026-10-01. I did not count cases where a later action restored the rating (E1115, E1158, E1303) or where another currency basis was still rated.

**Q22.** Only E08 has ever been in default (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The current foreign-currency rating is BBB (A03).

**Q25.** 66 instruments, counted from INST ratings in force on 2026-10-01. Instruments with only an EX action count as unrated.

**Q26.** A+ (A40, local-currency basis).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (A38). The Country Ceiling (A37) is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** Eight entities were exactly at their ceiling. CV's ceiling is A and applies to E15, E1039 and E1194. VD's ceiling is BB and applies to E05, E1028, E1101, E1126 and E1236.

**Q31.** No. None of the CV or VD entities has a foreign-currency rating above its ceiling.

**Q32.** E09, via E11 → E10 → E09.

**Q33.** The credit risk of E10, rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ after A27.

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331, assuming records E1001–E1351 are all present. That is 370 entity records, minus 13 QA records, minus 26 duplicate records sharing an LEI.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled issuers, using the RESEARCH record's country where records disagree.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. RESEARCH record E17 holds for domicile, overriding E10's DE.

**Q43.** 1 (the Halden Bank entity, E10/E17).

**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency.

**Q45.** No. I07 is rated BBB- (A45), but it is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 is a finance subsidiary with no issuer rating; its only action is a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected (EX) action (A47), so it is unrated.

**Q48.** 106 instruments. There are 115 in total, and 9 have only an EX action.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 277},
"Q10": {"investment_grade": "no"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E1005","E1029","E1034","E1046","E1056","E1060","E1064","E1072","E1079","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
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