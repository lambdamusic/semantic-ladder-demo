**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02) is not until 2025-06-20.

**Q2.** No. The only 2026 Kestrel actions are affirmations (A03, A04); the downgrade (A02) was in 2025.

**Q3.** No. I02 is subordinated and its latest action (A07) rates it BB+, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action (A09, 2025-09-15) sets POS.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk, and the latest LTIDR is A (A09).

**Q6.** The Valdoria Country Ceiling is BB (A12). It caps the foreign-currency rating (A14: BB), while the local-currency rating (A13: BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is QA data and ignored, and A29 is an instrument rating.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), which counts as a default.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10 (E17 is the same entity), E12, E13, E14, E15 and CV. E07 was withdrawn (A19), and E04, E11 and VD have no issuer rating.

**Q10.** Depends. The foreign-currency rating is BB (speculative grade), but the local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and no rating change followed before 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1, from A36. The A35 watch and the A33 affirmation are not downgrades.

**Q14.** None. Halden Foods' first rating (A30) is dated 2024-02-01.

**Q15.** A-. A26 assigned A- on 2023-05-01, and the downgrade (A27) came on 2026-04-15. E17 is the same entity as E10.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). The watch in A35 did not change it.

**Q17.** No. A17 is a Rating Watch action that leaves the rating at A-.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's watch (A35) was cleared by the A33 affirmation, which carries no watch.

**Q19.** E01 and E09, from A03 and A25. E06's A17 has no outlook value, so it cannot be counted as Negative.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which says nothing about default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only an expected rating.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The Country Ceiling (A37) is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB (A14) equals the VD ceiling of BB, and E15's A (A41) equals the CV ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings, not above, and no other company's country has a ceiling in the data.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent, so it is not in E09's group.

**Q35.** 3: E09, E10 and E11 (E17 is the same entity as E10).

**Q36.** 2: E02 and E04 (E03 is the same entity as E02).

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA test data.

**Q38.** No. They have different LEIs (E06 and E13), so they are different entities.

**Q39.** A, from A09 (E03 is the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA data.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. RESEARCH holds on domicile, and E17 says LU.

**Q43.** 1: Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of Valdoria, the issuer E05's country.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47) and no assignment yet.

**Q48.** 7: I01 to I07. I08 is still unrated.

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