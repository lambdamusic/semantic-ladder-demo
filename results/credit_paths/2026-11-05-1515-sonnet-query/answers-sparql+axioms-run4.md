**Q1.** A-. Kestrel's foreign-currency issuer rating (LTIDR) was A- on 1 Jan 2025 (A01, valid to 2025-06-20).
**Q2.** No. The only downgrade was A02 on 2025-06-20; A03 on 2026-02-10 affirmed BBB and set a Negative outlook.
**Q3.** No, BB+. The 2031 note I02 was cut to BB+ by A07.
**Q4.** Positive. E02 and E03 are the same entity, and A09 (E03, 2025-09-15) is A with a Positive outlook.
**Q5.** E02, rated A. I03 is guaranteed by E02, and E02/E03 hold A (A09).
**Q6.** Valdoria's Country Ceiling is BB (A12). It caps the foreign-currency rating at BB (A14), while the local-currency rating is BBB- (A13).
**Q7.** E08, E10 and E16 (A21/A22, A27, A44). I only checked records E01–E16, so other issuers may be missing.
**Q8.** E08, which has been RD since A22 on 2026-07-08.
**Q9.** 378, counted as rated records. I did not collapse duplicate records, so this may be too high.
**Q10.** Depends. The local-currency rating is BBB- (investment grade), but the foreign-currency rating is BB (not).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1 (A36).
**Q14.** BB- (A30).
**Q15.** A- (A26).
**Q16.** No. It was BBB+ on 1 Jan 2025 and is BBB+ now (A33); only the watch status changed.
**Q17.** No. A17 was a Rating Watch Negative placement with A- unchanged.
**Q18.** 32 issuers, listed in the JSON.
**Q19.** 48 issuers, listed in the JSON.
**Q20.** No. E07's rating was withdrawn (A19, WD, "commercial reasons"), which is not a default.
**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19), and I found no other case.
**Q22.** E08 (RD on 2026-07-08) is the only default record.
**Q23.** F2 (A04).
**Q24.** Yes, BBB (A03).
**Q25.** 72, summing the investment-grade rating buckets of instruments in force.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The data holds only a Country Ceiling of BB for VD (A12) and no issuer rating.
**Q30.** E05 (BB at the VD ceiling of BB) and E15 (A at the CV ceiling of A). I checked only a few entities, so this may be incomplete.
**Q31.** No known case. E05 and E15 are at their ceilings, not above them, but I did not check every company.
**Q32.** E09.
**Q33.** E10, rated BBB+ (A27). I05 is guaranteed by E10.
**Q34.** No. E12 has no parent, so it is not in E09's group.
**Q35.** 3. E09, E10 and E11, where E17 is a duplicate record of E10.
**Q36.** 2. E02 (E03 is the same entity) and E04.
**Q37.** 511. There are 540 records, and 58 of them form 29 sameEntityAs pairs.
**Q38.** No. E06 and E13 are separate records with no sameEntityAs link.
**Q39.** A (A09).
**Q40.** 79, counted as records, so duplicates may inflate it.
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1. Only E10 and E17 are in LU, and they are the same entity.
**Q44.** Yes. I07 has localCurrency true.
**Q45.** No. I07 is a local-currency obligation, so the foreign-currency ceiling does not apply to it.
**Q46.** No. E11 has only a BBB rating of type CO (A46), not an issuer rating.
**Q47.** A (A47).
**Q48.** 113, summing the instruments in force by rating.
**Q49–Q59, Q61.** Not answered. My queries did not retrieve the group structure for these.
**Q60.** E5145, and no. I5007 is guaranteed by E5145, which is in a different group from the issuer E5133.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":378},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"BB-"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09","E5013","E5019","E5020","E5023","E5033","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":113},"Q49":{"parent":null},"Q50":{"count":null},"Q51":{"count":null},"Q52":{"count":null},"Q53":{"same_group":null},"Q54":{"entities":[]},"Q55":{"count":null},"Q56":{"rating":null},"Q57":{"entity":null},"Q58":{"entities":[]},"Q59":{"count":null},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":null}}
```