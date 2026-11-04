**Q1.** A-. A01 (2024-03-12) set A-, and the next LTIDR FC action, A02, only came on 2025-06-20.

**Q2.** No. The only 2026 Kestrel action on the issuer is A03, an affirmation (the outlook moved to NEG).

**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk, and A09 affirmed E02 at A.

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings. The local-currency rating, BBB- (A13), is not capped, while the FC rating is held at BB (A14).

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A44 (E16) is QA data and is ignored, and A29 is an instrument action.

**Q8.** E08. A22 downgraded it to RD on 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 was withdrawn. VD has only a ceiling, E11 only a credit opinion, and E04 and E16 have no issuer rating.

**Q10.** Depends. FC is BB (speculative) and LC is BBB- (investment grade), per A13 and A14.

**Q11.** BBB+ (A36, a downgrade on 2024-09-30).

**Q12.** A- (A34).

**Q13.** 1. Only A36 is a downgrade. A35 is a watch and A33 an affirmation.

**Q14.** None. E12's first rating, A30, came on 2024-02-01.

**Q15.** A-. E10's rating was A- from A26 until the downgrade A27 on 2026-04-15.

**Q16.** No. It was BBB+ throughout, since A35 and A33 did not change it.

**Q17.** No. A17 is only a Rating Watch and leaves the rating at A-.

**Q18.** E06 (A17, 2026-09-03). E14's watch (A35) was superseded by the affirmation A33, which carries no watch.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only an expected rating (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The Country Ceiling A37 is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC is BB, equal to the VD ceiling of BB, and E15's FC is A, equal to the CV ceiling of A (A41 and A37).

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ after A27.

**Q34.** No. E12 has no parent and a different LEI, so it is not in the E09 group.

**Q35.** 3. The group is E09, E10 and E11, and E17 duplicates E10.

**Q36.** 2. The group is E02 and E04, and E03 duplicates E02.

**Q37.** 16. There are 19 records, minus the duplicates E03 and E17 and the QA record E16.

**Q38.** No. Their LEIs differ (E06 and E13).

**Q39.** A (A09, via E03, which is the same entity as E02).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17 (LU).

**Q43.** 0. The only LU record is E17, and the RATINGS record for that entity says DE.

**Q44.** Yes. I07 pays in XVD, Valdoria's domestic currency.

**Q45.** No. The ceiling caps only foreign-currency ratings, and I07 is local-currency debt.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is an expected rating (EX) only.

**Q48.** 7. These are I01 to I07, and I08 is unrated.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```