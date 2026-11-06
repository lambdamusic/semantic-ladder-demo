**Q1.** A-. E01's FC LTIDR rating of A- ran from 2024-03-12 to 2025-06-20 (A01), which covers 1 Jan 2025.

**Q2.** No. E01's rating stayed BBB through 2026; the 2026-02-10 change (A03) only moved the outlook to negative.

**Q3.** No. I02 is rated BB+ from 2025-06-20 (A07, still open).

**Q4.** Positive. E02's A rating carries a POS outlook from 2025-09-15 (A09, still open).

**Q5.** Northwind Holdings (E02). I03 has credit_risk_of E02, and it is rated A (A11).

**Q6.** The data doesn't state a reason. Valdoria Telecom's FC rating (BB, A14) equals Valdoria's country ceiling (BB, ceilings.csv), while its LC rating (BBB-, A13) is not capped, so the ceiling is the likely cause. This is an inference.

**Q7.** 31 issuers had a rating lower than the prior one during 2026 (for example E08, E10, E1034, E1051). E1064's 2026-02-02 move from A- to BBB+ is labelled AF, but I counted it because the symbol fell.

**Q8.** E08 is the only issuer in default: RD from 2026-07-08 (A22).

**Q9.** 278. This counts entities with an open, non-withdrawn LTIDR rating on 1 Oct 2026. It is a manual tally, so treat it as a careful count rather than a verified query.

**Q10.** Depends. Valdoria Telecom's LC rating is BBB- (investment grade), but its FC rating is BB (not), so the answer depends on the currency basis.

**Q11.** BBB+. Marlow Utilities (E14) was BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. Marlow Utilities (E14) was A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** Once. Marlow Utilities (E14) went from A- to BBB+ on 2024-09-30 (A36); later records are watch or affirmation.

**Q14.** None. Halden Foods (E12) has no rating before 2024-02-01 (A30).

**Q15.** A-. Halden Bank (E10) was A- until 2026-04-15 (A26).

**Q16.** No. Marlow Utilities (E14) stayed at BBB+ (A36, A35, A33), though it was placed on watch and then cleared.

**Q17.** No. Orrin Bank (E06) stayed at A- and moved to Rating Watch Negative (A16, A17).

**Q18.** 32 issuers were on Rating Watch Negative on 1 Oct 2026, each with an open RW record (e.g., E06 from 2026-09-03, A17).

**Q19.** 28 issuers had a Negative outlook on 1 Oct 2026 (e.g., E01, E09, E1005).

**Q20.** No. Pellam Retail (E07) was withdrawn on 2026-05-12 (A19).

**Q21.** 35 entities had a rating that was withdrawn and not replaced (their latest record is WD, e.g., E07 A19, E1001 A1002).

**Q22.** E08 is the only entity that has been in default (RD, A22).

**Q23.** F2. Kestrel Energy (E01) holds an open STIDR of F2 (A04).

**Q24.** Yes. Kestrel Energy (E01) has a BBB issuer rating (A03).

**Q25.** 66 instruments held investment-grade ratings on 1 Oct 2026, from the open instrument records (e.g., I01 BBB, A06).

**Q26.** A+. Corvenia Power (E15) holds an LC rating of A+ (A40).

**Q27.** A-. The Corvenia Power 2032 note (I06) is rated A- (A42).

**Q28.** BBB+. The Republic of Corvenia (CV) FC issuer rating is BBB+ (A38).

**Q29.** None. The Republic of Valdoria (VD) has no rating records.

**Q30.** Corvenia-domiciled E15, E1039, E1194 (ceiling A), and Valdoria-domiciled E05, E1028, E1101, E1126, E1236 (ceiling BB), all with open FC ratings at the ceiling.

**Q31.** No. No FC issuer rating exceeds its country ceiling on 1 Oct 2026.

**Q32.** E09. Halden Leasing (E11) has parent E10, and ultimate parent E09 (Halden Group plc).

**Q33.** E10 (Halden Bank), rated BBB+. The Halden Leasing 2028 notes (I05) have credit_risk_of E10 and are rated BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no parent and no ultimate parent, so it is outside the Halden Group (E09, E10, E11).

**Q35.** 3: E09, E10, E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 entity records in entities.csv (316 issuers plus 15 finance subsidiaries).

**Q38.** No. Orrin Bank AG (E06, DE) and Orrin Bancorp Inc (E13, US) are separate entities.

**Q39.** A. Northwind Holdings (E02) has an A rating with a positive outlook (A09).

**Q40.** 65 GB-domiciled issuers held an open issuer rating on 1 Oct 2026, excluding withdrawn ones (e.g., E07, E1007, E1021, E1057, E1062, E1124, E1200).

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** LU. Halden Bank (E10) is domiciled in Luxembourg.

**Q43.** 1: E10 is the only LU-domiciled entity.

**Q44.** Yes. The Valdoria Telecom 2027 note (I07) has local_currency = yes.

**Q45.** No. BBB- (A45) is numerically above BB, but I07 is local-currency and the ceiling is a foreign-currency cap. The data does not state that scope, so this relies on an inference.

**Q46.** No. Halden Leasing (E11) has no LTIDR rating records.

**Q47.** None. There is no rating record for the Corvenia Power 2034 note (I08).

**Q48.** 106 instruments held an open rating on 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E1034", "E1051", "E1053", "E1057", "E1058", "E1064", "E1080", "E1093", "E1112", "E1144", "E1151", "E1159", "E1160", "E1163", "E1167", "E1169", "E1186", "E1213", "E1228", "E1229", "E1243", "E1255", "E1263", "E1285", "E1290", "E1294", "E1298", "E1300", "E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 278},
  "Q10": {"investment_grade": "depends"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06", "E1006", "E1013", "E1019", "E1037", "E1039", "E1059", "E1061", "E1066", "E1088", "E1098", "E1099", "E1109", "E1126", "E1132", "E1133", "E1146", "E1168", "E1181", "E1194", "E1203", "E1209", "E1238", "E1242", "E1260", "E1264", "E1266", "E1267", "E1297", "E1314", "E1317", "E1323"]},
  "Q19": {"issuers": ["E01", "E09", "E1005", "E1029", "E1034", "E1046", "E1055", "E1056", "E1059", "E1064", "E1072", "E1079", "E1080", "E1105", "E1118", "E1158", "E1160", "E1188", "E1190", "E1211", "E1228", "E1248", "E1261", "E1263", "E1271", "E1282", "E1294", "E1300"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07", "E1001", "E1007", "E1021", "E1032", "E1041", "E1048", "E1057", "E1062", "E1063", "E1076", "E1084", "E1107", "E1121", "E1124", "E1138", "E1140", "E1155", "E1159", "E1166", "E1172", "E1200", "E1205", "E1206", "E1218", "E1219", "E1225", "E1233", "E1234", "E1244", "E1253", "E1277", "E1308", "E1316", "E1320"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes", "rating": "BBB"},
  "Q25": {"count": 66},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E15", "E1039", "E1194", "E05", "E1028", "E1101", "E1126", "E1236"]},
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