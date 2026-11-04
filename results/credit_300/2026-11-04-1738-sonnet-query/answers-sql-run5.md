**Q1.** A-. Kestrel's FC issuer rating was A- from A01 (2024-03-12) and was cut to BBB only on 2025-06-20 (A02).

**Q2.** No. The only 2026 action, A03 (2026-02-10), is an affirmation at BBB with the outlook moved to Negative.

**Q3.** No. The 2031 note I02 was cut to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its A09 (2025-09-15) is the latest action, with a Positive outlook.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes E02's risk (A10/A11 rate the note A too).

**Q6.** Not in the JSON. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The Valdoria country ceiling (A12) is BB, so the FC rating is capped at the ceiling, while LC is not.

**Q7.** 43 entities had a 2026 downgrade action, listed in the JSON. I counted dates up to today (2026-11-04). I excluded E1341, whose downgrade is dated 2026-11-09. I merged RESEARCH duplicates into their RATINGS entity, and I kept QA-sourced entities.

**Q8.** E08, which was rated RD from A22 (2026-07-08).

**Q9.** 291. This counts distinct LEIs with a non-withdrawn LTIDR on 2026-10-01.

**Q10.** Depends. E05 is BBB- in local currency (investment grade) but BB in foreign currency (not).

**Q11.** BBB+. A36 downgraded E14 from A- on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10's downgrade, A27, was not until 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 put it on watch and A33 affirmed it).

**Q17.** No. E06's only 2026 action, A17, is a Rating Watch Negative placement at an unchanged A-.

**Q18.** 32 issuers were on Rating Watch Negative on 2026-10-01, listed in the JSON. This counts an entity if either its FC or LC rating was on watch.

**Q19.** 37 issuers had a Negative outlook on 2026-10-01, listed in the JSON. This uses each entity's latest rating action.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), and it never had a default rating.

**Q21.** 35 entities, listed in the JSON, held an issuer rating at some point but had only a withdrawal as their latest action by 2026-10-01.

**Q22.** E08 only, via the RD rating in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 66 instruments. This counts those whose latest INST rating is BBB- or better and is not an expiry (EX).

**Q26.** A+, from A40.

**Q27.** A-, from A42 on the subordinated I06.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12, BB) and no issuer rating.

**Q30.** 8 entities. The CV ceiling is A, which E15, E1039 and E1194 sit at. The VD ceiling is BB, which E05, E1028, E1101, E1126 and E1236 sit at.

**Q31.** No. No CV entity's FC rating is above A, and no VD entity's is above BB.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** E10, rated BBB+. I05 is issued by E11 but guaranteed by E10 (A29 gives the note BBB+).

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is a RESEARCH duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 342 distinct LEIs, plus the two sovereigns CV and VD, which have no LEI.

**Q38.** No. They have different LEIs and different countries (E06 is DE, E13 is US).

**Q39.** A. E02 and E03 are the same entity, and both A08 and A09 are at A.

**Q40.** 74. This is 75 GB entities with a non-withdrawn rating, counting LEI duplicates once.

**Q41.** BB+, from A44 (2026-06-01). E16 comes from the QA source.

**Q42.** DE. E10 is in the RATINGS system. E17 (LU) is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, is the same entity as E10, which is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, the Valdoria currency.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a CO rating (A46, BBB) and no LTIDR.

**Q47.** None. I08's latest action is EX (A47, 2026-09-01) even though the note matures in 2034, so it has no current rating.

**Q48.** 106 instruments. This counts those whose latest INST action is not an expiry (EX).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E16","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":291},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1133","E06","E1260","E1099","E1132","E1181","E1013","E1238","E1061","E1297","E1109","E1168","E1317","E1242","E1037","E1209","E1203","E1146","E1323","E1066","E1314","E1266","E1039","E1059","E1267","E1088","E1194","E1006","E1264","E1019","E1098","E1126"]},
"Q19":{"issuers":["E1348","E1046","E1190","E1072","E1350","E1294","E1055","E1105","E1344","E1158","E1079","E09","E1211","E1160","E1351","E1029","E1342","E1034","E1248","E1188","E1271","E1347","E1056","E1340","E1059","E1282","E1005","E1080","E1228","E1263","E1345","E1300","E1343","E1064","E01","E1261","E1118"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1218","E1107","E1063","E1138","E1041","E1140","E1206","E1320","E1219","E1062","E1316","E1244","E1121","E1205","E1155","E1032","E1007","E1308","E1253","E1057","E1159","E1076","E1084","E1048","E1166","E07","E1021","E1277","E1225","E1233","E1234","E1200","E1172","E1001","E1124"]},
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
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```