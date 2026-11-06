**Q1.** A-. E01's rating was set by A01 (2024-03-12) and not changed until A02 (2025-06-20).
**Q2.** No. The only 2026 action is A03 (2026-02-10), an affirmation at BBB with the outlook revised to Negative.
**Q3.** No, it is BB+. I02 is subordinated and was downgraded to BB+ by A07 (2025-06-20).
**Q4.** Positive. A09 (2025-09-15) is the latest action on LEI 213800PHEIYNJMHTDV74, recorded under E03, so it applies to E02.
**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and E02's rating is A (A08, A09).
**Q6.** The Country Ceiling for VD is BB (A12) and caps foreign-currency ratings. E05's FC rating is BB (A14) and its LC rating is BBB- (A13); local-currency ratings are not capped.
**Q7.** 30 issuers had a 2026 LTIDR downgrade, merging duplicate records by LEI and ignoring QA records. They are listed in the JSON, where E1160, E1169 and E1298 are the RATINGS IDs for downgrades recorded on E1161, E1170 and E1299.
**Q8.** E08. A22 (2026-07-08) took it to RD, a default, and nothing later changed that.
**Q9.** About 277. This counts distinct LEIs with a non-withdrawn LTIDR, FC or LC, on 2026-10-01, excluding QA records, sovereign ceilings and credit opinions. A few records (E1115, E1158, E1303) have actions dated after a withdrawal; I followed the latest-action rule and counted them, so the figure is approximate.
**Q10.** Depends on the basis. The FC rating is BB (A14), which is speculative grade, and the LC rating is BBB- (A13), which is investment grade.
**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action, A35, only placed it on Watch.
**Q12.** A-. A34 (2023-01-15) assigned A- and the downgrade came later.
**Q13.** 1. Only A36 is a DG for E14.
**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).
**Q15.** A-. E10 and E17 share an LEI, and A26 (A-) held until A27 (2026-04-15).
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; A35 was a Watch and A33 an affirmation.
**Q17.** No. A17 (2026-09-03) is a Rating Watch with the rating unchanged at A-.
**Q18.** 32 issuers were on RWN, each with an RW as their latest action; they are in the JSON. RW rows carry no outlook, and those that were later withdrawn or changed are excluded.
**Q19.** 27 issuers had a Negative outlook. I carried the outlook forward through RW rows, so E1146 and E1132 are counted, and E1158 is counted by the same latest-action rule as in Q9.
**Q20.** No. E07's rating was BB and was withdrawn by A19 (commercial reasons), which is not a default.
**Q21.** 35 entities had a rating that was later withdrawn and held no other rating on 2026-10-01 (listed in the JSON). Entities with an LC rating still active, such as E1279 and E1106, are not included.
**Q22.** E08 only. A22 is the only RD or D rating in the data.
**Q23.** F2. A04 is the E01 STIDR action.
**Q24.** Yes. The FC LTIDR is BBB (A03).
**Q25.** 66. Of the 106 instruments with a rating on 2026-10-01, 40 are BB+ or below, using each instrument's latest INST action and ignoring EX.
**Q26.** A+ (A40). Local-currency ratings are not capped.
**Q27.** A-. I06 was rated A- by A42, which is below the CV ceiling of A (A37).
**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not a rating.
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** Eight entities. In CV (ceiling A), E15 and E1039 and E1194 are at A. In VD (ceiling BB), E05, E1028, E1101, E1126 and E1236 are at BB.
**Q31.** No. No FC rating of an entity in CV or VD exceeds A or BB respectively.
**Q32.** E09. E11's parent is E10, whose parent is E09, which has no parent.
**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27.
**Q34.** No. E12 has no parent, while E10 belongs to E09's group.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 (same entity as E03) and E04.
**Q37.** 331. There are 370 records, minus 13 QA records and 26 duplicate-LEI records.
**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214).
**Q39.** A (A09).
**Q40.** 64 GB-domiciled issuers, with the same Q9 caveat on E1115.
**Q41.** None. E16 is a QA record, so it and A43/A44 are ignored.
**Q42.** LU. The RESEARCH record (E17) holds for country, and E10 says DE.
**Q43.** 1: E17 (Halden Bank).
**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and E05 is domiciled in VD.
**Q45.** No. I07 is local-currency debt, so the ceiling does not apply, and its BBB- rating (A45) is not capped.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected action (A47), so it is unrated.
**Q48.** 106. Of 115 instruments, 9 have only EX actions (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1058","E1163","E1213","E1228","E1307","E1186","E1034","E1169","E1159","E1160","E1167","E1285","E1263","E1298","E1300","E1080","E1057","E1053","E1051","E1144","E1243","E1255","E1290","E1294","E1112","E1229","E1093"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 277},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1109","E1264","E1168","E1019","E1006","E1088","E1099","E1297","E1260","E1209","E1181","E1146","E1066","E1098","E1126","E1059","E1132","E1061","E1266","E1323","E1238","E1314","E1317","E1037","E1013"]},
"Q19": {"issuers": ["E01","E09","E1118","E1158","E1079","E1228","E1056","E1034","E1029","E1046","E1064","E1146","E1072","E1261","E1263","E1294","E1300","E1080","E1005","E1248","E1271","E1132","E1282","E1190","E1160","E1105","E1211"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320","E1159"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 331},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 64},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```