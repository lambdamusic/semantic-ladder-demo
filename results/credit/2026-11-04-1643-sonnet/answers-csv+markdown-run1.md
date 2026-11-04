**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12) until the downgrade in A02 (2025-06-20).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04).

**Q3.** No, BB+. I02's latest rating is the downgrade A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09, is an affirmation with a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest rating is A (A09, recorded on E03).

**Q6.** The Country Ceiling for VD is BB (A12). It caps the foreign-currency rating at BB (A14), while the local-currency rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and A44 is a QA record, so both are ignored.

**Q8.** E08. It has been at RD since A22 (2026-07-08).

**Q9.** 12. The issuers are E01, E02 (same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn. VD has only a Country Ceiling, E11 only a credit opinion, and E16 is QA.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and nothing changed it before 2025-06-01.

**Q12.** A-, from A34.

**Q13.** 1 (A36).

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-, from A26. The downgrade A27 came later, on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). The RW in A35 did not change the rating.

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.

**Q18.** E06 (A17). E14's watch was cleared by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's current LTIDR is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05 is at BB against VD's ceiling of BB, and E15 is at A against CV's ceiling of A.

**Q31.** No. Both E05 and E15 sit exactly at their ceilings, and no company is above one.

**Q32.** E09. E11 is owned by E10, which is owned by E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent and a different LEI from the Halden Bank group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 (E03 is a duplicate) and E04.

**Q37.** 16. The 19 records minus two duplicates (E03, E17) and the QA record E16.

**Q38.** No. They have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. E17 says LU, but the RATINGS record E10 holds.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD.

**Q45.** No. I07 is a local-currency obligation, so the ceiling does not apply. It is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), so it is unrated.

**Q48.** 7: I01 to I07. I08 is unrated.

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