**Q1.** A-. E01's LTIDR FC was set by A01 (A-, 2024-03-12) and not changed until the downgrade A02 on 2025-06-20.
**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the outlook moved to NEG but the rating stayed BBB.
**Q3.** No, it is BB+. The 2031 note I02 is subordinated and was downgraded to BB+ by A07.
**Q4.** POS. E02 and E03 share one LEI, so they are one entity; the latest action is A09 (E03, 2025-09-15), affirmed A with a Positive outlook.
**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so it carries the guarantor's credit risk, and E02's latest rating is A (A08, A09).
**Q6.** Valdoria's Country Ceiling is BB (A12), and it caps foreign-currency ratings but not local-currency ones. E05's FC rating is BB (A14) and its LC rating is BBB- (A13).
**Q7.** 38 issuers had an LTIDR downgrade (DG) dated in 2026, including E08 and E10; the full list is in the JSON. Withdrawals, Watches and affirmations were not counted.
**Q8.** E08. Saxby Shipping was downgraded to RD by A22 on 2026-07-08 and no later action changed that.
**Q9.** 377. This counts distinct entities (records merged by LEI, QA excluded) whose latest LTIDR on 1 Oct 2026 was not a withdrawal.
**Q10.** Depends. E05's foreign-currency rating is BB (speculative grade) and its local-currency rating is BBB- (investment grade).
**Q11.** BBB+. A36 (2024-09-30) set BBB+ and the next action, A35 (2025-11-20), came later.
**Q12.** A-. A34 (2023-01-15) set it and A36 did not follow until 2024-09-30.
**Q13.** 1. The only downgrade is A36.
**Q14.** None. E12's first rating was A30 on 2024-02-01.
**Q15.** A-. E10 and E17 are one entity; the downgrade to BBB+ (A27) came on 2026-04-15.
**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now; A35 and A33 only changed the Watch status.
**Q17.** No. E06's only 2026 action is A17, a Rating Watch (RW), which is not a downgrade.
**Q18.** 32 issuers; the list is in the JSON and includes E06.
**Q19.** 47 issuers; the list is in the JSON and includes E01 and E09.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default; its last rating before that was BB.
**Q21.** 35 entities had an issuer rating at some point and none on 1 Oct 2026 (the latest action was a withdrawal), including E07; the list is in the JSON.
**Q22.** E08 only. It went to RD via A22.
**Q23.** F2 (A04).
**Q24.** Yes. E01's LTIDR is BBB.
**Q25.** 72. Of the 113 instruments with a rating in force on 1 Oct 2026, 72 were BBB- or higher; Expected ratings (EX) are not ratings.
**Q26.** A+ (A40, the LC rating).
**Q27.** A-. I06 was assigned A- by A42.
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not its issuer rating.
**Q30.** 13 entities have an FC rating equal to their country's ceiling, including E15 and E05; the list is in the JSON.
**Q31.** No. No non-sovereign FC rating was above its country's ceiling.
**Q32.** E09, Halden Group plc. E11's parent is E10, whose parent is E09.
**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).
**Q34.** No. E12 has no parent and sits outside the E09 group.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 497. This is the count after merging records by LEI and excluding QA records.
**Q38.** No. They have different LEIs (E06 and E13).
**Q39.** A (A09).
**Q40.** 79, after taking country from the RESEARCH record where records disagree.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** LU. E10 and E17 are the same entity, and RESEARCH's record (E17) holds for domicile.
**Q43.** 1 (E10/E17).
**Q44.** Yes. I07 pays in XVD, Valdoria's domestic currency.
**Q45.** No. The ceiling does not apply to local-currency debt; I07 is rated BBB- against a ceiling of BB.
**Q46.** No. E11 has only a Credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), so it is still unrated.
**Q48.** 113.
**Q49.** E5001. The chain from Cerid Rosor Holdings SA to the top is 6 levels.
**Q50.** 6.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. E5168 is the RESEARCH duplicate of E5062 (same LEI), and RATINGS holds for parent links, so Belir Mining sits in the Belir group, not Rotam.
**Q54.** E5106, E5124 and E5130. E5106 counts because RESEARCH (E5169) puts it in VD.
**Q55.** 31 distinct rated entities have a VD-domiciled entity above them in their chain of parents.
**Q56.** BB-. E5144 is the lowest of the group's current FC ratings.
**Q57.** E5002, 2 levels above each of them.
**Q58.** E5145. It guarantees I5007, issued by E5133 in a different group.
**Q59.** 12.
**Q60.** Geren Group SA (E5145). It is not in the issuer's group: E5133 is in the Vesol group and E5145 is in the Geren group.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1294","E1151","E1034","E1213","E1300","E1163","E5097","E5019","E5113","E1159","E1057","E1053","E1144","E1243","E1229","E1307","E5033","E1255","E1263","E1228","E1298","E1080","E5116","E1186","E1112","E1169","E08","E1285","E1290","E1064","E1093","E1051","E1058","E1167","E5156","E10","E5059","E1160"]},
"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1013","E1297","E1238","E1061","E1317","E1242","E1037","E1209","E1181","E1133","E06","E1194","E1088","E1098","E1126","E1019","E1006","E1264","E1146","E1203","E1066","E1314","E1323","E1168","E1109","E1267","E1059","E1266","E1039","E1099","E1132","E1260"]},
"Q19":{"issuers":["E1080","E1005","E5116","E1046","E1034","E1188","E5057","E1248","E5073","E5099","E1263","E1228","E5050","E1064","E1261","E01","E1118","E5020","E1029","E5059","E1160","E5019","E5113","E1211","E5131","E09","E1158","E1105","E1079","E1055","E1294","E5119","E5141","E1271","E1190","E1072","E5156","E5039","E1300","E5102","E5097","E1059","E5062","E5013","E5023","E1056","E1282"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1218","E1316","E1244","E1234","E1233","E1200","E1225","E1076","E1057","E1155","E1308","E1253","E1032","E1159","E1007","E1062","E1277","E1219","E1206","E1320","E1001","E1124","E1172","E1048","E1084","E1021","E07","E1166","E1041","E1138","E1063","E1107","E1140","E1205","E1121"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E5047","E1194","E5124","E15","E1101","E1039","E1028","E5116","E5091","E1126","E1236","E5012","E05"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":497},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5124","E5130"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```