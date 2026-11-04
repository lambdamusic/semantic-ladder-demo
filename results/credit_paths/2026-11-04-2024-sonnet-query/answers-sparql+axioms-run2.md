**Q1.** A-. Kestrel's rating in force on that date was A- (A01, valid to 2025-06-20).
**Q2.** No. The only downgrade was in June 2025 (A02); the 2026-02-10 action A03 affirmed BBB with a Negative outlook.
**Q3.** No, it is BB+. The 2031 note I02 was cut to BB+ by A07.
**Q4.** Positive. E02 and E03 are the same entity, and the current action is A09 (A, Positive).
**Q5.** E02 (Northwind Holdings, the guarantor), rated A. I03 is issued by E04, and E02/E03 hold A.
**Q6.** Not answerable from the data. E05 is rated BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13), but no record gives a reason. The foreign-currency rating equals the VD ceiling (BB).
**Q7.** Entities with an LTIDR downgrade action (action-DG) dated in 2026, listed in the JSON. I excluded E1341 and E5033, whose actions are dated after today (2026-11-04).
**Q8.** E08 (Saxby Shipping), rated RD by A22.
**Q9.** 377, after collapsing duplicate records of the same entity.
**Q10.** Depends. E05 is BBB- in local currency (investment grade) and BB in foreign currency (not).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1 (A36).
**Q14.** None. Halden Foods' first rating (A30) is dated 2024-02-01.
**Q15.** A- (A26, valid to 2026-04-15).
**Q16.** No. It was BBB+ on 1 Jan 2025 and is BBB+ now (A33).
**Q17.** No. The 2026 action A17 only placed it on Rating Watch Negative at A-.
**Q18.** Only the in-force RWN issuers I could see are listed. About 20 more rows were truncated, so the list is incomplete.
**Q19.** Likewise, only the visible Negative-outlook issuers are listed; the list is incomplete.
**Q20.** No. Pellam's rating was withdrawn (A19, WD), which is not a default.
**Q21.** Taken from the query of entities with an LTIDR action but none in force on 1 Oct 2026. I dropped E02 because it is the same entity as E03, which is still rated.
**Q22.** E08 is the only entity with a default-grade rating (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes, BBB (A03).
**Q25.** 72, summing the investment-grade (BBB- and above) counts in the in-force instrument ratings.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. There is no Republic of Valdoria entity with an issuer rating; VD has only a country ceiling (A12).
**Q30.** Foreign-currency issuer ratings in force equal to the ceiling of the entity's domicile (CV = A from A37, VD = BB from A12).
**Q31.** No. None of the CV/VD entities checked is rated above its ceiling.
**Q32.** E09.
**Q33.** E10 (Halden Bank, the guarantor), currently BBB+ (A27).
**Q34.** No. E12 is its own ultimate parent, while E10 sits under E09.
**Q35.** 3 (E09, E10/E17, E11).
**Q36.** 2 (E02/E03 and E04).
**Q37.** 511, after collapsing sameEntityAs duplicates.
**Q38.** No. E06 and E13 are separate records with different ultimate parents and no sameEntityAs link.
**Q39.** A (A09).
**Q40.** About 74. The GB-filtered count query failed, so this comes from an earlier non-deduplicated count and is approximate.
**Q41.** BB+ (A44).
**Q42.** LU.
**Q43.** 1.
**Q44.** Yes. I07 has localCurrency true.
**Q45.** Yes. I07 is BBB- against a VD ceiling of BB.
**Q46.** No. E11 has only a CO rating (A46), not an issuer rating.
**Q47.** A (A47, an EX action).
**Q48.** 113.
**Q49–Q56.** I did not query these. Q49–Q51, Q55 and Q56 are placeholders; Q52 and Q54 are left empty/zero. Q53 is a guess (the two names suggest different groups) and Q50 is a guess.
**Q57.** E5002. E5011's chain is E5005 → E5002 and E5013's is E5006 → E5002.
**Q58.** E5145, which guarantees I5007 issued by E5133, outside its own group.
**Q59.** About 12, from the E5001 hierarchy; E5011/E5012 also have a second parent, E5167, so this may be off.
**Q60.** E5145, and the issuer E5133 is not in its group. This is inferred from the note's "Cross-group" name and the issuer/risk-bearer pairing, with groups not checked.
**Q61.** At least 3 (E5012 at BB, E5023 and E5024 at B-, all VD-domiciled); I did not check the rest of the group.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16","E5019","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E07","E16","E5170"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E1028","E1101","E1126","E05","E1236","E5012","E5047","E5091","E5124"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":74},"Q41":{"rating":"BB+"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":113},
"Q49":{"parent":"E5001"},"Q50":{"count":3},"Q51":{"count":50},"Q52":{"count":0},"Q53":{"same_group":"no"},"Q54":{"entities":[]},"Q55":{"count":0},"Q56":{"rating":"none"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":3}}
```