**Q1.** A-. E01's rating was assigned A- in A01 (2024-03-12) and not cut to BBB until A02 (2025-06-20).
**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook.
**Q3.** No, BB+. I02, the subordinated 2031 note, was cut to BB+ in A07, which is below investment grade.
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and E03's A15-era action A09 (2025-09-15) is the latest, at A with a Positive outlook.
**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and the note is rated A.
**Q6.** The data doesn't state a reason. It does show a Country Ceiling for VD of BB (A12), and E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13).
**Q7.** The 2026 long-term issuer downgrades are in the JSON. The list includes records that duplicate another entity by LEI (E1170, E1161, E1299). I did not exclude downgrades dated after today.
**Q8.** E08. A22 moved it to RD on 2026-07-08, and no other entity has an RD, D or SD rating.
**Q9.** 391. This counts distinct issuers, merged by LEI, whose latest issuer rating on 1 Oct 2026 is not WD, and it includes the sovereign CV. It is 390 without CV.
**Q10.** Depends. E05 is BBB- (investment grade) in local currency but BB in foreign currency.
**Q11.** BBB+. E14 was cut from A- to BBB+ in A36 on 2024-09-30, and the later actions A35 and A33 did not change the rating.
**Q12.** A-, from A34.
**Q13.** 1. Only A36 is a downgrade of E14.
**Q14.** None. E12 was first rated on 2024-02-01 (A30).
**Q15.** A-. E10 was cut to BBB+ only on 2026-04-15 (A27).
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+, since the watch (A35) and affirmation (A33) did not change the rating.
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating still A-.
**Q18.** The 32 entities in the JSON have a latest rating with Rating Watch Negative on 1 Oct 2026.
**Q19.** The 57 entities in the JSON had a Negative outlook on that date.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.
**Q21.** The 35 entities in the JSON were rated before but had only a WD (withdrawn) rating on 1 Oct 2026.
**Q22.** E08 only, via A22.
**Q23.** F2, from A04.
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 75. This is the number of instruments with a latest rating of BBB- or better on 1 Oct 2026.
**Q26.** A+, from A40.
**Q27.** A-, from A42 on I06.
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling record (A12), not an issuer rating.
**Q30.** The 13 entities in the JSON have a foreign-currency issuer rating equal to the Country Ceiling. The ceilings are A for CV (A37) and BB for VD (A12).
**Q31.** No. No CV entity is above A and no VD entity is above BB in foreign currency.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** E10 (Halden Bank), rated BBB+. I05 is issued by E11 but guaranteed by E10, and the note is rated BBB+ (A29).
**Q34.** No. E12 has no parent link, while E09, E10 and E11 form the Halden group.
**Q35.** 3: E09, E10 and E11. E17 shares E10's LEI, so I counted it as the same entity.
**Q36.** 2: E02 and E04. E03 duplicates E02 by LEI.
**Q37.** 511. There are 540 records, but 509 distinct LEIs plus CV and VD, which have no LEI, give 511.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A, from A08 and A09.
**Q40.** 87. This counts distinct GB issuers, merged by LEI, with a non-WD latest issuer rating on 1 Oct 2026.
**Q41.** BB+, from A44.
**Q42.** DE. E10 is domiciled in DE, though the duplicate record E17 says LU.
**Q43.** 1, namely E17. It is an LEI duplicate of E10, which is in DE, so this is a data conflict.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency.
**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but it is a local-currency note and the ceiling is a foreign-currency cap.
**Q46.** No. E11 has only a CO-type rating, BBB (A46), and no issuer rating.
**Q47.** A, but this is uncertain. I08's only action is an EX action (A47), and the data doesn't define EX, so this may be an expected rather than an assigned rating.
**Q48.** 119.
**Q49.** E5001 (Cerid Group plc). E5011's parent E5167 shares an LEI with E5005, which sits under E5002 and then E5001.
**Q50.** 6: E5047 → E5035 → E5023 → E5011 → E5167 (= E5005) → E5002 → E5001.
**Q51.** 59. Descendants of E5001 number 55, and the E5167 branch adds E5011, E5023, E5035 and E5047.
**Q52.** 20, counting E5168.
**Q53.** Depends. E5062 sits under E5060 (Belir), while E5168 has the same LEI and sits under E5086 (Rotam).
**Q54.** E5124 and E5130.
**Q55.** 31.
**Q56.** BB-, held by E5144.
**Q57.** E5002. E5011 reaches it through E5167 (= E5005), and E5013 reaches it through E5006.
**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the Vesol group.
**Q59.** 12.
**Q60.** E5145, and it is not in the same group as the issuer E5133 (Vesol group, E5132).
**Q61.** 20.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1300","E1151","E1167","E1080","E5113","E1051","E10","E1034","E1347","E1343","E1290","E1350","E1341","E1229","E1342","E5097","E1351","E5059","E1255","E1340","E16","E1186","E1161","E1263","E1058","E1349","E1112","E08","E5116","E1170","E1344","E1228","E1163","E1243","E5033","E1299","E5019","E1053","E1348","E1213","E1346","E1159","E1057","E1345","E1064","E1294","E1093","E1144","E1307","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":391},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1203","E1314","E1194","E1210","E1260","E1133","E1146","E1242","E1066","E1168","E1297","E1109","E1061","E1132","E1088","E06","E1098","E1266","E1006","E1267","E1037","E1013","E1317","E1181","E1323","E1059","E1099","E1238","E1264","E1039","E1126","E1019"]},
"Q19":{"issuers":["E1300","E5099","E1080","E1105","E5113","E1034","E1347","E1343","E1118","E1056","E1064","E1350","E1342","E1055","E5097","E1351","E1046","E5059","E5020","E1340","E1161","E1263","E1282","E01","E5131","E5023","E5141","E5116","E09","E1271","E5039","E5102","E1344","E1228","E1060","E5073","E1079","E5019","E5050","E5062","E1348","E1072","E1190","E1005","E1345","E1248","E5057","E1294","E1188","E5119","E5170","E1029","E5013","E1262","E1158","E5156","E1211"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1206","E1159","E1057","E1041","E07","E1277","E1155","E1254","E1121","E1063","E1021","E1172","E1048","E1124","E1084","E1140","E1316","E1138","E1234","E1218","E1244","E1107","E1032","E1205","E1219","E1076","E1166","E1308","E1200","E1320","E1225","E1062","E1233","E1007"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":75},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1194","E15","E1039","E5116","E5124","E1236","E1126","E05","E5047","E1028","E1101","E5091","E5012"]},
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
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"A"},
"Q48":{"count":119},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":59},
"Q52":{"count":20},
"Q53":{"same_group":"depends"},
"Q54":{"entities":["E5124","E5130"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":20}}
```