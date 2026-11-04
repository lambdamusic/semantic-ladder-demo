**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02) came in June 2025.

**Q2.** No. The only 2026 Kestrel actions are affirmations (A03, A04); the downgrade to BBB was A02 in 2025.

**Q3.** No. I02 was cut to BB+ (A07, 2025-06-20), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and A08/A09/A11 show A.

**Q6.** The Country Ceiling for Valdoria is BB (A12), which caps foreign-currency ratings. Valdoria Telecom's local-currency rating is BBB- (A13) and its foreign-currency rating is BB (A14).

**Q7.** E08, E10 and E16. Their 2026 issuer-rating downgrades are A21/A22, A27 and A44. I05's downgrade (A29) is an instrument action, and its issuer E11 has no issuer rating.

**Q8.** E08. It was rated RD from 2026-07-08 (A22).

**Q9.** 13. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. Valdoria Telecom is BBB- (investment grade) in local currency (A13) but BB (not investment grade) in foreign currency (A14).

**Q11.** BBB+ (A36, 2024-09-30).

**Q12.** A- (A34).

**Q13.** 1 time. Only A36 is a downgrade (A- to BBB+).

**Q14.** None. Halden Foods was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 is the same LEI.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33, A35).

**Q17.** No. A17 is only a Rating Watch Negative placement, with A- unchanged.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the 2026-05-01 affirmation (A33) with a STA outlook.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which was rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05 is BB against Valdoria's BB ceiling (A14, A12), and E15 is A against Corvenia's A ceiling (A41, A37).

**Q31.** No. No foreign-currency issuer rating exceeds its country's ceiling.

**Q32.** E09, via E11 to E10 to E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is issued by E11 and guaranteed by E10, whose rating is BBB+ after A27.

**Q34.** No. E12 has no parent link and nothing in the data ties it to E09's group, so the shared name alone is not evidence.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 and E04. E03 duplicates E02 by LEI.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10, going by the shared LEIs.

**Q38.** No. They have different LEIs and countries (E06 and E13), and no link between them.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 in the RATINGS system says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a RESEARCH duplicate of the German-domiciled E10.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's currency, and its BBB- matches the local-currency rating (A13, A45). The data does not define XVD explicitly.

**Q45.** No. The BB ceiling caps foreign-currency ratings, and I07 is a local-currency obligation.

**Q46.** No. E11 has only a "CO" rating-type record (A46), not an issuer rating (LTIDR or STIDR).

**Q47.** None. I08's rating was marked EX (expired) on 2026-09-01 (A47), before the 2034 maturity.

**Q48.** 7. I01–I07 are rated, and I08's rating expired (A47).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10", "E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 13},
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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```