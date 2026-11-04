**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB (A03, A04). The downgrade was in 2025 (A02).

**Q3.** No. The 2031 note (I02) was last rated BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 share the same LEI, so I treat them as one entity. The latest action is E03's affirmation on 2025-09-15 with a Positive outlook (A09).

**Q5.** The holder takes the credit risk of E02, the guarantor of the I03 notes. E02 is rated A (A09). The issuer E04 has no rating of its own.

**Q6.** The data states no reason. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). Valdoria's country ceiling is BB (A12), which is consistent with the gap, but that link is an inference.

**Q7.** E08 and E10. The 2026 issuer downgrades are A21 and A22 (E08) and A27 (E10). A29 downgraded the I05 instrument, not an issuer.

**Q8.** E08. It was rated RD from 2026-07-08 (A22) with no later action.

**Q9.** 12. Counting E02 and E03 once, the issuers with a live LTIDR are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), and VD has only a country ceiling (A12).

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action is 2025-11-20 (A35).

**Q12.** A-, assigned 2023-01-15 (A34).

**Q13.** 1, the downgrade in A36.

**Q14.** No rating. E12's first rating is dated 2024-02-01 (A30), after the date asked.

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26) and downgraded only on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33, A35). Only the watch status changed, and it was cleared by the affirmation.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17), not a downgrade. Orrin Bancorp (E13) is a different entity.

**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by an affirmation with a Stable outlook on 2026-05-01 (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 4: I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-). I02 (BB+) and I04 (BB) are not investment grade.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The LC rating is A- (A39).

**Q29.** The data cannot settle this. VD has only a country ceiling of BB (A12) and no issuer rating.

**Q30.** E15 and E05. E15's FC rating is A, equal to the Corvenia ceiling (A41, A37). E05's FC rating is BB, equal to the Valdoria ceiling (A14, A12). Other countries have no ceiling data.

**Q31.** No. E15 and E05 are at their ceilings, not above them, and no other country has a ceiling in the data.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05. E10 is currently rated BBB+ (A27).

**Q34.** No. The data links E12 to no parent, so nothing ties it to the E09/E10/E11 group. The shared "Halden" name is not evidence.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2. E02 and E03 are one entity (same LEI), and E04 is its subsidiary.

**Q37.** 16. There are 17 entity records, and E02 and E03 are the same entity.

**Q38.** No. They have different LEIs and countries (DE vs US).

**Q39.** A (A09).

**Q40.** 5: E01, E02 (= E03), E09, E12 and E14.

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
"Q30": {"entities": ["E15", "E05"]},
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