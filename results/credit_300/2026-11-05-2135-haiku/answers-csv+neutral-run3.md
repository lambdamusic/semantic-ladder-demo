**Q1.** A-. Only A01 (AS, A-, 2024-03-12) applies on 1 Jan 2025; the downgrade (A02) came later, on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03 (affirmed BBB, outlook NEG, 2026-02-10).

**Q3.** No, BB+. I02 was cut from BBB to BB+ by A07 (2025-06-20).

**Q4.** Positive (POS). The latest action on E02/E03 is A09 (affirmed A, POS, 2025-09-15).

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so the holder carries E02's risk, and I03's latest rating (A11) is A.

**Q6.** Valdoria's Country Ceiling (A12, BB) caps foreign-currency ratings of VD-domiciled entities. E05's FC rating (A14, BB) sits at that ceiling, while its LC rating (A13, BBB-) is not capped.

**Q7.** 30 issuers, listed in the JSON. Each has a 2026-dated DG action; for example E08 (A21, A22), E10 (A27) and E1051 (A102, A104).

**Q8.** Saxby Shipping (E08). Its distressed debt exchange (A22, RD, 2026-07-08) is the only default.

**Q9.** 278. Hand tally of entities whose latest LTIDR action on or before 1 Oct 2026 is not a withdrawal. Sovereign CV is included; VD is not, since it has only a ceiling.

**Q10.** Depends. FC is BB (A14, speculative grade); LC is BBB- (A13, investment grade).

**Q11.** BBB+. A36 (DG, 2024-09-30) is the latest action before 1 Jun 2025; A35 (RW) comes later.

**Q12.** A-. A34 (AS, 2023-01-15) is the rating on 1 Jan 2024.

**Q13.** 1. The only DG on E14 is A36 (2024-09-30).

**Q14.** None. E12's first rating (A30) is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. A26 (AS, 2023-05-01) is the latest action before 2026-01-01; A27 (DG to BBB+) is dated 2026-04-15.

**Q16.** No. E14 was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33, AF, 2026-05-01); only watch status changed.

**Q17.** No. E06's 2026 action (A17, 2026-09-03) is a Rating Watch placement, not a downgrade.

**Q18.** 30 issuers, listed in the JSON. Each one's latest action on or before 1 Oct 2026 carries RWN.

**Q19.** 30 issuers, listed in the JSON. Each one's latest non-blank outlook is NEG.

**Q20.** No. E07 was withdrawn (A19, 2026-05-12), which is not a default.

**Q21.** 35 entities, listed in the JSON. Each had a rating at some point, and its latest LTIDR action on or before 1 Oct 2026 is a withdrawal.

**Q22.** Saxby Shipping (E08), the only entity with RD.

**Q23.** F2. A04 (STIDR, affirmed, 2026-02-10).

**Q24.** Yes. Kestrel's FC issuer rating is BBB (A03), which is investment grade.

**Q25.** 66. Of 115 instruments, 9 have no assigned rating (EX only or nothing), and 40 of the remaining 106 are below BBB-.

**Q26.** A+. A40 (LC, 2024-03-01).

**Q27.** A-. I06 (AS, 2024-03-01).

**Q28.** BBB+. A38, the sovereign's FC issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** Eight entities, listed in the JSON. Five VD entities sit at the BB ceiling and three CV entities sit at the A ceiling.

**Q31.** No. No FC issuer rating is above BB for VD or above A for CV.

**Q32.** Halden Group plc (E09). E11 → E10 → E09, and E09 has no parent.

**Q33.** Halden Bank AG (E10), rated BBB+. I05 is guaranteed by E10, and its latest rating (A29, DG, 2026-04-15) is BBB+.

**Q34.** No. E12 has no parent link, so the data does not place it in E09's group.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 331. There are 357 non-QA records, less 26 RESEARCH duplicates. This includes the two sovereign records.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. A09 (AF, A, POS, 2025-09-15) is the latest action on the group.

**Q40.** 66. Hand count of GB-domiciled entities with an issuer rating on 1 Oct 2026. E10 is excluded because its RESEARCH record (E17) puts it in LU.

**Q41.** None. E16 is a QA record, so its data is ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile over E10's DE.

**Q43.** 1 (E10).

**Q44.** Yes. XVD is VD's domestic currency, so the note is local-currency debt.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. A47 for I08 is EX (expected), which is not a rating until an AS action.

**Q48.** 106. Of 115 instruments, 9 have no assigned rating as of 1 Oct 2026.

---

**Notes:** Counts (Q9, Q25, Q37, Q40, Q48) and lists (Q7, Q18, Q19, Q21, Q30) are hand tallies across about 470 actions, so they should be spot-checked. Piren (E1115), Nular (E1158) and Lunor (E1303) have rating actions after a withdrawal; I treated the later action as a re-rating. Excluding them would change Q9 (−3), Q21 (+3), Q19 (−E1158) and Q40 (−E1115). Several AF/UG actions carry ratings that don't match the prior rating; I used the recorded rating as stated. Some actions are dated after today (2026-11-06), but none changes an answer.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307"]},
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
  "Q18": {"issuers": ["E06","E1006","E1013","E1019","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
  "Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1160","E1188","E1190","E1196","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
  "Q37": {"count": 331},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 66},
  "Q41": {"rating": "none"},
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 106}
}
```