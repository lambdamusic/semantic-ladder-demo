**Q1.** A-. E01's rating was assigned as A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03).

**Q3.** No. The 2031 note (I02) was cut to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its 2025-09-15 affirmation (A09) carries a POS outlook.

**Q5.** The holder takes E02's risk as guarantor of I03, and E02 is rated A. The rating comes from A09 on E03, which is the same entity as E02, and A11 also affirms I03 at A.

**Q6.** The data doesn't state a reason. It shows a Valdoria country ceiling of BB (A12), a foreign-currency rating of BB (A14) equal to that ceiling, and a local-currency rating of BBB- (A13). That fits the foreign-currency rating being capped by the ceiling.

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44. E06 only went on watch (A17), and E14's downgrade was in 2024 (A36).

**Q8.** E08, which was at RD from 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), VD has only a country ceiling, and E11 has only a "CO" rating.

**Q10.** Depends. The local-currency rating is BBB- (A13, investment grade) and the foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36), and nothing changed the rating before 2025-06-01.

**Q12.** A-, assigned on 2023-01-15 (A34).

**Q13.** 1, the downgrade in A36.

**Q14.** None. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A-. E17 shares E10's LEI, so it is the same entity, and E10 was rated A- (A26) until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 only put it on watch and affirmed it).

**Q17.** No. A17 is a Rating Watch Negative action that keeps the A- rating.

**Q18.** E06 (A17). E14's watch from 2025 (A35) was resolved by the 2026 affirmation with no watch (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19) and it never had a default rating.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08 expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals the VD ceiling of BB, and E15's A equals the CV ceiling of A.

**Q31.** No. No company's foreign-currency rating exceeds its country's ceiling, and only VD and CV have ceilings.

**Q32.** E09. E11 has parent E10 and E10 has parent E09.

**Q33.** The holder takes E10's risk as guarantor of I05, and E10 is rated BBB+ (A27). I05 itself is also BBB+ (A29).

**Q34.** No. E12 has no parent, and E09 is not linked to it.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. E06 and E13 have different LEIs and different countries.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE and the RESEARCH duplicate E17 says LU. I took the RATINGS record, but the sources conflict.

**Q43.** 0. The only LU record is E17, a RESEARCH duplicate of E10, which is DE in RATINGS, so the answer depends on how that conflict is resolved.

**Q44.** Depends. I07's currency is "XVD", and the data does not say that XVD is Valdoria's local currency.

**Q45.** Depends. I07 is BBB- (A45) against a ceiling of BB (A12), but a ceiling limits only foreign-currency obligations, so the answer depends on Q44.

**Q46.** No. E11 has only a "CO" rating (A46), whose meaning the data doesn't define, and no LTIDR.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7, I01 to I07. I08 expired.

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