**Q1.** A-. A01 assigned E01 A- on 2024-03-12, and nothing changed before 2025-01-01 (A02 is dated 2025-06-20).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); its downgrade (A02) was in 2025.

**Q3.** No, it is BB+. I02's latest action is A07 (2025-06-20, DG to BB+), which supersedes A23 (BBB).

**Q4.** POS. E03 shares E02's LEI, so it is the same legal entity, and A09 (2025-09-15) affirmed A with a Positive outlook, later than A08.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 but guaranteed by E02 (A08/A09).

**Q6.** The data doesn't state a reason. E05's FC rating (A14, BB) equals the Valdoria country ceiling (A12, BB), while its LC rating (A13) is BBB-, which is consistent with a ceiling cap on FC.

**Q7.** E08, E10 and E16. E08 had A21 and A22, E10 had A27, and E16 had A44, all downgrades in 2026.

**Q8.** E08. A22 put it at RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10 (E17 is the same entity), E12, E13, E14, E15, E16 and CV. E07 is withdrawn, and VD only has a country ceiling, not an issuer rating.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13) but its FC rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the first downgrade came later.

**Q13.** 1, from A36.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 assigned E10 A- and the downgrade A27 came on 2026-04-15. E17 is the same LEI.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). A35 was a watch and A33 an affirmation.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33.

**Q19.** E01 and E09. A03 and A25 are the latest actions and both show NEG.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), with no default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, because of the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired on 2026-09-01 (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling (A12, CC, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC is BB, equal to the VD ceiling BB, and E15's FC is A, equal to the CV ceiling A (A37).

**Q31.** No. No FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, E10, rated BBB+. I05 is issued by E11 but guaranteed by E10 (A27).

**Q34.** No. E12 has no parent link to the E09 group, and the data shows no relationship.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10, going by shared LEI.

**Q38.** No. They have different LEIs, countries and entity IDs.

**Q39.** A (A09, which affirmed A8's rating).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 is in DE. E17's LU is a conflicting record of the same LEI from the RESEARCH source.

**Q43.** 0. The only LU row is E17, a duplicate of the DE-domiciled E10.

**Q44.** Depends. I07 is in "XVD" (a currency code not defined in the data), and its BBB- matches E05's LC rating (A13), but the data never says XVD is Valdoria's local currency.

**Q45.** Depends, because it hinges on Q44. I07 is BBB- (A45) against a BB ceiling (A12), but a ceiling applies to FC obligations, not LC ones.

**Q46.** No. E11 only has a "CO" record (A46), not an issuer rating (LTIDR).

**Q47.** None. I08's rating expired (A47, EX) on 2026-09-01.

**Q48.** 7: I01 to I07. I08's rating had expired.

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
"Q44": {"local_currency": "depends"},
"Q45": {"above_ceiling": "depends"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```