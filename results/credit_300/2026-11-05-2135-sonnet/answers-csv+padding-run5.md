**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01), and the downgrade to BBB came later, on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB with the outlook moved to Negative (A03).

**Q3.** No. The 2031 note is I02, downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) affirmed A with a Positive outlook.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 and guaranteed by E02, and E02's latest rating is A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps E05's foreign-currency rating at BB (A14). Its local-currency rating is BBB- (A13).

**Q7.** 43 issuers were downgraded in 2026 (see the JSON). I counted DG actions dated up to today (2026-11-05), and I mapped research-system duplicates to their RATINGS record. E1341's downgrade (A1720) is dated 2026-11-09, so it is excluded.

**Q8.** E08 only. It was downgraded to RD on 2026-07-08 (A22) and has had no later action.

**Q9.** 290. This counts distinct LEIs whose last LTIDR action on or before 2026-10-01 was not a withdrawal. Several entities have actions dated after a withdrawal (e.g. E1115, E1158, E1303), and I followed action dates.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded on 2024-09-30 (A36), and the watch placed on 2025-11-20 (A35) came after 1 June 2025.

**Q12.** A-, assigned on 2023-01-15 (A34).

**Q13.** 1. The only DG action for E14 is A36.

**Q14.** None. E12's first action is dated 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26), and the downgrade is dated 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). The Rating Watch in A35 is not a rating change.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative (A17), with the rating held at A-.

**Q18.** 32 issuers. For E1019 and E1059 the watch sits on the local-currency rating only. The record IDs are in the JSON.

**Q19.** 34 issuers. Entities whose latest action is a Rating Watch have no outlook, and I excluded actions dated after 1 October (e.g. A1730, A1736).

**Q20.** No. E07 was withdrawn for commercial reasons (A19), not in default.

**Q21.** 36 entities, all of which were withdrawn (WD) before 2026-10-01 (list in the JSON).

**Q22.** E08 only (RD, A22).

**Q23.** F2 (STIDR, A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. This counts instruments whose latest INST action on or before 2026-10-01 is BBB- or better. I treated EX as the end of the rating, and instruments with only an EX action have no rating.

**Q26.** A+ (A40).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling (A12, BB), not an issuer rating.

**Q30.** 8 entities: E05, E1028, E1101, E1126 and E1236 at VD's BB ceiling, and E15, E1039 and E1194 at CV's A ceiling.

**Q31.** No. No company has a foreign-currency rating above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent link, so the data shows it outside the E09 group. Only the shared "Halden" name suggests a connection.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 344. That is 370 records minus 26 duplicates that share an LEI with another record.

**Q38.** No. They have different LEIs, countries and no link between them.

**Q39.** A (A09).

**Q40.** 74, including 7 QA-source entities.

**Q41.** BB+ (A44, E16, 2026-06-01).

**Q42.** DE. RATINGS says DE for E10, while the duplicate research record E17 says LU, which conflicts; I used the RATINGS source.

**Q43.** 0. Only the duplicate research record E17 says LU, and I took the RATINGS country (DE) as authoritative.

**Q44.** Yes. I07 is denominated in XVD, which I take to be Valdoria's currency. The data does not define XVD explicitly.

**Q45.** No. The ceiling limits foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 only has a "CO" record (A46), which is not an issuer rating (LTIDR). It does have a guaranteed note, I05.

**Q47.** None. I08's rating was marked EX on 2026-09-01 (A47), which I read as the rating having ended.

**Q48.** 106. This is 99 filler instruments plus I01 to I07; instruments with only an EX action count as unrated.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1188","E1190","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
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
"Q48": {"count": 106}
}
```