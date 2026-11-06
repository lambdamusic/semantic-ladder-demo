**Q1.** A-. Kestrel's foreign-currency long-term rating was A- on that date (A01, valid 2024-03-12 to 2025-06-20).

**Q2.** No. The only downgrade was on 2025-06-20 (A02). The 2026-02-10 action (A03) was an affirmation at BBB, with the outlook moving to Negative.

**Q3.** No. The 2031 note (I02) has been rated BB+ since 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E02's current rating (A09) has a POS outlook. E03 is merged into E02.

**Q5.** E02, the guarantor of I03 and the instrument's credit_risk_of. It is rated A (I03, A11), and E02's issuer rating is also A.

**Q6.** The data doesn't state a reason, but it is consistent with the Country Ceiling. Valdoria's ceiling is BB (from 2025-04-01), and E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13).

**Q7.** E08 and E10. E08 was downgraded on 2026-01-20 and 2026-07-08 (A21, A22), and E10 on 2026-04-15 (A27). I05, the Halden Leasing note, was also downgraded on 2026-04-15, but that is an instrument rating and E11 has no issuer rating.

**Q8.** E08. Its rating has been RD since 2026-07-08 (A22).

**Q9.** 12. Issuer ratings in force and not withdrawn: CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15. E07 is withdrawn (A19), and VD has none.

**Q10.** Depends. E05 is BB in foreign currency (non-investment grade) and BBB- in local currency (investment grade).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was on 2024-09-30 (A36).

**Q14.** None. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A- (E10, A26).

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now. Only the watch and outlook status changed (A35, A33).

**Q17.** No. The 2026-09-03 action (A17) put E06 on Rating Watch Negative and the rating stayed at A-.

**Q18.** E06 (A17). E14's watch ended on 2026-05-01.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19), and no default rating is recorded for it.

**Q21.** E07. Its rating was withdrawn (WD, A19).

**Q22.** E08. It is the only entity with a default-grade rating (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** E05 and E15. E05 is BB against a VD ceiling of BB, and E15 is A against a CV ceiling of A.

**Q31.** No. E05 and E15 are exactly at their ceilings, not above them.

**Q32.** E09.

**Q33.** E10, the guarantor of I05. I05 is rated BBB+ (A29), the same as E10's issuer rating.

**Q34.** No. E12 has no parent, and E10's ultimate parent is E09.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 16 entity rows, after duplicate records were merged (E03 into E02, E17 into E10).

**Q38.** No. E06 (DE) and E13 (US) are separate entities with different LEIs.

**Q39.** A (A09).

**Q40.** 5. The GB issuers with an issuer rating on 2026-10-01 are E01, E02, E09, E12 and E14. E07 is withdrawn.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU.

**Q43.** 1 (E10).

**Q44.** Yes. I07 has local_currency = yes and is denominated in XVD.

**Q45.** No. I07 is a local-currency obligation, and the ceiling applies to foreign-currency ratings. Its BBB- (A45) is therefore not capped by the BB ceiling.

**Q46.** No. E11 has only an instrument rating (I05) and no issuer rating.

**Q47.** None. I08 has no rating records.

**Q48.** 7. I01 to I07 have current ratings and I08 has none.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
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
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```