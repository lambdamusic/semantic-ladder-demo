**Q1.** A-. A01 assigned A- on 2024-03-12, and the downgrade in A02 only came on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03/A04).

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07, which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) has a POS outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and A09/A11 affirm A.

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating of BBB- (A13) is not capped.

**Q7.** E08, E10, E16. The downgrades are A21/A22 (E08), A27 (E10) and A44 (E16). A17 for E06 is a watch, not a downgrade.

**Q8.** E08. It was rated RD on 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. E07 was withdrawn (A19), and the CC and CO rows are not issuer ratings.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later RW (A35) kept BBB+.

**Q12.** A-. A34 assigned A- on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. The first E12 rating (A30) is dated 2024-02-01.

**Q15.** A-. E10 was rated A- from A26, and the downgrade in A27 came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33, A35, A36).

**Q17.** No. A17 only puts E06 on Rating Watch Negative and leaves the rating at A-.

**Q18.** E06. A35's watch on E14 was followed by A33, which affirms BBB+ with no watch.

**Q19.** E01, E09. A03 and A25 give them NEG outlooks, and E06 has no outlook after A17.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and no default rating appears in its history.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08. It was rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The E01 issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling of BB (A12), and no issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB (A14, A12), and E15's FC rating of A equals the CV ceiling of A (A41, A37).

**Q31.** No. No company's FC rating exceeds its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10, by shared LEI.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10, by shared LEI.

**Q38.** No. They have different LEIs, countries (DE and US) and no link between them.

**Q39.** A. A09 affirmed it on 2025-09-15, and E03 is the same entity as E02.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU. I treated the RATINGS record as authoritative, which is a judgement call.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, domiciled in DE.

**Q44.** Yes, probably. I07 is denominated in XVD, apparently Valdoria's currency, but the data does not state this outright.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is local-currency (BBB- in A45).

**Q46.** No. E11 only has a CO-type rating (A46), not an issuer rating.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

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