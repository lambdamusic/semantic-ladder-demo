**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action on E01's LTIDR (A02) came only in June 2025.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, and both are affirmations.

**Q3.** No. The 2031 note (I02) was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and the latest action, A09 on 2025-09-15, gives POS.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), the guarantor of I03. E02's current rating is A (A09).

**Q6.** The Valdoria Country Ceiling is BB (A12), and it caps foreign-currency ratings. E05's FC rating is BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27, which also covers E17, the same entity. A44 is on E16, a QA record, so it is ignored. I05's downgrade (A29) is an instrument action, not an issuer one.

**Q8.** E08. A22 moved it to RD, which is a default, on 2026-07-08.

**Q9.** 12. The issuers are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn. E11 has only a credit opinion and VD only a ceiling. E04 and E16 have no issuer rating.

**Q10.** Depends. Its FC rating is BB (speculative grade) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and that held until the later watch and affirmation.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade did not come until September 2024.

**Q13.** 1. A36 is the only downgrade.

**Q14.** None. E12's first rating action (A30) is dated 2024-02-01.

**Q15.** A-. A26 set A- for E10 (the same entity as E17), and the downgrade (A27) came after 2026-01-01.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+ now (A33, A35).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement, and the rating stays at A-.

**Q18.** E06. A17 placed it on RWN. E14's RWN (A35) was cleared by the 2026-05-01 affirmation (A33).

**Q19.** E01 and E09 (A03, A25). E06's outlook is blank after A17, so I did not count it.

**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07. It was rated from A18 and withdrawn by A19.

**Q22.** E08. A22 moved it to RD, a default.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's FC rating is A, equal to the CV ceiling of A.

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no other entity has a ceiling that applies.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the risk of Halden Bank (E10), the guarantor of I05. E10's current rating is BBB+ (A27).

**Q34.** No. E12 has no parent, so it is not in the E09 group.

**Q35.** 3: E09, E10 (with E17) and E11.

**Q36.** 2: E02 (with E03) and E04.

**Q37.** 16. There are 19 records. E03 duplicates E02 and E17 duplicates E10, and E16 is QA test data.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09 affirmed A).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is not GB, and E07 was withdrawn.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH (E17) holds for domicile, overriding the DE on the RATINGS record.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, the issuer's country.

**Q45.** No. It is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. A08 for I08 is only an expected rating (EX), so the note stays unrated.

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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```