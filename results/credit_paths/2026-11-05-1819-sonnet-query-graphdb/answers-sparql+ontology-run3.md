Q1–Q47 are answered below from the record-level results I could read. The later queries (Q48–Q61, plus the counts in Q9, Q25 and Q37 and the full-dataset lists) returned malformed results, so I have left those as null rather than guess. I could not check the dataset-wide answers (Q7, Q8, Q18, Q19, Q21, Q22, Q30, Q31) against the full dataset. They cover only the records I could read: the E01–E17 block, the sovereigns, and instruments I01–I08.

**Q1.** A-. The rating was assigned A- on 2024-03-12 (A01) and not changed until the downgrade to BBB on 2025-06-20 (A02).
**Q2.** No. The only 2026 action on E01 is an affirmation with a Negative outlook (A03).
**Q3.** No, it is BB+. I02 is subordinated, and its latest action is the downgrade to BB+ on 2025-06-20 (A07).
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 on 2025-09-15, an affirmation of A with a Positive outlook.
**Q5.** The holder takes the credit risk of E02, Northwind Holdings. I03 is guaranteed by E02, whose issuer rating is A; the note itself is also rated A (A10/A11).
**Q6.** The Valdorian Country Ceiling is BB (A12). It caps the foreign-currency rating (BB, A14), while the local-currency rating (BBB-, A13) is not capped.
**Q7.** E08 and E10 (A21, A22, A27); E16's downgrade is QA data and is ignored.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22).
**Q10.** Depends. Foreign-currency is BB (speculative) and local-currency is BBB- (investment grade).
**Q11.** BBB+. A36 downgraded it from A- on 2024-09-30.
**Q12.** A-, from the assignment on 2023-01-15 (A34).
**Q13.** 1 (A36). The Rating Watch (A35) is not a downgrade.
**Q14.** None. The first action on E12 is 2024-02-01 (A30).
**Q15.** A-. The downgrade to BBB+ (A27) only came on 2026-04-15. E17 shares E10's LEI and carries no rating actions.
**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 did not change it).
**Q17.** No. The only 2026 action on E06 is a Rating Watch (A17).
**Q18.** E06 (A17). E14's Watch was resolved by the affirmation A33 on 2026-05-01.
**Q19.** E01 and E09 (A03, A25).
**Q20.** No. E07 was withdrawn (A19, commercial reasons), which is not a default.
**Q21.** E07 (A19).
**Q22.** E08 (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. The rating is BBB.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** E05 (BB, ceiling BB) and E15 (A, ceiling A); other entities were not checked.
**Q31.** No, among the entities I checked: E05 and E15 sit exactly at their ceilings.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** The holder takes the credit risk of E10, Halden Bank, which is rated BBB+ since A27. I05 is guaranteed by E10.
**Q34.** No. E12 has no parent, so it is not in E09's group.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.
**Q45.** No. The note is local-currency, so the ceiling does not apply.
**Q46.** No. E11 has only a Credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47), so it is unrated.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10"]},"Q8":{"entities":["E08"]},"Q9":{"count":null},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":null},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":null},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":null},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":null},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":null},"Q49":{"parent":null},"Q50":{"count":null},"Q51":{"count":null},"Q52":{"count":null},"Q53":{"same_group":null},"Q54":{"entities":null},"Q55":{"count":null},"Q56":{"rating":null},"Q57":{"entity":null},"Q58":{"entities":null},"Q59":{"count":null},"Q60":{"risk_of":null,"same_group":null},"Q61":{"count":null}}
```