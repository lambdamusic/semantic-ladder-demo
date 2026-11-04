**Q1.** A-. A05 aside, the issuer rating A01 (A-, 2024-03-12) was in force on that date; the downgrade A02 came in June 2025.

**Q2.** No. The only 2026 Kestrel issuer actions are affirmations (A03, A04), at BBB with a Negative outlook.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), downgraded to BB+ by A07.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed A with a Positive outlook, superseding A08.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A10, A11), and E02/E03 is rated A (A08, A09).

**Q6.** The data points to the sovereign country ceiling. VD's country ceiling is BB (A12), and E05's foreign-currency rating is BB (A14) while its local-currency rating is BBB- (A13). The data does not state the reason explicitly.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 downgraded an instrument (I05), not an issuer rating.

**Q8.** E08. A22 (2026-07-08) moved it to RD, and nothing later changes that.

**Q9.** 12. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), and VD only has a country ceiling (A12), not an issuer rating.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded it to BBB+, and A35 (a watch) came only in November 2025.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1 time (A36).

**Q14.** No rating. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 applied until the downgrade A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A35 watch, then A33 affirmation).

**Q17.** No. A17 is a Rating Watch Negative placement at A-, not a downgrade.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33, which carries no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and no default is recorded.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 4. I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) are investment grade, while I02 (BB+) and I04 (BB) are not.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** It has none. VD only has a country ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating BB equals VD's ceiling BB (A14, A12), and E15's A equals CV's ceiling A (A41, A37).

**Q31.** No. E05 is at VD's ceiling and E15 is at CV's, and none is above.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+ (I05 guaranteed by E10; A29).

**Q34.** No. E12 has no parent link to the Halden group in the data, and only the name is similar.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02 and E04). E03 is a duplicate record of E02, so it adds nothing.

**Q37.** 16. The file has 17 rows, and E03 duplicates E02 (same LEI).

**Q38.** No. They have different LEIs, countries (DE versus US) and entity IDs (E06, E13).

**Q39.** A (A08, A09).

**Q40.** 5 (E01, E02, E09, E12, E14). E07 is excluded because its rating was withdrawn.

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
"Q14": {"rating": "NR"},
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
"Q25": {"count": 4},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "NR"},
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
"Q40": {"count": 5}
}
```