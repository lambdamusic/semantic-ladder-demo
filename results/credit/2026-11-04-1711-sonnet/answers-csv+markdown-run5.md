**Q1.** A-. A01 set A- on 2024-03-12, and the next action (A02) came only on 2025-06-20.

**Q2.** No. The only 2026 issuer actions on E01 are A03 and A04, both affirmations (AF), and A03 only moved the outlook to NEG.

**Q3.** No, BB+. I02 is subordinated, and A07 downgraded it to BB+ (speculative grade).

**Q4.** Positive. E03 shares its LEI with E02, so they are one entity, and its latest action is A09 (2025-09-15, POS).

**Q5.** The holder takes the credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and E02/E03's latest LTIDR is A (A09).

**Q6.** The Valdoria Country Ceiling is BB (A12), which caps foreign-currency ratings (A14: BB). The local-currency rating (A13: BBB-) is not capped.

**Q7.** E08 and E10. E08 had downgrades A21 and A22, and E10 had A27. A29 downgrades an instrument (I05), and A44 is on QA record E16, which is ignored.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and RD counts as default.

**Q9.** 12. The issuers are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn (A19), VD has only a Country Ceiling, E11 has only a credit opinion, E04 has no rating, and E16 is QA.

**Q10.** Depends. The foreign-currency rating is BB (A14, speculative), but the local-currency rating is BBB- (A13, investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action (A35) is dated 2025-11-20.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade (DG) for E14. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.

**Q15.** A-. E10 and E17 share an LEI, and A26 (A-) held until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. A17 is a Rating Watch (RW) with the rating unchanged at A-.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's Watch (A35) was cleared by A33, which has no watch value.

**Q19.** E01 and E09. A03 and A25 set NEG outlooks. A17 gives no outlook, so I did not count E06.

**Q20.** No. E07's rating was withdrawn (A19, WD, commercial reasons), which is not a default.

**Q21.** E07. It had LTIDR ratings (A18) and then a withdrawal (A19).

**Q22.** E08. A22 moved it to RD, a default.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR FC is BBB (A03), which is investment grade.

**Q25.** 5. The instruments rated investment grade are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 has only an expected rating (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). A37 is the Country Ceiling, which is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling (A12/A14). E15's FC rating is A, equal to the CV ceiling (A37/A41).

**Q31.** No. E05's FC rating is BB and the VD ceiling is BB. E15's FC rating is A and the CV ceiling is A.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10 (the guarantor), rated BBB+ (A27). I05 is guaranteed by E10.

**Q34.** No. E12 has no parent and no link to E09, and E10's parent is E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. The data has 19 records. E03 and E17 duplicate E02 and E10, and E16 is QA and ignored.

**Q38.** No. Their LEIs differ (E06 and E13).

**Q39.** A (A09 on E03, the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14.

**Q41.** None. E16 is QA and must be ignored.

**Q42.** DE. The RATINGS record E10 holds. The LU on E17 is from a RESEARCH record.

**Q43.** 0. The only LU record is E17, which is the same entity as E10 (DE per RATINGS).

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB- (A45) against a BB ceiling, but the ceiling does not cap local-currency debt.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX).

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