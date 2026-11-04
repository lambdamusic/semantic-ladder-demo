**Q1.** A-. E01's rating was set by A01 (assigned 2024-03-12) and not changed until A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions, A03 and A04, are affirmations. A03 changes the outlook to NEG but leaves the rating at BBB.

**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ by A07 on 2025-06-20 (A23 had assigned BBB). BB+ is speculative grade.

**Q4.** Positive. A09 on E03 affirmed A with a POS outlook on 2025-09-15. E03 has the same LEI as E02, so it is the same entity, and A09 supersedes A08's STA.

**Q5.** The holder takes E02's credit risk, rated A. I03 is issued by E04 but guaranteed by E02, and E02's latest rating is A (A09).

**Q6.** The Country Ceiling for VD is BB (A12) and caps foreign-currency ratings. E05's FC rating is therefore BB (A14), while its uncapped LC rating is BBB- (A13).

**Q7.** 31 entities had a DG action dated in 2026. They are listed in the JSON. Research-system records are mapped to their RATINGS record, so E1170 appears as E1169, E1161 as E1160 and E1299 as E1298. QA records and instrument downgrades are excluded.

**Q8.** E08 was in default. A22 downgraded it to RD on 2026-07-08, and nothing later changed that.

**Q9.** 278. Of the 300 distinct entities in E1001–E1324, 34 had their FC rating withdrawn and 266 held one. Another 12 of the earlier entities held a rating, and sovereign VD has only a ceiling.

**Q10.** Depends. E05's FC rating is BB (speculative) but its LC rating is BBB- (investment grade) (A13, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action, A35, is dated 2025-11-20.

**Q12.** A-. A34 assigned A- on 2023-01-15, before A36.

**Q13.** 1. Only A36 is a DG; A35 is a watch and A33 an affirmation.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. A26 assigned A- to E10 in 2023, and the next action, A27, is dated 2026-04-15. E17 is the same entity and has no actions of its own.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+; A35 is only a watch and A33 an affirmation.

**Q17.** No. E06's only 2026 action is A17, which places it on Rating Watch with the rating unchanged at A-.

**Q18.** 32 issuers were on RWN, which means their latest action was an RW. The IDs are in the JSON.

**Q19.** 28 issuers had a NEG outlook, meaning their latest action carried NEG. The IDs are in the JSON. I excluded issuers whose latest action was an RW, since that action carries no outlook.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), which is not a default.

**Q21.** 35 entities. These are E07 and 34 others whose last rating action by 2026-10-01 was a WD. The IDs are in the JSON.

**Q22.** Only E08. It reached CCC (A21) and then RD (A22).

**Q23.** F2, from A04 on E01.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. This counts instruments whose latest INST rating was BBB- or higher on 2026-10-01. Instruments with only an EX action are excluded.

**Q26.** A+, from A40.

**Q27.** A-. I06 was assigned A- by A42.

**Q28.** BBB+, from A38. The A at CV is the Country Ceiling (A37), not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** 8 entities had an FC rating exactly at their country's ceiling. Those in VD (ceiling BB) are E05, E1028, E1101, E1126 and E1236. Those in CV (ceiling A) are E15, E1039 and E1194.

**Q31.** No. No VD or CV entity's FC rating is above its ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ by A27.

**Q34.** No. E12 has no parent, while E10 sits in the E09 group. The shared "Halden" name does not make them one group.

**Q35.** 3. The group is E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2. The group is E02 and E04. E03 is a duplicate of E02.

**Q37.** 330 distinct legal entities. This excludes QA records, collapses duplicate LEIs, and includes the two sovereigns.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09).

**Q40.** 66 GB-domiciled issuers held an issuer rating on 2026-10-01. That is 61 among E1001–E1324 plus 5 from the earlier records.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. RATINGS record E10 says DE, and it overrides the RESEARCH record E17 (LU).

**Q43.** 0. The only LU record is E17, which is overridden by E10's DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, even though its BBB- (A45) is above the BB ceiling.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an EX action (A47) and no assignment.

**Q48.** 106 instruments held an INST rating on 2026-10-01. Of 115 instruments, 9 have only an EX action and are unrated: I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

Some entities (E1115, E1158, E1303) have rating actions dated after a withdrawal. I treated the latest action by date as current, so they count as rated. I also treated the LC rating on E1279 and E1106 as still held after the FC withdrawal.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1307","E1169","E1160","E1159","E1167","E1186","E1080","E1093","E1051","E1053","E1057","E1034","E1112","E1263","E1285","E1290","E1294","E1298","E1300","E1151","E1144","E1243","E1255","E1229"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 278},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1088","E1194","E1203","E1133","E1006","E1099","E1168","E1019","E1013","E1037","E1059","E1066","E1061","E1098","E1109","E1264","E1260","E1126","E1132","E1146","E1181","E1209","E1238","E1266","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1158","E1034","E1080","E1064","E1228","E1263","E1294","E1300","E1271","E1160","E1118","E1079","E1190","E1046","E1056","E1029","E1248","E1261","E1105","E1005","E1072","E1211","E1282","E1188","E1055","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E15","E1039","E1194"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 330},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 66},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```