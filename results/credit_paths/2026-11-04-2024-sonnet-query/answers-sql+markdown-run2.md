**Q1.** A-. E01's FC LTIDR was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.
**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations (A03 revised the outlook to NEG, which is not a downgrade).
**Q3.** No, BB+. I02 is subordinated and was downgraded to BB+ by A07 on 2025-06-20.
**Q4.** POS. E02 and E03 share an LEI, so they are one entity, and its latest action is A09 (2025-09-15, AF, POS).
**Q5.** The holder takes E02's credit risk (Northwind Holdings), because I03 is guaranteed by E02. I03 is rated A (A11), in line with E02's A.
**Q6.** Valdoria's Country Ceiling (A12) is BB and caps FC ratings (E05 FC is BB, A14). The LC rating, BBB- (A13), is not capped.
**Q7.** 38 issuers (LTIDR downgrades dated 2026, per the list in the JSON below). This includes E5033, whose downgrade A5028 is dated 2026-11-06, after today's date of 2026-11-04.
**Q8.** E08. A22 (2026-07-08) took it to RD, a default.
**Q9.** 377 distinct entities held a non-withdrawn LTIDR on 1 Oct 2026, after merging records that share an LEI and excluding QA records.
**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade).
**Q11.** BBB+. E14 was downgraded by A36 on 2024-09-30 and nothing changed it before 1 June 2025.
**Q12.** A-. A34 (2023-01-15) set it and it was unchanged on 2024-01-01.
**Q13.** 1, from A36.
**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.
**Q15.** A-. E10's A26 holds until A27 on 2026-04-15.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 was a Watch, A33 an affirmation).
**Q17.** No. E06's only 2026 action, A17, is a Rating Watch.
**Q18.** 32 issuers had a latest action carrying RWN on 1 Oct 2026 (list in JSON).
**Q19.** 49 issuers had a Negative outlook on 1 Oct 2026, carrying the outlook through RW actions that leave it blank and excluding withdrawn entities (list in JSON).
**Q20.** No. E07's A19 is a withdrawal for commercial reasons, not a default.
**Q21.** 35 entities (list in JSON).
**Q22.** E08 only (RD via A22).
**Q23.** F2 (A04).
**Q24.** Yes, BBB (A03).
**Q25.** 72 of the 113 instruments rated on 1 Oct 2026 were investment grade.
**Q26.** A+ (A40).
**Q27.** A- (A42). I06 is subordinated, and the issuer's FC rating of A is not the instrument rating.
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not a rating.
**Q30.** 13 entities had a FC rating exactly equal to their country's ceiling, which is A for CV and BB for VD (list in JSON).
**Q31.** No. No entity domiciled in CV or VD has a FC rating above its ceiling.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** The holder takes E10's credit risk (Halden Bank), because I05 is guaranteed by E10. I05 is rated BBB+ (A29), the same as E10 after A27.
**Q34.** No. E12 has no parent and is not linked to E09.
**Q35.** 3 (E09, E10, E11). E17 is a second record of E10.
**Q36.** 2 (E02, E04). E03 is a second record of E02.
**Q37.** 497 distinct legal entities, after merging records that share an LEI and excluding QA records.
**Q38.** No. They have different LEIs.
**Q39.** A. E02 and E03 are one entity, and its latest action, A09, affirmed A.
**Q40.** 79.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile.
**Q43.** 1 (E10).
**Q44.** Yes. I07 pays in XVD, VD's domestic currency.
**Q45.** No. It is local-currency debt, so the ceiling does not apply.
**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), not an assigned rating.
**Q48.** 113.
**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 (same entity as E5005) → E5002 → E5001.
**Q50.** 6.
**Q51.** 58.
**Q52.** 19.
**Q53.** No. RATINGS holds the parent links, so Belir Mining sits under E5060 and E5059 (Belir Group). The RESEARCH record E5168 pointing to E5086 is overridden.
**Q54.** E5106, E5124 and E5130. The RESEARCH record E5169 puts E5106 in VD.
**Q55.** 31.
**Q56.** BB- (E5144).
**Q57.** E5002.
**Q58.** E5145. It guarantees I5007, which E5133 (Vesol group) issued.
**Q59.** 12.
**Q60.** The holder takes E5145's credit risk (Geren Group). It is not in the same group as the issuer E5133, which belongs to the Vesol group.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1294","E1151","E1053","E1144","E5019","E1159","E1057","E1243","E5113","E1167","E1058","E1080","E5116","E1290","E1285","E1034","E1051","E1064","E1093","E08","E1169","E1186","E1112","E1307","E1229","E1298","E1263","E1255","E5033","E1228","E5156","E10","E5059","E1160","E5097","E1163","E1213","E1300"]},
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
"Q18":{"issuers":["E1059","E1109","E1168","E1194","E1209","E1242","E06","E1039","E1088","E1098","E1146","E1013","E1061","E1126","E1133","E1317","E1019","E1037","E1203","E1267","E1006","E1297","E1099","E1260","E1132","E1181","E1323","E1238","E1066","E1314","E1264","E1266"]},
"Q19":{"issuers":["E1211","E5023","E5102","E1005","E1271","E5097","E1055","E1079","E1158","E1261","E5013","E5156","E1029","E1188","E1294","E5062","E1228","E1282","E1300","E5099","E1064","E5057","E5073","E09","E1046","E5020","E5050","E5131","E01","E1132","E1059","E5019","E5059","E5141","E1248","E1263","E1034","E1118","E1190","E5039","E5113","E5119","E1056","E1072","E1080","E1146","E1105","E1160","E5116"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1219","E1206","E1320","E1218","E1253","E1155","E1032","E1007","E1308","E1057","E1159","E1225","E1200","E1234","E1233","E1277","E1048","E1084","E1172","E1124","E1001","E1140","E1041","E1107","E1063","E1138","E1062","E1121","E1205","E1316","E1244","E07","E1021","E1166","E1076"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes","rating":"BBB"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15","E1028","E1039","E1101","E1126","E1194","E1236","E5012","E5047","E5091","E5116","E5124"]},
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