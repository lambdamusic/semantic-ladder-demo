**Q1.** A-. E01's foreign-currency long-term rating was A- from A01 (2024-03-12), and nothing changed until 2026.

**Q2.** No. E01's only 2026 action is A03/A04, which are affirmations (AF); the downgrades A02 and A06 were in 2025.

**Q3.** No. I02 (subordinated) was downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), carries a POS outlook.

**Q5.** The holder takes E02's credit risk, which is rated A. I03 is guaranteed by E02, and E02/E03's issuer rating is A (A08, A09).

**Q6.** Not a JSON question. E05's foreign-currency rating is BB (A14) against BBB- in local currency (A13). This fits the VD Country Ceiling of BB (A12), which caps foreign-currency but not local-currency ratings.

**Q7.** E08 and E10. They were downgraded by A21/A22 and A27. E16's downgrade (A44) is QA test data and is ignored. I05's downgrade is an instrument rating, not an issuer's.

**Q8.** E08. A22 set it to RD on 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02 (including E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is withdrawn, VD has only a ceiling, E11 has only a credit opinion, and E16 is QA.

**Q10.** Depends. Its foreign-currency rating is BB (speculative), while its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the next action was A35 on 2025-11-20.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10's rating was A- (A26) until the downgrade A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 Watch, A33 affirmation).

**Q17.** No. E06's only 2026 action, A17, is a Rating Watch, which is not a downgrade. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's Watch (A35) was superseded by A33 with no watch.

**Q19.** E01 and E09. Their latest actions, A03 and A25, carry a NEG outlook.

**Q20.** No. E07's only later action, A19, is a withdrawal (WD), which is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's long-term rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+. E15's local-currency rating comes from A40.

**Q27.** A-, from A42.

**Q28.** BBB+. CV's foreign-currency long-term rating is A38; A37 is the ceiling, not its rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05 is at BB, equal to VD's BB ceiling (A14, A12). E15 is at A, equal to CV's A ceiling (A41, A37).

**Q31.** No. No foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and E10's rating after A27 is BBB+.

**Q34.** No. E12 has no parent link or shared LEI with the E09/E10/E11 chain.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 entity records. Merging E17 into E10 and E03 into E02 removes two, and the QA record E16 is excluded.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, from A09 on E03, the same entity as E02.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds, and the LU record E17 is a duplicate.

**Q43.** 0. The only LU record is E17, which is E10, and RATINGS says E10 is in DE.

**Q44.** Yes. I07 is in XVD, VD's domestic currency.

**Q45.** No. The note's BBB- rating is above the BB ceiling, but the ceiling does not cap local-currency debt.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47), so it is still unrated.

**Q48.** 7, namely I01 to I07.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```