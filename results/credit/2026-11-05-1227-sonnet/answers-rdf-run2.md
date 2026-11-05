**Q1.** A-. A01 assigned E01 A- on 2024-03-12, and nothing changed it until A02 on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB. The downgrade was A02, in 2025.

**Q3.** No, it is BB+. I02 was BBB (A23), then downgraded to BB+ (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so I treat them as the same entity. E02 was Stable (A08), and the later E03 affirmation A09 (2025-09-15) is Positive.

**Q5.** The guarantor E02, rated A. I03 is issued by E04 but guaranteed by E02, and E02/E03 is A (A09).

**Q6.** The data doesn't state a reason. It is consistent with the country ceiling: E05's FC rating is BB (A14) against LC BBB- (A13), and VD's ceiling (CC) is BB (A12).

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44. A29 is a downgrade of the instrument I05, not of an issuer.

**Q8.** E08. A22 rated it RD on 2026-07-08, with no later action.

**Q9.** 13. E01, E02 (same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV each have a current LTIDR. E07 was withdrawn (A19), and VD has only a country ceiling.

**Q10.** Depends. Its LC rating is BBB- (investment grade, A13) but its FC rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 (2025-11-20) came later.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. E10 and E17 share an LEI, so they are the same entity. A26 gave A- and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). A35 put it on watch and A33 affirmed it.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17). E13, Orrin Bancorp, is a different entity.

**Q18.** E06. A17 is a Rating Watch Negative dated 2026-09-03. E14's watch (A35) was followed by an affirmation (A33).

**Q19.** E01 and E09. Their latest outlooks are Negative (A03, A25).

**Q20.** No. E07 was withdrawn for commercial reasons (A19), not defaulted.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, through the RD rating in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 and I04 are BB+ and BB. I08 expired.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling of BB (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating BB equals VD's ceiling BB (A14, A12). E15's FC rating A equals CV's ceiling A (A41, A37).

**Q31.** No. E05 and E15 are exactly at their ceilings. E15's A+ (A40) is a local-currency rating.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor E10, rated BBB+. I05 is guaranteed by E10, and A29 downgraded E10 to BBB+ (A27).

**Q34.** No. Nothing in the data links E12 to the E09/E10/E11 chain, and the shared name is not evidence.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, and E06 is in DE while E13 is in US.

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE, per E10, which is in the RATINGS source. The duplicate record E17 says LU, so the data conflicts.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE). This is a judgement call, since the two records conflict.

**Q44.** Yes, though this is inferred. I07 is in XVD, which the data does not define, but it looks like Valdoria's currency (E05 is in VD).

**Q45.** No. A country ceiling applies to FC obligations, and I07's BBB- (A45) matches E05's LC rating, which is below the ceiling anyway.

**Q46.** No. E11 only has a CO-type rating (A46) and no LTIDR. The data doesn't define CO.

**Q47.** None. A47 shows the rating as expired (EX) on 2026-09-01.

**Q48.** 7. I01–I07 have current ratings, and I08's expired.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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