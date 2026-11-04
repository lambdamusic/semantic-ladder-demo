**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01), so it held on 1 Jan 2025.

**Q2.** No. The only 2026 action on E01 is the 2026-02-10 affirmation at BBB (A03); the downgrade was in 2025 (A02).

**Q3.** No. The 2031 note is I02 (SUB), now rated BB+ (A07), which is sub-investment grade.

**Q4.** Positive (POS). E02's current LTIDR is A with a POS outlook (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and credit_risk_of is E02 (A09).

**Q6.** The data gives no explicit reason. E05's FC rating is BB (A14) against LC BBB- (A13). The FC rating equals Valdoria's ceiling of BB, which fits a country-ceiling effect, but the data doesn't state the cause.

**Q7.** 31 issuers had a net downgrade in 2026. I judged this from the actual rating-level change rather than the action label, because several labels are inconsistent (for example, E1229's 2026-06-02 "DG" was actually an upgrade). The list is in the JSON.

**Q8.** E08. Its rating went to RD on 2026-07-08 (A22) and remains in force.

**Q9.** 278. This counts every entity with an open, non-withdrawn LTIDR, including the sovereign CV and the RD-rated E08. It is 277 if you exclude CV.

**Q10.** Depends. E05 is BB in foreign currency (sub-investment grade) and BBB- in local currency (investment grade) (A14, A13).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating began on 2024-02-01 (A30).

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now. It spent time on watch (A35) and was then affirmed (A33).

**Q17.** No. E06's only 2026 action was placing the A- rating on RWN (A17), which is not a rating change.

**Q18.** 31 issuers had an open RWN on 1 Oct 2026. The list is in the JSON.

**Q19.** 28 issuers had an open NEG outlook on 1 Oct 2026. The list is in the JSON.

**Q20.** No. E07's rating was withdrawn (WD, A19) and E07 never had a default rating.

**Q21.** 35 entities. Each one's last open rating is WD, with no other open rating.

**Q22.** E08, the only entity ever rated RD (A22).

**Q23.** F2. E01's STIDR is F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. This counts instruments with an open INST rating of BBB- or better.

**Q26.** A+ (A40).

**Q27.** A-. I06's rating is A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** 8 entities. The ceilings are CV = A and VD = BB. The CV entities at A in foreign currency are E15, E1039 and E1194. The VD entities at BB in foreign currency are E05, E1028, E1101, E1126 and E1236.

**Q31.** No. No CV entity is above A and no VD entity is above BB.

**Q32.** E09 (ultimate_parent_id for E11).

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, so credit_risk_of is E10, and E10 is BBB+ (A27).

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is merged into E02.

**Q37.** 331, the number of rows in entities.csv after duplicates were merged.

**Q38.** No. E06 and E13 are separate entities with different LEIs and countries, and neither is a parent of the other.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled entities with an open, non-withdrawn issuer rating.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE (E10).

**Q43.** 0. No entity is domiciled in LU.

**Q44.** Yes. I07 is in XVD with local_currency = yes.

**Q45.** No. I07 is BBB- (A45) and VD's ceiling is BB, but the ceiling applies to foreign-currency ratings and I07 is a local-currency note.

**Q46.** No. E11 has no rating records of its own; its notes are rated through the guarantor E10.

**Q47.** None. I08 has no rating record.

**Q48.** 106 instruments (7 of the I0x series plus 99 of the I1xxx series).

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"POS"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18":{"issuers":["E06","E1006","E1013","E1019","E1037","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q30":{"entities":["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
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
"Q43":{"count":0},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"no"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```