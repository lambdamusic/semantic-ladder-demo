**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12) and was not changed until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook, and an outlook is not a downgrade.

**Q3.** No. I02 is subordinated and has been rated BB+ since A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are one entity, and its latest action is A09 (affirmed A, Positive outlook, 2025-09-15).

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and the E02/E03 entity's latest rating is A (A09).

**Q6.** Valdoria Telecom's FC rating (A14, BB) is capped by Valdoria's Country Ceiling of BB (A12). Its LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument downgrade, and A44 belongs to QA record E16, which is ignored.

**Q8.** E08. It has been at RD, a default, since A22 (2026-07-08).

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), VD has only a ceiling, E11 has only a credit opinion, and E16 is QA.

**Q10.** Depends. Its LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the Watch in A35 came later (2025-11-20).

**Q12.** A-, from A34.

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. The Halden Bank record E17 has no actions, and E10 (same LEI) held A- (A26) until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). A35 was a Watch, not a change.

**Q17.** No. Orrin Bank AG (E06) has only A17, a Rating Watch. Orrin Bancorp (E13) is a different entity, with a different LEI.

**Q18.** E06, from A17 (2026-09-03). E14's Watch (A35) was superseded by the affirmation in A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's only other action is the withdrawal in A19, which is not a default.

**Q21.** E07. Its rating was withdrawn in A19 (2026-05-12).

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The current rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are BB+ and BB, and I08 has only an Expected action.

**Q26.** A+, the LC rating in A40.

**Q27.** A-, from A42. It is a subordinated note and is rated on its own record.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB (A14) equals Valdoria's ceiling of BB (A12). E15's FC rating of A (A41) equals Corvenia's ceiling of A (A37).

**Q31.** No. No company's FC rating is above its ceiling, and the LC ratings in A13 and A40 are not capped.

**Q32.** E09. E11's parent is E10, and E10's parent is E09, which has no parent.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 or anyone else.

**Q35.** 3. They are E09, E10 (the same entity as E17) and E11.

**Q36.** 2. They are E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records, but E03 duplicates E02 and E17 duplicates E10, and QA record E16 is excluded.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09.

**Q40.** 5. These are E01, E02 (with E03), E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record E17 (LU) overrides E10's DE for domicile.

**Q43.** 1. Only Halden Bank, which is E10 and E17 as one entity.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), but as local-currency debt it is not capped by the BB ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7, which is I01 to I07. I08 is still unrated.

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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```