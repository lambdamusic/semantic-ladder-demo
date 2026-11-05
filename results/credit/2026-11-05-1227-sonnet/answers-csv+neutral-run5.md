**Q1.** A-. A01 (2024-03-12) set E01's FC LTIDR at A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation (BBB, outlook to NEG); the downgrade A02 was in 2025.

**Q3.** No, it is BB+. I02 (subordinated) was downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive (POS). E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action: A, POS.

**Q5.** The holder takes E02's credit risk, which is rated A. I03 is guaranteed by E02, and E02's latest LTIDR is A (A09, on the duplicate record E03).

**Q6.** Foreign-currency ratings are capped by the Country Ceiling, and Valdoria's ceiling is BB (A12). E05's FC rating is therefore BB (A14), while its LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is QA test data, and A29 is an instrument rating.

**Q8.** E08. A22 put it at RD on 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, E04 and E11 have no issuer rating (E11 has only a CO), VD has only a Country Ceiling, and E16 is QA.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the Watch in A35 only came later (2025-11-20).

**Q12.** A-. This is the rating from A34 (2023-01-15), before the downgrade in A36.

**Q13.** 1. Only A36 is a downgrade; A33 is an affirmation and A35 a Watch.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E17 has the same LEI as E10, so they are one entity. A26 gave A-, and the downgrade A27 only came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+; the Watch in A35 and the affirmation in A33 did not change it.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) is its latest action and carries RWN. E14's Watch (A35) was superseded by A33, which has no Watch.

**Q19.** E01 and E09. Their latest outlooks are NEG (A03 and A25).

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and a withdrawal is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The instruments rated investment grade are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only an Expected rating (EX) and is unrated.

**Q26.** A+ (A40).

**Q27.** A- (A42). This is below Corvenia's ceiling of A (A37).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling of BB, and E15's FC rating is A, equal to Corvenia's ceiling of A.

**Q31.** No. E05 (BB) and E15 (A) are both at their ceilings, not above.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, which is rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent, and E09 is not E12's parent.

**Q35.** 3: E09, E10 (with E17) and E11.

**Q36.** 2: E02 (with E03) and E04.

**Q37.** 16. The 19 records include two duplicates (E03 and E17) and one QA record (E16).

**Q38.** No. The two records have different LEIs, and a similar name does not make the same entity.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in LU, not GB.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, and it overrides E10's DE.

**Q43.** 1. Only E10, via its RESEARCH record E17.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, which is E05's country.

**Q45.** No. Local-currency debt is not capped by the Country Ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7: I01 to I07.

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
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```