**Q1.** A-. Kestrel's FC LTIDR was set by A01 (A-, 2024-03-12) and not changed until A02 on 2025-06-20.

**Q2.** No. The only 2026 actions on Kestrel are affirmations (A03, A04).

**Q3.** No. The 2031 note (I02) is subordinated and was last rated BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02, the guarantor of I03), rated A. E02's current rating is A per A09, which was recorded under the duplicate record E03.

**Q6.** Valdoria Telecom's FC rating (A14, BB) is capped by Valdoria's Country Ceiling of BB (A12). Its LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument action, not an issuer one.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and RD is a default.

**Q9.** 12. They are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is withdrawn, E04 and E11 have no issuer rating, and VD has only a Country Ceiling.

**Q10.** Depends. Its LC rating is BBB- (investment grade) and its FC rating is BB (speculative grade); the FC rating is the headline one.

**Q11.** BBB+. A36 downgraded it on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-, set by A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30), so it had no rating on 2024-01-01.

**Q15.** A-. A26 set it, and A27 did not come until 2026-04-15.

**Q16.** No. It was BBB+ throughout; A35 was a Watch and A33 an affirmation.

**Q17.** No. A17 (2026-09-03) is a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 placed it on RWN in 2026-09. E14's Watch (A35) was resolved by the affirmation A33, which carries no Watch.

**Q19.** E01 and E09 (A03, A25). E06's Watch action leaves the outlook blank, so I did not count it.

**Q20.** No. A19 is a withdrawal for commercial reasons, which says nothing about default.

**Q21.** E07, which was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. Its LTIDR is BBB (A03).

**Q25.** 4. I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) are investment grade; I02 (BB+) and I04 (BB) are not.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling (A12), and E15's is A, equal to the CV ceiling (A37).

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes Halden Bank's credit risk (E10, the guarantor of I05), rated BBB+ (A27).

**Q34.** No. E12 has no parent link and a different LEI, so the data shows no connection despite the similar name.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 16. There are 17 records, and E02 and E03 share an LEI.

**Q38.** No. Their LEIs differ (E06 vs E13).

**Q39.** A (A09, recorded under E03, which is the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

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
"Q25": {"count": 4},
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
"Q40": {"count": 5}
}
```