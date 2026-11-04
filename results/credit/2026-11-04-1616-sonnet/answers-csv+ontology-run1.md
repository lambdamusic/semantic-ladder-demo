**Q1.** A-. A01 assigned A- on 2024-03-12, and the next LTIDR FC action (A02) was not until 2025-06-20.

**Q2.** No. The only 2026 Kestrel action is A03, an affirmation (BBB, outlook to Negative).

**Q3.** No. I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. A09 is on E03, which shares E02's LEI, so it is the same entity. It affirmed A with a POS outlook on 2025-09-15.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is guaranteed by E02, and A11 affirmed it at A.

**Q6.** The Country Ceiling for Valdoria (VD, A12) is BB. E05's FC rating is capped at BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument rating, not an issuer's.

**Q8.** E08. A22 downgraded it to RD on 2026-07-08, which is a default.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), and VD has only a Country Ceiling.

**Q10.** Depends. The FC rating is BB (speculative) and the LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded Marlow from A- to BBB+ on 2024-09-30, and A35 (2025-11-20) is later.

**Q12.** A-. A34 assigned A- on 2023-01-15, and A36 came later.

**Q13.** 1. Only A36 is a DG.

**Q14.** None. E12's first action (A30) was on 2024-02-01.

**Q15.** A-. A26 assigned A- and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The Watch in A35 did not change the rating.

**Q17.** No. A17 is a Rating Watch action with the rating unchanged at A-.

**Q18.** E06. A17 put it on RWN on 2026-09-03. E14's earlier Watch (A35) was superseded by A33.

**Q19.** E01 and E09. A03 and A25 give them NEG outlooks. E06's latest action has no outlook recorded.

**Q20.** No. A19 withdrew the rating for commercial reasons, and a withdrawal is not a default. The last rating was BB.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which went to RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR FC is BBB (A03).

**Q25.** 4. I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) are investment grade. I02 (BB+) and I04 (BB) are not.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** It has no issuer rating. VD only has a Country Ceiling (A12), which is not a rating of the sovereign.

**Q30.** E05 and E15. Their FC ratings are BB (ceiling BB) and A (ceiling A).

**Q31.** No. No FC rating exceeds its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A29 downgraded it to BBB+.

**Q34.** No. E12 has no parent and a different LEI, so it is not linked to E09, E10 or E11.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2. E02 and E03 share an LEI and are one entity, and E04 is its subsidiary.

**Q37.** 16. There are 17 records, and E02 and E03 are one entity.

**Q38.** No. They have different LEIs (ORRN… and ORBC…).

**Q39.** A (A09 on the same-LEI record E03, after A08).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn.

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