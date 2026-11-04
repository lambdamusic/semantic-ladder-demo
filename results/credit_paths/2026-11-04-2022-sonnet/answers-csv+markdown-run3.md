**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01) and not changed until the 2025-06-20 downgrade (A02).
**Q2.** No. The only 2026 action on E01 is an affirmation of BBB (A03).
**Q3.** No, BB+. The 2031 note is I02 (subordinated), downgraded to BB+ on 2025-06-20 (A07), which supersedes the earlier BBB (A23).
**Q4.** Positive. E03 shares E02's LEI, and its 2025-09-15 affirmation set POS (A09).
**Q5.** E02, rated A. I03 is guaranteed by E02 (A08, A09).
**Q6.** The Country Ceiling for VD is BB (A12), and it caps the FC rating. E05's FC rating is BB (A14) and its LC rating is BBB- (A13).
**Q7.** 35 entities had a 2026 downgrade (list in JSON). I excluded QA records and A5028 (E5033), which is dated 2026-11-06, after today.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22).
**Q9.** 376. This counts distinct LEIs with an LTIDR in force on 2026-10-01 and excludes QA records. Where a withdrawal is dated earlier than a later action (E1115, E1158, E1303), I followed the latest date.
**Q10.** Depends. The FC rating is BB (speculative) and the LC rating is BBB- (investment grade).
**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).
**Q12.** A-. It was assigned on 2023-01-15 (A34).
**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 an affirmation.
**Q14.** None. E12 was first rated on 2024-02-01 (A30).
**Q15.** A-. E10 and E17 share an LEI, and the downgrade to BBB+ came only on 2026-04-15 (A27).
**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).
**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.
**Q18.** 31 entities, listed in JSON. Each has a latest action that is a watch with RWN. E1059 and E1019 are on watch for their LC ratings only.
**Q19.** 45 entities, listed in JSON. Each has a latest action with a NEG outlook. Entities whose latest action is a watch carry no outlook, so I excluded them (E1132, E1146).
**Q20.** No. E07 was rated BB and then withdrawn (A18, A19). A withdrawal is not a default.
**Q21.** 35 entities, listed in JSON. Each had an LTIDR that was later withdrawn, with no other basis left in force; the research-only records are given by their RATINGS twin.
**Q22.** E08. It is the only entity ever rated RD or D (A22).
**Q23.** F2 (A04).
**Q24.** Yes. The FC rating is BBB (A03).
**Q25.** 72. Of the 122 instruments, 113 held a rating and 72 of those were rated BBB- or higher.
**Q26.** A+ (A40).
**Q27.** A- (I06, A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.
**Q30.** 13 entities (listed in JSON). The VD ceiling is BB and the CV ceiling is A. The list includes E5106's neighbours only where the RESEARCH domicile applies, so E1245 (research: FR) is not counted.
**Q31.** No. No VD entity has an FC rating above BB and no CV entity has one above A.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ (A27).
**Q34.** No. E12 has no parent, while E10 sits under E09.
**Q35.** 3: E09, E10 and E11. E17 is E10's duplicate record.
**Q36.** 2: E02 and E04. E03 is a duplicate of E02.
**Q37.** 497. This is 540 records, less 14 QA records and 29 duplicate LEI records. The two sovereigns have no LEI and are counted as entities.
**Q38.** No. They have different LEIs (E06 and E13).
**Q39.** A (A09).
**Q40.** 79. These are GB-domiciled entities with an LTIDR in force on 2026-10-01, and no GB record has a RESEARCH override.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile.
**Q43.** 1. It is the single entity E10/E17.
**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and E05 is domiciled in VD.
**Q45.** No. The ceiling does not apply to local-currency debt, so the BBB- rating (A45) is not capped.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an expected rating (A47), not an assigned one.
**Q48.** 113. Nine instruments have only an expected rating or none: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.
**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5005 → E5002 → E5001.
**Q50.** 6.
**Q51.** 58, from E5001 to E5058. E5011 joins via E5167, the RESEARCH record of E5005.
**Q52.** 19, from E5086 to E5104.
**Q53.** No. The link from E5168 to E5086 is on a RESEARCH record, but RATINGS holds the parent links and puts Belir Mining under E5060.
**Q54.** E5106, E5124 and E5130. E5106 is VD per the RESEARCH record E5169.
**Q55.** 31. Rated entities with a VD-domiciled strict ancestor: Cerid 6, Rotam 2, Wonod 8 plus E5130, and Geren 14.
**Q56.** BB-. The lowest is E5144 (A5108).
**Q57.** E5002.
**Q58.** E5145. It guarantees I5007, issued by E5133, which sits in the Vesol group.
**Q59.** 12.
**Q60.** E5145. It is not in the same group as the issuer E5133, which is in the Vesol group.
**Q61.** 19.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1169","E1051","E1080","E1307","E1167","E1298","E1160","E5156","E5116","E5059","E1285","E1263","E1290","E1294","E1228","E1229","E1243","E1300","E1093","E1112","E1064","E1053","E1058","E1057","E1159","E1163","E1186","E1144","E1213","E1255","E5113","E5097","E5019"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":376},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1098","E1006","E1238","E1059","E1297","E1109","E1314","E1266","E1242","E1260","E1267","E1264","E1181","E1168","E1099","E1088","E1061","E1037","E1039","E1019","E1194","E1203","E1209","E1132","E1133","E1317","E1146","E1013","E1126","E1066"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300","E5013","E5019","E5020","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
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