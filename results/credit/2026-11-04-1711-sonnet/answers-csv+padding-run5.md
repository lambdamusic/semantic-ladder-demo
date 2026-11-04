**Q1.** A-. E01's rating was assigned at A- on 2024-03-12 (A01) and not cut until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations at BBB (A03, A04).

**Q3.** No. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and the latest action is A09 (2025-09-15, POS).

**Q5.** The holder takes the credit risk of E02, the guarantor of I03, which is rated A (A08, A09).

**Q6.** The data gives no stated reason. E05's FC rating of BB (A14) equals the Valdoria country ceiling of BB (A12), while its LC rating is BBB- (A13). That is consistent with the ceiling capping FC ratings.

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21, A22, A27, A44). E06's action was a watch, not a downgrade (A17). The I05 downgrade (A29) is an instrument action.

**Q8.** E08. It was rated RD on 2026-07-08 (A22).

**Q9.** 13. Issuers with a current LTIDR are E01, E02 (including E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). E04 and E11 have no issuer rating, and VD only has a country ceiling.

**Q10.** Depends. E05 is BBB- in local currency (A13, investment grade) and BB in foreign currency (A14, not investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later actions A35 and A33 kept it there.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34).

**Q13.** 1, for A36.

**Q14.** None. E12's first rating came on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 is the same LEI.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The watch in A35 was later resolved.

**Q17.** No. E06 was placed on Rating Watch Negative at A- (A17), and the rating was not lowered.

**Q18.** E06 only (A17). E14's watch (A35) ended with the affirmation in A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and there is no default rating.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is rated BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating was ended by an EX action on 2026-09-01 (A47), which I read as expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling record (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB matches the VD ceiling of BB (A12, A14). E15's FC rating of A matches the CV ceiling of A (A37, A41).

**Q31.** No. No company's FC rating exceeds its ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and no link between them.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The authoritative RATINGS record E10 says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record is DE. This is uncertain because of the conflict.

**Q44.** Yes, most likely. I07 is denominated in XVD, which is presumably Valdoria's currency, though the data does not define the code. Its BBB- matches E05's LC rating (A13, A45).

**Q45.** No. The BB ceiling (A12) caps foreign-currency ratings, and I07 is a local-currency instrument rated BBB-.

**Q46.** No. E11 has only a "CO" type record (A46), which is not an issuer rating.

**Q47.** None. I08's rating of A was ended by the EX action on 2026-09-01 (A47).

**Q48.** 7: I01 to I07. I08's rating ended on 2026-09-01.

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