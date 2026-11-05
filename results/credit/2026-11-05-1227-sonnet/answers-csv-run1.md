**Q1.** A-. A01 assigned A- on 2024-03-12 and A02 did not downgrade until 2025-06-20.
**Q2.** No. The only 2026 action on Kestrel (E01) is A03, an affirmation at BBB with the outlook moved to Negative.
**Q3.** No, it is BB+. I02 was cut to BB+ by A07 on 2025-06-20, below investment grade.
**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.
**Q5.** A holder takes the risk of Northwind Holdings (E02), the guarantor of I03, rated A (A09 via E03, same LEI).
**Q6.** The data points to the Country Ceiling. VD's ceiling is BB (A12), so the foreign-currency rating is BB (A14) while the local-currency rating is BBB- (A13).
**Q7.** E08, E10 and E16. E08 had A21 and A22, E10 had A27, and E16 had A44; A29 is an instrument downgrade and A17 is only a watch.
**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.
**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), and VD has only a Country Ceiling, not an issuer rating.
**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).
**Q11.** BBB+. A36 downgraded it on 2024-09-30, and A35 on 2025-11-20 was only a watch.
**Q12.** A-. A34 assigned it on 2023-01-15.
**Q13.** 1. Only A36 is a downgrade for E14.
**Q14.** None. E12's first rating is A30, dated 2024-02-01.
**Q15.** A-. E17 shares E10's LEI, and A26 set A- until A27 on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33).
**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative with the rating unchanged at A-.
**Q18.** E06. A17 is on watch; E14's watch (A35) was superseded by the affirmation A33 with no watch.
**Q19.** E01 (A03) and E09 (A25).
**Q20.** No. E07 was withdrawn for commercial reasons (A19), and there is no default rating.
**Q21.** E07, which was rated (A18) and then withdrawn (A19).
**Q22.** E08, which reached RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. The LTIDR is BBB (A03).
**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 expired (A47).
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. Valdoria (VD) has only a Country Ceiling of BB (A12), which is not an issuer rating.
**Q30.** E05 and E15. E05's foreign-currency BB equals VD's ceiling of BB, and E15's foreign-currency A equals CV's ceiling of A (A37).
**Q31.** No. E05 and E15 are exactly at their ceilings, and no other country has a ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** A holder takes the risk of Halden Bank (E10), the guarantor of I05, rated BBB+ (A27).
**Q34.** No. E12 has no parent and no link to E09 or E10.
**Q35.** 3: E09, E10 and E11. E17 duplicates E10.
**Q36.** 2: E02 and E04. E03 duplicates E02.
**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).
**Q38.** No. They have different LEIs and countries (DE vs US), and no link in the data.
**Q39.** A (A09, via E03 with the same LEI).
**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.
**Q41.** BB+ (A44).
**Q42.** DE. The RATINGS record E10 says DE; the RESEARCH duplicate E17 says LU, which conflicts, and I treated the RATINGS record as authoritative.
**Q43.** 0. The only LU record is E17, a duplicate of E10, so I did not count it as a separate LU entity. Counting records rather than entities would give 1.
**Q44.** Yes. The currency XVD appears to be Valdoria's own currency, which is inferred from the code and not stated in the data. Its BBB- rating (A45) matches E05's local-currency rating (A13).
**Q45.** No. The ceiling applies to foreign-currency ratings, and this is a local-currency note.
**Q46.** No. E11 has only a CO-type rating (A46), not an issuer rating.
**Q47.** None. I08's rating expired on 2026-09-01 (A47).
**Q48.** 7, which is I01 to I07. I08 expired.

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