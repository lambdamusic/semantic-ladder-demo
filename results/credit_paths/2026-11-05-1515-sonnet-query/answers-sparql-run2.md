**Q1.** A-. Kestrel's last action before 1 Jan 2025 was A01 (A-, 2024-03-12); the downgrade A02 came on 2025-06-20.
**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB.
**Q3.** No, it is BB+. I02 (subordinated) was rated BB+ by A07 on 2025-06-20.
**Q4.** Positive. E02 and E03 share the same LEI, so I treated them as one entity. The latest outlook is A09 on E03 (POS, 2025-09-15), and E02's only action is A08 (STA, 2023).
**Q5.** E02, rated A. I03 is issued by E04 and guaranteed by E02, so the holder takes the guarantor's risk. E02/E03's latest rating is A, and I03 is also rated A.
**Q6.** The data does not state a reason. It does show Valdoria's country ceiling (A12 on VD) at BB, equal to E05's FC rating.
**Q7.** 51 entities had a downgrade in 2026 (all listed in the JSON). They include E08, E10 and E16; E01, E06 and E14 do not.
**Q8.** E08. Its latest rating on 1 Oct 2026 is RD (A22, 2026-07-08). E07's last action is a withdrawal.
**Q9.** 389. This counts distinct LEI-based issuers whose latest long-term issuer rating on 1 Oct 2026 was not a withdrawal.
**Q10.** Depends. E05's foreign-currency rating is BB (sub-investment grade) and its local-currency rating is BBB- (investment grade).
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).
**Q12.** A-. This is E14's A-AS rating from 2023-01-15 (A34).
**Q13.** 1. A36 is the only downgrade action on E14.
**Q14.** None. E12's first rating is 2024-02-01.
**Q15.** A-. E10's rating was A- until the downgrade on 2026-04-15. E17 shares E10's LEI.
**Q16.** No. The rating was BBB+ on 1 Jan 2025 and is still BBB+, although a Rating Watch Negative (A35) came and went in between.
**Q17.** No. E06's 2026 action is a Rating Watch Negative at A- (A17), not a downgrade.
**Q18.** 30 issuers (listed in the JSON), found from each entity's latest foreign-currency issuer rating on 1 Oct 2026.
**Q19.** 57 issuers (listed in the JSON). I took the latest rating action that carries an outlook for each entity, so entities whose latest action is a watch rather than an outlook are not included.
**Q20.** No. Pellam's last action is a withdrawal (A19, 2026-05-12). Earlier D and RD actions appear only in the other record set, which I did not rely on.
**Q21.** 37 entities, including E07, whose latest long-term action on 1 Oct 2026 was a withdrawal.
**Q22.** E08 only. It is the only entity with any D/RD rating in the data.
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 75, out of 119 rated instruments.
**Q26.** A+ (local currency, A40).
**Q27.** A- (A42 on I06).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling record (A12, BB), not an issuer rating.
**Q30.** 13 entities. Their foreign-currency issuer rating equals their country's ceiling (listed in the JSON).
**Q31.** No. My comparison query returned no rows, but it only ranked ratings from B- to AAA and ignored the D/RD/WD cases.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** E10, rated BBB+. I05 is issued by E11 and guaranteed by E10, which was downgraded to BBB+ on 2026-04-15.
**Q34.** No. E12 has no parent link to E09 or E10.
**Q35.** 3 (E09, E10, E11).
**Q36.** 2 (E02, E04).
**Q37.** 511. There are 540 entity records; I counted by LEI where one exists, so duplicate records collapse.
**Q38.** No. They have different LEIs and countries (DE vs US).
**Q39.** A, from E03's A09 on 2025-09-15, which is later than E02's A (A08).
**Q40.** 87, counting distinct LEI-based entities with country GB.
**Q41.** BB+ (E16, A44).
**Q42.** DE. Record E17 shares E10's LEI but says LU.
**Q43.** 1, but this is ambiguous. Only E17 says LU, and it shares E10's LEI, so it may just be a duplicate of a DE entity.
**Q44.** Yes. I07's currency is XVD, Valdoria's local currency.
**Q45.** Yes. I07 is rated BBB- (A45) against a Valdoria ceiling of BB.
**Q46.** No. E11 has only a counterparty rating (A46, BBB), not an issuer rating.
**Q47.** A (A47, 2026-09-01).
**Q48.** 119.
**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167. E5167 shares E5005's LEI, so it is a duplicate record and the chain continues E5005 → E5002 → E5001.
**Q50.** 6 levels, counting E5167 as the same legal entity as E5005.
**Q51.** 59. There are 55 members through E5001, plus 4 more (E5011, E5023, E5035, E5047) reached via the duplicate E5167.
**Q52.** 20.
**Q53.** No. Belir Mining's top parent is E5059 (Belir Group AG), not E5086.
**Q54.** E5124 and E5130.
**Q55.** 23, counting rated entities with a VD-domiciled ancestor.
**Q56.** BB- (E5144).
**Q57.** E5002, via E5011 → E5167 (= E5005) → E5002 and E5013 → E5006 → E5002.
**Q58.** E5145. It guarantees I5007 (the Cross-group notes), issued by E5133, which is in the Vesol group.
**Q59.** 12. There are 11 via direct parent links, plus E5011 reached via the E5167/E5005 duplicate.
**Q60.** E5145. It is not in the same group as the issuer E5133, which is in the Vesol group (E5132).
**Q61.** 20, which is approximate. There are 18 below investment grade through E5001, plus E5023 (B-) and E5047 (BB) reached via the duplicate. E5011 and E5035 were not checked.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1341","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E08","E10","E16","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},"Q9":{"count":389},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1347","E1348","E1350","E1351","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5170"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":75},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1028","E1039","E1101","E1126","E05","E1194","E1236","E15","E5012","E5047","E5091","E5116","E5124"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":87},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"A"},"Q48":{"count":119},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":59},"Q52":{"count":20},"Q53":{"same_group":"no"},"Q54":{"entities":["E5124","E5130"]},"Q55":{"count":23},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":20}}
```