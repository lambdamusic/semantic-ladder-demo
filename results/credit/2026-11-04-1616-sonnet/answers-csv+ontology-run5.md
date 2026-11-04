**Q1.** A-. A01 (2024-03-12) set E01 at A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with the outlook revised to Negative, and that is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), and its latest rating is BB+ (A07), which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and its latest action is A09 (2025-09-15) with a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's rating is A (A08, A09). I03 itself is also rated A (A11).

**Q6.** Valdoria's Country Ceiling is BB (A12) and it caps foreign-currency ratings, so E05's FC rating is BB (A14). Its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument rating, not an issuer one.

**Q8.** E08. A22 moved it to RD (restricted default) on 2026-07-08, and RD counts as default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E04 and E11 have no rating of their own, and VD has only a Country Ceiling.

**Q10.** No. The headline FC rating is BB (A14), which is speculative grade. The LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later actions (A35, A33) leave it at BBB+.

**Q12.** A-. This is from A34, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first action is A30 on 2024-02-01, so it had no rating on 2024-01-01.

**Q15.** A-. E10 was assigned A- in A26, and the downgrade (A27) came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The Watch in A35 did not change the rating.

**Q17.** No. A17 for E06 is a Rating Watch Negative, and the rating stays A-.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's Watch (A35) was resolved by the affirmation in A33.

**Q19.** E01 and E09. A03 and A25 set their outlooks to NEG, and neither has had a later action.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and a withdrawal says nothing about default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 4. These are I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-). I02 (BB+) and I04 (BB) are speculative grade.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not the sovereign's own rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB (A14), equal to Valdoria's BB ceiling (A12). E15's FC rating is A (A41), equal to Corvenia's A ceiling (A37).

**Q31.** No. Both companies with a ceiling are exactly at it, not above it.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ (A27). I05 is also BBB+ (A29).

**Q34.** No. E12 has a different LEI and no parent link to the E09 group, so only the name is similar.

**Q35.** 3, namely E09, E10 and E11.

**Q36.** 2. E02 (with its duplicate record E03) and E04.

**Q37.** 16. There are 17 records, and E02 and E03 share an LEI and are one entity.

**Q38.** No. E06 and E13 have different LEIs and no link between them.

**Q39.** A. The latest action on this entity, via E02 and E03, is A09, an affirmation at A.

**Q40.** 5, namely E01, E02, E09, E12 and E14. E07 (GB) had its rating withdrawn.

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
"Q10": {"investment_grade": "no"},
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