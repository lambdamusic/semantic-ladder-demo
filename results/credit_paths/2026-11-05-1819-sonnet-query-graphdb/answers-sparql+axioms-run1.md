**Q1.** A-. Action A01 gave Kestrel (E01) a foreign-currency rating of A- that stayed in force until 2025-06-20.
**Q2.** No. The 2026-02-10 action (A03) affirmed BBB and only moved the outlook to Negative.
**Q3.** No. The 2031 note (I02) was cut to BB+ by A07, which is below investment grade.
**Q4.** Positive. Northwind Holdings has two records, E02 and E03, linked as the same entity. E03's action A09 carries a Positive outlook.
**Q5.** The note (I03) takes the risk of the guarantor, Northwind Holdings (E02), and is rated A (A11).
**Q6.** The data only partly answers this. Valdoria Telecom (E05) is rated BB on a foreign-currency basis (A14) against BBB- on local currency (A13). Valdoria's Country Ceiling is BB (A12), and the definitions say foreign-currency ratings are subject to it. The data does not state the causal link itself.
**Q7.** E10 (A27, 2026-04-15) and E16 (A44, 2026-06-01). The query was truncated, so other issuers may be missing.
**Q8.** E08, which holds an RD rating (A22, 2026-07-08).
**Q9.** 378. This is a raw count that may include duplicate records for the same entity.
**Q10.** Depends. E05 is BB on foreign currency (sub-investment grade) and BBB- on local currency (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1, from A36.
**Q14.** BB- (A30).
**Q15.** A- (A26, for E10; E17 is a duplicate record).
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33), so only the watch and outlook changed.
**Q17.** No. Orrin Bank (E06) was only placed on Rating Watch Negative (A17) with its A- unchanged.
**Q18.** The 31 issuers returned are listed in the JSON, including E06. The list may be incomplete.
**Q19.** The query returned about 260 rows and only 27 were visible, so the JSON holds a partial list (including E01 and E09).
**Q20.** No. Pellam's (E07) rating was withdrawn (A19, WD), which is not a default.
**Q21.** E07, whose rating was withdrawn. The check was not exhaustive.
**Q22.** E08, the only RD or D rating found.
**Q23.** F2 (A04).
**Q24.** Yes, BBB (A03).
**Q25.** 72.
**Q26.** A+ (A40).
**Q27.** A- (A42, instrument I06).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling of BB (A12), which is not an issuer rating.
**Q30.** E05, E5047 and E5012 at Valdoria's BB ceiling, and E15 at Corvenia's A ceiling. This is a partial, best-effort list.
**Q31.** No. None of the checked ratings were above their country's ceiling, but coverage was incomplete.
**Q32.** E09.
**Q33.** The notes (I05) take the guarantor Halden Bank (E10)'s credit risk, rated BBB+ (A29).
**Q34.** No. Halden Foods (E12) has no parent, while Halden Bank (E10) sits under E09.
**Q35.** 4.
**Q36.** 3.
**Q37.** 511.
**Q38.** No. The data gives no link between them, and they differ in domicile (E06 DE, E13 US).
**Q39.** A (A09).
**Q40.** 79. This is a raw count that may include duplicate records.
**Q41.** BB+ (A44).
**Q42.** LU (E10 and E17).
**Q43.** 1. The two LU records, E10 and E17, appear to be one entity.
**Q44.** Yes. I07 is flagged as a local-currency obligation.
**Q45.** No. It is rated BBB- (A45) and is a local-currency obligation, so the foreign-currency ceiling does not apply.
**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46), which does not count.
**Q47.** None. I08 has only an Expected rating (A47), so it is still unrated.
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6. The chain is E5035, E5023, E5011, E5167, E5002, E5001, with E5005 being the same entity as E5167.
**Q51.** 58. The raw count is 59, less one duplicate record.
**Q52.** 19. This is an estimate because that query failed.
**Q53.** No. Belir Mining's (E5168) ultimate parent is E5059, and Rotam Group (E5086) is its own ultimate parent.
**Q54.** Not determined because the query failed.
**Q55.** 31.
**Q56.** BB- (E5144). Not every member was visible.
**Q57.** E5002.
**Q58.** E5145, which guarantees I5007 issued by E5133. The check was incomplete.
**Q59.** 12. This is an estimate.
**Q60.** E5145. It is presumably not in the same group as the issuer E5133 (the instrument is labelled "Cross-group"), but this was not verified.
**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E10","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":378},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"BB-"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1203","E1314","E1194","E1210","E1260","E1133","E1146","E1242","E1066","E1168","E1297","E1109","E1061","E1132","E1088","E06","E1098","E1266","E1006","E1267","E1037","E1013","E1317","E1181","E1323","E1059","E1099","E1238","E1264","E1039","E1126","E1019"]},"Q19":{"issuers":["E1300","E5099","E1080","E1105","E5113","E1034","E1118","E1056","E1064","E1055","E5097","E1046","E5059","E5020","E1161","E1263","E1282","E01","E5131","E5023","E5141","E5116","E09","E1271","E5039","E5102","E1228","E1060"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E5047","E5012","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":4},"Q36":{"count":3},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":[]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```