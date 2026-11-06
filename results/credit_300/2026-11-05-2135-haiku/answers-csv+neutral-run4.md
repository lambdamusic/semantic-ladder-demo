**Q1.** A- (A01 is the latest action on or before 2025-01-01, an assignment at A-).

**Q2.** No. The 2026 actions on E01 are an affirmation (A03) and a short-term affirmation (A04), with no downgrade.

**Q3.** No, rated BB+. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. The latest action on E02/E03 (same LEI) is the affirmation A09 (2025-09-15) with outlook POS.

**Q5.** The holder takes Northwind Holdings' (E02) risk, rated A. I03 is guaranteed by E02 (guarantor), so it is rated in line with E02, and A10/A11 give A.

**Q6.** The FC rating is capped by Valdoria's Country Ceiling of BB (A12), while the LC rating (BBB-, A13) is not subject to the ceiling. Both E05 ratings were set on 2025-04-01 (A13, A14).

**Q7.** 31 issuers, all with a DG action dated 2026 (canonical RATINGS record IDs): E08, E10, E1034, E1051, E1053, E1057, E1058, E1064, E1080, E1093, E1112, E1144, E1151, E1159, E1160, E1163, E1167, E1169, E1186, E1213, E1228, E1229, E1243, E1255, E1263, E1285, E1290, E1294, E1298, E1300, E1307. Some DG labels are inconsistent with the rating moving (e.g. E1229 A1481 "DG" to BB+ from BB, E1051 A1104 "DG" at A+ unchanged). I counted them as the ontology defines DG (the action code).

**Q8.** E08, which was downgraded to RD on 2026-07-08 (A22). RD is a default under the ontology.

**Q9.** Not settled by hand. Counting issuers with a live LTIDR on 1 Oct 2026 needs a full scan of about 350 entities, which I did not complete reliably.

**Q10.** Depends on currency basis. The LC rating is BBB- (A13, investment grade) and the FC rating is BB (A14, speculative).

**Q11.** BBB+. A36 (DG to BBB+, 2024-09-30) is the latest action before 2025-06-01; the RW of 2025-11-20 is after that date.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 (2024-09-30) is a DG action on E14.

**Q14.** None. Halden Foods' first rating is A30 (BB-) on 2024-02-01, which is after 2024-01-01.

**Q15.** A-. A26 (A-) was the rating on 2026-01-01; A27 (DG to BBB+) is dated 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33, affirmed 2026-05-01). The RW in A35 does not change the rating.

**Q17.** No. E06 has only a Watch placement (A17, RW), which is not a downgrade.

**Q18.** Not settled. The ontology gives no rule for when a watch ends. Open RWN watches under the rule "open until a later action on that rating" include E06, E1098, E1238, E1266, E1297 and E1059 (LC), but a full list needs a script.

**Q19.** Not settled by hand; it needs a full scan of outlooks as of 1 Oct 2026.

**Q20.** No. E07 was withdrawn (A19, 2026-05-12), which the ontology says is not a default.

**Q21.** 35 entities. Each had a WD on its rating with no later rating action (E07, E1124, E1032, E1063, E1084, E1218, E1279, E1138, E1001, E1140, E1076, E1062, E1041, E1205, E1206, E1233, E1225, E1277, E1200, E1166, E1244, E1021, E1320, E1107, E1121, E1155, E1316, E1308, E1172, E1159, E1234, E1219, E1048, E1057, E1007). E1115, E1158 and E1303 have actions after their WD, which conflicts with the rule, so I did not count them. E1106's WD covers only LC; its FC rating remains.

**Q22.** E08 (the only RD record).

**Q23.** F2 (A04, STIDR affirmed 2026-02-10).

**Q24.** Yes. The current issuer rating is BBB (A03), which is investment grade.

**Q25.** Not settled by hand; it needs a full instrument-level scan as of 1 Oct 2026.

**Q26.** A+ (A40, LC assigned 2024-03-01, no later LC action).

**Q27.** A- (A42, subordinated instrument I06 assigned 2024-03-01).

**Q28.** BBB+ (A38, assigned 2024-01-01). A37 (A) is the Country Ceiling, not the sovereign's issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB) and no LTIDR action.

**Q30.** Eight entities. CV's ceiling is A (A37): E15, E1039 and E1194 have FC A. VD's ceiling is BB (A12): E05, E1028, E1101, E1126 and E1236 have FC BB.

**Q31.** No. No VD-domiciled FC rating exceeds BB, and no CV-domiciled one exceeds A.

**Q32.** E09. E11 → E10 → E09, and E09 has no parent.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10 (guarantor), and I05 is rated BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no parent, while Halden Bank (E10) belongs to E09's group. The shared name is misleading.

**Q35.** 3: E09, E10 and E11. E17 is a RESEARCH duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a RESEARCH duplicate of E02.

**Q37.** 331. I took 370 records, removed the 13 QA records (E16, E1340–E1351), and removed 26 RESEARCH duplicates of RATINGS records with the same LEI. Sovereigns VD and CV are included as entities.

**Q38.** No. The two have different LEIs (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214).

**Q39.** A (A09, affirmed 2025-09-15, via E03 which is the same entity as E02).

**Q40.** Not settled by hand; it needs a full scan of GB-domiciled issuers as of 1 Oct 2026.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. The RESEARCH record E17 overrides the RATINGS record E10 (DE) on domicile.

**Q43.** 1: E10 (domiciled in LU per E17, the RESEARCH record).

**Q44.** Yes. The 2027 note I07 is in XVD, the domestic currency of VD where E05 is domiciled.

**Q45.** No. The note is local-currency, and the ceiling applies only to foreign-currency debt. BBB- (A45) being above the BB ceiling is therefore not a breach.

**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46, CO), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47, EX), and EX is not a rating until an AS action.

**Q48.** Not settled by hand; it needs a full instrument-level scan as of 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": null},
  "Q10": {"investment_grade": "depends"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": null},
  "Q19": {"issuers": null},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07","E1124","E1032","E1063","E1084","E1218","E1279","E1138","E1001","E1140","E1076","E1062","E1041","E1205","E1206","E1233","E1225","E1277","E1200","E1166","E1244","E1021","E1320","E1107","E1121","E1155","E1316","E1308","E1172","E1159","E1234","E1219","E1048","E1057","E1007"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": null},
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