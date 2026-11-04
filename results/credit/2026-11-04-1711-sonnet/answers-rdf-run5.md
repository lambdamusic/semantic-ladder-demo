**Q1.** A-. E01's latest action on or before that date is A01, assigned A- on 2024-03-12. The downgrade to BBB (A02) came later, in June 2025.

**Q2.** No. E01's only 2026 action is A03, which affirmed BBB on 2026-02-10. Its downgrade (A02) was in 2025.

**Q3.** No. I02 (Kestrel 6.25% 2031) was last rated BB+ in A07, and that is below investment grade.

**Q4.** Positive. E03 and E02 share the same LEI, so I treated them as one entity. The latest action is A09 (2025-09-15), which affirmed A with a Positive outlook.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes E02's risk. E02 has an A issuer rating (A08, A09), and I03 itself is rated A (A11).

**Q6.** The data states no reason. E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13). BB equals the Republic of Valdoria's country ceiling (A12), which is consistent with a ceiling effect, but that is an inference.

**Q7.** E08, E10 and E16. Their 2026 downgrades are A21 and A22 for E08, A27 for E10 and A44 for E16. I05's downgrade (A29) is an instrument rating, so I excluded it.

**Q8.** E08. A22 moved it to RD (restricted default) on 2026-07-08, and nothing came after.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country-ceiling rating (A12), which I did not count as an issuer rating. E11's rating is of a different type (A46), and E04 has none.

**Q10.** Depends. E05's local-currency rating is BBB- (A13), which is investment grade. Its foreign-currency rating is BB (A14), which is not.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36) and was unchanged on 2025-06-01.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. The only downgrade is A36. A35 is a Rating Watch action, not a downgrade.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. E10 has been rated A- since A26 (2023-05-01). The downgrade to BBB+ (A27) came in April 2026. E17 shares E10's LEI and has no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35, A33). The Rating Watch did not change the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-. Orrin Bancorp (E13) is a different entity.

**Q18.** E06 (A17, 2026-09-03). E14's watch (A35) was followed by A33, an affirmation with no watch.

**Q19.** E01 (A03) and E09 (A25). E06's watch action carries no outlook.

**Q20.** No. E07's last action is a withdrawal for commercial reasons (A19), not a default.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which was rated RD in A22.

**Q23.** F2 (A04, STIDR, affirmed 2026-02-10).

**Q24.** Yes. E01's long-term issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade. I08's only action is "EX" (A47), which the data does not define, so I did not count it.

**Q26.** A+ (A40, local-currency LTIDR for E15).

**Q27.** A-, from A42 on I06.

**Q28.** BBB+ (A38, foreign-currency LTIDR for CV).

**Q29.** None. VD has only a country-ceiling rating of BB (A12), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB (A14, A12). E15's A equals CV's ceiling of A (A41, A37).

**Q31.** No. No foreign-currency rating exceeds its country ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ after A27. I05 itself is also BBB+ (A29).

**Q34.** Depends. E12 has no parent link in the data, so nothing connects it to the E09–E10–E11 group. The shared "Halden" name alone doesn't settle it.

**Q35.** 3 (E09, E10, E11). E17 duplicates E10 by LEI.

**Q36.** 2 (E02 and E04). E03 duplicates E02 by LEI.

**Q37.** 17. There are 19 entity records. E03 duplicates E02 and E17 duplicates E10, both by shared LEI.

**Q38.** No. E06 (DE) and E13 (US) have different LEIs and countries.

**Q39.** A (A09).

**Q40.** 6 (E01, E02, E09, E12, E14, E16). E07 was withdrawn.

**Q41.** BB+ (A44). E16's source system is QA, which may be a test record, but the data doesn't say.

**Q42.** DE (E10). The duplicate record E17 says LU but shares E10's LEI. I took the RATINGS record.

**Q43.** 0. E17 is the only LU record, and it duplicates E10, which is domiciled in DE. Counting raw records it would be 1.

**Q44.** Yes, probably. I07 is denominated in XVD, which I take to be Valdoria's currency. This is an assumption, since the data doesn't define XVD. Its BBB- rating matches E05's local-currency rating.

**Q45.** No. The ceiling (BB, A12) applies to foreign-currency obligations, and I07 is local-currency.

**Q46.** No. E11's only rating is a different type (CO, A46), not a long-term issuer rating.

**Q47.** A. The only action is "EX" (A47), which the data does not define. It may be an expected rating rather than a final one.

**Q48.** 7 (I01–I07). I08 is excluded because its "EX" status is unclear.

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
"Q34": {"same_group": "depends"},
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
"Q47": {"rating": "A"},
"Q48": {"count": 7}
}
```