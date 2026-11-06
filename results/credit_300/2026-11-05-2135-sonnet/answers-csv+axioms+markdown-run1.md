**Q1.** A-. E01's last action on or before 2025-01-01 was A01 (assigned A-, 2024-03-12); the downgrade A02 came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook, which is not a downgrade.

**Q3.** No, BB+. The 2031 note is I02 (subordinated), downgraded to BB+ by A07.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (2025-09-15, A, POS).

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes E02's credit risk, and E02's current rating is A (A09).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling. E05's FC rating is BB (A14), equal to VD's ceiling (A12), while its LC rating is BBB- (A13) and is not capped.

**Q7.** Thirty-one entities had a downgrade (DG) in 2026; they are listed in the JSON. I counted only issuer-rating downgrades, named duplicates by their RATINGS record, and ignored QA records.

**Q8.** E08. A22 took it to RD on 2026-07-08, and no other entity has an RD or D rating.

**Q9.** 278. This counts distinct LEIs with an issuer rating in force on 2026-10-01 and not withdrawn. I counted E1279, whose LC rating survives its FC withdrawal, and E1158, E1115 and E1303, which were re-rated after a withdrawal.

**Q10.** Depends. E05 is BB on foreign currency (A14, speculative) but BBB- on local currency (A13, investment grade).

**Q11.** BBB+. E14 was downgraded to BBB+ by A36 on 2024-09-30, and nothing changed it before 2025-06-01.

**Q12.** A-, from A34 (assigned 2023-01-15), since the downgrade A36 came later.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** None. E12's first rating action is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- (A26) and downgraded to BBB+ only on 2026-04-15 (A27).

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 and A33 did not change the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement, and E13 (Orrin Bancorp) is a different entity.

**Q18.** Thirty-one entities, listed in the JSON, have a Rating Watch Negative as their latest action on 2026-10-01. For E1019 and E1059 the watch is on the local-currency rating only.

**Q19.** Twenty-three entities, listed in the JSON, had a Negative outlook on their latest action. Entities whose latest action was a Watch placement, which carries no outlook, are excluded.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** Thirty-five entities, listed in the JSON, were rated at some point but had no issuer rating on 2026-10-01, because a withdrawal was their latest action.

**Q22.** E08 only. It is the only entity ever rated RD or D (A22).

**Q23.** F2, from A04.

**Q24.** Yes. E01's current LTIDR is BBB (A03).

**Q25.** 66. I counted instruments whose latest INST action is an assigned or in-force rating of BBB- or better; expected ratings (EX) do not count.

**Q26.** A+, from A40.

**Q27.** A-, from A42 (I06).

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** Eight entities. E05, E1028, E1101, E1126 and E1236 sit at VD's BB ceiling, and E15, E1039 and E1194 sit at CV's A ceiling.

**Q31.** No. Every VD-domiciled company's FC rating is at or below BB, and every CV-domiciled company's is at or below A.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ (A27).

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3. The group is E09, E10 (E17 is the same entity) and E11.

**Q36.** 2. The group is E02 (E03 is the same entity) and E04.

**Q37.** 331. There are 357 non-QA records, of which 26 are RESEARCH duplicates sharing an LEI with another record.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09.

**Q40.** 66. This counts distinct GB-domiciled entities holding an issuer rating on 2026-10-01 (domicile taken from RESEARCH records).

**Q41.** None. E16 is a QA test record, so its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds domicile for the entity it shares with E10.

**Q43.** 1, namely E10, through its RESEARCH record E17.

**Q44.** Yes. I07 pays in XVD, VD's domestic currency, and the issuer E05 is domiciled in VD.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not yet a rating.

**Q48.** 106. Of the 115 instruments, I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049 have only EX actions.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1064","E1058","E1163","E1213","E1307","E1228","E1186","E1034","E1159","E1160","E1169","E1167","E1263","E1285","E1112","E1080","E1093","E1300","E1294","E1298","E1255","E1243","E1229","E1057","E1053","E1144","E1290","E1051","E1151"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":278},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1267","E1242","E1039","E1088","E1194","E1203","E1133","E1006","E1109","E1099","E1168","E1019","E1260","E1264","E1013","E1037","E1061","E1066","E1059","E1146","E1098","E1209","E1266","E1297","E1317","E1323","E1238","E1181","E1314","E1126"]},
"Q19":{"issuers":["E01","E09","E1118","E1158","E1079","E1228","E1029","E1046","E1056","E1064","E1190","E1271","E1261","E1263","E1034","E1294","E1300","E1282","E1160","E1005","E1080","E1211","E1072"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":331},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":66},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```