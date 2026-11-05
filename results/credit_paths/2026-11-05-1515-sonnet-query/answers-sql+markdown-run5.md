**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.
**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04. A03 revised the outlook to NEG but did not change the rating.
**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), and its latest action A07 rated it BB+.
**Q4.** Positive (POS). E02 and E03 share an LEI, so they are one entity, and its latest action is A09 (2025-09-15, POS).
**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is guaranteed by E02, and I03 is rated A (A11).
**Q6.** The data doesn't state a reason. It is consistent with VD's Country Ceiling of BB (A12) capping the foreign-currency rating at BB (A14), while the local-currency rating of BBB- (A13) is not capped.
**Q7.** 38 issuers had a long-term rating downgrade in 2026 (full list in the JSON). The query counted DG actions dated anywhere in 2026, including after today.
**Q8.** E08. Its RD from A22 (2026-07-08) is a default.
**Q9.** 377. This counts distinct LEIs whose latest long-term rating on 1 Oct 2026 was not a withdrawal, with QA records excluded.
**Q10.** Depends. E05 is BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13), which is investment grade.
**Q11.** BBB+. A36 (2024-09-30) set it, and the later RW A35 did not change it.
**Q12.** A-. This is A34, since the downgrade came later.
**Q13.** 1. The only downgrade is A36.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. A26 applies until the downgrade A27 on 2026-04-15, and the E17 record shares E10's LEI.
**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33).
**Q17.** No. E06's only 2026 action is the Watch A17, which is not a downgrade.
**Q18.** 32 issuers were on Rating Watch Negative (list in the JSON). It includes E06 (A17).
**Q19.** 49 issuers had a Negative outlook (list in the JSON), including E01 (A03) and E09 (A25).
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.
**Q21.** 35 entities (list in the JSON), including E07.
**Q22.** E08 only.
**Q23.** F2, from A04.
**Q24.** Yes. E01 is BBB (A03).
**Q25.** 72. This is the number of instruments whose latest non-EX rating on 1 Oct 2026 was BBB- or better.
**Q26.** A+ (A40).
**Q27.** A- (A42). It is below the CV ceiling of A (A37).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** 13 entities (list in the JSON), including E15 and E05, whose foreign-currency ratings equal their country's ceiling.
**Q31.** No. No non-sovereign had a foreign-currency rating above its ceiling.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** The holder takes Halden Bank's credit risk (E10), rated BBB+. I05 is guaranteed by E10, and both E10 (A27) and I05 (A29) are BBB+.
**Q34.** No. E12 has no parent, while E10 belongs to the E09 group.
**Q35.** 3.
**Q36.** 2.
**Q37.** 497. This counts distinct LEIs or IDs across non-QA records.
**Q38.** No. Their LEIs differ (E06 and E13).
**Q39.** A (A09, for the merged E02/E03 entity).
**Q40.** 79. This counts GB-domiciled LEIs with a long-term issuer rating that was not withdrawn on 1 Oct 2026, using the RESEARCH country where records disagree.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile.
**Q43.** 1.
**Q44.** Yes. I07 is in XVD, the domestic currency of VD.
**Q45.** No. It is local-currency debt, so the ceiling does not apply. It is rated BBB- (A45).
**Q46.** No. E11 has only a Credit Opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), which is not yet a rating.
**Q48.** 113.
**Q49.** E5001.
**Q50.** 6.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. Belir Mining's chain ends at E5059, and Rotam Group (E5086) is a different top entity.
**Q54.** E5106, E5124, E5130.
**Q55.** 31.
**Q56.** BB-, held by E5144.
**Q57.** E5002 (Cerid Energy plc). It is 2 levels above E5011, and E5001 is the next common ancestor.
**Q58.** E5145, which guarantees I5007, issued by E5133.
**Q59.** 12.
**Q60.** The holder takes Geren Group's credit risk (E5145, guarantor of I5007). It is not in the same group as the issuer E5133, which belongs to the Vesol group.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1294","E1151","E1093","E1064","E1112","E08","E1169","E1186","E5019","E5113","E1053","E1144","E1243","E1159","E1057","E5156","E1285","E1290","E5116","E1080","E1058","E1167","E1213","E1163","E5097","E1300","E1229","E1255","E1263","E1228","E1298","E1307","E5033","E10","E5059","E1160"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":377},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1039","E1098","E1099","E1181","E1088","E1297","E1066","E1238","E1168","E1260","E1061","E1019","E1264","E1146","E1194","E1037","E1132","E1109","E1314","E1126","E1317","E1267","E1203","E1209","E1323","E1266","E1059","E1013","E1242","E1133","E06","E1006"]},
"Q19":{"issuers":["E5019","E1261","E5099","E09","E5023","E5116","E1046","E5013","E01","E1064","E1300","E1005","E1188","E1282","E5050","E1056","E5156","E1211","E5119","E5057","E1072","E5097","E5141","E5020","E5073","E1034","E1118","E5039","E1059","E5102","E1029","E5062","E1146","E5113","E1294","E5131","E1079","E5059","E1105","E1190","E1055","E1271","E1080","E1160","E1228","E1158","E1132","E1263","E1248"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1316","E1244","E1032","E1159","E1057","E1155","E1253","E1007","E1308","E1206","E1320","E1219","E1218","E1225","E1233","E1234","E1200","E1021","E07","E1166","E1048","E1084","E1062","E1205","E1121","E1138","E1041","E1063","E1107","E1140","E1076","E1277","E1001","E1172","E1124"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E15","E1028","E1194","E1101","E1236","E5116","E1126","E5091","E05","E5012","E5047","E5124"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":497},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":79},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":58},
"Q52":{"count":19},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106","E5124","E5130"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":19}
}
```