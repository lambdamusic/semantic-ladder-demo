**Q1.** A-. E01's LTIDR (FC) was set to A- by A01 (2024-03-12). The next action, A02, was on 2025-06-20.

**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04, and affirmations are not downgrades.

**Q3.** No, it is BB+. I02 is subordinated, and A07 (2025-06-20) downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI). The latest action is A09 (2025-09-15), which affirmed A with a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and its latest rating is A (A11), in line with E02's A.

**Q6.** Valdoria's Country Ceiling (VD, A12) is BB and caps foreign-currency ratings. E05's FC rating is therefore BB (A14), while its uncapped LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27 (E17 is the same entity as E10). A29 downgraded instrument I05, not an issuer, and A44 is on QA record E16, which is ignored.

**Q8.** E08. A22 (2026-07-08) moved it to RD, a default, and nothing later changes that.

**Q9.** 12. Issuers with an issuer rating on that date are E01, E02 (with E03), E05, E06, E08 (RD), E09, E10 (with E17), E12, E13, E14, E15 and CV. E07 was withdrawn. E11 has only a credit opinion. VD has only a Country Ceiling. E04 has no rating. E16 is QA.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative grade, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and nothing changed it before 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came later, on 2024-09-30.

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch, and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10 was assigned A- by A26 and downgraded only on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 (after A36) and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's Watch from A35 was resolved by the A33 affirmation, which carries no Watch.

**Q19.** E01 and E09. A03 and A25 are their latest actions and both carry a NEG outlook.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), and a withdrawal says nothing about default. Nothing else in the data shows a default.

**Q21.** E07. It had a rating (A18) that was withdrawn (A19). E08 still holds RD.

**Q22.** E08. It reached RD in A22, which is the only default in the data.

**Q23.** F2, from A04 (STIDR, affirmed 2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments on that date are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are speculative grade, and I08 is unrated.

**Q26.** A+, from A40 (E15, LC).

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38 (CV, LTIDR FC). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling (A12). E15's FC rating is A, equal to the CV ceiling (A37).

**Q31.** No. E05's FC rating (BB) and E15's FC rating (A) both sit at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09, which has no parent.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and its latest rating is BBB+ (A29), matching E10's current rating (A27).

**Q34.** No. E12 has no parent, so it is outside E09's group, which contains E09, E10 and E11.

**Q35.** 3. The Halden group is E09, E10 (E17 is the same entity) and E11.

**Q36.** 2. The Northwind group is E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records. E03 duplicates E02 and E17 duplicates E10 (same LEIs), and E16 is QA.

**Q38.** No. Their LEIs differ (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A, from A09 (affirmed 2025-09-15, via E03, the same entity).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn, and E10 is domiciled in LU because the RESEARCH record holds on country.

**Q41.** None. E16 is a QA test record, so its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds on domicile, overriding E10's DE.

**Q43.** 1. Only E10 (via E17) is domiciled in LU.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap, and its BBB- rating (A45) is above BB only in a way the ceiling does not constrain.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47, EX), so it is unrated until an AS action confirms it.

**Q48.** 7. I01 to I07 each have a rating, and I08 has none.

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