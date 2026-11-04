**Q1.** A-. E01 was assigned A- on 2024-03-12 (A01) and not downgraded until 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB (A03, 2026-02-10); the downgrade was in 2025 (A02).

**Q3.** No. The 2031 note is I02, rated BB+ after the 2025-06-20 downgrade (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action is A09 (2025-09-15, A/POS), which supersedes A08.

**Q5.** The holder takes the credit risk of E02, the guarantor of I03, rated A (A09, A08).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12). The local-currency rating of BBB- (A13) is not capped. This question has no JSON field.

**Q7.** 37 non-test entities were downgraded in 2026 (listed in the JSON). They include E1057 and E1159, which were later withdrawn. I excluded the QA records and A5028, which is dated 2026-11-06, after today.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) and nothing has followed.

**Q9.** 376. This is a manual count of distinct LEIs with a non-QA issuer rating not ended by a withdrawal; it is the least certain figure here.

**Q10.** It depends on the basis. The foreign-currency rating is BB (A14), which is not investment grade, while the local-currency rating is BBB- (A13), which is.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and A35 on 2025-11-20 is only a watch.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1 time, in A36.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27). E17 has the same LEI and no actions.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33, A35).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17). Orrin Bancorp (E13) has a different LEI and no 2026 action.

**Q18.** 32 issuers had a Rating Watch Negative as the latest action on their rating series on 2026-10-01. The list includes E1019 and E1059, whose watches are on the local-currency series.

**Q19.** 45 issuers had Negative as the outlook on their latest action on 2026-10-01. E5033's downgrade (A5028) is dated after the cutoff.

**Q20.** No. A19 is a withdrawal "for commercial reasons"; the last rating was BB (A18), and there is no RD or D on E07.

**Q21.** 35 entities. All were withdrawn before 2026-10-01, with no later rating action.

**Q22.** E08 only, the only RD or D in the data (A22).

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 72 instruments. This counts instruments whose latest non-expected rating is BBB- or better; EX actions are not ratings in force.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42, I06).

**Q28.** BBB+ (A38, FC).

**Q29.** None. VD has only a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** 13 entities. Nine are domiciled in VD and rated BB (the ceiling is BB), and four are domiciled in CV and rated A (the ceiling is A).

**Q31.** No. No foreign-currency issuer rating exceeded the VD ceiling of BB or the CV ceiling of A.

**Q32.** E09 (E11 → E10 → E09).

**Q33.** The holder takes the credit risk of E10, the guarantor of I05. E10 is rated BBB+ (A27).

**Q34.** No. E12 has no parent, while E10 sits under E09.

**Q35.** 3 entities: E09, E10 and E11. E17 has the same LEI as E10.

**Q36.** 2 entities: E02 and E04. E03 has the same LEI as E02.

**Q37.** 497. That is 540 records, less 14 QA records and 29 duplicate-LEI records.

**Q38.** No. They have different LEIs.

**Q39.** A (A09 supersedes A08).

**Q40.** 79. This is a manual count of GB-domiciled entities with an issuer rating in force.

**Q41.** None. E16 is a QA test record, so its actions are not rating actions.

**Q42.** LU. The RESEARCH record E17 sets the domicile for the entity it shares with E10.

**Q43.** 1 entity (E10/E17).

**Q44.** Yes. I07 is denominated in XVD, Valdoria's domestic currency.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is local-currency, so its BBB- (A45) is not capped by the BB ceiling.

**Q46.** No. E11 has only a credit opinion (A46).

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating in force.

**Q48.** 113. That is 122 instruments less 9 that have only an expected rating.

**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 (same LEI as E5005) → E5002 → E5001.

**Q50.** 6 levels.

**Q51.** 58 entities (E5001–E5058; E5167 is a duplicate of E5005 and E5170 is a QA record).

**Q52.** 19 entities (E5086–E5104).

**Q53.** No. E5062's RATINGS record puts it under Belir Group (E5059); the parent shown on the RESEARCH record E5168 is not used.

**Q54.** E5106, E5124 and E5130. E5106 is VD-domiciled through its RESEARCH record E5169.

**Q55.** 31 rated entities have a VD-domiciled ancestor. The count is Cerid 6, Rotam 2, Wonod 9 (8 under E5106, 1 under E5124) and Geren 14.

**Q56.** BB-. This is E5144 (A5108).

**Q57.** E5002.

**Q58.** E5145. It guarantees I5007, issued by E5133, which belongs to the Vesol group.

**Q59.** 12 entities at the third level below the top.

**Q60.** The holder takes the credit risk of E5145, the guarantor. It is not in the same group as the issuer E5133.

**Q61.** 19 group members hold a foreign-currency issuer rating below investment grade.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1170","E1051","E1080","E1307","E1167","E5116","E5059","E1290","E1299","E1161","E1285","E1263","E1255","E1243","E1228","E1229","E1213","E1186","E1159","E1163","E1144","E1151","E1112","E1093","E1064","E1053","E1058","E1057","E1034","E1294","E1300","E5113","E5019","E5156","E5097"]},
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
"Q18":{"issuers":["E06","E1314","E1132","E1013","E1264","E1098","E1039","E1181","E1260","E1088","E1066","E1006","E1037","E1019","E1059","E1099","E1061","E1146","E1168","E1194","E1126","E1203","E1210","E1238","E1242","E1266","E1267","E1297","E1317","E1323","E1109","E1133"]},
"Q19":{"issuers":["E01","E09","E1056","E1079","E1190","E1046","E1072","E1080","E1118","E1034","E1055","E1161","E1282","E1300","E1158","E1262","E1263","E1294","E1248","E1064","E1005","E1029","E1228","E1211","E1188","E1060","E5039","E5050","E5059","E5062","E5020","E5023","E5013","E5019","E5057","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1308","E1316","E1320"]},
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