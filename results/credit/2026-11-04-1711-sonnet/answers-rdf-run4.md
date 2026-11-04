**Q1.** A-. E01's last action before that date was A01, an assignment of A- on 2024-03-12. The downgrade to BBB (A02) came in June 2025.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB; the downgrade (A02) was in 2025.

**Q3.** No. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 and E03 share the same LEI, so I treat them as one entity. The latest action is A09 (2025-09-15), an affirmation with a Positive outlook.

**Q5.** E02, rated A. I03 is issued by E04 and guaranteed by E02, so the holder relies on the guarantor. I03 is rated A (A11), the same as E02 (A08, A09).

**Q6.** The data states no reason. It is consistent with the country ceiling: E05's foreign-currency rating is BB (A14) and Valdoria's ceiling (A12) is BB, while its local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16. Their downgrades are A21 and A22, A27, and A44. I05 (A29) was also downgraded, but that is an instrument rating.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and no later action cures it.

**Q9.** 13. They are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is excluded because its rating was withdrawn (A19). E11 is excluded because its only rating is of type CO (A46), which the data does not define. VD is excluded because its only rating is a country ceiling.

**Q10.** Depends. E05's foreign-currency rating is BB (A14), which is not investment grade. Its local-currency rating is BBB- (A13), which is.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action (A35) came in November 2025.

**Q12.** A-. This is from A34, assigned 2023-01-15, before the downgrade.

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating (A30) was on 2024-02-01.

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 has the same LEI but no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The Rating Watch (A35) is not a rating change.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at an unchanged A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06. A17 placed it on watch on 2026-09-03. E14's watch (A35) was followed by an affirmation (A33), so it no longer applied.

**Q19.** E01 and E09 (A03, A25). E06's A17 carries no outlook.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not default.

**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is rated BBB (A03).

**Q25.** 5: I01, I03, I05, I06 and I07. I08 is excluded because its action code EX is undefined (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The country ceiling for CV is A (A37).

**Q29.** None. VD only has a country ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 (BB against a BB ceiling) and E15 (A against an A ceiling). Ceilings exist only for VD and CV.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. E10 guarantees I05, and E10 is BBB+ after A27. I05 is also BBB+ (A29).

**Q34.** No. E12 has no parent link to E09, and a similar name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. E06 and E13 have different LEIs and different countries.

**Q39.** A (A09, which is E03, the same entity as E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44). The record comes from the QA source system.

**Q42.** DE (E10). The duplicate record E17 says LU, so the data conflicts.

**Q43.** 1, counting E17. If E17 is the same entity as E10, which says DE, the answer is uncertain.

**Q44.** Yes, probably. I07 is in XVD and its issuer is in VD. Its rating, BBB-, matches E05's local-currency rating. The data does not state that XVD is Valdoria's currency.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 appears to be local-currency, so BBB- is not capped.

**Q46.** Depends. E11 only has a CO-type rating (A46), and the data does not say whether that counts as an issuer rating.

**Q47.** None. I08 has only an EX action (A47), and the data does not define EX, so I do not treat it as a held rating.

**Q48.** 7, which is I01 to I07. I08 is excluded as in Q47.

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
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "depends"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```