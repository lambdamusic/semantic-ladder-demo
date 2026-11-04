**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed it until A02 on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the downgrade A02 was in 2025.

**Q3.** No. I02 is rated BB+ (A07, after the A23 BBB assignment), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action A09 (2025-09-15) gives a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and E02's latest rating is A (A09 on the duplicate record E03).

**Q6.** The data doesn't state a reason, but the sovereign Country Ceiling for Valdoria (A12, BB) appears to cap the foreign-currency rating. E05's FC rating is BB (A14) against an LC rating of BBB- (A13).

**Q7.** E08, E10 and E16 had issuer-rating downgrades in 2026 (A21, A22, A27, A44). I05's downgrade (A29) is on an instrument, not an issuer rating.

**Q8.** E08, which was at RD from A22 (2026-07-08).

**Q9.** 13. They are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn, and VD has only a country ceiling (CC). E11 has only a "CO" record, not an issuer rating.

**Q10.** Depends. E05 is BBB- in local currency (A13), which is investment grade, and BB in foreign currency (A14), which is not.

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30.

**Q12.** A-, per A34.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E17 is the same entity as E10 (same LEI), and A26's A- stood until A27 in April 2026.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33, A35). Only the watch status changed.

**Q17.** No. A17 puts E06 on Rating Watch Negative but keeps the rating at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the A33 affirmation with a Stable outlook.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 has no default rating; it was withdrawn for commercial reasons (A19).

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, from the RD rating in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) qualify. I08 expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling (A12, CC), which is not an issuer rating.

**Q30.** E05 (FC BB, VD ceiling BB) and E15 (FC A, CV ceiling A).

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The guarantor, Halden Bank (E10), currently rated BBB+ (A27). I05 is guaranteed by E10.

**Q34.** No. E12 has no parent and no link to E09 in the data.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries and no link.

**Q39.** A (A09 affirmed A on the duplicate record E03).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10, from the RATINGS system, says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record, E17, is a duplicate of the German E10. If E17's country were trusted, the count would be 1.

**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency but isn't defined in the data. Its BBB- (A45) matches E05's local-currency rating.

**Q45.** No. The ceiling (A12, BB) constrains foreign-currency ratings, and I07 appears to be local-currency.

**Q46.** No. E11 has only a "CO" record (A46), not an LTIDR or other issuer rating.

**Q47.** None. I08 expired (A47, EX), so it holds no rating now.

**Q48.** 7 (I01–I07). I08 had expired by then.

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