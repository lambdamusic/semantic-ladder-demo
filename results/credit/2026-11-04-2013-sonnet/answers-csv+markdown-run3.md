**Q1.** A-. A01 (2024-03-12) set E01's FC LTIDR at A-, and the next action, A02, is dated 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation (BBB, outlook NEG), which is not a downgrade.

**Q3.** No, BB+. I02 is subordinated, and its latest action A07 (2025-06-20) is a downgrade to BB+, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and its latest action A09 (2025-09-15) has outlook POS.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest rating (A09, via E03) is A.

**Q6.** The data doesn't state a reason. It does show VD's Country Ceiling at BB (A12), which caps E05's FC rating at BB (A14), while the uncapped LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's A44 is QA test data and is ignored.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, which is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn, E11 has only a credit opinion, E04 has no rating, VD has only a Country Ceiling, and E16 is QA.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action, A35, came later, on 2025-11-20.

**Q12.** A-. A34 (2023-01-15) assigned A-, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch placement and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26, and the downgrade A27 came on 2026-04-15. E17 is the same entity.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), and the Watch in A35 left the rating unchanged.

**Q17.** No. E06's only 2026 action, A17, is a Rating Watch placement, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's earlier Watch (A35) was superseded by A33, which carries no watch.

**Q19.** E01 and E09, from A03 and A25. E06's outlook is blank after A17, so I did not count it.

**Q20.** No. A19 withdrew E07's rating (WD), and a withdrawal says nothing about default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04 (STIDR, affirmed).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling (A12/A14), and E15's FC rating is A, equal to the CV ceiling (A37/A41).

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose latest action A27 set BBB+.

**Q34.** No. E12 has no parent, while E10 is in E09's group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records, but E03 duplicates E02 and E17 duplicates E10, and E16 is QA test data that describes no real entity.

**Q38.** No. Their LEIs differ (E06 and E13).

**Q39.** A, from A09 (via E03).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is excluded because RESEARCH places it in LU, E07 is withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding the DE on E10.

**Q43.** 1, the Halden Bank entity (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. A local-currency obligation is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating (EX), so I08 stays unrated.

**Q48.** 7: I01 to I07. I08 is unrated.

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