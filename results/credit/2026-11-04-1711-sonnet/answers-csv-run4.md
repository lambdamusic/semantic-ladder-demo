**Q1.** A-. E01's last action before that date was A01 (2024-03-12, A-); the downgrade A02 came in June 2025.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations (BBB with a Negative outlook, and F2).

**Q3.** No, BB+. I02 was assigned BBB (A23) and cut to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action is A09 (2025-09-15, outlook POS). It supersedes A08 (STA).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02 (A08, and A09 on E03 as the duplicate record); I03 itself is rated A (A11).

**Q6.** The data points to the Country Ceiling. Valdoria's CC is BB (A12), and E05's FC rating is BB (A14) against BBB- in local currency (A13). The data doesn't state the rationale explicitly.

**Q7.** E08, E10 and E16. The issuer downgrades in 2026 are A21 and A22 (E08), A27 (E10) and A44 (E16). I05's downgrade (A29) is an instrument action.

**Q8.** E08. A22 (2026-07-08) rated it RD and nothing later changes that.

**Q9.** 13. The issuers are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), E04 and E11 have no issuer rating (A46 is a CO), and VD has only a CC.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 from A-, and A35 only came later, in November 2025.

**Q12.** A-. A34 (2023-01-15) was still in force.

**Q13.** 1. Only A36 is a downgrade; A33 and A35 are an affirmation and a watch.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. A26 stood until the downgrade A27 on 2026-04-15, and E17 is the same entity as E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The watch in A35 was resolved by A33.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating still A-.

**Q18.** E06 (A17, RWN). E14's watch (A35) was cleared by A33.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. A19 withdrew E07's rating (last rating BB, A18), and there is no default record.

**Q21.** E07. Its rating was withdrawn (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's "EX" action isn't defined in the data, so I did not count it.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A-rated record A39 is the local-currency rating.

**Q29.** None. VD has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB (A12, A14), and E15's FC rating of A equals the CV ceiling of A (A37, A41).

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ (A27). I05 is also BBB+ (A29).

**Q34.** No. E12 has no parent link and is not in E09's hierarchy; the shared name doesn't establish group membership.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries and entity IDs.

**Q39.** A (A08, A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 in RATINGS says DE. The RESEARCH duplicate E17 says LU, which conflicts, and I treated RATINGS as authoritative.

**Q43.** 0. The only LU record is E17, a RESEARCH duplicate of E10 (DE), so it is not a distinct entity. If you took that record at face value the count would be 1.

**Q44.** Yes, inferred. I07 is in XVD, which is not an ISO code but looks like Valdoria's currency. Its BBB- (A45) matches the local-currency rating (A13).

**Q45.** No. The BB ceiling (A12) applies to foreign-currency obligations, and I07 appears to be local-currency.

**Q46.** No. E11 has only a "CO" record (A46), which is not an issuer rating (LTIDR).

**Q47.** None. I08's only record is A47, with action "EX", which the data doesn't define. I read it as an expected or provisional rating rather than a final one, but that's an assumption; if it is a final rating, it is A.

**Q48.** 7: I01–I07. I08 is excluded for the reason in Q47 (it would be 8 if A47 counts).

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