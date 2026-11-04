**Q1.** A-. E01's FC LTIDR was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04, and the downgrades A02, A06 and A07 were in 2025.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and then downgraded to BB+ by A07.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** E02's credit risk, rated A. I03 is guaranteed by E02 (the guarantor, not the issuer E04), and E02's latest LTIDR is A (A09, via E03).

**Q6.** The Country Ceiling (A12) caps VD at BB. E05's FC rating is BB (A14) while its LC rating is BBB- (A13), because FC ratings are capped by the ceiling and LC ratings are not.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 is an instrument action, and A44 is a QA record, so it is ignored.

**Q8.** E08, which was rated RD (a default) from A22 on 2026-07-08.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 is withdrawn, E16 is QA, and E04, E11 and VD have no issuer rating.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13) but its FC rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating, A30, came on 2024-02-01.

**Q15.** A-. A26 assigned E10 A- and no later action was recorded against E10 or its duplicate E17 until A27 (2026-04-15), which is after 2026-01-01.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 did not change it).

**Q17.** No. A17 is a Rating Watch placement, not a downgrade.

**Q18.** E06, from A17. E14's earlier Watch (A35) was superseded by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). A17 and the E08 actions carry no outlook, so I did not count them.

**Q20.** No. A19 withdrew E07's rating, which is not a default, and its last rating was BB.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 only has an expected rating.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (FC BB, VD ceiling BB) and E15 (FC A, CV ceiling A).

**Q31.** No. No FC rating exceeds its country's ceiling.

**Q32.** E09, via the chain E11 → E10 → E09.

**Q33.** E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ by A27.

**Q34.** No. E12 has no parent and no LEI link to the Halden Bank group.

**Q35.** 3: E09, E10 (with its duplicate E17) and E11.

**Q36.** 2: E02 (with E03) and E04.

**Q37.** 16. There are 19 records. E03 duplicates E02 and E17 duplicates E10, and E16 is a QA test record that describes no real entity.

**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214).

**Q39.** A.

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, over the RESEARCH duplicate E17, which says LU.

**Q43.** 0. E17 says LU, but it is the same entity as E10, whose RATINGS record says DE.

**Q44.** Yes. I07 pays in XVD, which is VD's domestic currency.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, and it is rated BBB- (A45).

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an Expected rating (A47), which does not count as a rating.

**Q48.** 7, which is I01 to I07.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```