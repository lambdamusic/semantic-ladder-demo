**Q1.** A-. A01 (2024-03-12) was still in force on 1 Jan 2025, because A02 only came on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is an affirmation (A03, BBB). The downgrade was A02 in 2025.

**Q3.** No, it is BB+. I02 was downgraded to BB+ by A07 and nothing has changed it since.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15, POS) supersedes A08.

**Q5.** The credit risk is E02's, rated A. I03 is guaranteed by E02, and the current rating is A09 (recorded under E03, the same entity).

**Q6.** The data does not state a reason. It is consistent with a country ceiling: the Valdoria ceiling is BB (A12), and the foreign-currency rating is BB (A14). The local-currency rating is BBB- (A13), which is higher.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 is an instrument and E16 is a QA test record, so neither counts.

**Q8.** E08. A22 gave it RD on 2026-07-08 and it is still in force.

**Q9.** 12. These are E01, E02/E03 (counted once), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) was in force on 1 Jun 2025.

**Q12.** A-. A34 (2023-01-15) was in force on 1 Jan 2024.

**Q13.** 1. Only A36 is a downgrade; A33 is an affirmation and A35 is a watch placement.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 (E10) was in force until A27 on 2026-04-15, and E17 is the same entity.

**Q16.** No. It was BBB+ on 1 Jan 2025 (A36) and is BBB+ now (A33 affirmed it). The only action in between was a watch placement, A35.

**Q17.** No. A17 is a placement on Rating Watch with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch, A35, was superseded by A33.

**Q19.** E01 (A03) and E09 (A25). A17 gives E06 no outlook.

**Q20.** No. A19 withdrew the E07 rating, and its last rating was BB, not a default rating.

**Q21.** E07. Its rating was withdrawn by A19.

**Q22.** E08. A22 gave it RD, and no other record carries RD or D.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05 is BB against the VD ceiling of BB, and E15 is A against the CV ceiling of A.

**Q31.** No. Both E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11's parent is E10 and E10's parent is E09, per the RATINGS records.

**Q33.** The credit risk is E10's, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent and no link to E09, E10 or E11.

**Q35.** 3. These are E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2. These are E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates by LEI, and E16 is a QA test record, not a legal entity.

**Q38.** No. They have different LEIs and no link between them.

**Q39.** A (A09).

**Q40.** 5. These are E01, E02/E03, E09, E12 and E14. E10 is domiciled in LU, not GB.

**Q41.** None. E16 is a QA test record, so its actions are not counted as ratings in force.

**Q42.** LU. The RESEARCH record E17 gives the country, and E17 is the same entity as E10.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is denominated in XVD, which is Valdoria's domestic currency.

**Q45.** No. The BB ceiling (A12) limits foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is an expected rating, which is not a rating in force.

**Q48.** 7. These are I01 to I07; I08 has only an expected rating.

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