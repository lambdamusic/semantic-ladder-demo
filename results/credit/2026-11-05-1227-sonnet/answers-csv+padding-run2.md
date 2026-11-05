**Q1.** A-. A01 assigned A- to E01 on 2024-03-12, and it stayed until the downgrade A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), with the outlook moved to Negative.

**Q3.** No, BB+. I02 was downgraded to BB+ in A07, and it is subordinated.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action A09 (2025-09-15) gives POS.

**Q5.** E02, rated A. I03 is guaranteed by E02, and E02 is rated A via A08 and A09 (E03 is the same entity).

**Q6.** The data gives only the rating pattern. E05's foreign-currency rating is BB (A14) against BBB- local (A13), and VD's Country Ceiling is BB (A12). The foreign-currency rating is therefore at the ceiling, which fits the ceiling acting as a cap, though the data doesn't state that rule.

**Q7.** E08, E10 and E16 had issuer downgrades in 2026 (A21, A22, A27, A44). I05's downgrade (A29) is on an instrument, not an issuer rating.

**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. E05 is BBB- (investment grade) in local currency (A13) and BB (not investment grade) in foreign currency (A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30.

**Q12.** A-. A34 assigned A- on 2023-01-15.

**Q13.** 1, from A36.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 gave E10 A- in 2023, and E17 is the same LEI. The downgrade A27 came only in April 2026.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). The RWN in A35 was later cleared.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at an unchanged A- (A17).

**Q18.** E06 (A17). E14's watch (A35) was cleared by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 was withdrawn for commercial reasons (A19) and has no default rating.

**Q21.** E07, which was withdrawn in A19.

**Q22.** E08, because of the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08 had expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), not an issuer rating.

**Q30.** E05 (BB, matching the VD ceiling of BB) and E15 (A, matching the CV ceiling of A, A37). Ceilings for other countries are not in the data.

**Q31.** No. Among the countries with a stated ceiling, E05 and E15 are at it, not above it. The data has no ceilings for other countries.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** E10, rated BBB+. E10 guarantees I05, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent link to E09, and nothing else in the data ties it to the group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (shared LEIs).

**Q38.** No. They have different LEIs, countries (DE vs US) and no link between them.

**Q39.** A (A09 affirmed A).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS-system record E10 says DE, and E17 (LU, RESEARCH) is a duplicate by LEI.

**Q43.** 0. The only LU record is E17, which duplicates the DE-domiciled E10.

**Q44.** Yes. The note I07 is in XVD, which appears to be Valdoria's currency, though the data doesn't define it. Its BBB- rating matches the local-currency rating A13.

**Q45.** No. The ceiling of BB (A12) constrains foreign-currency ratings, and I07 is a local-currency obligation.

**Q46.** No. E11 has only a "CO" type rating (A46), which the data doesn't define. It has no LTIDR.

**Q47.** None. A47 shows I08 expired on 2026-09-01.

**Q48.** 7: I01 to I07. I08 had expired.

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