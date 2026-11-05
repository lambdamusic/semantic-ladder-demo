**Q1.** A-. E01's LTIDR (FC) was assigned A- in A01 on 2024-03-12 and stayed there until A02 (2025-06-20).

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with a Negative outlook, which is not a downgrade.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and downgraded to BB+ in A07 on 2025-06-20, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity. The latest action is A09 (2025-09-15, Positive), which supersedes A08 (Stable).

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and the E02/E03 LTIDR is A (A09).

**Q6.** The data does not state a cause, but the likely one is the Country Ceiling. E05's FC rating is BB (A14) against an LC rating of BBB- (A13), and Valdoria's ceiling is BB (A12). The ceiling caps FC ratings and not LC ones.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and E16's downgrade (A44) is QA test data and is ignored.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), which is a default, and there is no later action.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08 (RD still counts as a rating), E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, VD has only a ceiling, E11 has only a credit opinion, E04 has no rating, and E16 is QA.

**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action was A35 on 2025-11-20.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34), and the downgrade came later.

**Q13.** 1. The only downgrade is A36. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E17 and E10 share an LEI. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after the Watch (A35) and affirmation (A33).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative, which leaves the rating at A- and is not a downgrade.

**Q18.** E06. It was placed on Watch on 2026-09-03 (A17). E14's Watch (A35) was cleared by the affirmation A33.

**Q19.** E01 and E09. They were affirmed with a Negative outlook in A03 and A25.

**Q20.** No. E07's rating was withdrawn in A19 for commercial reasons, and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08. Its RD in A22 is a default, and no other entity has RD or D.

**Q23.** F2. E01's STIDR was affirmed at F2 in A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are BB+ and BB, and I08 is only Expected.

**Q26.** A+. E15's LC LTIDR is A+ (A40).

**Q27.** A-. I06 was assigned A- in A42.

**Q28.** BBB+. CV's FC LTIDR is in A38. A37 is the ceiling and A39 is the LC rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling (A12), and E15's FC rating of A equals CV's ceiling (A37).

**Q31.** No. No FC rating exceeds its ceiling: E05 is at BB and E15 is at A.

**Q32.** E09. E11's parent is E10, whose parent is E09, which has none.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose rating was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent and is not in E09's chain, which includes E10 and E11.

**Q35.** 3: E09, E10 (the same entity as E17) and E11.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. E03 duplicates E02, E17 duplicates E10, and E16 is QA, which leaves 16.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A. The latest action on E02/E03 is the A09 affirmation.

**Q40.** 5: E01, E02, E09, E12 and E14. E02 counts as GB (E03 is the RESEARCH record, also GB), E07 was withdrawn, and E16 is QA. E17 is LU.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. RESEARCH holds on domicile, and E17 says LU while E10 says DE.

**Q43.** 1. Only the Halden Bank entity (E17, the same as E10) is in LU.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), but the ceiling does not cap local-currency debt, so there is nothing to exceed.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated until an AS action.

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