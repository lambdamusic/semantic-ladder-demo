**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, is not until 2025-06-20.

**Q2.** No. The only 2026 issuer action on Kestrel (E01) is A03, an affirmation at BBB with the outlook revised to Negative.

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) is the latest action: A, POS.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), the guarantor of I03. Its issuer rating is A (A08, A09).

**Q6.** The foreign-currency rating (A14, BB) is capped by Valdoria's Country Ceiling (A12, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 (A21, A22) and E10 (A27). A29 downgrades an instrument, not an issuer, and E16's A44 is QA data, so it is ignored.

**Q8.** E08. It went to RD (a default) in A22 on 2026-07-08 and had no later action.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E04 and E11 have none (E11 has only a CO, A46), VD has only a Country Ceiling, E07 was withdrawn, and E16 is QA.

**Q10.** No on its headline foreign-currency rating of BB (A14). Its local-currency rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. A36 (2024-09-30) downgraded Marlow (E14) to BBB+, and A35 only placed it on Watch.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36.

**Q14.** None. Halden Foods (E12) was first rated in A30 on 2024-02-01.

**Q15.** A-. A26 set A- for Halden Bank (E10), and the downgrade in A27 is not until 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 is a Watch, A33 an affirmation).

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-.

**Q18.** E06 (A17). E14's Watch from A35 was cleared by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam Retail (E07) was rated BB and then withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, through the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB.

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (foreign-currency BB, ceiling BB) and E15 (foreign-currency A, ceiling A).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11 sits under E10, which sits under E09.

**Q33.** The holder takes the credit risk of Halden Bank (E10), the guarantor of I05. Its rating is BBB+ (A27).

**Q34.** No. Halden Foods (E12) has no parent and no link to E09, and the shared name proves nothing.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10, and E12 is not in the group.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 16. There are 19 records. E16 is QA, and E03 and E17 duplicate E02 and E10 by LEI.

**Q38.** No. They have different LEIs and are separate entities.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in DE.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17.

**Q43.** 0. The only LU record is E17, and RATINGS says that entity is in DE.

**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a Credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated.

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
"Q10": {"investment_grade": "no"},
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