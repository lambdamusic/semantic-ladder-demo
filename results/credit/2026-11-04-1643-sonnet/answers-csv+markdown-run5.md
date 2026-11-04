**Q1.** A-. E01's LTIDR FC was set by A01 (2024-03-12) and not changed until A02 (2025-06-20).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04).

**Q3.** No, it is BB+. I02 was downgraded to BB+ by A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes the credit risk of E02, the guarantor of I03. E02's current rating is A (A09).

**Q6.** The Valdoria Country Ceiling is BB (A12), and it caps the FC rating (A14, BB). The LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. The E16 downgrade (A44) is QA data and is ignored.

**Q8.** E08. A22 (2026-07-08) set its rating to RD, which counts as default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn. E11 has only a credit opinion. VD has only a ceiling. E16 is QA.

**Q10.** Depends. The FC rating is BB (speculative), and the LC rating is BBB- (investment grade).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+.

**Q12.** A-, from A34.

**Q13.** 1 (A36). A35 is a Watch and A33 is an affirmation.

**Q14.** None. The first rating, A30, came on 2024-02-01.

**Q15.** A-. E17 is the same entity as E10 and has no actions of its own. A26 set A- and the downgrade came later (A27, 2026-04-15).

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now. The Watch (A35) was not a change.

**Q17.** No. A17 is only a Rating Watch.

**Q18.** E06 (A17). E14's Watch (A35) was cleared by A33, which has no watch value.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 withdrew the rating for commercial reasons, which says nothing about default.

**Q21.** E07. Its rating was withdrawn (A19). E16 is QA and ignored.

**Q22.** E08 only (A22, RD).

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The ceiling of A (A37) is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A). The sovereign CV is not a company and sits at BBB+, below the ceiling.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the credit risk of E10, the guarantor of I05. E10's current rating is BBB+ (A27).

**Q34.** No. E12 has no parent link to E09.

**Q35.** 3. These are E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2. These are E02 (with E03) and E04.

**Q37.** 16. There are 19 records, minus 2 duplicates (E03, E17) and minus the QA record E16.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17 (LU).

**Q43.** 0. The only LU record, E17, is a duplicate of E10, which is DE in the system of record.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, the issuer's country.

**Q45.** No. A local-currency obligation is not capped by the ceiling, so the ceiling does not apply to I07 (BBB-, A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. A47 is an Expected rating only, so I08 is unrated.

**Q48.** 7. I01 to I07 are rated, and I08 is not.

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