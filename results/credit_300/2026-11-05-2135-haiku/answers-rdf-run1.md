**Q1.** A-. The last LTIDR action before 1 Jan 2025 is A01 (AS A-, 2024-03-12); A02 (BBB) came later, in June 2025.

**Q2.** No. A03 (2026-02-10) affirmed BBB with a Negative outlook, and A04 assigned a short-term F2 with no prior short-term rating to compare.

**Q3.** No, BB+. The I02 2031 note was downgraded from BBB to BB+ (A07, 2025-06-20), and the BBB record (A23) is superseded.

**Q4.** Stable. Northwind Holdings (E02) has one action, A08 (AS A, STA).

**Q5.** E04 (Northwind Finance BV), rated A. The I03 notes are issued by E04 and guaranteed by E02, and the latest rating is A11 (A, 2025-09-15).

**Q6.** The data gives no stated reason. The foreign-currency rating (A14, BB) equals the Valdoria country ceiling (A12, BB), which is consistent with a ceiling cap, but the data does not say so.

**Q7.** 40 issuers had a 2026 rating change down. Examples: E1034 (A-→BBB+, A1070), E1051 (AA-→A+, A1102), E1064 (A-→BBB+, A1141/A1140). E1341 (A1720, 2026-11-09) is dated after today, so I excluded it.

**Q8.** E08. Its RD action (A22, 2026-07-08) follows a CCC rating and a distressed debt exchange.

**Q9.** Not reliably countable in this pass. Entity-level rated issuers less withdrawn ones would give the answer, but I did not complete a full tally.

**Q10.** Depends. Local-currency BBB- (A13) is investment grade, while foreign-currency BB (A14) is not.

**Q11.** BBB+. The downgrade to BBB+ (A36, 2024-09-30) is still in effect on 1 Jun 2025.

**Q12.** A-. The last rating before 1 Jan 2024 is A34 (A-, 2023-01-15).

**Q13.** Once. The only downgrade is A36 (2024-09-30).

**Q14.** None. Halden Foods' first rating is A30 (BB-, 2024-02-01), after 1 Jan 2024.

**Q15.** A-. Halden Bank AG (E10) was rated A- (A26) until the DG to BBB+ on 2026-04-15 (A27). E17 has the same LEI and no ratings.

**Q16.** No. The rating stayed BBB+ (A35 RW on 2025-11-20, then A33 AF on 2026-05-01).

**Q17.** No. Orrin Bank AG (E06) stayed A- (A16, A17), with a RW placed on 2026-09-03 but no downgrade.

**Q18.** 31 issuers have a latest watch action of RWN with no later rating action before 1 Oct 2026. I treated unresolved watches as still open, which the data does not confirm.

**Q19.** 34 issuers have a latest outlook of Negative as of 1 Oct 2026. I excluded withdrawn issuers and those whose negative outlook was later superseded.

**Q20.** No. Pellam Retail (E07) was withdrawn (A19), with no default.

**Q21.** 39 issuers were withdrawn with no later rating action. E1158, E1115, and E1303 are excluded because they have rating actions dated after their withdrawal.

**Q22.** E08 only.

**Q23.** F2. The short-term rating is A04 (STIDR, 2026-02-10).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 69 instruments were rated investment grade on 1 Oct 2026. This includes I1012 and I1021, whose EX action code is undefined, so 67 if those are excluded.

**Q26.** A+. Corvenia Power SA (E15) local-currency rating is A40 (A+, 2024-03-01).

**Q27.** A-. The I06 2032 note is A42 (A-, 2024-03-01).

**Q28.** BBB+. The Republic of Corvenia's foreign-currency issuer rating is A38 (BBB+, LTIDR).

**Q29.** None. The only VD record is A12, typed CC and rated BB, which appears to be the country ceiling rather than an issuer rating.

**Q30.** E05, E1028, E1039, E1101, E1126, E1194. The Valdoria (VD) ceiling is BB and the Corvenia (CV) ceiling is A; these entities' latest foreign-currency ratings match those ceilings.

**Q31.** No. None of the foreign-currency ratings exceed their country ceilings.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09.

**Q33.** E11 (Halden Leasing SA), rated BBB+. The I05 2028 note is A29 (BBB+, 2026-04-15) and is guaranteed by E10.

**Q34.** No. E12 has no parent link, and E10's chain runs through E09 and E11 only.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02 and E04). E03 shares E02's LEI and is treated as a duplicate.

**Q37.** Not reliably countable in this pass. The data has many duplicates (for example E17/E10, E03/E02, E1002/E1001, E1022/E1021) that would need deduplication by LEI.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A (A08).

**Q40.** Not reliably countable in this pass, for the same reason as Q9.

**Q41.** BB+. Brindle Capital (E16) was downgraded from BBB- to BB+ (A44, 2026-06-01).

**Q42.** DE, per E10. E17 (same LEI) says LU, so the data conflicts.

**Q43.** 1 (E17), though E17 duplicates E10's LEI.

**Q44.** Yes. The 2027 note (I07) is in XVD, which I take as Valdoria's local currency; that is an inference, not stated.

**Q45.** Depends. BBB- (A45) is numerically above the BB ceiling (A12), but ceilings govern foreign currency and this note is local currency.

**Q46.** Depends. E11 has a BBB rating (A46) of type CO, which the data does not define.

**Q47.** A (A47, I08 EX). The EX code is undefined, so the rating is treated as current.

**Q48.** 112. There are 115 instrument records, and I1001, I1007, and I1015 have no rating action on or before 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "Stable"},
  "Q5": {"risk_of": "E04", "rating": "A"},
  "Q7": {"issuers": ["E1034", "E1051", "E1053", "E1057", "E1058", "E1064", "E1080", "E1093", "E1112", "E1144", "E1151", "E1159", "E1161", "E1163", "E1167", "E1170", "E1186", "E1213", "E1228", "E1229", "E1243", "E1255", "E1263", "E1285", "E1290", "E1294", "E1299", "E1300", "E1307", "E1340", "E1342", "E1343", "E1344", "E1345", "E1346", "E1347", "E1348", "E1349", "E1350", "E1351"]},
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
  "Q18": {"issuers": ["E06", "E1006", "E1013", "E1019", "E1037", "E1039", "E1059", "E1061", "E1066", "E1088", "E1098", "E1099", "E1109", "E1126", "E1132", "E1133", "E1146", "E1168", "E1181", "E1194", "E1203", "E1210", "E1242", "E1260", "E1264", "E1266", "E1267", "E1297", "E1314", "E1317", "E1323"]},
  "Q19": {"issuers": ["E01", "E09", "E1029", "E1034", "E1046", "E1055", "E1060", "E1064", "E1079", "E1080", "E1105", "E1118", "E1132", "E1161", "E1188", "E1190", "E1211", "E1228", "E1248", "E1262", "E1263", "E1271", "E1282", "E1294", "E1300", "E1340", "E1342", "E1343", "E1344", "E1345", "E1347", "E1348", "E1350", "E1351"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07", "E1002", "E1007", "E1021", "E1032", "E1041", "E1048", "E1057", "E1062", "E1063", "E1076", "E1084", "E1106", "E1107", "E1121", "E1124", "E1138", "E1140", "E1155", "E1159", "E1166", "E1172", "E1200", "E1205", "E1206", "E1218", "E1219", "E1225", "E1233", "E1234", "E1244", "E1254", "E1277", "E1279", "E1308", "E1316", "E1320"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": 69},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E1028", "E1039", "E1101", "E1126", "E1194"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E11", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": null},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": null},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "depends"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 112}
}
```