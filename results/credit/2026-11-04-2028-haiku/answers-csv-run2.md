**Q1.** A-. Kestrel Energy's LTIDR (FC) was A- from A01 (2024-03-12) until it was downgraded to BBB by A02 (2025-06-20).

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04), and the 2026 downgrade-type records on other entities do not involve E01.

**Q3.** No, rated BB+. I02 was assigned BBB (A23), then downgraded to BB+ (A07, 2025-06-20), which is below investment grade.

**Q4.** POS, but the data conflicts. The RATINGS record E02 shows STA (A08, 2023-11-01), while E03 (same LEI, RESEARCH source) shows POS (A09, 2025-09-15), the later record.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is guaranteed by E02 (guarantor_id), and I03 is rated A (A11).

**Q6.** The foreign-currency rating is capped by Valdoria's country ceiling of BB (A12, rating type CC), while the local-currency rating BBB- (A13) is not subject to that cap. The data doesn't state the mechanism explicitly, so this rests on the meaning of CC.

**Q7.** E08 (DG to CCC on 2026-01-20, then DG to RD on 2026-07-08), E10 (DG to BBB+ on 2026-04-15), and E16 (DG to BB+ on 2026-06-01). The 2026 downgrade of I05 (A29) is on an instrument of E11, not E11's issuer rating, so E11 is excluded.

**Q8.** E08, which was moved to RD (restricted default) by A22 on 2026-07-08.

**Q9.** 13. Entities with an active LTIDR on that date are E01, E02 (E03 is the same LEI), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16, and the sovereign CV. E07 was withdrawn (A19), and VD and E04 have no LTIDR.

**Q10.** Depends on currency basis. LC rating is BBB- (A13), which is investment grade, while FC rating is BB (A14), which is not.

**Q11.** BBB+. E14 was downgraded to BBB+ by A36 (2024-09-30), and the next action (A35, 2025-11-20) was a watch placement with no rating change.

**Q12.** A-, from A34 (2023-01-15), which was in force until A36 (2024-09-30).

**Q13.** Once. A36 (2024-09-30) is the only DG action on E14 (A33 and A35 are affirmation and watch actions).

**Q14.** None. E12's first rating is A30 (BB-, 2024-02-01), which is after 2024-01-01.

**Q15.** A-. E10 was A- from A26 (2023-05-01), and the downgrade to BBB+ came later (A27, 2026-04-15).

**Q16.** No. The rating stayed BBB+ (A36, then A33 affirmation). A35 placed the rating on watch but did not change it.

**Q17.** No. Orrin Bank AG (E06) was placed on Rating Watch Negative (A17, 2026-09-03), but its A- rating was not changed.

**Q18.** E06 only. A17 placed it on watch with no resolution by 2026-10-01. E14's watch from A35 appears resolved by A33 (2026-05-01), which has a blank watch field.

**Q19.** E01 (NEG, A03, 2026-02-10) and E09 (NEG, A25, 2026-03-01). No later actions changed either outlook.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of default.

**Q21.** E07. Its rating was withdrawn by A19 (2026-05-12). E11 is excluded because its only record is type CO, which the data does not define as an issuer rating.

**Q22.** E08, the only entity with an RD rating (A22).

**Q23.** F2. This is the STIDR assigned by A04 (2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 6. Investment-grade instruments on 2026-10-01 are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-), and I08 (A). I02 (BB+) and I04 (BB) are not.

**Q26.** A+. E15's local-currency rating is A+ (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. CV's FC LTIDR is BBB+ (A38).

**Q29.** None. VD has only a country ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 (FC BB, A14, equal to the Valdoria ceiling of BB) and E15 (FC A, A41, equal to the Corvenia ceiling of A, A37).

**Q31.** No. The only ceilings are for VD and CV, and neither company is above its ceiling. Other countries have no ceiling records, so they can't be assessed.

**Q32.** E09 (Halden Group plc). Halden Leasing (E11) is owned by Halden Bank AG (E10), which is owned by E09.

**Q33.** The guarantor, Halden Bank AG (E10), rated BBB+ (A27). I05 is guaranteed by E10, and its BBB+ rating (A29) matches E10's.

**Q34.** No. E12 has no parent_id, and E09 is not linked to it. The shared "Halden" name is not evidence of a group link in this data.

**Q35.** 3: E09, E10, and E11. E17 shares E10's LEI, so it is the same entity.

**Q36.** 2: E02 and E04. E03 shares E02's LEI.

**Q37.** 17. There are 19 records, and E03 and E17 duplicate E02 and E10 by LEI. Excluding the two sovereigns (VD, CV), which have no LEI, gives 15.

**Q38.** No. They have different LEIs, countries (DE vs US), and no parent link.

**Q39.** A. Both E02 (A08) and E03 (A09) give A.

**Q40.** 6: E01, E02, E09, E12, E14, E16. Each is GB-domiciled with an active LTIDR. E07 (GB) was withdrawn.

**Q41.** BB+, from A44 (2026-06-01).

**Q42.** DE, per E10. E17 gives LU for the same LEI, so the record conflicts.

**Q43.** 0. The only LU record (E17) shares its LEI with E10, which is domiciled in DE. If E17 is taken at face value, the answer would be 1.

**Q44.** Yes, inferred. I07's currency is XVD, which appears to be Valdoria's local currency, and I07 is rated BBB-, matching the LC rating (A13) rather than the FC rating. The data does not define XVD explicitly.

**Q45.** No. BBB- is above the BB ceiling, but ceilings cap FC ratings. Since I07 is treated as local currency (Q44), it is not capped.

**Q46.** No. E11 has no LTIDR. Its only record is a CO action (A46), and CO is not defined as an issuer rating.

**Q47.** A, from A47 (2026-09-01). The meaning of the EX action code is not defined, so this assumes the rating remains in force.

**Q48.** 8. All instruments I01–I08 have a rating on 2026-10-01.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
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
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 17},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 6},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 0},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```