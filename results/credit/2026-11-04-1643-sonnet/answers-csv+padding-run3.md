**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation (A03, BBB, Negative outlook).

**Q3.** No, it is BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (2025-09-15, Positive), which supersedes A08 (Stable).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and I03 is rated A (A11).

**Q6.** The data does not state a reason. It is consistent with the foreign-currency rating being held at Valdoria's Country Ceiling of BB (A12, A14), while the local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16 had issuer-rating downgrades in 2026 (A21/A22, A27, A44). I05's instrument downgrade (A29) is not counted because its issuer E11 has no issuer rating. E06's action (A17) is a watch placement, not a downgrade.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. E07 was withdrawn (A19), E11 has only a CO-type record, and VD has only a country ceiling.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later watch (A35) did not change the rating.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade for E14; A35 is a watch placement.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). The watch from A35 was resolved by A33.

**Q17.** No. A17 (2026-09-03) places E06 on Rating Watch Negative at A-, which is not a downgrade.

**Q18.** E06. A17 is its latest action and carries RWN. E14's watch (A35) was superseded by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). E06's latest action is a watch with no outlook.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and nothing in the data shows a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) held investment-grade ratings. I02 and I04 are below investment grade, and I08 was expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 (FC BB against a BB ceiling) and E15 (FC A against an A ceiling, A37).

**Q31.** No. E05 is at its ceiling (BB) and E15 is at its ceiling (A), so neither is above.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10 and rated BBB+ (A29).

**Q34.** No. E12 has no parent link to E09 or E10, and only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10 but is a duplicate record.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. The 19 records contain two duplicates by LEI: E03 = E02 and E17 = E10.

**Q38.** No. They have different LEIs, countries (DE and US) and entity records.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+. E16 was downgraded to BB+ on 2026-06-01 (A44).

**Q42.** DE. E10 is domiciled in DE, and E17, which says LU, is a lower-quality duplicate with the same LEI.

**Q43.** 0. The only LU record is E17, which is a duplicate of E10 (DE).

**Q44.** Yes, though the data does not define XVD. I07 is in XVD, which appears to be Valdoria's currency, and its BBB- matches E05's local-currency rating (A13).

**Q45.** No. If XVD is local currency, the ceiling (BB, A12) does not apply to I07's BBB- rating (A45).

**Q46.** No. E11 only has a CO-type record (A46), not an issuer rating.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7: I01 to I07. I08's rating had expired by 1 October 2026.

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