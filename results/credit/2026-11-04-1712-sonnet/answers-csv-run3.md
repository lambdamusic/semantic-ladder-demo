**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action on E01 (A02) was not until 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations at BBB (A03, A04).

**Q3.** No. I02 was cut to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (POS, 2025-09-15).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A08, A09).

**Q6.** The data doesn't state a reason. The FC rating of BB (A14) equals the Valdoria country ceiling of BB (A12), while the LC rating is BBB- (A13), which suggests the ceiling is capping the FC rating.

**Q7.** E08, E10 and E16. They were downgraded in A21 and A22, A27, and A44 respectively. A17 for E06 is only a watch, and A29 is an instrument action.

**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. The LC rating is BBB- (investment grade, A13) but the FC rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36).

**Q12.** A-, from A34.

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 applied until the downgrade in A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33, A35). The RWN in A35 is a watch, not a rating change.

**Q17.** No. A17 in 2026 is a Rating Watch Negative with the rating kept at A-.

**Q18.** E06 (A17). E14's watch (A35) was followed by an affirmation with no watch (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and it never had a default rating.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which was rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 had expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling (A12), which is not an issuer rating.

**Q30.** E05 (FC BB equals the VD ceiling of BB) and E15 (FC A equals the CV ceiling of A).

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+ (A27). I05 is guaranteed by E10.

**Q34.** No. E12 has no parent and no link to E09 or E10 in the data. The shared name alone doesn't establish a group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. The 19 rows include two duplicates by shared LEI: E03 (of E02) and E17 (of E10).

**Q38.** No. They have different LEIs and different countries.

**Q39.** A. A08 and A09 (via the duplicate E03) both give A.

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE, per E10 in the RATINGS system. The RESEARCH duplicate E17 says LU, so the records conflict.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is DE in the primary record. If the E17 record were correct, the answer would be 1.

**Q44.** Yes, probably. I07 is denominated in XVD, which is not a standard ISO code and is not defined in the data, but it looks like Valdoria's local currency.

**Q45.** No. The ceiling of BB (A12) applies to FC ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 only has a "CO" rating (A46), which is not an issuer default rating.

**Q47.** None. I08 expired on 2026-09-01 (A47), so it holds no rating now.

**Q48.** 7. These are I01 to I07, and I08 had expired.

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