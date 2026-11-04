**Q1.** A-. Kestrel's foreign-currency LTIDR was A- from A01 (2024-03-12) until A02 downgraded it to BBB on 2025-06-20.

**Q2.** No. The only 2026 action on E01's issuer rating is A03, an affirmation at BBB with a Negative outlook.

**Q3.** No. The 2031 note I02 (subordinated) went from BBB (A23) to BB+ (A07, downgrade 2025-06-20).

**Q4.** Positive. E03 shares its LEI with E02, so they are one entity, and its latest action is A09 (2025-09-15, affirmed A, POS).

**Q5.** The guarantor, E02 (Northwind Holdings), whose current rating is A. I03 is issued by E04 but guaranteed by E02, and the latest action on E02/E03 is A09 (A).

**Q6.** The Valdoria country ceiling caps the foreign-currency rating. A12 sets the ceiling at BB, and E05's foreign-currency LTIDR is BB (A14), while the local-currency LTIDR is BBB- (A13).

**Q7.** 35 issuers (list in JSON). They have a 2026 downgrade (DG) on an issuer rating. I excluded QA test records and instrument downgrades such as A29. I also excluded A5028 (E5033), which is dated 2026-11-06, after today.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, and it was the only default rating in force on 1 Oct 2026.

**Q9.** About 377. I counted entities with an issuer rating in force on 1 Oct 2026, merging records that share a LEI and excluding withdrawn ratings, QA records, and entities with only credit opinions or ceilings. This was a manual tally, so treat it as approximate.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and nothing changed the rating until A35 (RW, 2025-11-20).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once, by A36.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10 and E17 share a LEI, and A26 (A-) held until A27 (2026-04-15).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 only changed the watch and affirmed it).

**Q17.** No. E06's only 2026 action, A17, places it on Rating Watch at A- and does not change the rating.

**Q18.** 32 issuers (list in JSON). Each has an in-force action carrying Rating Watch Negative (RWN) on 1 Oct 2026, with no later action resolving it.

**Q19.** 46 issuers (list in JSON). Each has a latest in-force action with a Negative outlook, and no later action replaces it.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and it was never rated RD or D.

**Q21.** 35 entities (list in JSON). Each had an issuer rating that was later withdrawn (WD) with no other basis still in force.

**Q22.** E08 only, via A22 (RD).

**Q23.** F2, from A04.

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 72. I counted instruments whose in-force rating on 1 Oct 2026 was BBB- or higher. Expected ratings (EX) are not in force.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling of BB (A12) and no LTIDR.

**Q30.** 12 entities (list in JSON). Each has a foreign-currency rating equal to its country's ceiling, which is BB for Valdoria and A for Corvenia. E5106 counts as VD-domiciled via its research duplicate E5169, but it is rated B-, so it is not in the list.

**Q31.** No. The foreign-currency ratings of the entities domiciled in VD and CV are at or below their ceilings.

**Q32.** E09. E11 → E10 → E09.

**Q33.** The guarantor, E10, which is rated BBB+ after A27.

**Q34.** No. E12 has no parent and is only similar in name.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 497. This is 540 rows, minus 14 QA records and 29 research duplicates sharing a LEI.

**Q38.** No. They have different LEIs, countries and types.

**Q39.** A (A09).

**Q40.** 79 distinct GB-domiciled issuers (manual tally).

**Q41.** None. E16 is a QA test record, so its actions are not treated as rating actions.

**Q42.** LU. The research record E17 says LU, and domicile follows research.

**Q43.** 1. E10 and E17 are one entity.

**Q44.** Yes. I07 is in XVD, which is Valdoria's domestic currency, and the issuer is domiciled in VD.

**Q45.** No. The ceiling applies to foreign-currency ratings, and this note is local-currency at BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46).

**Q47.** None. I08 has only an expected rating (A47, EX), which is not in force.

**Q48.** 113. This is 7 original, 99 of the I1xxx series and 7 of the I50xx series. The 8 instruments with only an EX action are excluded.

**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 (same LEI as E5005) → E5005 → E5002 → E5001.

**Q50.** 6 levels.

**Q51.** 58, which is E5001 to E5058. E5170 is a QA record and E5167 is a duplicate.

**Q52.** 19, which is E5086 to E5104. The research parent claim on E5168 is overridden by the RATINGS record.

**Q53.** No. Per the RATINGS records Belir Mining (E5062) sits under E5060 in the Belir group, and only a research duplicate (E5168) claims E5086 as parent.

**Q54.** E5106, E5124 and E5130. E5106 is VD-domiciled via its research duplicate E5169.

**Q55.** 31. These are rated entities with a VD-domiciled ancestor: 6 under Cerid, 2 under Rotam, 9 under Wonod and 14 under Geren.

**Q56.** BB-, held by E5144, the lowest among the rated Vesol members.

**Q57.** E5002. E5011's chain runs through E5005 and E5013's through E5006, and both meet at E5002.

**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the Vesol group. All other guarantees are within a group.

**Q59.** 12 entities at level 3, two under each of E5005 to E5010. E5011 counts under E5005 through the E5167 duplicate.

**Q60.** E5145 (Geren Group SA), the guarantor of I5007. It is not in the same group as the issuer E5133 (Vesol).

**Q61.** 19. These are the Cerid members whose current foreign-currency IDR is BB+ or below.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1170","E1051","E1080","E1307","E1167","E1299","E1161","E1163","E1159","E1034","E1112","E1053","E1057","E1058","E1064","E1093","E1263","E1285","E1144","E1213","E1228","E1243","E1255","E1294","E1300","E1290","E1186","E5019","E5097","E5116","E5113","E5059","E5156"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1079","E1046","E1029","E1080","E1056","E1072","E1118","E1190","E1211","E1248","E1262","E1271","E1282","E1188","E1294","E1300","E1263","E1228","E1034","E1064","E1158","E1005","E1055","E1105","E1060","E5020","E5013","E5019","E5023","E5039","E5050","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156"]},
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
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5124","E1039","E1194","E15","E5116"]},
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