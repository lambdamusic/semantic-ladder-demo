**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action, A02, came on 2025-06-20.

**Q2.** No. Kestrel's only 2026 actions are the affirmations A03 and A04, both on 2026-02-10.

**Q3.** No. I02 is rated BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is a duplicate record of Northwind Holdings. A09 affirmed it at A with a POS outlook on 2025-09-15, later than A08.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02. The rating comes from A09, recorded under the duplicate E03.

**Q6.** The data points to the country ceiling. Valdoria's ceiling is BB (A12), the foreign-currency rating is capped at BB (A14), and the local-currency rating is BBB- (A13). The data states no reason beyond this.

**Q7.** E08, E10 and E16 had issuer-rating downgrades in 2026 (A21 and A22, A27, A44). E06's A17 is a watch, not a downgrade. I05's downgrade (A29) is an instrument rating.

**Q8.** E08. A22 moved it to RD on 2026-07-08 and nothing later supersedes it.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country ceiling (A12) and E11 only a CO record (A46), neither of which I counted as an issuer rating.

**Q10.** Depends. Valdoria Telecom's local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded Marlow from A- on 2024-09-30.

**Q12.** A-, assigned in A34 on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 an affirmation.

**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 assigned it in 2023, and the downgrade to BBB+ (A27) did not come until 2026-04-15. E17 is a duplicate of E10.

**Q16.** No. Marlow was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). The 2025 watch (A35) did not change the rating.

**Q17.** No. Orrin Bank's only 2026 action is A17, which placed it on Rating Watch Negative at an unchanged A-.

**Q18.** E06 (A17). E14's watch (A35) was followed by the affirmation A33, which carries no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 withdrew Pellam's rating for commercial reasons and there is no default rating.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08. A22 recorded RD, and no other record shows a default.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating was expired by A47 on 2026-09-01, so I excluded it.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 (FC BB against Valdoria's ceiling of BB) and E15 (FC A against Corvenia's ceiling of A). Only these two countries have ceilings in the data.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link to E09 and shares only the name.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and names.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE, per the RATINGS record E10. The RESEARCH duplicate E17 says LU, so the sources conflict.

**Q43.** 0. The only LU record is E17, a RESEARCH duplicate of E10, whose primary record says DE. If you trust E17, the answer would be 1.

**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency, and its BBB- matches the local-currency rating (A13). The data does not define XVD explicitly.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 has only a CO record (A46) and an instrument rating. The data does not define CO, so I did not treat it as an issuer rating.

**Q47.** None. A47 expired I08's rating on 2026-09-01.

**Q48.** 7. I01 to I07 are rated; I08 has expired.

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