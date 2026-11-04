**Q1.** A-. E01's latest rating before 1 Jan 2025 is A01 (A- LTIDR, FC, 2024-03-12). The downgrade to BBB (A02) came later, in June 2025.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB. Its downgrades were in 2025 (A02, I01's A06, I02's A07).

**Q3.** No. The 2031 note is I02, whose latest rating is BB+ (A07, 2025-06-20), below investment grade.

**Q4.** Positive. E02 and E03 share one LEI and are the same entity. The latest action is A09 (E03, affirmed A, Positive outlook, 2025-09-15), which supersedes A08.

**Q5.** The guarantor E02, rated A. I03 is issued by E04 and guaranteed by E02, and A09 gives E02 an A rating.

**Q6.** The data doesn't state a reason. It is consistent with the sovereign ceiling: VD has a country-ceiling record at BB (A12), and E05's FC rating is BB (A14) against BBB- in LC (A13).

**Q7.** E08, E10 and E16. Their issuer-level downgrades in 2026 are A21/A22, A27 and A44. I05's downgrade (A29) is an instrument rating.

**Q8.** E08. A22 puts it at RD on 2026-07-08, and nothing later changes that.

**Q9.** 13. These are E01, E02 (with E03 as a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country-ceiling record and E11 only a counterparty rating, so neither counts.

**Q10.** Depends. E05 is BBB- in LC (investment grade, A13) but BB in FC (not, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 (a watch action, 2025-11-20) comes later.

**Q12.** A-. A34 (2023-01-15) was still current on 2024-01-01.

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. This is E10 (A26), and its downgrade A27 came in April 2026. E17 is a duplicate record with the same LEI and no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). The watch in A35 doesn't change the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17, 2026-09-03). E14's earlier watch (A35) was followed by A33, an affirmation on 2026-05-01 with a Stable outlook.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 has no default rating, and its last action is a withdrawal (A19).

**Q21.** E07, withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's "EX" action is undefined in the data, so I did not count it.

**Q26.** A+ (A40).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country-ceiling record at BB (A12), not an issuer rating.

**Q30.** E05 and E15. E05 is FC BB against a VD ceiling of BB, and E15 is FC A against a CV ceiling of A (A37).

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor E10, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent or other link to E09, E10 or E11. Only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 17. There are 19 entity records, but E17 duplicates E10 and E03 duplicates E02, going by their shared LEIs.

**Q38.** No. They have different LEIs and countries (E06 is DE, E13 is US).

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44). The entity's source system is "QA", which may matter for reliability.

**Q42.** DE (E10). The duplicate record E17 says LU, so the data conflicts on this.

**Q43.** 0. The only LU record, E17, duplicates E10, which is recorded as DE. If E17 is counted as its own entity, the answer is 1.

**Q44.** Depends. I07 is in "XVD", and the data doesn't say that is Valdoria's local currency.

**Q45.** Depends. The ceiling is BB (A12) and I07 is BBB-, but a ceiling applies to FC, not LC. The answer turns on whether XVD is local currency.

**Q46.** No. E11 has only a counterparty rating (A46, type CO), not an issuer rating.

**Q47.** None. I08's only record is an "EX" action (A47), which the data doesn't define. I treated it as a non-final rating, so it is not counted in Q25 or Q48.

**Q48.** 7: I01 to I07, excluding I08 for the same reason.

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
"Q44": {"local_currency": "depends"},
"Q45": {"above_ceiling": "depends"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```