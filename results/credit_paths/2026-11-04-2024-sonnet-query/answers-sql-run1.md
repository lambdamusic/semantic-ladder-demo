**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12), and the downgrade to BBB (A02) came only on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with the outlook moved to Negative.

**Q3.** No, it is BB+. The 2031 note is I02, and A07 cut it to BB+ on 2025-06-20.

**Q4.** Positive. E03 is the research-system duplicate of E02 (same LEI), and its latest action, A09 on 2025-09-15, affirmed A with a Positive outlook. That supersedes E02's Stable outlook from A08.

**Q5.** You take the credit risk of E02, Northwind Holdings, rated A. I03 was issued by E04 and guaranteed by E02, and I03 is rated A (A11).

**Q6.** The data does not state a reason. It only shows a Country Ceiling for Valdoria of BB (A12) and E05 at FC BB against LC BBB- (A13, A14), which is consistent with a ceiling effect.

**Q7.** 47 issuers had a 2026 LTIDR downgrade dated on or before today, 2026-11-04 (see the JSON). I excluded four downgrades dated after today (E1349, E1346, E5033, E1341), since they cannot have happened yet.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and it has no later action.

**Q9.** 390. This counts distinct LEIs among entities with a current LTIDR, which merges duplicate records of the same legal entity.

**Q10.** Depends. E05 is BB in foreign currency (A14), which is sub-investment grade, and BBB- in local currency (A13), which is investment grade.

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30.

**Q12.** A-. E14 held A- from A34 (2023-01-15) until the downgrade.

**Q13.** 1. The only downgrade is A36, since A35 is a watch placement and A33 an affirmation.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10 was A- from A26 until the downgrade on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after A33.

**Q17.** No. E06's only 2026 action, A17, is a Rating Watch Negative placement at A-, not a downgrade.

**Q18.** 30 issuers were on RWN on 2026-10-01 (see the JSON). I mapped the research duplicate E1210 to E1209.

**Q19.** 57 issuers had a Negative outlook and were not on watch on 2026-10-01. I mapped the research duplicates E1262, E1060 and E1161 to E1261, E1059 and E1160.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and no default rating was ever assigned.

**Q21.** 35 entities (see the JSON). They had a rating that was later withdrawn, with no later rating before 2026-10-01.

**Q22.** E08 only. It is the only entity ever rated RD or D (A22).

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade.

**Q25.** 72. This counts instruments whose latest INST rating on 2026-10-01 was investment grade and not an expiry (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** 13 entities have a foreign-currency issuer rating exactly at their country's ceiling. The ceilings are CV A and VD BB. Examples are E15 (CV, A) and E05 (VD, BB).

**Q31.** No. No company's FC rating is above its country's ceiling on 2026-10-01.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** You take the credit risk of E10, Halden Bank, the guarantor of I05. It is rated BBB+ (A29 for the note, A27 for E10).

**Q34.** No. E12 has no parent and is separate from the E09/E10 group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 511. The 540 rows collapse to 509 distinct LEIs plus 2 sovereigns with no LEI.

**Q38.** No. They have different LEIs (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A, by the same logic as Q4 (E02 A08, E03 A09).

**Q40.** 87 distinct GB-domiciled issuers, counted by LEI.

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE. E10, the RATINGS record, says DE, while the research duplicate E17 says LU.

**Q43.** 0. The only LU row is E17, a research duplicate of E10, which is domiciled in DE. If E17 is taken at face value, the count is 1.

**Q44.** Yes. I07 is denominated in XVD, apparently Valdoria's currency.

**Q45.** No. The ceiling caps foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46, BBB), not an issuer rating.

**Q47.** None. A47 shows the rating on I08 as expired (EX) on 2026-09-01.

**Q48.** 113.

**Q49.** E5001. E5047's chain is E5001 > E5002 > E5005 > E5011 > E5023 > E5035 > E5047, with E5167 being a duplicate of E5005.

**Q50.** 6.

**Q51.** 59, with duplicate records merged by LEI.

**Q52.** 19. E5168 is a research duplicate of Belir Mining and is merged out.

**Q53.** No. The authoritative record E5062 sits in the Belir group, and only the duplicate E5168 shows a Rotam parent.

**Q54.** E5124 and E5130.

**Q55.** 23.

**Q56.** BB-, held by E5144.

**Q57.** E5002. Both chains run E5001 > E5002, then split via E5005 and E5006.

**Q58.** E5145. It guarantees I5007, which was issued by E5133 in the Vesol group.

**Q59.** 12.

**Q60.** You take the credit risk of E5145, the guarantor of I5007, and it is not in the same group as the issuer E5133 (Vesol Group).

**Q61.** 20.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1186","E1243","E1255","E08","E1151","E1299","E1307","E1213","E1080","E5156","E1285","E1112","E1263","E1064","E1347","E1344","E1348","E5019","E1163","E1053","E1051","E1300","E10","E1034","E1229","E5116","E5059","E16","E1144","E1159","E5113","E1057","E1340","E1228","E1294","E1058","E1342","E1093","E1161","E1343","E1170","E5097","E1290","E1350","E1167","E1345","E1351"]},
"Q8":{"entities":["E08"]},"Q9":{"count":390},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1099","E1260","E1132","E1264","E1006","E1039","E1266","E1317","E1037","E1242","E1267","E1297","E1061","E1238","E1013","E1066","E1314","E1203","E1146","E1323","E1133","E06","E1088","E1194","E1126","E1098","E1209","E1181","E1109","E1168"]},
"Q19":{"issuers":["E5141","E5119","E1294","E1055","E1350","E1344","E1105","E1158","E1190","E5039","E1072","E5156","E1347","E1271","E1079","E5116","E1080","E1005","E1211","E1261","E5019","E5113","E5131","E1059","E09","E1348","E1046","E5059","E1160","E1351","E5020","E1029","E1342","E5170","E1248","E5057","E1034","E1188","E5102","E5097","E1300","E1263","E5073","E5050","E1228","E1345","E5099","E5023","E1056","E5062","E1340","E5013","E1282","E1064","E1118","E1343","E01"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1200","E1233","E1225","E1234","E1048","E1084","E1244","E1316","E1205","E1121","E1076","E1218","E1166","E07","E1021","E1253","E1032","E1159","E1007","E1308","E1057","E1155","E1140","E1107","E1138","E1063","E1041","E1124","E1172","E1001","E1062","E1219","E1320","E1206","E1277"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1028","E1194","E1039","E5012","E5091","E5116","E1101","E1126","E1236","E15","E05","E5047","E5124"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":87},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":59},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5124","E5130"]},"Q55":{"count":23},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":20}}
```