**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed before 2025-01-01.
**Q2.** No. E01's only 2026 actions are affirmations (A03, A04).
**Q3.** No, BB+. I02 was cut from BBB (A23) to BB+ (A07), which is sub-investment grade.
**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (POS, 2025-09-15).
**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02 (issuer E04), and E02/E03 is rated A (A09).
**Q6.** The data doesn't state a reason. The FC rating (A14, BB) equals the Valdoria Country Ceiling (A12, BB), while the LC rating (A13) is BBB-. That suggests the ceiling caps the FC rating, but that is my inference.
**Q7.** E08, E10, E16. These had issuer-rating downgrades in 2026 (A21/A22, A27, A44).
**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.
**Q9.** 13. These are E01, E02 (E03 is the same LEI), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn, and VD has only a country ceiling.
**Q10.** Depends. The LC rating is BBB- (A13, investment grade) but the FC rating is BB (A14, not).
**Q11.** BBB+. A36 downgraded E14 from A- on 2024-09-30.
**Q12.** A-, from A34.
**Q13.** 1. Only A36 is a downgrade; A35 is a watch action.
**Q14.** None. E12's first rating is A30 on 2024-02-01.
**Q15.** A-. A26 stands for E10 (E17 is the same LEI) until the downgrade on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33, A35).
**Q17.** No. A17 is only a Rating Watch Negative action, with the rating still A-.
**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33.
**Q19.** E01 (A03) and E09 (A25).
**Q20.** No. A19 is a withdrawal for commercial reasons, not a default.
**Q21.** E07. It was withdrawn by A19.
**Q22.** E08, via the RD at A22.
**Q23.** F2 (A04).
**Q24.** Yes. BBB (A02, A03).
**Q25.** 5. These are I01, I03, I05, I06 and I07. I08's EX action is not defined, so I excluded it.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.
**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling BB (A14, A12). E15's FC rating is A, equal to the CV ceiling A (A41, A37).
**Q31.** No. No FC rating exceeds its country's ceiling.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** Halden Bank (E10), rated BBB+. E10 is the guarantor of I05 and was downgraded in A27.
**Q34.** No. E12 has no parent link and a different LEI.
**Q35.** 3 (E09, E10, E11). E17 duplicates E10.
**Q36.** 2 (E02, E04). E03 duplicates E02.
**Q37.** 17. The 19 rows include two duplicates, E03 (= E02) and E17 (= E10), by shared LEI.
**Q38.** No. They have different LEIs and are different entities.
**Q39.** A (A08, A09).
**Q40.** 6: E01, E02, E09, E12, E14, E16.
**Q41.** BB+ (A44).
**Q42.** DE. E10 says DE and the LEI ends in DE; E17's LU conflicts and is a duplicate record.
**Q43.** 0. The only LU record is E17, a duplicate of the DE entity E10, so it conflicts with E10 rather than describing a separate entity.
**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency, but the data does not define it.
**Q45.** No. The ceiling (BB) applies to FC, and I07's BBB- (A45) matches the LC rating (A13).
**Q46.** No. E11 has only a "CO" rating (A46), not an issuer rating.
**Q47.** None. I08's only action is EX (A47) on 2026-09-01 and its meaning is undefined, so I can't tell whether the A rating still stands.
**Q48.** 7 (I01–I07), excluding I08 for the reason in Q47.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":13},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06"]},
"Q19":{"issuers":["E01","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":5},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":17},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":6},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":7}
}
```