**Q1.** A-. Kestrel's LTIDR was A- from A01 (2024-03-12), and the downgrade to BBB (A02) came only on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, which are affirmations. A03 moved the outlook to Negative, but the rating stayed BBB.

**Q3.** No. I02, the 2031 note, was cut to BB+ by A07, which is sub-investment grade.

**Q4.** Positive. E03 is a duplicate record of E02 (same LEI). Its latest action, A09 (2025-09-15), has a POS outlook and is newer than A08's STA.

**Q5.** A holder takes the risk of the guarantor, E02, which is rated A (A08, A09). The issuer E04 is a finance subsidiary, and I03 itself is also rated A.

**Q6.** This isn't a question with a JSON field. The Valdoria Country Ceiling (A12) is BB, and it caps the foreign-currency rating (A14, BB). The local-currency rating (A13) is BBB-.

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21 and A22, A27, A44). E11's I05 downgrade is an instrument rating, not an issuer downgrade.

**Q8.** E08. It was rated RD from A22 on 2026-07-08. E07's rating was withdrawn (A19), which is not a default.

**Q9.** 13. These are CV, E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and E16. E07 was withdrawn, and E11 has only a "CO" rating.

**Q10.** Depends. Valdoria Telecom's local-currency rating is BBB- (investment grade, A13). Its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 from A- on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating, A30, came on 2024-02-01.

**Q15.** A-. This is E10's rating (A26). E17 is a duplicate record, and the downgrade A27 came later, in April 2026.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now. The 2025 watch (A35) was resolved by the affirmation A33.

**Q17.** No. A17 is a Rating Watch Negative placement with the rating unchanged at A-.

**Q18.** E06, from A17.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. The data shows only a withdrawal (A19) for E07, not a default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08 (A22, RD).

**Q23.** F2, from A04.

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. Of the instruments, I01, I03, I05, I06 and I07 were investment grade on that date. I02 and I04 were not. I08's A47 has action code "EX", which the data doesn't define, so I haven't counted it. If it is a final rating, the count would be 6.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling record (A12), no issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB against the BB ceiling. E15's is A against the A ceiling.

**Q31.** No. No company's foreign-currency rating is above its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor E10 is the risk, and it is rated BBB+ (A27). I05 itself is also rated BBB+.

**Q34.** No. E12 has no parent link to E09, and the shared name isn't evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 and E04. E03 duplicates E02 by LEI.

**Q37.** 17. E03 duplicates E02 and E17 duplicates E10, both by LEI.

**Q38.** No. They have different LEIs, countries and parent records.

**Q39.** A, from A08 and A09.

**Q40.** 6: E01, E02/E03 (one entity), E09, E12, E14 and E16.

**Q41.** BB+, from A44.

**Q42.** DE (E10). The LU record E17 is a RESEARCH duplicate of E10.

**Q43.** 0. The only LU record is E17, which duplicates the DE entity E10.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's local currency. The data doesn't define this explicitly.

**Q45.** No. I07 is rated BBB- (A45). The Country Ceiling of BB caps foreign-currency ratings, and I07 is local-currency.

**Q46.** No. E11 has only a "CO" rating (A46), not an issuer rating (LTIDR).

**Q47.** None. The only action on I08 is A47, with the undefined code "EX" and rating A. I've treated it as not a settled rating, but it could be one.

**Q48.** 7. I01 to I07 each have a standing rating, and I08 is excluded for the reason given in Q47.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16"]},
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
"Q19": {"issuers": ["E01","E09"]},
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
"Q30": {"entities": ["E05","E15"]},
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