Ambiguous or duplicated records are flagged where they matter. Q6 has no JSON field.

**Q1.** A-. E01's rating was A- (A01, 2024-03-12) until it was downgraded on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB with a Negative outlook (A03).

**Q3.** No, BB+. The 2031 note I02 was cut to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 is a duplicate record of E02 (same LEI), and its latest action is A09 (2025-09-15, A, Positive).

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02.

**Q6.** The data supports this only partly. Valdoria's Country Ceiling is BB (A12), and Valdoria Telecom's foreign-currency rating is BB (A14), against a local-currency rating of BBB- (A13).

**Q7.** The list is every entity with a 2026 downgrade action, including local-currency ones. It is in the JSON.

**Q8.** E08. It was downgraded to RD in 2026 and has no later rating.

**Q9.** 390. There are 391 entities with a non-withdrawn foreign-currency long-term rating, and E02 and E03 share one LEI.

**Q10.** Depends. Valdoria Telecom's local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not).

**Q11.** BBB+. A36 downgraded Marlow Utilities (E14) on 2024-09-30.

**Q12.** A- (A34).

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods' (E12) first rating is dated 2024-02-01.

**Q15.** A-. Halden Bank (E10) held A- from 2023-05-01 until the downgrade on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+; the watch and affirmation did not change it.

**Q17.** No. Orrin Bank's (E06) only 2026 action is a Rating Watch Negative placement (A17).

**Q18.** The 30 issuers on Rating Watch Negative are in the JSON.

**Q19.** The 57 issuers with a Negative outlook are in the JSON.

**Q20.** No. Pellam Retail's (E07) rating was withdrawn (WD, A19), not moved to default.

**Q21.** The 36 entities whose latest rating is a withdrawal are in the JSON.

**Q22.** E08, the only entity ever rated RD.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB.

**Q25.** 72 of the 113 instruments with a current rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** The list is in the JSON. The ceilings are A for Corvenia (CV) and BB for Valdoria (VD).

**Q31.** No. No company's foreign-currency rating is above its ceiling.

**Q32.** E09, Halden Group plc.

**Q33.** Halden Bank (E10), rated BBB+. I05 is issued by E11 and guaranteed by E10, whose rating was cut on 2026-04-15 (A27).

**Q34.** No. E12 has no parent link to E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 511. There are 540 records, and 29 LEIs are shared by two records.

**Q38.** No. They have different LEIs and countries.

**Q39.** A.

**Q40.** 87. There are 88 GB records with a current issuer rating, minus the E02/E03 duplicate.

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE. E17 is a Luxembourg research record that duplicates E10 (same LEI).

**Q43.** 0. The only LU record, E17, is a duplicate of E10, which is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, the Valdoria local currency.

**Q45.** No. I07 is rated BBB- (A45), but the BB ceiling applies to foreign-currency obligations, and this note is local-currency.

**Q46.** No. E11 has only a "CO" record (A46), not a long-term issuer rating.

**Q47.** None. I08's A rating carries an EX (expired) action dated 2026-09-01 (A47).

**Q48.** 113.

**Q49.** E5001. E5167 duplicates E5005 (same LEI), and E5005 sits under E5002 and then E5001.

**Q50.** 6. The chain is E5047, E5035, E5023, E5011, E5005 (E5167), E5002, E5001.

**Q51.** 59. There are 55 members, plus 4 more reached through the E5167/E5005 duplicate.

**Q52.** 20. This is uncertain because of duplicate records such as E5168.

**Q53.** Yes. Belir Mining (E5062) shares an LEI with E5168, which I took to sit in the Rotam group; I did not verify that link.

**Q54.** E5124 and E5130.

**Q55.** 23.

**Q56.** BB-.

**Q57.** E5002, Cerid Energy plc.

**Q58.** E5145, guarantor of I5007, which E5133 in the Vesol group issued.

**Q59.** 12. This is 11 by the parent links, plus E5011 once E5167 and E5005 are merged.

**Q60.** E5145, and no, it is not in the same group as the issuer E5133 (Vesol group).

**Q61.** 20. This counts 18 members rated below investment grade by the parent links, plus E5023 and E5047 via the duplicate.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1064","E1159","E1186","E1213","E1255","E1300","E1340","E1341","E1342","E1343","E1346","E10","E5019","E1051","E1294","E1053","E1057","E1167","E1229","E1243","E1350","E1058","E1263","E1347","E1348","E1080","E1344","E1349","E1351","E1093","E1161","E1290","E1112","E1151","E1299","E1144","E1163","E1228","E16","E5059","E1170","E1307","E1345","E5113","E5033","E5116","E1285","E08","E5097","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":390},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5170"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E1028","E1101","E1126","E05","E1236","E5012","E5047","E5091","E5124"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":511},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":87},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":59},
"Q52":{"count":20},
"Q53":{"same_group":"yes"},
"Q54":{"entities":["E5124","E5130"]},
"Q55":{"count":23},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":20}
}
```