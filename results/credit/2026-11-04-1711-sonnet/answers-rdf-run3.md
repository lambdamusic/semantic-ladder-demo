**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12) and stayed so until the downgrade in A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is the affirmation of BBB in A03/A04 (2026-02-10); the downgrades in A02, A06 and A07 were in 2025.

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07 (2025-06-20), below investment grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI, a RESEARCH duplicate). Its latest action is A09 (2025-09-15), an affirmation of A with a Positive outlook.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 but guaranteed by E02, and I03 itself is A (A11) and E02/E03 is A (A09).

**Q6.** The data does not state a reason. It is consistent with the country ceiling: VD's CC is BB (A12) and E05's FC LTIDR is BB (A14), while its LC LTIDR is BBB- (A13).

**Q7.** E08, E10 and E16. Their issuer downgrades are A21/A22, A27 and A44. I05's downgrade (A29) is an instrument rating. E16 comes from a "QA" source system, which the data does not explain.

**Q8.** E08. A22 (2026-07-08) moved it to RD, and nothing later changes that.

**Q9.** 13. These are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13) but its FC rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 only placed it on watch in November 2025.

**Q12.** A-. A34 (2023-01-15) applies until A36.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30 (2024-02-01).

**Q15.** A-. A26 assigned A- to E10, and the downgrade A27 only came on 2026-04-15. E17 is a duplicate of E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). A35 added a watch that was later resolved.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative on A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06. A17 (2026-09-03) is unresolved. E14's watch (A35) was superseded by A33.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes, BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08's EX action is not a current rating.

**Q26.** A+, from A40.

**Q27.** A- (A42).

**Q28.** BBB+, from A38. A37 is the country ceiling, not the issuer rating.

**Q29.** None. VD only has a country-ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 (FC BB = VD ceiling BB) and E15 (FC A = CV ceiling A).

**Q31.** No. No company's FC rating exceeds its country's ceiling; E05's LC rating of BBB- is local currency.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10, rated BBB+. I05 is issued by E11 but guaranteed by E10, which was downgraded to BBB+ in A27. I05 itself is also BBB+ (A29).

**Q34.** No. E12 has no parent link to E09, E10 or E11; only the name is shared.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 (=E03) and E04.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and countries (DE vs US), and no linking relation.

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn, and E03 is E02.

**Q41.** BB+ (A44, though from a "QA" source).

**Q42.** DE. E10 says DE. The duplicate E17 says LU, a conflict I resolved in favour of the RATINGS record.

**Q43.** 0. The only LU record is E17, which is a duplicate of E10 (DE). Counting the record as written would give 1.

**Q44.** Yes, inferred. I07's currency is XVD, which appears to be Valdoria's own currency, but the data does not define it.

**Q45.** No. The ceiling limits foreign-currency ratings, and I07 appears to be local-currency, so BBB- vs the BB ceiling is not a breach.

**Q46.** No. E11's only rating is type CO (A46), not an issuer default rating, and the data does not define CO.

**Q47.** None. I08 has only an "EX" action (A47), which is not defined; if it means an expected rating, it is not a final rating.

**Q48.** 7: I01 to I07. I08 has only the EX record.

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
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```