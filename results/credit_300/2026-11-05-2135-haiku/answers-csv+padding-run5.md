**Notes on the data**
- Action codes CO, EX, RW, WD and RD are not defined in the data. I read RW as rating watch, WD as withdrawal, RD as default, and CO and EX as unclear.
- Five rating actions are dated after today (2026-11-05): A1011, A1029, A1078, A1713 and A1720. I excluded them from "current" views. A1720 would have moved E1341 to a downgrade.
- Several records share an LEI (for example E02/E03, E10/E17, E1147/E1148), so I treated them as one legal entity. Some records come from the QA or RESEARCH source systems and may not be reliable.
- Questions that need a full count or list across the whole dataset (Q9, Q18, Q19, Q25, Q37, Q40, Q48) were not fully enumerated by hand. They are marked null in the JSON.

**Q1.** A-. A01 assigned A- on 2024-03-12, and the downgrade to BBB (A02) came on 2025-06-20, after the date asked about.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04). The downgrade was in 2025 (A02).

**Q3.** No, BB+. The 2031 notes (I02) were downgraded from BBB to BB+ on 2025-06-20 (A07, after A23).

**Q4.** POS, but the records conflict. E03 (RESEARCH source) shows Positive on 2025-09-15 (A09), while E02 (RATINGS source) shows Stable from 2023-11-01 (A08). The data does not say which record is authoritative.

**Q5.** E02 (Northwind Holdings), which guarantees the notes. The issuer is E04, and the notes (I03) are rated A (A11).

**Q6.** The data gives no reason. Valdoria Telecom's foreign-currency rating (BB, A14) equals Valdoria's country ceiling (BB, A12), which fits a transfer cap, but the data does not say so.

**Q7.** 43 issuers: E08, E10, E16, E1034, E1051, E1053, E1057, E1058, E1064, E1080, E1093, E1112, E1144, E1151, E1159, E1161, E1163, E1167, E1170, E1186, E1213, E1228, E1229, E1243, E1255, E1263, E1285, E1290, E1294, E1299, E1300, E1307, E1340, E1342–E1351 (excluding E1341, whose downgrade is dated after today). This is from a hand scan of 2026-dated DG actions, so it may not be exhaustive. Instrument I05 was also downgraded in 2026 but is excluded.

**Q8.** E08. Its RD rating (A22, 2026-07-08) followed a distressed debt exchange.

**Q9.** Not counted. A full count needs every entity's latest status checked against 2026-10-01.

**Q10.** Depends. Local-currency rating is BBB- (A13, investment grade), while foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. The downgrade to BBB+ on 2024-09-30 (A36) was still in place on 2025-06-01, and the 2025 rating watch did not change the rating.

**Q12.** A-. A34 assigned A- on 2023-01-15.

**Q13.** 1. The only downgrade is A36 (2024-09-30). A35 is a rating watch, not a downgrade.

**Q14.** None. Halden Foods' first rating (BB-, A30) was assigned on 2024-02-01, after 1 January 2024.

**Q15.** A-. Halden Bank AG (E10) was rated A- (A26) until its downgrade to BBB+ on 2026-04-15 (A27). The LU record E17 has no ratings.

**Q16.** No. The rating stayed at BBB+ from 2024-09-30 onward. The 2025 rating watch and the 2026 affirmation did not change it.

**Q17.** No. The 2026-09-03 action (A17) placed Orrin Bank on a Rating Watch Negative, but it was not a downgrade.

**Q18.** Not fully counted. Watches with no later action as of 1 October 2026 include E06, E1066, E1098, E1133, E1238, E1242, E1260, E1266 and E1297. Several older watches also have no resolution, so the full answer depends on how stale watches are treated.

**Q19.** Not fully counted. Examples include E01 (A03), E09 (A25) and E1342 (A1722). The full list was not compiled.

**Q20.** No. Pellam Retail (E07) was withdrawn on 2026-05-12 (A19), which is not a default.

**Q21.** 35 entities had a rating that was withdrawn with no later rating: E07, E1002, E1007, E1021, E1032, E1041, E1048, E1057, E1062, E1063, E1076, E1107, E1121, E1124, E1138, E1140, E1155, E1159, E1166, E1172, E1200, E1205, E1206, E1218, E1219, E1225, E1233, E1234, E1244, E1254, E1277, E1279, E1308, E1316, E1320. Entities that were re-rated after a withdrawal are excluded.

**Q22.** E08. It is the only entity with an RD rating.

**Q23.** F2. This is the short-term rating set on 2026-02-10 (A04).

**Q24.** Yes. The issuer rating is BBB (A03, 2026-02-10).

**Q25.** Not counted.

**Q26.** A+. This is Corvenia Power's local-currency rating (A40, 2024-03-01).

**Q27.** A-. The 2032 notes (I06) were rated A- on 2024-03-01 (A42).

**Q28.** BBB+. This is the foreign-currency issuer rating for the Republic of Corvenia (A38, 2024-01-01).

**Q29.** None as an issuer rating. The only Valdoria entry is a country ceiling of BB (A12, CC type), which is not an issuer rating.

**Q30.** The entities at ceiling on 1 October 2026 are E05, E1028, E1101, E1126 and E1236 (Valdoria, BB ceiling) and E15, E1039 and E1194 (Corvenia, A ceiling). This comes from a scan and may not be complete.

**Q31.** No. No foreign-currency issuer rating is above its country's ceiling. The highest Valdoria entities are BB, and the highest Corvenia entities are A.

**Q32.** E09 (Halden Group plc), via E10 (Halden Bank AG).

**Q33.** E10 (the guarantor, Halden Bank AG). The issuer is E11 and the notes (I05) are rated BBB+ after the downgrade on 2026-04-15 (A29).

**Q34.** No. E12 has no parent link to E09 or E10, and its LEI differs.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10, so it is the same legal entity.

**Q36.** 2: E02 and E04. E03 has the same LEI as E02.

**Q37.** Not counted. Duplicate LEIs would need to be collapsed first.

**Q38.** No. Their LEIs differ (549300AMVE… and 815600O8X…).

**Q39.** A. Both E02 (A08) and E03 (A09) are rated A.

**Q40.** Not counted.

**Q41.** BB+. This is the 2026-06-01 downgrade from BBB- (A44). The record is QA source.

**Q42.** DE, per the RATINGS record E10. The RESEARCH record E17 gives LU, so the records conflict.

**Q43.** 1 record (E17). It shares an LEI with E10, which is domiciled in DE, so it may not be a separate legal entity.

**Q44.** Yes, inferred. I07's currency is XVD, which matches Valdoria's country code VD, but the data does not define XVD as local currency.

**Q45.** Depends. The BBB- rating (A45) is numerically above the BB ceiling, but the ceiling only caps foreign-currency ratings. The instrument rating has no currency basis recorded.

**Q46.** No. Halden Leasing has only a CO-type rating (A46, BBB). CO is not an issuer rating type in the data.

**Q47.** A. The 2034 notes (I08) were rated A on 2026-09-01 (A47), with the action code EX (undefined).

**Q48.** Not counted.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
  "Q18": {"issuers": null},
  "Q19": {"issuers": null},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320"]},
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
  "Q37": {"count": null},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": null},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": null}
}
```