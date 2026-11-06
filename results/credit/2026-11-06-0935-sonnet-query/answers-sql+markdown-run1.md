**Q1.** A-. E01's rating was set at A- by A01 and stayed there until the downgrade A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04, and A03 only moved the outlook to NEG.

**Q3.** No, it is BB+. I02 was downgraded to BB+ by A07, which is speculative grade.

**Q4.** POS. E02 and E03 share an LEI, so they are one entity. The latest action is A09 on E03, which gives POS.

**Q5.** The holder takes Northwind Holdings' credit risk (E02, with E03 as the same entity), rated A. I03 is guaranteed by E02, and the latest issuer rating (A09 on E03) is A.

**Q6.** The foreign-currency rating is capped by the Valdoria Country Ceiling. VD's ceiling is BB (A12), and E05's FC rating is BB (A14) against an LC rating of BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. E16 is QA test data and is ignored.

**Q8.** E08. It went to RD on 2026-07-08 (A22), and RD counts as default.

**Q9.** 12. These are E01, E02/E03, E05, E06, E08, E09, E10/E17, E12, E13, E14, E15 and CV. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. Its LC rating is BBB- (investment grade), but its FC rating is BB (speculative).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the later actions A35 and A33 kept it at BBB+.

**Q12.** A-, from A34.

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating, A30, came on 2024-02-01.

**Q15.** A-. The E10 downgrade A27 did not happen until 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+.

**Q17.** No. E06's only 2026 action is the Rating Watch A17, which does not change the rating.

**Q18.** E06, from A17. E14's earlier watch (A35) was cleared by A33.

**Q19.** E01 (A03) and E09 (A25). E06's outlook is blank on its watch action, so I have not counted it.

**Q20.** No. E07's rating was withdrawn (A19), which is not a default, and its last rating was BB.

**Q21.** E07. Its LTIDR was withdrawn by A19.

**Q22.** E08, which reached RD (A22).

**Q23.** F2, from A04.

**Q24.** Yes. It is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42 on I06.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's FC rating is A, equal to the CV ceiling of A.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. The chain runs E11 to E10 to E09.

**Q33.** The holder takes Halden Bank's credit risk (E10), rated BBB+. I05 is guaranteed by E10, and A27 set E10 at BBB+.

**Q34.** No. E12 has no parent and is not in E09's chain.

**Q35.** 3. These are E09, E10 (with E17 as the same entity by LEI) and E11.

**Q36.** 2. These are E02 (with E03 as the same entity) and E04.

**Q37.** 16. That is 19 records, less the duplicates E03 and E17 and the QA record E16.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, from A09.

**Q40.** 5. These are E01, E02/E03, E09, E12 and E14.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile.

**Q43.** 1. That is Halden Bank, E10/E17.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. The note is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.

**Q48.** 7. These are I01 to I07, and I08 is excluded.

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