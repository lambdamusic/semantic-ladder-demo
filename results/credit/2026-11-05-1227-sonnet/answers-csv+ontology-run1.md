**Q1.** A. The latest action on or before 1 Jan 2025 is A01 (2024-03-12), which assigned A- (not A). A02's downgrade to BBB only came in June 2025.

**Q2.** No. A03 (2026-02-10) is an affirmation, and the outlook moved to Negative, which is not a downgrade.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15, POS).

**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is guaranteed by E02, and E02/E03's latest LTIDR is A (A09).

**Q6.** Valdoria's Country Ceiling caps foreign-currency ratings but not local-currency ones. The FC rating is BB (A14), equal to the ceiling BB (A12), while the LC rating is BBB- (A13). This one is not in the JSON.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. The other 2026 downgrades are not issuer downgrades: A29 is an instrument and A44 is a QA record.

**Q8.** E08. A22 set RD (restricted default) on 2026-07-08.

**Q9.** 12. These are E01, E02 (same entity as E03), E05, E06, E08, E09, E10 (same entity as E17), E12, E13, E14, E15 and CV. E07 is withdrawn, E04 and E11 have no issuer rating (E11 has only a credit opinion), VD has only a ceiling, and E16 is QA.

**Q10.** Depends. The foreign-currency (headline) rating is BB (speculative grade), but the local-currency rating is BBB- (investment grade) (A13, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the next action was in 2024-09.

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. A26 assigned A- to E10, which is the same entity as E17. The downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The Watch (A35) and affirmation did not change the rating.

**Q17.** No. A17 is a Rating Watch Negative and the rating stays A-.

**Q18.** E06. A17 (2026-09-03) is a Watch Negative. E14's Watch from A35 was followed by A33, which carries no watch.

**Q19.** E01 and E09. A03 and A25 set a Negative outlook, and nothing later changes it.

**Q20.** No. A19 is a withdrawal for commercial reasons, which is not a default.

**Q21.** E07. Its rating was withdrawn (A19). E08 still has a rating (RD).

**Q22.** E08. It reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The LTIDR FC is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A, guaranteed by E02), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are speculative grade, and I08 is unrated.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The Country Ceiling A (A37) is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling record (A12).

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling BB (A12, A14), and E15's FC rating is A, equal to the CV ceiling A (A37, A41).

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. The chain runs E11 → E10 → E09.

**Q33.** The holder takes Halden Bank's credit risk (E10), rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27.

**Q34.** Yes. Halden Foods (E12) has no parent in the data and is not in Halden Group's chain. Halden Bank (E10) is in Halden Group's chain (E10 → E09). The name similarity does not make them related, so I count them as separate groups. The correct answer is **No**.

**Q35.** 3. The Halden group is E09, E10 (same entity as E17) and E11.

**Q36.** 2. The Northwind group is E02 (same entity as E03) and E04.

**Q37.** 16. There are 19 records. Removing the duplicates E03 and E17 and the QA record E16 leaves 16.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09 (E03, same entity as E02).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 is withdrawn, and E10 is domiciled in LU per the RESEARCH record.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile.

**Q43.** 1. Only Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and E05 is domiciled in VD.

**Q45.** No. Local-currency debt is not capped by the ceiling, and I07 is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX), so I08 is unrated.

**Q48.** 7. These are I01 to I07. I08 is unrated.

Correction to Q34: I first wrote "Yes" but my own reasoning supports "No", and the JSON below uses "no".

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