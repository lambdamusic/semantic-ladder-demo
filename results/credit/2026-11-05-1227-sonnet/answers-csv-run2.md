**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed before 2025-06-20 (A02).

**Q2.** No. The only 2026 Kestrel action on the issuer is A03, an affirmation at BBB with a Negative outlook.

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07, which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), the guarantor of I03, which is rated A (A08, A09).

**Q6.** The data states no reason. Valdoria's Country Ceiling is BB (A12), and E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13), which is consistent with the ceiling capping it. That is an inference.

**Q7.** E08, E10 and E16. The 2026 downgrades are A21 and A22 (E08), A27 (E10) and A44 (E16). A17 is a watch action, not a downgrade. I05 (A29) was also downgraded, but it is an instrument, not an issuer.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and nothing later changes that.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and E04 and E11 have no issuer rating. VD has only a Country Ceiling (A12), which I did not count as an issuer rating.

**Q10.** It depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and A35 (2025-11-20) is later than the date asked.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. A36 is the only downgrade.

**Q14.** None. Halden Foods was first rated on 2024-02-01 (A30).

**Q15.** A-. E17 shares E10's LEI, so it is the same entity, and the downgrade to BBB+ (A27) came only on 2026-04-15.

**Q16.** No. It was BBB+ throughout. A35 was a watch, and A33 affirmed BBB+.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch Negative with the rating kept at A-.

**Q18.** E06 (A17). E14's earlier RWN (A35) was followed by an affirmation with no watch (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and no default rating exists.

**Q21.** E07, withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 is excluded under Q47.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12) and no issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB (A14) against a VD ceiling of BB, and E15's is A (A41) against a CV ceiling of A.

**Q31.** No. No foreign-currency rating exceeds its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of Halden Bank (E10), the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. E12 has no parent and no link to the E09 group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US), and neither is the other's parent.

**Q39.** A (A09, via E03, the same entity as E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE, per E10 from the RATINGS source. The RESEARCH duplicate E17 says LU, so the data conflicts, and I chose the RATINGS record.

**Q43.** 0. The only LU record is E17, which is a duplicate of the DE-domiciled E10.

**Q44.** Yes, with a caveat. I07 is denominated in XVD, which appears to be Valdoria's currency, but the data never states Valdoria's local currency.

**Q45.** No. I07 is rated BBB- (A45) and is a local-currency obligation, so the BB ceiling on foreign currency should not apply.

**Q46.** No. E11 has only a "CO" record (A46), whose meaning isn't defined, and no LTIDR.

**Q47.** None. A47 shows an "EX" action on 2026-09-01. I read this as the rating ending, but the data doesn't define the code.

**Q48.** 7: I01 through I07, with I08 excluded for the reason in Q47.

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