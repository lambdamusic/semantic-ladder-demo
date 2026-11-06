**Q1.** A-. The latest FC LTIDR action on E01 before 1 Jan 2025 is A01 (assigned A-, 2024-03-12); the next action, A02, is dated 2025-06-20.

**Q2.** No. E01's 2026 actions are A03 and A04, both affirmations.

**Q3.** No. The 2031 note (I02) is subordinated, and its latest action (A07, 2025-06-20) is a downgrade to BB+.

**Q4.** POS (Positive). E02's latest action is A09 (affirmed A, outlook POS, 2025-09-15), recorded against its RESEARCH duplicate E03, which is the same LEI.

**Q5.** Northwind Holdings (E02). I03 is guaranteed by E02, so it is rated in line with E02's issuer rating, which is A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12). It caps foreign-currency ratings of VD-domiciled entities, so E05's FC rating is BB (A14), while its local-currency rating (BBB-, A13) is not capped.

**Q7.** 31 issuers were downgraded in 2026, per DG actions dated 2026. Records are listed in the JSON. E1169 is named by its RATINGS record; its actions sit on its RESEARCH duplicate E1170. E1064's 2026 DG (A1140) conflicts with its neighbouring actions (A1141 AF at BBB+, A1142 UG to A-), so treat it as doubtful.

**Q8.** E08. Its latest action is A22 (RD, 2026-07-08), and nothing later overrides it.

**Q9.** Not determined in this pass. An exact count needs the latest LTIDR action for each of about 330 entities as of 1 Oct 2026.

**Q10.** Depends. Its FC rating is BB (A14, not investment grade), but its LC rating is BBB- (A13, investment grade).

**Q11.** BBB+. A36 (downgrade to BBB+, 2024-09-30) is the latest action on E14 before 1 Jun 2025.

**Q12.** A-. A34 (assigned A-, 2023-01-15) is the latest action before 1 Jan 2024.

**Q13.** 1. A36 is the only DG action on E14.

**Q14.** None. Halden Foods' first rating, E12's A30 (assigned BB-), is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. A26 (assigned A-, 2023-05-01) is the latest action before 1 Jan 2026; the downgrade to BBB+ (A27) came on 2026-04-15. E17 is the RESEARCH duplicate and has no actions of its own.

**Q16.** No. After 1 Jan 2025, E14's only actions are A35 (watch) and A33 (affirmation), and neither changes the rating.

**Q17.** No. E06's 2026 action is A17, a Rating Watch placement, not a downgrade.

**Q18.** 31 issuers were on Rating Watch Negative on 1 Oct 2026, judged by each entity's latest action. Several watches date from 2022–2024 and the data sets no expiry, so I treat them as still open. That is a judgment, and the data does not settle it.

**Q19.** Not determined in this pass. It needs the per-entity latest outlook as of 1 Oct 2026, which I have not completed.

**Q20.** No. E07's latest action is A19, a withdrawal.

**Q21.** 33 entities had a rating that was withdrawn and not reinstated by 1 Oct 2026, judged by their latest action. Records are listed in the JSON.

**Q22.** E08. It is the only entity with an RD (A22).

**Q23.** F2. This is A04 (affirmed, 2026-02-10).

**Q24.** Yes. Its current issuer rating is BBB (A03).

**Q25.** Not determined in this pass. It needs the latest instrument rating for each of about 115 instruments as of 1 Oct 2026.

**Q26.** A+. This is E15's LC rating, A40 (assigned 2024-03-01).

**Q27.** A-. I06 is subordinated, and its instrument rating is A- (A42).

**Q28.** BBB+. This is A38. A37 (A) is the Country Ceiling, not a sovereign rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** Eight entities had FC issuer ratings exactly at their country's ceiling: five VD entities at BB (VD ceiling BB, A12) and three CV entities at A (CV ceiling A, A37). Records are listed in the JSON.

**Q31.** No. The VD ceiling is BB and the CV ceiling is A, and no FC issuer rating sits above either.

**Q32.** E09. The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank). I05 is guaranteed by E10, so it is rated in line with E10's BBB+ (A27), and the instrument's own rating is BBB+ (A29).

**Q34.** No. E12 has no parent link and is not in E09's group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 331. There are 370 records, minus 13 QA records (E16 and E1340–E1351), minus 26 duplicate RESEARCH records that share an LEI with another record.

**Q38.** No. The LEIs differ: E06 is 549300AMVE3VRVG7HK43 and E13 is 815600O8X8K2F154N214.

**Q39.** A. This is E02's latest action, A09 (affirmed A, POS, 2025-09-15).

**Q40.** Not determined in this pass. It needs the full GB issuer census as of 1 Oct 2026.

**Q41.** None. E16 is a QA record, and the ontology says to ignore it.

**Q42.** LU. The RESEARCH record E17 holds for domicile, so it overrides E10's DE.

**Q43.** 1. Only E17/E10 (Halden Bank) is domiciled in LU.

**Q44.** Yes. XVD is VD's domestic currency, so I07 is local-currency debt.

**Q45.** No. Local-currency debt is not subject to the ceiling, so BBB- is not capped.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. A47 is an EX action (expected rating), and the instrument stays unrated until an AS action.

**Q48.** Not determined in this pass. It needs the latest instrument action for each instrument as of 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E1034", "E1051", "E1053", "E1057", "E1058", "E1064", "E1080", "E1093", "E1112", "E1144", "E1151", "E1159", "E1161", "E1163", "E1167", "E1169", "E1186", "E1213", "E1228", "E1229", "E1243", "E1255", "E1263", "E1285", "E1290", "E1294", "E1298", "E1300", "E1307"]},
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
  "Q18": {"issuers": ["E06", "E1267", "E1194", "E1203", "E1133", "E1088", "E1099", "E1019", "E1168", "E1209", "E1098", "E1037", "E1061", "E1264", "E1132", "E1126", "E1059", "E1314", "E1317", "E1146", "E1013", "E1181", "E1266", "E1238", "E1297", "E1323", "E1260", "E1066", "E1242", "E1109", "E1039"]},
  "Q19": {"issuers": null},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07", "E1001", "E1032", "E1041", "E1048", "E1057", "E1062", "E1063", "E1076", "E1084", "E1107", "E1121", "E1124", "E1138", "E1140", "E1155", "E1159", "E1166", "E1172", "E1200", "E1205", "E1206", "E1218", "E1219", "E1225", "E1233", "E1234", "E1244", "E1277", "E1279", "E1308", "E1316", "E1320"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": null},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E1028", "E1101", "E1126", "E1236", "E15", "E1039", "E1194"]},
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
  "Q48": {"count": null}
}
```