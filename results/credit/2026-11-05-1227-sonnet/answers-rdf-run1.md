**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01), and the next action was 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB (A03, A04). The downgrade was in 2025 (A02).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E03 is the same entity as E02: both carry LEI 213800PHEIYNJMHTDV74. The latest action is A09 (2025-09-15), an affirmation at A with a Positive outlook.

**Q5.** The guarantor E02, rated A. I03 is issued by E04 but guaranteed by E02 (A10, A11).

**Q6.** The data gives no stated reason. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The FC rating equals Valdoria's country ceiling of BB (A12), which is consistent with a cap, but that is an inference.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44). I05's downgrade (A29) is an instrument rating whose issuer is E11, so I left E11 out.

**Q8.** E08, rated RD since 2026-07-08 (A22).

**Q9.** 13. These are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country ceiling (A12). E11 has only a CO-type rating (A46).

**Q10.** Depends. E05's LC rating is BBB- (investment grade) and its FC rating is BB (not) (A13, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action is 2025-11-20 (A35).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, the downgrade A36. The others are an assignment, a watch and an affirmation.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was rated A- (A26) until the downgrade on 2026-04-15 (A27). E17 shares E10's LEI and has no ratings.

**Q16.** No. The rating stayed BBB+ (A35, A33). Only a watch was added and then resolved by an affirmation.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17). Orrin Bancorp (E13) is a different entity.

**Q18.** E06 (A17, 2026-09-03). E14's watch (A35) was followed by an affirmation with a Stable outlook (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn on 2026-05-12 for commercial reasons (A19), and it has no default rating.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's A rating expired on 2026-09-01 (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country-ceiling rating (A12), not an issuer rating.

**Q30.** E05 (FC BB = VD ceiling BB) and E15 (FC A = CV ceiling A) (A12, A14, A37, A41).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The guarantor E10, rated BBB+ (A27). I05 is issued by E11 but guaranteed by E10 (A29).

**Q34.** No. E12 has no parent link, and E10 sits under E09. Only the name is shared.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and countries (DE and US).

**Q39.** A (A09).

**Q40.** 6: E01, E02 (=E03), E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44). The record comes from the "QA" source system.

**Q42.** DE (E10). The duplicate record E17 says LU, but E10 comes from the RATINGS system.

**Q43.** 0. The only LU record is E17, which shares E10's LEI, and E10 is recorded as DE. Counting E17 alone would give 1.

**Q44.** Yes, probably. I07 is in XVD and its issuer E05 is in VD, but the data doesn't define XVD explicitly.

**Q45.** No. A local-currency note is not bound by the FC ceiling of BB (A12), and I07 is rated BBB- (A45).

**Q46.** No. E11 has only a CO-type rating (A46), not an issuer default rating.

**Q47.** None. I08's A rating expired on 2026-09-01 (A47).

**Q48.** 7: I01 to I07. I08 had expired.

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