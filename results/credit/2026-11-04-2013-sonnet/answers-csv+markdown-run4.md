**Q1.** A-. A01 assigned A- to E01 on 2024-03-12, and the next action, A02, was not until 2025-06-20.
**Q2.** No. The only 2026 actions on E01's issuer ratings are affirmations (A03, A04).
**Q3.** No. I02 is rated BB+ after the downgrade A07, which is speculative grade.
**Q4.** POS. E03 is the same entity as E02 (same LEI), and its latest action, A09 on 2025-09-15, gives a Positive outlook.
**Q5.** The holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, and the E02/E03 rating was affirmed at A (A08, A09).
**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12). The local-currency rating is not capped, so E05's LC rating is BBB- (A13) and its FC rating is BB (A14).
**Q7.** E08 and E10. E08 had downgrades A21 and A22. E10 had downgrade A27 (the Halden Bank record is the same entity as E17). The downgrade of I05 (A29) is an instrument rating, not an issuer downgrade. A44 on E16 is QA data and ignored.
**Q8.** E08. A22 moved it to RD on 2026-07-08, and RD is a default.
**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19). E11 has only a credit opinion (CO), and VD has only a Country Ceiling (CC). E16 is QA.
**Q10.** Depends on the basis. The local-currency rating is BBB- (A13), which is investment grade. The foreign-currency rating is BB (A14), which is not.
**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action, A35 on 2025-11-20, is only a Watch.
**Q12.** A-, from A34.
**Q13.** 1. Only A36 is a downgrade for E14. A35 is a Watch and A33 is an affirmation.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. E10 (the same entity as E17) was assigned A- by A26 and was not downgraded until A27 in April 2026.
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33).
**Q17.** No. A17 is a Rating Watch placement and leaves the rating at A-.
**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's Watch (A35) was cleared by the affirmation A33, which carries no watch value.
**Q19.** E01 and E09. A03 gave E01 a Negative outlook and A25 gave E09 a Negative outlook.
**Q20.** No. E07's rating was withdrawn (A19), which is not a default, and its last rating was BB.
**Q21.** E07. Its LTIDR was withdrawn by A19, so it has no rating of that type.
**Q22.** E08. It reached RD in A22.
**Q23.** F2, from A04.
**Q24.** Yes. The current LTIDR FC is BBB (A03).
**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A, via the E02 guarantee), I05 (BBB+), I06 (A-) and I07 (BBB-).
**Q26.** A+, from A40.
**Q27.** A-, from A42.
**Q28.** BBB+, from A38. The A in A37 is the Country Ceiling, not the sovereign's rating.
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB. E15's FC rating of A equals CV's ceiling of A.
**Q31.** No. No company's FC rating is above its country's ceiling.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** The holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ by A27.
**Q34.** No. E12 has no parent link, so it is not in E09's group.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 16. There are 19 records. E03 and E17 are duplicates of E02 and E10, and E16 is QA.
**Q38.** No. They have different LEIs.
**Q39.** A, from the affirmation A09.
**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU per the RESEARCH record, E07 was withdrawn, and E16 is QA.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile.
**Q43.** 1. The only entity domiciled in LU is the Halden Bank entity (E10/E17).
**Q44.** Yes. I07 is in XVD, the domestic currency of E05's country, VD.
**Q45.** No. The ceiling applies only to foreign-currency obligations, and I07 is local-currency.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), so it is still unrated.
**Q48.** 7, I01 to I07. I08 is unrated.

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