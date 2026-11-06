**Q1.** A-. E01's last action before 1 Jan 2025 was AS at A- (A01, 2024-03-12). The downgrade to BBB came later (A02, 2025-06-20).

**Q2.** No. E01's only 2026 actions (A03, A04) are affirmations, and A03 only changed the outlook to Negative.

**Q3.** No, it is BB+. The 2031 note (I02) is subordinated, and A07 downgraded it to BB+ on 2025-06-20.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 on E03 (2025-09-15), which affirmed A with a POS outlook.

**Q5.** The holder takes E02's credit risk (Northwind Holdings), and the note is rated A. I03 is issued by the finance subsidiary E04 but guaranteed by E02, and A10/A11 rate it A.

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling, which is BB (A12). E05's FC rating is BB (A14), while its LC rating is BBB- (A13) and is not capped.

**Q7.** Issuers with a DG action in 2026 are listed in the JSON. I excluded QA records and used the RATINGS record ID where an entity has duplicate records (E1160, E1169, E1298). I took each action's DG label at face value without checking the direction of each rating move, and E1051 shows A+ before and after.

**Q8.** E08 (Saxby Shipping). It went to RD on 2026-07-08 (A22), the only default in the data.

**Q9.** 278. This counts distinct LEIs (or IDs, for sovereigns) with a non-withdrawn long-term issuer rating on 1 Oct 2026, excluding QA records.

**Q10.** Depends. E05 is BB on foreign currency (speculative) and BBB- on local currency (investment grade).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30.

**Q12.** A-. A34 assigned A- on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade, and the Rating Watch (A35) is not.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10's rating was A- from A26 until the downgrade on 2026-04-15 (A27). E17 is the same entity.

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now (A33).

**Q17.** No. E06 only had a Rating Watch placed on 2026-09-03 (A17), which is not a downgrade.

**Q18.** Issuers whose latest action by 1 Oct 2026 was a Rating Watch Negative are in the JSON. E1019 and E1059 are on watch for their local-currency ratings.

**Q19.** Issuers whose latest action by 1 Oct 2026 carried a Negative outlook are in the JSON. I did not carry an outlook forward through Rating Watch actions, which have none.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** 35 entities had a rating at some point but none on 1 Oct 2026, listed in the JSON. Each has only withdrawals as its last actions across all currency bases.

**Q22.** E08 only (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66. This counts instruments of non-QA issuers whose latest rating on 1 Oct 2026 is BBB- or higher. Expected-rating (EX) and withdrawn actions are excluded.

**Q26.** A+ (A40).

**Q27.** A-. I06 is subordinated, and A42 is its only rating.

**Q28.** BBB+ (A38, the foreign-currency rating).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** Foreign-currency ratings exactly at the ceiling are in the JSON: the ceiling is A for CV (A37) and BB for VD (A12). That gives A for E1039, E1194 and E15, and BB for E1028, E1101, E1126, E1236 and E05.

**Q31.** No. Every CV-domiciled company is at or below A and every VD-domiciled company is at or below BB.

**Q32.** E09. The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** The holder takes E10's credit risk (Halden Bank), the guarantor of I05, and the note is rated BBB+ (A29). The CO on E11 is not a rating.

**Q34.** No. E12 has no parent link, so it is outside the E09 group that contains E10.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331. This counts distinct LEIs (or IDs, for sovereigns) among non-QA records.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09 on E03, same entity as E02).

**Q40.** 66. This is the same count as Q9, restricted to entities whose record shows GB. I did not apply the RESEARCH-country override to duplicates here.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record (E17) holds for country, over the RATINGS record's DE.

**Q43.** 1: E10/E17.

**Q44.** Yes. I07 is in XVD, VD's domestic currency.

**Q45.** No. I07 is a local-currency note, so the Country Ceiling does not apply to it.

**Q46.** No. E11 has only a Credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47), so it stays unrated.

**Q48.** 106. This is the same count as Q25 without the investment-grade restriction.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":278},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E1028","E1101","E1126","E1236","E05"]},
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