**Q1.** A-. E01's LTIDR FC was assigned A- on 2024-03-12 (A01) and not changed until the downgrade on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation (A03/A04); the downgrade was in 2025 (A02).

**Q3.** No, BB+. I02 is E01's subordinated note, and its latest action is the downgrade to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (2025-09-15, outlook POS).

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk; E02/E03 are currently A (A08, A09).

**Q6.** Not in the JSON. E05's FC rating is capped at the Valdoria Country Ceiling of BB (A12, A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** 38 entities had a downgrade in 2026 (listed in the JSON, using RATINGS IDs for duplicate records). I excluded QA records, and counted A5028 (E5033, dated 2026-11-06) even though it is later than today.

**Q8.** E08. Its rating went to RD on 2026-07-08 (A22, distressed exchange).

**Q9.** 377. I merged same-LEI records, excluded QA and sovereigns, and removed 32 entities whose latest action is a withdrawal. E1115, E1158 and E1303 have actions dated after their withdrawal, so I counted them as rated.

**Q10.** Depends. E05's FC rating is BB (speculative), but its LC rating is BBB- (investment grade) (A13, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34).

**Q13.** 1. Only A36 is a downgrade; A35 (watch) and A33 (affirmation) are not.

**Q14.** None. E12's first rating action is dated 2024-02-01 (A30), after the question date.

**Q15.** A-. E10 was assigned A- (A26), and the downgrade to BBB+ is dated 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; the intervening actions are a watch and an affirmation (A35, A33).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which is not a downgrade.

**Q18.** 32 issuers (listed in the JSON). I took each entity's latest action and kept those where it is a Rating Watch Negative (RW) action; E1019 is on watch for its LC rating.

**Q19.** 43 issuers (listed in the JSON), based on each entity's latest LTIDR action having outlook NEG. Where the latest action is a watch with a blank outlook (E1146, E1132), I did not count it.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** 35 entities (listed in the JSON), each with a withdrawal as the latest action. E1279 and E1106 still hold an LC or FC rating, so they are not included.

**Q22.** E08 only. It is the only entity with an RD or D rating (A22).

**Q23.** F2. This is the short-term rating on STIDR, affirmed in A04.

**Q24.** Yes. E01's current LTIDR FC is BBB (A03).

**Q25.** 72. Of the 113 instruments with an INST rating on 2026-10-01, 41 are speculative grade; EX actions do not count as ratings.

**Q26.** A+ (A40).

**Q27.** A-. I06 has a single INST action (A42).

**Q28.** BBB+ (A38). The Country Ceiling of A (A37) is not the sovereign's own rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** 12 entities (listed in the JSON). Ceilings are BB for VD and A for CV; these entities have an FC rating exactly at their country's ceiling, with country taken from RESEARCH where records disagree (E5106 is VD).

**Q31.** No. No VD entity has an FC rating above BB, and no CV entity has one above A.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** 497. That is 540 records, minus 29 same-LEI duplicates and 14 QA records, and it includes the two sovereigns.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A08, A09).

**Q40.** 79. These are GB-domiciled entities (after RESEARCH country corrections) with an issuer rating in force on 2026-10-01.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, and it shares E10's LEI.

**Q43.** 1. Only E17, which is the same entity as E10.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and E05 is domiciled in VD.

**Q45.** No. The note is local-currency debt, which the ceiling does not cap, and it is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected-rating action (A47, EX).

**Q48.** 113. There are 122 instruments, and 9 have only EX actions or none.

**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 (which is E5005) → E5002 → E5001.

**Q50.** 6 levels, by the chain in Q49.

**Q51.** 58 (E5001–E5058).

**Q52.** 19 (E5086–E5104).

**Q53.** No. RATINGS holds parent links, and it puts E5062 under E5060 and E5059, not Rotam; the E5168 link to E5086 is ignored.

**Q54.** E5106, E5124 and E5130. E5106 is VD per the RESEARCH record E5169.

**Q55.** 31. These are rated descendants of VD-domiciled entities: E5005 (6), E5106 (8), E5124 (1), E5091 (2) and E5145 (14).

**Q56.** BB-. Vesol members range from BB- (E5144) to A+ (E5140); E5141 is BB after its downgrade (A5106).

**Q57.** E5002. E5011 goes through E5167 (E5005) to E5002, and E5013 goes through E5006 to E5002.

**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the Vesol group; every other guarantee is for a subsidiary in the same group.

**Q59.** 12. There are 12 members at depth 3, counting E5011 via E5167.

**Q60.** E5145 (Geren Group), and no. The issuer E5133 belongs to the Vesol group, not Geren.

**Q61.** 19 Cerid members with a current FC rating of BB+ or lower.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1169","E1051","E1080","E1307","E1167","E1298","E5156","E5116","E5059","E1160","E1285","E1263","E1290","E1034","E1294","E5033","E1300","E1229","E1228","E1243","E1255","E1213","E1112","E1093","E1064","E1144","E1159","E1163","E1053","E1057","E1058","E1186","E5113","E5097","E5019","E1151"]},
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
"Q18":{"issuers":["E06","E1019","E1006","E1013","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1282","E1294","E5020","E5023","E5019","E5013","E5039","E5050","E5057","E5059","E5062","E5073","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E5097","E1034","E1046","E1056","E1072","E1079","E1080","E1118","E1160","E1188","E1190","E1211","E1228","E1263","E1271","E1300","E1248","E1261","E1005","E1029","E1059"]},
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
"Q30":{"entities":["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5124","E15","E1039","E1194","E5116"]},
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