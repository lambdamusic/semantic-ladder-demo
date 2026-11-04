**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01), and the downgrade to BBB came on 2025-06-20 (A02), after 1 Jan 2025.

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with the outlook revised to Negative (A03), which is not a downgrade.

**Q3.** No, it is BB+. The 2031 note (I02) is subordinated and was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is E03's A09 (2025-09-15), an affirmation at A with a Positive outlook.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), which guarantees the note (I03). I03 is rated A (A10, affirmed in A11), in line with E02's A.

**Q6.** Valdoria's Country Ceiling (A12) is BB, and the foreign-currency rating is capped at it (E05's FC rating is BB, A14). The local-currency rating of BBB- (A13) is not capped.

**Q7.** 31 issuers were downgraded in 2026, listed in the JSON. Duplicate records are folded into the RATINGS record, and QA records are excluded.

**Q8.** Saxby Shipping (E08). It was downgraded to RD on 2026-07-08 (A22), which is a default. No other record has an RD or D rating.

**Q9.** 278. That is 277 distinct LEIs with a live long-term issuer rating, plus the Republic of Corvenia (CV), which has no LEI.

**Q10.** Depends. E05 is BB on the foreign-currency basis (speculative) and BBB- on the local-currency basis (investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions A35 and A33 left it unchanged.

**Q12.** A-, as assigned on 2023-01-15 (A34).

**Q13.** 1, the downgrade A36.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was A- (A26) until the downgrade to BBB+ on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+ (A33).

**Q17.** No. Orrin Bank's only 2026 action is a Rating Watch Negative placement (A17), which leaves the rating at A-.

**Q18.** 32 issuers were on Rating Watch Negative on 1 Oct 2026, listed in the JSON.

**Q19.** 28 issuers had a Negative outlook on 1 Oct 2026, listed in the JSON.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19) for commercial reasons, and a withdrawal says nothing about default.

**Q21.** 35 entities, listed in the JSON, are those whose latest rating action is a withdrawal.

**Q22.** Only Saxby Shipping (E08).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66 instruments held an investment-grade rating. The unconfirmed expected rating on I08 is not counted.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The Country Ceiling of A (A37) is a separate item.

**Q29.** None. The Republic of Valdoria (VD) carries only a Country Ceiling (A12), and that is not its issuer rating.

**Q30.** The Country Ceilings are A for CV (A37) and BB for VD (A12). The eight entities whose foreign-currency rating equals that ceiling are in the JSON.

**Q31.** No. No CV entity is rated above A and no VD entity is rated above BB.

**Q32.** Halden Group plc (E09). E11 is owned by E10, which is owned by E09.

**Q33.** The holder takes the credit risk of Halden Bank (E10), the guarantor of I05. E10's rating is BBB+ and I05 is also BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no parent and sits outside the E09 chain.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10, so it is the same entity.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 331: 329 distinct LEIs plus the two sovereigns, which have none. QA records are excluded.

**Q38.** No. Orrin Bank AG (E06) and Orrin Bancorp Inc (E13) have different LEIs.

**Q39.** A.

**Q40.** 66 distinct GB issuers.

**Q41.** None. Brindle Capital (E16) is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds, and the LU shown on E17 is only the RESEARCH copy.

**Q43.** 0. The only LU record is E17, and the RATINGS record for the same LEI says DE.

**Q44.** Yes. The 2027 note (I07) pays in XVD, the domestic currency of VD.

**Q45.** No. The note is local-currency debt and not capped by the ceiling, and its BBB- (A45) exceeds the BB ceiling anyway.

**Q46.** No. Halden Leasing (E11) has only a Credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected rating (A47), so it remains unrated.

**Q48.** 106 instruments held a rating on 1 Oct 2026.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E08","E10"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E06","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E09"]},
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
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```