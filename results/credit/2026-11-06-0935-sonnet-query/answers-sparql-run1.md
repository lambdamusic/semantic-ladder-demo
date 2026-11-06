**Q1.** A-. Kestrel's FC LT IDR was A- from A01 (2024-03-12). It was only cut to BBB on 2025-06-20 (A02).

**Q2.** No. Kestrel's only 2026 actions are affirmations on 2026-02-10 (A03, A04), with the outlook moved to Negative.

**Q3.** No. The 2031 note (I02) is rated BB+ since the downgrade on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 (NORTHWIND HLDGS) shares E02's LEI, so I treat them as the same entity. E03's latest action, A09 (2025-09-15), has a Positive outlook, and E02's own record is the older A08.

**Q5.** The guarantor, E02, because I03 was issued by E04 and guaranteed by E02. I03 is rated A (A11).

**Q6.** The data doesn't state a reason. The pattern is consistent with a country-ceiling cap: E05's FC rating is BB (A14), equal to Valdoria's Country Ceiling of BB (A12), while its LC rating is BBB- (A13).

**Q7.** E08, E10 and E16 had issuer-rating downgrades in 2026 (A21, A22, A27, A44). I05, the instrument issued by E11, was also downgraded (A29), but E11 itself has no issuer rating.

**Q8.** E08. It was rated RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. The issuers are E01, E02 (with E03 as the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. E05 is BB on an FC basis (A14) and BBB- on an LC basis (A13).

**Q11.** BBB+. Marlow was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-, from A34.

**Q13.** 1, from A36. A35 is only a watch, and A33 affirmed the rating.

**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.

**Q15.** A-, from A26 for E10. E17 is the same entity and has no actions of its own.

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is still BBB+ after the watch period (A35, A33).

**Q17.** No. Orrin Bank's only 2026 action is a Rating Watch Negative (A17) at A-, which is not a downgrade.

**Q18.** E06 (A17, unresolved). E14's watch was resolved by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and no default is recorded.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, rated RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5: I01, I03, I05, I06 and I07. I08's only record, A47, has the action code "EX", which the data doesn't define, so I excluded it as not a settled rating. If it counts, the answer is 6.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria has only a Country Ceiling (BB, A12), which is not an issuer rating.

**Q30.** E05 (BB against the ceiling of BB) and E15 (A against the ceiling of A).

**Q31.** No. No company's FC issuer rating is above its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, the guarantor of I05 (which E11 issued). I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent link to E09, so the data does not put it in the group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 records, and E03 and E17 are duplicates by LEI of E02 and E10.

**Q38.** No. They have different LEIs and different countries (E06 is DE, E13 is US).

**Q39.** A. The rating is unchanged since A08, affirmed in A09.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 says DE. The LU record E17 is a research duplicate with the same LEI.

**Q43.** 0. The only LU record, E17, is a duplicate of the DE entity E10, so I don't count it as a distinct LU entity.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's local currency (inferred from the code, not stated in the data).

**Q45.** Yes. I07 is rated BBB- (A45), above Valdoria's ceiling of BB (A12).

**Q46.** No. E11 has only a type-CO rating (A46), not an issuer (LTIDR) rating.

**Q47.** None. I08's only record, A47, is an "EX" action that the data doesn't define, so I can't treat it as a settled rating. It shows A.

**Q48.** 7: I01 to I07. I08 is excluded for the reason in Q25.

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
"Q45": {"above_ceiling": "yes"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```