**Q1.** A-. A01 set E01's foreign-currency LTIDR at A- on 2024-03-12, and the next action (A02) came only on 2025-06-20.

**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04, and affirmations are not downgrades.

**Q3.** No. I02 is rated BB+ (A07, a downgrade from BBB in A23), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and its latest action (A09, 2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes the credit risk of E02, which is rated A. I03 is guaranteed by E02, and E02's latest rating is A (A08, A09 via E03).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling. VD's ceiling is BB (A12), so E05's foreign-currency rating is BB (A14) while its local-currency rating is BBB- (A13), which the ceiling does not cap.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and A44 is on QA record E16, which is ignored.

**Q8.** E08. It was downgraded to RD (restricted default) on 2026-07-08 (A22) and has no later action.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 was withdrawn, E04 has no rating, E11 has only a credit opinion, VD has only a Country Ceiling, and E16 is QA.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action was on 2025-11-20.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came later.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** None. E12's first rating action (A30) was on 2024-02-01.

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. E06's only 2026 action (A17) is a Rating Watch, and the rating stays A-.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's Watch (A35) was cleared by the affirmation A33, which carries no watch.

**Q19.** E01 and E09. A03 and A25 are the latest outlooks for each, and both are NEG.

**Q20.** No. E07's rating was withdrawn (A19), which is not a credit event, and it was never rated in default.

**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's long-term rating is BBB (A03), which is investment grade.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 and I04 are speculative, and I08 is unrated.

**Q26.** A+ (A40).

**Q27.** A- (A42). This is below the Corvenia ceiling of A.

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05 is at BB, equal to the VD ceiling of BB, and E15 is at A, equal to the CV ceiling of A (A41, A37).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes the credit risk of E10, which is rated BBB+ (A27). I05 is guaranteed by E10.

**Q34.** No. E12 has no parent and is not in the chain E11, E10, E09.

**Q35.** 3: E09, E10 (which includes E17) and E11.

**Q36.** 2: E02 (which includes E03) and E04.

**Q37.** 16. The 19 records minus QA record E16, minus the duplicates E03 (same LEI as E02) and E17 (same LEI as E10). The two sovereigns, VD and CV, are counted.

**Q38.** No. They have different LEIs, so they are different entities.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU per the RESEARCH record, E07 is withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA test record, so its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile.

**Q43.** 1 (E10 / E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05's country is VD.

**Q45.** No. I07 is local-currency debt, so the ceiling does not apply to it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated until an AS action.

**Q48.** 7. I01 to I07 are rated, and I08 is not.

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