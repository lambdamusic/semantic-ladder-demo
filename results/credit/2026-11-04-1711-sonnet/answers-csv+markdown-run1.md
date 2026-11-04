**Q1.** A-. The latest action on or before 1 Jan 2025 is A01 (2024-03-12, A-), before the downgrade A02.

**Q2.** No. The only 2026 Kestrel actions are A03 and A04, and both are affirmations.

**Q3.** No, it is BB+. I02 was last set by A07 (2025-06-20, BB+), which is speculative grade.

**Q4.** Positive (POS). E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action and carries POS.

**Q5.** A holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, whose current rating comes from A09.

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling, which is BB (A12). The local-currency rating of BBB- (A13) is not capped, and the FC rating of BB (A14) equals the ceiling.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27 (E17 is the same entity). A29 is an instrument rating, and A44 is a QA record, so it is ignored.

**Q8.** E08. A22 moved it to RD, which is a default, and there are no later actions.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, E04 and E11 have no issuer rating (E11 has only a credit opinion), VD has only a ceiling, and E16 is QA.

**Q10.** It depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded it to BBB+, and the next action is A35 in November 2025.

**Q12.** A-. A34 (2023-01-15) holds until A36.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** None. The first Halden Foods action is A30 on 2024-02-01.

**Q15.** A-. A26 holds until the downgrade A27 on 2026-04-15, and E17 is the same entity.

**Q16.** No. It was BBB+ on 1 Jan 2025 and is BBB+ now (A36, A35, A33).

**Q17.** No. A17 (2026) is a Rating Watch, and the rating stays A-.

**Q18.** E06 (A17). E14's Watch from A35 was superseded by the affirmation A33 in 2026, which carries no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 withdrew Pellam's rating for commercial reasons, which is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03), and BBB is investment grade.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The ceiling A37 is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 (FC BB equals the Valdoria ceiling BB) and E15 (FC A equals the Corvenia ceiling A). CV's own FC rating of BBB+ is below the ceiling.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** A holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27.

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. The 19 records include two duplicates (E03 and E17) and one QA record (E16).

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09 on E03, the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, and the RATINGS record gives DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where issuer E05 is domiciled.

**Q45.** No. The ceiling caps only foreign-currency ratings, and this note is local-currency.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. A47 is only an Expected rating (EX), so I08 stays unrated.

**Q48.** 7, namely I01 to I07. I08 is unrated.

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