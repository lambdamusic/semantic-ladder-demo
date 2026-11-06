**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, is dated 2025-06-20.

**Q2.** No. The only 2026 issuer action is A03 (AF, BBB, outlook to NEG), and an affirmation is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02, subordinated: A23 assigned BBB, then A07 downgraded it to BB+ in 2025.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15, AF, A, POS).

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, whose latest rating is A (A08, A09).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12). Valdoria Telecom's FC rating is BB (A14), while its local-currency rating, which is not capped, is BBB- (A13).

**Q7.** 29 issuers had a DG action on an issuer rating in 2026; they are listed in the JSON. QA records are ignored, and research duplicates are mapped to their RATINGS record (E1170 to E1169, E1161 to E1160, E1299 to E1298).

**Q8.** Only E08 (Saxby Shipping). A22 (2026-07-08) downgraded it to RD, which is a default.

**Q9.** 278. There are 331 distinct entities (370 records less 26 duplicates and 13 QA records). 12 of those in the first block of 19 records hold an LTIDR, and 266 of the E1001–E1324 block do after removing the 34 withdrawn. I applied the latest-dated-action rule throughout. E1115, E1158 and E1303 have actions dated after their WD, so I counted them as rated.

**Q10.** Depends. The FC rating is BB (speculative grade) and the LC rating is BBB- (investment grade); see A13 and A14.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and nothing changed it before 2025-06-01.

**Q12.** A-. This is the rating from A34 (2023-01-15).

**Q13.** 1. Only A36 is a DG; A35 is a Watch and A33 is an affirmation.

**Q14.** None. A30 assigned Halden Foods' first rating on 2024-02-01.

**Q15.** A-. A26 set A- for E10 (E17 is the same entity), and the downgrade A27 came on 2026-04-15.

**Q16.** No. It stayed BBB+, since the RW (A35) and AF (A33) do not change the rating.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch, which leaves the rating at A-.

**Q18.** 32 issuers had a Watch Negative as their latest action on 1 October 2026; they are listed in the JSON.

**Q19.** 21 issuers had a Negative outlook on their latest rating action. I excluded issuers whose latest action is a Watch, because those actions carry no outlook.

**Q20.** No. E07 was rated BB and then withdrawn (A19), and a withdrawal is not a default.

**Q21.** 35 entities had a rating that was later withdrawn, with no later rated action (E07 plus 34 others, listed in the JSON).

**Q22.** E08. Its RD (A22) is the only default rating in the data.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66. Of the 106 instruments with a rating, 66 sit at BBB- or better, and the other 40 are speculative grade.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** Eight entities. The VD ceiling is BB: E05, E1028, E1101, E1126 and E1236 have FC BB. The CV ceiling is A: E15, E1039 and E1194 have FC A.

**Q31.** No. No entity's FC rating is above its ceiling. E1245's research record places it in FR, not CV.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. I05's guarantor is E10, and A27 downgraded E10 to BBB+.

**Q34.** Yes for Halden Bank. No for Halden Foods, which is not in the group: E12 has no parent, while Halden Bank (E10) is a subsidiary of E09. So Halden Foods and Halden Bank are not in the same group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 331. That is 370 records less 26 duplicates (same LEI) and 13 QA records.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A08, A09).

**Q40.** 66. I used the RESEARCH record where domicile disagrees. E1115 is counted as rated.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile and overrides E10's DE.

**Q43.** 1 (Halden Bank).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. It is local-currency debt, and the ceiling does not cap it. Its rating is BBB- (A45).

**Q46.** No. E11 has only a Credit Opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated.

**Q48.** 106. Nine of the 115 instruments are unrated: I08 and 8 others that have only an EX action.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1034","E1307","E1159","E1169","E1160","E1167","E1186","E1080","E1057","E1053","E1051","E1093","E1112","E1263","E1243","E1255","E1285","E1290","E1298","E1300","E1294","E1144"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1088","E1194","E1203","E1133","E1006","E1146","E1059","E1019","E1013","E1037","E1061","E1066","E1098","E1099","E1109","E1264","E1126","E1132","E1168","E1181","E1209","E1260","E1266","E1297","E1314","E1317","E1323","E1238"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1034","E1056","E1046","E1029","E1228","E1053","E1160","E1190","E1261","E1263","E1271","E1248","E1294","E1005","E1300","E1079","E1064"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1225","E1206","E1140","E1001","E1138","E1320","E1277","E1219","E1316","E1007","E1021","E1062","E1057","E1308","E1121","E1076","E1107","E1234","E1205","E1244","E1253","E1155","E1048","E1041","E1159","E1172","E1200","E1166"]},
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