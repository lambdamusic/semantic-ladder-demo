**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is an affirmation at BBB (A03, A04). The instrument downgrades I01 and I02 (A06, A07) were in 2025.

**Q3.** No. I02 (2031 note) was downgraded to BB+ in A07, which is below investment grade.

**Q4.** Positive. E03 and E02 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15), which gives a Positive outlook.

**Q5.** The guarantor E02 (Northwind Holdings), rated A. I03 is issued by E04 and guaranteed by E02. E02's LTIDR is A (A08, A09).

**Q6.** The data doesn't state a reason. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The BB equals the Valdoria country ceiling (A12), which fits a ceiling effect, but that is inference.

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44. The I05 downgrade (A29) is an instrument rating, not an issuer rating.

**Q8.** E08. It was rated RD from A22 (2026-07-08) with no later action.

**Q9.** 13. These are E01, E02 (same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. I excluded E07, whose rating was withdrawn (A19). I also excluded VD (country ceiling only) and E11 (type CO only).

**Q10.** Depends. Its LC rating is BBB- (investment grade, A13) and its FC rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action was in November 2025.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade; the Rating Watch (A35) and the affirmation (A33) are not.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 held A- (A26) until the downgrade on 2026-04-15. E17 "HALDEN BANK" shares E10's LEI and has no ratings of its own.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A36, A35, A33).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative with the rating kept at A- (A17).

**Q18.** E06 (A17). E14's earlier watch (A35) was followed by an affirmation (A33).

**Q19.** E01 (A03) and E09 (A25). Both are Negative outlooks that were not superseded.

**Q20.** No. Nothing shows default for E07; its rating was withdrawn for commercial reasons (A19).

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's action code "EX" (A47) isn't defined in the data, so I did not count it.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a country ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A). The ceilings come from A12 and A37.

**Q31.** No. No company's FC rating is above its ceiling. E15's LC rating of A+ is above it, but that is a local-currency rating.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The guarantor E10 (Halden Bank AG), rated BBB+ after the downgrade in A27.

**Q34.** No. The data has no parent link between E12 and E09/E10, only a similar name.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10, going by shared LEIs.

**Q38.** No. They have different LEIs and countries.

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E16's source system is "QA", so it may be a test record. Without it the count is 5.

**Q41.** BB+ (A44).

**Q42.** DE. E10 says DE. The duplicate record E17 says LU and comes from the RESEARCH source.

**Q43.** 0. The only LU record is E17, which is the same entity as E10 (DE). If you counted records, it would be 1.

**Q44.** Yes, most likely. XVD appears to be Valdoria's currency, and I07's BBB- matches E05's LC rating. The data doesn't define XVD explicitly.

**Q45.** No. The ceiling limits FC ratings, and this note is local-currency.

**Q46.** No. E11 only has a CO-type rating (A46); no issuer default rating is recorded.

**Q47.** None. I08's only record is an "EX" action at A (A47), and the data doesn't define EX. It could mean expired or expected, so I did not treat it as a held rating.

**Q48.** 7: I01 to I07.

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