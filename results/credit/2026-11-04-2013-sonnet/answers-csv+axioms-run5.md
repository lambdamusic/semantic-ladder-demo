**Q1.** A-. A01 assigned A- on 2024-03-12, and the next LTIDR action (A02) only came on 2025-06-20.

**Q2.** No. Kestrel's only 2026 issuer action is an affirmation (A03, A04); its downgrades were in 2025 (A02, A06, A07).

**Q3.** No, it is BB+. I02 was downgraded to BB+ (A07), which replaced the earlier BBB (A23).

**Q4.** Positive. Northwind Holdings (E02) and "NORTHWIND HLDGS" (E03) share a LEI, so they are one entity, and the latest action is A09 (affirmed, POS).

**Q5.** E02, rated A. I03 is guaranteed by E02, so the credit risk is the guarantor's, and E02's rating in force is A (A09, via E03).

**Q6.** Valdoria's Country Ceiling is BB (A12), so the foreign-currency rating is capped at BB (A14). The local-currency rating of BBB- (A13) is not subject to that cap.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22 and E10 in A27. I05's downgrade (A29) is an instrument action, and E16's (A44) is a QA test record.

**Q8.** E08. A22 is RD and is still in force.

**Q9.** 12. They are E01, E02 (= E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn (A19), E16 is a test record, and E11 has only a credit opinion (A46).

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and A35 (2025-11-20) came later.

**Q12.** A-. A34 was the only action in force on that date.

**Q13.** 1. Only A36 is a downgrade, and A35 is a watch placement.

**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.

**Q15.** A-. A26 was in force until A27 on 2026-04-15, and E17 is the same entity as E10.

**Q16.** No. Marlow was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. A17 is a Rating Watch placement with the rating unchanged at A-.

**Q18.** E06. A17 is in force with RWN, and E14's earlier RWN (A35) was superseded by A33.

**Q19.** E01 and E09 (A03, A25). E06's in-force action (A17) carries no outlook.

**Q20.** No. Its rating was withdrawn (A19), and its last rating was BB, not RD or D.

**Q21.** E07. Its rating (A18) ended with the withdrawal (A19).

**Q22.** E08, via RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05 is BB against a VD ceiling of BB, and E15 is A against a CV ceiling of A.

**Q31.** No. Neither E05 nor E15 is above its ceiling, and CV's own BBB+ is a sovereign rating, which the ceiling constraint excludes.

**Q32.** E09. E11's parent is E10 and E10's parent is E09 (RATINGS records).

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating in force is BBB+ (A27).

**Q34.** No. E12 has no parent and no shared LEI with the Halden Bank record, so nothing links it to the group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. Excluding the QA test record E16 leaves 18, and merging the duplicates E03 and E17 leaves 16.

**Q38.** No. They have different LEIs and no link between them.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA test record, so its actions are not treated as in-force ratings.

**Q42.** LU. The RESEARCH record (E17) says LU, and it is the same entity as E10 (shared LEI).

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, which is the domestic currency of VD, the domicile of the issuer E05.

**Q45.** No. The ceiling constraint applies to foreign-currency issuer ratings, and I07 is a local-currency note, so BBB- against a BB ceiling is not a breach.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating in force.

**Q48.** 7: I01 to I07.

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