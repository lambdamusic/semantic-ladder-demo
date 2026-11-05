**Q1.** A-. E01's rating was set by A01 (assigned 2024-03-12) and not changed until the downgrade A02 on 2025-06-20.
**Q2.** No. The only 2026 actions on E01 are A03 (affirmed, outlook moved to NEG) and A04 (short-term affirmed), and neither is a downgrade.
**Q3.** No, BB+. The 2031 note is I02, a subordinated note; its latest action is the downgrade A07 to BB+, which is speculative grade.
**Q4.** POS. E02 and E03 share one LEI and are one entity, and the latest action is A09 (E03, 2025-09-15) with a Positive outlook.
**Q5.** The holder takes E02's credit risk, rated A. I03 is issued by the finance subsidiary E04 and guaranteed by E02, whose latest rating is A (A08/A09).
**Q6.** Valdoria Telecom's FC rating is BB and its LC rating is BBB- (A14, A13). The FC rating is capped by Valdoria's Country Ceiling of BB (A12), while LC is not capped.
**Q7.** See the list in the JSON. These are the entities with an LTIDR downgrade (DG) in 2026 up to today, 2026-11-05, with duplicate records merged by LEI. A5028 is dated 2026-11-06, after today, so E5033 is not counted.
**Q8.** E08. A22 on 2026-07-08 moved it to RD, a restricted default, after a distressed debt exchange.
**Q9.** 377. This counts distinct entities (merged by LEI) whose latest LTIDR on or before 2026-10-01 is not WD, excluding QA records.
**Q10.** Depends. E05 is BB on foreign currency (A14) and BBB- on local currency (A13), so the answer depends on which basis is meant.
**Q11.** BBB+. The downgrade A36 on 2024-09-30 applies, and the later RW (A35) leaves the rating unchanged.
**Q12.** A-, set by A34 on 2023-01-15.
**Q13.** 1. The only downgrade of E14 is A36.
**Q14.** None. E12's first rating, A30, is dated 2024-02-01.
**Q15.** A-. E10's downgrade to BBB+ (A27) is dated 2026-04-15, after 1 January 2026.
**Q16.** No. E14 was BBB+ on 1 January 2025 and is BBB+ now (A33).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement with the rating unchanged.
**Q18.** See the list in the JSON. These are entities whose latest LTIDR action on or before 2026-10-01 carries an RWN watch, including E06 (A17).
**Q19.** See the list in the JSON. These are entities whose latest LTIDR action on or before 2026-10-01 carries a NEG outlook, including E01 and E09.
**Q20.** No. E07 was withdrawn (A19, commercial reasons), which is not a default, and its last rating before that was BB.
**Q21.** See the list in the JSON. These are entities that had an LTIDR but whose latest LTIDR on 2026-10-01 is a withdrawal, including E07.
**Q22.** E08. It is the only entity with an RD or D rating (A22).
**Q23.** F2, from A04.
**Q24.** Yes. E01's rating is BBB (A02, affirmed by A03).
**Q25.** 72. Of 113 instruments with a rating on 2026-10-01, 72 are investment grade; expected ratings (EX) are not counted.
**Q26.** A+, from A40.
**Q27.** A-. I06 was assigned A- by A42.
**Q28.** BBB+, from A38. The Country Ceiling of A (A37) is not the sovereign's rating.
**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.
**Q30.** See the list in the JSON. These are entities whose FC LTIDR equalled their country's ceiling on 2026-10-01, using the RESEARCH country where records disagree.
**Q31.** No. No FC rating sits above the ceiling of its country.
**Q32.** E09. E11's parent is E10, whose parent is E09, which has no parent.
**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and E10's latest rating is BBB+ (A27).
**Q34.** No. E12 has no parent and is not linked to E09 or E10.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 497. This counts distinct LEIs, or the record ID where there is no LEI, excluding QA records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A, from A08 and A09. The Positive outlook does not change the rating.
**Q40.** 79. This counts distinct entities rated on 2026-10-01 and domiciled in GB.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.
**Q43.** 1.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** No. I07 is rated BBB- (A45) against a ceiling of BB, but local-currency debt is not capped by the ceiling.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an expected rating (A47), so it is still unrated.
**Q48.** 113. This counts instruments with a non-withdrawn rating on 2026-10-01 and excludes 9 with EX only.
**Q49.** E5001. The chain from E5047 reaches E5001 at depth 6.
**Q50.** 6.
**Q51.** 58.
**Q52.** 19. This is the group of E5086.
**Q53.** No. RATINGS holds for parent links, so E5062 sits in the E5059 group, while E5086 heads its own group. The RESEARCH record E5168 that points to E5086 is overridden.
**Q54.** E5106, E5124, E5130.
**Q55.** 31.
**Q56.** BB-, held by E5144.
**Q57.** E5002. Both E5011 and E5013 reach it at 2 levels up; the next shared ancestor is E5001.
**Q58.** E5145. It guarantees I5007, which is issued by E5133, in a different group.
**Q59.** 12.
**Q60.** The holder takes E5145's credit risk, and E5145 is not in the same group as the issuer E5133. E5133 sits in the group of E5132, while E5145 heads its own group.
**Q61.** 19. This counts group members whose current FC LTIDR is below BBB-.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1058","E1167","E1285","E1290","E08","E1112","E1186","E1169","E5116","E1080","E5059","E10","E1160","E1064","E1093","E1151","E1294","E5156","E5019","E5113","E1053","E1057","E1144","E1159","E1243","E1051","E1228","E1229","E1255","E1263","E1307","E1298","E5097","E1163","E1300","E1213","E1034"]},
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
"Q18":{"issuers":["E1039","E1266","E1059","E1099","E1132","E1260","E1013","E1061","E1297","E1238","E06","E1133","E1181","E1037","E1242","E1317","E1209","E1098","E1126","E1088","E1194","E1267","E1006","E1019","E1264","E1066","E1146","E1203","E1314","E1323","E1109","E1168"]},
"Q19":{"issuers":["E5019","E5113","E5131","E09","E1211","E1046","E5116","E1005","E1080","E1228","E5050","E5073","E5099","E1263","E1105","E1158","E5039","E5156","E1072","E1190","E5013","E5023","E1056","E1282","E1059","E5062","E5020","E5059","E1029","E1160","E1248","E5057","E1034","E1188","E01","E1064","E1118","E1261","E5097","E5102","E1300","E1079","E1271","E5119","E5141","E1055","E1294"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1166","E1021","E1076","E1206","E1219","E1320","E1041","E1063","E1107","E1140","E1138","E1048","E1084","E1244","E1316","E1218","E1007","E1032","E1057","E1155","E1159","E1308","E1253","E1062","E1277","E1121","E1205","E1233","E1200","E1225","E1234","E1124","E1172","E1001"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes","rating":"BBB"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1028","E1126","E1101","E05","E5047","E1236","E5091","E1194","E5116","E5124","E15","E5012"]},
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
"Q52":{"count":19},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106","E5124","E5130"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":19}
}
```