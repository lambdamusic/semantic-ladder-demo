**Q1.** A-. Kestrel Energy's issuer rating on 1 Jan 2025 was A- (A01, valid 2024-03-12 to 2025-06-20).

**Q2.** No. The 2026-02-10 action (A03) affirmed BBB and only moved the outlook to Negative.

**Q3.** No. The 2031 note (I02) is BB+ (A07), below investment grade.

**Q4.** Positive. Northwind Holdings (E02, the same entity as E03) has an A rating with a Positive outlook (A09).

**Q5.** E02, rated A. The Northwind Finance 2030 note (I03) is guaranteed by E02, and I03 is rated A (A11).

**Q6.** Valdoria Telecom's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB equals the Republic of Valdoria's Country Ceiling (A12), so the foreign-currency rating appears capped at the ceiling. The data does not state the reason explicitly.

**Q7.** E08, E10 and E16. Their issuer ratings were downgraded in 2026 (A21/A22, A27, A44). I did not count the I05 downgrade (A29), because it is an instrument rating.

**Q8.** E08. It was rated RD on 1 Oct 2026 (A22).

**Q9.** 13. These are E01, E02/E03, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. VD has only a Country Ceiling, and E07's rating was withdrawn. E16 is included even though A44 lacks the in-force flag; it has no end date and nothing replaces it.

**Q10.** Depends. The local-currency rating is BBB- (investment grade) and the foreign-currency rating is BB (not).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A36 on 2024-09-30.

**Q14.** None. Halden Foods' first rating was dated 2024-02-01 (A30).

**Q15.** A-. Halden Bank (E10) held A- until 2026-04-15 (A26).

**Q16.** No. Marlow was BBB+ on 1 Jan 2025 and is BBB+ now; only the Watch and outlook changed.

**Q17.** No. Orrin Bank's A- was kept and placed on Rating Watch Negative (A17).

**Q18.** E06.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. Pellam Retail's rating was withdrawn (A19), not defaulted.

**Q21.** E07.

**Q22.** E08.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01, I03, I05, I06 and I07.

**Q26.** A+ (A40).

**Q27.** A- (A42, instrument I06).

**Q28.** BBB+ (A38).

**Q29.** None. The Republic of Valdoria has only a Country Ceiling of BB (A12), no issuer rating.

**Q30.** E05 and E15. E05 is BB against Valdoria's BB ceiling, and E15 is A against Corvenia's A ceiling.

**Q31.** No.

**Q32.** E09.

**Q33.** E10, rated BBB+. The Halden Leasing 2028 note (I05) is guaranteed by E10 and rated BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no ownership link to the Halden group; it is its own ultimate parent.

**Q35.** 3. The group is E09, E10 and E11, with E17 being the same entity as E10.

**Q36.** 2. The group is E02 (the same entity as E03) and E04.

**Q37.** 17. There are 19 records, with E03 duplicating E02 and E17 duplicating E10.

**Q38.** No. The data has no sameEntityAs link between E06 and E13.

**Q39.** A (A09).

**Q40.** 6. These are E01, E02, E09, E12, E14 and E16, counting E02 and E03 as one entity.

**Q41.** BB+ (A44). The record is not flagged as in force, but it has no end date and nothing supersedes it.

**Q42.** LU. Halden Bank's country is DE, but its derived domicile is LU.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, Valdoria's domestic currency, and is marked as local currency.

**Q45.** No. The BB ceiling applies to foreign-currency ratings, and I07 is local currency (BBB-).

**Q46.** No. E11 has only a counterparty-obligation rating (A46), which is not an issuer rating, and it is not in force.

**Q47.** None. The 2034 note (I08) had its A rating expired (A47, action EX) on 2026-09-01.

**Q48.** 7. Instruments I01 to I07 held an in-force rating; I08's had expired.

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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```