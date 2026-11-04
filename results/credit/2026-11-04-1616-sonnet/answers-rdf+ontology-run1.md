**Q1.** A-. E01's rating was set by A01 (assigned A- on 2024-03-12) and held until the downgrade in A02 (2025-06-20).

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations (the negative outlook in A03 is not a downgrade).

**Q3.** No. The 2031 note is I02, and its latest action, A07 (2025-06-20), downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15), an affirmation at A with a positive outlook.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02, the same entity as E03), rated A. I03 is guaranteed by E02, so it carries the guarantor's risk. E02's latest rating is A (A09).

**Q6.** E05's FC rating is BB (A14), against a BBB- LC rating (A13). The Valdoria Country Ceiling is BB (A12) and caps FC ratings but not LC ratings.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 downgraded instrument I05, which is not an issuer rating.

**Q8.** E08. A22 moved it to RD, a default, on 2026-07-08, and nothing later changes that.

**Q9.** 12. The issuers holding an LTIDR or STIDR are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), and VD has only a Country Ceiling.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later watch (A35) did not change the rating.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36. A35 is a Rating Watch and A33 is an affirmation.

**Q14.** No rating. E12's first action, A30, is dated 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26 and was not downgraded until A27 (2026-04-15).

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ after A33.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's watch (A35) was superseded by the affirmation in A33, which carries no watch.

**Q19.** E01 and E09. A03 and A25 are the latest actions for E01 and E09, and both carry a negative outlook.

**Q20.** No. E07's last action, A19, is a withdrawal, which says nothing about default.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08. Its RD rating in A22 is a default, and no other record shows RD or D.

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 4. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-). I02 (BB+) and I04 (BB) are speculative grade.

**Q26.** A+. E15's LC rating comes from A40.

**Q27.** A-. The note is I06, and A42 assigned it A-.

**Q28.** BBB+. CV's FC LTIDR comes from A38. The Country Ceiling of A (A37) is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's FC rating is A, equal to the CV ceiling of A. No other country has a ceiling.

**Q31.** No. E05 and E15 are at their ceilings, not above them, and LC ratings are not capped.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes the credit risk of Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent link and nothing connects it to E09, so the data does not show it in the same group as E10.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2. E02 and E03 share an LEI and are one entity, and E04 is its subsidiary.

**Q37.** 16. There are 17 records, and E02 and E03 are the same entity.

**Q38.** No. Their LEIs differ: E06's is ORRN00BANK00000DE233 and E13's is ORBC00BANCORP000US45.

**Q39.** A, from A09.

**Q40.** 5: E01, E02/E03, E09, E12 and E14. E07 is also in GB but was withdrawn.

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
"Q25": {"count": 4},
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
"Q40": {"count": 5}
}
```