**Q1.** A-. E01's FC rating was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01 stayed at BBB; the 2026-02-10 action (A03, AF) moved only the outlook to Negative.

**Q3.** No, BB+. I02 was cut from BBB to BB+ on 2025-06-20 (A07), and that row is still open.

**Q4.** Positive. E02's A rating has outlook POS from 2025-09-15 (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03's credit_risk_of is E02, and I03 is rated A (A11).

**Q6.** Valdoria Telecom's foreign-currency rating is capped by Valdoria's country ceiling. E05's FC rating is BB (A14), which matches the VD ceiling of BB (ceilings.csv), while its LC rating of BBB- (A13) sits above it. The data does not state the capping rule explicitly, so this is an inference from the ceiling and the FC/LC split.

**Q7.** 31 issuers had a rating-level drop in 2026, listed in the JSON. Some rows carry action codes that conflict with the rating move (e.g., E1064 is labelled AF but fell from A- to BBB+), so I counted by rating level. WD (withdrawal) and RW/outlook-only changes were not counted.

**Q8.** E08 only. Its rating was RD (restricted default) from 2026-07-08 (A22), the only default code in the data.

**Q9.** 278. I counted distinct entities with an open LTIDR row that is not WD-only (E08's RD counted as a rating). This is a long manual tally, so treat it as approximate.

**Q10.** Depends. E05's FC rating is BB (not IG, A14), but its LC rating is BBB- (IG, A13).

**Q11.** BBB+. E14's BBB+ ran from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14's A- ran until 2024-09-30 (A34).

**Q13.** 1. E14's only rating-level move was A- to BBB+ on 2024-09-30 (A36); the later RWN and AF rows kept BBB+.

**Q14.** None. E12's first rating starts 2024-02-01 (A30), after 1 Jan 2024.

**Q15.** A-. E10's A- ran to 2026-04-15 (A26), so it was in force on 1 Jan 2026.

**Q16.** No. E14 stayed BBB+ (A36, A35, A33); there was only a watch placement and an affirmation.

**Q17.** No. E06 stayed A-; the only 2026 action was a Rating Watch placement on 2026-09-03 (A17).

**Q18.** 32 issuers have an open RWN watch flag (RW actions with watch = RWN and no valid_to).

**Q19.** 28 issuers have an open NEG outlook.

**Q20.** No. E07 was withdrawn (WD) on 2026-05-12 (A19); withdrawal is not default.

**Q21.** 35 entities. Their only open rating row is WD, so they no longer hold a rating on 1 Oct 2026. I treated withdrawal as no longer having a rating.

**Q22.** E08 only (RD, A22).

**Q23.** F2. E01's short-term rating (STIDR) is F2 from 2026-02-10 (A04).

**Q24.** Yes. E01's FC issuer rating is BBB (A03), which is investment grade.

**Q25.** 66 instruments are rated investment grade (BBB- or above) with open ratings. The rated instruments total 106, of which 40 are below BBB-.

**Q26.** A+. E15's LC rating is A+ (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. CV's FC rating is BBB+ (A38).

**Q29.** None. VD has no rows in ratings.csv (its ceiling is BB, but that is not an issuer rating).

**Q30.** 7 entities sit exactly at their country ceiling. CV's ceiling is A: E15 (A) and E1194 (A, RWN). VD's ceiling is BB: E05, E1028, E1101, E1126, E1236 (all BB).

**Q31.** No. No CV- or VD-domiciled entity has an FC rating above its ceiling.

**Q32.** E09 (Halden Group plc). E11's ultimate_parent_id is E09.

**Q33.** E10, rated BBB+. I05's credit_risk_of is E10, and I05 is BBB+ (A29).

**Q34.** No. E12 has no parent or ultimate parent, and it does not appear in E10's ancestor chain (E10 → E09).

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 331. That is the number of rows in entities.csv, including the two sovereigns (CV, VD).

**Q38.** No. They are different entities with different IDs and countries (DE vs US), and there is no parent link between them.

**Q39.** A. E02's A rating has outlook POS (A09).

**Q40.** 66 GB-domiciled issuers hold an open issuer rating. This is a manual count against the Q9 list, so treat it as approximate.

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** LU. E10's country is LU.

**Q43.** 1 (E10).

**Q44.** Yes. I07 is marked local_currency = yes (currency XVD).

**Q45.** No. The ceiling in the data governs FC ratings (see Q6, Q30), and I07 is a local-currency note. The data does not explicitly say ceilings apply only to FC, so this answer rests on that reading.

**Q46.** No. E11 has no rows in ratings.csv; its note I05 is rated on E10's credit.

**Q47.** None. I08 has no row in ratings.csv.

**Q48.** 106. Of the 115 instruments, 106 have an open rating; I08 and eight 1000-series instruments (I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049) have none.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "Positive"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
  "Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
  "Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
  "Q30": {"entities": ["E05","E15","E1028","E1101","E1126","E1194","E1236"]},
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