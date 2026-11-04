**Q1.** A-. A01 assigned A- on 2024-03-12, and the next Kestrel action (A02) came on 2025-06-20.

**Q2.** No. The only 2026 Kestrel actions are A03 and A04, which are affirmations (AF); the downgrade A02 was in 2025.

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and the latest action, A09 (2025-09-15), carries a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02, guarantor of I03), rated A. The latest action is A09, recorded under E03, the same entity as E02.

**Q6.** Valdoria's Country Ceiling (A12) is BB, and it caps foreign-currency ratings (A14: BB). Local-currency ratings are not capped (A13: BBB-).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27 (E17 is the same entity). E16's downgrade (A44) is QA data and is ignored; E06's action (A17) is a Watch, not a downgrade.

**Q8.** E08. A22 downgraded it to RD (restricted default), and nothing followed.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), E16 is QA, and E11 and VD have only a credit opinion (CO) or a Country Ceiling (CC), which are not issuer ratings.

**Q10.** Depends. The foreign-currency rating is BB (A14, speculative grade) and the local-currency rating is BBB- (A13, investment grade).

**Q11.** BBB+. A36 downgraded it on 2024-09-30; the Watch in A35 came later.

**Q12.** A-, from A34.

**Q13.** 1, which is A36.

**Q14.** None. Halden Foods' first rating (A30) was assigned on 2024-02-01.

**Q15.** A-. This is E10 (E17 is the same entity), assigned in A26, with the downgrade in A27 not until April 2026.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 was a Watch and A33 an affirmation.

**Q17.** No. A17 in 2026 is a Rating Watch with the rating unchanged.

**Q18.** E06, from A17. E14's Watch (A35) was cleared by the A33 affirmation, which has no watch.

**Q19.** E01 (A03) and E09 (A25). A17 for E06 leaves the outlook blank, so I used its last stated outlook, Stable.

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn in A19. E16 is excluded as QA.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The current rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The Country Ceiling (A37) is a separate thing.

**Q29.** None. Valdoria has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB (A14), equal to Valdoria's ceiling of BB. E15's is A (A41), equal to Corvenia's ceiling of A.

**Q31.** No. Neither foreign-currency rating exceeds its ceiling, and only VD and CV have ceilings.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes Halden Bank's credit risk (E10, guarantor of I05), rated BBB+ (A27).

**Q34.** No. E12 has no parent, so it is not in E09's group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records; E03 and E17 duplicate E02 and E10, and E16 is QA.

**Q38.** No. They have different LEIs and are different entities.

**Q39.** A, from A09. This is the E03 record, which is the same entity as E02.

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is DE in the RATINGS record, and E07 and E16 are excluded.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record (E10) takes precedence over the RESEARCH record (E17: LU).

**Q43.** 0. The only LU record is E17, which is a RESEARCH duplicate of E10 (DE).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and its issuer E05 is domiciled in VD.

**Q45.** No. The ceiling caps only foreign-currency debt, and I07 is local-currency.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected (EX) rating, so I08 stays unrated.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```