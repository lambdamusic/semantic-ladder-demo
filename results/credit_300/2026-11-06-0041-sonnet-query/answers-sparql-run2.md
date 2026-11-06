**Q1.** A-. Kestrel Energy plc (E01) was rated A- from A01 (2024-03-12) until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. E01's only 2026 actions (A03, A04, 2026-02-10) are affirmations, with the outlook moved to Negative.

**Q3.** No. The 2031 note I02 was cut to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity, and the latest action is A09 (2025-09-15, A / Positive).

**Q5.** Northwind Holdings (E02), rated A. Northwind Finance (E04) issued I03, but E02 guarantees it, and I03 is rated A (A11).

**Q6.** Not enough in the data to say why. It does show Valdoria's Country Ceiling is BB (A12), the same as the FC rating of BB (A14), against LC of BBB- (A13). That fits the foreign-currency rating being capped at the ceiling, but no record states it as the reason.

**Q7.** Entities with a 2026 downgrade action (DG) on their issuer rating are listed in the JSON. I excluded E1051 (A+ to A+) and E1229 (BB to BB+). Their DG labels don't match the rating moves, so I could not confirm them as downgrades.

**Q8.** E08 (Saxby Shipping) was in default. It was rated RD from A22 (2026-07-08). Pellam's rating was only withdrawn (WD).

**Q9.** 292 rated entity records, with a caveat. The count is by record and I did not de-duplicate it. Several entities appear twice under one LEI, for example E02/E03, so the distinct-issuer count is lower.

**Q10.** Depends. Valdoria Telecom (E05) is BBB- on a local-currency basis (investment grade) and BB on a foreign-currency basis (not).

**Q11.** BBB+. Marlow Utilities (E14) was cut to BBB+ on 2024-09-30 (A36).

**Q12.** A-. This is from A34 (2023-01-15), before the later downgrade.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' (E12) first rating is A30, dated 2024-02-01.

**Q15.** A-. Halden Bank (E10) was cut to BBB+ only on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now. Only a watch and outlook changes occurred (A35, A33).

**Q17.** No. Orrin Bank (E06) only went on Rating Watch Negative (A17), staying at A-.

**Q18.** The JSON list is incomplete. My result set was cut off, so about 9 rows were not shown. It is based on the latest action per entity being a Rating Watch Negative.

**Q19.** The JSON list is likely incomplete for the same reason. E09 is included on the strength of A25.

**Q20.** No. Pellam Retail (E07) had its rating withdrawn for commercial reasons (A19), which is not a default.

**Q21.** Partial list, from withdrawals (WD) I saw: E07, E1002, E1007, E1021. The result set was truncated, so there may be more.

**Q22.** Only E08 (RD, A22). I checked for RD/D/SD ratings, and only E08 appeared.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 66. I counted instruments whose latest rating on 1 October 2026 was investment grade, excluding those whose latest action was EX (action code not defined in the data; I treated it as an expiry). Of the 69 investment-grade rated instruments, three had a latest EX action and were removed: I08, I1012, I1021.

**Q26.** A+ (A40, Corvenia Power SA, E15).

**Q27.** A- (A42). The 2032 note is I06.

**Q28.** BBB+ (A38).

**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling of BB (A12) and no issuer rating.

**Q30.** The JSON list covers entities whose foreign-currency issuer rating equals their country's ceiling. The ceilings are CV = A and VD = BB. It may be incomplete.

**Q31.** No, from what I could see. Corvenia Power's LC rating of A+ is above the ceiling, but its FC rating is A, equal to it. Rows were truncated, so I could not check every entity.

**Q32.** E09 (Halden Group plc). E11's parent is E10, and E10's parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. E10 guarantees I05, and I05 itself is also BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no parent link and a different LEI to the Halden group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10, sharing its LEI.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 344. There are 370 entity records and 26 LEIs shared by two records each.

**Q38.** No. E06 is a German bank and E13 is a US holding company, with different records and no shared LEI.

**Q39.** A, from A09 and the earlier A08.

**Q40.** 75 records with country GB, not de-duplicated for entities that share an LEI.

**Q41.** BB+ (A44). Brindle Capital (E16).

**Q42.** DE. The LU record E17 is a duplicate of E10.

**Q43.** 1. The only LU record is E17, which is a duplicate of E10, so it is arguably the same entity as a DE one.

**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency.

**Q45.** Yes. I07 is rated BBB- (A45) against a Valdoria ceiling of BB (A12).

**Q46.** No. E11's only rating is a type-CO rating of BBB (A46), which is not an issuer rating.

**Q47.** None. The 2034 note I08 was last rated A on 2026-09-01 with action EX (A47), which I read as an expiry, so no current rating.

**Q48.** 106 rated instruments, taken as 112 latest ratings less the six whose latest action is EX before 1 October 2026 (I08, I1008, I1012, I1021, I1046, I1049).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E16"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":292},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1126"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":75},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```