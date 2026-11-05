**Q1.** A-. E01's foreign-currency issuer rating was A- from 2024-03-12 to 2025-06-20 (action A01).

**Q2.** No. On 2026-02-10 only the outlook moved to Negative (A03), and the rating stayed BBB.

**Q3.** No. The 2031 note (I02) was cut to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's current rating is A with a POS outlook (A09).

**Q5.** The holder takes E02's credit risk (Northwind Holdings, the guarantor of I03), which is rated A (A09).

**Q6.** Not asked in the JSON. Valdoria Telecom (E05) is rated BB foreign-currency and BBB- local-currency (A14, A13). The data does not state the reason, though the VD ceiling of BB fits the foreign-currency cap.

**Q7.** Thirty-six issuers had a foreign-currency issuer-rating downgrade in 2026 (listed in the JSON). They include E08 and E10.

**Q8.** E08 (Saxby Shipping) is the only entity in default. Its rating has been RD since 2026-07-08 (A22).

**Q9.** 377. This counts distinct rated entities with a non-withdrawn issuer rating in force on 1 October 2026. I could not check whether it includes the two sovereigns.

**Q10.** Depends. E05 is BB in foreign currency (not investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+. Marlow's rating on 2025-06-01 was BBB+ (A36).

**Q12.** A-. Marlow's rating on 2024-01-01 was A- (A34).

**Q13.** 1. Only the 2024-09-30 downgrade from A- to BBB+ (A36) counts.

**Q14.** None. Halden Foods' first rating (E12, A30) began on 2024-02-01.

**Q15.** A-. E10's rating on 2026-01-01 was A- (A26).

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now. Only the watch and outlook changed (A35, A33).

**Q17.** No. The 2026-09-03 action on E06 was a Rating Watch Negative placement (A17) with the rating unchanged at A-.

**Q18.** Thirty-two issuers were on Rating Watch Negative (listed in the JSON).

**Q19.** Forty-seven issuers had a Negative outlook (listed in the JSON).

**Q20.** No. E07's rating was withdrawn (WD, A19), which is not a default rating.

**Q21.** Thirty-five entities had an issuer rating that was later withdrawn and no longer had one on 1 October 2026 (listed in the JSON). They include E07.

**Q22.** E08 is the only entity ever rated RD, D or SD.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB.

**Q25.** 72 instruments were rated BBB- or higher on 1 October 2026.

**Q26.** A+ (A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (A38).

**Q29.** None. The data holds no rating records for the Republic of Valdoria (VD).

**Q30.** Thirteen entities were exactly at their country's ceiling (listed in the JSON). They include E05 and E15.

**Q31.** No. No non-sovereign issuer was rated above its country ceiling.

**Q32.** E09 (Halden Group plc).

**Q33.** The holder takes E10's credit risk (Halden Bank, the guarantor of I05), which is rated BBB+ (A27).

**Q34.** No. E12 has no parent and is its own group, while E10 sits under E09.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 497. The entities table is already merged, with 497 unique entity_ids.

**Q38.** No. E06 and E13 are separate entities, each with its own record.

**Q39.** A (A09).

**Q40.** 79 distinct GB issuers.

**Q41.** None. No Brindle Capital entity turned up in my entity search.

**Q42.** LU (E10, Halden Bank).

**Q43.** 1 (E10 is the only LU entity).

**Q44.** Yes. I07 has local_currency = yes and is denominated in XVD.

**Q45.** Yes. I07 is rated BBB-, which is above the VD ceiling of BB.

**Q46.** No. E11 has no rating records.

**Q47.** None. I08 has no rating records.

**Q48.** 113 instruments held a rating on 1 October 2026.

**Q49.** E5001 (Cerid Group plc).

**Q50.** 6 levels, from the ancestors table (E5001 is at level 6 above E5047).

**Q51.** 58.

**Q52.** 19.

**Q53.** No. E5062 belongs to the E5059 group and E5086 is a separate top entity.

**Q54.** E5106, E5124 and E5130.

**Q55.** 31 rated entities have a VD-domiciled entity above them.

**Q56.** BB-. E5144 holds BB- as the lowest foreign-currency issuer rating in the Vesol group.

**Q57.** E5002 (Cerid Energy plc). E5011's chain runs E5005, E5002, E5001 and E5013's runs E5006, E5002, E5001.

**Q58.** E5145 (Geren Group SA). It guarantees I5007, which E5133 (Vesol group) issued.

**Q59.** 12.

**Q60.** The holder takes E5145's credit risk (the guarantor of I5007). It is not in the issuer's group, since the issuer E5133 sits under E5132.

**Q61.** 19 Cerid group members hold a foreign-currency issuer rating below investment grade.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1080","E1064","E1093","E1167","E1058","E08","E1186","E1169","E1112","E1290","E1285","E5156","E1255","E1263","E1228","E1229","E1298","E1307","E1151","E1294","E1051","E1160","E10","E5059","E1144","E1159","E1057","E1053","E5113","E1243","E5019","E1163","E5097","E1213","E1300"]},
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
"Q18":{"issuers":["E06","E1133","E1006","E1019","E1264","E1013","E1061","E1238","E1297","E1037","E1209","E1242","E1317","E1039","E1059","E1266","E1109","E1168","E1088","E1194","E1099","E1132","E1260","E1066","E1146","E1203","E1314","E1323","E1181","E1098","E1126","E1267"]},
"Q19":{"issuers":["E1055","E1294","E5119","E5141","E09","E1211","E5019","E5113","E5131","E1005","E1080","E5116","E1034","E1188","E1248","E5057","E1056","E1059","E1282","E5013","E5023","E5062","E1271","E1105","E1158","E01","E1064","E1118","E1261","E1046","E1228","E1263","E5050","E5073","E5099","E1072","E1190","E5039","E5156","E1079","E1029","E1160","E5020","E5059","E1300","E5097","E5102"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1062","E1218","E1041","E1063","E1107","E1138","E1140","E1206","E1219","E1320","E1121","E1205","E1244","E1316","E1048","E1084","E1076","E07","E1021","E1166","E1001","E1124","E1172","E1277","E1200","E1225","E1233","E1234"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E5012","E1236","E5047","E1194","E5091","E15","E5116","E5124","E1028","E1126","E05","E1101","E1039"]},
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
"Q45":{"above_ceiling":"yes"},
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