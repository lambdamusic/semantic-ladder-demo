**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. The only 2026 actions on Kestrel are affirmations (A03, A04); its downgrade was in 2025 (A02).

**Q3.** No, it is rated BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (2025-09-15) with a POS outlook.

**Q5.** The holder takes the risk of the guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (instruments.csv), and E02/E03 is rated A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating of BBB- (A13) is not capped by it.

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21, A22, A27, A44). I05's downgrade (A29) is an instrument rating, not an issuer rating for E11.

**Q8.** E08. It was downgraded to RD (restricted default) on 2026-07-08 (A22) and has no later action.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. E07 is excluded because its rating was withdrawn (A19). VD has only a Country Ceiling and E11 only a CO rating, so neither counts as an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. Marlow was downgraded to BBB+ on 2024-09-30 (A36), and that was still in force on 2025-06-01.

**Q12.** A-. This is from A34 (2023-01-15), before the A36 downgrade.

**Q13.** 1. The only downgrade is A36; the others are an assignment, an affirmation and a watch (A34, A33, A35).

**Q14.** None. Halden Foods' first rating was assigned 2024-02-01 (A30).

**Q15.** A-. Halden Bank (E10, with E17 as a duplicate by LEI) was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. Marlow was BBB+ on 2025-01-01 (A36) and is still BBB+ (A35, A33).

**Q17.** No. The only 2026 action on Orrin Bank is a Rating Watch Negative (A17), with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation with no watch on 2026-05-01 (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19) and it has no default rating.

**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. Kestrel's LTIDR is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) qualify. I02 and I04 are below investment grade, and I08 had an EX action on 2026-09-01.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. The sovereign has only a Country Ceiling record (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling (A14, A12), and E15's is A, equal to Corvenia's ceiling (A41, A37).

**Q31.** No. No company's FC rating is above its country's ceiling; the two with ceilings are exactly at them.

**Q32.** E09 (E11 → E10 → E09).

**Q33.** The holder takes the risk of the guarantor, Halden Bank (E10), rated BBB+ (A27). I05 is guaranteed by E10.

**Q34.** No. E12 has no parent link and a different LEI from the Halden Group / Halden Bank chain.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs); sovereigns are counted.

**Q38.** No. They have different LEIs, countries and entity IDs (E06 and E13), with no link between them.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 is the primary RATINGS record. E17 is a RESEARCH duplicate (same LEI) that conflicts with it on country (LU), so E10's DE is used.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is in DE; if the E17 country were trusted instead, it would be 1.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's currency, and its BBB- matches the local-currency rating (A13, A45). The data does not define XVD explicitly.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency instrument.

**Q46.** No. E11 has only a CO rating (A46), not an issuer rating.

**Q47.** None. I08's only action is EX on 2026-09-01 (A47), which I read as the rating no longer being held; the data does not define EX.

**Q48.** 7: I01–I07. I08 is excluded under the same reading of EX.

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
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```