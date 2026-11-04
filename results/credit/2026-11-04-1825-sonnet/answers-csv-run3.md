**Q1.** A-. A01 assigned A- on 2024-03-12, and A02 did not lower it until 2025-06-20.

**Q2.** No. The only 2026 Kestrel issuer actions are A03 and A04, which are affirmations (AF).

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07, so it is sub-investment grade.

**Q4.** Positive. A09 (2025-09-15) is on E03, which shares E02's LEI, so I treat it as the same entity. It supersedes the Stable outlook in A08.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02, and A11 rates the notes A.

**Q6.** The data doesn't state the cause. The foreign-currency rating is BB (A14), equal to Valdoria's Country Ceiling of BB (A12). The local-currency rating is BBB- (A13), so the ceiling plausibly caps the foreign-currency rating.

**Q7.** E08, E10 and E16. They were downgraded by A21/A22, A27 and A44. The I05 downgrade (A29) is an instrument action, and A17 is a watch, not a downgrade.

**Q8.** E08. A22 moved it to RD on 2026-07-08.

**Q9.** 13. The issuers are E01, E02 (E03 is the same LEI), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn, E04 and E11 have no LTIDR, and VD has only a country ceiling.

**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade. The foreign-currency rating is BB (A14), which is not.

**Q11.** BBB+. A36 downgraded it from A- on 2024-09-30. The RWN in A35 came later and did not change the rating.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Its first rating is A30, on 2024-02-01.

**Q15.** A-. A26 is the rating on 2026-01-01, and E17 is the same LEI. The downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33). The 2025 watch (A35) was later cleared.

**Q17.** No. A17 is a Rating Watch Negative with the rating kept at A-, not a downgrade.

**Q18.** E06 (A17). E14's watch from A35 was resolved by the affirmation in A33.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. A19 withdrew its rating for commercial reasons, and the last rating was BB with no default status.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08. It was downgraded to RD in A22 after a distressed debt exchange.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country-ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB (A14), equal to VD's ceiling of BB. E15's is A (A41), equal to CV's ceiling of A (A37).

**Q31.** No. The two companies with ceilings, E05 and E15, are at their ceilings, not above them.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 puts E10 at BBB+.

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, minus E03 (same LEI as E02) and E17 (same LEI as E10).

**Q38.** No. They have different LEIs, countries (DE and US) and records.

**Q39.** A (A08 and A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 says DE and E17 says LU, but both share an LEI. I treat E10, from the RATINGS system, as authoritative, but the data conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of the DE-domiciled E10.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's currency, though the data does not define it.

**Q45.** No. I07 is BBB- (A45), above the BB ceiling, but the ceiling applies to foreign-currency obligations and I07 is local-currency.

**Q46.** No. E11 has only a "CO" record (A46), which is not an issuer-rating type like LTIDR. Only its notes (I05) are rated.

**Q47.** None. A47 shows the rating expired (EX) on 2026-09-01, although the maturity is 2034, which is odd.

**Q48.** 7: I01 to I07. I08's rating expired.

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