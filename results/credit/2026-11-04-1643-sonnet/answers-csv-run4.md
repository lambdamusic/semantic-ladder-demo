**Q1.** A-. Kestrel's LTIDR was A- from A01 (2024-03-12) until it was downgraded in A02 (2025-06-20).

**Q2.** No. The only 2026 action on Kestrel's issuer rating is A03, an affirmation at BBB. The downgrade was A02 in 2025.

**Q3.** No. I02 was rated BBB (A23), then downgraded to BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity. Its latest action is A09 (2025-09-15), an affirmation with a POS outlook.

**Q5.** E02, the guarantor of I03 (Northwind Finance's 2030 notes). I03 is rated A (A10, A11), the same as E02's A.

**Q6.** The Republic of Valdoria's Country Ceiling is BB (A12), which caps E05's foreign-currency rating at BB (A14). Its local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16 had issuer ratings downgraded in 2026 (A21/A22, A27, A44). I05's downgrade (A29) is an instrument action, and its issuer E11 has no issuer rating.

**Q8.** E08. A22 on 2026-07-08 moved it to RD, restricted default, after a distressed debt exchange.

**Q9.** 13. E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16 hold an issuer rating. E07's was withdrawn (A19), and VD (a Country Ceiling only) and E11 (a "CO" rating) don't count.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded from A- on 2024-09-30 (A36), and A35 (2025-11-20) was a later watch action.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came after that date (A36).

**Q13.** 1. Only A36 is a downgrade of E14.

**Q14.** None. E12's first rating was A30, on 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26 and downgraded only on 2026-04-15 (A27). E17 is a duplicate record of E10 (same LEI).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating kept at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33 with no watch.

**Q19.** E01 (A03) and E09 (A25). E06's outlook is blank in A17, so it isn't counted.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and there is no default action.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 and I04 are below investment grade, and I08 expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB (A12, A14). E15's A equals CV's ceiling of A (A37, A41).

**Q31.** No. No foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. The chain runs E11 → E10 → E09.

**Q33.** E10, the guarantor of I05. I05 is rated BBB+ (A29), the same as E10's current BBB+ (A27).

**Q34.** No. E12 has no parent link or shared LEI with the Halden Group.

**Q35.** 3. The group is E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2. The group is E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs (E06 vs E13) and different countries.

**Q39.** A (A08, A09).

**Q40.** 6. E01, E02, E09, E12, E14 and E16 are the GB entities holding an issuer rating. E07 was withdrawn.

**Q41.** BB+ (A44). E16's source system is QA, which may make it less reliable.

**Q42.** DE. E10's record in the RATINGS system says DE. The LU in E17 comes from a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, duplicates E10, which is domiciled in DE.

**Q44.** Depends. I07's currency is XVD, which isn't a standard code and isn't defined in the data. It is probably Valdoria's currency, but the data doesn't confirm that.

**Q45.** Depends. I07 is rated BBB-, above the BB ceiling (A12). The ceiling only constrains foreign-currency obligations, and whether XVD is local currency is unconfirmed.

**Q46.** No. E11's only rating is a "CO" type (A46), not an issuer rating.

**Q47.** None. I08 expired on 2026-09-01 (A47).

**Q48.** 7. I01–I07 are rated, and I08 expired.

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