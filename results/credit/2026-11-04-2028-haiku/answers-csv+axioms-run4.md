**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) until A02 downgraded it to BBB on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, BB+. I02 was BBB (A23), then downgraded to BB+ (A07, 2025-06-20).

**Q4.** Positive. E03 (the same entity as E02 by LEI) has A09 (2025-09-15) with outlook POS, which is the current LTIDR.

**Q5.** E02 (Northwind Holdings), rated A. I03's guarantor is E02, so E02 carries the credit risk, and its current LTIDR is A (A09).

**Q6.** The foreign-currency rating is capped by Valdoria's country ceiling. E05's FC rating is BB (A14), equal to the Republic of Valdoria's CC of BB (A12), while its LC rating is BBB- (A13) and not subject to that cap. The data doesn't state the reason explicitly; this is inferred from the ceiling rule.

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and then RD (A22), and E10 to BBB+ (A27). E16 (Brindle) is excluded because it is a QA test record and its actions aren't rating actions.

**Q8.** E08. Its RD rating (A22, 2026-07-08) is still in force on 1 Oct 2026.

**Q9.** 12. The issuers holding an in-force issuer rating are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 (withdrawn, A19), E11 (credit opinion only, A46) and E16 (QA) are excluded, and E03 is the same entity as E02. Including the sovereign CV is my reading of "issuer".

**Q10.** Depends. The LC rating is BBB- (A13), which is investment grade, but the FC rating is BB (A14), which is not.

**Q11.** BBB+. E14 was BBB+ from the DG on 2024-09-30 (A36), and the next action is RW on 2025-11-20 (A35), which does not change the rating.

**Q12.** A-. E14's A- was assigned on 2023-01-15 (A34) and was next changed on 2024-09-30 (A36).

**Q13.** Once. The only DG on E14 is A36 (2024-09-30); the RW and AF actions are not downgrades.

**Q14.** None. E12's first rating is BB- from 2024-02-01 (A30), after 1 Jan 2024.

**Q15.** A-. E10 (the same entity as E17) was A- from A26 until its change on 2026-04-15 (A27).

**Q16.** No. The rating stayed BBB+ (A36, then A35 and A33). The only change was a watch placement (A35, RWN) and an affirmation (A33).

**Q17.** No. E06's 2026 action is a Rating Watch placement (A17), not a downgrade.

**Q18.** E06. A17 (2026-09-03) placed E06 on RWN with no later resolving action. E14's RWN (A35) was followed by an affirmation with no watch flag (A33, 2026-05-01), so I treat it as resolved.

**Q19.** E01 and E09. Their current LTIDRs carry NEG: A03 for E01 and A25 for E09.

**Q20.** No. E07 has no RD or D rating, and its last action was a withdrawal (A19).

**Q21.** E07. It had BB (A18) and was withdrawn (A19). E11 never had an issuer rating (only a CO, A46), and E16 is a QA record.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. The short-term IDR for E01 was affirmed at F2 (A04, 2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I08 has only an expected rating (A47, EX), which is not in force, so it is excluded.

**Q26.** A+. E15's LC rating is A+ (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. CV's FC LTIDR is BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (CC) of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating BB (A14) equals Valdoria's CC of BB (A12), and E15's FC rating A (A41) equals Corvenia's CC of A (A37). Sovereigns are excluded from the ceiling check.

**Q31.** No. E05 and E15 are at their ceilings, not above, and no other entity has a ceiling in its country.

**Q32.** E09 (Halden Group plc). E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank AG), rated BBB+. I05's guarantor is E10, and its current LTIDR is BBB+ (A27).

**Q34.** No. Halden Foods (E12) has no parent link and a different LEI from Halden Bank (E10).

**Q35.** 3. The Halden group is E09, E10 and E11. E17 is a RESEARCH record for the same LEI as E10, so it is not counted separately.

**Q36.** 2. The Northwind group is E02 and E04. E03 is the same entity as E02 by LEI.

**Q37.** 16. The data has 19 records; excluding the QA record E16 leaves 18, and removing the duplicates E03 (= E02) and E17 (= E10) leaves 16. The two sovereigns (VD, CV) are included because they have no LEI and so are not merged.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. E02's current LTIDR is A (A09, recorded against E03).

**Q40.** 5. E01, E02, E09, E12 and E14 are GB-domiciled issuers with in-force issuer ratings. E07 has been withdrawn and E16 is a QA record.

**Q41.** None. Brindle (E16) is a QA test record, and its actions are not rating actions under the ontology, so it has no in-force rating even though A44 shows BB+.

**Q42.** LU. E10 is domiciled in LU through its same-entity RESEARCH record E17, even though E10's own country field says DE.

**Q43.** 1. Only E10 (E17 is the same entity) is domiciled in LU.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. The 2027 note is local-currency, and the CeilingShape constraint applies only to FC LTIDRs. Although BBB- is numerically above the BB ceiling, the ceiling does not cap it.

**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating of A (A47, EX), which is not in force.

**Q48.** 7. I01, I02, I03, I04, I05, I06 and I07 all have in-force ratings. I08 has only an expected rating and is excluded.

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