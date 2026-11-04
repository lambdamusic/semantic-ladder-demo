**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) and was cut to BBB only in A02 (2025-06-20).

**Q2.** No. E01's downgrade was A02 in 2025; the 2026 action A03 is an affirmation at BBB with a Negative outlook.

**Q3.** No, BB+. The 2031 note is I02 (subordinated). A07 downgraded it to BB+ on 2025-06-20, replacing A23 (BBB).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed A with a Positive outlook after A08 (Stable).

**Q5.** E02, rated A. I03 is issued by E04 and guaranteed by E02, and the guarantor's risk is what the holder takes. A09 affirmed E02/E03 at A.

**Q6.** The data doesn't state a reason. It is consistent with the Country Ceiling: VD's ceiling is BB (A12), which matches E05's FC BB (A14), while LC is BBB- (A13).

**Q7.** 38 entities have a 2026 downgrade, listed in the JSON. Test records are excluded, and research duplicates are reported under their RATINGS record. E1159, E1057 and E5033 are in the list although they were later withdrawn or are dated after 1 Oct. For example A1366 on E1170 is reported as E1169.

**Q8.** E08. A22 (2026-07-08) took it to RD, and it is the only RD/D rating in the data.

**Q9.** 377. This counts distinct issuers (by LEI) with a rating in force on 2026-10-01, excluding QA records and 35 withdrawn issuers. It is a hand count over a very large file, so treat it as approximate.

**Q10.** Depends. FC is BB (A14, non-investment grade) and LC is BBB- (A13, investment grade).

**Q11.** BBB+. A36 downgraded E14 from A- (A34) on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade; A33, dated 2026, is an affirmation.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 assigned it in 2023 and A27 did not downgrade it until 2026-04-15. E17 is the same entity as E10.

**Q16.** No. E14 was BBB+ (A36) on 2025-01-01 and is still BBB+ (A33). The 2025 watch (A35) didn't change the rating.

**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative placement at A-, not a downgrade.

**Q18.** 31 entities, listed in the JSON. Each has an RWN action as its latest in force on 2026-10-01 (for example A17 on E06). E1209 is reported for the research record E1210.

**Q19.** 45 entities, listed in the JSON. Each has a Negative outlook on its latest in-force action, for example A03 on E01 and A25 on E09. This list is hand-compiled and may miss an entity.

**Q20.** No. A19 withdrew E07's rating for commercial reasons; it never moved to RD or D.

**Q21.** 35 entities, listed in the JSON. Each had an issuer rating that was withdrawn with no later action, for example A19 on E07 and A1002 on E1002 (reported as E1001). A few WD records are followed by later actions (E1115, E1158, E1303), so those entities are still rated.

**Q22.** E08, via A22 (RD).

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 72 instruments hold an investment-grade rating. This counts the latest INST action per instrument and excludes the nine instruments that only have an Expected rating (EX), such as I08.

**Q26.** A+, from A40 (LC).

**Q27.** A-, from A42 on I06.

**Q28.** BBB+, from A38 (CV, LTIDR FC).

**Q29.** None. VD has only a Country Ceiling (A12, BB) and no LTIDR.

**Q30.** 13 entities, listed in the JSON. They are rated at the BB ceiling for VD (A12) or the A ceiling for CV (A37), for example E05 (A14) and E15 (A41).

**Q31.** No. No non-sovereign VD or CV entity is rated above its ceiling, so the CeilingShape constraint finds no violation.

**Q32.** E09. E11's parent is E10, whose parent is E09, and E09 has none.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent record and no shared LEI with E10 or E09, so only the name suggests a link.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10, and E12 is unlinked.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 497. That is 540 records, less 14 QA test records and 29 research duplicates matched by LEI.

**Q38.** No. They have different LEIs and countries, and no record links them.

**Q39.** A, from A09 (affirmed 2025-09-15, recorded on E03, which shares E02's LEI).

**Q40.** 79 distinct GB-domiciled issuers hold an issuer rating, counted by hand from the entity list.

**Q41.** None. E16 is a QA test record, so its action A43/A44 does not count as an in-force rating.

**Q42.** LU. E17 (RESEARCH) gives LU, and the domicile rule prefers the research country over E10's DE.

**Q43.** 1. Only E10/E17, which is one entity, is domiciled in LU.

**Q44.** Yes. I07 is in XVD and its issuer E05 is domiciled in VD, whose domestic currency is XVD.

**Q45.** No. I07 is a local-currency note, and the ceiling (A12, BB) applies only to foreign-currency LTIDRs. Its BBB- (A45) is therefore not constrained.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected rating (A47, EX), which is not in force.

**Q48.** 113. Of 122 instruments, 9 carry only an EX rating.

**Q49.** E5001. The chain is E5047, E5035, E5023, E5011, E5005 (E5011's parent E5167 has E5005's LEI), E5002, then E5001.

**Q50.** 6 levels, because E5167 and E5005 are one entity.

**Q51.** 58, which is E5001 to E5058. E5170 is a QA record and is excluded.

**Q52.** 19, which is E5086 to E5104.

**Q53.** No. The RATINGS record for Belir Mining (E5062) places it under Belir (E5060/E5059). The research duplicate E5168 names E5086 as parent, and the rules ignore it.

**Q54.** E5106, E5124 and E5130. E5106 is domiciled in VD through its research record E5169, and the other two are VD in the entity list.

**Q55.** 30. This counts rated descendants of VD-domiciled entities: 6 under E5005, 2 under E5091, 8 under E5106 and 14 in the Geren group under E5145.

**Q56.** BB-. E5144 (A5108) is the lowest of the Vesol members' FC ratings.

**Q57.** E5002. E5011's chain runs E5005, E5002 and E5013's runs E5006, E5002.

**Q58.** E5145. I5007 is issued by E5133 (Vesol group) and guaranteed by E5145 (Geren group). All other guarantors are in the issuer's own group.

**Q59.** 12, which is E5011 to E5022.

**Q60.** E5145 is the risk-bearer, and it is not in the same group as the issuer. I5007's guarantor is E5145 (Geren), and the issuer E5133 is in the Vesol group.

**Q61.** 19 Cerid members hold an FC rating below investment grade, such as E5007 (B, A5002) and E5012 (BB, A5005). The full list is in the hand count; 15 more are investment grade.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1169","E1051","E1080","E1307","E5116","E5059","E1167","E1298","E1160","E1285","E1034","E1229","E1263","E1053","E1058","E1064","E1112","E1144","E1159","E1163","E1186","E1228","E1213","E1093","E5113","E5033","E5019","E1294","E1290","E5156","E1255","E1243","E1300","E1057","E1151"]},
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
"Q18": {"issuers": ["E06","E1264","E1098","E1061","E1209","E1037","E1181","E1006","E1099","E1088","E1059","E1109","E1132","E1133","E1146","E1168","E1194","E1203","E1242","E1260","E1266","E1267","E1297","E1314","E1317","E1323","E1238","E1039","E1019","E1126","E1013"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1261","E1263","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
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
"Q55": {"count": 30},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```