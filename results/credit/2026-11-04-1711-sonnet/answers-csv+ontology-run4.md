**Q1.** A-. E01's LTIDR (FC) was set to A- by A01 (2024-03-12), and the next action, A02, is not until 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03 and A04), and the downgrade A02 was in 2025.

**Q3.** No, it is BB+. I02 is subordinated and was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) affirmed it with a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, whose latest LTIDR is A (A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), and the FC rating is capped at it (A14, BB). The LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. I05's downgrade (A29) is an instrument rating, and E16 is QA data and ignored.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and RD is a default.

**Q9.** 12. These are E01, E02 (including E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, E04 has no rating, and E16 is QA.

**Q10.** Depends. E05's FC rating is BB, which is speculative (A14), but its LC rating is BBB-, which is investment grade (A13). FC is the headline rating.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later actions (A35, A33) left it unchanged.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade did not come until 2024-09-30.

**Q13.** 1. Only A36 is a downgrade, because the Watch (A35) and affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- by A26 and was not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+; the Watch (A35) and affirmation (A33) did not change it.

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-, so it is not a downgrade.

**Q18.** Only E06 (A17, RWN). E14's Watch (A35) was cleared by the A33 affirmation, which carries no Watch.

**Q19.** E01 (A03) and E09 (A25). E06's last action (A17) carries no outlook.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a credit event, and nothing in the data shows a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only an expected rating (A47, EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A).

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no other country in the data has a ceiling.

**Q32.** E09. E11's parent is E10 (I05 is guaranteed by E10), and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, which A27 downgraded to BBB+.

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 (E03 is a duplicate) and E04.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA, which leaves 16 including the two sovereigns.

**Q38.** No. They have different LEIs, so they are different entities.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, and E10 is domiciled in DE per the RATINGS record.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 is authoritative over the RESEARCH record E17 (LU).

**Q43.** 0. The only LU record is E17, which is a RESEARCH duplicate of E10 (DE in RATINGS).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), but local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not a rating, and its debt is guaranteed by E10.

**Q47.** None. A47 is only an expected rating (EX), so I08 remains unrated.

**Q48.** 7: I01 to I07. I08 has no assigned rating.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```