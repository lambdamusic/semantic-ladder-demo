**Q1.** A-. The latest FC issuer rating on or before 1 Jan 2025 is A01 (Assigned A-, 2024-03-12). The downgrade to BBB came later, in A02 (2025-06-20).

**Q2.** No. E01's 2026 actions are affirmations (A03 AF BBB; A04 AF F2 on the short-term scale), with no downgrade.

**Q3.** No, BB+. I02 (Kestrel 6.25% 2031, subordinated) was assigned BBB in A23, then moved to BB+ in A07 (DG, 2025-06-20).

**Q4.** Positive. E02 and E03 share LEI 213800PHEIYNJMHTDV74, so they are one entity. Its latest outlook is in A09 (AF A, POS, 2025-09-15), which supersedes A08 (STA, 2023).

**Q5.** Northwind Holdings (E02), rated A. I03 (Northwind Finance 3.75% 2030) is guaranteed by E02, so the holder takes E02's credit risk. I03's instrument ratings A10 and A11 are both A.

**Q6.** Valdoria Telecom's FC rating (BB, A14) sits at the Valdoria Country Ceiling (BB, A12), while its LC rating (BBB-, A13) is not capped. The ontology defines the ceiling as capping FC ratings for transfer and convertibility risk, and not LC ratings, so the gap comes from that cap. The data itself does not state the cause; this is the ontology's definition applied to the figures.

**Q7.** Twenty-nine issuers were downgraded in 2026 (DG actions dated 2026). Two DG-labelled actions run against the rating movement (E1051 A1104; E1229 A1481), so the list relies on the action codes. The list is by hand and may not be exhaustive.

**Q8.** E08. Its RD (restricted default) action A22 (2026-07-08) is the latest action, and no later action changes it.

**Q9.** Not counted. This needs a full pass over all LTIDR entities, which I did not complete reliably.

**Q10.** No. The headline FC rating is BB (A14); the BBB- LC rating (A13) is not the headline.

**Q11.** BBB+. A36 (DG to BBB+, 2024-09-30) is the latest action on or before 2025-06-01.

**Q12.** A-. A34 (AS A-, 2023-01-15) is the latest action on or before 2024-01-01; A36 came later.

**Q13.** 1. A36 is the only DG action on E14.

**Q14.** None. E12's first action is A30 (AS BB-, 2024-02-01), which is after 1 Jan 2024.

**Q15.** A-. E10 and E17 share LEI 391200QYPVFF2O9K2039, so they are one entity. A26 (AS A-, 2023-05-01) is the latest action before 2026-01-01; the DG to BBB+ (A27) is dated 2026-04-15.

**Q16.** No. The 1 Jan 2025 rating was BBB+ (A36), and the later actions A35 (RW) and A33 (AF) keep it at BBB+.

**Q17.** No. E06's only 2026 action is A17 (Rating Watch, A-, 2026-09-03), which is not a downgrade.

**Q18.** Thirty-one issuers, by latest action. Those whose most recent action is an RW carrying RWN are listed. Some watches date back years with no clearing action in the data, so treat this as uncertain. Entities whose latest action is an AF or UG without a watch (e.g. E14, E1012, E1091, E1213, E1276, E1303) are excluded.

**Q19.** Not completed. I did not finish enumerating negative-outlook entities across the full dataset.

**Q20.** No. E07's latest action is A19 (WD, 2026-05-12), which is a withdrawal, not a default.

**Q21.** Thirty-six entities whose latest action is a withdrawal. E1279 is excluded because its LC rating (A195–A196) is still in force.

**Q22.** E08. It is the only entity with an RD or D action.

**Q23.** F2. A04 (AF, STIDR, 2026-02-10).

**Q24.** Yes. The latest FC issuer rating is BBB (A03, AF, 2026-02-10), which is investment grade.

**Q25.** Not counted. This requires enumerating all instrument ratings as of 1 Oct 2026.

**Q26.** A+. A40 (AS, LC, 2024-03-01) is the only LC action for E15.

**Q27.** A-. I06 (Corvenia Power 7.10% 2032) was assigned A- in A42.

**Q28.** BBB+. A38 (AS, FC, 2024-01-01) is the only FC action for the Republic of Corvenia (CV).

**Q29.** None. VD has only a Country Ceiling (A12, type CC, BB), which is not an issuer rating.

**Q30.** E05, E1028, E1101, E1236 (VD ceiling BB, FC rating BB); and E15, E1039, E1194 (CV ceiling A, FC rating A). I checked the entities domiciled in VD and CV in the data, but not exhaustively for every entity.

**Q31.** No. No company's FC rating in the data is above BB for VD-domiciled entities or above A for CV-domiciled entities.

**Q32.** E09 (Halden Group plc). E11 → E10 → E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 (Halden Leasing 2.90% 2028) is guaranteed by E10, and its latest rating is BBB+ (A29, DG, 2026-04-15).

**Q34.** No. E12 and E10 have different LEIs and no parent link connects them.

**Q35.** 3 (E09, E10/E17, E11).

**Q36.** 2 (E02/E03 and E04).

**Q37.** Not counted. This needs a full deduplication of all entity records by LEI.

**Q38.** No. E06 (LEI 549300AMVE3VRVG7HK43) and E13 (LEI 815600O8X8K2F154N214) have different LEIs.

**Q39.** A. A09 (AF, 2025-09-15), the latest action on E02/E03.

**Q40.** Not counted. This needs a full pass over GB-domiciled issuers.

**Q41.** None. E16 is a QA record, so its actions (A43, A44) must be ignored.

**Q42.** LU. The RESEARCH record E17 holds for domicile, overriding E10's DE.

**Q43.** 1 (Halden Bank, E10/E17).

**Q44.** Yes. XVD is Valdoria's domestic currency, so the note is local-currency debt.

**Q45.** No. BBB- is above the BB ceiling, but the ceiling caps only FC debt, and the 2027 note is in XVD.

**Q46.** No. E11 has only a credit opinion (A46, type CO), which is not an issuer rating.

**Q47.** None. A47 is an EX (expected) action, which is not a rating until an AS action confirms it.

**Q48.** Not counted. This needs a full pass over instrument ratings as of 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E1034", "E1051", "E1053", "E1057", "E1058", "E1064", "E1080", "E1093", "E1144", "E1151", "E1159", "E1161", "E1163", "E1167", "E1170", "E1186", "E1213", "E1228", "E1229", "E1243", "E1255", "E1263", "E1285", "E1290", "E1294", "E1300", "E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": null},
  "Q10": {"investment_grade": "no"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06", "E1013", "E1019", "E1037", "E1039", "E1059", "E1061", "E1066", "E1088", "E1098", "E1099", "E1109", "E1126", "E1132", "E1133", "E1146", "E1168", "E1181", "E1194", "E1203", "E1210", "E1238", "E1242", "E1260", "E1264", "E1266", "E1267", "E1297", "E1314", "E1317", "E1323"]},
  "Q19": {"issuers": null},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07", "E1002", "E1007", "E1021", "E1032", "E1041", "E1048", "E1057", "E1062", "E1063", "E1076", "E1084", "E1107", "E1121", "E1124", "E1138", "E1140", "E1155", "E1159", "E1166", "E1172", "E1200", "E1205", "E1206", "E1218", "E1219", "E1225", "E1233", "E1234", "E1244", "E1254", "E1277", "E1308", "E1316", "E1320"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": null},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E1028", "E1101", "E1236", "E15", "E1039", "E1194"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": null},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": null},
  "Q41": {"rating": "none"},
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": null}
}
```