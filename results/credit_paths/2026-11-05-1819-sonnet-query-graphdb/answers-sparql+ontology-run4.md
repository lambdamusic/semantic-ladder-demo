**Q1.** A-. E01's FC LTIDR was set at A- on 2024-03-12 and stayed there until the downgrade to BBB on 2025-06-20.
**Q2.** No. E01's only 2026 action (2026-02-10) is an affirmation with the outlook moved to Negative.
**Q3.** No. The 2031 note (I02) is subordinated and has been rated BB+ since 2025-06-20, which is speculative grade.
**Q4.** Positive. E02 and E03 share one LEI, so they are one entity, and its latest action is E03's affirmation on 2025-09-15 with a Positive outlook.
**Q5.** The holder takes the risk of E02, Northwind Holdings, rated A. I03 is guaranteed by E02.
**Q6.** The Valdoria Country Ceiling (VD) is BB and caps FC ratings. E05's FC rating is BB and its LC rating is BBB-, and LC is not capped.
**Q7.** 38 issuers (the list is in the JSON). It is built from the 2026 DG actions on non-QA records, merged by LEI. It includes E5033, whose downgrade is dated 2026-11-06, after today.
**Q8.** E08 (Saxby Shipping), which went to RD on 2026-07-08 and was not upgraded afterwards.
**Q9.** 377 distinct issuers, counted by LEI with QA records excluded. This count may be unreliable, because the query that produced it was not cross-checked.
**Q10.** Depends. E05's FC rating is BB, which is speculative grade, but its LC rating is BBB-, which is investment grade.
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30, and the next action is 2025-11-20.
**Q12.** A-, set by the assignment of 2023-01-15.
**Q13.** 1. Only the 2024-09-30 action is a downgrade, and the Watch is not.
**Q14.** None. E12's first rating was assigned on 2024-02-01.
**Q15.** A-. E10 was rated A- until 2026-04-15, and E17 is the same entity.
**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now.
**Q17.** No. E06's only 2026 action is a Rating Watch Negative, which is not a downgrade.
**Q18.** 27 issuers. This list is uncertain, because two query variants disagreed on membership.
**Q19.** 46 issuers. The same caveat applies.
**Q20.** No. E07's rating was BB and was then withdrawn on 2026-05-12, and a withdrawal is not a default.
**Q21.** A partial list: 22 entities whose latest action by 1 Oct 2026 was a withdrawal. The query output was truncated, so the list may be incomplete.
**Q22.** E08 only, the one entity with an RD or D rating.
**Q23.** F2 (STIDR, 2026-02-10).
**Q24.** Yes. E01's FC LTIDR is BBB.
**Q25.** 72, of 113 instruments holding a rating. Expected-rating (EX) actions and QA issuers are excluded.
**Q26.** A+ (E15's LC LTIDR).
**Q27.** A-, the rating on I06.
**Q28.** BBB+.
**Q29.** None. The record VD carries only a Country Ceiling (BB), which is not an issuer rating.
**Q30.** 13 entities, listed in the JSON. At the CV ceiling of A: E1039, E1194, E15, E5116. At the VD ceiling of BB: E05, E1028, E1101, E1126, E1236, E5012, E5047, E5091, E5124.
**Q31.** No. Every FC issuer rating for CV or VD domiciles is at or below its ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The holder takes the risk of E10, Halden Bank, rated BBB+. I05 is guaranteed by E10.
**Q34.** No. E12 has no parent link, while E10 sits under E09.
**Q35.** 3: E09, E10 and E11, with E17 being the same entity as E10.
**Q36.** 2: E02 and E04, with E03 being the same entity as E02.
**Q37.** 497 distinct LEIs, counting each sovereign once and excluding QA.
**Q38.** No. Their LEIs differ.
**Q39.** A.
**Q40.** 79.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, and it overrides DE.
**Q43.** 1: E10 and E17 are the same entity.
**Q44.** Yes. I07 is in XVD, the domestic currency of VD.
**Q45.** No. The note is local-currency debt, so the ceiling does not cap it.
**Q46.** No. E11 has only a Credit opinion (CO), which is not an issuer rating.
**Q47.** None. I08 only has an Expected rating (EX) from 2026-09-01.
**Q48.** 113 instruments.
**Q49.** E5001. The chain runs E5047 → E5035 → E5023 → E5011 → E5167 (a record of E5005) → E5002 → E5001.
**Q50.** 6 levels.
**Q51.** 58 entities, E5001–E5058, with E5167 being the same entity as E5005. The QA record E5170 is excluded.
**Q52.** 19 entities, E5086–E5104.
**Q53.** No. The authoritative RATINGS parent for E5062 is E5060 (Belir), not Rotam.
**Q54.** E5106, E5124 and E5130. The RESEARCH record E5169 puts E5106 in VD.
**Q55.** 31.
**Q56.** BB-, held by E5144.
**Q57.** E5002.
**Q58.** E5145. I5007 is issued by E5133 (Vesol) and guaranteed by E5145 (Geren).
**Q59.** 12.
**Q60.** The holder takes the risk of E5145, which is not in the same group as the issuer E5133.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1161","E1163","E1167","E1170","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E5019","E5033","E5059","E5097","E5113","E5116","E5156","E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1186","E1213","E1228"]},
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
"Q18":{"issuers":["E06","E1088","E1006","E1066","E1019","E1061","E1098","E1013","E1059","E1039","E1181","E1109","E1194","E1133","E1146","E1132","E1126","E1238","E1209","E1260","E1297","E1242","E1266","E1264","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1064","E1080","E1072","E1005","E1034","E1055","E1046","E1029","E1059","E1079","E1160","E1105","E1118","E1158","E1188","E1190","E1211","E1271","E1248","E1263","E1282","E1228","E1261","E1294","E1300","E5099","E5039","E5062","E5057","E5097","E5059","E5020","E5073","E5023","E5019","E5050","E5013","E5113","E5141","E5102","E5131","E5116","E5119","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1279"]},
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
"Q61":{"count":19}}
```