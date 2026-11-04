**Q1.** A-. A01 (2024-03-12) set A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. The only 2026 Kestrel issuer actions are affirmations (A03 and A04); the DG A02 was in 2025.

**Q3.** No, BB+. The 2031 note (I02) is subordinated, and its latest action, A07, downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity. The latest action, A09 (2025-09-15), has outlook POS and supersedes A08's STA.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk, and E02/E03's latest LTIDR (A09) is A.

**Q6.** The foreign-currency rating is capped at Valdoria's Country Ceiling of BB (A12). The local-currency rating is not capped, so it sits at BBB- (A13 vs A14).

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. The 2026 downgrade of I05 (A29) is an instrument rating.

**Q8.** E08. A22 moved it to RD (a default) on 2026-07-08, with no later action.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), and E04, E11 and VD have no issuer rating (VD has only a Country Ceiling).

**Q10.** Depends. The foreign-currency rating is BB (speculative), and the local-currency rating is BBB- (investment grade) (A14, A13).

**Q11.** BBB+. A36 downgraded it to BBB+ on 2024-09-30. A35 (a Watch) did not change the rating.

**Q12.** A-. Only A34 (2023-01-15) had been set by then.

**Q13.** 1. Only A36 is a DG; A35 is a Watch and A33 an affirmation.

**Q14.** No rating. The first action on E12 is A30, on 2024-02-01.

**Q15.** A-. A26 set A- and the downgrade A27 came only on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 put it on RWN on 2026-09-03. E14's earlier watch (A35) was superseded by A33, which carries no watch.

**Q19.** E01 and E09. E01's latest action, A03, has outlook NEG, and E09's, A25, has NEG. E06's outlook is blank after the watch (A17), so I left it out.

**Q20.** No. A19 withdrew the rating for commercial reasons, and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19). E08's RD is still a rating.

**Q22.** E08, via the RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The current LTIDR is BBB (A03).

**Q25.** 4. On 2026-10-01, I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) were investment grade; I02 (BB+) and I04 (BB) were not.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The A in A37 is the Country Ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling of BB (A14, A12). E15's is A, equal to Corvenia's ceiling of A (A41, A37).

**Q31.** No. E05 sits at its ceiling and E15 at its own, so none is above.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose latest LTIDR (A27) is BBB+.

**Q34.** No. E12 has no parent and a different LEI, so nothing in the data links it to E09/E10.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 17 records, and E02 and E03 share an LEI.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09 on E03, the same entity as E02.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn.

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