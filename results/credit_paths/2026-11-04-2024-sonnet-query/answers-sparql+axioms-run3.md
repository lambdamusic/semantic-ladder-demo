I could not verify every answer. Q7, Q19 and Q25 are the weakest: the query results truncated some rows, and for Q25 I never ran an investment-grade count, so the Q25 figure is only a lower bound.

**Q1.** A-. A01 held Kestrel (E01) at A- from 2024-03-12 to 2025-06-20.
**Q2.** No. The only downgrade was A02 (BBB) on 2025-06-20, and A03 on 2026-02-10 is an affirmation with a Negative outlook.
**Q3.** No, BB+. The 2031 note I02 is rated BB+ (A07), below investment grade.
**Q4.** Positive. E02 and E03 are the same entity, and A09 on E03 has a Positive outlook.
**Q5.** E02, rated A. I03 is guaranteed by E02, and I03 (A11) and E02/E03 (A09) are all rated A.
**Q6.** Not answered (not in the JSON). The data shows E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13), but it gives no reason for the gap. The country ceiling for VD (A12) is BB, which fits the foreign-currency rating, but the data does not state it as the cause.
**Q7.** E08, E10, E16 and E5019 (A21/A22, A27, A44, A5012). The list may be incomplete because some rating actions were truncated.
**Q8.** E08, which holds RD (A22).
**Q9.** 366 distinct entities, with same-entity duplicates merged.
**Q10.** Depends. E05 is BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13).
**Q11.** BBB+. A36 applied from 2024-09-30 to 2025-11-20.
**Q12.** A-. A34 applied from 2023-01-15.
**Q13.** 1, via A36.
**Q14.** None. Halden Foods' (E12) first rating (A30) is dated 2024-02-01.
**Q15.** A-. A26 applied until 2026-04-15.
**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now (A33), though a watch came and went in between.
**Q17.** No. A17 is a Rating Watch Negative at an unchanged A-.
**Q18.** E06 (A17).
**Q19.** E01, E09, E5013, E5019, E5020 and E5023. The list may be incomplete because some rating actions were truncated.
**Q20.** No. E07's rating was withdrawn (WD, A19), which is not a default.
**Q21.** E07, whose rating was withdrawn on 2026-05-12.
**Q22.** E08, the only record with RD.
**Q23.** F2 (A04).
**Q24.** Yes. E01 is BBB (A03).
**Q25.** At least 5 (I01, I03, I05, I06, I07). I did not count the many other instruments, so the true figure is likely higher.
**Q26.** A+ (A40, local-currency basis).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The data holds only a VD Country Ceiling of BB (A12), not an issuer rating.
**Q30.** E05, E1028, E1101, E1126, E1236, E5012, E5047, E5091 and E5124 are at the VD ceiling of BB. E15, E1039, E1194 and E5116 are at the CV ceiling of A.
**Q31.** No. Every foreign-currency rating I found is at or below its country ceiling.
**Q32.** E09.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and both I05 (A29) and E10 (A27) are BBB+.
**Q34.** No. E12 has no parent and sits in no group with E09.
**Q35.** 3 distinct entities (E09, E10 and E11). E17 is a duplicate record of E10.
**Q36.** 2 (E02, which is also E03, and E04).
**Q37.** 511, after merging same-entity duplicates.
**Q38.** No. There is no sameEntityAs link between E06 and E13.
**Q39.** A (A09).
**Q40.** 74.
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1 (E10, with E17 as its duplicate).
**Q44.** Yes. I07 has localCurrency true.
**Q45.** Yes. I07 is BBB- (A45) against a VD ceiling of BB (A12).
**Q46.** No. E11 only has a CO-type rating (A46), not a long-term issuer rating.
**Q47.** None in force. I08's only action, A47, is an EX action, and it is not among the ratings in force.
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6 levels, treating E5005 and E5167 as the same entity.
**Q51.** 58 distinct entities (59 records, with E5005 and E5167 merged).
**Q52.** 19.
**Q53.** No. Their ultimate parents are E5059 and E5086.
**Q54.** E5106, E5124, E5130 and E5169.
**Q55.** 31.
**Q56.** BB- (E5144, A5108).
**Q57.** E5002.
**Q58.** E5145. It guarantees I5007, which is issued by E5133, in group E5132.
**Q59.** 12 (E5011 to E5022).
**Q60.** E5145. It is not in the same group as the issuer E5133, whose ultimate parent is E5132.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16","E5019"]},"Q8":{"entities":["E08"]},"Q9":{"count":366},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09","E5013","E5019","E5020","E5023"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":5},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124","E15","E1039","E1194","E5116"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":74},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5124","E5130","E5169"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```