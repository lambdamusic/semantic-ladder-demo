**Q1.** A-. E01's LTIDR was assigned at A- (A01) and not changed until the 2025-06-20 downgrade (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03).

**Q3.** No, it is BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), and BB+ is below investment grade.

**Q4.** POS. E03 is a RESEARCH duplicate of E02 (same LEI), and its latest action (A09, 2025-09-15) affirms A with a Positive outlook.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02 (instruments.csv), and E02's rating is A (A09 on its duplicate E03).

**Q6.** The data gives no stated reason, but the pattern is consistent with a ceiling. The Valdoria country ceiling is BB (A12), which equals E05's FC rating of BB (A14). The LC rating is BBB- (A13).

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21 and A22, A27, A44). E06's action was a Watch (A17), not a downgrade.

**Q8.** E08. It was rated RD on 2026-07-08 (A22), with no later action.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (not, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-. This is the original assignment (A34).

**Q13.** 1, by A36.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E17 is a duplicate of E10, whose A- (A26) stood until the 2026-04-15 downgrade (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch Negative with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the 2026-05-01 affirmation with no watch (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of a default.

**Q21.** E07, which was withdrawn (A19).

**Q22.** E08 (A22).

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 had expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the Valdoria ceiling of BB (A14, A12). E15's FC rating of A equals the Corvenia ceiling of A (A41, A37).

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent and no link to E09 in the data.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and no parent link.

**Q39.** A (A09 affirmation on E03, the duplicate of E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. E10 in the RATINGS system says DE. The RESEARCH duplicate E17 says LU, which conflicts, so I treated it as a data-quality error.

**Q43.** 0. The only LU record is E17, which duplicates E10 and conflicts with its DE domicile.

**Q44.** Yes, inferred. I07 is denominated in XVD, which appears to be Valdoria's currency (VD), though the data does not define the code.

**Q45.** No. The ceiling (BB, A12) constrains foreign-currency ratings, and I07 is local-currency, rated BBB- (A45).

**Q46.** No. E11 has only a "CO" record (A46), not an LTIDR, and the data doesn't define CO.

**Q47.** None. I08 expired on 2026-09-01 (A47).

**Q48.** 7: I01 to I07. I08 had expired.

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