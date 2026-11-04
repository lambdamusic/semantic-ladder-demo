**Q1.** A-. Action A01 (2024-03-12) set A- and the next action, A02, came on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No. I02 is subordinated and its latest rating is BB+ (A07, 2025-06-20), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) gives POS.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk. Its latest LTIDR is A (A09, via E03).

**Q6.** The Valdoria Country Ceiling is BB (A12), and foreign-currency ratings are capped at it. E05's FC rating is BB (A14), while its LC rating is BBB- (A13), which is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is QA test data and is ignored.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and RD is a default.

**Q9.** 12. The issuers are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. I excluded:
- E03 and E17, which duplicate E02 and E10;
- E04, which has no rating of its own;
- E07, whose rating was withdrawn in A19;
- E11, which has only a credit opinion;
- VD, which has only a ceiling;
- E16, which is QA.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the headline foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the later watch (A35) did not change it.

**Q12.** A-. A34 (2023-01-15) set A-, and the downgrade came later.

**Q13.** 1, which is A36.

**Q14.** None. E12's first action, A30, was on 2024-02-01.

**Q15.** A-. E10 (the same entity as E17) was at A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33 affirmed it).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.

**Q18.** E06. The watch was placed on 2026-09-03 (A17). E14's earlier watch (A35) was superseded by the affirmation A33.

**Q19.** E01 and E09, from A03 and A25. E10's outlook was reset to STA in A27.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a credit event.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The current LTIDR is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is unrated, and I02 and I04 are speculative.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05 is FC BB against the VD ceiling of BB, and E15 is FC A against the CV ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, whose current LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent, and the Halden group consists of E09, E10 and E11.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records, minus the duplicates E03 and E17 and the QA record E16.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09, via E03).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is LU rather than GB.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH holds for domicile, and E17 says LU while E10 says DE.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated.

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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```