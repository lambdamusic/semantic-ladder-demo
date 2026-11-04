**Q1.** A-. E01's long-term foreign-currency rating was set by A01 (assigned A-, 2024-03-12) and held until A02 in June 2025.

**Q2.** No. E01's only 2026 action is the affirmation A03 (BBB, outlook Negative), and an outlook change is not a downgrade. The downgrades A02, A06 and A07 were in 2025.

**Q3.** No. I02 is subordinated and was downgraded to BB+ by A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with a Positive outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest rating is A (A09, shared with E03).

**Q6.** Valdoria Telecom's (E05) foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12), while the local-currency rating is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A44 is on E16, a QA record, so it is ignored, and A29 is an instrument rating.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and RD is a default.

**Q9.** 12. They are E01, E02 (including E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the Watch (A35) came later.

**Q12.** A-. This is the assignment A34 (2023-01-15), before the downgrade.

**Q13.** 1, by A36.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E17 is the same entity as E10 (same LEI), and E10 was rated A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ before 2025-01-01 and is still BBB+ after the Watch (A35) and the affirmation (A33).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which leaves the rating unchanged.

**Q18.** E06. Its Watch (A17, 2026-09-03) is the latest action. E14's Watch (A35) was superseded by the affirmation A33, which carries no Watch.

**Q19.** E01 and E09, per A03 and A25.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn (A19). E08 still holds the rating RD.

**Q22.** E08, by A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. They are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB, and E15's foreign-currency rating of A equals CV's ceiling of A.

**Q31.** No. No foreign-currency rating exceeds its country's ceiling, and E15's local-currency A+ is not capped.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ by A27.

**Q34.** No. E12 has no parent link to E09, and E10 (the same entity as E17) is a subsidiary of E09.

**Q35.** 3: E09, E10 (including E17) and E11.

**Q36.** 2: E02 (including E03) and E04.

**Q37.** 16. There are 19 records. E16 is QA test data, and E03 and E17 duplicate E02 and E10 by LEI.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** Germany (DE). The RATINGS record E10 holds, over the LU shown on the RESEARCH-sourced duplicate E17.

**Q43.** 0. The only LU record, E17, is the same entity as E10, which is domiciled in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of E05's country VD.

**Q45.** No. I07 is rated BBB-, above the BB ceiling, but as a local-currency obligation it is not capped.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, so I08 is still unrated.

**Q48.** 7: I01 to I07.

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