**Q1.** A-. E01's last action on or before 1 Jan 2025 was A01 (assigned A- on 2024-03-12). The downgrade to BBB (A02) came on 2025-06-20.

**Q2.** No. In 2026 E01 has only affirmations, A03 (long-term BBB) and A04 (short-term F2), and no downgrade.

**Q3.** No, it is BB+. The 2031 note is I02, subordinated debt of E01, and its latest rating is BB+ (A07, 2025-06-20, down from BBB in A23).

**Q4.** Positive. E02 and E03 share one LEI, so they are one entity, and the latest action is A09 (affirmed A, POS, 2025-09-15).

**Q5.** The holder takes E02's credit risk (Northwind Holdings, the same entity as E03), which is rated A. I03 is issued by the finance subsidiary E04 and guaranteed by E02, and A08/A09 give E02 an A.

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling. E05's FC rating is BB (A14) and its LC rating is BBB- (A13), and the ceiling on VD (A12) is BB.

**Q7.** I counted only long-term issuer-rating downgrades (DG) dated 2026, merging duplicate records by LEI and ignoring QA records. Examples are A21/A22 (E08), A27 (E10) and A1070 (E1034). The JSON lists all of them, using the RATINGS record ID where an entity has several.

**Q8.** E08, which was downgraded to RD on 2026-07-08 (A22). No other record carries RD or D.

**Q9.** 278. 313 distinct entities (by LEI) ever held an issuer rating, including the sovereign CV, whose issuer ratings are A38 and A39. 35 of them had withdrawn their rating by 1 Oct 2026. QA records are excluded.

**Q10.** No. The headline foreign-currency rating is BB (A14), although the local-currency rating is BBB- (A13).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later Watch (A35) leaves the rating unchanged.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36. The Watch and the affirmation do not count as downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30), after that date.

**Q15.** A-. E10's A- (A26) held until the downgrade in A27 on 2026-04-15. E17 is the same entity (same LEI).

**Q16.** No. It was BBB+ on 1 Jan 2025 and is still BBB+ (A33).

**Q17.** No. E06 has only an assignment (A16) and a Rating Watch (A17), and E13 is a different entity.

**Q18.** The latest action is an RW with watch RWN and no later action. Examples are A17 (E06) and A1010 (E1006). The JSON lists all of them.

**Q19.** The latest outlook is NEG for the entities listed in the JSON, for example E01 (A03) and E09 (A25). I excluded entities whose latest action is a Watch, because that action carries no outlook.

**Q20.** No. E07 was assigned BB (A18) and withdrawn (A19), and a withdrawal is not a default.

**Q21.** The 35 entities whose latest issuer-rating action is a withdrawal, for example E07 (A19) and E1001 (A1002, recorded on E1002).

**Q22.** E08 only. It was downgraded to RD in A22, and no other record carries RD or D.

**Q23.** F2 (A04).

**Q24.** Yes. E01's long-term issuer rating is BBB (A03), which is investment grade.

**Q25.** 66. This is the number of instruments whose latest non-EX action by 1 Oct 2026 is BBB- or higher.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42 on I06).

**Q28.** BBB+. CV's foreign-currency issuer rating is A38. The A in A37 is its Country Ceiling, not its rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** I compared each entity's foreign-currency rating with its country's ceiling (CV = A, VD = BB), using the RESEARCH country where records disagree. Eight entities sit exactly at the ceiling: E15, E1039 and E1194 at A, and E05, E1028, E1101, E1126 and E1236 at BB.

**Q31.** No. No foreign-currency rating is above its country's ceiling.

**Q32.** E09. The chain runs E11, then E10, then E09, and E09 has no parent.

**Q33.** The holder takes E10's credit risk (guarantor of I05). The note is rated BBB+ (A29), in line with E10's current BBB+.

**Q34.** No. E12 has no parent link to E09 and is not the same entity as E10, so it is not in the group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 (the same entity as E03) and its finance subsidiary E04.

**Q37.** 331. That is 357 non-QA records (including the two sovereigns) less 26 LEI duplicates, with the 13 QA records excluded.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09, E02/E03).

**Q40.** 66. I counted GB-domiciled entities holding a non-withdrawn issuer rating, using the RESEARCH country where records disagree.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. RESEARCH holds for domicile, and its record E17 says LU, whereas the RATINGS record E10 says DE.

**Q43.** 1: E10, which is the same entity as E17.

**Q44.** Yes. I07 pays in XVD, which is VD's domestic currency.

**Q45.** No. Local-currency debt is not capped by the ceiling. I07 is rated BBB- (A45), above the BB ceiling, which is allowed.

**Q46.** No. E11 has no issuer-rating actions, and A46 is a credit opinion, which is not a rating.

**Q47.** None. I08 has only an Expected action (A47, EX), so it is unrated.

**Q48.** 106. Of 115 instruments, 9 carry only an EX action and are unrated.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1112","E1093","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1294","E1298","E1300","E1290","E1307"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":278},
"Q10":{"investment_grade":"no"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":331},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```