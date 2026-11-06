**Q1.** A-. Kestrel's LTIDR was A- from A01 (2024-03-12) until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. Kestrel's only 2026 actions are the affirmations A03 and A04, and the downgrades A02, A06 and A07 were in 2025.

**Q3.** No, BB+. The 2031 note (I02) is subordinated, and A07 downgraded it to BB+.

**Q4.** POS. E02 and E03 share an LEI, so they are the same entity. The latest action is A09 (E03, 2025-09-15), an affirmation at A with a positive outlook.

**Q5.** A holder takes the credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, whose latest issuer rating is A (A09).

**Q6.** Valdoria's Country Ceiling is BB (A12), and the foreign-currency rating is capped at it, so E05's FC rating is BB (A14). The local-currency rating of BBB- (A13) is not capped.

**Q7.** E08 (A21, A22) and E10 (A27). E16's downgrade is QA test data and is ignored. The 2026 downgrade of I05 is an instrument, not an issuer.

**Q8.** E08. A22 moved it to RD, a default, on 2026-07-08.

**Q9.** 12. Counting entities once by LEI, the issuers holding an LTIDR are CV, E01, E02/E03, E05, E06, E08, E09, E10/E17, E12, E13, E14 and E15. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. Its FC rating is BB (speculative), but its LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 set it on 2024-09-30, and the next action, A35, came after that date.

**Q12.** A-, from A34.

**Q13.** 1, the downgrade A36.

**Q14.** None. E12's first rating, A30, came on 2024-02-01.

**Q15.** A-. A26 set it, and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ before and after. A35 and A33 were a Watch and an affirmation, not rating changes.

**Q17.** No. A17 is only a Rating Watch.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's Watch from A35 was followed by A33, which carries no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 withdrew the rating for commercial reasons, which is not a default, and its last rating was BB.

**Q21.** E07, withdrawn by A19.

**Q22.** E08, which went to RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The FC rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (BB against a BB ceiling) and E15 (A against an A ceiling).

**Q31.** No.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** A holder takes the credit risk of E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ after A27.

**Q34.** Yes. Halden Foods (E12) has no parent and no link to the Halden group in the data, so E12 is not in the same group as E10. This is "no", not "yes". The JSON below uses "no".

**Q35.** 3: E09, E10 (E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA.

**Q38.** No. They have different LEIs.

**Q39.** A.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10's country is LU per the RESEARCH record.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile.

**Q43.** 1, the entity behind E10 and E17.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is BBB- and local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. A47 is only an expected rating (EX), so I08 is unrated.

**Q48.** 7, I01 to I07. I08 is unrated.

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