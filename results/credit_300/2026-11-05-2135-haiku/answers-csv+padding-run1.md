**Q1.** A-. The FC issuer rating was A- from A01 (2024-03-12) until downgraded to BBB by A02 on 2025-06-20 for E01.

**Q2.** No. The 2026 actions on E01 are affirmations (A03: BBB, outlook Negative; A04: F2).

**Q3.** No, BB+. I02 was downgraded from BBB (A23) to BB+ (A07) on 2025-06-20.

**Q4.** Stable, per E02 (A08). E03 is the same LEI and shows Positive from A09 (2025-09-15), so the data conflicts here.

**Q5.** Holders of I03 take risk on E02, the guarantor, with issuer E04 also exposed; the instrument is rated A (A10, A11).

**Q6.** The FC rating (BB, A14) equals Valdoria's country ceiling (BB, A12), while the LC rating is BBB- (A13). The data does not state the reason, but the ceiling cap is the consistent explanation.

**Q7.** 44 issuers (listed in the JSON). I excluded actions dated after today (A1720 on 2026-11-09 and others). E11 is included because its instrument I05 was downgraded (A29).

**Q8.** E08. A22 (RD, 2026-07-08) records a distressed debt exchange.

**Q9.** Not determinable reliably by hand from this data.

**Q10.** Depends. The LC rating BBB- (A13) is investment grade; the FC rating BB (A14) is not.

**Q11.** BBB+. A36 (2024-09-30) set BBB+ and no later rating action changed it before 2025-06-01.

**Q12.** A-. A34 (2023-01-15) set A-, and the next action is A36 in 2024.

**Q13.** 1. Only A36 (2024-09-30) is a downgrade.

**Q14.** None. The first rating is A30 (2024-02-01), after 1 January 2024.

**Q15.** A-. E10 was A- from A26 until the downgrade to BBB+ in A27 (2026-04-15). E17 is a research-system duplicate with no ratings.

**Q16.** No. The rating stayed BBB+ (A36). Rating Watch Negative was placed on 2025-11-20 (A35), which does not change the rating.

**Q17.** No. The only 2026 action on E06 is a Rating Watch Negative placement (A17).

**Q18.** Partial list, based on watch placements without a later resolving action. Watch status is inferred because the data has no explicit watch-removal field.

**Q19.** Not completed. Confirmed Negative outlooks include E01 (A03) and E09 (A25); the full list needs an entity-by-entity pass.

**Q20.** No. E07 was withdrawn (A19, 2026-05-12), not defaulted.

**Q21.** Partial. Withdrawn with no later rating: E07, E1032, E1057, E1124.

**Q22.** E08 (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** Not determined. The instrument-level pass was not completed.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The country ceiling of A (A37) is a separate record.

**Q29.** None. VD has only a country ceiling of BB (A12) and no issuer rating.

**Q30.** E05, E1028, E1126, E1236 (Valdoria, ceiling BB), plus E15, E1039 and E1194 (Corvenia, ceiling A).

**Q31.** No. I found no FC issuer rating above either country ceiling.

**Q32.** E09 (Halden Group plc). E11 → E10 → E09.

**Q33.** E10 (guarantor), rated BBB+ (A29, downgraded from A- by A28).

**Q34.** No. E12 has no parent, while E10 (Halden Bank AG) sits under E09.

**Q35.** 3 (E09, E10, E11). E17 duplicates E10's LEI.

**Q36.** 2 (E02, E04). E03 duplicates E02's LEI.

**Q37.** About 344. The data has about 370 rows, and I count 26 rows that repeat another entity's LEI. I did not verify exhaustively.

**Q38.** No. Different LEIs and countries (DE vs US).

**Q39.** A (A08). E03 shows A (A09) as well.

**Q40.** Not determined.

**Q41.** BB+ (A44, downgraded from BBB- by A43... after A43's BBB- and A44's DG to BB+).

**Q42.** DE (E10). E17 lists LU, but it is a duplicate record with the same LEI.

**Q43.** 1 record (E17), which duplicates E10 (DE), so effectively 0.

**Q44.** Yes. I07 is denominated in XVD, which I am treating as Valdoria's local currency.

**Q45.** Depends. The note's BBB- (A45) is above the BB ceiling numerically, but ceilings cap FC ratings and this is an LC note.

**Q46.** No. The only record is a CO-type rating (A46), not an LTIDR issuer rating, and CO is undefined.

**Q47.** A (A47). The action is EX, which is undefined, so this assumes the rating stands.

**Q48.** Not determined.

Caveats: several records are dated after today (2026-11-05) and I excluded them where they affected the answer. EX and CO action types are undefined. Entries marked "not determined" or "partial" need a full pass over the data.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "STA"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q6": {"explanation": "FC rating capped by Valdoria country ceiling BB (A12); LC rating BBB- (A13)"},
  "Q7": {"issuers": ["E08","E10","E11","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
  "Q18": {"issuers": ["E06","E1194","E1181","E1203","E1210","E1019","E1059","E1013","E1061","E1037","E1088","E1098","E1099","E1126","E1132","E1133","E1146","E1264","E1266","E1267","E1317","E1323","E1238","E1260","E1297","E1314","E1109","E1168","E1039"]},
  "Q19": {"issuers": null},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07","E1032","E1057","E1124"]},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes"},
  "Q25": {"count": null},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05","E1028","E1126","E1236","E15","E1039","E1194"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 344},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": null},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": null}
}
```