**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed it until A02 in June 2025.

**Q2.** No. The only 2026 Kestrel action is A03, an affirmation; the downgrade (A02) was in 2025.

**Q3.** No. I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) carries a POS outlook.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes Northwind Holdings' credit risk, and E02/E03's latest LTIDR (A09) is A.

**Q6.** The Country Ceiling for Valdoria (A12) is BB, which caps foreign-currency ratings (A14, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 (A21, A22) and E10 (A27). A29 is an instrument downgrade, and A44 is a QA record, so it is ignored.

**Q8.** E08. A22 moved it to RD, which is a default, and it is still in force.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15, with E07 withdrawn, E16 a QA record, and E11 and VD holding no issuer rating.

**Q10.** Depends. Its foreign-currency rating is BB (speculative), but its local-currency rating is BBB- (investment grade).

**Q11.** BBB+, from A36 (a downgrade on 2024-09-30).

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch placement.

**Q14.** None. E12's first rating was assigned on 2024-02-01.

**Q15.** A-. E10's A26 holds until A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. A17 is only a Rating Watch placement and the rating stays A-.

**Q18.** E06 (A17). E14's Watch (A35) was superseded by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 withdrew the rating for commercial reasons, and E07 has no default rating.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. Its LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-); I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not the sovereign's own rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** E05 (FC BB against a VD ceiling of BB) and E15 (FC A against a CV ceiling of A).

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose current LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent, so it is not in the group headed by E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records; E03 and E17 duplicate other entities, and E16 is a QA record.

**Q38.** No. They have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 was withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds for country and overrides DE.

**Q43.** 1. E10 and E17 are one entity.

**Q44.** Yes. I07 is in XVD and its issuer is domiciled in VD, whose domestic currency is XVD.

**Q45.** No. It is a local-currency obligation, so the ceiling does not apply.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A08's only action is an expected rating (A47), and no assignment has confirmed it.

**Q48.** 7: I01 through I07.

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