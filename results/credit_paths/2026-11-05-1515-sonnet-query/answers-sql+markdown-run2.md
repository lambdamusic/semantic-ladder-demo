**Q1.** A-. E01's last action before 2025-01-01 is A01 (assigned A- on 2024-03-12); the downgrade A02 only came on 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations; A03 changed the outlook to NEG, not the rating.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), downgraded to BB+ in A07.

**Q4.** POS. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) set the outlook to POS.

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, rated A. I03 is guaranteed by E02, whose latest rating is A (A09).

**Q6.** The data gives no stated reason, but it is consistent with the Country Ceiling. VD's ceiling is BB (A12), and E05's FC rating is BB (A14), against LC at BBB- (A13).

**Q7.** 38 issuers had a downgrade action in 2026; the IDs are in the JSON. E5033's downgrade is dated 2026-11-06, which is after today's date, but I counted it.

**Q8.** E08 (Saxby Shipping). It went to RD on 2026-07-08 (A22), and RD counts as default.

**Q9.** 377. This is the number of distinct entities, merged by LEI and excluding QA, whose latest issuer rating on 2026-10-01 is not a withdrawal.

**Q10.** Depends. E05's LC rating is BBB- (investment grade) but its FC rating is BB (speculative grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action, A35, is only a Watch placement.

**Q12.** A-. A34 assigned A- on 2023-01-15, and no change came before 2024-01-01.

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10's A26 holds until A27 on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33 is an affirmation).

**Q17.** No. E06 only had a Watch placement (A17), which is not a downgrade.

**Q18.** 32 issuers were on RWN on 2026-10-01, including E06; the IDs are in the JSON.

**Q19.** 47 issuers had a NEG outlook on 2026-10-01, including E01 and E09; the IDs are in the JSON.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** 35 entities, including E07, whose latest issuer-rating action by 2026-10-01 is a withdrawal; the IDs are in the JSON.

**Q22.** Only E08 (A22, RD).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB.

**Q25.** 72 instruments held an investment-grade rating on 2026-10-01, excluding EX-only ratings.

**Q26.** A+ (A40).

**Q27.** A-. I06 was assigned A- in A42.

**Q28.** BBB+ (A38).

**Q29.** None. The record VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 13 entities had an FC rating equal to their country's ceiling; the IDs are in the JSON.

**Q31.** No. No FC rating exceeded its country's ceiling (A for CV, BB for VD).

**Q32.** E09.

**Q33.** The holder takes the credit risk of E10, Halden Bank, rated BBB+. I05 is guaranteed by E10, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent link, so it is outside the E09 group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 497 distinct LEIs or records, excluding QA.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A, per A09 on E03 (same LEI as E02).

**Q40.** 79. These are distinct GB-domiciled issuers, using RESEARCH country where records disagree.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding the DE on E10.

**Q43.** 1.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an expected rating (A47, EX), so it is unrated.

**Q48.** 113 instruments held a rating on 2026-10-01.

**Q49.** E5001.

**Q50.** 6 levels. The chain is E5035, E5023, E5011, E5005, E5002, E5001.

**Q51.** 58.

**Q52.** 19.

**Q53.** No. Belir Mining (E5062) sits under E5059, a different tree from Rotam (E5086).

**Q54.** E5106, E5130 and E5124.

**Q55.** 31 entities.

**Q56.** BB-, held by E5144.

**Q57.** E5002. It is the nearest shared ancestor of E5011 and E5013.

**Q58.** E5145, which guarantees I5007 issued by E5133 in another group.

**Q59.** 12.

**Q60.** The holder takes the credit risk of E5145, which is not in the same group as the issuer E5133.

**Q61.** 19.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1059","E1266","E1039","E1013","E1297","E1238","E1061","E1099","E1132","E1260","E1267","E1098","E1126","E1019","E1006","E1264","E1194","E1088","E1133","E06","E1317","E1242","E1037","E1209","E1168","E1109","E1181","E1146","E1203","E1066","E1314","E1323"]},
"Q19":{"issuers":["E1034","E1188","E5057","E1248","E1064","E1261","E01","E1118","E1079","E1080","E1005","E5116","E1190","E1072","E5156","E5039","E1158","E1105","E5073","E5099","E1263","E1228","E5050","E5020","E1029","E5059","E1160","E5019","E5113","E1211","E5131","E09","E1271","E1046","E1300","E5102","E5097","E1055","E1294","E5119","E5141","E1059","E5062","E5013","E5023","E1056","E1282"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1206","E1320","E1219","E1062","E1218","E1032","E1159","E1057","E1155","E1253","E1007","E1308","E1048","E1084","E1138","E1041","E1063","E1107","E1140","E1277","E1076","E1225","E1233","E1234","E1200","E1001","E1172","E1124","E1316","E1244","E1021","E07","E1166","E1205","E1121"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1039","E1101","E1126","E1194","E1236","E15","E5012","E5047","E5091","E5116","E5124"]},
"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":497},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":79},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":58},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5106","E5130","E5124"]},"Q55":{"count":31},"Q56":{"rating":"BB-"},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":12},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":19}}
```