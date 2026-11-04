**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the downgrade A02 was in 2025.

**Q3.** No. I02 was cut to BB+ by A07, and BB+ is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action, affirming A with a POS outlook.

**Q5.** The guarantor E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and E02's current FC LTIDR is A (A08, A09).

**Q6.** The data doesn't state the reason, but it fits the Country Ceiling. Valdoria's ceiling is BB (A12), so E05's FC rating is BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 is an instrument rating and A44 is a QA record, so both are excluded.

**Q8.** E08. It has been at RD (A22) since 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E04, E11 and VD have no issuer rating, E07 is withdrawn and E16 is QA.

**Q10.** Depends. E05's LC rating is BBB- (investment grade) but its FC rating is BB (speculative grade).

**Q11.** BBB+. A36 (2024-09-30) set it, and the Watch in A35 came later.

**Q12.** A-, set by A34.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch placement.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. A26 set it and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33 affirmed it).

**Q17.** No. E06's only 2026 action is A17, a Watch placement.

**Q18.** E06. A17 is its latest action and carries RWN. E14's earlier Watch (A35) was superseded by A33.

**Q19.** E01 and E09. A03 and A25 are their latest actions and carry a NEG outlook.

**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal says nothing about default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05 is at BB against the VD ceiling of BB, and E15 is at A against the CV ceiling of A.

**Q31.** No. Neither E05 nor E15 is above its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor E10 (Halden Bank), rated BBB+ (A27). I05 is guaranteed by E10.

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3: E09, E10 (with E17) and E11.

**Q36.** 2: E02 (with E03) and E04.

**Q37.** 16. The 19 records collapse to 17 entities because E03 matches E02 and E17 matches E10 by LEI, and I excluded the QA record E16.

**Q38.** No. Their LEIs differ (E06 vs E13).

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn, E16 is QA, and E10 is domiciled in DE.

**Q41.** None. E16 is a QA record and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, over the RESEARCH record E17's LU.

**Q43.** 0. The only LU record is E17, and E10's RATINGS record gives DE.

**Q44.** Yes. I07 pays in XVD, which is VD's domestic currency, and E05 is domiciled in VD.

**Q45.** No. I07 is local-currency debt, so the ceiling doesn't apply to it. It is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, and no Assigned action has confirmed it.

**Q48.** 7. I01 to I07 are rated, and I08 is unrated.

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