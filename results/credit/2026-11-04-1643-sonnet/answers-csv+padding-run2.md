**Q1.** A-. E01's rating was assigned at A- on 2024-03-12 (A01) and not changed until A02 on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, it is BB+. I02's latest action is A07 (2025-06-20, DG to BB+), which supersedes A23 (BBB).

**Q4.** Positive (POS). E03 shares E02's LEI, so I treat them as one entity. A09 (2025-09-15) is the latest action and carries a POS outlook.

**Q5.** The guarantor, E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and A09 affirms A for E03, which is E02.

**Q6.** The data supports only a partial answer. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). VD's country ceiling is BB (A12), which matches the foreign-currency rating; the data states no causal reason.

**Q7.** E08, E10, E16. They were downgraded in A21/A22, A27 and A44. I05's 2026 downgrade (A29) is on an instrument, not an issuer.

**Q8.** E08. A22 put it at RD on 2026-07-08 with no later action.

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade), but its foreign-currency rating is BB (not).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the watch in A35 only began on 2025-11-20.

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26, and the downgrade in A27 came only on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). A35 added a watch but not a rating change.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative (A17), with the rating still A-. E13 is a different entity.

**Q18.** E06, from A17 (RWN, 2026-09-03). E14's watch (A35) was resolved by A33.

**Q19.** E01 and E09, from A03 and A25 (both NEG).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of default.

**Q21.** E07, withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 has expired.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a country ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. Their foreign-currency ratings (BB in A14, A in A41) equal the ceilings for VD (BB, A12) and CV (A, A37).

**Q31.** No. The two companies with a ceiling are exactly at it, not above.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The guarantor, E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest action is A27.

**Q34.** No. E12 has no parent link and a different LEI from the E09 group.

**Q35.** 3. These are E09, E10 and E11. E17 duplicates E10 (same LEI).

**Q36.** 2. These are E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE vs US) and no link between them.

**Q39.** A, from A09.

**Q40.** 6. These are E01, E02, E09, E12, E14 and E16. E07 was withdrawn and E10 is in DE.

**Q41.** BB+, from A44.

**Q42.** DE. E10 is recorded as DE, and the LU on E17 is a duplicate record with the same LEI.

**Q43.** 0. The only LU record is E17, which resolves to E10 (DE), so this rests on a conflicting record.

**Q44.** Depends. I07 is in currency XVD, and the data does not say what XVD is or that it is Valdoria's local currency.

**Q45.** Depends. I07 is rated BBB- (A45), above the BB ceiling (A12). The ceiling applies only to foreign-currency obligations, so this hinges on Q44.

**Q46.** No. E11's only rating is a "CO" type (A46), not an issuer rating, and the data does not define CO.

**Q47.** None. A47 shows the I08 rating expired on 2026-09-01.

**Q48.** 7. These are I01 to I07, since I08's rating had expired.

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