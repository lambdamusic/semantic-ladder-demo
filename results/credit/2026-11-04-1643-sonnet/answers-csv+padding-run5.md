**Q1.** A-. A01 assigned A- to E01 on 2024-03-12, and the next action (A02) came later, on 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), with the outlook moved to Negative.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and then downgraded to BB+ (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action with a POS outlook.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, and E02's rating is A (A08, affirmed in A09 under the duplicate record E03).

**Q6.** The data points to the country ceiling: VD's ceiling is BB (A12). E05's foreign-currency rating is BB (A14), equal to that ceiling, while its local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21, A22, A27, A44). The E06 action (A17) is a watch, not a downgrade.

**Q8.** E08. A22 moved it to RD (restricted default) on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. I excluded E07 (withdrawn, A19), E11 (only a "CO" rating, which the data does not define) and VD (only a country ceiling).

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and A35 (2025-11-20) is after the question date.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. E12's first rating (A30) is dated 2024-02-01.

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative (A17), with the rating still A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation with a Stable outlook (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19). That is not a default, and its last rating was BB.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are sub-investment grade. I08's rating expired on 2026-09-01 (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD's only record is a country ceiling (CC, A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to VD's ceiling of BB (A14, A12), and E15's is A, equal to CV's ceiling of A (A41, A37).

**Q31.** No. Neither E05 nor E15 is above its ceiling, and the data holds ceilings only for VD and CV.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent link to the E09/E10/E11 chain, and the shared name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and entity IDs (E06 and E13).

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn, and E08 is domiciled in GR.

**Q41.** BB+. A44 downgraded it from BBB-, though E16 comes from the QA source system.

**Q42.** DE. E10 in the RATINGS system says DE. The duplicate E17 (RESEARCH) says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record says DE. If you trust E17 over E10, the answer would be 1.

**Q44.** Depends. I07's currency is "XVD", which the data does not define, though it is presumably Valdoria's currency.

**Q45.** Depends. I07 is rated BBB- (A45) against a BB ceiling (A12). The ceiling constrains foreign-currency obligations, so whether this is "above" turns on the undefined XVD in Q44.

**Q46.** No. E11 has only a "CO" rating (A46), a type the data does not define, and no LTIDR.

**Q47.** None. I08's rating expired on 2026-09-01 (A47, EX), so it had no current rating on today's date.

**Q48.** 7. I01 to I07 held a rating, while I08's expired on 2026-09-01.

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
"Q44": {"local_currency": "depends"},
"Q45": {"above_ceiling": "depends"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```