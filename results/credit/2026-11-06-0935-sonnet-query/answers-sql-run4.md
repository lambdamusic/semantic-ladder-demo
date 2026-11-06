**Q1.** A-. The last action before that date was A01 (2024-03-12, A-), and the downgrade A02 only came on 2025-06-20.

**Q2.** No. A03 (2026-02-10) affirmed Kestrel at BBB and only moved the outlook to Negative. The downgrade A02 was in 2025.

**Q3.** No. The 2031 note (I02, subordinated) was cut to BB+ by A07, which is sub-investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) affirmed it at A with a POS outlook.

**Q5.** The risk is that of E02, rated A. I03 is issued by E04 but guaranteed by E02, and its rating is A (A11).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12). The foreign-currency rating is BB (A14) and the local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16. The downgrades are A21 and A22 for E08, A27 for E10 and A44 for E16. I05's downgrade (A29) is an instrument action, so E11 is not counted.

**Q8.** E08. A22 moved it to RD (restricted default) on 2026-07-08. E07 was only withdrawn (A19).

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07's rating is withdrawn, and E11 and VD have no LTIDR.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded it on 2024-09-30.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement.

**Q14.** None. The first Halden Foods rating is A30, on 2024-02-01.

**Q15.** A-, from A26. The downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ from 2024-09-30 and is still BBB+ (A33 affirmed it).

**Q17.** No. A17 only placed E06's A- rating on Rating Watch Negative.

**Q18.** E06, from A17. E14's watch (A35) was cleared by A33.

**Q19.** E01 (A03) and E09 (A25). E06 is on watch, with no outlook shown.

**Q20.** No. A19 withdrew the rating for commercial reasons, and no default rating appears for E07.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, via A22 (RD).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating ended with A47 (EX). The data does not define EX, so I read it as ending the rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** E15 and E05. E15's foreign-currency rating of A equals Corvenia's ceiling of A (A41, A37). E05's BB equals Valdoria's ceiling of BB (A14, A12).

**Q31.** No. E15 and E05 are at their ceilings, not above them.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The risk is that of E10, rated BBB+. I05 is guaranteed by E10, and the rating is BBB+ after A27/A29.

**Q34.** No. E12 has no parent link to E09 or E10, and the similar name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. Of the 19 rows, E03 duplicates E02 and E17 duplicates E10, going by the shared LEIs.

**Q38.** No. They have different LEIs and countries, and neither is the other's parent.

**Q39.** A, from A08 and the A09 affirmation under the same LEI.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07's rating is withdrawn.

**Q41.** BB+ (A44). The entity's source system is QA, which may mean it is a test record.

**Q42.** DE, per E10. The duplicate E17 says LU, which conflicts with E10.

**Q43.** 0. The only LU row is E17, a duplicate of E10, which is domiciled in DE. This one is uncertain because of the conflict.

**Q44.** Yes. I07 is in XVD, which appears to be Valdoria's currency, and its BBB- matches the local-currency rating.

**Q45.** No. The ceiling applies to foreign-currency obligations, and this is a local-currency note.

**Q46.** No. E11 has only a credit opinion (A46) and an instrument rating, not an issuer rating.

**Q47.** None. A47 (EX, 2026-09-01) ended the rating, which was A before. This assumes EX means the rating ended.

**Q48.** 7. This is I01 to I07; I08 is excluded because of A47.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
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