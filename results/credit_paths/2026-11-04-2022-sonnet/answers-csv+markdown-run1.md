**Q1.** A-. A01 (2024-03-12) set A- and the next action, A02, is dated 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated); its latest action, A07 (2025-06-20), downgraded it to BB+.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes E02's (Northwind Holdings) credit risk, rated A. I03 is issued by E04 but guaranteed by E02, whose FC rating is A (A08, A09).

**Q6.** E05's FC rating is capped by Valdoria's Country Ceiling of BB (A12), so FC is BB (A14). The LC rating of BBB- (A13) is not capped.

**Q7.** 38 issuers received a downgrade (DG) action dated in 2026, listed in the JSON. RESEARCH-record actions are mapped to the RATINGS record of the same LEI, QA records are ignored, and A5028 (2026-11-06) is included because it is dated 2026.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, which is a default.

**Q9.** 377. This counts distinct LEIs (CV included) whose latest issuer-rating action by date is not a withdrawal, excluding QA records. E1115, E1158 and E1303 are counted because later-dated actions follow their withdrawals; E1106 and E1279 keep one currency basis.

**Q10.** No. The headline FC rating is BB (A14), although the LC rating is BBB- (A13).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+ and it held through 2025-06-01.

**Q12.** A-. A34 (2023-01-15) assigned A- and the downgrade came later.

**Q13.** 1. Only A36 is a DG on E14.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. E17 is E10's duplicate (same LEI), and A26 held A- until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35 and A33 did not change it).

**Q17.** No. E06's only 2026 action, A17, is a Rating Watch placement with the rating unchanged at A-.

**Q18.** 31 issuers, listed in the JSON, are on RWN: those whose latest action on a rating is a Rating Watch with no later action by 2026-10-01.

**Q19.** 44 issuers, listed in the JSON, have a Negative outlook. The test is that the latest action on the rating by 2026-10-01 carries a NEG outlook; a later Rating Watch action (blank outlook) counts as no outlook.

**Q20.** No. E07 was assigned BB (A18) and then withdrawn (A19), which is not a default.

**Q21.** 35 entities had a rating that was later withdrawn, with no later-dated action, by 2026-10-01 (see JSON).

**Q22.** Only E08, which reached RD in A22.

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. Its LTIDR is BBB (A03).

**Q25.** 72. Of the 113 instruments with an INST rating in force on 2026-10-01, 72 are BBB- or better; expected (EX) ratings are not counted.

**Q26.** A+ (A40).

**Q27.** A-. I06 has its own rating of A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12), not an issuer rating.

**Q30.** 13 entities have an FC rating exactly at their ceiling (see JSON): nine in VD (ceiling BB) and four in CV (ceiling A). Domicile follows the RESEARCH record; this excludes E1245, which RESEARCH places in FR.

**Q31.** No. No VD or CV entity has an FC rating above its ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's (Halden Bank) credit risk, rated BBB+. I05 is guaranteed by E10, whose latest rating is A27's BBB+.

**Q34.** No. E12 has no parent, while E10 sits under E09.

**Q35.** 3 (E09, E10, E11). E17 is the same entity as E10.

**Q36.** 2 (E02 and E04). E03 is the same entity as E02.

**Q37.** 497. This is 16 core entities, 315 in the E1xxx range and 166 in the E5xxx range, after merging same-LEI duplicates and dropping QA records.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 79 GB-domiciled issuers hold an issuer rating, counting by LEI and applying the RESEARCH country; E10 is therefore not GB.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH holds domicile (E17) and overrides E10's DE.

**Q43.** 1 (E10/E17).

**Q44.** Yes. I07 is in XVD, which is the domestic currency of E05's country, VD.

**Q45.** No. Local-currency debt is not capped by the Country Ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX).

**Q48.** 113. Of the 120 instruments, seven have only expected ratings (I08, I1001, I1007, I1008, I1012, I1015, I1021) and I1046 and I1049 also have only EX, so I count 113 with an assigned rating.

**Q49.** E5001. Following parent links from E5047 gives E5035, E5023, E5011, then E5167, which is the same entity as E5005, then E5002 and E5001.

**Q50.** 6. The levels are E5035, E5023, E5011, E5005, E5002, E5001.

**Q51.** 58 (E5001 to E5058). E5011 joins through E5167, which is E5005; the E5170 test record is ignored.

**Q52.** 19 (E5086 to E5104).

**Q53.** No. RATINGS holds parent links, so Belir Mining E5062 sits under E5060 and E5059, not under Rotam; the E5168 research link is ignored.

**Q54.** E5106, E5124 and E5130. RESEARCH places Wonod Steel BV (E5169, same LEI as E5106) in VD.

**Q55.** 31. VD-domiciled ancestors sit under Cerid (E5005), Wonod (E5106 and E5124), Rotam (E5091) and Geren (E5145); the 31 rated descendants are 6, 9, 2 and 14 respectively.

**Q56.** BB-. Vesol ratings run from A+ to E5144's BB- (A5108), the lowest.

**Q57.** E5002. E5011 reaches it via E5167/E5005 and E5013 reaches it via E5006.

**Q58.** E5145. It guarantees I5007, whose issuer E5133 belongs to the Vesol group; every other guarantee stays within its own group.

**Q59.** 12. These are the children of E5005 to E5010, including E5011 via E5167.

**Q60.** The holder takes E5145's (Geren Group SA) credit risk, and E5145 is not in the issuer's group. I5007's issuer E5133 is in the Vesol group, while its guarantor E5145 is a separate ultimate parent.

**Q61.** 19 Cerid group members hold an FC rating of BB+ or lower, based on their latest actions.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1169","E1051","E1080","E1307","E1167","E1298","E1160","E5156","E5116","E5059","E1053","E1058","E1285","E1294","E1263","E1290","E1186","E1159","E1163","E1144","E1228","E1229","E1213","E1112","E1093","E5113","E5019","E5033","E1064","E1243","E1255","E1300","E1151","E5097","E1057","E1034"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":377},
"Q10":{"investment_grade":"no"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1264","E1098","E1061","E1209","E1181","E1019","E1059","E1037","E1039","E1006","E1013","E1088","E1099","E1109","E1132","E1133","E1146","E1260","E1267","E1266","E1242","E1203","E1194","E1168","E1317","E1314","E1323","E1297","E1238","E1066"]},
"Q19":{"issuers":["E01","E09","E1056","E1046","E1079","E1080","E1118","E1190","E1211","E1282","E1294","E1300","E1263","E1248","E1228","E1005","E1029","E1072","E1105","E1188","E1261","E1059","E1034","E1064","E1158","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124","E15","E1039","E1194","E5116"]},
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