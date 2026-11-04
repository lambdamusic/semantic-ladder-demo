**Q1.** A-. A01 (2024-03-12) set E01 at A-, and the downgrade A02 only came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB.

**Q3.** No, BB+. The 2031 note is I02 (subordinated), and A07 (2025-06-20) downgraded it from BBB (A23) to BB+.

**Q4.** POS. E03 is a RESEARCH duplicate of E02 (same LEI), and its latest action A09 (2025-09-15) affirms A with a Positive outlook.

**Q5.** The holder takes the risk of E02, the guarantor of I03 (issuer E04), which is rated A (A08, A09).

**Q6.** The country ceiling for Valdoria is BB (A12), which caps foreign-currency ratings (E05 FC BB, A14). The local-currency rating is BBB- (A13).

**Q7.** The issuers with a downgrade dated 2026 are in the JSON. I mapped RESEARCH duplicates to their RATINGS record and excluded QA-source records. I also excluded A5028 (E5033), which is dated 2026-11-06, after today.

**Q8.** E08. A22 (2026-07-08) moved it to RD after a distressed debt exchange.

**Q9.** 377, from my manual tally, so treat it as approximate. This counts canonical, non-QA issuers whose latest LTIDR action on or before 2026-10-01 is not a withdrawal. E1115, E1158 and E1303 count as rated because later actions follow their WD. E1279 counts because its LC rating was not withdrawn.

**Q10.** Depends. E05 is BBB- in local currency (A13, investment grade) and BB in foreign currency (A14, not investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-. A34 assigned it on 2023-01-15, before the A36 downgrade.

**Q13.** 1, the downgrade A36.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10's rating was A- from A26 until A27 downgraded it on 2026-04-15. E17 is a RESEARCH duplicate with no actions.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). The RWN in A35 is a watch, not a rating change.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-.

**Q18.** The issuers whose latest action leaves them on RWN on 2026-10-01 are in the JSON. E1019 and E1059 are included on the basis of an LC-basis watch only.

**Q19.** The issuers whose latest outlook-bearing action is Negative are in the JSON. Entities whose latest action is an RW row (blank outlook) are excluded.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** The 35 entities that had an issuer rating but whose last action is a withdrawal are in the JSON. They are E07 and 34 others, using the canonical record IDs.

**Q22.** E08 only (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's BBB (A03) is investment grade.

**Q25.** 72. This counts instruments whose latest INST rating on 2026-10-01 is BBB- or higher, excluding EX actions. I could not tell from the data what EX means, so I treated it as "no held rating".

**Q26.** A+ (A40, LC).

**Q27.** A- (A42). The 2032 note is I06.

**Q28.** BBB+ (A38, FC LTIDR).

**Q29.** None. VD only has a Country Ceiling (A12, BB) and no issuer rating.

**Q30.** The entities whose FC rating equals their country ceiling (BB for VD, A for CV) are in the JSON.

**Q31.** No. No VD entity is above BB and no CV entity is above A in FC.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05, which is rated BBB+ after A27.

**Q34.** No. E12 has no parent link, and the shared "Halden" name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 497. That is 540 rows, less 29 duplicate LEIs, less 14 QA records (E16, E1340–E1351, E5170). Excluding QA is my assumption.

**Q38.** No. E06 and E13 have different LEIs and countries (DE and US).

**Q39.** A, affirmed via A09 (E03 is a duplicate of E02).

**Q40.** 79, from my manual tally, so treat it as approximate.

**Q41.** None. E16 comes only from the QA source system, which I treated as non-production. Its recorded actions would give BB+ (A44).

**Q42.** DE. E10 is the RATINGS record. E17 (LU) is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, duplicates E10, which is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, which I infer to be Valdoria's currency. The data does not define XVD.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency BBB- (A45).

**Q46.** No. E11 only has a CO rating (A46), not an LTIDR.

**Q47.** None. I08's only action is A47, an EX on 2026-09-01.

**Q48.** 113, which is the 122 instruments less the 9 whose only action is EX.

**Q49.** E5001. The chain is E5047→E5035→E5023→E5011→E5167 (a duplicate of E5005)→E5002→E5001.

**Q50.** 6 levels.

**Q51.** 58, the entities E5001 to E5058, with the QA record E5170 excluded.

**Q52.** 19, the entities E5086 to E5104. I excluded the RESEARCH duplicate E5168.

**Q53.** No. E5062 sits under E5059 (Belir). Only the RESEARCH duplicate E5168 points to E5086.

**Q54.** E5124 and E5130. E5169 is a duplicate and is excluded.

**Q55.** 23 rated entities have a VD-domiciled ancestor. That is 14 under E5145, 6 under the Cerid VD chain, 2 under E5091 and 1 under E5124.

**Q56.** BB-. E5144 is the lowest in the Vesol group.

**Q57.** E5002. Both chains run through E5002 to E5001, and E5011 reaches it via the duplicate E5167 of E5005.

**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the Vesol group. All other guarantees are within-group.

**Q59.** 12: E5011 to E5022.

**Q60.** The holder takes the risk of E5145 (Geren Group SA), and it is not in the same group as the issuer E5133 (Vesol).

**Q61.** 19 Cerid members hold a sub-investment-grade FC issuer rating.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1051","E1080","E1307","E1167","E1169","E5019","E5116","E5113","E1160","E1298","E1294","E1290","E1285","E1263","E1159","E1163","E1186","E1213","E1228","E1229","E1243","E1255","E1300","E1112","E1064","E1053","E1057","E1058","E1034","E1093","E1144","E1151","E5156","E5059"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1132","E1146","E1168","E1181","E1194","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E1203","E1133","E1126"]},
"Q19": {"issuers": ["E01","E09","E1080","E1056","E1005","E1079","E1190","E1046","E1029","E1072","E1118","E1034","E1300","E1282","E1263","E1271","E1261","E1294","E1158","E1160","E1059","E1064","E1105","E1228","E1211","E1055","E5039","E5050","E5013","E5020","E5023","E5019","E5057","E5059","E5062","E5073","E5099","E5102","E5113","E5116","E5097","E5119","E5131","E5141","E5156"]},
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
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124","E15","E1039","E1194","E5116"]},
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