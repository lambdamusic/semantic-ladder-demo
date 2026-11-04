**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04).

**Q3.** No, BB+. I02 was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 is a duplicate of E02 (same LEI), and its latest action is A09 on 2025-09-15, with a POS outlook.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, and both I03 (A11) and E02 (A09) are rated A.

**Q6.** The Republic of Valdoria's country ceiling is BB (A12), which caps E05's foreign-currency rating at BB (A14). Its local-currency rating is BBB- (A13). This is an inference from the records, since the data doesn't state the cause.

**Q7.** E08, E10 and E16 had issuer-rating downgrades in 2026 (A21, A22, A27, A44). I05 (A29) is an instrument downgrade, not an issuer one.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country ceiling, and E11 has only a "CO" rating, which the data doesn't define.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36).

**Q12.** A-. This is E14's rating from A34, assigned 2023-01-15.

**Q13.** 1 (A36). The watch (A35) and affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was on 2024-02-01 (A30).

**Q15.** A-. E10 was rated A- from A26 and downgraded only on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A36, A35, A33).

**Q17.** No. E06 has only a Rating Watch Negative action, with the rating held at A- (A17).

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). E06's latest action (A17) has no outlook recorded.

**Q20.** No. E07 was withdrawn for commercial reasons (A19), with no default rating.

**Q21.** E07 (withdrawn, A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08's rating expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 (FC BB at the Valdoria ceiling of BB) and E15 (FC A at the Corvenia ceiling of A). No other country has a ceiling in the data.

**Q31.** No. Only VD and CV have ceilings, and E05 and E15 sit exactly at theirs.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ in A27 (I05 itself is BBB+, A29).

**Q34.** No. E12 has no parent link to the E09/E10 group, and only the name suggests a connection.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. E06 and E13 have different LEIs and countries.

**Q39.** A (A09 affirmed, on E03, the duplicate of E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, and the RESEARCH duplicate E17 (same LEI) says LU.

**Q43.** 0. The only LU record is E17, a duplicate of the German E10.

**Q44.** Yes, probably. I07 is in XVD, which looks like Valdoria's currency, and its BBB- matches E05's local-currency rating. The data doesn't define XVD explicitly.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 only has a "CO" type rating (A46), not an issuer rating.

**Q47.** None. I08's rating expired on 2026-09-01 (A47, EX).

**Q48.** 7: I01 to I07. I08 had expired.

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