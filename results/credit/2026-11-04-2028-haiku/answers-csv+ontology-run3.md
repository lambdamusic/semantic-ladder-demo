**Q1.** A-. A01 (2024-03-12) is the latest action on or before 2025-01-01; the downgrade in A02 came later.

**Q2.** No. The 2026 actions on E01 (A03, A04) are affirmations, and A03 is at BBB with a Negative outlook.

**Q3.** No, rated BB+. I02 was downgraded from BBB (A23) to BB+ (A07), which is speculative grade.

**Q4.** Positive (POS). E02 and E03 are the same entity (same LEI), and the latest outlook is set by A09 (2025-09-15).

**Q5.** Northwind Holdings (E02), rated A. I03's guarantor is E02, so holders take E02's credit risk, and the instrument rating is A (A11).

**Q6.** The Valdoria Country Ceiling caps foreign-currency ratings, and the ceiling is BB (A12). E05's FC rating (A14) is BB, at that cap, while its local-currency rating (A13, BBB-) is not capped under the ontology's definition of lad:basis-LC.

**Q7.** E08 and E10. A21 and A22 downgrade E08 in 2026, and A27 downgrades E10 (Halden Bank).

**Q8.** E08. Its latest action is A22 (2026-07-08), which sets RD, a default.

**Q9.** 12. E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV hold an issuer rating on that date. E07 is withdrawn (A19), E11 holds only a credit opinion (A46), and E16 is QA data.

**Q10.** Depends. The FC headline rating is BB (A14), which is not investment grade, but the LC rating is BBB- (A13), which is. The question doesn't say which basis it means.

**Q11.** BBB+. A36 (2024-09-30) is the latest action on or before 2025-06-01; A35 came later.

**Q12.** A-. A34 (2023-01-15) is the latest action before 2024-01-01; the downgrade A36 came later.

**Q13.** 1. E14 has one downgrade (A36); A35 is a Rating Watch, which is not a downgrade.

**Q14.** None. E12's first rating is A30 (2024-02-01), after 1 January 2024.

**Q15.** A-. E10 and E17 are the same entity, and A26 is the latest action on or before 2026-01-01; the downgrade A27 came later.

**Q16.** No. The rating on 2025-01-01 was BBB+ (A36), and the later actions (A35 Rating Watch, A33 affirmation) left it at BBB+.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) places it on Rating Watch Negative, and no later action clears it. E14's watch from A35 was cleared by the affirmation in A33, which has no watch flag.

**Q19.** E01 and E09. A03 (NEG) and A25 (NEG) are the latest outlook-setting actions for those issuers.

**Q20.** No. E07 has a withdrawn rating (A19), and a withdrawal is not a credit event.

**Q21.** E07. It had a BB rating (A18) that was withdrawn (A19) and has no issuer rating on 1 October 2026. E11 never had an issuer rating, since A46 is a credit opinion.

**Q22.** E08. A22 sets RD, a default. No other entity has an RD or D action.

**Q23.** F2. A04 (2026-02-10) is the latest short-term action for E01.

**Q24.** Yes. E01's current long-term rating is BBB (A03), which is investment grade.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I08 has only an expected rating (EX), so it is unrated.

**Q26.** A+. E15's LC rating is A40 (2024-03-01).

**Q27.** A-. I06 is assigned A- (A42).

**Q28.** BBB+. CV's FC issuer rating is A38 (2024-01-01). A37 is a Country Ceiling, which is not an issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not the sovereign's own rating.

**Q30.** E05 and E15. E05 (domiciled in VD) has FC BB (A14), equal to the VD ceiling of BB (A12). E15 (domiciled in CV) has FC A (A41), equal to the CV ceiling of A (A37).

**Q31.** No. E05 (BB) and E15 (A) are exactly at their ceilings, and no other entity has a ceiling.

**Q32.** E09 (Halden Group plc). E11's parent is E10, whose parent is E09, which has no parent.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, so holders take E10's credit risk, and the instrument rating was downgraded to BBB+ (A29).

**Q34.** No. E12 has no parent link, and E10's group is E09, E10, E11. Name similarity isn't evidence of a group link.

**Q35.** 3. The Halden group is E09 (parent), E10 (Halden Bank, which includes E17) and E11.

**Q36.** 2. The Northwind group is E02 (which includes E03) and E04.

**Q37.** 16. There are 17 entity IDs, but E03 duplicates E02 and E17 duplicates E10 (same LEIs), and E16 is QA data to be ignored. The sovereigns VD and CV count as entities.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A. Northwind Holdings' latest FC long-term action is A09 (2025-09-15), which affirms A.

**Q40.** 5. E01, E02, E09, E12 and E14 are GB-domiciled with issuer ratings on that date. E07 is GB-domiciled but withdrawn, and E16 is QA data.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. E10 has DE in RATINGS, but E17 (RESEARCH) has LU, and RESEARCH holds for domicile.

**Q43.** 1. Only Halden Bank (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. BBB- is numerically above the BB ceiling (A12), but the ceiling only caps foreign-currency debt, and I07 is local-currency, so the ceiling doesn't apply to it.

**Q46.** No. E11 has only a credit opinion (A46), which the ontology says must never be counted as a rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating until an AS action.

**Q48.** 7. I01, I02, I03, I04, I05, I06 and I07 are rated on that date. I08 is unrated.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 12},
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
  "Q25": {"count": 5},
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
  "Q37": {"count": 16},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 5},
  "Q41": {"rating": "none"},
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```