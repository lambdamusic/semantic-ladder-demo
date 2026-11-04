**Q1.** A-. A01 (2024-03-12) set E01 at A-, and nothing changed it until A02 in June 2025.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, and both are affirmations.

**Q3.** No. I02 is subordinated, and A07 (2025-06-20) downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action with outlook POS.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02/E03's latest LTIDR FC is A (A09).

**Q6.** This is not a structured question, so there is no JSON entry. VD's Country Ceiling is BB (A12), which caps E05's foreign-currency rating at BB (A14). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. The other 2026 downgrades are on instrument I05 (A29) and on QA entity E16 (A44), which is ignored.

**Q8.** E08. A22 put it at RD on 2026-07-08, and RD counts as a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 is withdrawn, and E11 and VD hold only a credit opinion (A46) or a Country Ceiling (A12), neither of which is an issuer rating.

**Q10.** No. The headline foreign-currency rating is BB (A14), which is speculative grade. The local-currency rating is BBB- (A13), so the answer is "yes" only on that basis.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 from A- to BBB+, and A35 only added a Watch.

**Q12.** A-. This is from A34 (2023-01-15), before the A36 downgrade.

**Q13.** 1. A36 is the only DG on E14.

**Q14.** None. E12's first action is A30 on 2024-02-01.

**Q15.** A-. A26 set E10 at A-, and the downgrade A27 came in April 2026. E17 shares the LEI but has no actions.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+, since A35 (Watch) and A33 (affirmation) did not change it.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch, which is not a downgrade.

**Q18.** E06. A17 put it on RWN in September 2026. E14's Watch (A35) was resolved by the affirmation A33, which carries no Watch.

**Q19.** E01 and E09. Their latest actions, A03 and A25, both carry a NEG outlook.

**Q20.** No. E07's rating was BB and was then withdrawn for commercial reasons (A19). A withdrawal is not a default.

**Q21.** E07. It was rated BB in A18 and withdrawn in A19.

**Q22.** E08. It reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR FC is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose latest rating is A29's downgrade to BBB+... more precisely A27 (2026-04-15) set E10 at BBB+.

**Q34.** No. E12 has no parent and a different LEI from the Halden Bank group.

**Q35.** 3. The group is E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2. The group is E02 (with its duplicate E03) and E04.

**Q37.** 16. There are 19 records, less the duplicates E03 and E17 and the QA record E16.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, from A09 on the same entity as E02.

**Q40.** 5. The GB issuers are E01, E02, E09, E12 and E14. E07 is withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, over the RESEARCH record E17 (LU).

**Q43.** 0. The only LU record, E17, is a duplicate of E10, and RATINGS says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7. I01 to I07 hold ratings, and I08 does not.

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
"Q10": {"investment_grade": "no"},
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