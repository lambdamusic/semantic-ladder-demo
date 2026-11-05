**Q1.** A-. A01 (2024-03-12) set the rating, and it was cut to BBB only on 2025-06-20 (A02).

**Q2.** No. The 2026 actions on E01 are A03 (BBB affirmed, outlook moved to negative) and A04 (F2 affirmed).

**Q3.** No. I02's latest rating is BB+ (A07, 2025-06-20), which is below investment grade.

**Q4.** Ambiguous. E02 (A08) shows Stable, but E03 (A09, later) shows Positive; both carry the same LEI (213800PHEIYNJMHTDV74), and the data doesn't say which record governs.

**Q5.** Northwind Finance BV (E04), with guarantor E02 also in the chain. I03 is rated A (A11, 2025-09-15).

**Q6.** The data gives no explicit reason. E05's foreign-currency rating (BB, A14) equals Valdoria's country ceiling (BB, A12, type CC), while its local-currency rating is BBB- (A13), so the ceiling is the likely cause.

**Q7.** E08 (A21 CCC, A22 RD), E10 (A27 BBB+) and E16 (A44 BB+). I05 was also downgraded in 2026 (A29), but it is an instrument, not an issuer.

**Q8.** E08, rated RD (A22, 2026-07-08) with no later rating.

**Q9.** 13. These are the entities with active LTIDR/STIDR ratings: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16, CV. E11 is excluded because its only rating is type CO (undefined), E07 was withdrawn (A19), and E03 is counted with E02 (same LEI).

**Q10.** Depends. The local-currency rating BBB- (A13) is investment grade; the foreign-currency rating BB (A14) is not.

**Q11.** BBB+. A36 (2024-09-30) set it; the later A35 is a watch placement only.

**Q12.** A-. A34 (2023-01-15) is the latest rating before that date.

**Q13.** 1. A36 (2024-09-30, DG) is the only downgrade; A35 is a watch placement, not a rating change.

**Q14.** None. Halden Foods' first rating is A30 (2024-02-01), after that date.

**Q15.** A-. A26 (2023-05-01) stands until A27 (2026-04-15).

**Q16.** No. A36 (BBB+) is still current; A35 added a watch and A33 affirmed BBB+.

**Q17.** No. E06's actions are A16 (2024) and A17 (watch, 2026-09-03), with no downgrade.

**Q18.** E06, on Rating Watch Negative from A17 (2026-09-03) with no resolution recorded. E14's watch (A35) appears resolved by the 2026-05-01 affirmation (A33) that carries no watch flag, but that is an inference.

**Q19.** E01 (A03, negative) and E09 (A25, negative).

**Q20.** No. E07 was withdrawn (A19, WD); a withdrawal is not a default.

**Q21.** E07, which was rated until its withdrawal (A19, 2026-05-12).

**Q22.** E08, its only default being RD (A22).

**Q23.** F2, the short-term issuer rating (A04, 2026-02-10).

**Q24.** Yes. E01's long-term issuer rating is BBB (A03).

**Q25.** 6. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A) are investment grade; I02 (BB+) and I04 (BB) are not.

**Q26.** A+. E15's local-currency rating is A40 (2024-03-01).

**Q27.** A-. I06's only rating is A42 (2024-03-01).

**Q28.** BBB+. CV's foreign-currency issuer rating is A38; A37 (A) is its country ceiling and A39 is its local-currency rating.

**Q29.** None. VD's only rating is a CC rating (A12, BB), which is the country ceiling, not an issuer rating.

**Q30.** E05 (foreign-currency BB, A14, equal to VD's ceiling of BB in A12) and E15 (foreign-currency A, A41, equal to CV's ceiling of A in A37).

**Q31.** No. E05 (BB) and E15 (A) sit at, not above, their ceilings; the data has no ceilings for other countries.

**Q32.** E09. The chain is E11 → E10 → E09 (Halden Group plc, no parent).

**Q33.** E11 is the issuer; guarantor E10 also carries risk. I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent recorded and shares no parent with E10 (which sits under E09).

**Q35.** 3: E09, E10 and E11. E12 has no recorded parent link, and E17 shares E10's LEI so is not added.

**Q36.** 2: E02 and E04. E03 shares E02's LEI and is the same entity.

**Q37.** 15 distinct LEI-bearing entities. The 19 records include 2 duplicate-LEI pairs (E02/E03, E10/E17) and 2 sovereigns (VD, CV) with no LEI, giving 17 if the sovereigns are counted.

**Q38.** No. They have different LEIs, countries (DE vs US) and names.

**Q39.** A. Both E02 (A08) and E03 (A09) show A.

**Q40.** 6: E01, E02, E09, E12, E14, E16. E16 is QA-sourced, and E07 is excluded because it was withdrawn.

**Q41.** BB+ (A44, 2026-06-01). Note that E16 is QA-sourced.

**Q42.** Ambiguous. E10 "Halden Bank AG" is DE (RATINGS), while E17 "HALDEN BANK" is LU (RESEARCH); both share LEI 391200QYPVFF2O9K2039.

**Q43.** 1: E17, per its LU record. That record conflicts with E10's DE.

**Q44.** Depends. I07 is denominated in XVD, but the data doesn't state that XVD is Valdoria's local currency.

**Q45.** Depends. I07's BBB- (A45) is above the BB ceiling (A12) only if the note is a foreign-currency obligation. If XVD is local currency, the ceiling doesn't apply (see Q44).

**Q46.** Depends. E11's only rating is A46 (BBB), of type CO, which the data doesn't define as an issuer rating.

**Q47.** A (A47, 2026-09-01). The EX action code is undefined in the data, so this is a caveat, not a certainty.

**Q48.** 8. All eight instruments (I01–I08) have a current rating.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "ambiguous (STA per E02; POS per E03)"},
  "Q5": {"risk_of": "E04", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E16"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 13},
  "Q10": {"investment_grade": "depends"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06"]},
  "Q19": {"issuers": ["E01", "E09"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": 6},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E15"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E11", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 15},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 6},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "ambiguous (DE or LU)"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "depends"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "depends"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```