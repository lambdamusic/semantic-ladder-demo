**Q1.** A-. E01's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with the outlook moved to Negative (A03).

**Q3.** No. The 2031 note (I02) is rated BB+ since the 2025-06-20 downgrade (A07), which is below investment grade.

**Q4.** Positive (E02, A09).

**Q5.** E02, Northwind Holdings, rated A. I03 is guaranteed by E02, which is the entity whose credit risk it takes (credit_risk_of = E02), and I03 is rated A (A11).

**Q6.** The data doesn't state a reason. E05's FC rating is BB (A14) and its LC rating is BBB- (A13), and the VD country ceiling is BB (ceilings.csv), which is consistent with the FC rating being capped.

**Q7.** E08 and E10. E08 went B to CCC (A21) and then to RD (A22), and E10 went A- to BBB+ (A27).

**Q8.** E08. Its rating is RD (A22), and no other entity holds a default rating.

**Q9.** 12. The count covers CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07's rating is withdrawn (A19), and E04 and E11 have no issuer rating of their own.

**Q10.** Depends. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (not, A14).

**Q11.** BBB+ (E14, A36).

**Q12.** A- (E14, A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A- (E10, A26).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now (A33). Only the watch and outlook changed in between.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement at an unchanged A- (A17).

**Q18.** E06 (A17). E14's watch ended on 2026-05-01.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), and its last rating was BB, not a default rating.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (E01, A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (E15, A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV, A38).

**Q29.** None. VD has a ceiling but no rating records.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's is A, equal to the CV ceiling of A.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09 (E11's ultimate_parent_id).

**Q33.** E10, Halden Bank, rated BBB+. E10 guarantees I05 and is the entity whose credit risk it takes, and its rating is BBB+ (A27, A29).

**Q34.** No. E12 has no parent link to E09 or E10, so the data doesn't place it in that group despite the shared name.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 16. That is the number of rows in entities.csv, and the duplicate records are already merged into them.

**Q38.** No. E06 (DE, Orrin Bank AG) and E13 (US, Orrin Bancorp Inc) are separate entities with different LEIs.

**Q39.** A (E02, A09).

**Q40.** 5 (E01, E02, E09, E12, E14). E07 is excluded because its rating is withdrawn.

**Q41.** None. Brindle Capital isn't in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity has country LU.

**Q44.** Yes. I07 has local_currency = yes (currency XVD).

**Q45.** No. The ceiling is a single country figure, which here limits foreign-currency ratings, and I07 is a local-currency note. Its BBB- also exceeds the BB ceiling, so if the ceiling were applied to it the answer would flip.

**Q46.** No. E11 has no ratings of its own; I05's rating (A29) is an instrument rating that reflects E10's credit risk.

**Q47.** None. I08 has no rating records.

**Q48.** 7 (I01 to I07).

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