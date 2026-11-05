**Q1.** A-. Kestrel's long-term rating A- (A01) was in force from 2024-03-12 until 2025-06-20.
**Q2.** No. The only 2026 action is an affirmation with the outlook moved to Negative (A03, 2026-02-10).
**Q3.** No, BB+. The 2031 note (I02) was cut to BB+ (A07).
**Q4.** Positive. The Northwind records E02 and E03 are the same entity, and A09 (A, Positive) is the current action.
**Q5.** E02, rated A. The note (I03) is guaranteed by E02, and its rating (A11) is A.
**Q6.** Not answered from the data. It shows Valdoria Telecom (E05) rated BB foreign-currency and BBB- local-currency (A14, A13), with Valdoria's country ceiling at BB (A12).
**Q7.** The 28 entities downgraded in 2026 are in the JSON. The count may be incomplete.
**Q8.** E08 (Saxby Shipping), rated RD (A22).
**Q9.** 377 distinct issuers hold a non-withdrawn long-term issuer rating.
**Q10.** Depends. Valdoria Telecom is BB foreign-currency (below investment grade) and BBB- local-currency (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** Once (A36, 2024-09-30).
**Q14.** None. The first Halden Foods rating (E12) is dated 2024-02-01.
**Q15.** A- (A26, E10, same entity as E17).
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; only the watch status changed.
**Q17.** No. Orrin Bank (E06) was only placed on Rating Watch Negative (A17).
**Q18.** E06 is confirmed. My query for other issuers on watch was truncated, so the list may be incomplete.
**Q19.** The JSON lists the seven I saw: E01, E09, E1005, E1029, E1034, E1046 and E1055. About 120 more rows were truncated, so the list is incomplete.
**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), not because of default.
**Q21.** E07 is the only one I can confirm (rating withdrawn, A19). The check was truncated, so there may be others.
**Q22.** E08 (CCC, then RD, A21 and A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** 72.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. I found only a country-ceiling record for the Republic of Valdoria, no issuer rating.
**Q30.** The JSON lists the entities whose foreign-currency rating equals the ceiling in CV (A) and VD (BB). I could not check other countries' ceilings.
**Q31.** No, for the CV and VD companies checked; none exceeds its ceiling. Other countries' ceilings were not checked.
**Q32.** E09.
**Q33.** E10, rated BBB+ (guarantor of I05; A29).
**Q34.** No. Halden Foods (E12) is its own ultimate parent.
**Q35.** 3 (E09, E10/E17, E11).
**Q36.** 2 (E02/E03 and E04).
**Q37.** 511 distinct entities, with sameEntityAs duplicates merged.
**Q38.** No. There is no sameEntityAs link between E06 and E13.
**Q39.** A.
**Q40.** 79.
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1.
**Q44.** Yes (I07 has localCurrency true).
**Q45.** Yes. It is rated BBB- (A45) against a ceiling of BB (A12).
**Q46.** No. E11 has only an instrument-level rating (A46, type CO).
**Q47.** A (A47).
**Q48.** 113.
**Q49.** E5001.
**Q50.** 7 levels. E5047's ancestors are E5035, E5023, E5011, E5005, E5167, E5002 and E5001.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. Belir's ultimate parent is E5059, not Rotam (E5086).
**Q54.** E5106, E5124 and E5130. E5169 is a duplicate record of E5106.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002.
**Q58.** E5145, which guarantees I5007 issued by E5133 in the Vesol group.
**Q59.** 12.
**Q60.** E5145, and no, it is not in the same group as the issuer E5133.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":7},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5124","E5130"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```