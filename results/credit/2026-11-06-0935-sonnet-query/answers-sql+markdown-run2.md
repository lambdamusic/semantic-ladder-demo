**Q1.** A-. E01's rating was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the outlook moved to NEG, but the rating did not change.

**Q3.** No, it is BB+. I02 is subordinated, and its latest action A07 set it at BB+.

**Q4.** POS. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15) with outlook POS.

**Q5.** The holder takes E02's (Northwind Holdings') credit risk, rated A. I03 is guaranteed by E02, and E02/E03's latest rating is A (A09).

**Q6.** This is not in the structured answers. The likely reason is the Valdoria Country Ceiling of BB (A12), which caps E05's FC rating (A14, BB). Its LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22 and E10 by A27. E16's downgrade is QA test data and is ignored.

**Q8.** E08. A22 set it to RD on 2026-07-08, and RD counts as a default.

**Q9.** 12. These are CV, E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14 and E15. E07 is withdrawn, E11 has only a credit opinion, VD has only a Country Ceiling, and E16 is QA.

**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 (2024-09-30) set it; the later actions A35 and A33 both stayed at BBB+.

**Q12.** A-. A34 set it on 2023-01-15 and A36 did not come until 2024-09-30.

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first action, A30, is dated 2024-02-01.

**Q15.** A-. A26 set E10's rating (the same entity as E17), and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now.

**Q17.** No. A17 is only a Rating Watch (RW), which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's watch (A35) was superseded by the affirmation A33, which carries no watch.

**Q19.** E01 and E09. They have NEG outlooks from A03 and A25.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. I01 is BBB, I03 is A, I05 is BBB+, I06 is A- and I07 is BBB-. I02 (BB+) and I04 (BB) are speculative, and I08 has only an expected rating (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB. E15's FC rating is A, equal to CV's ceiling of A.

**Q31.** No. No FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's (Halden Bank's) credit risk, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3. The group is E09, E10 (the same entity as E17) and E11.

**Q36.** 2. The group is E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. E16 is QA, E03 duplicates E02, and E17 duplicates E10.

**Q38.** No. They have different LEIs.

**Q39.** A (A09).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is QA, so it is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile.

**Q43.** 1. That is E10, which is the same entity as E17.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), so it is unrated.

**Q48.** 7. All instruments except I08 held a rating.

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