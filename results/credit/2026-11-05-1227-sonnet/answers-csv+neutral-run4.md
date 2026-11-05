**Q1.** A-. A01 (2024-03-12) set E01's FC LTIDR at A-, and the next action, A02, is not until 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations, and A03 only moved the outlook to negative.

**Q3.** No, it is BB+. I02 is subordinated, and A07 (2025-06-20) downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes E02's credit risk (Northwind Holdings), rated A. I03 is guaranteed by E02, and E02's latest LTIDR is A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), and it caps FC ratings but not LC ratings. E05's FC rating is therefore BB (A14), while its LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument rating, and E16 (A44) is QA data and ignored.

**Q8.** E08. A22 (2026-07-08) took it to RD, which is a default, and nothing later changes that.

**Q9.** 12. The issuers are E01, E02 (including E03), E05, E06, E08, E09, E10 (including E17), E12, E13, E14, CV and E15. E04 and E11 have none, VD has only a ceiling, E07's rating was withdrawn, and E16 is QA.

**Q10.** Depends. Its LC rating is BBB- (investment grade) and its FC rating is BB (speculative), per A13 and A14.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the later A35 is only a watch.

**Q12.** A-. A34 (2023-01-15) set it, and A36 came later.

**Q13.** 1. Only A36 is a downgrade. A35 is a watch and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E17 is the same entity as E10, and A26 stood until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch with A- unchanged, and E06 has no downgrade.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's watch from A35 was cleared by A33, which has no watch.

**Q19.** E01 and E09 (A03 and A25 both carry NEG). E06's A17 carries no outlook, so I did not count it.

**Q20.** No. A19 is a withdrawal for commercial reasons, which says nothing about default.

**Q21.** E07. Its LTIDR was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative, and I08 is only an expected rating (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. VD's ceiling is BB and E05's FC rating is BB. CV's ceiling is A and E15's FC rating is A.

**Q31.** No. E05 (BB) and E15 (A) are exactly at their ceilings, and no other country has a ceiling.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** The holder takes E10's credit risk (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent and is not in E09's chain, while E10 is a subsidiary of E09.

**Q35.** 3: E09, E10 (the same entity as E17) and E11.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. Excluding the QA record E16 leaves 18, and merging E03 into E02 and E17 into E10 leaves 16, counting the two sovereigns.

**Q38.** No. They have different LEIs (E06 549300AMVE…, E13 815600O8X8…).

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is excluded because RESEARCH records it in LU.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. For domicile the RESEARCH record (E17) holds over the RATINGS record.

**Q43.** 1, the single Halden Bank entity (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. It is local-currency debt, so the ceiling does not cap it, and it is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX), so I08 stays unrated.

**Q48.** 7: I01 to I07.

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