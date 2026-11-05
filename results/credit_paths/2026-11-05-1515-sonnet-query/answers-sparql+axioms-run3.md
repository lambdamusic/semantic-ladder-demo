**Q1.** A-. Kestrel's FC issuer rating was set to A- by A01 (2024-03-12), and it held until the downgrade on 2025-06-20 (A02).
**Q2.** No. Kestrel's 2025-06-20 downgrade (A02) was in 2025, and the 2026-02-10 action (A03) was an affirmation with a Negative outlook.
**Q3.** No. The 2031 note (I02) is subordinated and currently rated BB+ (A07), which is speculative grade.
**Q4.** Positive. Northwind Holdings' records E02 and E03 share an LEI, so they are one entity, and A09 (2025-09-15) affirmed A with a Positive outlook.
**Q5.** The notes (I03) carry the credit risk of E02, the guarantor. They are rated A (A11).
**Q6.** The data has no recorded reason, so I can't answer why. Valdoria Telecom's FC rating is BB, which matches the Valdoria Country Ceiling (BB), and its LC rating is BBB- (A13, A14); the ceiling is the likely cause, but that is an inference.
**Q7.** Entities with a long-term issuer-rating downgrade dated in 2026, QA records excluded, are listed in the JSON. One of them, E5033, has a downgrade dated 2026-11-06, which is after today's date.
**Q8.** E08 (Saxby Shipping) was in default. It has been rated RD since 2026-07-08 (A22).
**Q9.** 377. This is 376 distinct LEIs with a long-term issuer rating in force, plus the Republic of Corvenia (CV), which has no LEI but holds FC and LC ratings.
**Q10.** Depends. Its FC rating is BB (speculative) and its LC rating is BBB- (investment grade).
**Q11.** BBB+ (A36, in force from 2024-09-30 to 2025-11-20).
**Q12.** A- (A34).
**Q13.** One time (A36).
**Q14.** None. Halden Foods' first rating, BB-, was assigned on 2024-02-01 (A30).
**Q15.** A-. Halden Bank's A26 held until the 2026-04-15 downgrade (A27).
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; the Watch and the affirmation (A35, A33) did not change the rating.
**Q17.** No. Orrin Bank's only 2026 action is a Watch Negative (A17), which is not a downgrade.
**Q18.** The entities on Rating Watch Negative on 1 October 2026 are listed in the JSON; they include E06 and E1059 (an LC rating).
**Q19.** The entities with a Negative outlook on 1 October 2026 are listed in the JSON.
**Q20.** No. Pellam's rating was withdrawn on 2026-05-12 (A19), and a withdrawal is not a default.
**Q21.** The entities that once held an issuer rating but had none in force on 1 October 2026 are listed in the JSON; they include E07, whose rating was withdrawn.
**Q22.** Only E08, which reached RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 72 instruments held an investment-grade rating in force on 1 October 2026.
**Q26.** A+ (A40, LC).
**Q27.** A- (A42).
**Q28.** BBB+ (A38). The Country Ceiling of A (A37) is a separate item.
**Q29.** None. Valdoria has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** Four CV entities (A) and nine VD entities (BB) have an FC rating exactly at their country's ceiling; they are listed in the JSON.
**Q31.** No.
**Q32.** E09 (Halden Group plc).
**Q33.** The notes (I05) carry the credit risk of E10, the guarantor. They are rated BBB+ (A29).
**Q34.** No. Halden Foods (E12) has no parent and is its own ultimate parent, separate from E09.
**Q35.** 3 (E09, E10/E17 which are the same entity, and E11).
**Q36.** 2 (E02/E03 and E04).
**Q37.** 497. This is 495 distinct non-QA LEIs plus the two sovereigns (CV and VD), which have no LEI.
**Q38.** No. They have different LEIs (E06 and E13).
**Q39.** A (A09).
**Q40.** 79.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. RESEARCH record E17 holds for domicile over RATINGS record E10, which says DE.
**Q43.** 1 (E10/E17).
**Q44.** Yes. I07 is in XVD with localCurrency true.
**Q45.** No. A local-currency note is not capped by the ceiling.
**Q46.** No. E11 is a finance subsidiary with only a private CO rating (A46), which does not count.
**Q47.** None. I08 has only an EX action (A47), so it is still unrated.
**Q48.** 113 instruments held a rating in force on 1 October 2026.
**Q49.** E5001 (Cerid Group plc).
**Q50.** 6. The chain is E5035, E5023, E5011, E5005 (same entity as E5167), E5002, E5001.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. They have different ultimate parents (E5059 and E5086).
**Q54.** E5130, E5124 and E5106. E5169 is a duplicate record of E5106.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002 (Cerid Energy plc).
**Q58.** E5145, which guarantees the Cross-group note (I5007) issued by E5133 in the Vesol group.
**Q59.** 12.
**Q60.** The holders take the credit risk of E5145 (the guarantor), which is not in the same group as the issuer E5133.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09","E5013","E5019","E5020","E5023","E5033","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E07"]},
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
"Q54":{"entities":["E5130","E5124","E5106"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":19}
}
```