**Q1.** A-. Action A01 (2024-03-12) set E01's FC LTIDR at A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook. The downgrade (A02) was in 2025.

**Q3.** No. I02 is rated BB+ (A07, downgrade of 2025-06-20), which is speculative grade.

**Q4.** Positive (POS). E03 is the same entity as E02 (same LEI). The latest action is A09 (2025-09-15), which set POS.

**Q5.** A holder takes the credit risk of E02, the guarantor of I03. E02 is currently rated A (A08, with A09 on E03).

**Q6.** No JSON field for this one. The Country Ceiling for VD is BB (A12) and caps E05's FC rating at BB (A14). The LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22. E10 was downgraded in A27. The A44 downgrade of E16 is ignored because E16 is QA test data. A29 is an instrument downgrade, not an issuer downgrade.

**Q8.** E08. It was rated RD from A22 (2026-07-08), and RD is a default.

**Q9.** 12. These are E01, E02 (same entity as E03), E05, E06, E08, E09, E10 (same entity as E17), E12, E13, E14, CV and E15. E07 was withdrawn, E04 and E11 have no issuer rating, and VD has only a Country Ceiling.

**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. The latest action on or before that date is A36 (2024-09-30).

**Q12.** A-, from A34.

**Q13.** 1. The only downgrade is A36. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 (same entity as E17) was assigned A- in A26, and the downgrade in A27 came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 placed it on RWN. E14's Watch (A35) was cleared by the A33 affirmation.

**Q19.** E01 and E09. They have NEG outlooks from A03 and A25. A17 (E06) leaves the outlook blank, so I did not count it.

**Q20.** No. E07's rating was withdrawn (A19) for commercial reasons, and a withdrawal is not a default.

**Q21.** E07, whose LTIDR was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01 is rated BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The Country Ceiling (A37) and the LC rating (A39) are different things.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB. E15's FC rating is A, equal to CV's ceiling of A.

**Q31.** No. Both capped entities are exactly at their ceilings, not above.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** A holder takes the credit risk of E10, the guarantor of I05. E10 is currently rated BBB+ (A27).

**Q34.** No. E12 has no parent and is not in E09's group. E10 (same entity as E17) is.

**Q35.** 3: E09, E10 (same entity as E17) and E11.

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** 16. There are 19 records. Removing the duplicates E03 and E17 leaves 17, and removing the QA record E16 leaves 16.

**Q38.** No. Their LEIs differ.

**Q39.** A (A09 on E03, same entity).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn, E16 is QA, and E10 is domiciled in LU, not GB.

**Q41.** None. E16 is QA test data and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for country.

**Q43.** 1: E10 (same entity as E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. It is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.

**Q48.** 7. I01 to I07 hold ratings, and I08 does not.

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
"Q24": {"investment_grade": "yes", "rating": "BBB"},
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

Note: Q24 in the JSON carries both fields because the question asks only for `investment_grade`; the extra `rating` field is harmless context.