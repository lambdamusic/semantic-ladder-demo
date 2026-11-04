**Q1.** A-. E01's rating was assigned on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04).

**Q3.** No. I02 was cut to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is an affirmation with a POS outlook (A09).

**Q5.** E02, the guarantor of I03, rated A. E04 is the issuer, but E02 guarantees the notes, and E02's latest rating is A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12). The foreign-currency rating is capped at BB (A14), while the local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16. E08 was downgraded twice (A21, A22), E10 once (A27), and E16 once (A44).

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is excluded because it was withdrawn (A19), and VD only has a Country Ceiling (A12), not an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. The downgrade to BBB+ was dated 2024-09-30 (A36), and the watch action only came later (A35).

**Q12.** A-, from A34.

**Q13.** 1, from A36. A35 is a watch action and A33 is an affirmation.

**Q14.** None. E12's first rating was on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 shares E10's LEI and has no actions of its own.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at an unchanged A- (A17).

**Q18.** E06 (A17). E14's watch (A35) was followed by an affirmation with no watch (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and it was never rated in default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which was rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating ended with an EX action on 2026-09-01 (A47), which I read as expiry.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to Valdoria's ceiling of BB (A14, A12). E15's is A, equal to Corvenia's ceiling of A (A41, A37).

**Q31.** No. No foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** E10, the guarantor of I05, rated BBB+ (A27). The note itself is also BBB+ (A29).

**Q34.** No. E12 has no parent link to E09, and the shared name is the only connection.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10, since each pair shares an LEI.

**Q38.** No. They have different LEIs, countries (DE and US) and entity records.

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because it was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 says DE, and E17 says LU, but E17 shares E10's LEI, which ends in "DE62".

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE). The data conflicts here, so this follows the LEI.

**Q44.** Yes, probably. Its currency is XVD, which looks like a Valdoria currency code, but the data never defines it.

**Q45.** No. The Country Ceiling applies to foreign-currency ratings, and this note appears to be in local currency. Its BBB- (A45) is also above the BB ceiling, so the answer would change if XVD were not local currency.

**Q46.** No. E11 has only a "CO" rating (A46), which is not an issuer rating type (LTIDR/STIDR), and the data does not define CO.

**Q47.** None. I08's rating ended with an EX action (A47), which I read as expiry.

**Q48.** 7: I01, I02, I03, I04, I05, I06 and I07. I08 is excluded.

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