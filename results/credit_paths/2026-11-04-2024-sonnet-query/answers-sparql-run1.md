**Q1.** A-. The last foreign-currency rating before 1 Jan 2025 was A01 (A-, 2024-03-12). The downgrade to BBB (A02) came on 2025-06-20.
**Q2.** No. A03 (2026-02-10) was an affirmation at BBB with a Negative outlook. There was no 2026 downgrade.
**Q3.** No. Kestrel's 2031 note (I02) has been BB+ since A07 (2025-06-20), which is below investment grade.
**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (E03, 2025-09-15), which carries a Positive outlook.
**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and I03 is rated A (A10, A11).
**Q6.** Not answerable from the data. The data gives no reason. It only shows E05's local-currency rating at BBB- (A13) and its foreign-currency rating at BB (A14).
**Q7.** The issuers with a downgrade action in 2026 are listed in the JSON. Some of these actions show an unchanged rating level, so the list may be overstated.
**Q8.** E08. Saxby Shipping was rated RD by A22 on 2026-07-08.
**Q9.** 393. This counts entities whose latest long-term rating on each basis was not WD. Duplicate records for the same legal entity are not merged, so it may be slightly high.
**Q10.** Depends. Valdoria Telecom's local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not).
**Q11.** BBB+ (A36, 2024-09-30).
**Q12.** A- (A34, 2023-01-15).
**Q13.** 1. Only A36 is a downgrade for Marlow.
**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.
**Q15.** A-. This is E10's rating (A26). The 2026-04-15 downgrade to BBB+ came later.
**Q16.** No. Marlow was BBB+ on 1 Jan 2025 and BBB+ now (A33).
**Q17.** No. Orrin Bank has only A17, a Rating Watch Negative action at A-, in 2026.
**Q18.** The issuers on Rating Watch Negative are listed in the JSON.
**Q19.** The issuers with a Negative outlook are listed in the JSON.
**Q20.** No. Pellam's rating was withdrawn (A19, "commercial reasons"), which is not a default.
**Q21.** The known withdrawals are listed in the JSON. Part of the query output was truncated, so the list may be incomplete.
**Q22.** E08, via the RD rating in A22.
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 75. This sums the latest instrument ratings of BBB- or better on 1 Oct 2026.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None found. I did not retrieve a rating for the Republic of Valdoria.
**Q30–Q31.** Not settled. Corvenia's ceiling is A (A37) and Corvenia Power's foreign-currency rating is A (A41), so E15 sits at the ceiling. I did not retrieve other countries' ceilings.
**Q32.** E09. Halden Leasing (E11) has parent E10, whose parent is E09.
**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10 (A27).
**Q34.** No. Halden Foods (E12) has no parent. Halden Bank (E10) sits under E09.
**Q35.** 3: E09, E10, E11.
**Q36.** 2: E02 and E04. E03 duplicates E02.
**Q37.** About 511. This is a rough estimate of roughly 540 entity records minus 29 duplicate pairs sharing an LEI.
**Q38.** No. They have different LEIs, countries and types.
**Q39.** A.
**Q40.** 88.
**Q41.** BB+ (A44, 2026-06-01).
**Q42.** DE (E10). E17 is a LU-domiciled research duplicate of E10.
**Q43.** 0 distinct entities. The only LU record, E17, is a duplicate of E10, which is domiciled in DE.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.
**Q45.** No. I07 is a local-currency obligation, so the country ceiling does not apply to it.
**Q46.** No. E11 has only a counterparty-obligation rating (A46, type CO), not an issuer rating.
**Q47.** None. A47 marks I08's rating as expired (EX) on 2026-09-01.
**Q48.** 119. This sums the latest instrument ratings on 1 Oct 2026.
**Q49–Q61.** Not resolved. I did not finish querying the Cerid, Rotam, Belir, Wonod and Vesol hierarchies, so the values in the JSON for these are placeholders, not answers.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":393},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5170"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1007","E1032","E1057","E1155","E1159","E1172","E1218","E1219","E1234"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":75},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E15"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":511},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":88},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":119},
"Q49":{"parent":"E5001"},
"Q50":{"count":0},
"Q51":{"count":0},
"Q52":{"count":0},
"Q53":{"same_group":"no"},
"Q54":{"entities":[]},
"Q55":{"count":0},
"Q56":{"rating":"none"},
"Q57":{"entity":"E5001"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":0},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":0}
}
```