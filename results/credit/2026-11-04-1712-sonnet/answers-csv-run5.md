**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. The only 2026 action on Kestrel's issuer ratings is an affirmation at BBB with a Negative outlook (A03, A04).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and the latest outlook is POS (A09, 2025-09-15).

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, the guarantor of I03, which is rated A (A08, A09).

**Q6.** The Valdoria country ceiling is BB (A12), which caps the foreign-currency rating (A14, BB), while the local-currency rating is BBB- (A13).

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44) were downgraded in 2026. E06's action is a Watch (A17), not a downgrade.

**Q8.** E08. It was rated RD on 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn, VD has only a country ceiling, and E11 has only a "CO" rating, which I did not count as an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. The downgrade from A- to BBB+ was on 2024-09-30 (A36).

**Q12.** A-, from the 2023-01-15 assignment (A34).

**Q13.** 1, on 2024-09-30 (A36).

**Q14.** None. The first rating was assigned 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in 2023 (A26) and downgraded only in April 2026 (A27). E17 is a duplicate of E10, as it shares the same LEI.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33). The Watch in A35 was not a rating change.

**Q17.** No. The only 2026 action on Orrin Bank is a Rating Watch Negative at A- (A17).

**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by the affirmation without a watch (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), not because of a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which went to RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 and I04 are not, and I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), not an issuer rating.

**Q30.** E05 (FC BB at the VD ceiling of BB) and E15 (FC A at the CV ceiling of A).

**Q31.** No. Only the VD and CV ceilings are given, and neither is exceeded.

**Q32.** E09 (E11 → E10 → E09).

**Q33.** The holder takes the risk of E10, the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. E12 has no parent link, and Halden Bank sits under E09.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10, based on matching LEIs.

**Q38.** No. They have different LEIs and countries (DE and US), and no link joins them.

**Q39.** A. The rating was assigned in 2023 (A08) and affirmed through E03 in 2025 (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. E17 shows LU, but it is a RESEARCH-system duplicate of E10, which is in DE.

**Q43.** 0. The only LU record, E17, duplicates the DE entity E10. This is a judgement call, because counting E17 as a separate record would give 1.

**Q44.** Yes, probably. I07 is denominated in XVD, which appears to be Valdoria's currency, though the data does not define it.

**Q45.** No. The BB ceiling caps foreign-currency ratings, and I07 is a local-currency note rated BBB-.

**Q46.** No. E11 has only a "CO" rating (A46), not an LTIDR or other issuer rating.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7. I01–I07 hold ratings, and I08's rating has expired.

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