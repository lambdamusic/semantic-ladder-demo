**Q1.** A-. The latest E01 LTIDR FC action on or before that date is A01 (A-), and A02 only came in June 2025.
**Q2.** No. E01's only 2026 action is the affirmation A03, and A02 (the downgrade) was in 2025.
**Q3.** No. I02 is rated BB+ after the downgrade A07, which is speculative grade.
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with a POS outlook.
**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk, and E02's current rating is A (A09).
**Q6.** The foreign-currency rating is BB (A14), the same level as the VD Country Ceiling (A12, BB). The local-currency rating is BBB- (A13) and is not capped.
**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is QA data and is ignored, and A29 is an instrument rating.
**Q8.** E08. A22 put it at RD, which is a default, and it is still in force.
**Q9.** 12: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, E11 has only a credit opinion, E04 and VD have no issuer rating, and E16 is QA.
**Q10.** Depends. The foreign-currency rating is BB (speculative) and the local-currency rating is BBB- (investment grade).
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the rating was unchanged on 2025-06-01.
**Q12.** A-, set by A34.
**Q13.** 1, the downgrade A36.
**Q14.** None. E12 was first rated on 2024-02-01 (A30).
**Q15.** A-. E10 and E17 are the same entity, and A26 is still in force on that date (A27 came in April 2026).
**Q16.** No. It was BBB+ on 2025-01-01 (after A36) and is still BBB+ (A33).
**Q17.** No. A17 is a Rating Watch placement, not a downgrade.
**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by the affirmation A33.
**Q19.** E01 (A03) and E09 (A25). E06's A17 carries no outlook, so I have not counted it.
**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal is not a default; its last rating was BB.
**Q21.** E07. Its rating was withdrawn in A19, and E16 is excluded as QA.
**Q22.** E08, which reached RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. The LTIDR is BBB (A03).
**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** E05 and E15. E05's FC rating is BB against a VD ceiling of BB (A14, A12), and E15's is A against a CV ceiling of A (A41, A37).
**Q31.** No. No company is above its ceiling; E05 and E15 are exactly at theirs.
**Q32.** E09. E11's parent is E10, and E10's parent is E09.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and A27 is its current rating.
**Q34.** No. E12 has no parent and is not in E09's chain.
**Q35.** 3: E09, E10 (also record E17) and E11.
**Q36.** 2: E02 (also record E03) and E04.
**Q37.** 16. There are 19 records. E03 duplicates E02 and E17 duplicates E10, which leaves 17, and the QA record E16 is not a real entity.
**Q38.** No. Their LEIs differ (E06 and E13), and there is no other link between them.
**Q39.** A (A09, which is E03, the same entity).
**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 was withdrawn, and E16 is QA.
**Q41.** None. E16 is a QA record, so its actions are ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, and E10 has the same LEI.
**Q43.** 1, the E10/E17 entity.
**Q44.** Yes. I07 pays in XVD, which is the domestic currency of VD, E05's domicile.
**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, and it is rated BBB- (A45).
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.
**Q48.** 7. I01–I07 hold ratings, and I08 does not.

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