**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed it before 2025-01-01.

**Q2.** No. Kestrel's only 2026 actions on E01 are affirmations (A03, A04); its downgrade (A02) was in 2025.

**Q3.** No, BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive (POS). E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) has outlook POS.

**Q5.** The holder takes the credit risk of the guarantor, Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and the latest actions give A (A09, A11).

**Q6.** The FC rating is capped by the Valdoria country ceiling of BB (A12). E05's FC rating is BB (A14) against a LC rating of BBB- (A13).

**Q7.** E08, E10 and E16. They were downgraded by A21/A22, A27 and A44. The E06 action (A17) is a watch, not a downgrade.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. E07 is withdrawn (A19), VD has only a country ceiling, and E11 has only a CO.

**Q10.** Depends. The LC rating is BBB- (A13, investment grade) and the FC rating is BB (A14, not investment grade).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30.

**Q12.** A-. A34 assigned A- on 2023-01-15 and it was unchanged on 2024-01-01.

**Q13.** 1. Only A36 is a downgrade for E14; A35 is a watch.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E17 is the same entity as E10 (same LEI), and E10 held A- from A26 until the 2026-04-15 downgrade.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch Negative with the rating left at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the A33 affirmation with no watch.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is rated BBB (A03), which is investment grade.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 expired (A47), and I02 and I04 are below investment grade.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB, and E15's FC rating is A, equal to CV's ceiling of A.

**Q31.** No. No company's FC rating exceeds its ceiling.

**Q32.** E09, via E11 → E10 → E09.

**Q33.** The holder takes the credit risk of the guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 in the data.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, minus the duplicates E03 and E17.

**Q38.** No. They have different LEIs, countries and entity IDs.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE; E17 (RESEARCH) says LU but is a duplicate of E10 with the same LEI.

**Q43.** 0. The only LU record, E17, duplicates E10, whose primary record is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's currency, though the data doesn't state this explicitly.

**Q45.** No. The country ceiling constrains FC ratings, and I07 is a local-currency note rated BBB- (A45), consistent with E05's LC rating (A13).

**Q46.** No. E11 has only a CO record (A46), not an issuer rating.

**Q47.** None. I08 expired on 2026-09-01 (A47).

**Q48.** 7: I01 to I07. I08 expired.

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