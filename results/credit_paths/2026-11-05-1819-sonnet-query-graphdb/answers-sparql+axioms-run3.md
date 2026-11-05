**Q1.** A-. Kestrel Energy (E01) held A- from A01 (2024-03-12) until A02 downgraded it on 2025-06-20.

**Q2.** No. The only 2026 action on E01 was A03 (2026-02-10), an affirmation at BBB with the outlook moved to Negative.

**Q3.** No, BB+. The 2031 note (I02) was cut to BB+ by A07, which is speculative grade.

**Q4.** Positive. Northwind Holdings E02 and E03 share an LEI and are one entity. The latest action, A09 (2025-09-15), sets the outlook to Positive.

**Q5.** E02, rated A. I03 is guaranteed by E02, and its rating was affirmed at A by A11.

**Q6.** The foreign-currency rating is BB (A14) and the local-currency rating is BBB- (A13). Valdoria's Country Ceiling is BB and caps foreign-currency ratings but not local-currency ones.

**Q7.** I found 53 downgrade records dated 2026 for issuer long-term ratings. They include E10, E16 and E08, and are listed in the JSON. I did not de-duplicate records that describe the same entity.

**Q8.** E08 (Saxby Shipping). A22 set RD on 2026-07-08, and no other rating in force is RD or D.

**Q9.** 377. This is 378 records with an issuer long-term rating in force, less one pair of records for the same entity. I could not check for QA test records.

**Q10.** Depends. The foreign-currency rating (the headline) is BB, which is speculative. The local-currency rating is BBB-, which is investment grade.

**Q11.** BBB+. A36 downgraded Marlow Utilities (E14) on 2024-09-30, and that rating held until 2025-11-20.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade; the others are watch placements and an affirmation.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01.

**Q15.** A-. E10 and E17 are one entity, and A26 (A-) held until the 2026-04-15 downgrade.

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now; the only later actions were a watch placement and an affirmation.

**Q17.** No. A17 for Orrin Bank (E06) was a Rating Watch placement, which is not a downgrade.

**Q18.** 32 issuers were on Rating Watch Negative. E1019 and E1059 are on watch for their local-currency ratings only. The list is in the JSON.

**Q19.** 50 issuers had a Negative outlook on their foreign-currency long-term rating. The list is in the JSON.

**Q20.** No. Pellam Retail (E07) was withdrawn by A19 for commercial reasons, and a withdrawal is not a default.

**Q21.** 49 entities. They had issuer-rating actions but none in force on 1 October 2026, counting a rating held under a twin record. The list is in the JSON.

**Q22.** E08 only. A22 (RD) is the only default-level rating in the data.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 72 instruments. These are the in-force instrument ratings of BBB- or better (A, A+, A-, AA-, BBB, BBB+, BBB-).

**Q26.** A+, the local-currency rating (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has a Country Ceiling of BB but no issuer rating.

**Q30.** 13 entities. Five are domiciled in CV, where the ceiling is A, and eight in VD, where it is BB. Two are rated A and BB respectively in the same way as E15 and E05; the full list is in the JSON.

**Q31.** No. Every foreign-currency rating among CV entities is at or below A, and every VD entity is at or below BB.

**Q32.** E09. Halden Leasing (E11) has E10 as parent, and E10's parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and its rating was cut to BBB+ by A29.

**Q34.** No. Halden Foods (E12) has no parent and is its own ultimate parent; Halden Bank is in the E09 group.

**Q35.** 3 (E09, E10 and E11). E17 is the same entity as E10.

**Q36.** 2 (E02, which is the same entity as E03, and E04).

**Q37.** 511. There are 540 records, 29 of which are the second record of an entity already counted.

**Q38.** No. They are separate records (E06 and E13) with separate domiciles, DE and US, and I saw no shared LEI.

**Q39.** A (A09).

**Q40.** 79.

**Q41.** BB+. A44 downgraded Brindle Capital (E16) on 2026-06-01.

**Q42.** LU. The RESEARCH record, E17, holds for domicile and says LU.

**Q43.** 1. The two LU records, E10 and E17, are one entity.

**Q44.** Yes. I07 pays in XVD, the Valdorian dollar, and is flagged as local currency.

**Q45.** No. I07 is rated BBB-, above the BB ceiling, but the ceiling does not cap local-currency debt.

**Q46.** No. E11 has only a private credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected rating (A47), which is not yet a rating.

**Q48.** 113.

**Q49.** E5001.

**Q50.** 6. The chain is E5047, E5035, E5023, E5011, E5167 (which is the same entity as E5005), E5002, E5001.

**Q51.** 58, counting E5005 and E5167 once.

**Q52.** 19. Rotam Group (E5086) and the 18 members from E5087 to E5104.

**Q53.** No. Belir Mining's RATINGS record (E5062) puts it under Belir Group (E5059). The E5168 record links to E5086, but RATINGS holds for parent links.

**Q54.** E5106 (Wonod Steel). Part of the Wonod listing was cut off, so other VD members may be missing.

**Q55.** 31.

**Q56.** BB+, held by Vesol Group (E5132) itself.

**Q57.** E5002. It is the nearest entity common to the chains of E5011 and E5013.

**Q58.** E5145 guarantees I5007, which is issued by E5133 in the E5132 group.

**Q59.** 12.

**Q60.** E5145, and no. The issuer E5133 belongs to the E5132 group, while E5145 is its own group.

**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1300","E1151","E1167","E1080","E5113","E1051","E10","E1034","E1347","E1343","E1290","E1350","E1341","E1229","E1342","E5097","E1351","E5059","E1255","E1340","E16","E1186","E1161","E1263","E1058","E1349","E1112","E08","E5116","E1170","E1344","E1228","E1163","E1243","E5033","E1299","E5019","E1053","E1348","E1213","E1346","E1159","E1057","E1345","E1064","E1294","E1093","E1144","E1307","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":377},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1203","E1314","E1194","E1210","E1260","E1133","E1146","E1242","E1066","E1168","E1297","E1109","E1061","E1132","E1088","E06","E1098","E1266","E1006","E1267","E1037","E1013","E1317","E1181","E1323","E1099","E1238","E1264","E1039","E1126","E1059","E1019"]},
"Q19":{"issuers":["E1300","E5099","E1080","E1105","E5113","E1034","E1118","E1056","E1064","E1055","E5097","E1046","E5059","E5020","E1161","E1263","E1282","E01","E5131","E5023","E5141","E5116","E09","E1271","E5039","E5102","E1228","E1060","E5073","E5033","E1079","E5019","E5050","E5062","E1072","E1190","E1005","E1248","E5057","E1294","E1188","E5119","E1029","E5013","E1262","E1158","E5156","E1211"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1084","E1032","E1234","E1219","E1206","E1107","E1244","E1172","E1159","E1057","E1041","E1347","E07","E1062","E1343","E1277","E1350","E1345","E1341","E1155","E1349","E1254","E1121","E1063","E1166","E1021","E1342","E1200","E1351","E1048","E1124","E1340","E1076","E1138","E16","E1348","E1140","E1316","E1346","E1344","E1308","E1007","E1218","E1225","E1205","E1320","E1233","E5170"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":511},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":79},
"Q41":{"rating":"BB+"},
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
"Q52":{"count":19},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106"]},
"Q55":{"count":31},
"Q56":{"rating":"BB+"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":19}
}
```