**Q1.** A-. E01's last action before 1 Jan 2025 was A02's predecessor, A01 (AS A-, 2024-03-12). The downgrade to BBB (A02) came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03 (AF BBB, with the outlook moved to negative). An affirmation and an outlook change are not downgrades.

**Q3.** No. The 2031 note (I02) is subordinated and was rated BB+ by A07 on 2025-06-20, which is speculative grade.

**Q4.** Positive. E02 and E03 share the LEI NWND00HOLDINGS00GB42, so they are one entity. The latest action is A09 (2025-09-15, AF A, POS).

**Q5.** The holder takes E02's credit risk (E02 and E03 are the same entity), which is rated A. I03 is guaranteed by E02, and A09 is the latest action (A).

**Q6.** E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The FC rating is capped by Valdoria's Country Ceiling, which is BB (A12); the LC rating is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is on a QA record and is ignored.

**Q8.** E08. A22 moved it to RD, which is a default, on 2026-07-08.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07's rating was withdrawn (A19). E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the watch in A35 came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 (and E17, which has the same LEI) has been rated A- since A26. The downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is A17, a Watch Negative placement with the rating unchanged. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's watch (A35) ended with the affirmation in A33.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), which is not a default.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's FC long-term rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 and I04 are BB+ and BB, and I08 is unrated.

**Q26.** A+, from A40 (the LC rating for E15).

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38. The CV record A37 is a Country Ceiling, not an issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB).

**Q30.** E05 and E15. E05's FC rating is BB, equal to Valdoria's ceiling of BB (A14, A12). E15's FC rating is A, equal to Corvenia's ceiling of A (A41, A37).

**Q31.** No. Neither E05 nor E15 is above its ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, because E10 guarantees I05. E10 is rated BBB+ after the downgrade in A27.

**Q34.** No. E12 has no parent link to the Halden group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).

**Q36.** 2: E02 (the same entity as E03) and its finance subsidiary E04.

**Q37.** 16. The 19 entity records include two duplicates (E17 = E10, E03 = E02) and one QA record (E16).

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09, 2025-09-15).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 says DE, and it takes precedence over the LU in the E17 record.

**Q43.** 0. The only LU record, E17, duplicates E10, which the system of record places in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and its issuer E05 is domiciled in VD.

**Q45.** No. I07 is rated BBB- (A45), above the BB ceiling, but local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, so I08 is unrated.

**Q48.** 7: I01 to I07.

```json
{"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
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
"Q42":{"country":"DE"},
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":7}}
```