**Q1.** A-. A01 (2024-03-12) set Kestrel's LTIDR at A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. The only 2026 actions on Kestrel (E01) are affirmations (A03, A04).

**Q3.** No, it is BB+. I02 (the 2031 subordinated note) was downgraded to BB+ in A07.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) shows POS.

**Q5.** The holder takes the risk of the guarantor, Northwind Holdings (E02), not the issuer E04 (I03 lists E02 as guarantor). E02/E03 is currently rated A (A09).

**Q6.** The data does not state a reason. It shows E05's foreign-currency rating at BB (A14) and its local-currency rating at BBB- (A13). The Republic of Valdoria's country ceiling is BB (A12), which is consistent with the foreign-currency rating being capped there.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44) were downgraded in 2026. Orrin's A17 is only a watch action, not a downgrade.

**Q8.** E08. A22 (2026-07-08) moved it to RD, and nothing later changes that.

**Q9.** 13. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. E07 is withdrawn, VD has only a country ceiling, and E11 has only a "CO" record.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded Marlow to BBB+, and the RWN in A35 only came on 2025-11-20.

**Q12.** A-, from A34.

**Q13.** 1, which is A36.

**Q14.** None. The first rating on Halden Foods (E12) is A30, on 2024-02-01.

**Q15.** A-. This is E10's rating from A26, before the A27 downgrade on 2026-04-15. E17 is a duplicate of E10 (same LEI).

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is still BBB+ (A33). The RWN in A35 is a watch, not a rating change.

**Q17.** No. A17 is a Rating Watch Negative action that keeps A-.

**Q18.** E06. E14's RWN (A35) was superseded by the affirmation in A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, through the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A02, affirmed in A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country ceiling (A12), not an issuer rating.

**Q30.** E05 (FC BB equals the VD ceiling BB) and E15 (FC A equals the CV ceiling A).

**Q31.** No. No company's foreign-currency rating exceeds its country ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes the risk of the guarantor, Halden Bank (E10), per I05. It is currently rated BBB+ (A27).

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10, both by LEI.

**Q38.** No. They have different LEIs, countries and types, and nothing links them.

**Q39.** A (A08, then A09 on the same entity via E03).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn, and E10 is in DE.

**Q41.** BB+ (A44).

**Q42.** DE. The primary RATINGS record E10 says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record, E17, duplicates E10, whose primary record is DE.

**Q44.** Yes, probably. I07 is denominated in XVD, and its BBB- matches E05's local-currency rating (A13), but the data does not define XVD explicitly.

**Q45.** No. The BB ceiling (A12) applies to foreign-currency ratings, and I07 is a local-currency obligation rated BBB-.

**Q46.** No. E11 has only a "CO" record (A46), whose meaning the data doesn't define, and no LTIDR.

**Q47.** None. A47 expired the rating on I08 on 2026-09-01.

**Q48.** 7. I01 to I07 were rated, and I08's rating had expired.

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