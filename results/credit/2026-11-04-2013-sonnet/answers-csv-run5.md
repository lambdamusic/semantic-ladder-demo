**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed it before 2025-01-01.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the downgrade A02 was in 2025.

**Q3.** No. I02 was downgraded to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest outlook (POS).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A09 and A10/A11 show A).

**Q6.** The foreign-currency rating is capped by the Country Ceiling. Valdoria's ceiling is BB (A12), so E05's foreign-currency rating is BB (A14) against BBB- local currency (A13).

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21/A22, A27, A44). E06's A17 is a watch placement, not a downgrade.

**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. VD has only a country ceiling, E07's rating was withdrawn, and E11's "CO" type is not an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) but the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later watch (A35) did not change the rating.

**Q12.** A-. A34 assigned A- on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was rated A- (A26) until the downgrade on 2026-04-15 (A27). E17 is a duplicate of E10 by LEI.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33). The watch in A35 was resolved by A33.

**Q17.** No. A17 is a Rating Watch Negative placement with the rating still A-, not a downgrade.

**Q18.** E06 only (A17). E14's watch (A35) was resolved by the 2026-05-01 affirmation (A33).

**Q19.** E01 (A03) and E09 (A25). E06 has no outlook recorded after A17.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and there is no default rating.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), not an issuer rating.

**Q30.** E05 (foreign currency BB, equal to the VD ceiling BB) and E15 (foreign currency A, equal to the CV ceiling A).

**Q31.** No. Only E05 and E15 have ceilings in the data, and both are at their ceiling, not above it. The other companies' countries have no ceiling in the data.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 gives BBB+.

**Q34.** No. E12 has no parent link, and the shared name is not evidence of group membership.

**Q35.** 3 (E09, E10, E11). E17 is a duplicate of E10 by LEI.

**Q36.** 2 (E02, E04). E03 duplicates E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10 by LEI.

**Q38.** No. They have different LEIs (E06 and E13), different countries and no link.

**Q39.** A. A09 affirmed A on E03, which is the same entity as E02 (same LEI).

**Q40.** 6 (E01, E02/E03, E09, E12, E14, E16). E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 in the RATINGS system says DE. E17 is a RESEARCH duplicate with the same LEI that says LU, so the sources conflict and I took the primary record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.

**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency. Its BBB- rating matches the local-currency rating (A13), but the data has no currency table to confirm this.

**Q45.** No. The ceiling (BB) limits foreign-currency ratings. I07 is rated BBB- (A45) and appears to be local-currency.

**Q46.** No. E11 only has a "CO" type action (A46), which is not an issuer rating type.

**Q47.** None. A47 shows I08's rating as expired (EX) on 2026-09-01.

**Q48.** 7 (I01–I07). I08's rating expired.

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