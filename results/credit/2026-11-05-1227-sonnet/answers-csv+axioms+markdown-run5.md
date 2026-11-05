**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01), and nothing changed it until 2025-06-20.

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03/A04), and the downgrade to BBB was in 2025 (A02).

**Q3.** No. I02 is rated BB+ after the downgrade A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 on 2025-09-15, shows POS.

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk. E02's current LTIDR FC is A (A08, affirmed by A09).

**Q6.** The foreign-currency rating is held to the Country Ceiling. E05's FC rating is BB (A14), against BBB- local-currency (A13), and Valdoria's ceiling is BB (A12).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27 (E17 is the same entity as E10). A29 is an instrument action, and A44 is on a QA record, which is ignored.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), which counts as default.

**Q9.** 12. The issuers are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is a QA record.

**Q10.** Depends. E05 is BBB- (investment grade) on local currency but BB (speculative) on foreign currency (A13, A14).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the later actions A35 and A33 do not change the rating level.

**Q12.** A-, from A34.

**Q13.** 1, which is A36. The Rating Watch (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26), and the downgrade A27 came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+, since A35 and A33 did not change the rating.

**Q17.** No. E06 only has a Rating Watch in 2026 (A17), which is not a downgrade. E13 (Orrin Bancorp) has a different LEI and is a separate entity.

**Q18.** E06 (A17). E14's Watch (A35) was superseded by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). The latest actions on E06 and E08 carry no outlook.

**Q20.** No. E07's only actions are the assignment A18 and a commercial-reasons withdrawal (A19), and neither is a default.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR FC is BBB (A03).

**Q25.** 5. I01 is BBB, I03 is A, I05 is BBB+, I06 is A- and I07 is BBB-. I02 and I04 are speculative grade, and I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling of BB (A12, A14). E15's FC rating is A, equal to Corvenia's ceiling of A (A37, A41).

**Q31.** No. E05 and E15 sit exactly at their ceilings, and the other companies' countries have no ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose LTIDR was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent link and is not in E09's chain.

**Q35.** 3: E09, E10 (E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records; merging E03 into E02 and E17 into E10 leaves 17, and excluding the QA record E16 leaves 16.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 was withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds for country, and it is the same entity as E10.

**Q43.** 1, the Halden Bank entity (E10/E17).

**Q44.** Yes. I07 pays in XVD, which is the domestic currency of VD, the country E05 is domiciled in.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected-rating action (A47), so it is still unrated.

**Q48.** 7: I01 to I07.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":12},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06"]},
"Q19":{"issuers":["E01","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":5},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":16},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":5},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":7}}
```