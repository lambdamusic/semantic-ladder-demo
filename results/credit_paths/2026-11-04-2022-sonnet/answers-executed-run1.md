**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. In 2026 E01 only had an outlook change to Negative at BBB (A03) and a new STIDR of F2 (A04); the downgrade to BBB was in 2025 (A02).

**Q3.** No, it is BB+. The 2031 note is I02, a subordinated note rated BB+ since 2025-06-20 (A07).

**Q4.** Positive. E02's open LTIDR is A with a POS outlook (A09).

**Q5.** E02 (Northwind Holdings plc), rated A. I03 is guaranteed by E02, so credit_risk_of is E02; both I03 and E02 are rated A.

**Q6.** Valdoria's country ceiling is BB (ceilings.csv, from 2025-04-01). That caps E05's foreign-currency rating at BB (A14), while its local-currency rating is BBB- (A13).

**Q7.** 36 issuers had a real rating-level downgrade in 2026 (listed in the JSON). I judged this by the rating falling, not by the action label. E5116's DG (A5088) is an outlook-only change, so I excluded it. E5033's drop starts 2026-11-06, after the data date.

**Q8.** E08 only. It holds RD since 2026-07-08 (A22).

**Q9.** 377. This counts entities with a non-withdrawn LTIDR or STIDR open on 1 October 2026. E1279 and E1106 count because they still hold an open FC or LC rating.

**Q10.** Depends. E05's foreign-currency rating is BB (non-IG, A14) and its local-currency rating is BBB- (IG, A13).

**Q11.** BBB+. E14's LTIDR was BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14's A- ran from 2023-01-15 to 2024-09-30 (A34).

**Q13.** Once. The only rating-level fall is A- to BBB+ on 2024-09-30 (A36); the later records are RWN and AF.

**Q14.** None. E12's first rating starts 2024-02-01 (A30).

**Q15.** A-. E10 was A- until 2026-04-15 (A26); E10 also covers merged record E17.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now, with a watch period in between (A35, A33).

**Q17.** No. E06 stayed at A- and was only placed on Rating Watch Negative on 2026-09-03 (A17).

**Q18.** 31 issuers (listed in the JSON), found from open rows carrying watch RWN.

**Q19.** 47 issuers (listed in the JSON). E5033 is excluded because its NEG outlook starts 2026-11-06, after the data date.

**Q20.** No. E07's rating was withdrawn (WD, A19), not a default.

**Q21.** 35 entities, all with an open WD record and no other open issuer rating (listed in the JSON).

**Q22.** Only E08, which reached RD in 2026 (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade, though the outlook is Negative.

**Q25.** 72 instruments held an investment-grade rating (BBB- or better) on 1 October 2026.

**Q26.** A+ (A40).

**Q27.** A-. I06 carries an instrument rating of A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** 13 entities (listed in the JSON). CV's ceiling is A and VD's is BB, and each of these has an open foreign-currency rating exactly at its country's ceiling.

**Q31.** No. No CV entity has an FC rating above A and no VD entity has one above BB; E1039's AA- is a local-currency rating.

**Q32.** E09 (entities.csv).

**Q33.** E10 (Halden Bank AG), rated BBB+. I05 is guaranteed by E10 (credit_risk_of), and both I05 and E10 are BBB+ (A29, A27).

**Q34.** No. E12 has no parent, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04 (E03 is merged into E02).

**Q37.** 497. Entities.csv has 497 rows after the merges, counting 16 + 315 + 166 across the E0x, E1xxx and E5xxx series.

**Q38.** No. E06 (DE) and E13 (US) are separate entities with different LEIs.

**Q39.** A, with a Positive outlook (A09).

**Q40.** 79. This counts GB-domiciled entities with an open, non-withdrawn issuer rating.

**Q41.** None. No Brindle Capital appears in the data.

**Q42.** LU (E10).

**Q43.** 1: E10 only.

**Q44.** Yes. I07 is in XVD with local_currency = yes.

**Q45.** No. I07's BBB- exceeds Valdoria's BB ceiling, but that ceiling applies to foreign-currency obligations and I07 is local-currency.

**Q46.** No. E11 has no ratings; I05 is rated through guarantor E10.

**Q47.** None. I08 has no rating record.

**Q48.** 113 instruments held a rating on 1 October 2026: the 72 investment-grade ones plus 41 non-investment-grade.

**Q49.** E5001.

**Q50.** 6 levels (ancestors.csv: E5047 to E5001).

**Q51.** 58 (E5001 to E5058).

**Q52.** 19 (E5086 to E5104).

**Q53.** No. E5062's top is E5059, while Rotam's top is E5086.

**Q54.** E5106, E5124 and E5130.

**Q55.** 32 rated entities, found via the ancestors table with VD-domiciled entities above them. By group: Cerid 6 (below E5005), Rotam 2 (below E5091), Wonod 10 (9 below E5106 plus E5130 below E5124), Geren 14 (below E5145).

**Q56.** BB-. E5144 is the lowest current FC rating in the Vesol group (A5108).

**Q57.** E5002. It is the nearest common ancestor of E5011 and E5013 in ancestors.csv.

**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the Vesol group.

**Q59.** 12 (E5011 to E5022 at levels_up 3 to E5001).

**Q60.** Credit risk is E5145 (Geren Group SA). Same group as the issuer: no, because the issuer E5133 is in the Vesol group.

**Q61.** 19 Cerid members have a sub-investment-grade FC issuer rating (BB+ or lower), e.g. E5007 B and E5029 BB+.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E5019","E5059","E5097","E5113","E5156"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 72},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E15","E1039","E1194","E5116","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},
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
"Q55": {"count": 32},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```