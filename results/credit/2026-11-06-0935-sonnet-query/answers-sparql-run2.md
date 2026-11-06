**Q1.** A-. Kestrel Energy's (E01) rating on 1 January 2025 was A-, assigned in A01 on 2024-03-12 and not changed until A02 on 2025-06-20.

**Q2.** No. A03 (2026-02-10) affirmed the BBB rating and moved the outlook to Negative. The only downgrade, A02, was in 2025.

**Q3.** No, rating BB+. The 2031 note (I02) was cut from BBB to BB+ in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive. E03 ("NORTHWIND HLDGS") has the same LEI as E02, so I treat them as one entity. The latest action, A09 (2025-09-15), gives A with a Positive outlook.

**Q5.** The holder takes the risk of E02 (Northwind Holdings), the guarantor of I03, and E02 is rated A. The issuer is E04, a finance subsidiary, and I03 itself is also rated A (A11).

**Q6.** The data has no explanation field for this. The records show E05's local-currency rating at BBB- and its foreign-currency rating at BB (A13, A14). Valdoria's country ceiling (A12) is BB, which matches the foreign-currency rating, so a ceiling effect is the likely cause. I can't confirm that from the data.

**Q7.** E08, E10 and E16. The downgrades are A21 and A22 for E08, A27 for E10 and A44 for E16. E11's downgrade (A29) was on an instrument, not an issuer rating. E06 was only placed on watch.

**Q8.** E08. A22 (2026-07-08) rated it RD, a restricted default, and nothing came after it.

**Q9.** 13. The issuers are E01, E02 (counting E03 as the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is excluded because its rating was withdrawn (A19), and E11 has only a "CO" rating (A46), which I did not treat as an issuer rating.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not investment grade).

**Q11.** BBB+. A36 (2024-09-30) lowered Marlow Utilities (E14) to BBB+, and it was still BBB+ on 1 June 2025.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01, after 1 January 2024.

**Q15.** A-. This is E10's rating from A26 (2023-05-01); the downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. It was BBB+ on 1 January 2025 and is BBB+ now (A33, 2026-05-01). The watch in between (A35) was resolved.

**Q17.** No. A17 (2026-09-03) only placed Orrin Bank AG (E06) on Rating Watch Negative and left the A- rating unchanged.

**Q18.** E06, from A17.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 shows the rating withdrawn "for commercial reasons", which is not a default.

**Q21.** E07, because its rating was withdrawn in A19.

**Q22.** E08, which was rated RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. Its issuer rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I08's only record is an "EX" action (A47), whose meaning isn't defined in the data, so I did not count it.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38 (foreign-currency, 2024-01-01).

**Q29.** None. Valdoria (VD) only has a country-ceiling record (A12, BB), not an issuer rating.

**Q30.** E15 and E05. E15's foreign-currency rating of A equals Corvenia's ceiling of A (A37). E05's BB equals Valdoria's ceiling of BB (A12).

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09, via E11 → E10 → E09.

**Q33.** The holder takes the risk of E10 (Halden Bank), the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. The data has no parent link for E12, so it is not linked to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 looks like a duplicate of E10, but it has no parent link.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 entity records, and E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. E06 and E13 have different LEIs and countries (DE and US).

**Q39.** A, from A09 (E03, the same entity as E02).

**Q40.** 6: E01, E02 (with E03), E09, E12, E14 and E16.

**Q41.** BB+, from A44.

**Q42.** DE. E10 is recorded in Germany, though the duplicate record E17 says LU.

**Q43.** 1. Only E17 is recorded as LU, and it conflicts with E10's DE record.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's local currency.

**Q45.** No. The ceiling limits foreign-currency ratings, and I07 is local-currency, so its BBB- is not capped by the BB ceiling.

**Q46.** No. E11 only has a "CO" rating (A46, BBB), which is not an issuer default rating.

**Q47.** None. I08's only record is an "EX" action (A47), which is undefined in the data. If it is a final rating, it would be A.

**Q48.** 7. I01 to I07 each have a rating, and I08 is excluded for the reason in Q47.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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
"Q30": {"entities": ["E15", "E05"]},
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
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```