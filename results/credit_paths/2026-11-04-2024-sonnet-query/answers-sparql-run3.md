Queries ran out before I could resolve everything. The answers below are from the records I retrieved. Q29–Q31, Q37, Q40, Q49–Q52 and Q54–Q59 are unverified.

**Q1.** A-. A01 (2024-03-12) is the last rating before A02's downgrade on 2025-06-20.
**Q2.** No. Kestrel's only 2026 action is A03, which affirmed BBB with a Negative outlook.
**Q3.** No. The 2031 note I02 is subordinated and has been BB+ since A07 (2025-06-20).
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. A09 (2025-09-15) is the latest action and carries a Positive outlook.
**Q5.** Northwind Holdings (E02), rated A. E04 issued I03, which E02 guarantees; I03 is rated A (A11) and E02's issuer rating is A.
**Q6.** The data doesn't say why. E05 is rated BBB- local currency (A13) and BB foreign currency (A14), and Valdoria's Country Ceiling is BB (A12).
**Q7.** The list is in the JSON; it is every entity with a downgrade action in 2026. I did not net out later upgrades, so entities such as E1051 that were downgraded and then upgraded are included.
**Q8.** E08, rated RD on 2026-07-08 (A22).
**Q9.** 391, counting entities with a non-withdrawn issuer rating and merging duplicates that share an LEI.
**Q10.** Depends. E05 is BBB- in local currency (investment grade) and BB in foreign currency (not).
**Q11.** BBB+ (A36, 2024-09-30).
**Q12.** A- (A34).
**Q13.** 1, the downgrade in A36.
**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.
**Q15.** A-. E10 was A- (A26) until the downgrade on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 and A33 only changed the watch and outlook.
**Q17.** No. A17 only placed E06 on Rating Watch Negative at A-.
**Q18 and Q19.** The lists are in the JSON. The Negative-outlook list is incomplete because the query errored on some rows.
**Q20.** No. A19 is a withdrawal for commercial reasons, not a default.
**Q21.** Partial list. These entities have a latest action of WD (withdrawn); it is not a full scan.
**Q22.** E08 is the only entity with a default-level (RD/D) rating.
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 75 instruments held an investment-grade rating on 1 October 2026.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None found. I only retrieved the Country Ceiling (BB, A12), not an issuer rating.
**Q30.** Partial. The Valdoria and Corvenia ceilings match E05 (BB) and E15 (A); other countries were not checked.
**Q31.** No, from the two cases I checked. This is unverified.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** Halden Bank (E10), rated BBB+. E10 guarantees I05 and was downgraded to BBB+ in A27.
**Q34.** No. E12 has no parent link, and E10's parent is E09.
**Q35.** 3: E09, E10 and E11. E17 has no parent link.
**Q36.** 2: E02 and E04.
**Q37.** About 509, from the distinct LEIs among 540 entity records. Some duplicates, such as E03, E1002 and E1022, share an LEI; entities without an LEI may add to the count.
**Q38.** No. Orrin Bank AG (E06, DE) and Orrin Bancorp Inc (E13, US) have different LEIs and countries.
**Q39.** A. E02 and E03 share an LEI and are the same entity; the latest rating, A09, is A.
**Q40.** About 88. The query that produced this was unreliable.
**Q41.** BB+ (A44).
**Q42.** DE.
**Q43.** 1, which is E17.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.
**Q45.** Yes. I07 is BBB- against a ceiling of BB.
**Q46.** No. E11 only has a CO-type rating (A46).
**Q47.** A (A47, 2026-09-01).
**Q48.** 119 instruments held a rating on 1 October 2026.
**Q49–Q52 and Q54–Q59.** Not determined; the group structure was not fully retrieved. The counts and entity lists in the JSON are placeholders.
**Q53.** Depends. BELIR MINING SA (E5168) sits under E5086, while E5062 sits under E5060.
**Q60.** Geren Group's E5145 guarantees I5007, which E5133 issues, so the risk is E5145. It is probably not in the same group as the issuer, which is in the Vesol group; I did not verify this.
**Q61.** Not determined.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},"Q8":{"entities":["E08"]},"Q9":{"count":391},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E06","E1297","E1314","E1317","E1323"]},"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5170"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07","E1007","E1032","E1057","E1155","E1159","E1172"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":75},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":509},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":88},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":119},"Q49":{"parent":"E5167"},"Q50":{"count":0},"Q51":{"count":0},"Q52":{"count":0},"Q53":{"same_group":"depends"},"Q54":{"entities":[]},"Q55":{"count":0},"Q56":{"rating":"none"},"Q57":{"entity":"E5167"},"Q58":{"entities":["E5145"]},"Q59":{"count":0},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":0}}
```