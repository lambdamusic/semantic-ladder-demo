**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12) until the downgrade A02 on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, both affirmations. A03 changed the outlook to NEG, not the rating.

**Q3.** No, it is rated BB+. I02 is subordinated, and its latest rating is BB+ (A07).

**Q4.** POS. E02 and E03 share an LEI, so they are the same entity. The latest action is A09 (2025-09-15) with outlook POS.

**Q5.** The holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, whose LTIDR is A (A08, A09), and I03 is also rated A (A10, A11).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating. E05's FC rating is BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** 31 entities, listed in the JSON. These are issuers with a DG on an LTIDR or STIDR in 2026, deduplicated by LEI and shown as RATINGS record IDs.

**Q8.** E08. Its rating was set to RD on 2026-07-08 (A22).

**Q9.** 278 distinct issuers hold an LTIDR or STIDR that was not withdrawn as of 2026-10-01. QA records are excluded and records are merged by LEI.

**Q10.** Depends. The FC rating is BB (speculative) and the LC rating is BBB- (investment grade), so it turns on which basis is meant.

**Q11.** BBB+. The DG A36 on 2024-09-30 set BBB+, and nothing changed it by 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the downgrade.

**Q13.** 1. The only DG is A36. The RW (A35) and the affirmations are not downgrades.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01, after 2024-01-01.

**Q15.** A-. E10 was downgraded to BBB+ only on 2026-04-15 (A27). E17 is the same LEI.

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is BBB+ now; only a watch and an affirmation came in between.

**Q17.** No. E06 only had a Rating Watch Negative on 2026-09-03 (A17), which is not a downgrade.

**Q18.** 32 issuers, listed in the JSON, with the latest LTIDR on RWN as of 2026-10-01.

**Q19.** 28 issuers, listed in the JSON, with a latest LTIDR outlook of NEG that had not been withdrawn.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** 35 entities, listed in the JSON. Each held an LTIDR or STIDR at some point but had none on 2026-10-01, mostly through withdrawal.

**Q22.** E08 only, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. Of the 106 instruments with a rating, 66 are BBB- or better.

**Q26.** A+ (A40).

**Q27.** A- (A42 for I06).

**Q28.** BBB+ (A38). The Country Ceiling of A (A37) is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** 8 entities, listed in the JSON. Their FC rating equals the country ceiling (CV is A, VD is BB).

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, whose LTIDR is BBB+ (A27), and I05 is also BBB+ (A29).

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3 (E09, E10, E11). E17 is the same LEI as E10.

**Q36.** 2 (E02, E04). E03 is the same LEI as E02.

**Q37.** 331. That is the distinct LEIs or IDs after excluding the QA records.

**Q38.** No. They have different LEIs, in different countries.

**Q39.** A. The latest actions are A09 and A25 (after A08).

**Q40.** 66 distinct GB issuers.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. This is the RATINGS record E10, which holds over the RESEARCH record E17 (LU).

**Q43.** 1. The only LU record is E17, which duplicates E10.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD.

**Q45.** No. I07 is rated BBB- (A45) against a ceiling of BB, but local-currency debt is not capped.

**Q46.** No. E11 only has a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected rating (A47), so it is unrated.

**Q48.** 106 instruments held a rating, excluding EX actions.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1285","E1290","E1058","E1167","E1051","E10","E1160","E1229","E1307","E1255","E1263","E1228","E1298","E1294","E1151","E1080","E1034","E1064","E1093","E1159","E1057","E1053","E1144","E1243","E1186","E1112","E1169","E08","E1213","E1300","E1163"]},
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
"Q18":{"issuers":["E1013","E1297","E1238","E1061","E1146","E1203","E1066","E1314","E1323","E1133","E06","E1181","E1194","E1088","E1019","E1006","E1264","E1098","E1126","E1059","E1266","E1039","E1267","E1099","E1132","E1260","E1317","E1242","E1037","E1209","E1168","E1109"]},
"Q19":{"issuers":["E1211","E09","E1046","E1271","E1034","E1188","E1248","E1079","E1263","E1228","E1080","E1005","E1190","E1072","E1059","E1056","E1282","E1055","E1294","E1064","E1261","E01","E1118","E1029","E1160","E1158","E1105","E1300"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1206","E1320","E1219","E1076","E1218","E1001","E1172","E1124","E1062","E1225","E1233","E1234","E1200","E1032","E1159","E1057","E1155","E1253","E1007","E1308","E1205","E1121","E1316","E1244","E1021","E07","E1166","E1277","E1048","E1084","E1138","E1041","E1063","E1107","E1140"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E1039","E1236","E1101","E05","E1028","E1126","E1194","E15"]},
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
"Q42":{"country":"DE"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```