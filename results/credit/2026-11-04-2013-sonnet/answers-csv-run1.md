**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed until A02 on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, which affirmed BBB with a Negative outlook.

**Q3.** No, it is BB+. I02 was cut to BB+ by A07 on 2025-06-20, after BBB under A23.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action, with a POS outlook.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and A09 (on E03, the same entity) shows A.

**Q6.** The data doesn't state a reason. It shows a Valdoria Country Ceiling of BB (A12), a foreign-currency rating of BB (A14) and a local-currency rating of BBB- (A13), which is consistent with the ceiling capping the foreign-currency rating.

**Q7.** E08, E10 and E16. They were downgraded by A21 and A22, A27, and A44. E06's A17 is only a watch, not a downgrade.

**Q8.** E08. A22 moved it to RD on 2026-07-08.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD (country ceiling only), E04 and E11 (CO row only) have no issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 only placed it on watch.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- by A26, and the downgrade A27 came on 2026-04-15. E17 is the same LEI.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. A17 is a Rating Watch Negative, with the rating kept at A-.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's earlier RWN (A35) was resolved by the affirmation A33, which has no watch.

**Q19.** E01 and E09, from A03 and A25. E06's A17 has no outlook value.

**Q20.** No. The last action on E07 is a withdrawal (A19), and its last rating was BB, not a default rating.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 has expired.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency BB equals the Valdoria ceiling of BB, and E15's A equals the Corvenia ceiling of A.

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is issued by E11 but guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link and no shared ownership with E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 by LEI.

**Q38.** No. They have different LEIs, countries and entity IDs.

**Q39.** A, from A09 (on E03, the same entity as E02).

**Q40.** 6: E01, E02, E09, E10 is DE so excluded, E12, E14 and E16. That gives E01, E02, E09, E12, E14 and E16.

**Q41.** BB+, from A44.

**Q42.** DE. E10 in the RATINGS system says DE, and the LU on E17 comes from RESEARCH, a duplicate record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE. If E17's country were trusted, the answer would be 1.

**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's local currency, but the data doesn't define that code.

**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but a ceiling constrains foreign-currency obligations and I07 appears to be local-currency.

**Q46.** No. E11 has only a CO record (A46), not an LTIDR or STIDR.

**Q47.** None. A47 shows I08 expired on 2026-09-01.

**Q48.** 7: I01 to I07. I08 expired.

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