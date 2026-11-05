**Q1.** A-. E01's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02); the 2026-02-10 action (A03) was an affirmation with the outlook moved to Negative.

**Q3.** No. The 2031 note (I02) is subordinated and currently rated BB+ (A07).

**Q4.** Positive. E02's current rating record is A09 (outlook POS).

**Q5.** E02 (Northwind Holdings), rated A. I03 has credit_risk_of E02 as guarantor, and its current rating is A (A11), matching E02's A (A09).

**Q6.** The data doesn't state a reason. It shows E05's FC rating is BB (A14) against an LC rating of BBB- (A13), and the VD Country Ceiling is BB. That is consistent with the ceiling capping the FC rating, but it is not confirmed.

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and RD (A22), and E10 to BBB+ (A27).

**Q8.** E08. Its rating is RD (A22), still in force.

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15, each with an issuer rating in force. E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. E05's FC rating is BB (non-investment grade, A14), but its LC rating is BBB- (investment grade, A13).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade is A36; A35 is a Rating Watch action and A33 is an affirmation.

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A- (A26, valid until 2026-04-15).

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33), though the watch status changed in between (A35).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative (A17), not a downgrade; the rating stays A-.

**Q18.** E06 (A17). The E14 watch (A35) ended on 2026-05-01.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's is A, equal to the CV ceiling of A.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 has credit_risk_of E10 as guarantor, and E10's rating is BBB+ (A27).

**Q34.** No. E12 has no parent and no ancestors, so it is not in the E09 group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 16. That is the number of rows in entities.csv, with duplicates already merged.

**Q38.** No. E06 and E13 are separate entities with different LEIs and countries, and are not merged.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. Brindle Capital isn't in the data.

**Q42.** LU (E10).

**Q43.** 1. Only E10 is domiciled in LU.

**Q44.** Yes. I07 has local_currency = yes.

**Q45.** No. I07 is rated BBB- (A45), above VD's BB ceiling, but it is a local-currency note and the ceiling applies to FC ratings.

**Q46.** No. E11 has no rating records; I05 is rated through its guarantor E10.

**Q47.** None. I08 has no rating records.

**Q48.** 7: I01 to I07 each have a rating in force.

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