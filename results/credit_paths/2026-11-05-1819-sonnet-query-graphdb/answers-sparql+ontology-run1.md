**Q1.** A-. The 12 Mar 2024 assignment (E01) set A-, and the downgrade to BBB came on 20 Jun 2025, after this date.
**Q2.** No. E01's only 2026 action (10 Feb) was an affirmation with the outlook moved to Negative.
**Q3.** No, it is BB+. I02 is subordinated and was rated BBB at assignment, then BB+ after the 2025 downgrade.
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action (E03, 15 Sep 2025) set POS.
**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, whose current rating is A.
**Q6.** Valdoria Telecom (E05) has FC BB against LC BBB-. The FC rating is capped by Valdoria's Country Ceiling, which is BB, while the LC rating is not capped.
**Q7.** There are 38 issuers with a Downgrade action dated in 2026, listed below. The query counted any rating type and used the record IDs that carried the actions.
**Q8.** E08. It was downgraded to RD on 8 Jul 2026.
**Q9.** 377 distinct issuers, counted by LEI, across LTIDR and STIDR ratings still in force. QA records are excluded and withdrawals are not counted as ratings.
**Q10.** Depends. E05 is BB on foreign currency (speculative grade) and BBB- on local currency (investment grade).
**Q11.** BBB+. E14 was downgraded on 30 Sep 2024.
**Q12.** A-, from the 15 Jan 2023 assignment.
**Q13.** 1. Only the 30 Sep 2024 action is a downgrade; the Watch and the affirmation are not.
**Q14.** None. E12's first rating was assigned on 1 Feb 2024.
**Q15.** A-. E10 was not downgraded to BBB+ until 15 Apr 2026.
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now.
**Q17.** No. E06 only had a Rating Watch Negative placed on 3 Sep 2026.
**Q18.** 32 issuers, listed below.
**Q19.** 47 issuers, listed below. The query also returned three entities (E1106, E1218, E1308) with neither a Watch nor an outlook value, which I did not count.
**Q20.** No. E07's rating was withdrawn for commercial reasons, which is not a default.
**Q21.** 35 entities, listed below.
**Q22.** Only E08 (RD).
**Q23.** F2.
**Q24.** Yes. E01 is BBB.
**Q25.** 72 instruments.
**Q26.** A+ (E15, LC).
**Q27.** A-. I06 is the subordinated note, and its rating dates from 2024-03-01.
**Q28.** BBB+. The Country Ceiling record for CV is separate and is not the sovereign's rating.
**Q29.** None. VD has only a Country Ceiling (BB), no issuer rating.
**Q30.** 13 entities have an FC rating exactly at their ceiling. The ceilings are A for CV and BB for VD, and domicile follows the RESEARCH record where records disagree.
**Q31.** No. No company's FC rating is above its ceiling.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ in 2026.
**Q34.** No. E12 has no parent and is outside E09's group.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04). E03 is the same entity as E02.
**Q37.** 497. There are 495 distinct LEIs among non-QA records, plus the two sovereigns (CV, VD) that have none.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A.
**Q40.** 79.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** LU. The RESEARCH record E17 holds for country, over DE on E10.
**Q43.** 1. It is the single entity with LEI 391200QYPVFF2O9K2039 (E10/E17).
**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency.
**Q45.** No. I07 is local-currency, so the ceiling does not cap it.
**Q46.** No. E11 has only a Credit opinion (CO), which is not an issuer rating.
**Q47.** None. I08 has only an Expected-rating (EX) action, so it is still unrated.
**Q48.** 113.
**Q49.** E5001, Cerid Group plc.
**Q50.** 6. The levels are E5035, E5023, E5011, E5005, E5002, E5001.
**Q51.** 58.
**Q52.** 24.
**Q53.** No. Belir Mining's chain ends at E5059, Belir Group AG, which is not in Rotam's group.
**Q54.** E5106, E5124 and E5130.
**Q55.** 31.
**Q56.** BB-.
**Q57.** E5002, Cerid Energy plc.
**Q58.** E5059 and E5145. They guarantee I5002 and I5007, whose issuers (E5062, E5133) are in different groups.
**Q59.** 12.
**Q60.** The holder takes E5145's credit risk, and E5145 is not in the issuer's group.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1300","E1151","E1167","E1080","E5113","E1051","E10","E1034","E1290","E1229","E5097","E5059","E1255","E1186","E1161","E1263","E1058","E1112","E08","E5116","E1170","E1228","E1163","E1243","E5033","E1299","E5019","E1053","E1213","E1159","E1057","E1064","E1294","E1093","E1144","E1307","E5156"]},
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
"Q18":{"issuers":["E1203","E1314","E1194","E1210","E1260","E1133","E1146","E1242","E1066","E1168","E1297","E1109","E1061","E1132","E1088","E06","E1098","E1266","E1006","E1267","E1037","E1013","E1317","E1181","E1323","E1059","E1099","E1238","E1264","E1039","E1126","E1019"]},
"Q19":{"issuers":["E1300","E5099","E1080","E1105","E5113","E1034","E1118","E1056","E1064","E1055","E5097","E1046","E5059","E5020","E1161","E1263","E1282","E01","E5131","E5023","E5141","E5116","E09","E1271","E5039","E5102","E1228","E1060","E5073","E1079","E5019","E5050","E5062","E1072","E1190","E1005","E1248","E5057","E1294","E1188","E5119","E1029","E5013","E1262","E1158","E5156","E1211"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1084","E1032","E1234","E1219","E1206","E1107","E1244","E1172","E1159","E1057","E1041","E07","E1062","E1277","E1155","E1254","E1121","E1063","E1166","E1021","E1200","E1048","E1124","E1076","E1138","E1140","E1316","E1308","E1007","E1218","E1225","E1205","E1320","E1233"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1194","E15","E5116","E1039","E1101","E1028","E5012","E1236","E5047","E5124","E5091","E1126","E05"]},
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
"Q52":{"count":24},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106","E5124","E5130"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5059","E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":19}
}
```