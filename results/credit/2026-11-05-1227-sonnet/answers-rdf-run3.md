**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01) and was not downgraded to BBB until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB with a Negative outlook (A03, A04).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E03 and E02 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15, outlook POS), which supersedes A08 (STA).

**Q5.** The guarantor, E02. The I03 notes are issued by E04 but guaranteed by E02, and I03 is rated A (A10, A11), in line with E02's A.

**Q6.** The data doesn't say. E05 has FC BB (A14) and LC BBB- (A13), and neither record carries a comment. VD's Country Ceiling of BB (A12) is consistent with this, but the data does not state it as the reason.

**Q7.** E08, E10 and E16. Their 2026 downgrades are A21 and A22, A27, and A44. I05 (A29) is an instrument downgrade, not an issuer one.

**Q8.** E08. It was rated RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV, each with an LTIDR. E07 was withdrawn (A19). VD has only a Country Ceiling (A12), and E11 only a "CO" rating (A46), which the data does not define as an issuer rating.

**Q10.** Depends. E05 is BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and nothing changed the rating before 2025-11-20.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36. The other E14 actions are an assignment, a watch and an affirmation.

**Q14.** None. E12's first rating was on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in 2023 (A26) and not downgraded until 2026-04-15 (A27). E17 has the same LEI and no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). Only a watch was added and then resolved.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17). E13, Orrin Bancorp, is a different entity.

**Q18.** E06 (A17). E14's watch (A35) was superseded by A33, which has no watch.

**Q19.** E01 (A03) and E09 (A25). E06's last stated outlook was STA, and its A17 record carries no outlook.

**Q20.** No. E07 was withdrawn for commercial reasons (A19), not defaulted.

**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (A22, RD).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5, but only if I08 is excluded. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) count. I02 and I04 are BB+ and BB. I08's action code "EX" is not defined in the data, so I left it out.

**Q26.** A+ (A40).

**Q27.** A- (A42, subordinated).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 and E15. The ceilings are VD = BB and CV = A, and E05 FC is BB (A14) and E15 FC is A (A41). CV's own FC rating is BBB+, so it is not at the ceiling.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The guarantor, E10. I05 is issued by E11 but guaranteed by E10, and I05 is rated BBB+ (A29), matching E10's current rating of BBB+ (A27).

**Q34.** Yes. Halden Foods (E12) has no parent link in the data and is rated separately, so there is no evidence it belongs to the Halden group, and Halden Bank (E10) is under E09. The answer is "no" on the data given.

**Q35.** 3: E09, E10 and E11. E17 shares E10's LEI, so it is the same entity.

**Q36.** 2: E02 (=E03) and E04.

**Q37.** 17. There are 19 entity records, but E17 duplicates E10 and E03 duplicates E02 (same LEIs).

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44). E16's source system is "QA", which may mean the record is not production data.

**Q42.** DE (E10). The duplicate record E17 says LU.

**Q43.** 1, E17. It is probably the same entity as E10, so this is a data conflict.

**Q44.** Yes, though this is inferred. XVD appears to be Valdoria's currency, and I07's BBB- equals E05's LC rating (A13), but the data does not define XVD.

**Q45.** No. The ceiling (BB) limits foreign-currency ratings, and I07 is a local-currency obligation.

**Q46.** No. E11 has only a "CO" rating (A46) and no LTIDR.

**Q47.** A (A47), but the "EX" action code is undefined, so this may be an expected or expired rating.

**Q48.** 7: I01 to I07. I08 is excluded for the same reason as in Q25.

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
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "A"},
"Q48": {"count": 7}
}
```