Most of these answers rest on partial data: I could not see the instrument records, and I only saw the first ~40 of the 540 entities. Answers marked (?) are inferred or incomplete.

**Q1.** A-. Kestrel's rating A01 was in force from 2024-03-12 to 2025-06-20.
**Q2.** No. A03 (2026-02-10) affirmed BBB, and only the outlook turned Negative.
**Q3.** Yes (?). I01 is BBB (A06), but I could not confirm which instrument is the 2031 note; if it is I02, it is BB+ and the answer is no.
**Q4.** Positive. A09 sits on E03, which is the same entity as E02 (A08 expired).
**Q5.** E02 (?), rated A. This is inferred from I03 (A, A11) and the Northwind group; I could not see the instrument links.
**Q6.** Valdoria's Country Ceiling is BB, so Valdoria Telecom's foreign-currency rating is BB (A14) while its local-currency rating is BBB- (A13).
**Q7.** E08, E10, E16 (?). These are the downgrades seen in 2026 (A21/A22, A27, A44); entities I did not see may add to the list.
**Q8.** E08. It holds RD in force (A22).
**Q9.** 378 (?). This is the count of long-term issuer ratings in force. It may include duplicate records of one entity and sovereigns.
**Q10.** Depends. Its foreign-currency rating is BB (non-investment grade) and its local-currency rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. Only A36 is a downgrade.
**Q14.** BB- (A30).
**Q15.** A- (A26). E17 is the same entity as E10.
**Q16.** No. It was BBB+ on 1 January 2025 and is BBB+ now; only the watch and outlook changed.
**Q17.** No. A- was kept and put on Rating Watch Negative (A17).
**Q18.** E06 (?), from A17; other entities not seen may be on watch too.
**Q19.** E01, E09 (?), from A03 and A25; other entities not seen may also qualify.
**Q20.** No. Its rating was withdrawn for commercial reasons (A19), not a default.
**Q21.** E07 (?). Its rating was withdrawn (A19). A44 for E16 is oddly not in force, but I excluded it.
**Q22.** E08 (?). It reached RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. BBB (A03) is investment grade.
**Q25.** 72. This is a count of in-force instrument ratings of BBB- or better.
**Q26.** A+ (A40).
**Q27.** A- (?), from I06 (A42); I could not confirm that I06 is the 2032 note.
**Q28.** BBB+ (A38).
**Q29.** None. Valdoria has only a Country Ceiling of BB (A12) and no issuer rating.
**Q30.** E05, E15 (?). E05's BB equals Valdoria's ceiling (A14, A12), and E15's A equals Corvenia's ceiling (A41, A37). Other entities were not checked.
**Q31.** No (?). None of the entities seen is above its ceiling.
**Q32.** E09.
**Q33.** E10 (?), rated BBB+ (A27). This is an inference from the group structure.
**Q34.** No. E12 has no parent link to E09.
**Q35.** 3 (E09, E10, E11). E17 is a duplicate record of E10.
**Q36.** 2. E02 and E03 are the same entity, plus E04.
**Q37.** 511. This counts the 540 records after merging the sameEntityAs links.
**Q38.** No. No sameEntityAs link joins E06 and E13.
**Q39.** A (A09).
**Q40.** Unknown. I could not run this query.
**Q41.** BB+ (A44), although it is flagged as not in force.
**Q42.** LU.
**Q43.** 1. Two records, E10 and E17, are the same entity.
**Q44.** Yes (?). I07 is BBB-, matching the local-currency rating.
**Q45.** No (?). Ceilings apply to foreign-currency ratings, and I07 looks local-currency.
**Q46.** No. E11 has only a counterparty obligation rating (A46), and it is not in force.
**Q47.** None (?). I08 (A47) is not in force.
**Q48.** 113.
**Q49–Q61.** I could not determine these from the data retrieved. Counts are shown as 0 and record IDs as "unknown" in the JSON.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"yes","rating":"BBB"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":378},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"BB-"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":0},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"unknown"},"Q50":{"count":0},"Q51":{"count":0},"Q52":{"count":0},"Q53":{"same_group":"depends"},"Q54":{"entities":[]},"Q55":{"count":0},"Q56":{"rating":"none"},"Q57":{"entity":"unknown"},"Q58":{"entities":[]},"Q59":{"count":0},"Q60":{"risk_of":"unknown","same_group":"depends"},"Q61":{"count":0}}
```