**Q1.** A-. E01's rating was A- from A01 (2024-03-12) and was not changed until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is the affirmation A03 (BBB, outlook Negative), and neither of its instruments, I01 and I02, has a 2026 action.

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07 (2025-06-20).

**Q4.** Positive. E03 shares its LEI with E02, so I treated them as one entity. The latest action is A09 (2025-09-15, Positive), which supersedes A08 (Stable).

**Q5.** The guarantor E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02 (A08, A09).

**Q6.** The data states no reason. E05's foreign-currency rating is BB (A14) against BBB- local currency (A13). BB also equals the VD country-ceiling record (A12), so a ceiling effect is a plausible inference only.

**Q7.** E08, E10 and E16. Their 2026 downgrades are A21 and A22 (E08), A27 (E10) and A44 (E16). I05's downgrade (A29) is an instrument rating, so I did not count it.

**Q8.** E08. It was downgraded to RD in A22 (2026-07-08) and has no later action.

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), E11's CO rating is not an issuer rating, and VD has only a country ceiling.

**Q10.** Depends. Its foreign-currency rating is BB (non-investment grade) and its local-currency rating is BBB- (investment grade) (A14, A13).

**Q11.** BBB+. A36 (2024-09-30) was the latest action before that date.

**Q12.** A-, from A34.

**Q13.** Once, in A36. A35 is a watch and A33 an affirmation.

**Q14.** None. E12's first rating is A30 (2024-02-01).

**Q15.** A-. E10 was rated A- from A26 until the downgrade in A27 (2026-04-15). E17 shares E10's LEI and has no ratings.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ in A33, with only a watch (A35) in between.

**Q17.** No. E06 has only a Rating Watch Negative (A17). E13 (Orrin Bancorp) has a different LEI and no actions.

**Q18.** E06, from A17 (2026-09-03). E14's watch (A35) was resolved by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), and its last rating was BB, not default.

**Q21.** E07, because of the withdrawal in A19.

**Q22.** E08 (RD, A22).

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's A rating carries action EX (A47), which the data does not define; I treated it as ended.

**Q26.** A+, from A40 (E15 local currency).

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38 (CV foreign currency).

**Q29.** None. VD has only a country-ceiling record (A12, BB) and no issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB against VD's ceiling of BB (A14, A12). E15's is A against CV's ceiling of A (A41, A37).

**Q31.** No. No company's foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The guarantor E10 (Halden Bank AG), currently rated BBB+. I05 is issued by E11 and guaranteed by E10 (A27).

**Q34.** No. The data records no parent link between E12 and the E09/E10 group; only the name is similar.

**Q35.** 3: E09, E10 and E11. E17 shares E10's LEI, so it is a duplicate.

**Q36.** 2: E02 and E04. E03 duplicates E02 by LEI.

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and countries (E06 in DE, E13 in US).

**Q39.** A (A09 and A08).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because it was withdrawn.

**Q41.** BB+, from A44.

**Q42.** DE (E10). The duplicate record E17 says LU, so the data conflicts. I used the RATINGS-system record.

**Q43.** 0. The only LU record is E17, which duplicates E10 (domiciled in DE). Counting by record would give 1.

**Q44.** Yes, by inference. The note is in XVD and its BBB- matches E05's local-currency rating (A13). The data never states Valdoria's currency, though.

**Q45.** No. The ceiling applies to foreign-currency ratings, and the note is a local-currency obligation rated BBB- (A45), so it is not capped.

**Q46.** No. E11 has only a CO-type rating (A46), not a long-term or short-term issuer default rating. The meaning of CO is not defined.

**Q47.** None. I08's A rating carries action EX (A47, 2026-09-01), which I treated as ended.

**Q48.** 7: I01 to I07. I08 is excluded because of the EX action in A47.

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