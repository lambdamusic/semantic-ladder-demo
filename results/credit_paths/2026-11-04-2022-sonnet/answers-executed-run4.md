**Q1.** A-. E01's LTIDR (FC) was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. In 2026 E01 had only an outlook change to Negative at BBB, an affirmation (A03). Its downgrade to BBB was in 2025 (A02).

**Q3.** No, BB+. The 2031 note is I02 (subordinated), rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's current LTIDR is A with a POS outlook (A09).

**Q5.** The credit risk of E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and credit_risk_of is E02; I03 is rated A (A11) and E02 is also A (A09).

**Q6.** The data does not state a reason. E05 has FC BB and LC BBB- (A14, A13), and the VD country ceiling is BB (ceilings.csv). That is consistent with a ceiling cap on the foreign-currency rating, but the cap is my inference.

**Q7.** 36 issuers had an issuer-rating decrease in 2026, listed in the JSON. I judged by actual rating-level falls rather than the action label. For example, E1064's A- to BBB+ fall (A1141) is labelled AF, and outlook-only DG rows such as E5116 are excluded. E5033's DG dated 2026-11-06 is after 1 Oct 2026 and is excluded.

**Q8.** E08. Its rating is RD from 2026-07-08 (A22).

**Q9.** 377. This counts entities with a non-withdrawn LTIDR (FC or LC) in force on 2026-10-01, including sovereign CV and the RD entity E08. It is a long manual tally.

**Q10.** Depends. E05 is BB in foreign currency (not investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+. E14 was BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 was A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36). The later rows are a watch and an affirmation.

**Q14.** None. E12's first rating starts 2024-02-01 (A30).

**Q15.** A-. E10 was A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), with only a watch in between.

**Q17.** No. E06 stayed A- and was only placed on RWN on 2026-09-03 (A17).

**Q18.** 32 entities, listed in the JSON, with watch RWN in force on 2026-10-01. E1019 and E1059 are on watch only on their LC ratings.

**Q19.** 46 issuers with outlook NEG in force on 2026-10-01, listed in the JSON. E5033's NEG row starts 2026-11-06, so it is excluded.

**Q20.** No. E07's rating was withdrawn (WD, A19), not defaulted.

**Q21.** 35 entities whose current issuer rating is WD, listed in the JSON, with no other basis still in force.

**Q22.** E08 only. It has the only RD rating (A22).

**Q23.** F2. E01's STIDR is F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 72 instruments rated BBB- or above on 2026-10-01 (current instrument rows).

**Q26.** A+. E15's LTIDR (LC) is A+ (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating rows.

**Q30.** 13 entities with a current FC rating equal to their country's ceiling (CV: A, VD: BB), listed in the JSON.

**Q31.** No. No CV entity has an FC rating above A, and no VD entity has one above BB.

**Q32.** E09 (entities.csv, ancestors.csv).

**Q33.** The credit risk of E10 (Halden Bank), the guarantor of I05, rated BBB+ (A29, A27).

**Q34.** No. E12 has no parent, while E10 belongs to the E09 group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is merged into E02.

**Q37.** 497 entity rows in entities.csv, after merging and including the two sovereigns.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) are separate entities with different LEIs.

**Q39.** A (A09).

**Q40.** 79. These are GB-domiciled entities with a non-withdrawn LTIDR in force on 2026-10-01.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU. E10's country is LU, even though its parent E09 is GB.

**Q43.** 1: E10.

**Q44.** Yes. I07 has local_currency = yes, in XVD.

**Q45.** No. I07 is BBB- (A45), but the VD ceiling of BB limits foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 has no rating rows; I05 takes E10's risk.

**Q47.** None. I08 has no rating row.

**Q48.** 113 instruments with a rating in force on 2026-10-01 (72 investment grade, 41 below).

**Q49.** E5001 (entities.csv).

**Q50.** 6 levels (E5047 to E5001 in ancestors.csv).

**Q51.** 58: E5001 to E5058, with E5167 merged into E5005.

**Q52.** 19: E5086 to E5104.

**Q53.** No. E5062 sits in the E5059 group and Rotam Group Inc is E5086, a separate group.

**Q54.** E5106, E5124 and E5130, all VD.

**Q55.** 31 rated entities have a VD-domiciled entity above them: Cerid 6, Rotam 2, Wonod 9, Geren 14.

**Q56.** BB-, held by E5144 (A5108).

**Q57.** E5002. E5011's ancestors are E5005, E5002, E5001 and E5013's are E5006, E5002, E5001.

**Q58.** E5145. It guarantees I5007, issued by E5133, which is in the E5132 group. All other guarantors back issuers in their own group.

**Q59.** 12: E5011 to E5022 have E5001 at levels_up 3.

**Q60.** The credit risk of E5145. The issuer E5133 is in the E5132 group, so they are not in the same group.

**Q61.** 19 Cerid members have a current FC rating of BB+ or lower, listed by ID in the reasoning below. They are E5007, E5010, E5012, E5013, E5016, E5021, E5022, E5023, E5024, E5025, E5028, E5029, E5030, E5037, E5039, E5041, E5042, E5047 and E5048. E5001 has no rating.

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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
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
"Q30": {"entities": ["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236","E5012","E5047","E5091","E5116","E5124"]},
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