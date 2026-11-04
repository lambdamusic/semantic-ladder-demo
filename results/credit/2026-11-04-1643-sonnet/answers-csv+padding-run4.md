**Q1.** A-. A01 assigned E01 A- on 2024-03-12, and the next action is A02 in 2025-06.

**Q2.** No. E01's only 2026 actions are A03 and A04, and both are affirmations.

**Q3.** No, it is BB+. I02 was cut from BBB (A23) to BB+ (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action with outlook POS.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 and guaranteed by E02, and E02's latest rating is A (A09 via E03).

**Q6.** The data does not state a reason. It is consistent with the country ceiling: VD's CC is BB (A12), and E05's foreign-currency rating is BB (A14) against BBB- local currency (A13).

**Q7.** E08, E10 and E16 (A21, A22, A27, A44). I05's downgrade (A29) is an instrument rating, and E11 has no issuer rating.

**Q8.** E08, which was rated RD from 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV, E15 and E16. E07 is withdrawn, E04 and E11 have no issuer rating, and VD has only a country ceiling.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and A35 only adds a watch afterwards.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. A26 applies to E10, and E17 is a duplicate of E10 by LEI. The downgrade A27 came later, on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). The 2025 watch (A35) did not change the rating.

**Q17.** No. A17 is only a Rating Watch Negative on E06 at A-, with no downgrade. E13, Orrin Bancorp, is a different entity.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, through the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB, and E15's A equals CV's ceiling of A (A37).

**Q31.** No. E05 and E15 sit exactly at their ceilings and no other company has a ceiling on file.

**Q32.** E09. The chain is E11, then E10, then E09.

**Q33.** E10, the guarantor of I05, rated BBB+ (A27).

**Q34.** No. E12 has no parent link to the Halden group (E09, E10, E11) and only shares a name prefix and a different LEI.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs). The two sovereigns are counted.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A, from the latest action A09 (via E03).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn and E10 is domiciled in DE.

**Q41.** BB+, from the downgrade A44. E16's source system is QA, so it may be unverified.

**Q42.** DE. E10's primary record says DE. The duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, which is a duplicate of E10, and E10's primary record says DE, so this depends on which record you trust.

**Q44.** Yes, with an assumption. I07 is in XVD, which looks like Valdoria's currency. The data does not define it, but the BBB- rating matches E05's local-currency rating (A13).

**Q45.** No. The ceiling of BB constrains foreign-currency ratings, and I07 is a local-currency obligation rated BBB- (A45).

**Q46.** No. E11 has only a CO-type rating (A46). Its I05 notes rely on E10's guarantee.

**Q47.** None. A47 shows I08's rating expired on 2026-09-01.

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