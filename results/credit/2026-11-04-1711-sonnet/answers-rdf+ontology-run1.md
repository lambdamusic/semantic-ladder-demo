**Q1.** A-. E01's foreign-currency long-term rating was set to A- by A01 (2024-03-12). It did not change until A02 in 2025-06.

**Q2.** No. E01's only 2026 action is A03, an affirmation (BBB, outlook Negative), which is not a downgrade.

**Q3.** No. The 2031 note (I02) was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), has a Positive outlook. That supersedes the Stable outlook in A08.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes E02's credit risk (A09, A).

**Q6.** Its foreign-currency rating is capped by the Country Ceiling for VD. E05 is domiciled in VD, whose ceiling is BB (A12). The foreign-currency rating is BB (A14) and the local-currency rating is BBB- (A13), which is not capped.

**Q7.** E08 and E10 were downgraded in 2026 (A21, A22, A27). A44 is on E16, a QA record, so it is ignored. A29 is an instrument downgrade, not an issuer downgrade.

**Q8.** E08. A22 moved it to RD, a default, on 2026-07-08.

**Q9.** 12. The issuers holding a rating are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. E05's foreign-currency rating is BB (speculative grade), and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action, A35, is only a Watch.

**Q12.** A-. A34 assigned A- on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating was A30 on 2024-02-01.

**Q15.** A-. E10 held A- from A26 until the downgrade A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is A17, a Watch with the rating unchanged. E13 (Orrin Bancorp) is a different entity because its LEI differs.

**Q18.** E06. A17 (2026-09-03) placed it on Rating Watch Negative. E14's Watch from A35 ended with the later affirmation A33, which carries no watch.

**Q19.** E01 and E09 (A03 and A25).

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), and a withdrawal is not a default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40, local-currency basis).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The CV record's A in A37 is the Country Ceiling, not its rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** E05 and E15. The VD ceiling is BB (A12) and E05's foreign-currency rating is BB (A14). The CV ceiling is A (A37) and E15's foreign-currency rating is A (A41).

**Q31.** No. No foreign-currency rating exceeds its ceiling. The higher E15 A+ (A40) is local-currency, so it is not capped.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, so it carries E10's credit risk. E10's rating is BBB+ after A27, and I05 is also BBB+ (A29).

**Q34.** No, as far as the data shows. E12 has no parent link to E09 or E10, and sharing the "Halden" name is not evidence.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. The data has 19 entity records. E03 duplicates E02 and E17 duplicates E10, which leaves 17. E16 is a QA record and is excluded, which leaves 16.

**Q38.** No. Their LEIs differ (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A. E02 and E03 are the same entity, and A09 affirmed A on 2025-09-15.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. RATINGS is the system of record, and its E10 record says DE. The LU country on E17 is a research-system disagreement.

**Q43.** 0. The only LU record is E17, which is E10, domiciled in DE.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. The ceiling does not cap local-currency debt, so I07's BBB- (A45) is not above what the ceiling allows.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX), so I08 remains unrated.

**Q48.** 7: I01 to I07. I08 is unrated.

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