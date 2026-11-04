**Q1.** A-. A01 (2024-03-12, LTIDR FC) was the latest action before 2025-01-01. The June 2025 downgrade (A02) came later.

**Q2.** No. The 2026 actions for E01 (A03, A04) are affirmations. The downgrade was A02 in 2025.

**Q3.** No, BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so I treat them as one entity. The latest action is A09 (2025-09-15) with a Positive outlook.

**Q5.** The holder takes E02's risk, rated A. I03 is issued by E04 and guaranteed by E02. I03 itself is rated A (A11), and E03/E02 is also A (A09).

**Q6.** The data gives no explicit reason. E05's local-currency rating is BBB- (A13) and its foreign-currency rating is BB (A14). The BB matches Valdoria's country ceiling (VD, A12), which is consistent with a ceiling cap, but that is an inference.

**Q7.** E08, E10 and E16. These were downgraded in A21/A22, A27 and A44. I05's downgrade (A29) is on an instrument, not an issuer.

**Q8.** E08. It was rated RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19). VD has only a country ceiling (A12). E11 has only a CO-type rating (A46), which I did not count as an issuer rating.

**Q10.** Depends. Its local-currency rating is BBB-, which is investment grade (A13). Its foreign-currency rating is BB, which is not (A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action is 2025-11-20 (A35).

**Q12.** A-. This is A34 (2023-01-15).

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating is A30 (2024-02-01).

**Q15.** A-. E10 held A- (A26) until the downgrade on 2026-04-15 (A27). E17 "HALDEN BANK" has the same LEI and no ratings.

**Q16.** No. The rating was BBB+ on 2025-01-01. The later actions, A35 (RW) and A33 (AF), are both BBB+.

**Q17.** No. E06's only 2026 action is A17, which places it on Watch Negative with the rating unchanged at A-. E13 is a different entity.

**Q18.** E06. The watch started with A17 (2026-09-03). E14's watch (A35) was resolved by the affirmation A33.

**Q19.** E01 and E09. Their latest outlooks are Negative (A03 and A25). E06's watch (A17) is the latest action there, so I treat it as superseding its earlier Stable outlook.

**Q20.** No. E07 was withdrawn for commercial reasons (A19), not defaulted.

**Q21.** E07. It was rated BB (A18) and then withdrawn (A19).

**Q22.** E08. It was rated RD in A22.

**Q23.** F2. This is A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's action is "EX", which the data does not define. I treated it as not a held rating.

**Q26.** A+. This is A40.

**Q27.** A-. This is A42.

**Q28.** BBB+. This is A38. A37 (A) is the country ceiling and A39 (A-) is the local-currency rating.

**Q29.** None. VD only has a country ceiling of BB (A12).

**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to the Valdoria ceiling of BB (A14, A12). E15's foreign-currency rating is A, equal to the Corvenia ceiling of A (A41, A37).

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes E10's risk, rated BBB+. E10 guarantees I05, and E10 was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. The recorded hierarchy puts E12 outside Halden Bank's group (E09, E10, E11). Only the shared name suggests otherwise.

**Q35.** 3. These are E09, E10 and E11. E17 is a duplicate of E10, with the same LEI.

**Q36.** 2. These are E02 and E04. E03 is a duplicate of E02, with the same LEI.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10 by LEI.

**Q38.** No. They have different LEIs and different countries (DE and US).

**Q39.** A. This is A09 on E03, which is the same entity as E02 by LEI.

**Q40.** 6. These are E01, E02 (E03), E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+. This is A44. E16's source system is "QA", so it may be test data.

**Q42.** DE. E10 is recorded as DE. The duplicate E17 says LU, but its LEI ends in "DE62", the same as E10's.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE) by LEI. If E17 were counted as separate, the answer would be 1.

**Q44.** Yes, by inference. I07 is denominated in XVD, which appears to be Valdoria's currency, and its BBB- rating matches E05's local-currency rating. The data does not say explicitly that XVD is Valdoria's currency.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 only has a CO-type rating (A46), not an issuer rating (LTIDR). The data does not define CO.

**Q47.** None. I08's only action is "EX" (A47), which the data does not define, and I did not treat it as a held rating.

**Q48.** 7. These are I01 to I07. I08 is excluded for the same reason as in Q47.

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