**Q1.** A-. A01 assigned A- on 2024-03-12 and it ran until A02 on 2025-06-20.

**Q2.** No. Kestrel's only 2026 action is A03 (2026-02-10), an affirmation at BBB; the downgrade A02 was in 2025.

**Q3.** No, it is BB+. I02 was downgraded to BB+ by A07 (A23's BBB was superseded).

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) supersedes A08 with outlook POS.

**Q5.** E02, rated A. I03 is guaranteed by E02 (so the risk is the guarantor's), and E02's in-force rating is A (A09).

**Q6.** The data doesn't give a reason. It shows only FC BB (A14) against LC BBB- (A13), with a Country Ceiling of BB (A12). Here the local-currency rating is the higher one.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. E16's downgrade (A44) is on a QA test record, so I excluded it.

**Q8.** E08. A22 is an RD rating, in force since 2026-07-08.

**Q9.** 12. In-force issuer ratings are held by E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is withdrawn, E16 is a test record, and E04, E11 and VD have no issuer rating.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) was in force on 2025-06-01.

**Q12.** A-. A34 was in force on 2024-01-01.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. E12's first rating (A30) came on 2024-02-01.

**Q15.** A-. E17 shares E10's LEI, and A26 was in force until A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). A35 was only a watch placement.

**Q17.** No. A17 is a Rating Watch Negative placement, not a downgrade.

**Q18.** E06. A17 (2026-09-03) is in force. E14's watch (A35) was superseded by A33.

**Q19.** E01 and E09. A03 and A25 carry a Negative outlook. A17 has no outlook.

**Q20.** No. A19 withdrew the rating, and the last rating (BB) was not a default rating.

**Q21.** E07. Its rating was withdrawn by A19.

**Q22.** E08. A22 is an RD rating.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 is only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB (A12, A14). E15's is A, equal to the CV ceiling of A (A37, A41).

**Q31.** No. E05 and E15 sit exactly at their ceilings, not above.

**Q32.** E09. E11's parent is E10, whose RATINGS record gives E09 as parent.

**Q33.** E10, rated BBB+. E10 is the guarantor of I05, and A27 is in force.

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3: E09, E10 (=E17) and E11.

**Q36.** 2: E02 (=E03) and E04.

**Q37.** 16. The 19 entity records merge to 17 distinct entities (E02=E03 and E10=E17 by LEI), and I excluded E16 as a QA test record.

**Q38.** No. They have different LEIs and no sameEntityAs link.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 is withdrawn, and E16 is a test record.

**Q41.** None. E16 is a QA test record, so its actions are not rating actions in force.

**Q42.** LU. The RESEARCH record E17 gives LU, and it is the same entity as E10.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, and the issuer E05 is domiciled in VD, whose domestic currency is XVD.

**Q45.** No. The ceiling (BB) caps foreign-currency issuer ratings, and I07 is a local-currency instrument, so BBB- is not a breach.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating, which is not a rating in force.

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