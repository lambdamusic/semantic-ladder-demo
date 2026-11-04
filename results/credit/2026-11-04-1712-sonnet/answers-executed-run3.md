**Q1.** A-. E01's LTIDR on 1 Jan 2025 was A- (A01, valid 2024-03-12 to 2025-06-20).

**Q2.** No. E01's only 2026 action was an affirmation with a Negative outlook (A03, 2026-02-10); the downgrade to BBB was in 2025 (A02).

**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is below investment grade.

**Q4.** Positive. E02's current LTIDR carries a POS outlook (A09).

**Q5.** The credit risk of E02 (Northwind Holdings), the guarantor (I03 has credit_risk_of E02). E02 is rated A (A09), and I03 is also rated A (A11).

**Q6.** The data doesn't state a cause. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The VD country ceiling is BB from 2025-04-01, which fits with the foreign-currency rating being capped at that level.

**Q7.** E08 and E10. E08 went to CCC (A21) and then RD (A22), and E10 went to BBB+ (A27). I05 was also downgraded (A29), but its issuer E11 has no issuer rating.

**Q8.** E08. Its LTIDR is RD from 2026-07-08 with no end date (A22).

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. E05 is BB in foreign currency (A14), which is sub-investment grade, but BBB- in local currency (A13), which is investment grade.

**Q11.** BBB+ (A36, valid 2024-09-30 to 2025-11-20).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36); the RWN (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A-. E10's rating on 1 Jan 2026 was A- (A26), before the April downgrade.

**Q16.** No. E14 was BBB+ on 1 Jan 2025 (A36) and is BBB+ now (A33). Only the watch status changed in between (A35).

**Q17.** No. E06's 2026 action was a move to Rating Watch Negative with the rating held at A- (A17).

**Q18.** E06 (A17). E14's watch ended on 2026-05-01 (A33).

**Q19.** E01 and E09 (A03, A25). E06 has no outlook while on watch.

**Q20.** No. E07's rating was withdrawn (A19), not moved to a default rating, and its last rating was BB (A18).

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating record, only a ceiling of BB.

**Q30.** E05 and E15. E05 is BB against the VD ceiling of BB (A14), and E15 is A against the CV ceiling of A (A41).

**Q31.** No. No company's foreign-currency rating exceeds its country ceiling.

**Q32.** E09 (ultimate_parent_id for E11).

**Q33.** The credit risk of E10 (Halden Bank), the guarantor of I05. E10 is rated BBB+ (A27), and I05 is also BBB+ (A29).

**Q34.** No. E12 has no parent and no ultimate parent, while E10 belongs to E09's group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 15. There are 15 entity rows, and the duplicate records E03 and E17 are already merged into E02 and E10.

**Q38.** No. They are separate entities: E06 (DE) and E13 (US), with different LEIs and no merge.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity is domiciled in LU.

**Q44.** Yes. I07 is flagged local_currency = yes and is denominated in XVD.

**Q45.** No. I07 is rated BBB- (A45), but the ceiling (BB) is a foreign-currency constraint, and I07 is a local-currency obligation.

**Q46.** No. E11 has no issuer rating. I05's rating comes from its guarantor E10.

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
"Q37": {"count": 15},
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