**Q1.** A-. E01's long-term foreign-currency rating was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03 (2026-02-10), an affirmation at BBB.

**Q3.** No. The 2031 note (I02) was cut to BB+ in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive. E02 and E03 share the same LEI, so I treated them as one entity. The latest outlook is Positive in A09 (E03, 2025-09-15), which supersedes the Stable in A08.

**Q5.** The holder takes the guarantor's risk, E02, which is rated A. I03 is issued by E04 and guaranteed by E02, and the latest rating is A (A09, A11).

**Q6.** The data doesn't state a reason. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The VD country ceiling is BB (A12), which is consistent with a ceiling effect, but that is inference.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument rating, not an issuer rating, so I excluded it.

**Q8.** E08. A22 (2026-07-08) rates it RD, with no later action.

**Q9.** 12. These are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is excluded because its rating was withdrawn in A19, and VD has only a country ceiling (A12).

**Q10.** Depends. The foreign-currency rating is BB, which is not investment grade (A14). The local-currency rating is BBB-, which is investment grade (A13).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30 on 2024-02-01, so it was unrated on 2024-01-01.

**Q15.** A-, from A26. The downgrade in A27 came on 2026-04-15, after that date.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). The Rating Watch in A35 was resolved by the affirmation in A33.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17). Orrin Bancorp (E13) is a different entity.

**Q18.** E06. A17 (2026-09-03) placed it on Rating Watch Negative, with no later action.

**Q19.** E01 and E09, from A03 and A25. E06 is on watch and its action carries no outlook.

**Q20.** No. E07 was rated BB (A18) and then withdrawn for commercial reasons (A19), with no default rating.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which was rated RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The long-term issuer rating is BBB (A03).

**Q25.** 4. I01 is BBB, I03 is A, I05 is BBB+ and I06 is A-. I02 (BB+) and I04 (BB) are not investment grade.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** The data has no issuer rating for VD. A12 is a country ceiling of BB, not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB (A14) equals the VD ceiling of BB (A12). E15's A (A41) equals the CV ceiling of A (A37). CV itself is BBB+, below its ceiling.

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no other company has a ceiling in the data.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes the guarantor's risk, E10, which is rated BBB+ after A27 (2026-04-15). I05 is issued by E11 and guaranteed by E10.

**Q34.** Depends. E12 has no parent or group link to the Halden entities (E09, E10, E11). Only the name is similar, so the data can't settle it.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (the same entity as E03) and its subsidiary E04.

**Q37.** 16. There are 17 entity records, but E02 and E03 share one LEI. Instruments are not counted.

**Q38.** No. They have different LEIs, countries and entity types.

**Q39.** A, from A09 and A11, with E02 and E03 treated as one entity.

**Q40.** 5: E01, E02 (the same entity as E03), E09, E12 and E14. E07 is excluded because it was withdrawn.

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
"Q34": {"same_group": "depends"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5}
}
```