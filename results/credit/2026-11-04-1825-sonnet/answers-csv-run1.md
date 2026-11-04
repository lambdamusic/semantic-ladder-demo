**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. The only 2026 actions on Kestrel are affirmations at BBB (A03, A04), though the outlook turned Negative.

**Q3.** No. The 2031 note (I02) was downgraded to BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) gives a POS outlook.

**Q5.** The guarantor Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A11, A09).

**Q6.** The data does not say. It shows only the different ratings, LC BBB- (A13) and FC BB (A14), with no comment. The gap is consistent with the Valdoria country ceiling of BB (A12), but that is inference.

**Q7.** E08, E10 and E16. They received issuer downgrades in 2026 (A21, A22, A27, A44). Instrument I05's downgrade (A29) is not counted here.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and no later action cures it.

**Q9.** 13. Counting E03 and E02 once, the rated issuers are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and the CC rows and E11's CO row are not issuer ratings.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. Marlow was downgraded to BBB+ on 2024-09-30 (A36), and the later action on 2025-11-20 (A35) was after this date.

**Q12.** A-, assigned 2023-01-15 (A34).

**Q13.** 1, from A36 only.

**Q14.** None. Halden Foods was first rated on 2024-02-01 (A30).

**Q15.** A-. E17 shares E10's LEI, and E10 was rated A- from 2023-05-01 (A26) until the 2026-04-15 downgrade (A27).

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).

**Q17.** No. The only 2026 action on Orrin Bank is a Rating Watch Negative placement with A- unchanged (A17).

**Q18.** E06 (A17). Marlow's earlier watch (A35) was resolved by the 2026-05-01 affirmation without a watch (A33).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), not because of a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired on 2026-09-01 (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. The Republic of Valdoria has only a Country Ceiling of BB (A12), not an issuer rating.

**Q30.** E05 and E15. Their FC ratings equal their countries' ceilings: BB for Valdoria (A14, A12) and A for Corvenia (A41, A37).

**Q31.** No. No FC rating exceeds its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor Halden Bank (E10), rated BBB+ (I05 is guaranteed by E10; A27).

**Q34.** No. E12 has no parent link to E09, so the data does not place it in the group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. Of 19 rows, E03 duplicates E02 and E17 duplicates E10, as shown by shared LEIs.

**Q38.** No. They have different LEIs, countries and names.

**Q39.** A. The latest action is an affirmation at A (A09, on E03, the same entity).

**Q40.** 6: E01, E02, E09, E10 (DE, so no), E12, E14 and E16. The GB set is E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record (E10) says DE, while the RESEARCH duplicate (E17) says LU. I used the RATINGS record as the primary source.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is DE in the primary record.

**Q44.** Yes, probably. I07 is denominated in XVD, which appears to be Valdoria's currency, but the data does not define it.

**Q45.** No. I07 is BBB- (A45), matching E05's local-currency rating (A13). The BB ceiling applies to foreign-currency ratings.

**Q46.** No. E11 has only a "CO" rating type (A46), not an LTIDR.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7. I01 to I07 hold ratings, and I08 has expired.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10", "E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 13},
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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```