**Q1.** A-. E01's rating on 2025-01-01 was still the A- assigned in A01; the downgrade to BBB (A02) came on 2025-06-20.
**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook.
**Q3.** No. The 2031 note is I02 (subordinated), downgraded to BB+ in A07, which is speculative grade.
**Q4.** Positive. E03 has the same LEI as E02, so it is the same entity, and its latest action A09 (2025-09-15) is an affirmation at A with a POS outlook.
**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so the holder takes the guarantor's risk, and E02's latest rating is A (A09 on E03).
**Q6.** Valdoria's Country Ceiling (A12) is BB, which caps foreign-currency ratings. E05's FC rating is therefore BB (A14), while its uncapped LC rating is BBB- (A13).
**Q7.** 38 issuers (list in the JSON). These are the non-QA issuer ratings with a DG action dated 2026, with duplicate-LEI records merged. This includes E5033, whose DG (A5028) is dated 2026-11-06, after today's date.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), which is a default.
**Q9.** 377. This counts distinct LEIs whose latest LTIDR/STIDR action on 1 Oct 2026 is not WD, excluding QA records.
**Q10.** Depends. E05's FC rating is BB (speculative grade) and its LC rating is BBB- (investment grade).
**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30, and the next action is on 2025-11-20.
**Q12.** A-. A34 assigned A- on 2023-01-15, before the downgrade.
**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 is an affirmation.
**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.
**Q15.** A-. E10 was assigned A- in A26, and the downgrade A27 only came on 2026-04-15. E17 is the same entity as E10 and has no actions of its own.
**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; the Watch and the affirmation did not change the rating.
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative placement, which is not a downgrade.
**Q18.** 32 issuers (list in the JSON). Each has a Watch Negative as its latest action on 1 Oct 2026, not cleared by a later action.
**Q19.** 43 issuers (list in the JSON). Each has a NEG outlook on its latest action as of 1 Oct 2026. I treated a Watch action, which carries no outlook, as clearing the outlook.
**Q20.** No. E07 never went below BB and its rating was withdrawn (A19), which is not a default.
**Q21.** 36 entities (list in the JSON). Each had an issuer rating that was withdrawn, with no later action restoring it by 1 Oct 2026. Where a later action followed a withdrawal (E1115, E1303, E1158), the later action holds, so those entities still have a rating.
**Q22.** E08. It is the only entity ever rated RD or D (A22).
**Q23.** F2 (A04, STIDR on E01).
**Q24.** Yes. E01's current LTIDR is BBB (A03).
**Q25.** 72. These are the instruments whose latest INST rating on 1 Oct 2026 is BBB- or higher; EX actions are not ratings.
**Q26.** A+ (A40, LC LTIDR on E15).
**Q27.** A-. I06 was assigned A- in A42.
**Q28.** BBB+ (A38, FC LTIDR on CV).
**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.
**Q30.** 13 entities (list in the JSON). These are entities domiciled in VD (ceiling BB) or CV (ceiling A) whose latest FC rating equals the ceiling. For domicile I used the RESEARCH record where records disagree.
**Q31.** No. No VD entity has an FC rating above BB, and no CV entity has one above A.
**Q32.** E09. E11's parent is E10, whose parent is E09.
**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).
**Q34.** No. E12 has no parent, so it is its own group.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 497. That is 540 records, less 14 QA records and 29 duplicate-LEI records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A09).
**Q40.** 79. These are GB-domiciled entities with an issuer rating still in force on 1 Oct 2026, counting each LEI once.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record E17 holds for domicile and says LU, while the RATINGS record E10 says DE.
**Q43.** 1. Only E10/E17, the same entity, is domiciled in LU.
**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where issuer E05 is domiciled.
**Q45.** No. The ceiling caps only foreign-currency debt, and I07 is local-currency debt.
**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not an issuer rating.
**Q47.** None. I08 has only an Expected rating (A47, EX), so it is still unrated.
**Q48.** 113. Of 122 instruments, 9 have only EX actions.
**Q49.** E5001. The chain is E5047, E5035, E5023, E5011, E5167 (same entity as E5005), E5002, E5001.
**Q50.** 6 levels along that chain.
**Q51.** 58, being E5001–E5058; E5167 is the same entity as E5005, and E5170 is QA.
**Q52.** 19, being E5086–E5104. The research record E5168 names a Rotam parent, but RATINGS holds parent links and puts E5062 under Belir.
**Q53.** No. E5062's RATINGS parent chain ends at E5059 (Belir Group).
**Q54.** E5106, E5124 and E5130. E5106 is VD by the RESEARCH record E5169.
**Q55.** 31. These are rated entities below a VD-domiciled ancestor: 6 under E5005, 2 under E5091, 1 under E5124, 8 under E5106 and 14 under E5145.
**Q56.** BB-. Among Vesol members, E5144 is the lowest at BB- (A5108); the others are BB or higher.
**Q57.** E5002. E5011 and E5013 both pass through it on the way to E5001.
**Q58.** E5145. It guarantees I5007, issued by E5133, which sits in the Vesol group. All other guarantors are the issuer's own parent.
**Q59.** 12, being E5011–E5022.
**Q60.** E5145 (Geren Group). I5007 is guaranteed by E5145, which is not in the issuer E5133's group.
**Q61.** 19 Cerid members hold a latest FC rating below BBB- (listed in the earlier rating records E5007 through E5048).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1169","E1051","E1080","E1307","E1167","E5116","E5059","E5097","E1298","E1160","E1290","E5019","E1294","E1285","E5033","E1093","E1112","E1263","E1255","E1064","E1053","E1058","E1057","E1186","E1228","E1243","E1159","E1163","E1144","E1034","E1213","E1300","E5113","E5156","E1229","E1151"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 377},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1264","E1098","E1061","E1209","E1181","E1037","E1099","E1006","E1059","E1267","E1088","E1019","E1109","E1260","E1242","E1203","E1194","E1146","E1132","E1133","E1266","E1314","E1317","E1297","E1039","E1013","E1066","E1126","E1238","E1168","E1323"]},
"Q19": {"issuers": ["E01","E09","E1056","E1080","E1190","E5039","E1046","E1029","E1072","E5050","E1118","E1211","E1282","E1261","E1263","E1300","E1294","E1228","E1271","E5013","E5020","E5019","E5023","E5057","E5059","E5062","E5073","E5097","E5099","E5102","E5113","E5116","E5119","E5131","E5141","E5156","E1158","E1034","E1064","E1079","E1188","E1055","E1005"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1277","E1140","E1225","E1218","E1107","E1234","E1166","E1172","E1253","E1021","E1062","E1007","E1063","E1138","E1048","E1076","E1200","E1206","E1219","E1320","E1316","E1308","E1159","E1155","E1057","E1001","E1032","E1041","E1124","E1121","E1205","E1233","E1244","E1084"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 72},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E1028","E1101","E1126","E1236","E5012","E5047","E5091","E5124","E15","E1039","E1194","E5116"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 497},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 79},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 113},
"Q49": {"parent": "E5001"},
"Q50": {"count": 6},
"Q51": {"count": 58},
"Q52": {"count": 19},
"Q53": {"same_group": "no"},
"Q54": {"entities": ["E5106","E5124","E5130"]},
"Q55": {"count": 31},
"Q56": {"rating": "BB-"},
"Q57": {"entity": "E5002"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": 19}
}
```