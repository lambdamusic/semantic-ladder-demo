**Q1.** A-. A01 assigned A- in March 2024, and the downgrade to BBB (A02) only came on 2025-06-20.

**Q2.** No. The only 2026 Kestrel action on its issuer rating is an affirmation at BBB (A03).

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07, which supersedes A23 (BBB).

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) affirmed A with a POS outlook, superseding A08.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and A09 (recorded under E03) is E02's current rating.

**Q6.** The Country Ceiling for Valdoria is BB (A12), and it caps foreign-currency ratings, so the FC rating is BB (A14) while the LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is excluded because E16 is a QA test record.

**Q8.** E08. A22 gave it RD on 2026-07-08, and nothing later supersedes it.

**Q9.** 12. These are E01, E02 (=E03), E05, E06, E08, E09, E10 (=E17), E12, E13, E14, CV and E15. E07 is withdrawn (A19), E16 is a test record, and E04, E11 and VD have no issuer rating.

**Q10.** Depends. Valdoria Telecom's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and A35 (the watch) came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 applies until A27 (2026-04-15), which falls after 2026-01-01.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. A17 is a Rating Watch placement that keeps the rating at A-.

**Q18.** E06 (A17). E14's watch (A35) was superseded by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam was withdrawn (A19), not rated RD or D.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals Valdoria's BB ceiling (A12, A14), and E15's A equals Corvenia's A ceiling (A37, A41).

**Q31.** No. E05 sits at the ceiling and E15 sits at the ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. E10 guarantees I05, and A27 is E10's current rating.

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3, which are E09, E10 (=E17) and E11.

**Q36.** 2, which are E02 (=E03) and E04.

**Q37.** 16. The 19 records collapse to 17 after merging E03 into E02 and E17 into E10, and E16 is a test record, so it is not a legal entity.

**Q38.** No. They have different LEIs and different countries, with no link between them.

**Q39.** A (A09, for the same entity).

**Q40.** 5. These are E01, E02 (=E03, GB), E09, E12 and E14.

**Q41.** None. E16 is a QA test record, so its actions are not treated as ratings in force.

**Q42.** LU. The RESEARCH record E17 says LU and takes precedence for domicile (E10 is merged with it by LEI).

**Q43.** 1, which is E10 (=E17).

**Q44.** Yes. I07 is in XVD, which is the domestic currency of VD, E05's domicile.

**Q45.** No. The ceiling applies to foreign-currency ratings and I07 is a local-currency note, so the BB ceiling does not constrain its BBB- rating (A45).

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (A), not a rating in force.

**Q48.** 7. These are I01 to I07, and I08 is only an expected rating.

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