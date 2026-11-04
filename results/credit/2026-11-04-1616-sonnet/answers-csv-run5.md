**Q1.** A-. A01 set A- on 2024-03-12, and the next action, A02, was not until 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, and both are affirmations (BBB/NEG and F2).

**Q3.** No. I02 is rated BB+ after the downgrade in A07, which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so I treated it as the same entity, and its latest action, A09 (2025-09-15), has outlook POS.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and A09/A11 give A for the guarantor and the notes.

**Q6.** The data doesn't state a reason explicitly. The country ceiling for Valdoria (VD, A12) is BB, and the FC rating on E05 (A14) is BB, while the LC rating (A13) is BBB-. That is consistent with the FC rating being capped at the ceiling.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument downgrade, and E11 has no issuer rating of its own.

**Q8.** E08. A22 moved it to RD on 2026-07-08 after a distressed debt exchange, and nothing later changes that.

**Q9.** 12. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is excluded because its rating was withdrawn (A19), and VD has only a country ceiling (CC). I counted E08 because RD is still a rating.

**Q10.** Depends. Its LC rating is BBB- (A13), which is investment grade, and its FC rating is BB (A14), which is not.

**Q11.** BBB+. A36 (2024-09-30) is the latest action before that date.

**Q12.** A-. A34 is the only action before that date.

**Q13.** 1. Only A36 is a downgrade, and A35 is a watch placement.

**Q14.** No rating. The first action on E12 is A30 on 2024-02-01. E12 has no link to the Halden group.

**Q15.** A-. A26 applies until A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33). The watch in A35 was resolved by A33.

**Q17.** No. A17 is a Rating Watch Negative placement and the rating stays A-.

**Q18.** E06, from A17. E14's watch (A35) was superseded by A33, which has no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Its rating was withdrawn for commercial reasons (A19), and its last rating before that was BB.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. Its issuer rating is BBB (A03).

**Q25.** 4. I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) are investment grade. I02 (BB+) and I04 (BB) are not.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The A rating in A37 is the country ceiling, not the issuer rating.

**Q29.** It has no issuer rating. VD has only a country ceiling of BB (A12).

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. Both companies with a ceiling sit exactly at it, and no other country has a ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. E10 guarantees I05, and A27/A29 give BBB+ for both.

**Q34.** No. Nothing in the parent links connects E12 to E09, and its LEI prefix is different, so only the name is similar.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 duplicates E02 (same LEI).

**Q37.** 16. There are 17 rows, but E03 duplicates E02.

**Q38.** No. They have different LEIs and countries (DE vs US), and no link between them.

**Q39.** A. A08 and A09 are both A.

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