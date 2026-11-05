**Q1.** A-. A01 set Kestrel's FC LTIDR at A-, and the next action (A02) came in June 2025.
**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).
**Q3.** No. I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), has POS.
**Q5.** The holder takes the credit risk of Northwind Holdings (E02), rated A. I03 is guaranteed by E02, whose latest rating is A (A09 via E03).
**Q6.** Valdoria's Country Ceiling (VD, A12) is BB, which caps the foreign-currency rating. The FC rating is therefore BB (A14), while the uncapped LC rating is BBB- (A13).
**Q7.** E08 (A21, A22) and E10 (A27). The I05 downgrade (A29) is an instrument action, and E16 is QA data and ignored.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and RD is a default.
**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, VD has only a Country Ceiling, E11 has only a credit opinion, and E04 has nothing.
**Q10.** Depends. The LC rating is BBB- (investment grade, A13), but the FC rating is BB (speculative grade, A14).
**Q11.** BBB+. The downgrade A36 (2024-09-30) set it, and the watch in A35 came later.
**Q12.** A-. A34 was the latest action at that date.
**Q13.** 1 (A36).
**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30).
**Q15.** A-. A26 was in force, and the downgrade A27 came on 2026-04-15.
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33).
**Q17.** No. A17 is only a Rating Watch, and the rating stays A-.
**Q18.** E06. A17 placed it on RWN in September 2026, and E14's watch was cleared by the affirmation A33.
**Q19.** E01 (A03) and E09 (A25).
**Q20.** No. E07's rating was withdrawn (A19), which is not a default, and it has no rating now.
**Q21.** E07, whose rating was withdrawn in A19.
**Q22.** E08, which reached RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. The FC LTIDR is BBB (A03).
**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38). The Country Ceiling A37 is not the sovereign's rating.
**Q29.** None. VD has only a Country Ceiling (A12).
**Q30.** E05 (FC BB equals the VD ceiling BB) and E15 (FC A equals the CV ceiling A).
**Q31.** No. No company's FC rating exceeds its country's ceiling.
**Q32.** E09. The chain runs E11 to E10 to E09.
**Q33.** The holder takes the credit risk of the guarantor, Halden Bank (E10), rated BBB+ (A27).
**Q34.** No. E12 has no parent, so it is outside the E09 group.
**Q35.** 3: E09, E10 (the same entity as E17), and E11.
**Q36.** 2: E02 (the same entity as E03) and E04.
**Q37.** 16. There are 19 records, minus the duplicates E03 and E17 and the QA record E16.
**Q38.** No. Their LEIs differ.
**Q39.** A (A09 affirmed it via E03, the same entity).
**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA data.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for country.
**Q43.** 1. E10 and E17 are the same entity.
**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.
**Q45.** No. It is local-currency debt, so the ceiling doesn't apply.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an expected rating (A47, EX) and no assignment.
**Q48.** 7, namely I01 to I07.

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