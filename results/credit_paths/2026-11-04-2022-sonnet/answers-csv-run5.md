**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02) is dated 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with a Negative outlook. The downgrade was A02 in 2025.
**Q3.** No, it is BB+. The 2031 note is I02, and A07 downgraded it to BB+, superseding A23 (BBB).
**Q4.** POS. E03 is a RESEARCH duplicate of E02 (same LEI), and A09 (2025-09-15) is the latest action, affirming A with a Positive outlook.
**Q5.** The guarantor E02, rated A. I03 is issued by E04 and guaranteed by E02 (A08, A09).
**Q6.** Not in the JSON. The foreign-currency rating is BB (A14) and the local-currency rating is BBB- (A13). The BB matches Valdoria's country ceiling (VD, A12).
**Q7.** 37 issuers had a 2026 downgrade (list in JSON). I excluded QA-source test records (E16, E1340–E1351) and the future-dated A1720/A5028, and mapped RESEARCH duplicates to their RATINGS record. This is a scan, not a verified run.
**Q8.** E08. A22 (2026-07-08) downgraded it to RD after a distressed debt exchange, with no later action.
**Q9.** I can't give a reliable count. It needs a per-entity latest-status pass over several hundred entities that I did not complete, so the JSON has null.
**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), while the foreign-currency rating is BB (not investment grade, A14).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action is dated 2025-11-20.
**Q12.** A-, from A34 (2023-01-15).
**Q13.** One, A36.
**Q14.** None. The first rating action for E12 is A30, dated 2024-02-01.
**Q15.** A-. A26 assigned it in 2023, and the downgrade A27 only came on 2026-04-15. E17 is a duplicate with no ratings.
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; A35 is only a watch and A33 is an affirmation.
**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative placement at A-, not a downgrade. Orrin Bancorp (E13) is a different entity.
**Q18.** 32 issuers, listed in the JSON (E06 via A17, plus others whose latest action is a watch placement). For E1019 and E1059 only the local-currency rating is on watch (A1041/A1042 and A1132). This is a scan, not a verified run.
**Q19.** 56 issuers, listed in the JSON (E01 via A03, E09 via A25, plus others whose latest action carries a Negative outlook). QA test records are excluded. This is a scan, not a verified run.
**Q20.** No. A19 withdrew E07's rating for commercial reasons; that is not a default.
**Q21.** 36 entities, listed in the JSON (E07 via A19, plus others whose last issuer-rating action is a withdrawal). E1106 and E1279 are excluded because a rating on the other currency basis remains.
**Q22.** E08 only, via RD in A22.
**Q23.** F2, from A04 (STIDR).
**Q24.** Yes. The issuer rating is BBB (A02, A03).
**Q25.** 72, as a rough scan. This counts instruments whose latest rating is BBB- or higher. Instruments with only an EX record (such as I08) are treated as not currently rated, but the data does not define EX.
**Q26.** A+ (A40).
**Q27.** A-. The 2032 note is I06 (A42).
**Q28.** BBB+ (A38). The A in A37 is the country ceiling, not an issuer rating.
**Q29.** None. VD has only a country-ceiling record (A12, BB) and no issuer rating.
**Q30.** 13 entities have a foreign-currency rating exactly at the ceiling, listed in the JSON. The ceiling is BB for VD (A12) and A for CV (A37).
**Q31.** No. No foreign-currency rating exceeds its ceiling; only local-currency ratings do, for example E15 at A+ (A40).
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The guarantor E10, rated BBB+. I05 is guaranteed by E10, and A27 downgraded it to BBB+.
**Q34.** No. E12 has no parent and is not linked to E09 in the data; the shared name proves nothing.
**Q35.** 3: E09, E10, E11. E17 is a duplicate of E10.
**Q36.** 2: E02 and E04. E03 is a duplicate of E02.
**Q37.** 497. There are 540 rows, minus 29 RESEARCH duplicates sharing an LEI, minus 14 QA rows (E16, E1340–E1351, E5170). Including QA rows gives 511.
**Q38.** No. E06 and E13 have different LEIs and countries.
**Q39.** A (A08, A09).
**Q40.** I can't give a reliable count. It needs the same per-entity pass as Q9, so the JSON has null.
**Q41.** None. E16 is a QA-source record, which I treat as test data, so I don't report a current rating. For reference, its ratings are A43 (BBB-) and then A44 (BB+, 2026-06-01).
**Q42.** DE. E10 says DE; the E17 duplicate says LU, so the records conflict.
**Q43.** 0. Only the duplicate E17 says LU, and its original E10 is DE.
**Q44.** Yes, inferred. I07's currency XVD appears to be Valdoria's currency, but the data does not define it.
**Q45.** No. The ceiling constrains foreign-currency ratings, and I07 (BBB-, A45) is a local-currency note.
**Q46.** No. E11 has only a CO-type record (A46) and no issuer rating.
**Q47.** None. I08 has only an EX record (A47, 2026-09-01) and no assignment; the data doesn't define EX, so I read it as a rating that has ended.
**Q48.** 113, as a rough scan. These are the instruments with an assignment and no later EX; the 9 instruments with only an EX record are excluded.
**Q49.** E5001. The chain is E5047, E5035, E5023, E5011, then E5167, the RESEARCH duplicate of E5005, then E5002, then E5001.
**Q50.** 6 levels, counted along that chain.
**Q51.** 58 (E5001–E5058). I excluded the QA test record E5170 (parent E5001).
**Q52.** 19 (E5086–E5104).
**Q53.** No. E5062's parents run to E5059. E5168 is a RESEARCH duplicate of E5062 that wrongly points to E5086.
**Q54.** E5124 and E5130.
**Q55.** 23, as a rough scan. These are rated entities below a VD-domiciled ancestor, in the Cerid, Wonod, Rotam and Geren groups.
**Q56.** BB-. The lowest is E5144 (A5108); the other Vesol members are rated BB or higher.
**Q57.** E5002. E5011 reaches it via E5167 (the E5005 duplicate), and E5013 reaches it via E5006.
**Q58.** E5145. It guarantees I5007, issued by E5133, which belongs to the Vesol group; every other guarantor is within its issuer's group.
**Q59.** 12. The level-3 entities are E5011 and E5012–E5022, with E5011 counted via the E5005 duplicate.
**Q60.** The guarantor E5145 (I5007), and no, it is not in the same group as the issuer E5133, which sits under E5132.
**Q61.** 19 Cerid members have a latest foreign-currency rating below BBB-.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1169","E1051","E1080","E1307","E1167","E1229","E5156","E5116","E5059","E1285","E1298","E1160","E1263","E1186","E1064","E1053","E1058","E5097","E1093","E1294","E1290","E1112","E1159","E1163","E1213","E1255","E1300","E5113","E5019","E1228","E1243","E1144","E1151","E1057","E1034"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": null},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1264","E1098","E1061","E1181","E1209","E1019","E1109","E1037","E1242","E1006","E1267","E1013","E1132","E1133","E1146","E1088","E1099","E1059","E1066","E1168","E1194","E1203","E1238","E1260","E1266","E1297","E1314","E1317","E1323","E1039","E1126"]},
"Q19": {"issuers": ["E01","E09","E1056","E1046","E1190","E5039","E5050","E5059","E5062","E5013","E5019","E5020","E5023","E5057","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5156","E5141","E1282","E1080","E1079","E1072","E1211","E1248","E1263","E1261","E1300","E1034","E1228","E1118","E1147","E1160","E1005","E1029","E1064","E1188","E1271","E1294","E1105"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1115","E1121","E1124","E1138","E1140","E1155","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320","E1159"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 72},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5124","E5091","E15","E1039","E1194","E5116"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 497},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": null},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
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
"Q54": {"entities": ["E5124","E5130"]},
"Q55": {"count": 23},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```