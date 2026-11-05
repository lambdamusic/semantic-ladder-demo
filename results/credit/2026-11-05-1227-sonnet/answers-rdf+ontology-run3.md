**Q1.** A-. E01's long-term FC rating was set at A- by A01 (2024-03-12) and not changed until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is the affirmation A03 (BBB, outlook to Negative), and an affirmation or outlook change is not a downgrade.

**Q3.** No. I02 (2031 subordinated note) was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E02 and E03 share the LEI 213800PHEIYNJMHTDV74, so they are one entity. The latest action is A09 (2025-09-15), which affirmed A with a Positive outlook.

**Q5.** E02, rated A. I03 is guaranteed by E02 (the issuer E04 is a finance subsidiary), so the holder takes the parent's risk, and E02/E03's latest rating is A (A09).

**Q6.** The Country Ceiling for VD is BB (A12), which caps E05's FC rating (A14, BB). The LC rating (A13, BBB-) is not capped. The data doesn't state the reason explicitly, so this is inferred from the ceiling definition.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 (same LEI as E17) by A27. A44 is a QA record and is ignored, and the instrument downgrades (e.g. A29) are not issuer downgrades.

**Q8.** E08. It was in default (RD) from A22 (2026-07-08).

**Q9.** 12. These are E01, E02 (=E03), E05, E06, E08, E09, E10 (=E17), E12, E13, E14, CV and E15. E07 was withdrawn (A19). E16 is QA. VD has only a ceiling, and E04 and E11 have no issuer rating (E11 has only a credit opinion).

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13) but its FC rating is BB (speculative, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded it, and the next action is A35 (a Watch, rating unchanged).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade for E14. The Watch (A35) and the affirmation (A33) are not.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10/E17 held A- (A26) until the downgrade A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and still is (A33).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which leaves the rating unchanged.

**Q18.** E06. A17 (2026-09-03) is its latest action and carries the Watch Negative. E14's Watch (A35) was superseded by A33.

**Q19.** E01 and E09, from A03 and A25 respectively.

**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn by A19, so it has no issuer rating of that type.

**Q22.** E08, which reached RD (a default) in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's current long-term rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) were investment grade. I02 (BB+) and I04 (BB) were not, and I08 has only an expected rating.

**Q26.** A+. E15's LC rating is set by A40.

**Q27.** A-, from A42 (I06).

**Q28.** BBB+. CV's FC long-term rating is A38. A39 (A-) is the LC rating and A37 (A) is the Country Ceiling.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB (A14, A12). E15's FC rating is A, equal to the CV ceiling of A (A41, A37).

**Q31.** No. No FC rating exceeds its country's ceiling; E15's LC rating of A+ is not capped.

**Q32.** E09. E11's parent is E10, whose parent is E09, which has none.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ after A27.

**Q34.** No. E12 has no parent link, while E10 sits under E09.

**Q35.** 3: E09, E10 (=E17) and E11.

**Q36.** 2: E02 (=E03) and E04.

**Q37.** 16. There are 19 records, but E03 duplicates E02 and E17 duplicates E10, and E16 is QA test data.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, per A09 on E03 (the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. E17 (RESEARCH) holds for domicile and shares its LEI with E10.

**Q43.** 1: E17/E10 is the only entity domiciled in LU.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. The note is local-currency debt, so the ceiling doesn't cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7: I01 to I07.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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