**Q1.** A-. A05/A01 assigned A- on 2024-03-12, and the next action (A02) came on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the downgrade (A02) was in 2025.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action, with a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and the latest E02/E03 rating is A (A09).

**Q6.** The data doesn't state a reason. It does show the Valdoria country ceiling (VD, A12) at BB, equal to the foreign-currency rating of E05 (A14), while the local-currency rating is BBB- (A13), which is consistent with a ceiling cap.

**Q7.** E08, E10 and E16. Their downgrades are A21/A22, A27 and A44. I05's 2026 downgrade (A29) is an instrument action, and E11 has no issuer rating.

**Q8.** E08. A22 put it at RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), E11 has only a CO rating, VD has only a country ceiling, and E03 duplicates E02.

**Q10.** Depends. The foreign-currency rating is BB (A14), which is sub-investment grade, while the local-currency rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. A36 downgraded it to BBB+ on 2024-09-30, and A35 (2025-11-20) is later than 1 June 2025.

**Q12.** A-, from A34 (2023-01-15), before the 2024-09-30 downgrade.

**Q13.** 1, which is A36.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in A26, and the downgrade (A27) came on 2026-04-15. E17 is the same LEI.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33), and the 2025 watch (A35) was resolved by that affirmation.

**Q17.** No. The only 2026 action on E06 is a Rating Watch Negative at A- (A17), which is not a downgrade.

**Q18.** E06 (A17). E14's watch (A35) was superseded by the affirmation in A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 was withdrawn for commercial reasons (A19) and never rated in default.

**Q21.** E07, withdrawn by A19.

**Q22.** E08, which went to RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. Its BBB rating (A03) is investment grade.

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling (A12), not an issuer rating.

**Q30.** E05 (BB, equal to the Valdoria ceiling of BB) and E15 (A, equal to the Corvenia ceiling of A). Only these two countries have ceilings in the data.

**Q31.** No. E05 and E15 are at their ceilings, not above them (A12/A14, A37/A41).

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ (A27).

**Q34.** No. E12 has no parent link and a different LEI, so the data doesn't connect it to the Halden group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries and names (E06 and E13).

**Q39.** A (A09, affirmed 2025-09-15 on E03, the same entity as E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 says DE, and E17 (LU) is a RESEARCH-sourced duplicate by LEI.

**Q43.** 0. The only LU record is E17, which resolves to E10 in DE.

**Q44.** Depends. I07's currency is "XVD", which the data does not define, so it can't be confirmed as Valdoria's local currency.

**Q45.** Depends. I07 is rated BBB- (A45) against a BB ceiling (A12), but whether the ceiling applies depends on the undefined XVD currency.

**Q46.** No. E11 has only a CO-type rating (A46), not an issuer default rating.

**Q47.** None. A47 shows the rating expired on 2026-09-01.

**Q48.** 7: I01 to I07. I08 expired.

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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "depends"},
"Q45": {"above_ceiling": "depends"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```