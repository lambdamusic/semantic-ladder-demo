**Q1.** A-. E01's rating was A- (A01) from 2024-03-12 to 2025-06-20.
**Q2.** No. E01's only 2026 action was an affirmation with the outlook moved to Negative (A03), and the rating stayed BBB.
**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is below investment grade.
**Q4.** Positive (POS). E02's current rating row is A09.
**Q5.** E02, the guarantor, and the note (I03) is rated A (A11).
**Q6.** Valdoria's Country Ceiling (VD, BB from 2025-04-01) caps the foreign-currency rating. E05 is BB foreign-currency (A14) against BBB- local-currency (A13).
**Q7.** E08 and E10. E08 went to CCC (A21) and then RD (A22), and E10 went from A- to BBB+ (A27).
**Q8.** E08, which has been RD since 2026-07-08 (A22).
**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07's rating was withdrawn (A19), and E02 and E03 are one merged entity.
**Q10.** Depends. The foreign-currency rating is BB (not investment grade), but the local-currency rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36).
**Q14.** None. E12's first rating began 2024-02-01 (A30).
**Q15.** A- (A26, in force until 2026-04-15).
**Q16.** No. E14 was BBB+ on 1 January 2025 and is BBB+ now (A33). It went through a watch period (A35) in between.
**Q17.** No. E06 was placed on Rating Watch Negative (A17) with the rating still A-.
**Q18.** E06 (A17).
**Q19.** E01 (A03) and E09 (A25).
**Q20.** No. E07's rating was withdrawn (A19), not moved to a default rating, so the data shows no default. The data does not show its status after withdrawal.
**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).
**Q22.** E08 (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 5. The instruments rated investment grade are I01, I03, I05, I06 and I07.
**Q26.** A+ (A40).
**Q27.** A- (I06, A42).
**Q28.** BBB+ (A38).
**Q29.** None. The ratings table has no rating for VD.
**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to the VD ceiling BB, and E15's is A, equal to the CV ceiling A.
**Q31.** No. E05 and E15 are each at their ceiling, not above it.
**Q32.** E09.
**Q33.** E10, the guarantor, and the note (I05) is rated BBB+ (A29).
**Q34.** No. E12 has no parent, and E10 sits under E09.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 and E04.
**Q37.** 16. The entities table is already deduplicated and includes the two sovereigns.
**Q38.** No. E06 and E13 are separate records with different LEIs and countries (DE and US).
**Q39.** A (A09).
**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.
**Q41.** None. Brindle Capital does not appear in the data.
**Q42.** LU (E10).
**Q43.** 1: E10.
**Q44.** Yes. I07 is denominated in XVD with local_currency = yes.
**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency obligation rated BBB- (A45).
**Q46.** No. E11 has only an instrument rating (I05) and no issuer rating.
**Q47.** None. I08 has no rating row.
**Q48.** 7: I01 to I07.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":12},
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
"Q37":{"count":16},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":5},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":7}
}
```