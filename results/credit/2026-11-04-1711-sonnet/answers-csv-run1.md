**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02) came in June 2025.

**Q2.** No. The only 2026 actions on Kestrel Energy (E01) are affirmations at BBB (A03, A04).

**Q3.** No, BB+. I02 was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02, and A09 gives E02's latest rating as A.

**Q6.** The data doesn't say. A13 (LC BBB-) and A14 (FC BB) have no comment, and A12 only shows a Valdoria country ceiling of BB.

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44 respectively.

**Q8.** E08. It was rated RD on 2026-07-08 (A22).

**Q9.** 13. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07's rating was withdrawn, and E04, E11 and VD have no LTIDR.

**Q10.** Depends. The local-currency rating is BBB- (investment grade) and the foreign-currency rating is BB (not) (A13, A14).

**Q11.** BBB+. The downgrade in A36 (2024-09-30) predates this date, and the next action is A35 in November 2025.

**Q12.** A-. A34 assigned A- on 2023-01-15, before A36.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods was first rated on 2024-02-01 (A30).

**Q15.** A-. E17 shares E10's LEI, and A26 gave A- until the downgrade in A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33). A35 only placed it on watch, and A33 affirmed the rating.

**Q17.** No. A17 (2026-09-03) is a Rating Watch action with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch from A35 was resolved by A33 on 2026-05-01.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam Retail (E07) was last rated BB, and its rating was withdrawn for commercial reasons (A19).

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. Its LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has only a country ceiling (BB, A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB against a VD ceiling of BB (A14, A12), and E15's is A against a CV ceiling of A (A41, A37).

**Q31.** No. Only E05 and E15 have ceilings in the data, and both are at their ceiling, not above it.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 gives its current rating.

**Q34.** No. E12 has no parent link to E09 or E10, and the shared name isn't evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A (A09, via E03, which shares E02's LEI).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU. I took the RATINGS record as authoritative.

**Q43.** 0. The only LU record is the duplicate E17, which I treated as E10 (DE).

**Q44.** Yes, probably. I07 is in XVD, which the data doesn't define, but it appears to be Valdoria's currency, and its BBB- matches the LC rating in A13.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 appears to be local-currency.

**Q46.** No. E11 has only a "CO" rating type (A46), which the data doesn't define, and no LTIDR.

**Q47.** None. A47 shows the rating expired on 2026-09-01.

**Q48.** 7. These are I01–I07, and I08 has expired.

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