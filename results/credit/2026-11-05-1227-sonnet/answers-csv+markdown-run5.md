**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action on E01 LTIDR FC (A02) is not until 2025-06-20.
**Q2.** No. E01's only 2026 action is A03, an affirmation (the outlook moved to NEG), which is not a downgrade.
**Q3.** No, it is BB+. I02 is subordinated and was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), set POS.
**Q5.** The holder takes the credit risk of E02, the guarantor of I03, rated A (A09 via E03, same LEI).
**Q6.** The foreign-currency rating is capped by the Country Ceiling. VD's ceiling is BB (A12), and E05's FC rating is BB (A14) while its LC rating is BBB- (A13), which the ceiling does not cap.
**Q7.** E08 (A21 and A22) and E10 (A27). The E16 downgrade (A44) is QA test data and is ignored.
**Q8.** E08. It went to RD, a default, on 2026-07-08 (A22).
**Q9.** 12: E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn, E11 has only a credit opinion, and E04 and VD have no issuer rating (VD has only a Country Ceiling). E16 is QA and is ignored.
**Q10.** Depends. Its LC rating is BBB- (investment grade, A13) but its headline FC rating is BB (speculative, A14).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 on 2025-11-20 was only a Watch.
**Q12.** A-. A34 assigned A- on 2023-01-15.
**Q13.** 1. Only A36 is a downgrade; A33 is an affirmation and A35 is a Watch.
**Q14.** None. E12's first rating, A30, is dated 2024-02-01.
**Q15.** A-. E17 is the same entity as E10, and A26 holds until the 2026-04-15 downgrade (A27).
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ now; A35 and A33 did not change the rating.
**Q17.** No. A17 is a Rating Watch placement, and the rating stays A-.
**Q18.** E06 (A17, 2026-09-03). E14's Watch (A35) was cleared by A33, which has no watch value.
**Q19.** E01 (A03) and E09 (A25).
**Q20.** No. A19 withdrew E07's rating for commercial reasons, which is not a default, and its last rating was BB.
**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).
**Q22.** E08, which reached RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. E01's LTIDR FC is BBB (A03).
**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 only has an expected rating (A47, EX), so it is unrated.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** E05 (FC BB, equal to the VD ceiling of BB) and E15 (FC A, equal to the CV ceiling of A).
**Q31.** No. No company's FC rating exceeds its ceiling; only VD and CV have ceilings.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The holder takes the credit risk of E10, the guarantor of I05, rated BBB+ (A27).
**Q34.** No. E12 has no parent and is not in E09's group, while E10 and E17 are the same entity under E09.
**Q35.** 3: E09, E10 (with E17, same LEI) and E11.
**Q36.** 2: E02 (with E03) and E04.
**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10, and E16 is QA.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A09).
**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 is withdrawn, and E16 is QA.
**Q41.** None. E16 is QA test data and is ignored.
**Q42.** LU. The RESEARCH record (E17) holds for domicile, overriding DE on E10.
**Q43.** 1: Halden Bank (E10 and E17).
**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.
**Q45.** No. It is local-currency debt, so the ceiling does not cap it.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. A47 is only an expected rating (EX), so I08 is unrated.
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

Note: Q24 reports the rating as BBB, and Q3 as BB+. Q2 and Q3 also hold regardless of the QA records.