**Q1.** A-. E01's FC LTIDR was A- from 2024-03-12 to 2025-06-20 (A01), so it covered 1 Jan 2025.

**Q2.** No. E01 was affirmed at BBB on 2026-02-10 (A03), and only the outlook moved to Negative. Its last downgrade was in 2025 (A02).

**Q3.** No. I02 (the 2031 note) has been BB+ since 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E02's current LTIDR carries a POS outlook (A09).

**Q5.** E02 (Northwind Holdings), the guarantor of I03. The note is rated A (A11).

**Q6.** The data doesn't state a reason directly. It does show that Valdoria's Country Ceiling is BB from 2025-04-01. E05's FC rating is BB (A14) and its LC rating is BBB- (A13), which is consistent with the ceiling capping the FC rating.

**Q7.** E08 and E10. E08 was downgraded on 2026-01-20 and 2026-07-08 (A21, A22), and E10 on 2026-04-15 (A27). I count issuer ratings only. The I05 instrument downgrade (A29) is for E11, which has no issuer rating.

**Q8.** E08. Its rating is RD from 2026-07-08 and still in force (A22).

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07's rating was withdrawn (A19), and VD has no rating.

**Q10.** Depends. E05 is BB on the foreign-currency scale (not investment grade) and BBB- on the local-currency scale (investment grade).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade is A36, from A- to BBB+.

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). It was only put on watch in between (A35).

**Q17.** No. E06 stayed at A- and was placed on Rating Watch Negative on 2026-09-03 (A17), which is not a downgrade.

**Q18.** E06 (A17).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn (WD, A19), not moved to a default rating.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which went to RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB, and E15's FC rating of A equals the CV ceiling of A.

**Q31.** No. E05 is at its ceiling and E15 is at its ceiling.

**Q32.** E09.

**Q33.** E10 (Halden Bank), the guarantor of I05. The note is rated BBB+ (A29).

**Q34.** No. E12 has no parent and isn't in E09's group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 16, the number of rows in `entities`, which already has duplicates merged.

**Q38.** No. E06 and E13 are separate entities with different LEIs and countries.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. Brindle Capital isn't in the data.

**Q42.** LU (E10).

**Q43.** 1 (E10).

**Q44.** Yes. I07 has `local_currency` = yes and is denominated in XVD.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency obligation. Its BBB- rating (A45) is not capped by the BB ceiling.

**Q46.** No. E11 has only an instrument rating (I05) and no issuer-rating records.

**Q47.** None. I08 has no rating records.

**Q48.** 7. I01 to I07 each have a rating in force, and I08 has none.

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
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```