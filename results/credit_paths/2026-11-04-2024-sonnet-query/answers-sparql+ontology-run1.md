**Q1.** A-. E01's LTIDR was A- (A01, 2024-03-12) until it was downgraded to BBB on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action was an affirmation with a Negative outlook (A03), which is not a downgrade.

**Q3.** No, it is BB+. I02 is subordinated, and its rating was cut to BB+ by A07.

**Q4.** Positive. E02 and E03 share an LEI and are the same entity. The latest action is E03's affirmation, A09 (2025-09-15), with a POS outlook.

**Q5.** The holder takes E02's credit risk, since E02 guarantees I03. I03 is rated A (A11).

**Q6.** Not in the JSON. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB Country Ceiling for VD (A12) caps the foreign-currency rating, while the local-currency rating is not capped.

**Q7.** 38 issuers had a downgrade in 2026 (action DG on the issuer rating), listed in the JSON. They include E08, E10 and E5019.

**Q8.** E08 only, rated RD from 2026-07-08 (A22).

**Q9.** 377. This counts distinct LEIs (or IDs, for sovereigns) whose latest long-term issuer action on or before 2026-10-01 is not a withdrawal, excluding QA records.

**Q10.** Depends. E05 is BB on foreign currency (speculative) and BBB- on local currency (investment grade).

**Q11.** BBB+. E14 was downgraded by A36 on 2024-09-30.

**Q12.** A- (A34).

**Q13.** 1. Only A36 is a downgrade; the RW and AF actions are not.

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.

**Q15.** A- (A26). The downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. The rating stayed BBB+ throughout, and the later actions were a watch and an affirmation.

**Q17.** No. E06 only had a Rating Watch (A17), with the rating still A-.

**Q18.** 32 issuers, listed in the JSON. Their latest action on or before 2026-10-01 carries an RWN watch, including E06 and E1006.

**Q19.** 47 issuers, listed in the JSON. I excluded those whose latest action was a withdrawal. I also excluded E1132 and E1146, whose latest action is a watch with no outlook, though this is a judgement call.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** 36 entities, listed in the JSON. Each one's latest issuer action is a withdrawal, including E07. I left out E1106, which was withdrawn on local currency only and still has a foreign-currency rating.

**Q22.** Only E08. It is the only non-QA record with an RD or D rating.

**Q23.** F2 (A04).

**Q24.** Yes. E01's rating is BBB (A03).

**Q25.** 72. I counted instruments whose latest rating, ignoring withdrawn or expected-only ones, is BBB- or better. Of 113 rated instruments, 72 qualify.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** 13 entities, listed in the JSON. These are entities whose foreign-currency rating equals the ceiling: A for CV and BB for VD. Domicile follows the RESEARCH record where records disagree.

**Q31.** No. No entity's foreign-currency rating is above A in CV or above BB in VD.

**Q32.** E09. The chain is E11 to E10 to E09.

**Q33.** The holder takes E10's credit risk, since E10 guarantees I05. I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent and is not in the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 497, counting distinct LEIs (or IDs where there is no LEI) and excluding QA records.

**Q38.** No. Their LEIs differ.

**Q39.** A (A08 and A09).

**Q40.** 79. Country follows the RESEARCH record where records disagree.

**Q41.** None. E16 is a QA record, so it is ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile, although the RATINGS record E10 says DE.

**Q43.** 1. Only E17, which is the same entity as E10, is in LU.

**Q44.** Yes. I07 is in XVD, VD's domestic currency.

**Q45.** No. I07 is local-currency debt, so it is not capped by the ceiling.

**Q46.** No. E11 only has a credit opinion (A46), which is not a rating.

**Q47.** None. I08 only has an expected rating (A47), so it stays unrated.

**Q48.** 113 instruments held a rating on 2026-10-01.

**Q49.** E5001. The chain runs E5047, E5035, E5023, E5011, E5167 (the same entity as E5005), E5002, E5001.

**Q50.** 6 levels.

**Q51.** 58, counting by LEI so duplicate records are not double-counted.

**Q52.** 19. I excluded the Belir branch, because RESEARCH's parent link on E5168 conflicts with RATINGS, which holds for parent links.

**Q53.** No. E5062's RATINGS parent chain leads to E5059 (Belir Group), not Rotam.

**Q54.** E5106 and E5124 and E5130. E5106 is Wonod Steel BV, and its RESEARCH record E5169 places it in VD.

**Q55.** 31. These are rated entities that have at least one VD-domiciled entity above them in their chain of parents.

**Q56.** BB-, held by E5144.

**Q57.** E5002. E5011 reaches it via E5167 (the same entity as E5005), and E5013 reaches it via E5006.

**Q58.** E5145. It guarantees I5007, which was issued by E5133 in the Vesol group.

**Q59.** 12.

**Q60.** The holder takes E5145's credit risk. It is not in the same group as the issuer: E5133 belongs to the Vesol group and E5145 to the Geren group.

**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E08","E10","E5019","E5033","E5059","E5097","E5113","E5116","E5156"]},
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
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1194","E15","E5116","E1028","E1101","E1126","E05","E5012","E5047","E5091","E5124","E1236"]},
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