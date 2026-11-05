**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01), and the next action is dated 2025-06-20 (A02).
**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the downgrade was in 2025 (A02).
**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.
**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 affirmed A with a POS outlook on 2025-09-15.
**Q5.** The holder takes E02's (Northwind Holdings) credit risk, rated A. I03 is guaranteed by E02, whose latest rating is A (A08, A09).
**Q6.** No JSON field for this one. Valdoria's Country Ceiling is BB (A12), and it caps the foreign-currency rating (A14: BB), while the local-currency rating is not capped (A13: BBB-).
**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A44 is a QA record and is ignored, and A29 is an instrument rating, not an issuer rating.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and RD is a default.
**Q9.** 12. These are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), E04 and E11 have no issuer rating (E11 has only a credit opinion, A46), VD has only a ceiling, and E16 is QA.
**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade, but the foreign-currency rating is BB (A14), which is not.
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and nothing changed it before 2025-06-01.
**Q12.** A-, from A34 (2023-01-15).
**Q13.** 1, which is A36. A33 is an affirmation and A35 is a Rating Watch.
**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).
**Q15.** A-. E10 was assigned A- (A26), and the downgrade to BBB+ came on 2026-04-15 (A27).
**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).
**Q17.** No. E06 was only placed on Rating Watch (A17), and its rating stayed A-.
**Q18.** E06 (A17, 2026-09-03). E14's Watch from A35 was cleared by the affirmation A33.
**Q19.** E01 (A03) and E09 (A25). E02/E03 has a Positive outlook.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal says nothing about default.
**Q21.** E07, whose rating was withdrawn (A19).
**Q22.** E08, which reached RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's LTIDR FC is BBB (A03), which is investment grade.
**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 only has an expected rating (A47, EX), so it is unrated.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38). The Country Ceiling (A37) is not the sovereign's rating.
**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.
**Q30.** E05 and E15. E05's FC rating is BB (A14) against the VD ceiling of BB (A12), and E15's is A (A41) against the CV ceiling of A (A37).
**Q31.** No. No company's FC rating exceeds its country's ceiling.
**Q32.** E09. E11's parent is E10 (RATINGS), and E10's parent is E09.
**Q33.** The holder takes E10's (Halden Bank) credit risk, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ (A27).
**Q34.** No. E12 has no parent link, so it is not in E09's group.
**Q35.** 3: E09, E10 (the same entity as E17) and E11.
**Q36.** 2: E02 (the same entity as E03) and E04.
**Q37.** 16. The 19 records include two duplicates (E03 = E02 and E17 = E10), and E16 is QA test data describing no real entity.
**Q38.** No. Their LEIs differ.
**Q39.** A (A09).
**Q40.** 5: E01, E02, E09, E12 and E14. E10 is excluded because RESEARCH places it in LU, E07 was withdrawn, and E16 is QA.
**Q41.** None. E16 is a QA record, so it and its actions are ignored.
**Q42.** LU. RESEARCH holds on domicile (E17), overriding the DE in E10.
**Q43.** 1, the Halden Bank entity (E10/E17).
**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.
**Q45.** No. I07 is BBB- (A45), but local-currency debt is not capped by the ceiling.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an expected rating (A47, EX), so it stays unrated.
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