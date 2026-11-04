**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03/A04, an affirmation (AF), and the negative outlook is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), and its latest action is A07 (DG, BB+, 2025-06-20).

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and A09 (2025-09-15) is the latest action with outlook POS.

**Q5.** The holder takes E02's credit risk (Northwind Holdings), rated A. I03 is guaranteed by E02, and the combined E02/E03 record has latest LTIDR A (A09).

**Q6.** The data doesn't give a reason, but it is consistent with the Country Ceiling. E05's FC rating is BB (A14), its LC rating is BBB- (A13), and Valdoria's ceiling is BB (A12). The ceiling caps FC ratings only.

**Q7.** E08 and E10. The 2026 downgrades (DG) are A21 and A22 for E08 and A27 for E10 (E17 is the same entity). A44 is a QA record and is ignored. A29 is an instrument downgrade, not an issuer one.

**Q8.** E08, which has been RD since A22 (2026-07-08).

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15 and CV. E07 was withdrawn (A19), and VD has only a ceiling.

**Q10.** Depends. E05 is BB on the FC basis (speculative) and BBB- on the LC basis (investment grade).

**Q11.** BBB+, from A36 (DG, 2024-09-30). The RW in A35 came later.

**Q12.** A-, from A34.

**Q13.** 1, from A36. A35 is a Watch and A33 an affirmation.

**Q14.** None. E12's first rating is A30 (2024-02-01).

**Q15.** A-. E10 held A- from A26 until the downgrade in A27 on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). The Watch in A35 did not change it.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17). E14's Watch (A35) was superseded by A33, which carries no watch.

**Q19.** E01 (A03) and E09 (A25). E06's Watch action (A17) records no outlook, so I excluded it.

**Q20.** No. E07 was withdrawn (A19, WD), which is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08 (RD in A22).

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only expected (EX).

**Q26.** A+ (A40, LC basis).

**Q27.** A- (A42).

**Q28.** BBB+ (A38, FC basis). A37 is the ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. VD's ceiling is BB and E05's FC rating is BB (A14). CV's ceiling is A and E15's FC rating is A (A41).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes E10's credit risk (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest rating is A27 (BBB+).

**Q34.** No. E12 has no parent link to E09, and sharing the "Halden" name proves nothing.

**Q35.** 3: E09, E10 (same entity as E17) and E11.

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** 16. There are 19 records. E03 duplicates E02 and E17 duplicates E10, which leaves 17. E16 is a QA record and is ignored.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02 (with E03), E09, E12 and E14. E07 is withdrawn and E16 is a QA record.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. RATINGS (E10) overrides the research duplicate (E17), which has LU.

**Q43.** 0. The only LU record is E17, a duplicate of E10, and RATINGS records E10 as DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), but local-currency debt isn't capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX), so I08 is unrated.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```