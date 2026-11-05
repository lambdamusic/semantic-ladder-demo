**Q1.** A-. E01's last action before 1 Jan 2025 was the assignment A12 (A-); the downgrade to BBB came later, on 2025-06-20.
**Q2.** No. E01's only 2026 actions (A03, A04) are affirmations.
**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ by A07.
**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity, and the latest action is A09 (POS).
**Q5.** A holder takes the credit risk of E02, the guarantor of I03. I03 is rated A.
**Q6.** The foreign-currency rating is BB and the local-currency rating is BBB-. E05 is domiciled in VD, where the Country Ceiling is BB (A12) and caps foreign-currency ratings but not local-currency ones.
**Q7.** The 2026 downgrades are listed in the JSON. E5033's downgrade is dated 2026-11-06, which is after today, so I excluded it. QA record E16 is also excluded.
**Q8.** E08, which went to RD on 2026-07-08 (A22).
**Q9.** 377, counting distinct LEIs with a non-withdrawn issuer rating on 1 Oct 2026.
**Q10.** Depends. E05 is BB on the foreign-currency basis and BBB- on the local-currency basis.
**Q11.** BBB+. A36 downgraded E14 on 2024-09-30.
**Q12.** A-, from A34.
**Q13.** One downgrade (A36). The later RW and AF actions are not downgrades.
**Q14.** None. E12 was first rated on 2024-02-01.
**Q15.** A-. E10 was downgraded to BBB+ only on 2026-04-15.
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+ after the 2026 affirmation.
**Q17.** No. E06 only went on Rating Watch Negative (A17).
**Q18.** Listed in the JSON.
**Q19.** Listed in the JSON.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.
**Q21.** Listed in the JSON.
**Q22.** Only E08, which reached RD in A22.
**Q23.** F2, from A04.
**Q24.** Yes. E01 is BBB.
**Q25.** 72 instruments, excluding EX actions.
**Q26.** A+, from A40.
**Q27.** A-. I06 is subordinated and rated by A42.
**Q28.** BBB+, from A38. The A in A37 is the Country Ceiling, not the sovereign's rating.
**Q29.** None. VD has only a Country Ceiling (A12).
**Q30.** Listed in the JSON, against a CV ceiling of A and a VD ceiling of BB.
**Q31.** No. No foreign-currency rating exceeds its ceiling.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** The holder takes the credit risk of E10, the guarantor of I05. I05 is rated BBB+ (A29).
**Q34.** No. E12 has no parent and is outside the E09 group.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2. E02 and E03 are one entity, and the other member is E04.
**Q37.** 495 distinct entities, grouping by LEI and excluding QA records.
**Q38.** No. They have different LEIs.
**Q39.** A.
**Q40.** 79.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding DE on E10.
**Q43.** 1.
**Q44.** Yes. I07 is in XVD, VD's domestic currency.
**Q45.** No. It is a local-currency obligation, which the ceiling does not cap.
**Q46.** No. E11 has only a credit opinion (A46).
**Q47.** None. I08 has only an Expected rating (A47), which is not a rating.
**Q48.** 113.
**Q49.** E5001. The chain runs E5047 → E5035 → E5023 → E5011 → E5167 (the same entity as E5005) → E5002 → E5001.
**Q50.** 6 levels.
**Q51.** 59.
**Q52.** 25.
**Q53.** No. They are in different groups.
**Q54.** E5106, E5124 and E5130.
**Q55.** 31.
**Q56.** BB-, held by E5144.
**Q57.** E5002.
**Q58.** E5145, guarantor of I5007, whose issuer E5133 is in a different group.
**Q59.** 12.
**Q60.** A holder takes E5145's credit risk, and it is not in the issuer's group.
**Q61.** 19. The top, E5001, is investment grade and is not counted.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E5019","E5059","E5097","E5113","E5116","E5156"]},
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
"Q18":{"issuers":["E1181","E1109","E1203","E1088","E1238","E1314","E1194","E1209","E1099","E1260","E1297","E1242","E1006","E1133","E1146","E1066","E1168","E1019","E1061","E1132","E06","E1098","E1266","E1126","E1267","E1037","E1013","E1317","E1323","E1059","E1039","E1264"]},
"Q19":{"issuers":["E1300","E5099","E1064","E5113","E5039","E1160","E5141","E1080","E1105","E1072","E1211","E1005","E1034","E1271","E1118","E1158","E1056","E1248","E5062","E5057","E1055","E5097","E1046","E5059","E5020","E1263","E5073","E1188","E1282","E01","E5102","E1029","E5131","E5023","E5116","E09","E1228","E1059","E1079","E5019","E5050","E1261","E5013","E1190","E5119","E1294","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1001","E1084","E1032","E1234","E1219","E1206","E1107","E1244","E1172","E1159","E1057","E1041","E07","E1062","E1277","E1155","E1253","E1121","E1063","E1166","E1021","E1200","E1048","E1124","E1076","E1138","E1140","E1316","E1308","E1007","E1218","E1225","E1205","E1320","E1233"]},
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
"Q37":{"count":495},
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
"Q51":{"count":59},
"Q52":{"count":25},
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