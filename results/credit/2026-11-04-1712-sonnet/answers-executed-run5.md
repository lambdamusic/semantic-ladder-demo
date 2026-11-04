**Q1.** A-. E01's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02), and the 2026-02-10 action was an affirmation with a Negative outlook (A03).

**Q3.** No. The 2031 note (I02) has been rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's current LTIDR carries a POS outlook (A09).

**Q5.** Northwind Holdings (E02), via the guarantee. The note I03 is rated A (A11), and E02's LTIDR is also A (A09).

**Q6.** The data doesn't state a reason. E05 is rated BB FC (A14) against BBB- LC (A13), and the VD ceiling is BB, so the FC rating sits exactly at the ceiling.

**Q7.** E08 and E10. E08 was cut to CCC (A21) and then RD (A22), and E10 was cut to BBB+ (A27). I05, the E11 note, was also downgraded (A29), but E11 holds no issuer rating.

**Q8.** E08, which has been RD since 2026-07-08 (A22).

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15, each with an open LTIDR on 1 Oct 2026. E07's rating is withdrawn (A19), and E04 and E11 have none.

**Q10.** Depends. E05 is BBB- in local currency (investment grade, A13) but BB in foreign currency (not investment grade, A14).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36). The RWN in A35 was a watch, not a downgrade.

**Q14.** None. E12's first rating began on 2024-02-01 (A30).

**Q15.** A- (A26, valid until 2026-04-15).

**Q16.** No. The rating was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33). Only the watch and outlook changed.

**Q17.** No. E06 was placed on Rating Watch Negative with the rating held at A- (A17), which is not a downgrade.

**Q18.** E06 (A17). E14's watch ended on 2026-05-01 (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), and the data records no default for it.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. They are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** E05 and E15. E05 is BB FC against a BB ceiling for VD, and E15 is A FC against an A ceiling for CV.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09 (the entities table gives E09 as the ultimate parent of E11).

**Q33.** Halden Bank (E10), the guarantor. The note is rated BBB+ (A29), matching E10's BBB+ (A27).

**Q34.** No. E12 has no parent, so it is outside the E09 group that contains E10.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 16, the rows in entities.csv. Duplicates were already merged, as shown in record_ids.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) are separate entities with different LEIs and countries.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity has country LU.

**Q44.** Yes. I07 is flagged local_currency = yes and is denominated in XVD.

**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling number, but it is a local-currency note and the data gives the ceiling only as a country-level figure. I read it as a foreign-currency cap. E05's own LC rating is also BBB- (A13).

**Q46.** No. E11 has no issuer rating. Its note I05 takes E10's credit risk.

**Q47.** None. I08 has no rating records.

**Q48.** 7: I01 to I07.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```