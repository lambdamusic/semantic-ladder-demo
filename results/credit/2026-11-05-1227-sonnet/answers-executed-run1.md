**Q1.** A-. Kestrel's foreign-currency LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. The downgrade to BBB was in 2025 (A02); the 2026-02-10 action only affirmed BBB and moved the outlook to Negative (A03).

**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is below investment grade.

**Q4.** Positive. Northwind Holdings' current LTIDR is A with a Positive outlook (A09).

**Q5.** Northwind Holdings (E02), via the guarantor. The note (I03) is rated A (A11).

**Q6.** Valdoria's Country Ceiling is BB (from 2025-04-01), which caps the foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13). The data states the ceiling but doesn't spell out the rating methodology.

**Q7.** E08 and E10. E08 went to CCC (A21) and then RD (A22), and E10 went to BBB+ (A27). E11's note I05 was also downgraded (A29), but E11 itself has no issuer rating.

**Q8.** E08. Its rating is RD (A22), still in force.

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. Its foreign-currency rating is BB (sub-investment grade) and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. Halden Foods' first rating started on 2024-02-01 (A30).

**Q15.** A- (A26).

**Q16.** No. The rating stayed BBB+ throughout (A36, A35, A33). Only the watch status and outlook changed.

**Q17.** No. Orrin Bank's rating stayed A-, and it was only placed on Rating Watch Negative (A17).

**Q18.** E06 (A17). E14's watch ended on 2026-05-01 (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam's rating was withdrawn (WD, A19), which is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. No rating record exists for VD.

**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to the VD ceiling (A14). E15's is A, equal to the CV ceiling (A41).

**Q31.** No. The foreign-currency ratings of E05 and E15 equal their ceilings and none is above.

**Q32.** E09.

**Q33.** Halden Bank (E10), the guarantor. The note (I05) is rated BBB+ (A29).

**Q34.** No. E12 has no parent and appears in no ancestor chain, so there is no recorded link to E09's group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 16. The 16 entity rows cover all distinct entities, because duplicates (E03 into E02, E17 into E10) are already merged.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) have different LEIs and are separate entities.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** Luxembourg (LU), per E10.

**Q43.** 1: E10.

**Q44.** Yes. I07 is flagged local_currency = yes (denominated in XVD).

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note. Its BBB- also matches the local-currency issuer rating (A13).

**Q46.** No. E11 has no issuer rating, only the guaranteed instrument I05, which takes E10's credit risk.

**Q47.** None. I08 has no rating record.

**Q48.** 7: I01 to I07. I08 is unrated.

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