**Q1.** A-. E01's latest action on or before 1 Jan 2025 is A01 (A-). The downgrade A02 came in June 2025.

**Q2.** No. E01's only 2026 issuer actions are affirmations (A03, A04).

**Q3.** No, BB+. I02 was assigned BBB (A23) and downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and the latest action is A09 (A, POS).

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so the holder takes E02's risk. E02's latest rating is A (A09).

**Q6.** Valdoria's Country Ceiling is BB (A12) and caps the foreign-currency rating (A14, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. The 2026 downgrades are A21 and A22 (E08) and A27 (E10). A29 is an instrument rating, and A44 is a QA record, so I ignored it.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and RD counts as default.

**Q9.** 12. Counting distinct entities that hold an LTIDR/STIDR on 1 Oct 2026: E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn. E11 has only a credit opinion, and VD has only a ceiling.

**Q10.** Depends. The foreign-currency rating is BB (speculative, A14) and the local-currency rating is BBB- (investment grade, A13).

**Q11.** BBB+. A36 (2024-09-30) set BBB+ and it held through 1 Jun 2025.

**Q12.** A-. A34 (2023-01-15) set A-, and the downgrade A36 came later.

**Q13.** 1, which is A36. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first action is A30 on 2024-02-01.

**Q15.** A-. E17 shares E10's LEI, and A26 set A-. The downgrade A27 came in April 2026.

**Q16.** No. It was BBB+ on 1 Jan 2025 and is BBB+ now (A33, A35 and A36 did not change that).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 placed it on RWN. E14's Watch (A35) was superseded by A33, which carries no Watch.

**Q19.** E01 and E09. A03 and A25 set the NEG outlooks. E06 and E08 have blank outlooks in their latest actions, so nothing is recorded as Negative.

**Q20.** No. E07 was withdrawn (A19), and a withdrawal is not a default. No default is recorded.

**Q21.** E07. Its rating was withdrawn by A19.

**Q22.** E08. It reached RD in A22, and no other entity has RD or D.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The ceiling A37 is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling BB (A14, A12). E15's FC rating is A, equal to CV's ceiling A (A41, A37).

**Q31.** No. No company's FC rating exceeds its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent and a different LEI, so nothing links it to E09's group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 16. The file has 19 records. E03 and E17 are duplicates by LEI, and E16 is QA, so I excluded all three. The two sovereigns count as entities.

**Q38.** No. Their LEIs differ (E06 vs E13).

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E16 is QA and E07 is withdrawn.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. RATINGS holds over the RESEARCH record (E17, LU).

**Q43.** 0. The only LU record, E17, is a duplicate of E10, which RATINGS places in DE.

**Q44.** Yes. I07 is in XVD, VD's domestic currency.

**Q45.** No. I07 is local-currency, so the ceiling doesn't apply to it. It is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an expected rating (A47, EX) and no assignment.

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