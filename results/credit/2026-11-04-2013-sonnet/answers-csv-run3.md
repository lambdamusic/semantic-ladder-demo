**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action, A02, is dated 2025-06-20.

**Q2.** No. Kestrel's only 2026 actions, A03 and A04, are affirmations.

**Q3.** No. The 2031 note (I02) was downgraded to BB+ in A07, which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action with outlook POS.

**Q5.** The holder takes the credit risk of the guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02. A09/A11 affirm A.

**Q6.** The foreign-currency rating is capped by the sovereign Country Ceiling of BB (A12). The local-currency rating of BBB- (A13) is not constrained by it, so FC is BB (A14).

**Q7.** E08, E10 and E16. The 2026 issuer-level downgrades are A21 and A22 (E08), A27 (E10) and A44 (E16). A29 downgrades an instrument, not an issuer.

**Q8.** E08. Its latest action, A22, is RD (restricted default).

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, CV, E15 and E16. E07 was withdrawn, and E04, E11 and VD have no LTIDR.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded it on 2024-09-30, and A35 (2025-11-20) is later.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 applies, since the downgrade A27 only came on 2026-04-15. E17 is a duplicate of E10.

**Q16.** No. It was BBB+ throughout, and A35 and A33 are a watch and an affirmation.

**Q17.** No. A17 is only a Rating Watch Negative with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33 in 2026-05.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19) for commercial reasons, and it was never rated D or RD.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, via the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A). Only VD and CV have ceiling data.

**Q31.** No. No company's FC rating exceeds its ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the credit risk of the guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, and E03 and E17 are duplicates by LEI.

**Q38.** No. They have different LEIs, countries and types.

**Q39.** A (A08, A09, A11).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU. I treated the RATINGS record as authoritative, but the data doesn't state a precedence rule.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is DE in the RATINGS record. This depends on the same choice as Q42.

**Q44.** Yes, probably. The currency XVD is not a standard code, but A45 rated I07 BBB-, matching Valdoria's local-currency rating (A13). The data doesn't define XVD.

**Q45.** No. The BB ceiling (A12) caps foreign-currency ratings, and I07 appears to be local-currency. Its BBB- is also not above Valdoria Telecom's own LC rating.

**Q46.** No. E11 only has a "CO" record (A46), which is not an issuer rating type (LTIDR/STIDR), and CO is undefined in the data.

**Q47.** None. A47 shows I08 expired on 2026-09-01.

**Q48.** 7 (I01–I07).

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