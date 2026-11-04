**Q1.** A-. E01's FC LTIDR was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation (the outlook went to negative).

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07, so it is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action, with a POS outlook.

**Q5.** The holder takes Northwind Holdings' (E02) credit risk, rated A. I03 is guaranteed by E02, and E02/E03's latest LTIDR (A09) is A.

**Q6.** The FC rating is capped by the Country Ceiling. The ceiling for VD is BB (A12), and E05's FC rating is BB (A14), while its LC rating is BBB- (A13) because LC is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument action, and A44 is a QA record that is ignored.

**Q8.** E08. It was rated RD from A22 (2026-07-08), which is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 is withdrawn, VD has only a ceiling, E11 has only a credit opinion, E04 has no rating, and E16 is QA.

**Q10.** Depends. The LC rating is BBB- (investment grade) and the FC rating is BB (speculative grade).

**Q11.** BBB+. The downgrade A36 (2024-09-30) set BBB+, and the next action is on 2025-11-20.

**Q12.** A-, set by A34.

**Q13.** 1, which is A36.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E17 has the same LEI as E10, and A26 set A- until the downgrade on 2026-04-15.

**Q16.** No. BBB+ has held since A36 in 2024. A35 and A33 did not change it.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch placement, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) is in force. E14's earlier RWN (A35) was superseded by A33.

**Q19.** E01 and E09, from A03 and A25. A17 on E06 carries no outlook, so I did not count E06.

**Q20.** No. A19 is a withdrawal, which is not a default, and E07's last rating was BB.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. I01 is BBB, I03 is A, I05 is BBB+, I06 is A- and I07 is BBB-. I02 and I04 are speculative grade, and I08 is only an expected rating.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The ceiling in A37 is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's is A, equal to the CV ceiling of A.

**Q31.** No. No company's FC rating is above its ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes Halden Bank's (E10) credit risk, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link to E09.

**Q35.** 3, which are E09, E10 (with E17) and E11.

**Q36.** 2, which are E02 (with E03) and E04.

**Q37.** 16. There are 19 records, E03 and E17 are duplicates by LEI, and the QA record E16 is excluded.

**Q38.** No. They have different LEIs and are separate entities.

**Q39.** A, from A09 (E03 is the same entity as E02).

**Q40.** 5, which are E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA test record and is ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. E17's LU is overridden by the RATINGS country of DE.

**Q44.** Yes. I07 is in XVD, which is VD's domestic currency.

**Q45.** No. I07 is BBB- and the ceiling is BB, but the ceiling does not apply to local-currency debt.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.

**Q48.** 7, which are I01 to I07.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10"]},"Q8":{"entities":["E08"]},"Q9":{"count":12},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":5},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":16},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":5},"Q41":{"rating":"none"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":7}}
```