Notes on the data:
- "Current" means as of 5 Nov 2026. Several actions are dated after that (A1720, A1029, A1011, A1713, A1078), so I excluded them.
- Some entities have a RESEARCH record with the same LEI as a RATINGS record. I treat them as one legal entity, and where they conflict I say so.
- The `EX` and `CO` action codes are undefined. I treat `EX` as a rating action and `CO` as not an issuer rating.
- Q9, Q19 and Q40 need a full per-entity pass that I did not complete reliably, so I've left them unresolved.

**Q1.** A-. A01 (2024-03-12) assigned A-, and the downgrade to BBB came in A02 on 2025-06-20, after the date.

**Q2.** No. A02 (2025-06-20) is the only downgrade; A03 and A04 (2026-02-10) are affirmations, with A03 moving the outlook to NEG.

**Q3.** No, BB+. I02 was downgraded from BBB to BB+ in A07 (2025-06-20).

**Q4.** STA. E02's latest action, A08, carries STA. However, E03 (a RESEARCH record with the same LEI) shows POS in A09 (2025-09-15), and the data does not reconcile the two.

**Q5.** E02 (rating A). I03 is issued by E04 and guaranteed by E02, so the holder's main exposure is to the guarantor; I03 is rated A (A11), matching E02's A (A08).

**Q6.** The data does not state a reason. E05's FC rating (BB, A14) equals the Valdoria country ceiling (BB, A12), which is consistent with a ceiling cap, but the data does not say so.

**Q7.** 43 entities. These are the issuers with a DG action dated 2026 up to 5 Nov, from a manual pass: E08, E10, E16, E1034, E1051, E1053, E1057, E1058, E1064, E1080, E1093, E1112, E1144, E1151, E1159, E1161, E1163, E1167, E1170, E1186, E1213, E1228, E1229, E1243, E1255, E1263, E1285, E1290, E1294, E1299, E1300, E1307, E1340, E1342, E1343, E1344, E1345, E1346, E1347, E1348, E1349, E1350, E1351. E1341 has a DG dated 2026-11-09 (A1720), which is future-dated and excluded.

**Q8.** E08. A22 (2026-07-08) sets RD, and there is no later action.

**Q9.** Not resolved. This needs a latest-state pass over every LTIDR entity as of 1 Oct 2026, which I did not complete reliably.

**Q10.** Depends on currency. The LC rating is BBB- (A13), which is investment grade, but the FC rating is BB (A14), which is not.

**Q11.** BBB+. A36 (2024-09-30) moved E14 from A- to BBB+, and no later rating change happened before 2025-06-01.

**Q12.** A-. A34 (2023-01-15) assigned A-, and the first later change is A36 on 2024-09-30.

**Q13.** 1. Only A36 (2024-09-30) is a downgrade; A33 is an affirmation and A35 is a watch placement.

**Q14.** None. E12's first rating action is A30 (2024-02-01), after the date.

**Q15.** A-. A26 (2023-05-01) assigned A-, and the downgrade to BBB+ is A27 (2026-04-15), after the date.

**Q16.** No. E14 has been BBB+ since A36 and was only placed on watch (A35, 2025-11-20) and affirmed (A33, 2026-05-01).

**Q17.** No. E06 was placed on Rating Watch Negative at A- (A17, 2026-09-03), with no downgrade.

**Q18.** 30 issuers. Each is an entity whose latest RW action carries RWN and was not followed by a resolving action (AF, UG, DG or WD) before 1 Oct 2026. Treating a later UG/AF as resolving the watch is my assumption. The list is E06, E1267, E1194, E1203, E1242, E1039, E1133, E1088, E1210, E1019, E1317, E1098, E1059, E1132, E1146, E1013, E1099, E1109, E1264, E1266, E1314, E1061, E1037, E1238, E1297, E1323, E1181, E1260, E1168, E1126.

**Q19.** Not resolved. This needs a full latest-outlook pass, which I did not complete.

**Q20.** No. E07 was withdrawn (A19, 2026-05-12, commercial reasons), not defaulted. The only default record is the RD on E08 (A22).

**Q21.** 34 entities. Each has a last LTIDR action of WD before 1 Oct 2026 with no later rating. Exceptions: E1115 and E1303 were rated again after WD (A1250, A1649), and E1158 was rated again after WD (A1338); E1002 (research duplicate) carries the Tunod rating, since E1001 has no actions.

**Q22.** E08. It is the only entity with an RD action (A22).

**Q23.** F2. A04 (2026-02-10) affirmed the short-term rating at F2.

**Q24.** Yes. The issuer rating is BBB (A03, 2026-02-10), which is investment grade.

**Q25.** 69 instruments. This counts EX actions as ratings (I08, I1012, I1021). I1001, I1007 and I1015 have only future-dated actions, so they are unrated. If EX ends a rating, the count falls to 66.

**Q26.** A+. A40 (2024-03-01) assigned A+ on the LC basis.

**Q27.** A-. A42 (2024-03-01) assigned A- to I06.

**Q28.** BBB+. A38 (2024-01-01) is the FC issuer rating. The CC A (A37) is a ceiling, not an issuer rating.

**Q29.** None. VD has a country ceiling of BB (A12) but no issuer rating record.

**Q30.** E05, E1028, E1101, E1126, E1236 (Valdoria, ceiling BB) and E15, E1039, E1194 (Corvenia, ceiling A). The ceilings are dated 2025-04-01 and 2024-01-01 and I assume they still apply on 1 Oct 2026.

**Q31.** No. Where ceilings are known, no FC rating is above them. The data has no ceilings for other countries.

**Q32.** E09. E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (rating BBB+). I05 is guaranteed by E10, and E10's BBB+ rating comes from A27 (2026-04-15).

**Q34.** No. E12 has no parent_id linking it to E09 or E10. The name similarity is not evidence of a group relationship.

**Q35.** 3 (E09, E10, E11). E17 has the same LEI as E10 and is not counted separately.

**Q36.** 2 (E02, E04). E03 has the same LEI as E02.

**Q37.** 344. There are 370 entity rows, and 26 RESEARCH rows share an LEI with a RATINGS row.

**Q38.** No. E06 (LEI 549300AMVE3VRVG7HK43) and E13 (LEI 815600O8X8K2F154N214) have different LEIs.

**Q39.** A (A08, E02). The E03 research record also shows A (A09).

**Q40.** Not resolved. This needs the same full pass as Q9.

**Q41.** BB+. A44 (2026-06-01) downgraded E16 from BBB- to BB+.

**Q42.** DE (E10, ratings record). The E17 research record, with the same LEI, says LU, which conflicts.

**Q43.** 1 (E17, LU). Its LEI is the same as E10 (DE), so it may not be a separate entity.

**Q44.** Yes, probably. I07 is denominated in XVD, and its BBB- rating matches Valdoria's LC rating (A13). The data does not define XVD as local currency.

**Q45.** No. The ceiling caps FC ratings, and I07 is in XVD, which is likely local currency. BBB- would exceed the BB ceiling only if the note were FC.

**Q46.** No. E11 has only a CO record (A46, BBB), not an LTIDR issuer rating, and CO is not defined.

**Q47.** A. A47 (2026-09-01) shows A with action EX, which is undefined, so this is provisional.

**Q48.** 112. This counts EX as a rating; I001, I1007 and I1015 are unrated. If EX ends a rating, the count is 106.

```json
{"Q1": {"rating": "A-"},
 "Q2": {"downgraded": "no"},
 "Q3": {"investment_grade": "no", "rating": "BB+"},
 "Q4": {"outlook": "STA"},
 "Q5": {"risk_of": "E02", "rating": "A"},
 "Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
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
 "Q18": {"issuers": ["E06","E1267","E1194","E1203","E1242","E1039","E1133","E1088","E1210","E1019","E1317","E1098","E1059","E1132","E1146","E1013","E1099","E1109","E1264","E1266","E1314","E1061","E1037","E1238","E1297","E1323","E1181","E1260","E1168","E1126"]},
 "Q19": {"issuers": null},
 "Q20": {"in_default": "no"},
 "Q21": {"entities": ["E07","E1032","E1063","E1138","E1140","E1155","E1159","E1172","E1166","E1041","E1062","E1076","E1107","E1121","E1124","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E1007","E1021","E1002","E1057"]},
 "Q22": {"entities": ["E08"]},
 "Q23": {"rating": "F2"},
 "Q24": {"investment_grade": "yes"},
 "Q25": {"count": 69},
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
 "Q37": {"count": 344},
 "Q38": {"same": "no"},
 "Q39": {"rating": "A"},
 "Q40": {"count": null},
 "Q41": {"rating": "BB+"},
 "Q42": {"country": "DE"},
 "Q43": {"count": 1},
 "Q44": {"local_currency": "yes"},
 "Q45": {"above_ceiling": "no"},
 "Q46": {"issuer_rating": "no"},
 "Q47": {"rating": "A"},
 "Q48": {"count": 112}}
```