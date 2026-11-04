**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action (A02) is dated 2025-06-20.

**Q2.** No. The only 2026 action on Kestrel Energy (E01) is A03/A04, which are affirmations (BBB, Negative outlook).

**Q3.** No, it is BB+. I02 was assigned BBB (A23), then downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity. A09 (2025-09-15) affirmed it at A with a POS outlook, replacing the STA outlook from A08.

**Q5.** A holder takes the credit risk of Northwind Holdings (E02), the guarantor of I03, rated A (A09/A08). The issuer E04 has no rating of its own.

**Q6.** Valdoria's Country Ceiling is BB (A12). That caps the foreign-currency rating at BB (A14), while the local-currency rating is BBB- (A13). The ceiling is the likely cause, though the data does not state a reason outright.

**Q7.** E08, E10 and E16. The downgrades are A21/A22 (E08), A27 (E10) and A44 (E16). E06's action (A17) is only a watch, and E14's (A33) is an affirmation.

**Q8.** E08. A22 moved it to RD on 2026-07-08 (distressed debt exchange), and nothing later changes that.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a Country Ceiling (CC) record, and E11 has only a "CO" record (A46), so neither counts as having an issuer rating.

**Q10.** It depends on currency basis. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded it from A- to BBB+ on 2024-09-30, and the watch in A35 came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1 time, in A36. A35 is a watch and A33 is an affirmation.

**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 assigned it on 2023-05-01, and the downgrade in A27 came on 2026-04-15. E17 is a duplicate of E10, since the LEI is the same.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+. A35 put it on watch and A33 later affirmed it without a watch.

**Q17.** No. A17 (2026-09-03) places it on Rating Watch Negative at A-, which is not a downgrade.

**Q18.** E06. A17 set RWN on 2026-09-03. E14's RWN (A35) was superseded by the A33 affirmation with no watch.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 had expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (BB, A12), which is not an issuer rating.

**Q30.** E05 (FC BB, equal to the VD ceiling of BB) and E15 (FC A, equal to the CV ceiling of A).

**Q31.** No. Only VD and CV have ceilings, and no company exceeds them.

**Q32.** E09 (E11 → E10 → E09).

**Q33.** A holder takes the credit risk of Halden Bank (E10), the guarantor of I05. E10 is currently rated BBB+ (A27).

**Q34.** No. E12 has no parent link to E09, and the shared "Halden" name is not evidence of common ownership.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries and no link between them.

**Q39.** A.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE. The RESEARCH duplicate E17 says LU, which conflicts.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record says DE. This is a judgement call on conflicting data.

**Q44.** Yes, though this is inferred. I07 is denominated in XVD, which appears to be Valdoria's currency, but the data does not define it.

**Q45.** No. I07 is rated BBB-, above the BB ceiling, but a local-currency obligation is not capped by the foreign-currency ceiling.

**Q46.** No. E11 only has a "CO" record (A46), which is not an issuer rating type.

**Q47.** None. A47 shows the note as EX on 2026-09-01, so it holds no rating now.

**Q48.** 7, which is I01–I07. I08 is excluded because of A47.

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