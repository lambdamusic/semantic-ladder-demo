**Q1.** A-. A01 assigned E01 A- on 2024-03-12, and nothing changed it before 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook. The downgrade to BBB was A02 in 2025.

**Q3.** No. I02 is rated BB+ (A07, 2025-06-20), which is below investment grade. It was BBB at assignment (A23).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity. A09 (2025-09-15) is the latest action and affirms A with a POS outlook, replacing A08's STA.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (I03 guarantor_id). A11 rates the note A, and E02 holds A.

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16. The 2026 downgrades are A21 and A22 (E08), A27 (E10) and A44 (E16). A29 downgrades the I05 instrument, not an issuer.

**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), VD has only a Country Ceiling, and E11 has only a CO record.

**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade. The foreign-currency rating is BB (A14), which is not.

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade. A33 is an affirmation and A35 is a watch.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26. The record E17 shares its LEI. The downgrade to BBB+ (A27) came in April 2026.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33 affirmed it). The 2025 watch (A35) did not change the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating kept at A-.

**Q18.** E06. A17 (2026-09-03) is still in force. E14's watch (A35) was resolved by the A33 affirmation.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07 has never been in default. Its rating was withdrawn for commercial reasons (A19).

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01 is rated BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 has expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB (A14), equal to Valdoria's BB ceiling. E15's is A (A41), equal to Corvenia's A ceiling (A37). CV itself is BBB+, below its ceiling.

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link to the Halden group, and only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10 (matching LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and names, and no link between them.

**Q39.** A (A09 affirmed it; the earlier A08 assigned A).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn, and E10 is domiciled in DE.

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE. E10 in the RATINGS system says DE. The research duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a research-system duplicate of E10, which is domiciled in DE.

**Q44.** Yes, probably. I07 is denominated in XVD, which appears to be Valdoria's currency, and its BBB- matches the local-currency issuer rating (A13). The data does not define XVD explicitly.

**Q45.** No. The BB ceiling caps foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has only a "CO" record (A46), which is not an issuer rating type (LTIDR/STIDR), though the data does not define CO.

**Q47.** None. A47 shows I08's rating as expired (EX) on 2026-09-01.

**Q48.** 7. I01 to I07 are rated, and I08's rating has expired.

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