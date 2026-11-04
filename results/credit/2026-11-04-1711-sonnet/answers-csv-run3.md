**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01) and unchanged until 2025-06-20 (A02).

**Q2.** No. The only 2026 action on Kestrel's issuer rating is an affirmation at BBB (A03).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) carries a POS outlook.

**Q5.** E02 (Northwind Holdings), rated A. The notes (I03) are guaranteed by E02, whose rating is A (A08, A09), and I03 itself is also A (A11).

**Q6.** The data doesn't state a reason, but it points to the country ceiling. Valdoria's Country Ceiling is BB (A12), and E05's foreign-currency rating is BB (A14) against BBB- local currency (A13).

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44. E06's action (A17) is only a watch.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. E07 is withdrawn (A19), VD has only a country ceiling, and E11's CO record is not an issuer rating.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. The downgrade from A- (A34) to BBB+ came on 2024-09-30 (A36), and the next action is 2025-11-20.

**Q12.** A- (A34, assigned 2023-01-15).

**Q13.** 1, the downgrade in A36.

**Q14.** None. Halden Foods' first rating is dated 2024-02-01 (A30).

**Q15.** A-. E10 and E17 share an LEI and are the same entity. A26 gave A-, and the downgrade (A27) came only on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+. A35 is a watch and A33 an affirmation.

**Q17.** No. Orrin Bank's only 2026 action is a Rating Watch Negative with the rating held at A- (A17).

**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by the 2026-05-01 affirmation with no watch (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. The rating was withdrawn for commercial reasons (A19), and there is no default rating.

**Q21.** E07, withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 and I04 are below, and I08 expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12), not an issuer rating.

**Q30.** E05 and E15. Their foreign-currency ratings are BB, equal to Valdoria's ceiling (A14, A12), and A, equal to Corvenia's ceiling (A41, A37).

**Q31.** No. No company's foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10 (the guarantor, Halden Bank), rated BBB+ (A27). The notes I05 are also BBB+ (A29).

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10, E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and different countries (E06 is DE, E13 is US).

**Q39.** A. The latest action is the affirmation at A (A09, recorded under E03, the same entity as E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU, so the data conflicts. I took the primary system's value.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record says DE. This is ambiguous, and counting E17 on its own would give 1.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's currency, though the data has no currency table to confirm it.

**Q45.** No. I07 is BBB- (A45) against a ceiling of BB, but the ceiling applies to foreign-currency obligations and this note is local-currency.

**Q46.** No. E11 has no LTIDR, only a "CO" record (A46) whose type the data does not define.

**Q47.** None. The note's last action is expiry on 2026-09-01 (A47).

**Q48.** 7. I01–I07 are rated, and I08 expired (A47).

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