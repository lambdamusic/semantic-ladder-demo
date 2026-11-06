**Q1.** A- (FC, long-term issuer rating).
E01's latest LTIDR FC action before 2025-01-01 is A01 (Assigned A-, 2024-03-12); A02 (BBB) is dated 2025-06-20.

**Q2.** No.
The only 2026 actions on E01 are A03 (Affirmed BBB) and A04 (Affirmed F2, short-term), and neither is a downgrade.

**Q3.** No, BB+.
I02 (Kestrel 6.25% 2031, subordinated) was last rated by A07 (Downgraded to BB+, 2025-06-20), which supersedes A23 (BBB).

**Q4.** Positive.
E02 and E03 share LEI 213800PHEIYNJMHTDV74, so they are one entity; the latest outlook is set by A09 (Affirmed A, outlook POS, 2025-09-15).

**Q5.** Northwind Holdings (E02), rated A.
I03 is guaranteed by E02, so the holder takes E02's credit risk, and the instrument rating is A per A11 (Affirmed, 2025-09-15).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12). E05's FC rating is BB (A14) and its LC rating is BBB- (A13). The data doesn't state the cause; this is inferred from the ontology's definitions of Country Ceiling and FC/LC.

**Q7.** 31 issuers (listed in JSON). These are DG actions dated 2026 on issuer-rating records, excluding QA records and instrument-level actions.

**Q8.** E08.
A22 (Restricted default, RD, 2026-07-08) is its latest rating action, following a distressed debt exchange.

**Q9.** About 270.
This is a hand tally over the whole dataset, so treat it as approximate. It counts entities whose latest LTIDR action on or before 2026-10-01 isn't WD, including CV's sovereign rating; it treats E1158 and E1303 as rated because they have actions after their withdrawals.

**Q10.** Depends.
E05's LC rating is BBB- (A13, investment grade), while its FC rating is BB (A14, speculative).

**Q11.** BBB+.
E14's latest action before 2025-06-01 is A36 (Downgraded to BBB+, 2024-09-30).

**Q12.** A-.
E14's latest action before 2024-01-01 is A34 (Assigned A-, 2023-01-15).

**Q13.** 1.
The only downgrade on E14 is A36 (2024-09-30).

**Q14.** None.
E12's first action is A30 (Assigned BB-, 2024-02-01), which is after 2024-01-01.

**Q15.** A-.
E10's latest action before 2026-01-01 is A26 (Assigned A-, 2023-05-01); A27 (BBB+) is dated 2026-04-15.

**Q16.** No.
E14's rating stayed at BBB+ through A35 (Rating Watch, unchanged rating) and A33 (Affirmed).

**Q17.** No.
E06's only 2026 action is A17 (Placed on Rating Watch, 2026-09-03), which is not a downgrade.

**Q18.** 32 issuers (listed in JSON).
These are issuers whose latest action on or before 2026-10-01 is a Rating Watch (RWN). Several watches date from 2022–2024 with no resolving action in the data, so this list is sensitive to how stale watches are read.

**Q19.** 24 issuers (listed in JSON).
Each is the latest outlook-bearing action on or before 2026-10-01 that reads NEG. The data has no explicit end to outlooks, so I used the latest stated outlook.

**Q20.** No.
E07's latest action is WD (Withdrawn, 2026-05-12), and it has no default rating.

**Q21.** 38 entities (listed in JSON).
Each has a latest LTIDR action of WD on or before 2026-10-01.

**Q22.** E08.
It is the only entity with an RD (default) rating in the data.

**Q23.** F2.
E01's short-term rating is A04 (Affirmed F2, 2026-02-10).

**Q24.** Yes, BBB.
E01's issuer rating is A03 (Affirmed BBB, 2026-02-10), which is investment grade.

**Q25.** 66.
This counts instruments whose latest rating on or before 2026-10-01 is investment grade (BBB- or higher). Instruments with only EX (Expected) actions are unrated.

**Q26.** A+.
E15's local-currency rating is A40 (Assigned A+, 2024-03-01).

**Q27.** A-.
I06 (Corvenia Power 2032) is rated by A42 (Assigned A-, 2024-03-01).

**Q28.** BBB+.
CV's FC issuer rating is A38 (Assigned BBB+, 2024-01-01).

**Q29.** None.
VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** Eight entities (listed in JSON).
Each has an FC rating equal to its domicile's ceiling: BB for VD (A12) and A for CV (A37). Examples: E05 (BB), E15 (A).

**Q31.** No.
No domiciled entity has an FC issuer rating above its country's ceiling on 2026-10-01.

**Q32.** E09.
E11 → E10 → E09, and E09 has no parent.

**Q33.** Halden Bank AG (E10), rated BBB+.
I05 is guaranteed by E10, so the holder takes E10's credit risk, and I05's latest rating is A29 (Downgraded to BBB+, 2026-04-15).

**Q34.** No.
Halden Foods (E12) has no parent link, while Halden Bank (E10) sits under Halden Group (E09).

**Q35.** 3.
The Halden group comprises E09, E10 and E11 (E17 is the same entity as E10).

**Q36.** 2.
The Northwind group comprises E02 (including E03) and E04.

**Q37.** About 280.
This is an approximate hand tally of distinct non-QA LEIs, plus the two sovereigns. I could not verify it exactly.

**Q38.** No.
E06 and E13 have different LEIs.

**Q39.** A.
Northwind's latest rating is A09 (Affirmed A, 2025-09-15).

**Q40.** 65.
This counts active issuers domiciled in GB, using RESEARCH's domicile where records disagree. It is also a hand tally.

**Q41.** None.
E16 is a QA record, so its ratings are ignored.

**Q42.** LU.
E17 (RESEARCH) says LU, E10 (RATINGS) says DE, and RESEARCH holds for domicile.

**Q43.** 1.
Only E17/E10 is domiciled in LU.

**Q44.** Yes.
I07 is in XVD, the domestic currency of VD, so it is local-currency debt.

**Q45.** No.
I07 is local-currency debt, and the Country Ceiling (BB) caps only foreign-currency ratings, so it doesn't apply to I07 (rated BBB-).

**Q46.** No.
E11 has only a credit opinion (A46, type CO), which is not an issuer rating.

**Q47.** None.
I08 has only an EX (Expected) action (A47), so it is not yet rated.

**Q48.** 106.
There are 115 instruments in total; 9 have only EX actions and are unrated.

Caveats: the watch and outlook answers (Q18, Q19) assume the latest action sets the status, and the data never closes watches or outlooks. E1158 and E1303 have withdrawals followed by later rating actions; I treated them as rated.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E1034", "E1051", "E1053", "E1057", "E1058", "E1064", "E1080", "E1093", "E1144", "E1151", "E1112", "E1159", "E1161", "E1163", "E1167", "E1170", "E1186", "E1213", "E1228", "E1229", "E1243", "E1255", "E1263", "E1285", "E1290", "E1294", "E1299", "E1300", "E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 270},
  "Q10": {"investment_grade": "depends"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06", "E1006", "E1013", "E1019", "E1037", "E1039", "E1059", "E1061", "E1066", "E1088", "E1098", "E1099", "E1109", "E1126", "E1132", "E1133", "E1146", "E1168", "E1181", "E1194", "E1203", "E1210", "E1238", "E1242", "E1260", "E1264", "E1266", "E1267", "E1297", "E1314", "E1317", "E1323"]},
  "Q19": {"issuers": ["E01", "E1029", "E1034", "E1046", "E1055", "E1056", "E1064", "E1072", "E1079", "E1080", "E1118", "E1146", "E1161", "E1188", "E1190", "E1211", "E1228", "E1248", "E1262", "E1263", "E1271", "E1282", "E1294", "E1300"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07", "E1002", "E1007", "E1021", "E1032", "E1041", "E1048", "E1057", "E1062", "E1063", "E1076", "E1084", "E1106", "E1107", "E1115", "E1121", "E1124", "E1138", "E1140", "E1155", "E1159", "E1166", "E1172", "E1200", "E1205", "E1206", "E1218", "E1219", "E1225", "E1233", "E1234", "E1244", "E1254", "E1277", "E1279", "E1308", "E1316", "E1320"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": 66},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E15", "E1028", "E1039", "E1101", "E1126", "E1194", "E1236"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 280},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 65},
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