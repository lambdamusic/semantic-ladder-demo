**Q1.** A-, long-term issuer rating (A01, 2024-03-12, the latest rating before 2025-01-01).

**Q2.** No. The only 2025 downgrade is A02 (BBB, 2025-06-20), and the 2026 actions (A03, A04) are affirmations.

**Q3.** No, rated BB+. I02 was cut from BBB to BB+ (A23 → A07, 2025-06-20).

**Q4.** Stable (STA), per A08 (E02, 2023-11-01). E03 shares E02's LEI and has a Positive outlook (A09), so the data conflicts here.

**Q5.** Northwind Finance BV (E04), which issues I03. I03 is guaranteed by E02, and its rating is A (A11, 2025-09-15).

**Q6.** The data doesn't say why. E05 has LC BBB- (A13) and FC BB (A14), and the Valdoria country ceiling is BB (A12), which would fit a cap on the FC rating, but the cause isn't stated. Q6 has no JSON field in the spec, so it is omitted below.

**Q7.** E08 (A21, A22), E10 (A27), and E16 (A44) were downgraded in 2026. E11 is included only because its instrument I05 was downgraded (A29), and its issuer-level rating was not.

**Q8.** E08, which was rated RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV hold LTIDR/STIDR ratings; E03 duplicates E02's LEI, so it is not counted again.

**Q10.** Depends on currency. The local-currency rating is BBB- (IG, A13), but the foreign-currency rating is BB (not IG, A14).

**Q11.** BBB+. The last DG was A36 (BBB+, 2024-09-30), and the RW (A35, 2025-11-20) came later.

**Q12.** A-, per A34 (2023-01-15).

**Q13.** 1. The only downgrade is A36 (A- to BBB+, 2024-09-30); A35 is a watch placement, not a downgrade.

**Q14.** None. E12's first action is A30 (BB-, 2024-02-01), after 2024-01-01.

**Q15.** A-. E10 (Halden Bank AG) had A26 (A-, 2023-05-01) until A27 (2026-04-15). E17 shares E10's LEI but has no ratings.

**Q16.** No. The rating stayed at BBB+ (A36, A35, A33), though a Rating Watch Negative was added on 2025-11-20 (A35).

**Q17.** No. E06 (Orrin Bank AG) had no 2026 downgrade; A17 (2026-09-03) is a Rating Watch Negative.

**Q18.** E06, via A17 (RWN, 2026-09-03). E14's watch (A35) was superseded by the affirmation A33 (2026-05-01), which carries no watch.

**Q19.** E01 (A03, NEG) and E09 (A25, NEG). These are the only NEG outlook records.

**Q20.** No. E07's latest action is a withdrawal (A19, WD, 2026-05-12), not a default.

**Q21.** E07, whose rating was withdrawn (A19). E11 and VD have only non-issuer types (CO and CC), so I did not count them.

**Q22.** E08, which was rated RD (A22). No other entity has an RD or D rating.

**Q23.** F2, the short-term rating (A04, 2026-02-10).

**Q24.** Yes. The issuer rating is BBB (A03, 2026-02-10), which is IG.

**Q25.** 6. The IG-rated instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A). I08's action code EX is not defined in the data.

**Q26.** A+, the LC rating (A40, 2024-03-01).

**Q27.** A-, per A42 (I06, 2024-03-01).

**Q28.** BBB+. CV's FC issuer rating is A38 (BBB+, 2024-01-01).

**Q29.** None. The only VD record is A12, a country ceiling (type CC, BB), which is not an issuer rating.

**Q30.** E05 (FC BB, A14, against the VD ceiling BB in A12) and E15 (FC A, A41, against the CV ceiling A in A37).

**Q31.** No, on the data available. Ceilings exist only for VD and CV, and neither company is above its ceiling. Companies in other countries cannot be checked because no ceilings are given for them.

**Q32.** E09 (Halden Group plc). E11 → E10 → E09.

**Q33.** E11 (Halden Leasing SA), which is the issuer of I05. I05 is guaranteed by E10, and its rating is BBB+ (A29, 2026-04-15).

**Q34.** No. E12 has no parent and no shared LEI with E10 or E17; only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 has E10's LEI, so it is not counted separately, and it has no parent link to E09.

**Q36.** 2: E02 and E04. E03 shares E02's LEI.

**Q37.** 17. There are 19 entity records (including the sovereigns VD and CV), but E03 duplicates E02 and E17 duplicates E10 by LEI.

**Q38.** No. The LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214), and so do the countries (DE vs US).

**Q39.** A. Both E02 (A08) and E03 (A09) are rated A.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is GB but withdrawn, and E03 duplicates E02.

**Q41.** BB+, per A44 (2026-06-01).

**Q42.** DE, per E10 (Halden Bank AG). E17, which has the same LEI, is listed as LU, so the data conflicts.

**Q43.** 1 (E17, LU). That record shares E10's LEI, so it may be the same legal entity as E10 (DE), in which case the count would be 0.

**Q44.** Depends. I07 has currency XVD, which is not defined in the data as Valdoria's local currency, and no ccyBasis is given.

**Q45.** Depends. I07 is rated BBB- (A45), above the VD ceiling of BB (A12). That is only a breach if the note is foreign-currency, which Q44 cannot settle.

**Q46.** No. E11's only rating is A46, of type CO, which the data does not define as an issuer type; the issuer types are LTIDR and STIDR.

**Q47.** A, per A47 (I08, 2026-09-01). The action code EX is not defined in the data.

**Q48.** 8. All eight instruments (I01–I08) have a rating on 2026-10-01.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "STA"},
  "Q5": {"risk_of": "E04", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E11", "E16"]},
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
  "Q37": {"count": 17},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 6},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "depends"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```