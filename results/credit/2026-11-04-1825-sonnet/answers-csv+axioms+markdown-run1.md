**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. E01's only 2026 issuer actions are the affirmations A03 and A04, and no 2026 action on E01 is a downgrade.

**Q3.** No, it is BB+. I02 was downgraded to BB+ by A07 on 2025-06-20, which is speculative grade.

**Q4.** Positive. E03 shares its LEI with E02, so A09 (2025-09-15, outlook POS) is the latest action for Northwind Holdings.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes the parent's risk. E02's current LTIDR is A (A09, which is recorded on E03, the same entity).

**Q6.** Valdoria's Country Ceiling is BB (A12) and caps foreign-currency ratings. E05's FC rating is therefore BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A44 (E16) is QA data and is ignored.

**Q8.** E08. It has held RD since A22 on 2026-07-08.

**Q9.** 12. The issuers are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 was withdrawn, E16 is QA, and E04, E11 and VD have no issuer rating.

**Q10.** Depends. E05's LC rating is BBB- (investment grade) and its FC rating is BB (speculative grade).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30, and the watch in A35 left the rating unchanged.

**Q12.** A-, from A34.

**Q13.** 1. The only downgrade of E14 is A36.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10 and E17 are the same entity, and the downgrade A27 only took effect on 2026-04-15.

**Q16.** No. E14 was BBB+ after A36 and is still BBB+ after A33.

**Q17.** No. A17 is only a Rating Watch, and the rating stays A-.

**Q18.** E06. A17 was placed on 2026-09-03. E14's earlier watch (A35) ended with the affirmation A33.

**Q19.** E01 and E09 (A03 and A25). E06's latest action, A17, carries no outlook.

**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and its last rating before that was BB.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an expected rating (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The ceiling in A37 is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB. E15's FC rating is A, equal to the CV ceiling of A.

**Q31.** No. E05 and E15 are exactly at their ceilings, and no GB or other entity has a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose LTIDR was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 duplicate other entities, and E16 is QA test data.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in DE.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds, and E17's LU is overridden.

**Q43.** 0. E17 is domiciled in DE through its RATINGS twin E10, and no other entity has LU.

**Q44.** Yes. I07 pays in XVD, which is the domestic currency of VD, E05's domicile.

**Q45.** No. I07 is local-currency debt, so the ceiling does not apply to it.

**Q46.** No. E11 has only a credit opinion (A46, type CO), which is not an issuer rating.

**Q47.** None. I08 has only an Expected rating (A47, EX), so it is unrated.

**Q48.** 7: I01 to I07.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10"]},"Q8":{"entities":["E08"]},"Q9":{"count":12},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":5},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":16},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":5},"Q41":{"rating":"none"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":7}}
```