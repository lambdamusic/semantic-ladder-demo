**Q1.** A-. A01 assigned A- on 2024-03-12, and the downgrade to BBB (A02) only came on 2025-06-20.

**Q2.** No. Kestrel's only 2026 actions are affirmations (A03, A04); the downgrade was in 2025 (A02).

**Q3.** No. The 2031 note (I02) was cut to BB+ by A07, which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) carries a POS outlook.

**Q5.** The guarantor, E02 (Northwind Holdings). I03 is guaranteed by E02 and is rated A (A11).

**Q6.** The data points to Valdoria's Country Ceiling of BB (A12), which caps the foreign-currency rating at BB (A14) while the local-currency rating is BBB- (A13). The data does not state the cause explicitly.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44).

**Q8.** E08, which went to RD on 2026-07-08 (A22).

**Q9.** 13. These are CV, E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and E16. E07 was withdrawn (A19), E11 has only a CO record (A46), and VD has only a country ceiling (A12).

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+, after the downgrade in A36.

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. The downgrade to BBB+ (A27) came on 2026-04-15, after that date.

**Q16.** No. It was BBB+ then and is BBB+ now; A35 and A33 are a watch and an affirmation.

**Q17.** No. Orrin Bank has only a Rating Watch Negative action (A17), with the rating still A-.

**Q18.** E06 (A17). E14's watch from A35 was resolved by the A33 affirmation, which has no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and there is no default record.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's only record is action type EX (A47), which the data does not define; I treated it as an expected rating, not a held one.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria has only a Country Ceiling record (A12), not an issuer rating.

**Q30.** E05 (FC BB, matching Valdoria's ceiling of BB) and E15 (FC A, matching Corvenia's ceiling of A).

**Q31.** No. No company's foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, E10 (Halden Bank). I05 is guaranteed by E10 and is rated BBB+ (A29).

**Q34.** No. E12 has no parent link to E09 or E10; the shared name is the only connection.

**Q35.** 3 (E09, E10, E11). E17 duplicates E10 by LEI.

**Q36.** 2 (E02, E04). E03 duplicates E02 by LEI.

**Q37.** 17. E03 duplicates E02 and E17 duplicates E10, both by LEI.

**Q38.** No. They have different LEIs, countries and types.

**Q39.** A (A09 and A08).

**Q40.** 6 (E01, E02, E09, E12, E14, E16). E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44). The entity's source system is QA, so it may be a test record.

**Q42.** DE (E10). E17 is a LU research duplicate of the same LEI.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.

**Q44.** Yes, probably. I07 is in XVD, which appears to be Valdoria's currency, but the data does not state this.

**Q45.** No. The ceiling caps foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 has only a CO record (A46), not an issuer rating.

**Q47.** None. The only record for I08 is an EX action (A47) at A, which I read as an expected rating, but the data does not define EX.

**Q48.** 7 (I01–I07). I08 is excluded for the reason given in Q47.

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