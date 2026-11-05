**Q1.** A-. The rating from A01 (2024-03-12) holds until A02 (2025-06-20), which downgraded it to BBB.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, rated BB+. I02 (the 2031 SUB note) was downgraded to BB+ by A07 (2025-06-20).

**Q4.** Positive. E02 and E03 are the same entity (same LEI), and the latest action is A09 (2025-09-15, outlook POS).

**Q5.** The holder takes Northwind Holdings' credit risk (E02), since E04 is a finance subsidiary guaranteed by E02. I03 is rated A (A11).

**Q6.** Valdoria Telecom's FC rating (E05, BB, A14) is capped by the Valdorian Country Ceiling (VD, BB, A12), while its LC rating (BBB-, A13) is not capped because local-currency ratings are exempt from the ceiling.

**Q7.** E08 (Saxby Shipping, A21 and A22) and E10 (Halden Bank, A27). The 2026 instrument downgrade (A29) is excluded because it concerns I05, not an issuer.

**Q8.** E08. Its RD rating from A22 (2026-07-08) is a default.

**Q9.** 12. The issuers with an LTIDR or STIDR on 2026-10-01 are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. Excluded: E07 (withdrawn), E04 and E11 (no issuer rating), VD (only a ceiling), and QA record E16.

**Q10.** No. The headline FC rating is BB (A14); the LC rating is BBB- (A13), which is investment grade, so the answer depends on which rating you treat as headline.

**Q11.** BBB+. A36 (2024-09-30) set BBB+, and no action came before 2025-06-01 (A35 is 2025-11-20).

**Q12.** A-. A34 (2023-01-15) is the latest action on or before 2024-01-01; A36 came later.

**Q13.** 1. E14 has one downgrade, A36 (2024-09-30). A35 is a Watch placement, not a downgrade.

**Q14.** None. The first rating for E12 is A30 (2024-02-01), after 2024-01-01.

**Q15.** A-. The 2026 downgrade (A27) came after 2026-01-01, so A26 (2023-05-01) still held.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now; A35 and A33 changed the watch and outlook, not the rating.

**Q17.** No. A17 (2026-09-03) is a Rating Watch placement, not a downgrade.

**Q18.** E06. Only A17 carries RWN. A35's RWN on E14 was cleared by A33 (2026-05-01), which has no watch set.

**Q19.** E01 (A03, NEG) and E09 (A25, NEG). Every other outlook on 2026-10-01 is STA or POS, or is unset by a non-outlook action.

**Q20.** No. E07 withdrew its rating (A19), and a withdrawal is not a credit event. No default action is recorded.

**Q21.** E07, which had a rating until its withdrawal (A19, 2026-05-12). E11 is excluded because its only action is a credit opinion (A46), which is not an issuer rating.

**Q22.** E08, which is the only entity with an RD action (A22).

**Q23.** F2. The short-term rating is from A04 (2026-02-10).

**Q24.** Yes. Its LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I08 is only an expected rating (EX, A47), so it is not rated.

**Q26.** A+. This is E15's LC rating from A40 (2024-03-01).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. This is CV's LTIDR FC from A38 (2024-01-01).

**Q29.** None. VD has only a Country Ceiling (A12), which is not a sovereign's issuer rating.

**Q30.** E05 (FC BB, equal to the VD ceiling BB) and E15 (FC A, equal to the CV ceiling A).

**Q31.** No. Both companies domiciled in ceiling countries (E05 and E15) are exactly at their ceilings, not above.

**Q32.** E09. Halden Leasing (E11) → Halden Bank (E10) → Halden Group (E09), which has no parent.

**Q33.** The holder takes Halden Bank's credit risk (E10), because I05 is guaranteed by E10. I05 is rated BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no parent link and is its own group, separate from the Halden Group.

**Q35.** 3. The group is E09, E10 (Halden Bank, also recorded as E17) and E11.

**Q36.** 2. The group is E02 (also recorded as E03) and E04.

**Q37.** 16. There are 18 non-QA records, and E03 and E17 duplicate E02 and E10 by LEI. Sovereigns (VD, CV) count as entities.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 for E06 and 815600O8X8K2F154N214 for E13).

**Q39.** A. The latest action for E02/E03 is A09 (2025-09-15, affirmed).

**Q40.** 5. The GB issuers with an issuer rating on 2026-10-01 are E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA record, so it is ignored.

**Q42.** LU. RESEARCH (E17) holds for domicile, so Halden Bank is in Luxembourg, not Germany.

**Q43.** 1. Only Halden Bank (E10/E17) is domiciled in LU.

**Q44.** Yes. The note is in XVD, the domestic currency of Valdoria (VD).

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap, even though its BBB- rating is numerically above the BB ceiling.

**Q46.** No. The only action on E11 is a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (EX, A47), and it stays unrated until an AS action.

**Q48.** 7. I01, I02, I03, I04, I05, I06 and I07 are rated; I08 is not.

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
  "Q10": {"investment_grade": "no"},
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