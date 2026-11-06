**Q1.** A-. Kestrel's rating was A- from A01 (2024-03-12) until the downgrade to BBB in A02 on 2025-06-20.

**Q2.** No. In 2026, A03 affirmed BBB and moved the outlook to Negative, with no rating cut.

**Q3.** No. The 2031 note (I02) is rated BB+ after A07, which is below investment grade.

**Q4.** Positive. E02 and E03 share an LEI, so I treated them as one entity. Its latest action, A09 (2025-09-15), has a POS outlook.

**Q5.** The holder takes the credit risk of E02, the guarantor of I03, and the note is rated A (A10, A11).

**Q6.** The Valdoria country ceiling (A12) is BB. That caps Valdoria Telecom's foreign-currency rating at BB (A14), while its local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16. They were downgraded in A21 and A22, A27, and A44 respectively. I05's downgrade (A29) is an instrument action only, driven by guarantor E10.

**Q8.** E08. A22 on 2026-07-08 set it to RD, and nothing later changes that.

**Q9.** 13. These are CV, E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and E16. E07 is withdrawn, E11 has only a "CO" record, and VD has only a country ceiling.

**Q10.** Depends. The foreign-currency rating is BB (not investment grade) and the local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded E14 from A- on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1. Marlow has one downgrade, A36. A35 and A33 are watch and affirmation actions.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10 held A- from A26 until the downgrade on 2026-04-15, and E17 is a duplicate of E10.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33). Only the watch and outlook changed.

**Q17.** No. A17 (2026-09-03) only placed it on Rating Watch Negative at A-.

**Q18.** E06, from A17. E14's watch (A35) was resolved by A33.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. A19 withdrew the rating for commercial reasons, and the last rating before that was BB.

**Q21.** E07, because of the withdrawal in A19.

**Q22.** E08, from the RD rating in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08 is excluded, as explained under Q47.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals the Valdoria ceiling of BB, and E15's A equals the Corvenia ceiling of A.

**Q31.** No. None is above its ceiling.

**Q32.** E09, via E11 → E10 → E09.

**Q33.** The holder takes the risk of E10, the guarantor, and the note is rated BBB+ (A29).

**Q34.** No. E12 has no parent link to E09 or E10, and the shared "Halden" name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 (same LEI).

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. The 19 rows contain two duplicates, E03 (of E02) and E17 (of E10), identified by shared LEIs.

**Q38.** No. They have different LEIs (E06 and E13), different countries and different entity records.

**Q39.** A. E02 was assigned A in A08 and affirmed at A via E03 in A09.

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+, from A44. The entity's source system is "QA", so this may be test data.

**Q42.** DE. The LU value comes only from the duplicate research row E17.

**Q43.** 0. The only LU record is E17, which duplicates the German E10.

**Q44.** Yes. I07 is denominated in XVD, Valdoria's currency.

**Q45.** No. The ceiling caps foreign-currency ratings, and I07 is local-currency (BBB-).

**Q46.** No. E11 has only a "CO" record (A46), not an issuer rating (LTIDR).

**Q47.** None. The only action on I08 is A47 with code "EX", which the data does not define. I read it as an expected or provisional rating (A), not a held rating, so this answer rests on that reading.

**Q48.** 7: I01 to I07. This also excludes I08 for the reason given under Q47.

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