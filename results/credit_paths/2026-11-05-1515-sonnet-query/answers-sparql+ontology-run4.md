**Q1.** A-. Kestrel (E01) was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).

**Q2.** No. Kestrel's only 2026 action (A03) is an affirmation with a Negative outlook, not a downgrade.

**Q3.** No, BB+. The 2031 note (I02) is subordinated and was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. The RESEARCH record E03 (same LEI as E02) shows an affirmation at A with a Positive outlook on 2025-09-15 (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and its latest rating is A (A11).

**Q6.** The data points to the Country Ceiling. Valdoria's ceiling (A12) is BB, and Valdoria Telecom's (E05) foreign-currency rating is BB against BBB- local currency. The ceiling caps only foreign-currency ratings.

**Q7.** 38 issuers; the list is in the JSON. Each is a downgrade (DG) of a long-term issuer rating (LTIDR) in 2026, and the QA record E16 is excluded.

**Q8.** E08. Its latest long-term action is RD on 2026-07-08 (A22).

**Q9.** 376. This counts distinct LEIs with a non-withdrawn long-term issuer rating in force on 1 October 2026.

**Q10.** Depends. The foreign-currency rating is BB (speculative grade) and the local-currency rating is BBB- (investment grade) (A14, A13).

**Q11.** BBB+. The downgrade on 2024-09-30 (A36) is the latest action before that date.

**Q12.** A-, set by A34.

**Q13.** 1, which is A36.

**Q14.** None. Halden Foods' (E12) first rating was assigned on 2024-02-01.

**Q15.** A-. The downgrade to BBB+ came on 2026-04-15 (A27), after that date.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; the later actions were Watch (RW) and an affirmation.

**Q17.** No. Orrin Bank's (E06) only 2026 action is a Rating Watch Negative (A17), which is not a downgrade.

**Q18.** 32 issuers; the list is in the JSON.

**Q19.** 49 issuers; the list is in the JSON.

**Q20.** No. Pellam (E07) was withdrawn for commercial reasons (A19), which says nothing about default.

**Q21.** 35 issuers; the list is in the JSON.

**Q22.** E08 only (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 72. Of 113 rated instruments on 1 October 2026, 72 were investment grade, with Expected-rating (EX) actions excluded.

**Q26.** A+ (A40).

**Q27.** A- (A42, subordinated note I06).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 13 entities; the list is in the JSON. Each has a foreign-currency rating equal to its country's ceiling.

**Q31.** No. Every rated entity is at or below its ceiling.

**Q32.** E09. Halden Leasing (E11) is owned by E10, which is owned by E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, and its rating is BBB+ (A29).

**Q34.** Yes. Halden Foods (E12) has no parent in the data, so it is outside the Halden group.

*Correction to Q34:* Halden Foods (E12) has no parent link, so it is not in Halden Bank's group. The answer is **No**.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 497. This counts distinct LEIs, or the record ID where there is no LEI, excluding QA records.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, with a Positive outlook (A09).

**Q40.** 79.

**Q41.** None. Brindle (E16) is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.

**Q43.** 1, which is Halden Bank (LEI 391200QYPVFF2O9K2039).

**Q44.** Yes. XVD is Valdoria's domestic currency.

**Q45.** No. The note (I07) is local-currency, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected-rating action (A47).

**Q48.** 113.

**Q49.** E5001.

**Q50.** 6. The chain is E5047, E5035, E5023, E5011, E5167 (same LEI as E5005), E5002, E5001.

**Q51.** 58.

**Q52.** 25.

**Q53.** No. Belir Mining's chain ends at Belir Group AG (E5059), while Rotam Group (E5086) is a separate top.

**Q54.** E5106. The RESEARCH record E5169 holds domicile VD for that LEI, and the RATINGS record is E5106.

**Q55.** 31.

**Q56.** BB-.

**Q57.** E5002. It is the first shared ancestor of E5011 and E5013.

**Q58.** E5145, which guarantees I5007, issued by E5133 in a different group.

**Q59.** 12.

**Q60.** E5145. I5007 is guaranteed by E5145, whose group differs from the issuer E5133's. Its rating wasn't retrieved, so I report "none" for the rating field.

**Q61.** 20.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E08","E10","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":376},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1194","E5116","E1039","E15","E5012","E5124","E1101","E1236","E5047","E5091","E1028","E1126","E05"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":497},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":79},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":58},
"Q52":{"count":25},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":20}
}
```