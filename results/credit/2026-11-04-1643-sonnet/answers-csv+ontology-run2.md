**Q1.** A-. The latest Kestrel (E01) FC LTIDR action on or before that date is A01 (assigned A-, 2024-03-12). The downgrade A02 came later, in June 2025.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations. The downgrade A02 was in 2025.

**Q3.** No. The 2031 note (I02) is rated BB+ after downgrade A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), has a POS outlook.

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, rated A. I03 is guaranteed by E02, so it carries the guarantor's rating. E02's current LTIDR is A (A09, recorded under E03).

**Q6.** The Country Ceiling for Valdoria is BB (A12), and it caps the FC rating. E05's FC rating is BB (A14) and its LC rating is BBB- (A13), which the ceiling does not cap.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument rating, and E16's (A44) is QA data, so both are excluded.

**Q8.** E08. Its latest action, A22 (2026-07-08), set RD, which is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15 and CV. E04 and E11 have no issuer rating, E07 was withdrawn (A19), VD has only a ceiling, and E16 is QA.

**Q10.** Depends. E05 is rated BB on a foreign-currency basis (A14), which is speculative grade, and BBB- on a local-currency basis (A13), which is investment grade.

**Q11.** BBB+. E14 was downgraded to BBB+ in A36 (2024-09-30). The Watch in A35 (2025-11-20) came after this date.

**Q12.** A-. A34 (2023-01-15) is the latest action on or before that date. The downgrade A36 came later.

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch and A33 is an affirmation.

**Q14.** None. The first E12 action, A30, is dated 2024-02-01, after this date.

**Q15.** A-. E17 is the same entity as E10 (same LEI). A26 set A-, and the downgrade A27 was not until April 2026.

**Q16.** No. E14 was BBB+ on 1 January 2025 (A36) and is BBB+ now (A33). The Watch in between (A35) did not change the rating.

**Q17.** No. E06's only 2026 action, A17, is a Rating Watch, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's Watch (A35) was cleared by the later action A33, which has no watch.

**Q19.** E01 and E09. A03 and A25 are their latest actions and both carry a NEG outlook. E06's Watch action has no outlook recorded.

**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal says nothing about default.

**Q21.** E07. It was rated BB (A18) and then withdrawn (A19). E11 has only a credit opinion (A46), which is not a rating.

**Q22.** E08. It was rated RD in A22. No other entity has an RD or D rating.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. They are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 has only an expected rating (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The ceiling (A37) and the LC rating (A39) are different things.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling of BB. E15's FC rating is A, equal to Corvenia's ceiling of A.

**Q31.** No. E05 and E15 are exactly at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10, Halden Bank, rated BBB+. I05 is guaranteed by E10, and E10's current LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent and a different LEI, so it is not linked to E09 or E10.

**Q35.** 3. The group is E09, E10 (with its duplicate E17) and E11.

**Q36.** 2. The group is E02 (with its duplicate E03) and E04.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates by LEI, and E16 is QA and describes no real entity.

**Q38.** No. Their LEIs differ, and E13 is a US bancorp with no parent link.

**Q39.** A. E02 and E03 are one entity, and the latest action, A09, affirmed A.

**Q40.** 5. They are E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, and the RESEARCH record E17 saying LU is overridden.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is DE in RATINGS.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it. Its rating is BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), so it stays unrated until an AS action.

**Q48.** 7. These are I01 to I07. I08 has only an expected rating.

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