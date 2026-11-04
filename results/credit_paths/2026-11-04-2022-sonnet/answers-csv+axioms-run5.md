**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12) until A02 downgraded it to BBB on 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB.
**Q3.** No. I02 is rated BB+ after A07 (2025-06-20) downgraded it from BBB (A23).
**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.
**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and A09 is the rating in force.
**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13).
**Q7.** 37 entities, listed in the JSON, with the following caveats:
- QA test records are excluded.
- The future-dated A5028 (2026-11-06) is excluded.
- Instrument downgrades are not counted.
- Research duplicates are given under the rated ID.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, and it was still in force on 1 October 2026.
**Q9.** 377. This is distinct LEIs whose latest LTIDR or STIDR action is not a withdrawal, excluding QA records. Note that E1115, E1158 and E1303 stay rated because of later UG, AF and UG actions after their withdrawals, and E1106 and E1279 stay rated on one currency basis.
**Q10.** Depends. E05 is BBB- on local currency (A13, investment grade) but BB on foreign currency (A14, not).
**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the later actions are only a watch and an affirmation.
**Q12.** A-, from A34.
**Q13.** 1, which is A36.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. A26 assigned it, and A27's downgrade came only on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 is a watch, A33 an affirmation).
**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch placement.
**Q18.** 32 issuers, listed in the JSON. Each has a watch placement as its latest action in the series.
**Q19.** 44 issuers, listed in the JSON. Each has a NEG outlook on its latest action, and watch placements carry no outlook.
**Q20.** No. E07 was rated BB (A18) and then withdrawn (A19), and never defaulted.
**Q21.** 35 entities, listed in the JSON. Their latest action is a withdrawal.
**Q22.** E08 only. It is the only entity with an RD or D rating (A22).
**Q23.** F2, from A04.
**Q24.** Yes. A03 affirmed BBB.
**Q25.** 72. This counts instruments whose latest INST rating is BBB- or better; EX actions are not ratings in force.
**Q26.** A+, from A40 (LC).
**Q27.** A-, from A42.
**Q28.** BBB+, from A38.
**Q29.** None. VD has only a Country Ceiling (A12, BB), not an issuer rating.
**Q30.** 12 entities, listed in the JSON. Eight sit at VD's BB ceiling (E05, E1028, E1101, E1126, E1236, E5012, E5047, E5124) and four at CV's A ceiling (E15, E1039, E1194, E5116).
**Q31.** No. No VD entity is above BB and no CV entity is above A on a foreign-currency basis.
**Q32.** E09. E11 → E10 → E09.
**Q33.** Halden Bank AG (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded it.
**Q34.** No. E12 has no parent link, and E10's parent is E09.
**Q35.** 3: E09, E10 (E17 has the same LEI) and E11.
**Q36.** 2: E02 (E03 is the same LEI) and E04.
**Q37.** 497. That is 540 records, less 14 QA records and 29 research duplicates sharing an LEI.
**Q38.** No. They have different LEIs and countries.
**Q39.** A, from A09.
**Q40.** 79. This counts GB-domiciled entities with an issuer rating in force.
**Q41.** None. E16 is a QA test record, so its actions are not rating actions.
**Q42.** LU. The research record E17 shares E10's LEI and gives LU.
**Q43.** 1. E10 and E17 are the same entity.
**Q44.** Yes. I07 is in XVD and E05 is domiciled in VD.
**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is local-currency.
**Q46.** No. E11 has only a credit opinion (A46).
**Q47.** None. I08 has only an expected rating (A47, EX).
**Q48.** 113. Eight instruments have only an EX action and no rating in force: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049, which is 9 with I08.
**Q49.** E5001. E5047 → E5035 → E5023 → E5011 → E5005 → E5002 → E5001. E5011's parent E5167 shares E5005's LEI.
**Q50.** 6 levels.
**Q51.** 58, which is E5001–E5058.
**Q52.** 19, which is E5086–E5104.
**Q53.** No. The rules use the RATINGS parent (E5060, the Belir chain), not the research record's parent E5086.
**Q54.** E5106, E5124 and E5130. E5106 is VD-domiciled via research record E5169.
**Q55.** 31: 6 under Cerid's E5005, 9 under Wonod (8 below E5106 plus E5130), 2 under E5091 and 14 under E5145.
**Q56.** BB-, held by E5144 (A5108).
**Q57.** E5002.
**Q58.** E5145. It guarantees I5007, issued by E5133 in the Vesol group.
**Q59.** 12, which is E5011–E5022.
**Q60.** Geren Group SA (E5145), and no, it is not in the same group as the issuer. I5007 is issued by E5133 (Vesol Foods).
**Q61.** 19.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1170","E1051","E1080","E1307","E1167","E1299","E1161","E1290","E1285","E1294","E1263","E1053","E1159","E1163","E1034","E5116","E5059","E1112","E1213","E1228","E1229","E1058","E1057","E1093","E1186","E1243","E1255","E1064","E1144","E5113","E5156","E5019","E1300","E1151","E5097"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 377},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1264","E1098","E1061","E1006","E1210","E1059","E1013","E1019","E1109","E1037","E1088","E1099","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1238","E1242","E1260","E1266","E1267","E1297","E1314","E1317","E1323","E1066","E1039"]},
"Q19": {"issuers": ["E01","E09","E1046","E1056","E1079","E1080","E1029","E1190","E1211","E1282","E1118","E1248","E1262","E1263","E1294","E1300","E1158","E1005","E1034","E1072","E1188","E1228","E1064","E1105","E1059","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5097"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 72},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5124","E15","E1039","E1194","E5116"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 497},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 79},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 113},
"Q49": {"parent": "E5001"},
"Q50": {"count": 6},
"Q51": {"count": 58},
"Q52": {"count": 19},
"Q53": {"same_group": "no"},
"Q54": {"entities": ["E5106","E5124","E5130"]},
"Q55": {"count": 31},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```