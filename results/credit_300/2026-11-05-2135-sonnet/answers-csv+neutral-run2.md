**Q1.** A-. E01's rating on 2025-01-01 was the one assigned in A01 (2024-03-12). The downgrade to BBB came later, in A02 (2025-06-20).

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with the outlook revised to NEG. Only DG counts as a downgrade.

**Q3.** No. The 2031 note is I02, subordinated, and it was downgraded to BB+ in A07, which is speculative grade.

**Q4.** POS. E03 has the same LEI as E02, so it is the same entity. A09 (2025-09-15) is the latest action, an affirmation at A with a Positive outlook.

**Q5.** The holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, and E02's latest issuer rating is A (A09, recorded on E03).

**Q6.** Valdoria's Country Ceiling (VD, A12) is BB, and it caps foreign-currency ratings. E05's foreign-currency rating is therefore BB (A14), while its local-currency rating is BBB- (A13) and is not capped.

**Q7.** Thirty entities, listed in the JSON. They are those with a DG action on an issuer rating dated in 2026. QA records are excluded, and duplicate research records are mapped to the RATINGS record.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, which is a default, and it has had no later action.

**Q9.** 278 (approximate). About 313 distinct non-QA entities have ever held an issuer rating, and 35 of them have been withdrawn without a later action. I used action dates as given, so E1115, E1158 and E1303, which have actions dated after a withdrawal, count as rated.

**Q10.** Depends. E05's foreign-currency rating is BB (A14), which is speculative grade, but its local-currency rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 (2025-11-20) was only a Watch.

**Q12.** A-, set by A34 (2023-01-15).

**Q13.** 1. A36 is the only DG on E14.

**Q14.** None. E12's first rating was A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26 and was not downgraded until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after A35 (Watch) and A33 (affirmed).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch with the rating unchanged at A-.

**Q18.** Thirty-two entities, listed in the JSON. For each, the latest action on its issuer rating is a Rating Watch Negative dated on or before 2026-10-01, with nothing after it.

**Q19.** Twenty-eight entities, listed in the JSON. Each has a latest action carrying a NEG outlook. Where the latest action is a Watch with no outlook (for example E1146), I did not count it.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and a withdrawal says nothing about default.

**Q21.** Thirty-five entities, listed in the JSON, whose latest action on every issuer rating is a withdrawal. E1279 and E1106 are not included because each still holds a rating on the other currency basis.

**Q22.** E08 only. A22 is the only RD or D in the data.

**Q23.** F2, from A04 (2026-02-10).

**Q24.** Yes. E01's latest issuer rating is BBB (A03).

**Q25.** 66. Of the 106 rated instruments, 66 are rated BBB- or higher on 2026-10-01.

**Q26.** A+, from A40.

**Q27.** A-. I06 was assigned A- in A42, and it is subordinated.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling record (A12, BB), and the ceiling is not the sovereign's own rating.

**Q30.** Eight entities. Valdoria's ceiling is BB and Corvenia's is A. E05, E1028, E1101, E1126 and E1236 are at BB, and E15, E1039 and E1194 are at A.

**Q31.** No. No foreign-currency rating exceeds BB for VD entities or A for CV entities.

**Q32.** E09. E11's parent is E10, whose parent is E09, and E09 has no parent.

**Q33.** The holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, and E10's issuer rating (A27) and I05's rating (A29) are both BBB+.

**Q34.** No. E12 has no parent link to E09, so it is not in that group.

**Q35.** 3: E09, E10 (its research duplicate E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is a duplicate) and E04.

**Q37.** 331. There are 370 records; excluding 13 QA records and 26 duplicate research records leaves 331 entities. The sovereigns are included.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, from A09.

**Q40.** 66 (approximate). This counts GB-domiciled entities with an issuer rating that was not withdrawn by 2026-10-01.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile, while the RATINGS record E10 says DE.

**Q43.** 1: E10, whose RESEARCH record (E17) gives LU.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. The Country Ceiling applies only to foreign-currency debt, and I07 is local-currency, so it is not capped.

**Q46.** No. E11 is a finance subsidiary with no issuer-rating actions; its only action is a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47, EX); it stays unrated until an Assigned action confirms it.

**Q48.** 106. There are 115 instruments, of which 9 have only an Expected action: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1307","E1169","E1160","E1228","E1186","E1159","E1112","E1093","E1080","E1051","E1034","E1167","E1151","E1263","E1285","E1294","E1298","E1300","E1144","E1255","E1053","E1057","E1243","E1290"]},
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
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1006","E1088","E1194","E1203","E1133","E1059","E1264","E1168","E1260","E1297","E1314","E1317","E1323","E1266","E1238","E1181","E1066","E1061","E1037","E1013","E1019","E1099","E1098","E1109","E1126","E1132","E1146","E1209"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1034","E1080","E1263","E1294","E1300","E1228","E1160","E1055","E1046","E1056","E1064","E1029","E1105","E1190","E1271","E1261","E1248","E1005","E1072","E1079","E1211","E1282","E1188","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1124","E1032","E1063","E1218","E1084","E1233","E1206","E1225","E1308","E1140","E1021","E1001","E1277","E1138","E1320","E1219","E1316","E1244","E1107","E1234","E1205","E1007","E1159","E1121","E1076","E1048","E1062","E1057","E1200","E1155","E1041","E1166","E1172","E1253"]},
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