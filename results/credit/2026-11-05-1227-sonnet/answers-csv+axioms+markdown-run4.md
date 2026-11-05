**Q1.** A-. E01's latest LTIDR (FC) action on or before 1 Jan 2025 is A01 (2024-03-12), which assigned A-.
**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the downgrade A02 was in 2025.
**Q3.** No, BB+. I02 is subordinated, and its latest action is A07 (2025-06-20), a downgrade to BB+.
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) gives POS.
**Q5.** The credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so it carries the guarantor's risk, and E02's current LTIDR (FC) is A (A09).
**Q6.** Valdoria's Country Ceiling (A12) is BB, and it caps foreign-currency ratings. E05's FC rating is BB (A14), while its LC rating (A13) is BBB- and is not capped.
**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. The other 2026 downgrades are on an instrument (A29) and a QA record (A44), so they don't count.
**Q8.** E08. A22 (2026-07-08) set it to RD, a default, and nothing later changes that.
**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15 and CV. E07 is withdrawn (A19), E04, E11 and VD have no issuer rating, and E16 is a QA record.
**Q10.** Depends. E05's LC rating is BBB- (investment grade) and its FC rating is BB (not), so the answer turns on the currency basis.
**Q11.** BBB+. A36 (2024-09-30) is the latest action on or before 1 Jun 2025.
**Q12.** A-. A34 (2023-01-15) was the rating in force then.
**Q13.** 1. Only A36 is a downgrade; A35 is a Rating Watch placement.
**Q14.** None. E12's first rating is A30, assigned on 2024-02-01.
**Q15.** A-. E10's rating was A- from A26 until the downgrade A27 on 2026-04-15.
**Q16.** No. It was BBB+ on 1 Jan 2025, and the later actions (A35 Watch, A33 affirmation) keep it at BBB+.
**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement, and the rating stays A-.
**Q18.** E06 only. A17 (2026-09-03) put E06 on RWN. E14's earlier Watch (A35) was superseded by A33.
**Q19.** E01 (A03) and E09 (A25). E06's latest action A17 gives no outlook, so I don't count it as Negative.
**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.
**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).
**Q22.** E08, which reached RD in A22.
**Q23.** F2 (A04).
**Q24.** Yes. E01's LTIDR is BBB (A03).
**Q25.** 5. On 1 Oct 2026 I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 (BB+) and I04 (BB) are not, and I08 has only an expected rating.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A).
**Q31.** No. E05 and E15 are exactly at their ceilings, and none is above.
**Q32.** E09. E11 has parent E10, and E10 has parent E09, which has none.
**Q33.** The credit risk of E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose LTIDR is BBB+ after A27.
**Q34.** No. E12 has no parent link to E09 or its group.
**Q35.** 3: E09, E10 (the same entity as E17) and E11.
**Q36.** 2: E02 (the same entity as E03) and E04.
**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA test data.
**Q38.** No. E06 and E13 have different LEIs and no link between them.
**Q39.** A (A09 affirmed A, via the same-LEI record E03).
**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.
**Q41.** None. E16 is a QA test record, so its actions are ignored.
**Q42.** LU. The RESEARCH record E17 holds for country and says LU, though E10 says DE.
**Q43.** 1: E10, which is the same entity as E17.
**Q44.** Yes. I07 pays in XVD, the domestic currency of E05's country VD.
**Q45.** No. The ceiling caps only foreign-currency ratings, and I07 is local-currency.
**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.
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