**Q1.** A-. E01's rating on 1 Jan 2025 was the A- assigned 2024-03-12 (A01); the next action was 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB (A03, A04). Its downgrades were in 2025 (A02, A06, A07).

**Q3.** No. The 2031 note (I02) is BB+ after the 2025-06-20 downgrade (A07). That is below BBB-, using the conventional cut-off, since the data defines no scale.

**Q4.** Positive. E03 and E02 share the LEI NWND00HOLDINGS00GB42, so I treat them as one entity. The latest action is A09 (2025-09-15), which has a Positive outlook and supersedes A08 (Stable).

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes E02's risk. I03 and E02/E03 are both A (A10, A11, A09).

**Q6.** The data gives no stated reason. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB equals Valdoria's country ceiling (A12), which is consistent with a ceiling cap.

**Q7.** E08 and E10. E08 was downgraded to CCC and then RD (A21, A22), and E10 to BBB+ (A27). I05 was also downgraded (A29), but that is an instrument rating, not an issuer rating.

**Q8.** E08. It has been at RD since 2026-07-08 (A22), with no later action.

**Q9.** 12. These are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. I excluded E07, which was withdrawn (A19), and VD, which has only a country ceiling (A12).

**Q10.** Depends. E05 is BB in foreign currency (A14) and BBB- in local currency (A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36). The Watch on 2025-11-20 (A35) came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating is dated 2024-02-01 (A30), after that date.

**Q15.** A-. E10 held A- from 2023-05-01 (A26), and the downgrade came on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ throughout. The Watch (A35) was resolved by an affirmation at BBB+ (A33).

**Q17.** No. E06's 2026 action is a Rating Watch Negative at A- (A17), not a rating change.

**Q18.** E06 (A17). E14's earlier Watch (A35) was resolved by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's last action is a withdrawal "for commercial reasons" (A19), and there is no default rating.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is BBB (A03).

**Q25.** 4. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-). I02 (BB+) and I04 (BB) are not.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country-ceiling record, BB (A12), and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling of BB (A14, A12). E15's FC rating is A, equal to Corvenia's ceiling of A (A41, A37).

**Q31.** No. No FC rating exceeds its country's ceiling. E15's LC rating (A+) is above the ceiling, but that is local currency.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** E10, rated BBB+. I05 is issued by E11 but guaranteed by E10, whose current rating is BBB+ (A27).

**Q34.** No. E12 has no parent or other link to E10 or E9 in the data. The shared "Halden" name is not evidence of a group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is the same entity as E02 (same LEI).

**Q37.** 16. There are 17 entity records, but E02 and E03 share an LEI.

**Q38.** No. They have different LEIs and countries (DE and US) and different record IDs (E06, E13).

**Q39.** A (A09).

**Q40.** 5: E01, E02/E03, E09, E12 and E14. E07 is excluded because it was withdrawn.

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