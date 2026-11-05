**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action, A02, is dated 2025-06-20.

**Q2.** No. The only 2026 actions on Kestrel (E01) are affirmations (A03, A04).

**Q3.** No. The 2031 note (I02) was downgraded to BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E03 shares its LEI with E02, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook, later than A08's STA.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02, and the latest A rating is A09/A11 (E03 is the same entity as E02).

**Q6.** The data doesn't state a reason. The Valdoria country ceiling is BB (A12), and the FC rating of BB (A14) sits at that level while the LC rating is BBB- (A13), which is consistent with a ceiling cap.

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44. A29 downgrades an instrument (I05), not an issuer.

**Q8.** E08. A22 moved it to RD (restricted default) on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV, E15 and E16. E07 is withdrawn (A19), and VD (country ceiling only), E11 (CO type only) and E04 have no issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded to BBB+ on 2024-09-30, and A35 (2025-11-20) came later.

**Q12.** A-, from A34 (2023-01-15), before the A36 downgrade.

**Q13.** 1, from A36.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 assigned it to E10 and A27 only downgraded it on 2026-04-15. E17 is the same entity as E10 (same LEI).

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). A35 was only a watch.

**Q17.** No. The only 2026 action for E06 is A17, a Rating Watch Negative with rating A- unchanged.

**Q18.** E06 (A17). E14's watch (A35) was followed by the A33 affirmation with a STA outlook.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's last action is a withdrawal for commercial reasons (A19), and there is no default rating.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08 expired on 2026-09-01 (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling of BB (A12), not an issuer rating.

**Q30.** E05 (FC BB equals the VD ceiling of BB) and E15 (FC A equals the CV ceiling of A).

**Q31.** No. Only VD and CV have ceilings in the data, and E05 and E15 are at their ceilings, not above. The data cannot settle other countries.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+ (I05 guarantor E10, A27).

**Q34.** No. E12 has no parent and is not linked to E09, E10 or E11.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE vs US) and no link between them.

**Q39.** A, from A09 (E03 is the same entity as E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU, so the sources conflict and I took the primary record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is recorded as DE in the primary source.

**Q44.** Yes, by inference. I07 is in XVD, which appears to be Valdoria's currency, but the data doesn't define it.

**Q45.** No. The ceiling constrains foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45), in line with the LC issuer rating (A13).

**Q46.** No. E11 only has a "CO" rating (A46), not an LTIDR or STIDR, and the data doesn't define CO.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7, I01 to I07. I08 had expired by then (A47).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10", "E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 13},
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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```