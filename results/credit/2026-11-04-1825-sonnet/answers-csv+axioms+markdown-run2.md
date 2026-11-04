**Q1.** A-. A01 (2024-03-12) set A-, and the next change, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04; the downgrade A02 was in 2025.

**Q3.** No, BB+. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** E02, rated A. I03's guarantor is E02, so the holder takes E02's credit risk, and E02/E03's latest LTIDR (A09) is A.

**Q6.** Valdoria's Country Ceiling is BB (A12), and the foreign-currency rating is capped at it (A14, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 had downgrades A21 and A22, and E10 had A27. A29 is an instrument rating, and A44 is on QA record E16, which is ignored.

**Q8.** E08. Its latest action, A22, put it at RD, which is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn, E04 and E11 have no issuer rating (E11 has only a credit opinion), VD has only a ceiling, and E16 is QA.

**Q10.** Depends. The foreign-currency rating is BB (speculative grade), but the local-currency rating is BBB- (investment grade) (A13, A14).

**Q11.** BBB+. The downgrade A36 (2024-09-30) was in force on that date.

**Q12.** A-. A34 was in force on that date.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch placement.

**Q14.** None. The first action on E12 is A30 on 2024-02-01.

**Q15.** A-. A26 was in force, and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is the Watch placement A17, and E13 is a different entity.

**Q18.** E06. A17 placed it on RWN. E14's Watch (A35) was superseded by the affirmation A33.

**Q19.** E01 and E09 (A03 and A25 are both NEG).

**Q20.** No. E07's rating was withdrawn (A19), which is not a default, and its last rating was BB.

**Q21.** E07, which was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an Expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling BB, and E15's FC rating is A, equal to the CV ceiling A.

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05's guarantor is E10, and its LTIDR was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent and no shared LEI with the Halden Bank group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10.

**Q38.** No. They have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, over the RESEARCH record E17, which says LU.

**Q43.** 0. E17 resolves to DE.

**Q44.** Yes. I07 pays in XVD, which is the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency, so the ceiling does not apply, and it is rated BBB- anyway (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, so I08 stays unrated.

**Q48.** 7. These are I01 through I07.

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
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```