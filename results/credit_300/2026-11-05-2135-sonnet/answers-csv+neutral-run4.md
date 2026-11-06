**Q1.** A-. A01 (2024-03-12) set A-, and the next action (A02) is dated 2025-06-20.

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03, NEG outlook); the downgrade A02 was in 2025.

**Q3.** No. The 2031 note is I02, subordinated, and A07 downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E03 is the same LEI as E02, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes Northwind Holdings' risk (A09; A for the instrument too, A11).

**Q6.** Valdoria's Country Ceiling (VD, A12) is BB and caps foreign-currency ratings. Valdoria Telecom's FC rating is therefore BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** 31 issuers had an LTIDR downgrade (DG) dated in 2026 (listed in the JSON). I excluded QA records, instrument downgrades, and affirmations or watches. Records E1161, E1170 and E1299 are shown under their RATINGS twins E1160, E1169 and E1298.

**Q8.** Only E08, which went to RD on 2026-07-08 (A22).

**Q9.** 278 (a hand count). It covers distinct entities by LEI, excluding QA records, withdrawn ratings (WD) and the finance subsidiaries. I counted rated or withdrawn status by action date, so E1115, E1158 and E1303, whose later actions post-date a WD, still count as rated.

**Q10.** Depends. Valdoria Telecom (E05) is BBB- on local currency (A13, investment grade) but BB on foreign currency (A14, speculative).

**Q11.** BBB+. A36 (2024-09-30) lowered E14 from A- to BBB+, and A35 (RW, 2025-11-20) is after 2025-06-01.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, the downgrade A36. The RW (A35) and AF (A33) are not downgrades.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10's downgrade to BBB+ (A27) is dated 2026-04-15, after the date asked.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35, A33).

**Q17.** No. Orrin Bank AG (E06) only has a Watch (A17, RW). E13 is a different LEI.

**Q18.** 32 issuers had a latest action that left them on RWN (listed in the JSON). I counted any basis, so E1059 and E1019 are included on their LC ratings.

**Q19.** 30 issuers had a NEG outlook on their latest FC action. I carried the outlook forward through RW rows, which have a blank outlook. E1059 is included on its FC outlook.

**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.

**Q21.** 35 entities had an issuer rating that was later withdrawn (listed in the JSON). I did not count E1279 or E1106, because each still has an LC or FC rating on the other basis.

**Q22.** Only E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes, BBB (A03).

**Q25.** 66. Of the 106 rated instruments, 40 are speculative grade.

**Q26.** A+ (A40).

**Q27.** A- (A42). That is below Corvenia's ceiling of A (A37), so it is not capped.

**Q28.** BBB+ (A38). A37 is the ceiling, not a rating.

**Q29.** None. VD only has a Country Ceiling (A12).

**Q30.** 8 entities (listed in the JSON). The ceilings are BB for VD and A for CV. At the ceiling were E05, E1028, E1101, E1126 and E1236 (all BB, VD) and E15, E1039 and E1194 (all A, CV).

**Q31.** No. No VD entity is above BB and no CV entity is above A.

**Q32.** E09, via E11 → E10 → E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ in A27.

**Q34.** No. E12 has no parent link, so nothing ties it to E09's group.

**Q35.** 3: E09, E10 and E11. E17 is E10 again.

**Q36.** 2: E02 and E04. E03 is E02 again.

**Q37.** 331. That is 370 records minus 13 QA records, 2 duplicates among the E0x records (E03, E17) and 24 RESEARCH duplicates in the E10xx–E13xx range.

**Q38.** No. They have different LEIs, so they are different entities.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled entities held a rating (a hand count).

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds on domicile.

**Q43.** 1, E10 (through E17).

**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 only has an Expected (EX) action (A47), so it is unrated.

**Q48.** 106 of 115 instruments. The nine unrated ones are I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049, which have only EX actions.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1034","E1186","E1159","E1160","E1169","E1167","E1151","E1112","E1093","E1080","E1051","E1057","E1144","E1263","E1285","E1294","E1298","E1300","E1255","E1243","E1290","E1307","E1053","E1229"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1099","E1006","E1088","E1133","E1037","E1194","E1203","E1059","E1019","E1264","E1126","E1209","E1260","E1168","E1146","E1109","E1061","E1098","E1323","E1317","E1314","E1297","E1266","E1238","E1181","E1132","E1066","E1013"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1056","E1079","E1228","E1146","E1282","E1261","E1263","E1271","E1046","E1029","E1034","E1064","E1072","E1132","E1080","E1190","E1248","E1294","E1300","E1005","E1160","E1188","E1211","E1055","E1059","E1105"]},
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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```