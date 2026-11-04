**Q1.** A-. E01 LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02). The 2026-02-10 action (A03) only changed the outlook to Negative.

**Q3.** No. The 2031 note (I02, subordinated) has been BB+ since 2025-06-20 (A07).

**Q4.** Positive. E02 (merged with E03) has been BBB-free at A/POS since 2025-09-15 (A09).

**Q5.** E02 (Northwind Holdings), the guarantor (I03), rated A. I03 itself is rated A (A11), and E02's LTIDR is A (A09).

**Q6.** The Valdoria country ceiling is BB (VD, from 2025-04-01). E05's FC rating is BB (A14), capped at that ceiling, while its LC rating is BBB- (A13).

**Q7.** 36 issuers had a lower rating letter in 2026, judged by comparing ratings rather than action codes, because some actions are mislabelled. For example, E1064's A- to BBB+ on 2026-02-02 is coded AF (A1141), while E5116's 2026-05-16 DG (A5088) kept A and only changed the outlook, so I excluded it. E5033's DG starts 2026-11-06, after the as-of date, so I excluded it too.

**Q8.** E08 is the only one. It has held RD since 2026-07-08 (A22).

**Q9.** 377. This counts entities with a non-withdrawn issuer rating in force on 2026-10-01, including E1279, which has only an LC rating (A1596) after its FC rating was withdrawn.

**Q10.** Depends. E05's FC rating is BB (non-investment grade, A14) but its LC rating is BBB- (investment grade, A13).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** Once. The only downgrade was A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). In between there was only a watch period (A35).

**Q17.** No. E06's 2026-09-03 action (A17) put it on Rating Watch Negative, with the rating still A-.

**Q18.** 32 issuers are on Rating Watch Negative, listed in the JSON below.

**Q19.** 47 issuers have a Negative outlook, listed in the JSON below. E5033's Negative outlook starts after the as-of date, so it is excluded.

**Q20.** No. E07 went from BB to WD (withdrawn) on 2026-05-12 (A19) and never defaulted.

**Q21.** 35 entities had a rating that was later withdrawn and not replaced, listed in the JSON below.

**Q22.** Only E08, which went to RD on 2026-07-08 (A22).

**Q23.** F2 (E01 STIDR, A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 72. This is the count of instrument ratings in force on 2026-10-01 at BBB- or above.

**Q26.** A+ (E15 LC, A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV FC, A38).

**Q29.** None. VD has no ratings.

**Q30.** 13 entities. CV's ceiling is A (E15, E1039, E1194, E5116 are at A) and VD's is BB (E05, E1028, E1101, E1126, E1236, E5012, E5047, E5091, E5124 are at BB).

**Q31.** No. No FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10 and the ultimate parent is E09.

**Q33.** E10 (Halden Bank), the guarantor (I05), rated BBB+. I05 is itself rated BBB+ (A29), and E10's LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent, while E10 belongs to the E09 group.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, with E03 merged in, and E04).

**Q37.** 497 distinct entities in entities.csv, with duplicates already merged.

**Q38.** No. E06 (DE) and E13 (US) are separate entities with different LEIs and no parent link.

**Q39.** A, with a Positive outlook (E02, A09).

**Q40.** 78 GB-domiciled entities have an issuer rating in force.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 is flagged local_currency = yes and denominated in XVD.

**Q45.** No. I07 is rated BBB- (A45), above the VD ceiling of BB. But the ceiling constrains foreign-currency ratings and I07 is a local-currency note, so it is not capped.

**Q46.** No. E11 has no rating rows, and its notes (I05) take the guarantor E10's credit risk.

**Q47.** None. I08 has no instrument rating, even though E15 itself is rated A.

**Q48.** 113 instruments have a rating in force.

**Q49.** E5001.

**Q50.** 6 levels (E5047 to E5001 at levels_up 6).

**Q51.** 58 (E5001 to E5058).

**Q52.** 19 (E5086 to E5104).

**Q53.** No. Belir Mining's top is E5059 and Rotam's is E5086.

**Q54.** E5106, E5124 and E5130.

**Q55.** 31. By group, this is 6 in Cerid, 2 in Rotam, 9 in Wonod (below E5106 and E5124) and 14 in Geren (below the VD-domiciled E5145).

**Q56.** BB-, held by E5144.

**Q57.** E5002. E5011's chain is E5005, E5002, E5001 and E5013's is E5006, E5002, E5001.

**Q58.** E5145. It guarantees I5007, issued by E5133, which sits in the Vesol group.

**Q59.** 12 (E5011 to E5022).

**Q60.** Credit risk is E5145 (Geren Group). That is not the same group as the issuer E5133, which is in Vesol under E5132.

**Q61.** 19 Cerid members hold an FC rating of BB+ or lower.

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
"Q40": {"count": 78},
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