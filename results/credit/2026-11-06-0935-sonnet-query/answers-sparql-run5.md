**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01), and the next action was not until 2025-06-20.

**Q2.** No. E01's only 2026 actions (A03, A04, 2026-02-10) are affirmations: BBB with a Negative outlook, and F2.

**Q3.** No. The 2031 note (I02) was cut to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 is a RESEARCH-system duplicate of E02, with the same LEI. Its latest action (A09, 2025-09-15) gives A / Positive, which is later than E02's Stable (A08, 2023).

**Q5.** The risk is E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and I03 is rated A (A10, A11).

**Q6.** The data does not state a reason. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The Republic of Valdoria's country ceiling is BB (A12), which matches the FC rating, so a ceiling cap is the likely explanation.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44). I05's 2026 downgrade is an instrument rating, not an issuer downgrade.

**Q8.** E08. It was rated RD from 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn. E11's rating is a CO type, not an issuer rating. VD only has a country ceiling.

**Q10.** Depends. E05's LC rating is BBB- (investment grade) and its FC rating is BB (not).

**Q11.** BBB+. E14 was downgraded on 2024-09-30 (A36).

**Q12.** A-, assigned 2023-01-15 (A34).

**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 is an affirmation.

**Q14.** None. E12's first rating was on 2024-02-01 (A30).

**Q15.** A-. This is E10's rating from A26, before the 2026-04-15 downgrade (A27). E17 is a duplicate record.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. E06 only had a Rating Watch Negative placed on 2026-09-03 (A17), with the rating kept at A-.

**Q18.** E06. E14's watch (A35) was resolved on 2026-05-01 (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 6. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A). I02 (BB+) and I04 (BB) are below investment grade.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country-ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB. E15's FC rating is A, equal to CV's ceiling of A (A37).

**Q31.** No. No FC issuer rating is above its country ceiling.

**Q32.** E09. The chain is E11, then E10, then E09.

**Q33.** The risk is E10 (the guarantor), rated BBB+. I05 is issued by E11 but guaranteed by E10, and was downgraded to BBB+ on 2026-04-15 (A29).

**Q34.** No. E12 has no parent link to the Halden group, and the shared name is not evidence of a relationship.

**Q35.** 3. These are E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2. These are E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 records, and E03 and E17 are duplicates sharing the LEIs of E02 and E10.

**Q38.** No. E06 and E13 have different LEIs and different countries (DE and US).

**Q39.** A. Both E02 and E03 show A, and E03's latest action is an affirmation (A09).

**Q40.** 6. These are E01, E02, E09, E12, E14 and E16. E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS-system record E10 says DE, while the duplicate research record E17 says LU. I treated E10 as authoritative, but the conflict is unresolved.

**Q43.** 0. The only LU record, E17, is a duplicate of E10, which is DE in the RATINGS system. If E17 were treated as separate, the count would be 1.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's local currency. The data does not define XVD explicitly.

**Q45.** No. The BB ceiling constrains foreign-currency ratings. I07 is a local-currency obligation rated BBB- (A45).

**Q46.** No. E11's only rating (A46) is a CO type, not an issuer rating. I05 is rated, but that is an instrument rating.

**Q47.** A (A47, action EX on 2026-09-01).

**Q48.** 8. All eight instruments I01–I08 have a rating.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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
"Q25": {"count": 6},
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
"Q47": {"rating": "A"},
"Q48": {"count": 8}
}
```