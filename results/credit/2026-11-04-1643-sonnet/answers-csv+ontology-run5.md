**Q1.** A-. E01's LTIDR (FC) was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20.

**Q2.** No. E01's only 2026 actions (A03, A04) are affirmations; the downgrade A02 was in 2025.

**Q3.** No. I02 is subordinated and was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action (A09, 2025-09-15) gives a POS outlook.

**Q5.** A holder takes E02's credit risk, and E02 is rated A. I03 is guaranteed by E02 (not issued on E04's own credit), and the latest LTIDR on E02/E03 is A (A09).

**Q6.** The foreign-currency rating is held at the Country Ceiling. VD's ceiling is BB (A12), which caps E05's FC rating (A14, BB) but not its LC rating (A13, BBB-).

**Q7.** E08 and E10. These are the issuers with 2026 downgrades (A21 and A22 for E08, A27 for E10). E16's downgrade (A44) is QA test data and is ignored, and A29 is an instrument downgrade.

**Q8.** E08. It was rated RD, a default, on 2026-07-08 (A22), with no later action.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. E05 is BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and that held on 2025-06-01.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34).

**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 is an affirmation.

**Q14.** None. E12's first rating action is 2024-02-01 (A30).

**Q15.** A-. E10 and E17 share an LEI, and A26 (A-) held until the downgrade on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 did not change it).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which leaves the rating unchanged at A-.

**Q18.** E06. It was placed on RWN on 2026-09-03 (A17). E14's watch (A35) was ended by the affirmation A33, which carries no watch.

**Q19.** E01 and E09. They were affirmed with a NEG outlook in A03 and A25.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal says nothing about default.

**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).

**Q22.** E08. It reached RD on 2026-07-08 (A22).

**Q23.** F2. E01's STIDR was affirmed at F2 on 2026-02-10 (A04).

**Q24.** Yes. E01's current LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) were investment grade. I02 (BB+) and I04 (BB) were not, and I08 is unrated.

**Q26.** A+. E15's LC LTIDR was assigned A+ (A40).

**Q27.** A-. I06 was assigned A- (A42).

**Q28.** BBB+. CV's LTIDR (FC) was assigned BBB+ (A38). The A in A37 is the Country Ceiling, not the rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. E05 (BB) and E15 (A) are both at their ceilings, not above them, and GB, DE and the other countries have no ceiling in the data.

**Q32.** E09. E11 is owned by E10, which is owned by E09. E17 shows no parent, but the RATINGS record for E10 holds.

**Q33.** A holder takes E10's credit risk, and E10 is rated BBB+. I05 is guaranteed by E10, and E10 was downgraded to BBB+ (A27).

**Q34.** No. E12 has a different LEI and no parent link to E09 or E10.

**Q35.** 3. The group is E09, E10 and E11, and E17 is a duplicate of E10.

**Q36.** 2. The group is E02 and E04, and E03 is a duplicate of E02.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA test data, which leaves 16.

**Q38.** No. Their LEIs differ (ORRN… vs ORBC…), and the shared "Orrin" name is not an identifier.

**Q39.** A (A09).

**Q40.** 5. The GB issuers with a rating were E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record for E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. Only the RESEARCH record E17 says LU, and the RATINGS record gives DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap, and its BBB- (A45) sits above VD's BB ceiling without breaching it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47, EX), so it stays unrated until an assignment.

**Q48.** 7. I01 to I07 held ratings, and I08 did not.

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