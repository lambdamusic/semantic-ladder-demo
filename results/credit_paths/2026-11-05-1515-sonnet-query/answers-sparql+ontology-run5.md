**Q1.** A-. E01's last action on or before 2025-01-01 was A01 (A-, 2024-03-12); the downgrade to BBB came later, on 2025-06-20.

**Q2.** No. E01's only 2026 action, A03 (2026-02-10), is an affirmation (BBB, outlook Negative), which is not a downgrade.

**Q3.** No. The 2031 note (I02, subordinated) was downgraded to BB+ on 2025-06-20, which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15, A, POS).

**Q5.** The holder takes the credit risk of E02, the guarantor of I03. I03 is rated A.

**Q6.** The Valdoria Country Ceiling is BB (A12). It caps the foreign-currency rating (BB, A14) but not the local-currency rating (BBB-, A13).

**Q7.** Incomplete: the output was truncated, so this is only the visible part. It lists entities with a long-term downgrade in 2026, starting with E08 (A21, A22) and E10 (A27).

**Q8.** E08, rated RD since 2026-07-08 (A22). The output was truncated, so this may be incomplete.

**Q9.** 377 distinct issuers, counted by LEI, excluding QA records and withdrawn ratings.

**Q10.** Depends. Its foreign-currency rating is BB (speculative grade) and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A DG on 2024-09-30 set BBB+, and the next action was 2025-11-20.

**Q12.** A-. This was set on 2023-01-15 (E14).

**Q13.** 1. The only downgrade is 2024-09-30 (E14); the Rating Watch and the affirmation are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01.

**Q15.** A-. E10 held A- (A26) until the 2026-04-15 downgrade. E17 has the same LEI and no actions.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now; the Watch and affirmation did not change it.

**Q17.** No. E06 only had a Rating Watch (A17). Orrin Bancorp (E13) is a different entity with a different LEI.

**Q18.** Incomplete: the output was truncated, so these are only the visible entities on Rating Watch Negative, including E06.

**Q19.** Incomplete: the output was truncated, so these are only the visible entities with a Negative outlook, including E01 and E09. I left out E1158 because a later withdrawal conflicts with its outlook row.

**Q20.** No. E07 had its rating withdrawn for commercial reasons (A19), which is not a default.

**Q21.** Incomplete: the output was truncated, so these are only the visible entities whose last long-term action is a withdrawal. I left out entities with only a local-currency withdrawal, such as E1106, which may still hold a foreign-currency rating.

**Q22.** E08, which reached RD on 2026-07-08 (A22). The output was truncated, so there may be more.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 72 instruments held an investment-grade rating on 1 October 2026. Expected ratings (EX) were excluded.

**Q26.** A+.

**Q27.** A-. I06 was assigned A- on 2024-03-01.

**Q28.** BBB+ (A38).

**Q29.** None. VD only carries a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** Entities at the ceiling: BB for VD entities and A for CV entities. This relies on the country on each entity's own record.

**Q31.** No. None of the foreign-currency ratings I checked for VD or CV entities was above its ceiling.

**Q32.** E09. The chain is E11 to E10 to E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05. I05 is rated BBB+ (downgraded 2026-04-15).

**Q34.** No. E12 has no parent, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11. E17 is E10's RESEARCH record, not a separate entity.

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** About 497. The data has 509 distinct LEIs; I removed 14 QA LEIs and added the sovereigns (CV, VD), which have no LEI. This is approximate.

**Q38.** No. They have different LEIs.

**Q39.** A (A08, A09).

**Q40.** Not determined. I did not complete that query.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. RESEARCH holds on domicile, and E17 (HALDEN BANK) says LU.

**Q43.** 1, the Halden Bank entity (E17 and E10 share an LEI).

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** Yes. I07 is rated BBB- while the VD ceiling is BB, though local-currency debt is not capped by the ceiling.

**Q46.** No. E11 only has a Credit opinion (BBB), which is not a rating.

**Q47.** None. I08 only has an Expected rating (EX), so it is not yet rated.

**Q48.** 113 instruments.

**Q49.** E5001. The chain is E5047, E5035, E5023, E5011, E5167 (same LEI as E5005), E5002, E5001.

**Q50.** 6 levels.

**Q51.** 59.

**Q52.** 25.

**Q53.** No. E5062 goes up through E5060 to E5059, which has no parent in RATINGS, the system of record for parent links. A stray record linking E5059 to Rotam is overridden by that.

**Q54.** E5106, E5124 and E5130. E5106 is VD per the RESEARCH record E5169.

**Q55.** 31.

**Q56.** BB-, held by E5144.

**Q57.** E5002. E5011 reaches it via E5167 (same entity as E5005), and E5013 reaches it via E5006.

**Q58.** E5145, the guarantor of I5007 (issuer E5133, in the Vesol group).

**Q59.** 12.

**Q60.** The holder takes the risk of E5145 (Geren Group), the guarantor of I5007 (BBB). It is not in the same group as the issuer E5133, which is in the Vesol group.

**Q61.** At least 4, but this is a lower bound. The full query timed out; I counted E5012, E5023, E5024 and E5047 from the ceiling list.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1115","E1121","E1124","E1138","E1140","E1155","E1158","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes","rating":"BBB"},
"Q25":{"count":72},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124","E1039","E1194","E15","E5116"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":497},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":null},
"Q41":{"rating":"none"},
"Q42":{"country":"LU"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":113},
"Q49":{"parent":"E5001"},
"Q50":{"count":6},
"Q51":{"count":59},
"Q52":{"count":25},
"Q53":{"same_group":"no"},
"Q54":{"entities":["E5106","E5124","E5130"]},
"Q55":{"count":31},
"Q56":{"rating":"BB-"},
"Q57":{"entity":"E5002"},
"Q58":{"entities":["E5145"]},
"Q59":{"count":12},
"Q60":{"risk_of":"E5145","same_group":"no"},
"Q61":{"count":4}
}
```