**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12) until the downgrade in A02 (2025-06-20).

**Q2.** No. 2026 has only affirmations (A03 LTIDR BBB, A04 STIDR F2); the downgrades were in 2025 (A02, A06, A07).

**Q3.** No, it is BB+. I02 was BBB (A23) and was downgraded to BB+ in A07.

**Q4.** Positive. E03 has the same LEI as E02, so I treat them as one entity. The latest action is A09 (2025-09-15), an affirmation with a Positive outlook, which supersedes A08.

**Q5.** The guarantor E02, rated A. I03 is issued by E04 but guaranteed by E02, whose latest rating is A (A09, same entity as E03).

**Q6.** The data states no reason. E05 has an LC rating of BBB- (A13) and an FC rating of BB (A14). The BB FC rating equals Valdoria's country ceiling (A12), which is consistent with a ceiling effect, but that is an inference.

**Q7.** E08, E10 and E16. Their issuer-level downgrades are A21/A22, A27 and A44. A29 is an instrument downgrade, so it is excluded.

**Q8.** E08. It was at RD from A22 (2026-07-08) with no later action.

**Q9.** 13 (E01, E02/E03, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16, CV). E07 is withdrawn (A19), E06 is on watch but still rated (A17), and E11 has only a CO rating (A46).

**Q10.** Depends. E05 is BBB- on a local-currency basis (investment grade, A13) and BB on a foreign-currency basis (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) is the latest action on or before that date.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36. A35 is a watch and A33 is an affirmation.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. This is E10 (A26); the downgrade in A27 came in April 2026. E17 has the same LEI, so it is a duplicate record with no ratings.

**Q16.** No. It was BBB+ then and is BBB+ now (A33). A35 was only a Rating Watch.

**Q17.** No. E06 has only a Rating Watch Negative in 2026 (A17). E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and there is no default rating.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes, BBB (A03).

**Q25.** 5: I01, I03, I05, I06 and I07. I08 is excluded because its action code EX is undefined in the data (see Q47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. The only rating for VD is a country-ceiling record (A12), not an issuer rating.

**Q30.** E05 (FC BB equals the VD ceiling BB) and E15 (FC A equals the CV ceiling A, A37/A41).

**Q31.** No.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor E10, rated BBB+ (A27). I05 is issued by E11 but guaranteed by E10.

**Q34.** No. E12 has no parent link to the Halden group in the data; the shared name alone is not evidence.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 17. There are 19 entity records, but E17 duplicates E10 and E03 duplicates E02 (same LEIs).

**Q38.** No. They have different LEIs and countries (DE and US).

**Q39.** A (A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because it was withdrawn.

**Q41.** BB+ (A44). The record's source is "QA", which may mean test data.

**Q42.** DE (E10). E17 says LU but is a duplicate with the same LEI.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE); if you count E17 separately, it would be 1.

**Q44.** Yes, probably. I07 is in XVD, which the data does not define, but its BBB- matches E05's LC rating.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note at BBB- (A45), which is above the BB ceiling anyway.

**Q46.** No. E11 has only a CO rating (A46), not an issuer default rating.

**Q47.** None. A47 uses action code EX, which the data does not define. If it is an expected rating, it is not a held rating; if it is a held rating, the value would be A.

**Q48.** 7 (I01–I07), on the same basis as Q47 for I08.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":13},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":5},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":17},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":6},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":7}}
```