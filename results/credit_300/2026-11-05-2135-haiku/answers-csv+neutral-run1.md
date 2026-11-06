**Q1.** A-. The latest Kestrel FC action on or before 2025-01-01 is A01 (AS, A-, 2024-03-12); the downgrade came later in A02 (2025-06-20).

**Q2.** No. The 2026 actions on E01 are affirmations (A03 AF BBB NEG; A04 AF F2), and the only downgrade is A02 in 2025.

**Q3.** No, BB+. I02 was downgraded from BBB to BB+ by A07 (2025-06-20), which is its latest action.

**Q4.** Positive. E02 and E03 share an LEI, and the latest action is A09 (AF, A, POS, 2025-09-15).

**Q5.** The holder takes the guarantor's risk, E02 (Northwind Holdings), which is rated A. I03 is rated A (A11, AF), in line with E02.

**Q6.** The FC rating (BB, A14) is capped by the Republic of Valdoria's Country Ceiling of BB (A12). The LC rating (BBB-, A13) is not subject to the ceiling.

**Q7.** Thirty-one issuers were downgraded in 2026 (listed in the JSON). I found these by scanning the DG actions dated 2026, mapping duplicate records to their canonical IDs and excluding QA records. This was a manual scan, so treat it as a best reading.

**Q8.** E08. Its RD action (A22, 2026-07-08, distressed debt exchange) is the latest action.

**Q9.** 277. This is a manual tally of canonical non-QA, non-finance-subsidiary entities whose latest LTIDR action on or before 2026-10-01 is not a withdrawal. E1158 and E1303 have actions after their withdrawals; I counted them as rated (excluding them gives 275).

**Q10.** Depends. The LC rating (BBB-, A13) is investment grade, but the FC rating (BB, A14) is not.

**Q11.** BBB+. The latest action before 2025-06-01 is A36 (DG to BBB+, 2024-09-30). The later RW (A35) does not change the rating.

**Q12.** A-. A34 (AS, 2023-01-15) is the latest action before 2024-01-01.

**Q13.** 1. A36 (2024-09-30) is the only downgrade.

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01, after 1 January 2024.

**Q15.** A-. E10 (E17 is the same LEI) was rated A- by A26 (2023-05-01), and the downgrade to BBB+ came only on 2026-04-15 (A27).

**Q16.** No. The rating has been BBB+ since A36; later actions are AF (A33) and RW (A35), and neither changes the rating.

**Q17.** No. E06 has only AS (A16) and RW (A17, 2026-09-03), with no DG.

**Q18.** Twenty-nine issuers (listed in the JSON). A watch is treated as in force until a later action on the same entity and basis clears it. Some watches from 2022–2023 remain in force because nothing resolved them.

**Q19.** Twenty-nine issuers (listed in the JSON), based on the latest recorded outlook. Where RW or RD actions carry no outlook, I carried forward the previous one.

**Q20.** No. E07's latest action is a withdrawal (A19, 2026-05-12), which is not a default.

**Q21.** Thirty-six entities (listed in the JSON). These had an LTIDR history but no issuer rating on 2026-10-01, mostly through withdrawal.

**Q22.** E08 only. It is the only RD or D rating in the data.

**Q23.** F2. This is the short-term rating set by A04 (2026-02-10).

**Q24.** Yes. The long-term FC rating is BBB (A03).

**Q25.** 66. Of the 106 instruments rated on 2026-10-01, 66 are rated BBB- or higher. This is a manual tally.

**Q26.** A+. This is the LC rating set by A40 (2024-03-01).

**Q27.** A-. This is the instrument rating set by A42 (2024-03-01).

**Q28.** BBB+. This is the FC issuer rating set by A38 (2024-01-01).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05, E1028, E1126 and E1236 (domiciled in VD, ceiling BB), and E15, E1039 and E1194 (domiciled in CV, ceiling A).

**Q31.** No. No FC issuer rating is above its country's ceiling on 2026-10-01.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** Halden Bank AG (E10), rated BBB+. The 2028 notes (I05) are guaranteed by E10, and I05 was downgraded to BBB+ by A29.

**Q34.** No. E12 has no parent link, and E10's chain ends at E09.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 331. Of 370 records, I excluded 13 QA records and 26 RESEARCH duplicates of the same LEI. Sovereigns are counted, since the ontology defines them as legal entities.

**Q38.** No. The LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. This is the latest rating, set by A09 (AF, 2025-09-15).

**Q40.** 65. This is a manual tally of rated entities whose domicile is GB, using the RESEARCH record where it differs.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record E17 overrides the RATINGS record E10 (DE).

**Q43.** 1 (E10/E17).

**Q44.** Yes. XVD is VD's domestic currency, and E05 is domiciled in VD.

**Q45.** No. The Country Ceiling applies only to FC debt. I07 is XVD (local currency), so it is not capped.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only an EX action (A47), which is not a rating until an AS action confirms it.

**Q48.** 106. Seven of the 115 instruments are rated from the start (I01–I07), and 99 of the 107 I1xxx instruments have an AS action on or before 2026-10-01. The other nine (I08 and I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049) have only EX actions.

**Caveats:** Q7, Q9, Q18, Q19, Q21, Q25, Q37 and Q40 are manual tallies across hundreds of records, so small errors are possible. E1158 and E1303 have actions after their withdrawals, which the ontology says should not happen; I treated the later actions as setting a rating.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
  "Q18": {"issuers": ["E06","E1267","E1194","E1203","E1133","E1088","E1099","E1109","E1098","E1209","E1168","E1181","E1242","E1260","E1264","E1266","E1297","E1314","E1317","E1323","E1146","E1013","E1059","E1061","E1037","E1126","E1132","E1238","E1066"]},
  "Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1115","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320","E07"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": 66},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05","E1028","E1126","E1236","E15","E1039","E1194"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 331},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 65},
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