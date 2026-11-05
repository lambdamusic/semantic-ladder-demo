**Q1.** A-. E01's long-term foreign-currency rating was set at A- by A01 (2024-03-12) and held until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a negative outlook, which is not a downgrade.

**Q3.** No. I02, the subordinated 2031 note, was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and its latest action is A09 (2025-09-15, outlook POS).

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and the entity's latest long-term rating is A (A09).

**Q6.** The Valdoria Country Ceiling is BB (A12). E05's foreign-currency rating is capped at BB (A14), while its local-currency rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is QA test data and is ignored, and A29 is an instrument rating.

**Q8.** E08. It has been at RD, a default, since A22 (2026-07-08).

**Q9.** 12. These are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, and E11, E04 and VD have no issuer rating.

**Q10.** Depends. E05's foreign-currency rating is BB (speculative) and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+, from the downgrade in A36 (2024-09-30). The watch in A35 came later and did not change the rating.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10 (the same entity as E17) was rated A- from A26 until the downgrade in A27 on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+ after A35 and A33.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative placement, which is not a downgrade. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06, from A17 (2026-09-03). E14's watch (A35) was superseded by the affirmation in A33.

**Q19.** E01 and E09, from A03 and A25. E06's outlook is not restated in A17, and its last stated outlook was stable.

**Q20.** No. E07's rating was withdrawn in A19 for commercial reasons, which is not a default.

**Q21.** E07. Its rating was withdrawn in A19, and no other entity lost its rating.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals the VD ceiling of BB (A14, A12), and E15's A equals the CV ceiling of A (A41, A37).

**Q31.** No. No company's foreign-currency rating exceeds its country's ceiling, and only VD and CV have ceilings.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest rating is A27 (BBB+).

**Q34.** No. E12 has no parent link to E09, so it is not in that group.

**Q35.** 3. These are E09, E10 (the same entity as E17) and E11.

**Q36.** 2. These are E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. E17 duplicates E10 and E03 duplicates E02, and E16 is QA test data.

**Q38.** No. The two records have different LEIs.

**Q39.** A (A09).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile, overriding E10's DE.

**Q43.** 1. Only the entity recorded as E10 and E17 is domiciled in LU.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap, and its BBB- rating (A45) is above the BB ceiling anyway.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7. I01 to I07 are rated, and I08 is not.

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