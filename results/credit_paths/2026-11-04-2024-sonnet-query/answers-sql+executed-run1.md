**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).
**Q2.** No. The only 2026 action on E01 was an affirmation on 2026-02-10 (A03). It kept BBB and moved the outlook to Negative.
**Q3.** No. I02, the 2031 note, has been rated BB+ since 2025-06-20 (A07), which is sub-investment grade.
**Q4.** Positive. E02's current LTIDR is A with a POS outlook (A09).
**Q5.** The holder takes the risk of E02, the guarantor of I03, and the note is rated A (A11).
**Q6.** The Valdoria ceiling is BB (from 2025-04-01), and it caps E05's foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13).
**Q7.** 36 issuers had a rating cut in 2026; the IDs are in the JSON. I counted any lower LTIDR in 2026. A few DG-coded actions (E5116, and E1064/E1229/E1051 at some dates) show no rating drop, and three drops (E1064, E1290, E1307) are coded AF. The list may therefore not match the action codes exactly.
**Q8.** E08. Its rating became RD on 2026-07-08 (A22) and is still in force.
**Q9.** 377 distinct entities held a current non-withdrawn LTIDR.
**Q10.** Depends. E05's foreign-currency rating is BB (sub-investment grade) and its local-currency rating is BBB- (investment grade).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36).
**Q14.** None. E12's first rating began on 2024-02-01 (A30).
**Q15.** A- (A26).
**Q16.** No. The rating was BBB+ throughout; only the watch and outlook changed (A35, A33).
**Q17.** No. E06 stayed at A- and was only placed on Rating Watch Negative on 2026-09-03 (A17).
**Q18.** 32 issuers were on Rating Watch Negative; the IDs are in the JSON.
**Q19.** 47 issuers had a Negative outlook; the IDs are in the JSON.
**Q20.** Depends. E07's rating was withdrawn on 2026-05-12 (A19), and nothing in the data shows a default.
**Q21.** 35 entities; the IDs are in the JSON and include E07.
**Q22.** E08, which went CCC and then RD (A21, A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's LTIDR is BBB (A03).
**Q25.** 72 instruments held an investment-grade rating on 1 October 2026.
**Q26.** A+ (A40).
**Q27.** A- (A42, instrument I06).
**Q28.** BBB+ (A38).
**Q29.** None. The ratings table has no rows for VD.
**Q30.** 13 entities; the IDs are in the JSON. The ceilings are CV = A and VD = BB.
**Q31.** No. The ceilings are A for CV and BB for VD, and no company's foreign-currency rating exceeded its own country's ceiling in the list I checked.
**Q32.** E09.
**Q33.** The holder takes the risk of E10, the guarantor of I05, and the note is rated BBB+ (A29).
**Q34.** Yes. E12 is not in the E09 group (it has no parent), so it is not part of the same group as E10.

Correction to Q34: E12 has no parent and a different ultimate parent from E10, so the answer is **No**.

**Q35.** 3 entities: E09, E10 and E11.
**Q36.** 2 entities: E02 and E04.
**Q37.** 497 distinct entities, since merged duplicates are already collapsed.
**Q38.** No. E06 and E13 have different LEIs and countries and are separate records.
**Q39.** A, with a Positive outlook (A09).
**Q40.** 79 distinct GB-domiciled issuers held a current issuer rating.
**Q41.** None. No entity named Brindle appears in the data.
**Q42.** LU (E10).
**Q43.** 1 entity, E10.
**Q44.** Yes. I07 is flagged local_currency = yes and is denominated in XVD.
**Q45.** No. I07's BBB- is a local-currency rating, and the BB ceiling applies to foreign-currency ratings.
**Q46.** No. E11 has no rating rows.
**Q47.** None. I08 has no rating rows.
**Q48.** 113 instruments held a rating on 1 October 2026.
**Q49.** E5001.
**Q50.** 6 levels (E5047 to E5001 in the ancestors table).
**Q51.** 58 entities: 57 with E5001 as ultimate parent, plus E5001.
**Q52.** 19 entities: 18 plus E5086.
**Q53.** No. E5062 sits under E5059 and E5086 is its own group.
**Q54.** E5106, E5124 and E5130. The top entity E5105 is domiciled in FR.
**Q55.** 31 entities with a current issuer rating have a VD-domiciled ancestor.
**Q56.** BB-, held by E5144.
**Q57.** E5002.
**Q58.** E5145, which guarantees I5007, issued by E5133 in a different group.
**Q59.** 12 entities sit exactly three levels below E5001.
**Q60.** The holder takes the risk of E5145, the guarantor. It is not in the same group as the issuer E5133, which belongs to the Vesol group.
**Q61.** 19 members hold a foreign-currency issuer rating below investment grade, and the top entity E5001 is not among them.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E1057","E1169","E1112","E1051","E10","E5019","E1213","E1263","E1285","E1307","E1053","E1298","E5097","E1290","E1186","E1034","E1243","E1093","E1229","E1255","E5156","E1080","E1160","E1228","E1151","E1159","E1058","E5059","E1163","E1300","E1064","E1144","E1294","E5113","E1167"]},"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1039","E1059","E1266","E1037","E1209","E1242","E1317","E1181","E1006","E1019","E1264","E1099","E1132","E1260","E1267","E1109","E1168","E1066","E1146","E1203","E1314","E1323","E06","E1133","E1088","E1194","E1098","E1126","E1013","E1061","E1238","E1297"]},"Q19":{"issuers":["E1228","E1263","E5050","E5073","E5099","E1056","E1059","E1282","E5013","E5023","E5062","E1072","E1190","E5039","E5156","E1005","E1080","E5116","E1029","E1160","E5020","E5059","E1034","E1188","E1248","E5057","E1079","E01","E1064","E1118","E1261","E09","E1211","E5019","E5113","E5131","E1046","E1271","E1300","E5097","E5102","E1055","E1294","E5119","E5141","E1105","E1158"]},"Q20":{"in_default":"depends"},"Q21":{"entities":["E1206","E1219","E1320","E1041","E1063","E1107","E1138","E1140","E1062","E1200","E1225","E1233","E1234","E07","E1021","E1166","E1001","E1124","E1172","E1076","E1244","E1316","E1007","E1032","E1057","E1155","E1159","E1253","E1308","E1218","E1121","E1205","E1048","E1084","E1277"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236","E5012","E5047","E5091","E5116","E5124"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":497},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5124","E5130"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```