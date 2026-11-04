**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01) and not downgraded to BBB until 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with a Negative outlook (A03).

**Q3.** No, it is rated BB+. The 2031 note is I02 (subordinated), downgraded to BB+ on 2025-06-20 (A07, superseding A23's BBB).

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its latest action A09 (2025-09-15) is A with a POS outlook, which supersedes A08's STA.

**Q5.** Guarantor E02 (Northwind Holdings), rated A. I03 is issued by E04 and guaranteed by E02, so the holder takes E02's risk (A08, A09).

**Q6.** The data indicates a country-ceiling effect. E05's foreign-currency rating is BB, equal to Valdoria's Country Ceiling of BB (A12), while its local-currency rating is BBB- (A13, A14). The data gives no explicit reason.

**Q7.** Thirty-seven issuers were downgraded in 2026 (list in JSON).
- I excluded E1341 (A1720, dated 2026-11-09) because it is after today's date.
- I excluded QA-source records (E16, E1340–E1351, E5170) as test data.
- I mapped RESEARCH duplicates to their RATINGS record.

**Q8.** E08. It was downgraded to RD on 2026-07-08 after a distressed debt exchange (A22) and has no later action.

**Q9.** 377 distinct issuers.
- I counted entities with an LTIDR (long-term issuer default rating) that was not withdrawn by 2026-10-01.
- I merged duplicates and excluded QA records.
- I treated the sovereign VD as unrated, since it has only a country ceiling.

**Q10.** Depends. Its foreign-currency rating is BB, which is sub-investment grade, but its local-currency rating is BBB-, which is investment grade (A13, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and was later put on watch and affirmed at BBB+ (A35, A33).

**Q12.** A-, assigned 2023-01-15 (A34).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was rated A- from 2023 (A26) until its downgrade to BBB+ on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+; only a watch and an affirmation have occurred since (A35, A33).

**Q17.** No. E06 only went on Rating Watch Negative at A- (A17).

**Q18.** Thirty-two issuers (list in JSON). Each has a Rating Watch Negative action that no later action cleared as of 2026-10-01.

**Q19.** Forty-five issuers (list in JSON). Their latest action as of 2026-10-01 carries a Negative outlook. Watch actions carry no outlook, so I treated them as superseding any earlier outlook.

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19) and it was never rated in default.

**Q21.** Thirty-five entities (list in JSON). Each had an LTIDR that was withdrawn on or before 2026-10-01.

**Q22.** E08 only (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 74. I counted the 116 instruments still rated on 2026-10-01 whose latest rating is BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (A42, instrument I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12) and no issuer rating.

**Q30.** Thirteen entities (list in JSON).
- VD's ceiling is BB; E05, E1028, E1101, E1126, E1236, E5012, E5047, E5091 and E5124 are rated BB.
- CV's ceiling is A; E15, E1039, E1194 and E5116 are rated A.

**Q31.** No. No VD entity is rated above BB and no CV entity above A.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Guarantor E10 (Halden Bank), rated BBB+ after the 2026-04-15 downgrade (I05, A27).

**Q34.** No. E12 has no parent link, while Halden Bank sits under E09. The shared name is not evidence of common ownership.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 497. The file has 540 rows, of which 29 are duplicate records (same LEI) and 14 are QA-source records that I excluded.

**Q38.** No. They have different LEIs, countries (DE and US) and names.

**Q39.** A (A08, A09).

**Q40.** 79. These are the distinct GB-domiciled entities holding an issuer rating on 2026-10-01.

**Q41.** None. E16 exists only as a QA-source record (A43 and A44 give BBB- and then BB+), which I treated as test data. If QA data is meant to count, the rating is BB+.

**Q42.** DE. E10 is DE; the LU record E17 is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, is a duplicate of the German E10.

**Q44.** Yes. I07 is denominated in XVD and issued by a Valdoria entity. I am inferring XVD as Valdoria's local currency, since the data does not define it.

**Q45.** No. I07 is rated BBB- (A45) against a BB ceiling, but a Country Ceiling constrains foreign-currency obligations, not local-currency ones.

**Q46.** No. E11 has only a CO rating (A46) and no LTIDR.

**Q47.** None. The rating on I08 ended with an EX action on 2026-09-01 (A47, last rating A).

**Q48.** 116. Of the 122 instruments, six had ended before 2026-10-01: I08, I1008, I1012, I1021, I1046 and I1049. I counted I1001, I1007 and I1015 as rated because their EX actions fall after 2026-10-01.

**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 (= E5005) → E5002 → E5001.

**Q50.** 6 levels.

**Q51.** 58, covering E5001–E5058. E5167 is a duplicate of E5005, and I excluded the QA record E5170.

**Q52.** 19, covering E5086–E5104.

**Q53.** No. The RATINGS record E5062 sits under Belir (E5060 → E5059). The RESEARCH record E5168 claims parent E5086, but it conflicts with the RATINGS record, so I did not rely on it.

**Q54.** E5124 and E5130.

**Q55.** 24 entities.
- Cerid: E5012, E5023, E5024, E5036, E5047, E5048.
- Rotam: E5101, E5102.
- Wonod: E5130, E5131.
- Geren: 14 rated entities below E5145.

**Q56.** BB-, held by E5144 (A5108).

**Q57.** E5002. E5011's parent E5167 is the RESEARCH duplicate of E5005, which sits under E5002, and E5013 sits under E5006, also under E5002.

**Q58.** E5145. It guarantees I5007, issued by E5133 in the Vesol group. Every other guarantee is within its own group.

**Q59.** 12 entities, E5011–E5022, with E5011 reached through the E5167 = E5005 link.

**Q60.** Guarantor E5145 (Geren Group SA), which is not in the same group as the issuer E5133 (Vesol Foods).

**Q61.** 19. These are Cerid members whose current foreign-currency rating is below BBB-.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E10","E08","E1169","E1051","E1080","E1167","E1307","E1298","E5116","E5059","E5156","E1160","E1034","E1163","E5019","E1290","E1294","E1285","E1263","E1213","E1255","E1112","E1064","E1053","E1058","E1057","E1093","E5113","E1300","E1228","E1186","E1159","E1144","E1243","E1151","E1229","E5097"]},
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
"Q18": {"issuers": ["E06","E1264","E1098","E1061","E1209","E1181","E1059","E1168","E1037","E1006","E1019","E1109","E1132","E1133","E1146","E1088","E1099","E1066","E1126","E1203","E1194","E1238","E1242","E1260","E1266","E1267","E1297","E1314","E1317","E1323","E1013","E1039"]},
"Q19": {"issuers": ["E01","E09","E1056","E1079","E1046","E1029","E1080","E1190","E1118","E1072","E1282","E1248","E1263","E1271","E1228","E1211","E1034","E1005","E1064","E1158","E1188","E1261","E1294","E1300","E1055","E1059","E5019","E5050","E5020","E5013","E5023","E5039","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 74},
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
"Q48": {"count": 116},
"Q49": {"parent": "E5001"},
"Q50": {"count": 6},
"Q51": {"count": 58},
"Q52": {"count": 19},
"Q53": {"same_group": "no"},
"Q54": {"entities": ["E5124","E5130"]},
"Q55": {"count": 24},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```