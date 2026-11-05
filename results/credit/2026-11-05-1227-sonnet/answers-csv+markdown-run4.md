**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, is dated 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action with outlook POS.

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, which is rated A. I03 is guaranteed by E02, and A09 affirmed E02 at A.

**Q6.** The Country Ceiling for VD is BB (A12), which caps the foreign-currency rating (A14, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 downgrades an instrument, and A44 is a QA record, so both are excluded.

**Q8.** E08. A22 put it at RD on 2026-07-08, and RD counts as default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15.

**Q10.** Depends. The foreign-currency rating is BB (speculative) and the local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E17 is the same entity as E10, and A26 set A- until A27 on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+; A35 was a watch and A33 an affirmation.

**Q17.** No. A17 is a Rating Watch, not a downgrade.

**Q18.** E06. A17 placed it on RWN. E14's watch (A35) was cleared by A33.

**Q19.** E01 and E09 (A03 and A25 carry a negative outlook). E06's latest action, A17, has no outlook recorded, so I excluded it.

**Q20.** No. E07's rating was withdrawn (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. A37 is the Country Ceiling, not the rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals the VD ceiling of BB, and E15's A equals the CV ceiling of A.

**Q31.** No.

**Q32.** E09. The chain runs E11 → E10 → E09.

**Q33.** The holder takes the credit risk of E10, Halden Bank, which is rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent and is not in E09's group.

**Q35.** 3. The group is E09, E10 and E11, and E17 is the same entity as E10.

**Q36.** 2. The group is E02 and E04, and E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates, and E16 is a QA record, which leaves 16.

**Q38.** No. Their LEIs differ.

**Q39.** A, from A09 on E03, which is the same entity as E02.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in LU.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds on domicile.

**Q43.** 1, which is E10 (via E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

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