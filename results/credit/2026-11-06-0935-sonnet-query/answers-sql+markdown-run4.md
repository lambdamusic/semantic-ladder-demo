**Q1.** A-. Kestrel's rating was A- from A01 until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only 2026 actions on Kestrel are affirmations (A03, A04).

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** POS. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15, POS).

**Q5.** A holder takes the credit risk of E02 (Northwind Holdings), the guarantor of I03. Its rating is A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), and foreign-currency ratings are capped at the ceiling. Valdoria Telecom's FC rating is therefore BB (A14), while its uncapped LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 has DG actions A21 and A22, and E10 has DG action A27. E16 is QA data and is ignored.

**Q8.** E08. It was at RD from 2026-07-08 (A22), and RD counts as default.

**Q9.** 12. These are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. Its FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1 (A36).

**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30).

**Q15.** A- (A26). The downgrade to BBB+ came on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+. The watch (A35) and its later affirmation (A33) did not change it.

**Q17.** No. Orrin Bank's only 2026 action is a Rating Watch (A17), which is not a downgrade.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). E06's watch action carries no outlook, so I did not count it.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07 (withdrawn, A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 (BB+) and I04 (BB) are not, and I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, CV ceiling A).

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** A holder takes the credit risk of E10 (Halden Bank), the guarantor of I05. Its current rating is BBB+ (A27).

**Q34.** No. E12 has no parent link and is not in E09's group.

**Q35.** 3. The group is E09, E10 (E17 is the same entity) and E11.

**Q36.** 2. The group is E02 (E03 is the same entity) and E04.

**Q37.** 16. That is 19 records, less the duplicates E03 and E17 and the QA record E16.

**Q38.** No. Their LEIs differ.

**Q39.** A (A08, A09).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, and it shares an LEI with E10.

**Q43.** 1. Only E17 is in LU, and it is the same entity as E10.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB-, but it is local-currency debt and is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an expected rating (A47), so it is unrated.

**Q48.** 7. I01–I07 held ratings, and I08 did not.

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