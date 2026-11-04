**Q1.** A-. E01's latest action on or before 1 Jan 2025 was A01 (assigned A- on 2024-03-12, FC).

**Q2.** No. E01's only 2026 action is A03/A04 (affirmations on 2026-02-10), and affirmations are not downgrades.

**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive. E02 and E03 share the LEI NWND00HOLDINGS00GB42, so they are one entity. The latest action is A09 (E03, 2025-09-15, POS), which supersedes A08 (STA).

**Q5.** The guarantor, Northwind Holdings (E02, same entity as E03), rated A. I03 is guaranteed by E02 (issuer E04), and A11 rates I03 at A.

**Q6.** The data points to the Country Ceiling. E05 is domiciled in VD, whose ceiling is BB (A12), and its FC rating is BB (A14) against BBB- local currency (A13). FC ratings are capped by the ceiling and LC ratings are not.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22 and E10 in A27. A29 is an instrument downgrade (I05), not an issuer downgrade.

**Q8.** E08. A22 moved it to RD (a default) on 2026-07-08, with no later action.

**Q9.** 12. These are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, VD has only a Country Ceiling, and E04 and E11 have no issuer rating.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative, A14).

**Q11.** BBB+. A36 (DG to BBB+, 2024-09-30) was still in force on that date; the A35 Watch came later.

**Q12.** A-. This is A34, assigned on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** No rating. E12's first action is A30 on 2024-02-01, after the date.

**Q15.** A-. A26 held for E10 until the downgrade in A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 1 Jan 2025 and is still BBB+ (A35 and A33 did not change it).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch with the rating unchanged at A-. Orrin Bancorp (E13) is a different entity with a different LEI.

**Q18.** E06. A17 (2026-09-03) is its latest action. E14's Watch (A35) was followed by the A33 affirmation, which ended it.

**Q19.** E01 and E09. A03 and A25 are their latest LTIDR actions, both with a NEG outlook. E06's A17 carries no outlook, so I did not count it.

**Q20.** No. E07 was withdrawn (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn in A19 on 2026-05-12.

**Q22.** E08. Its RD rating (A22) is the only default in the data.

**Q23.** F2, from A04 (STIDR affirmed 2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 4. On 1 Oct 2026, I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) were investment grade. I02 (BB+) and I04 (BB) were not.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38, CV LTIDR FC). A37 is the Country Ceiling of A, which is not the sovereign's rating.

**Q29.** None in the data. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating BB equals the VD ceiling BB (A12, A14), and E15's FC rating A equals the CV ceiling A (A37, A41).

**Q31.** No. E05 and E15 are at their ceilings, not above, and no other company's country has a ceiling in the data.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10 and rated BBB+ (A29), in line with E10's BBB+ (A27).

**Q34.** No. E12 has no parent link or other connection to the Halden Group (E09, E10, E11); only the name is similar.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (same entity as E03) and its subsidiary E04.

**Q37.** 16. There are 17 entity records, but E02 and E03 share an LEI.

**Q38.** No. E06 and E13 have different LEIs (ORRN00BANK00000DE233 and ORBC00BANCORP000US45).

**Q39.** A, from A09 (E03 record, which is the same entity as E02).

**Q40.** 5: E01, E02/E03, E09, E12 and E14. E07 is GB but was withdrawn.

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
"Q14": {"rating": null},
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
"Q25": {"count": 4},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": null},
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
"Q40": {"count": 5}
}
```