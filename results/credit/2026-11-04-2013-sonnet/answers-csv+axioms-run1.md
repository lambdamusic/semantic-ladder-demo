**Q1.** A-. A01 (assigned 2024-03-12) was the rating in force until A02 on 2025-06-20.

**Q2.** No. The only 2026 Kestrel action on the issuer is A03, an affirmation at BBB.

**Q3.** No, it is BB+. I02 was downgraded to BB+ by A07, which superseded the BBB of A23.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its A09 (2025-09-15, POS) supersedes A08.

**Q5.** The holder takes the risk of E02 (Northwind Holdings), the guarantor of I03, which is rated A. A09 gives the A rating via E03, and I03 itself is also rated A (A11).

**Q6.** The foreign-currency rating is capped by the Valdoria Country Ceiling of BB (A12). A14 (FC, BB) sits at that ceiling, while A13 (LC, BBB-) is above it.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is on a QA test record, and I05's (A29) is on an instrument.

**Q8.** E08. A22 (RD, 2026-07-08) is still in force.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15 and CV. E07 is withdrawn (A19), E16 is a QA record, and VD has only a ceiling.

**Q10.** Depends. The local-currency rating is BBB- (A13, investment grade), but the foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. A36 (2024-09-30) was in force on that date.

**Q12.** A-. A34 (2023-01-15) was in force until A36.

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 stood until A27 on 2026-04-15, and the research duplicate E17 adds no actions.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). A35 only placed it on watch.

**Q17.** No. A17 is a Rating Watch placement at unchanged A-, not a downgrade.

**Q18.** E06. A17 carries RWN. E14's A35 watch was superseded by A33.

**Q19.** E01 and E09 (A03, A25). E06's latest action, A17, carries no outlook.

**Q20.** No. E07's rating was withdrawn (A19), and it never had a default rating.

**Q21.** E07. Its rating was withdrawn by A19.

**Q22.** E08. It reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05 is FC BB against a VD ceiling of BB, and E15 is FC A against a CV ceiling of A.

**Q31.** No. E05 and E15 are exactly at their ceilings, and no other company has a ceiling to compare against.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the risk of E10 (Halden Bank), the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. E12 has no parent and no link to the E09 group.

**Q35.** 3. These are E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2. These are E02 and E04. E03 is a duplicate of E02.

**Q37.** 16. There are 19 records, less two duplicates (E03, E17) and the QA test record E16.

**Q38.** No. They have different LEIs, countries and records, and nothing links them.

**Q39.** A (A09).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E10 is domiciled in LU (research record E17), and E07 and E16 do not count.

**Q41.** None. E16 is a QA test record, so its actions are not ratings in force.

**Q42.** LU. The RESEARCH record E17 sets the domicile for E10.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, which is Valdoria's domestic currency.

**Q45.** No. The ceiling (BB, A12) caps foreign-currency ratings, and I07 is a local-currency instrument. Its BBB- (A45) is therefore not tested against it.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX, A), which is not a rating in force.

**Q48.** 7. These are I01 to I07. I08 has only an expected rating.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
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
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```