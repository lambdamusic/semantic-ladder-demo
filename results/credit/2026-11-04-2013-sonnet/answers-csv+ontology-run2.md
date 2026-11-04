**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the downgrade was in 2025 (A02).

**Q3.** No. I02 is subordinated and its latest rating is BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and the latest action is A09 (POS).

**Q5.** The holder takes the credit risk of E02, the guarantor of I03, whose issuer rating is A (A09, recorded under E03).

**Q6.** The foreign-currency rating is capped by the Valdoria Country Ceiling of BB (A12). The local-currency rating is not capped (A13 BBB- vs A14 BB).

**Q7.** E08 and E10. They were downgraded in 2026 (A21, A22, A27). E16's downgrade (A44) is QA data and is ignored, and A29 is an instrument rating.

**Q8.** E08. It was rated RD from 2026-07-08 (A22), and RD is a default.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E11 has only a credit opinion, E04 and VD have no issuer rating, and E16 is QA.

**Q10.** No. The headline foreign-currency rating is BB (A14), which is speculative grade. The local-currency rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. The downgrade A36 (2024-09-30) applies, and the later actions are a watch and an affirmation.

**Q12.** A-, as assigned in A34 on 2023-01-15.

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26) and downgraded only on 2026-04-15 (A27). E17 is the same entity.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33, A35 and A36 leave it there).

**Q17.** No. A17 is a Rating Watch, which is not a downgrade.

**Q18.** E06 (A17). E14's watch (A35) was cleared by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. The rating was withdrawn for commercial reasons (A19), which is not a default, and its last rating was BB.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The current rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only "expected" (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The ceiling A37 is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05 is FC BB, equal to the VD ceiling of BB (A14, A12). E15 is FC A, equal to the CV ceiling of A (A41, A37).

**Q31.** No. E05 and E15 are exactly at their ceilings, and no other company's country has a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10, the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. E12 has no parent and is not in E09's chain.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records, but E03 duplicates E02, E17 duplicates E10, and E16 is QA, so it describes no real entity.

**Q38.** No. Their LEIs differ (E06 vs E13).

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in LU per the RESEARCH record E17.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile.

**Q43.** 1, which is Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.

**Q45.** No. Local-currency debt is not capped by the ceiling, and I07 is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, so I08 remains unrated.

**Q48.** 7, which is I01 to I07.

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
"Q10": {"investment_grade": "no"},
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