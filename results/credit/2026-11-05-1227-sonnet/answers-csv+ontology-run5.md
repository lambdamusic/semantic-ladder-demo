**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. Kestrel's only 2026 actions are the affirmations A03 (LTIDR) and A04 (STIDR). A03 revised the outlook to Negative, which is not a downgrade.

**Q3.** No. I02 (subordinated) was downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), has a POS outlook.

**Q5.** The holder takes the credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so it follows the guarantor's rating, and E02/E03's latest LTIDR is A (A09).

**Q6.** The Country Ceiling for Valdoria (A12) is BB. It caps the foreign-currency rating (A14: BB), while the local-currency rating is not capped (A13: BBB-).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A44 is on E16, a QA record, so it is ignored. A29 is a downgrade of an instrument (I05), not of an issuer.

**Q8.** E08. A22 moved it to RD (a default) on 2026-07-08 and nothing later changed that.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. I excluded E07 (withdrawn in A19), E04 and E11 (no LTIDR; E11 has only a credit opinion), VD (Country Ceiling only) and the QA record E16.

**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade. The foreign-currency rating is BB (A14), which is not.

**Q11.** BBB+. A36 (2024-09-30) downgraded it to BBB+, and A35 (2025-11-20) came later.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade A36 came later.

**Q13.** 1. Only A36 is a downgrade. A35 is a Rating Watch and A33 is an affirmation.

**Q14.** None. Its first action, A30, is dated 2024-02-01.

**Q15.** A-. E10 and E17 are the same entity, and A26 set A-. The downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (after A36), and A35 and A33 left it at BBB+.

**Q17.** No. A17 is a Rating Watch (RW), which leaves the rating at A-.

**Q18.** E06. Its Watch (A17) was placed on 2026-09-03 and not cleared. E14's Watch (A35) was cleared by the affirmation A33, which carries no watch.

**Q19.** E01 and E09. Their latest actions, A03 and A25, both carry NEG outlooks.

**Q20.** No. A19 withdrew the rating for commercial reasons, which says nothing about default.

**Q21.** E07. A19 withdrew its only issuer rating.

**Q22.** E08. A22 gave it RD, a default.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A02, affirmed in A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are speculative grade. I08 is unrated because EX is only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB (A14) equals Valdoria's ceiling of BB, and E15's FC rating of A (A41) equals Corvenia's ceiling of A (A37). The sovereign CV's FC rating of BBB+ is below its ceiling.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, which is the same entity as E17, and E10's parent is E09, which has no parent.

**Q33.** The holder takes the credit risk of E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent and is not in E09's chain.

**Q35.** 3. The group is E09, E10 (with E17) and E11.

**Q36.** 2. The group is E02 (with E03) and E04.

**Q37.** 16. Of the 19 records, E03 and E17 duplicate E02 and E10 by LEI, and E16 is a QA record.

**Q38.** No. They have different LEIs and are different entities.

**Q39.** A. E03's A09 affirmation on 2025-09-15 is the latest action for this entity.

**Q40.** 5. These are E01, E02, E09, E12 and E14. E10 is domiciled in LU, since the RESEARCH record holds for country. E07 was withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile.

**Q43.** 1. Only Halden Bank (E10/E17) is domiciled in LU.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. Local-currency debt is not capped by the ceiling, and its BBB- is in any case not an FC rating.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected (EX) action, so I08 stays unrated.

**Q48.** 7. I01 through I07 are rated, and I08 is not.

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