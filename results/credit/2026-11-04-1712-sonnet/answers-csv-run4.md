**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02, a downgrade to BBB) came only on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No. I02 was downgraded to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 on 2025-09-15, gives a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02 (A08, A09). The note itself is rated A (A11).

**Q6.** The data doesn't state a reason. The Valdoria Country Ceiling is BB (A12), and the foreign-currency rating is BB (A14) against BBB- local-currency (A13), which is consistent with the ceiling capping the foreign-currency rating.

**Q7.** E08, E10 and E16. These were downgraded in A21/A22, A27 and A44. E06's action (A17) is only a watch. I05 (E11's note) was downgraded in A29, but E11's issuer rating was not.

**Q8.** E08. A22 moved it to RD on 2026-07-08 and nothing later changes that.

**Q9.** 13. They are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19). E04 and E11 have no LTIDR. VD only has a country ceiling (CC), not an issuer rating.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) and its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 on 2025-11-20 came later.

**Q12.** A-. A34 assigned it on 2023-01-15 and the downgrade (A36) came later.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating (A30) is dated 2024-02-01.

**Q15.** A-. A26 gave E10 A- from 2023, and the downgrade in A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33). A35 was a watch, not a rating change.

**Q17.** No. A17 is a Rating Watch Negative with the rating kept at A-.

**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by the A33 affirmation with no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 was withdrawn for commercial reasons (A19) and has never been rated D or RD.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which was rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. They are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade. I08's rating ended with the EX action (A47). I'm reading EX as expired, but the data doesn't define it.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12), not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A). The ceilings come from A12 and A37, and the ratings from A14 and A41.

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11 has parent E10, which has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ (A27). The note itself is also BBB+ (A29).

**Q34.** No. Neither E12 nor E17 is linked to E09 by a parent_id. Sharing the "Halden" name isn't evidence of a group link, so the data records none.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, different countries, and no link between them.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 is recorded as DE in the RATINGS system. The LU record E17 is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU row is E17, which is a duplicate of E10, a DE entity.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's currency, but the data doesn't define XVD explicitly.

**Q45.** No. The BB ceiling constrains foreign-currency ratings, and I07 is a local-currency instrument rated BBB- (A45).

**Q46.** No. E11 has only a "CO" record (A46), and the data doesn't define that type. There is no LTIDR for E11.

**Q47.** None. A47 is an EX action on I08, which I read as the rating having expired.

**Q48.** 7: I01 to I07. I08's rating ended with A47.

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