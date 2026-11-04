**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01), and the next action was 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), and the outlook change to NEG is not a downgrade.

**Q3.** No. I02 is subordinated and was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (2025-09-15, POS).

**Q5.** The holder takes Northwind Holdings' (E02) credit risk, rated A. I03 is guaranteed by E02, so it is rated on the guarantor (A09 and A11, rating A).

**Q6.** The Valdoria Country Ceiling is BB (A12), which caps foreign-currency ratings. E05's FC rating is therefore BB (A14), while its LC rating is BBB- (A13), which is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is QA test data and is ignored. I05's downgrade (A29) is an instrument rating, not an issuer's.

**Q8.** E08. It went to RD on 2026-07-08 (A22), and RD is a default.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10 (E17 is the same entity), E12, E13, E14, CV and E15. E07 was withdrawn. E04, E11 and VD hold no issuer rating (E11 has only a credit opinion and VD only a ceiling).

**Q10.** No. The headline foreign-currency rating is BB (A14), which is speculative grade. Only the LC rating (BBB-, A13) is investment grade.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action is 2025-11-20.

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34), before the downgrade.

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26), and the downgrade to BBB+ came on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33). A35 was only a Watch.

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which leaves the rating unchanged.

**Q18.** E06. It was placed on RWN on 2026-09-03 (A17). E14's Watch (A35) was superseded by the affirmation A33 with no watch.

**Q19.** E01 and E09. Their latest actions carry a NEG outlook (A03, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07. Its LTIDR was withdrawn on 2026-05-12 (A19).

**Q22.** E08. It reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an Expected action (A47), so it is unrated.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the Valdoria ceiling of BB (A12, A14). E15's FC rating is A, equal to the Corvenia ceiling of A (A37, A41). No other country has a ceiling in the data.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes Halden Bank's (E10) credit risk, rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27.

**Q34.** No. E12 has no parent and a different LEI, so it is not linked to E09 or E10.

**Q35.** 3. These are E09, E10 (E17 is the same entity) and E11.

**Q36.** 2. These are E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA test data.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09, affirmed; same entity as E03).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 is withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, so the LU on E17 is ignored.

**Q43.** 0. The only LU record is E17, which is a duplicate of E10, whose RATINGS record says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7. These are I01 to I07, and I08 is unrated.

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
"Q10": {"investment_grade": "no"},
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