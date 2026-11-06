Several answers rest on inferred codes: CC = country ceiling, DG/UG/AS/AF/WD = downgrade/upgrade/assign/affirm/withdraw, RW/RWN = rating watch negative. CO and EX are undefined. Some counts and lists over the full dataset are incomplete because they can't be reliably done by hand; those are marked null or "partial".

**Q1.** A-. The LTIDR assigned 2024-03-12 (A01) was A- until downgraded to BBB on 2025-06-20 (A02).

**Q2.** No. The 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, BB+. I02 was downgraded from BBB to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E02 was STA (A08), but E03 (same LEI) was affirmed at A with POS on 2025-09-15 (A09), which is the later action.

**Q5.** E02 (guarantor), rated A. I03 is guaranteed by E02 and carries A (A11). The issuer E04 is also exposed but has no rating of its own.

**Q6.** The data doesn't state a reason. E05's FC rating (BB, A14) equals Valdoria's country ceiling (BB, A12), which is consistent with a sovereign cap, but that is inference.

**Q7.** 43 issuers had a DG action dated 2026. E1341 is excluded because its DG (A1720) is dated 2026-11-09, after today. E1299 is a duplicate record of E1298 (same LEI).

**Q8.** E08. It was moved to RD on 2026-07-08 (A22).

**Q9.** Not completed. Counting issuers with an active LTIDR across ~370 records needs a script.

**Q10.** Depends. The local-currency issuer rating is BBB- (A13), which is investment grade, but the foreign-currency rating is BB (A14), which is not.

**Q11.** BBB+. The DG to BBB+ on 2024-09-30 (A36) was the last rating change before that date.

**Q12.** A-. The assignment of A- on 2023-01-15 (A34) was the only rating then.

**Q13.** 1. The only downgrade is A36 (2024-09-30).

**Q14.** None. E12's first rating is assigned on 2024-02-01 (A30), after 1 January 2024.

**Q15.** A-. The rating was A- (A26) until downgraded to BBB+ on 2026-04-15 (A27).

**Q16.** No. The rating stayed at BBB+. The only later action is a rating watch placed on 2025-11-20 (A35), plus an affirmation (A33).

**Q17.** No. E06's only 2026 action is a rating watch negative (A17).

**Q18.** Partial. Active watches I could confirm include E06, E1098, E1109, E1126, E1132, E1133, E1146, E1181, E1194, E1210, E1242, E1260, E1266, E1297 and E1317. E1213 and E1276 are ambiguous.

**Q19.** Not completed. Negative-outlook status needs checking the latest LTIDR outlook for every entity.

**Q20.** No. E07 was withdrawn (A19), not put in default.

**Q21.** Partial. Withdrawn issuers include E07 (A19), E1032 (A1067), E1063 (A1138), E1084 (A1180), E1124 (A1268) and E1308 (A1664). The full list needs checking.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. Kestrel's short-term rating is STIDR F2 (A04).

**Q24.** Yes. Its issuer rating is BBB (A03).

**Q25.** Not completed. Counting instruments with an investment-grade rating on 1 October 2026 needs a script.

**Q26.** A+. The local-currency rating for E15 is A+ (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. The foreign-currency issuer rating for CV is BBB+ (A38).

**Q29.** None. VD has only a country-ceiling rating (BB, A12) and no issuer rating.

**Q30.** E05, E1028, E1126, E1236 (Valdoria, ceiling BB) and E15, E1039, E1194 (Corvenia, ceiling A). Each has a foreign-currency rating equal to its ceiling.

**Q31.** No. No Valdoria or Corvenia entity has a foreign-currency rating above its ceiling.

**Q32.** E09. Halden Leasing (E11) → Halden Bank (E10) → Halden Group (E09).

**Q33.** E10, rated BBB+. I05 is guaranteed by E10 and was downgraded to BBB+ on 2026-04-15 (A29).

**Q34.** No. E12 has no parent in the data, while E10 sits under E09.

**Q35.** 3. The group is E09, E10 and E11. The E17 record is a duplicate of E10.

**Q36.** 2. The group is E02 and E04.

**Q37.** 342. There are 370 records, minus 28 duplicates that share an LEI with another record (E03, E17 and 26 RESEARCH-source records).

**Q38.** No. They have different LEIs and countries.

**Q39.** A (A08 and A09).

**Q40.** Not completed. Counting GB issuers with an issuer rating on 1 October 2026 needs a script.

**Q41.** BB+. E16 was downgraded to BB+ on 2026-06-01 (A44).

**Q42.** DE. E10 is DE, but E17 (same LEI) says LU, which conflicts.

**Q43.** 1, E17 only. That record conflicts with E10 (DE), so the count could be 0.

**Q44.** Yes. I07 is denominated in XVD, the Valdoria currency.

**Q45.** Yes. The note is rated BBB- (A45), above the BB ceiling (A12). Ceilings normally constrain foreign-currency ratings, so this is a local-currency instrument.

**Q46.** No. E11 has only a CO rating (A46), not an LTIDR. CO is undefined, so this is an assumption.

**Q47.** A. I08 is rated A (A47, action EX).

**Q48.** Not completed. Counting instruments with a rating on 1 October 2026 needs a script.

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
  "Q18": {"issuers": ["E06","E1059","E1061","E1066","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1242","E1260","E1264","E1266","E1297","E1314","E1317","E1323"]},
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
  "Q30": {"entities": ["E05","E1028","E1126","E1236","E15","E1039","E1194"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 342},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": null},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "yes"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": null}
}
```