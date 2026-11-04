**Q1.** A-. The FC issuer rating was A- from A01 (2024-03-12) and was cut to BBB only on 2025-06-20 (A02).

**Q2.** No. The only 2026 action is A03 (2026-02-10), an affirmation at BBB with the outlook moved to Negative.

**Q3.** No. I02 (the 2031 note) was cut to BB+ in A07, which is below investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15), an affirmation at A with a Positive outlook.

**Q5.** The holder takes the credit risk of E02, the guarantor, not the issuer E04. I03 is rated A (A11).

**Q6.** The data gives no explicit reason. The VD Country Ceiling is BB (A12). E05's FC rating is BB (A14) and its LC rating is BBB- (A13), so the FC rating appears to be capped at the ceiling.

**Q7.** These are the FC downgrades dated in 2026, excluding E1341, whose date (2026-11-09) is still in the future (see the JSON list). I did not check whether each of those downgrades was later reversed.

**Q8.** E08. It was rated RD on 2026-07-08 (A22).

**Q9.** About 290. 291 entities have a latest FC rating that is not withdrawn, and E02/E03 share an LEI. I could not fully reconcile the LEI counts, so this is approximate.

**Q10.** Depends. E05 is BB on FC and BBB- (investment grade) on LC.

**Q11.** BBB+. The downgrade from A- came on 2024-09-30 (A36).

**Q12.** A-, from A34.

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is dated 2024-02-01.

**Q15.** A-. E10 held A- from A26 until the downgrade on 2026-04-15. E17 is only a duplicate record of E10.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 and A33 only changed the watch and outlook.

**Q17.** No. E06 only went on Rating Watch Negative (A17), which is not a downgrade.

**Q18.** The list in the JSON is incomplete, because part of the result set was not shown to me. E06 is certain (A17).

**Q19.** The list in the JSON is incomplete, for the same reason.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default. Only E08 has an RD.

**Q21.** The list in the JSON is incomplete. These are entities whose latest action is a withdrawal.

**Q22.** E08, from A22.

**Q23.** F2, from A04.

**Q24.** Yes. BBB is investment grade.

**Q25.** 66.

**Q26.** A+, from A40.

**Q27.** A-, from A42. This sits above the CV ceiling of BBB+.

**Q28.** BBB+, from A38.

**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling (BB, A12) and no issuer rating.

**Q30.** The list in the JSON is partial. I only had the VD ceiling (BB) and the CV ceiling (BBB+), and the lists I pulled were truncated.

**Q31.** Yes. E15's FC rating is A (A41), above the CV ceiling of BBB+.

**Q32.** E09, via E11 → E10 → E09.

**Q33.** The holder takes the risk of E10, the guarantor. I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent link, so it is not part of the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10 (same LEI).

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 344. There are 370 records, 368 of them with an LEI, and those 368 share only 342 distinct LEIs, so 26 are duplicates.

**Q38.** No. They have different LEIs and different countries (DE and US).

**Q39.** A, from A09 (E03, the same entity as E02).

**Q40.** 74, counted as distinct entities by LEI.

**Q41.** BB+, from A44.

**Q42.** DE. E17 (LU) is a duplicate of E10 with the same LEI.

**Q43.** 0. The only LU record is E17, which duplicates E10 (domiciled in DE). Counting the record instead would give 1.

**Q44.** Yes. I07 is denominated in XVD, the Valdoria local currency.

**Q45.** Yes. I07 is rated BBB- (A45), above the VD ceiling of BB.

**Q46.** No. E11 only has a CO-type rating (BBB, A46), not an issuer default rating.

**Q47.** None. I08's only action is an EX (A47, 2026-09-01), so it is no longer rated.

**Q48.** 106.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E16"]},"Q8":{"entities":["E08"]},"Q9":{"count":290},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06","E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146"]},"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1158"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E05","E1028","E1101","E1126"]},"Q31":{"any":"yes"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":344},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":74},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```