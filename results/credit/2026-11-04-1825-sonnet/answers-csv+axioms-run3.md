**Q1.** A-. A01 assigned A- on 2024-03-12, and it stayed in force until A02 on 2025-06-20.

**Q2.** No. The only Kestrel downgrade is A02 (2025); the 2026 action A03 is an affirmation at BBB.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. A09 (2025-09-15) is filed under E03, which shares Northwind Holdings' LEI, so it is the same entity as E02 and supersedes A08's Stable.

**Q5.** E02, rated A. I03 is guaranteed by E02, whose current rating is A (A09 via E03).

**Q6.** The data does not state a reason. It is consistent with the Country Ceiling: VD's ceiling is BB (A12), E05's FC rating is BB (A14), and the LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument, and A44 is E16, a QA test record.

**Q8.** E08. A22 put it at RD on 2026-07-08, and nothing has superseded it.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07's rating was withdrawn (A19), E11 has only a credit opinion, VD has only a ceiling, and E16 is a test record.

**Q10.** Depends. The LC rating is BBB-, which is investment grade (A13), but the FC rating is BB, which is not (A14).

**Q11.** BBB+. A36 downgraded E14 from A- on 2024-09-30, and A35, a watch, came later in 2025-11.

**Q12.** A-. A34 assigned it on 2023-01-15, and A36 had not yet happened.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement.

**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.

**Q15.** A-. A26 assigned A- to E10 in 2023, and the downgrade A27 came on 2026-04-15. E17 is the same entity.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33 affirmed it). The watch in A35 did not change the rating.

**Q17.** No. A17 is a Rating Watch placement at A-, not a downgrade.

**Q18.** E06 (A17). E14's watch (A35) was superseded by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Its BB rating (A18) was withdrawn (A19), and withdrawal is not a default.

**Q21.** E07. Its LTIDR (A18) was withdrawn by A19. E16 is a test record, so its actions are excluded.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. It is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating is only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 (FC BB against a BB ceiling, A14 and A12) and E15 (FC A against an A ceiling, A41 and A37).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link and a different LEI from the E09/E10/E11 group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 by LEI.

**Q38.** No. They have different LEIs, so there is no identity link.

**Q39.** A (A09, positive outlook).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in DE, and E16 is a test record.

**Q41.** None. E16 is a QA test record, so its actions are not ratings in force.

**Q42.** DE. E17 says LU, but it is the same entity as E10, whose RATINGS record says DE.

**Q43.** 0. E17's LU is overridden by the RATINGS record for the same entity (E10, DE).

**Q44.** Yes. I07 is in XVD, and the issuer E05 is domiciled in VD, whose domestic currency is XVD.

**Q45.** No. The Country Ceiling constrains foreign-currency ratings, and I07 is a local-currency note. Its BBB- (A45) is also below the BB ceiling's local-currency irrelevance.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX) for I08.

**Q48.** 7: I01 to I07. I08 has only an expected rating.

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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```