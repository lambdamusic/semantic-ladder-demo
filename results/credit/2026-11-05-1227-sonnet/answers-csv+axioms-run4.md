**Q1.** A-. Kestrel's LTIDR was A- from A01 (2024-03-12) until A02 (2025-06-20), so it was A- on 1 Jan 2025.

**Q2.** No. The only 2026 Kestrel actions are affirmations (A03, A04). The downgrade, A02, was in 2025.

**Q3.** No. I02 was downgraded to BB+ in A07, which is below investment grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI). A09 (2025-09-15, POS) supersedes A08.

**Q5.** E02, rated A. I03 is guaranteed by E02 (the guarantor's risk applies), and the current rating is A09 (A).

**Q6.** The data doesn't state a reason explicitly. It is consistent with the VD Country Ceiling of BB (A12) capping the FC rating (A14, BB), while the LC rating (A13) is BBB-.

**Q7.** E08 (A21, A22) and E10 (A27). E16's downgrade (A44) is a QA test record and doesn't count. The instrument downgrade A29 is not an issuer action.

**Q8.** E08. A22 is RD and still in force.

**Q9.** 12. The issuers are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15.

**Q10.** Depends. The LC rating is BBB- (investment grade), but the FC rating is BB (not).

**Q11.** BBB+. A36 (2024-09-30) was in force on that date.

**Q12.** A-. A34 (2023-01-15) was in force on that date.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement.

**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 was in force until A27 (2026-04-15). E17 is the same entity as E10.

**Q16.** No. It was BBB+ on 1 Jan 2025 (A36) and is BBB+ now (A33). The intervening actions (A35, A33) did not change the rating.

**Q17.** No. A17 is a Rating Watch placement, not a downgrade.

**Q18.** E06. A17 is the in-force RWN. E14's A35 was superseded by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 was rated BB and then withdrawn (A19); it was never in default.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08. A22 is RD.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. The in-force investment-grade instrument ratings are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 (FC BB, VD ceiling BB) and E15 (FC A, CV ceiling A).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and A27 is its current rating.

**Q34.** Yes. E12 has no parent link to E09 or E10, so it is not part of that group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 16. There are 19 records. Remove the duplicates E03 and E17, and exclude the QA test record E16.

**Q38.** No. They have different LEIs and no link between them.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 is withdrawn, and E16 is a test record.

**Q41.** None. E16 is a QA test record, so its actions don't count as ratings in force.

**Q42.** LU. The RESEARCH record E17 (the same entity as E10) overrides the DE country on the RATINGS record.

**Q43.** 1. E10 and E17 are one entity.

**Q44.** Yes. I07 is in XVD and the issuer is domiciled in VD, whose domestic currency is XVD.

**Q45.** No. The ceiling constrains foreign-currency issuer ratings, and I07 is a local-currency note. Separately, its rating (BBB-) is above the BB ceiling, but that comparison isn't a rule violation here.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is an expected rating (A), which is not a rating in force.

**Q48.** 7. I01 to I07 have ratings in force, and I08 has only an expected rating.

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