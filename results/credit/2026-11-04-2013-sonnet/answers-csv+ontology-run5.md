**Q1.** A-. A01 (2024-03-12) set A-, and the next action on E01 LTIDR FC, A02, came on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04), which are not downgrades.

**Q3.** No, it is BB+. I02 is subordinated, and its latest rating is A07 (2025-06-20), BB+, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) gives POS.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, so it follows E02's issuer rating, which is A after A09 (via E03, the same LEI).

**Q6.** Valdoria's Country Ceiling (A12) is BB. The FC rating (A14, BB) is capped at that ceiling, while the LC rating (A13, BBB-) is not.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and A44 is on QA record E16, which is ignored.

**Q8.** E08. A22 (2026-07-08) moved it to RD, which is a default.

**Q9.** 12. The issuers with an issuer rating are E01, E02 (E03 is the same entity), E05, E06, E08 (RD), E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, E11 has only a credit opinion, and VD has only a ceiling.

**Q10.** Depends. The FC rating is BB (speculative; A14), while the LC rating is BBB- (investment grade; A13). The FC rating is the headline one.

**Q11.** BBB+. A36 (2024-09-30) lowered it to BBB+, and A35 (2025-11-20) came after 1 June 2025.

**Q12.** A-. A34 (2023-01-15) set A-, and the downgrade A36 came later.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. A26 set A- for E10 (same entity as E17), and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. A17 is a Rating Watch action with the rating unchanged at A-.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's watch (A35) ended when A33 affirmed it without a watch.

**Q19.** E01 and E09. Their latest actions carry NEG outlooks (A03 and A25).

**Q20.** No. A19 withdrew E07's rating, which is not a credit event, and its last rating was BB.

**Q21.** E07. It had a rating that A19 withdrew.

**Q22.** E08. Its RD in A22 is a default, and no other entity has RD or D.

**Q23.** F2, from A04.

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A, via the guarantor), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only expected (EX), so it is unrated.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. A37 is the Country Ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB (A14, A12), and E15's FC rating of A equals the CV ceiling of A (A41, A37).

**Q31.** No. E05 and E15 are exactly at their ceilings, and no other company has a country with a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose latest LTIDR is A27 (BBB+).

**Q34.** No. E12 has no parent link, so it is not in E09's group.

**Q35.** 3: E09, E10 (E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records, minus the duplicates E03 and E17 and the QA record E16.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09 (E03, same entity).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, and E10 is domiciled in LU, since RESEARCH holds for domicile.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile.

**Q43.** 1, which is E10 (E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, the issuer's country.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7, which is I01 to I07.

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