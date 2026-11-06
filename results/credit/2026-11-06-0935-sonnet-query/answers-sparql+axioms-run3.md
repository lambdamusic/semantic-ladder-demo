**Q1.** A-. Kestrel's foreign-currency long-term rating was A- on that date (A01, valid 2024-03-12 to 2025-06-20).
**Q2.** No. The only 2026 action is A03 on 2026-02-10, which affirmed BBB and set a Negative outlook. The downgrade to BBB came in 2025 (A02).
**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is sub-investment grade.
**Q4.** Positive. A09 is on E03, which is the same entity as E02 (same LEI, `sameEntityAs`).
**Q5.** E02 (Northwind Holdings, the guarantor of I03), rated A (A09). I03 itself is also rated A (A11).
**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13), which is not capped.
**Q7.** E08, E10 and E16. They were downgraded by A21/A22, A27 and A44. The I05 downgrade (A29) is an instrument action.
**Q8.** E08. Its rating is RD (A22).
**Q9.** 13. These are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16. A44 for E16 is not in the in-force class, but it has no end date, so I counted it.
**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13). The foreign-currency rating is BB (not investment grade, A14).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1, from A36 on 2024-09-30.
**Q14.** None. Halden Foods' first rating is dated 2024-02-01 (A30).
**Q15.** A-. Halden Bank (E10, same entity as E17) was rated A- (A26) until 2026-04-15.
**Q16.** No. Marlow was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).
**Q17.** No. Orrin Bank (E06) went on Rating Watch Negative at A- (A17), with no rating change.
**Q18.** E06. A35 for Marlow ended on 2026-05-01.
**Q19.** E01 and E09 (A03, A25).
**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and there is no default record.
**Q21.** E07, whose rating was withdrawn (A19). E02's earlier rating continues under E03.
**Q22.** E08 (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 5. These are I01, I03, I05, I06 and I07.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. Valdoria has only a Country Ceiling (A12), not an issuer rating.
**Q30.** E05 and E15. Their foreign-currency ratings equal their country ceilings: BB for Valdoria and A for Corvenia.
**Q31.** No. No company's foreign-currency rating exceeds its ceiling.
**Q32.** E09.
**Q33.** E10 (Halden Bank, the guarantor), rated BBB+ (A27).
**Q34.** No. E12 has no parent link to E09.
**Q35.** 3 entities (E09, E10/E17 and E11).
**Q36.** 2 entities (E02/E03 and E04).
**Q37.** 18. There are 20 records, and E02/E03 and E10/E17 are each one entity.
**Q38.** No. They have different LEIs and no `sameEntityAs` link.
**Q39.** A (A09).
**Q40.** 6. These are E01, E02/E03, E09, E12, E14 and E16 (5 if E16's A44 is excluded).
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1 (E10/E17).
**Q44.** Yes. I07 is denominated in XVD and flagged `localCurrency` true.
**Q45.** No. The note is local-currency, so the foreign-currency ceiling does not apply, even though BBB- is above BB.
**Q46.** No. E11 has only a counterparty-type rating (A46), not an issuer rating.
**Q47.** None. I08's A rating was marked expired (A47, EX).
**Q48.** 7 (I01 to I07).

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":13},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":5},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":18},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":6},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":7}}
```