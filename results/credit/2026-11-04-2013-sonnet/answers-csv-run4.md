**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until the 2025-06-20 downgrade (A02).

**Q2.** No. The only 2026 actions on Kestrel are affirmations (A03, A04).

**Q3.** No, it is rated BB+. The 2031 note (I02) was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive (POS). E03 shares E02's LEI, so it is the same entity, and its A09 (2025-09-15) is the latest action, with POS outlook.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), the guarantor of I03, rated A. I03 is rated A (A11), and the guarantor's A rating comes from A08 and A09.

**Q6.** The data points to the country ceiling. Valdoria's Country Ceiling is BB (A12), and Valdoria Telecom's foreign-currency rating is BB (A14) against BBB- in local currency (A13). The data gives no explicit comment on the reason.

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21, A22, A27, A44). I counted issuer ratings only.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), E11 has only a "CO" row, and VD has only a country ceiling.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. Marlow was downgraded to BBB+ on 2024-09-30 (A36), and the watch added in A35 came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' first rating was on 2024-02-01 (A30).

**Q15.** A-. The downgrade to BBB+ came on 2026-04-15 (A27), after the date asked; the A- was assigned in A26.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A35, A33); only a watch was added and then resolved.

**Q17.** No. The only 2026 action on Orrin Bank is a Rating Watch Negative with the rating held at A- (A17).

**Q18.** E06 (A17). Marlow's earlier RWN (A35) was resolved by the 2026-05-01 affirmation with no watch (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and it was never rated in default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5: I01, I03, I05, I06 and I07. I02 and I04 are below investment grade, and I08 has expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB (A14, A12), and E15's A equals CV's ceiling of A (A41, A37).

**Q31.** No. No company's foreign-currency rating exceeds its ceiling, and only VD and CV have ceilings in the data.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the risk of the guarantor, Halden Bank (E10), rated BBB+ (A27). The issuer is E11, whose only rating row is a "CO" type; I05 itself is BBB+ (A29).

**Q34.** No. E12 has no parent and no link to E09 or E10 in the data.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10, going by shared LEIs.

**Q38.** No. They have different LEIs, countries and entity IDs (E06 and E13).

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44, downgraded from BBB-).

**Q42.** DE. The RATINGS record E10 says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record is in DE. If E17 were taken at face value the count would be 1.

**Q44.** Yes, inferred. I07 is in XVD, which appears to be Valdoria's currency, though the data does not define it.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a "CO" row (A46), not an LTIDR or STIDR.

**Q47.** None. I08 has an "EX" action on 2026-09-01 (A47), so I read it as expired. The code is not defined in the data.

**Q48.** 7: I01 to I07. I08 is no longer rated.

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