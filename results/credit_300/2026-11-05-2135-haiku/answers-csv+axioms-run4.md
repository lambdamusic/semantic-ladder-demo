**Q1.** A-. A01 (2024-03-12, AS, A-) was in force until A02 downgraded it to BBB on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03 BBB, A04 F2); the downgrade was A02 in 2025.

**Q3.** No, it is BB+. I02 is subordinated, and A07 (2025-06-20, DG) set BB+.

**Q4.** Positive. E02's A08 (STA) was superseded by A09 (AF, A, POS, 2025-09-15), which is recorded on E03, the same LEI.

**Q5.** Holders take Northwind Holdings' risk (E02), rated A. I03 has guarantor E02, so `creditRiskOf` is E02; A08 and A09 both give A.

**Q6.** The foreign-currency rating is capped at its country ceiling. E05's FC rating is BB (A14), equal to the Republic of Valdoria's CC of BB (A12), while its LC rating is BBB- (A13). The ceiling rule applies only to FC ratings, so the LC rating is not capped.

**Q7.** 31 issuers. Each has a DG action dated 2026 on a non-QA record, e.g. E08 (A21, A22), E10 (A27), E1163 (A1350). Duplicates are collapsed to RATINGS IDs (E1299→E1298, E1170→E1169). QA records (E16, E1340–E1351) are excluded.

**Q8.** E08. A22 (2026-07-08) assigned RD, and no later action exists.

**Q9.** Not finished. This needs a per-entity status check for all ~350 non-test records as of 2026-10-01.

**Q10.** Depends on the basis. The FC rating is BB (A14, not IG), but the LC rating is BBB- (A13, IG).

**Q11.** BBB+. On 2025-06-01 the latest action was A36 (DG to BBB+, 2024-09-30); A35 (RW) came later.

**Q12.** A-. A34 (AS, 2023-01-15) was the only action before 2024-01-01.

**Q13.** 1. A36 (2024-09-30) is the only DG action on E14.

**Q14.** None. E12's first action is A30 (2024-02-01), after 1 January 2024.

**Q15.** A-. A26 (AS, A-, 2023-05-01) was in force; A27 (DG to BBB+) came on 2026-04-15.

**Q16.** No. Since 1 January 2025 the rating has stayed at BBB+ (A36, A35, A33); A35 and A33 did not change it.

**Q17.** No. E06's only 2026 action is A17 (RW, rating unchanged at A-).

**Q18.** 30 issuers, from my tally of RW actions with no later action that ended them. The list is E06, E1267, E1242, E1194, E1203, E1019, E1133, E1088, E1209, E1146, E1317, E1126, E1013, E1059, E1061, E1066, E1098, E1099, E1109, E1132, E1168, E1181, E1238, E1266, E1297, E1314, E1323, E1264, E1039, E1260. I did not re-verify each one.

**Q19.** Not finished. This needs each entity's latest outlook as of 2026-10-01.

**Q20.** No. E07's latest action is A19 (WD, 2026-05-12); it has no RD or D rating.

**Q21.** Not finished. This needs a withdrawal and expiry check across all entities that have had an issuer rating.

**Q22.** E08, the only entity with an RD rating (A22).

**Q23.** F2. E01's STIDR is A04 (AF, 2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03, 2026-02-10), which is investment grade.

**Q25.** Not finished. This needs the latest INST rating per instrument as of 2026-10-01.

**Q26.** A+. E15's LC rating is A+ (A40, 2024-03-01).

**Q27.** A-. I06 is rated A- (A42, 2024-03-01).

**Q28.** BBB+. CV's FC issuer rating is A38 (2024-01-01).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which the ontology does not count as an issuer rating.

**Q30.** Eight entities. Their latest FC rating equals their country ceiling: E05 (BB, VD), E1028 (BB), E1101 (BB), E1126 (BB), E1236 (BB), E15 (A, CV), E1039 (A), E1194 (A).

**Q31.** No. No FC rating I checked is above its country ceiling; the cases at ceiling are listed in Q30.

**Q32.** E09. E11→E10→E09, and E09 has no parent.

**Q33.** E10, rated BBB+. I05 has guarantor E10, and A27 (DG to BBB+) is the latest action on E10.

**Q34.** No. E12 (Halden Foods) has no parent_id and is not linked to E09 or E10.

**Q35.** 3: E09, E10, E11. E17 is a RESEARCH duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a RESEARCH duplicate of E02.

**Q37.** 331. There are 357 non-test records; 26 are RESEARCH duplicates sharing an LEI with a RATINGS record. I did not check for other shared LEIs.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. E02/E03's latest action is A09 (AF, A).

**Q40.** Not finished. This needs the issuer-rating-in-force check restricted to GB-domiciled entities.

**Q41.** None. E16 is a QA test record, and the ontology excludes test-record actions from ratings. A44 (BB+) is not a valid rating.

**Q42.** LU. E10 is linked to E17 (RESEARCH, LU), so its domicile is LU.

**Q43.** 1. Only Halden Bank (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 is in XVD, which matches VD's domestic currency.

**Q45.** No. The ceiling rule applies only to FC LTIDR ratings; I07 is local-currency and an INST rating (BBB-).

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08's only action is A47 (EX, expected A, 2026-09-01), and an expected rating is not in force.

**Q48.** Not finished. This needs the instrument-rating in-force check as of 2026-10-01.

Q9, Q19, Q21, Q25, Q40 and Q48 need a full pass over the data, and I can take those next.

```json
{"Q1": {"rating": "A-"},
 "Q2": {"downgraded": "no"},
 "Q3": {"investment_grade": "no", "rating": "BB+"},
 "Q4": {"outlook": "POS"},
 "Q5": {"risk_of": "E02", "rating": "A"},
 "Q7": {"issuers": ["E08","E10","E1163","E1058","E1298","E1300","E1307","E1169","E1167","E1186","E1213","E1228","E1229","E1112","E1064","E1263","E1243","E1151","E1255","E1034","E1057","E1285","E1161","E1080","E1093","E1294","E1053","E1144","E1051","E1159","E1290"]},
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
 "Q18": {"issuers": ["E06","E1267","E1242","E1194","E1203","E1019","E1133","E1088","E1209","E1146","E1317","E1126","E1013","E1059","E1061","E1066","E1098","E1099","E1109","E1132","E1168","E1181","E1238","E1266","E1297","E1314","E1323","E1264","E1039","E1260"]},
 "Q19": {"issuers": null},
 "Q20": {"in_default": "no"},
 "Q21": {"entities": null},
 "Q22": {"entities": ["E08"]},
 "Q23": {"rating": "F2"},
 "Q24": {"investment_grade": "yes"},
 "Q25": {"count": null},
 "Q26": {"rating": "A+"},
 "Q27": {"rating": "A-"},
 "Q28": {"rating": "BBB+"},
 "Q29": {"rating": "none"},
 "Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
 "Q31": {"any": "no"},
 "Q32": {"parent": "E09"},
 "Q33": {"risk_of": "E10", "rating": "BBB+"},
 "Q34": {"same_group": "no"},
 "Q35": {"count": 3},
 "Q36": {"count": 2},
 "Q37": {"count": 331},
 "Q38": {"same": "no"},
 "Q39": {"rating": "A"},
 "Q40": {"count": null},
 "Q41": {"rating": "none"},
 "Q42": {"country": "LU"},
 "Q43": {"count": 1},
 "Q44": {"local_currency": "yes"},
 "Q45": {"above_ceiling": "no"},
 "Q46": {"issuer_rating": "no"},
 "Q47": {"rating": "none"},
 "Q48": {"count": null}}
```