**Q1.** A-. E01 was rated A- (A01, 2024-03-12) and downgraded to BBB on 2025-06-20 (A02), so A- applied on 1 Jan 2025.
**Q2.** No. E01's only 2026 actions were affirmations at BBB with a Negative outlook (A03, A04).
**Q3.** No. The 2031 note I02 was cut to BB+ (A07), which is below investment grade.
**Q4.** Positive. E02 and E03 share one LEI, so they are one entity. The latest action is A09 (2025-09-15, A, POS).
**Q5.** The holder takes the guarantor E02's risk (I03 is issued by E04 and guaranteed by E02). E02 is rated A, as is the note (A10, A11).
**Q6.** The data gives no explicit reason. E05's local-currency rating is BBB- (A13) and its foreign-currency rating is BB (A14). The Country Ceiling for VD is BB (A12), which fits a cap on the foreign-currency rating.
**Q7.** See JSON. These are the entities with a 2026 downgrade action on a long-term rating.
**Q8.** E08 only. It was downgraded to RD on 2026-07-08 (A22).
**Q9.** 391. This counts distinct LEIs whose latest issuer rating on either currency basis is not WD.
**Q10.** Depends. Its local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not).
**Q11.** BBB+ (A36, 2024-09-30).
**Q12.** A- (A34).
**Q13.** 1 (A36).
**Q14.** None. The first rating for E12 is dated 2024-02-01 (A30).
**Q15.** A-. E10 and E17 share an LEI, and the downgrade to BBB+ came only on 2026-04-15 (A27).
**Q16.** No. The rating was BBB+ on 1 Jan 2025 and is still BBB+ (A35 and A33 were a watch and an affirmation).
**Q17.** No. E06's only 2026 action was a Rating Watch Negative at A- (A17).
**Q18.** E06 (A17). This list may be incomplete, because my query mishandled watch rows.
**Q19.** See JSON. These are the entities whose latest foreign-currency or local-currency rating action carried a Negative outlook.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of default.
**Q21.** See JSON. These are the entities whose latest rating on every basis is WD.
**Q22.** E08 only, through the RD of A22. I did not query for D or SD separately beyond that.
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB.
**Q25.** 72. This is the number of instruments rated BBB- or higher on 1 Oct 2026, excluding EX and WD actions.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria has only a Country Ceiling of BB (A12) and no issuer rating.
**Q30.** See JSON. The ceilings are A for CV and BB for VD, and these entities' foreign-currency ratings equal them.
**Q31.** No. No CV entity is rated above A and no VD entity is rated above BB.
**Q32.** E09 (E11 → E10 → E09).
**Q33.** E10, the guarantor of I05 (A29), is rated BBB+.
**Q34.** No. E12 has no parent link, and the Halden group is E09, E10 and E11.
**Q35.** 3.
**Q36.** 2 (E02 and E04). E03 duplicates E02.
**Q37.** 511. This is the number of distinct LEIs among the 540 entity records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (E02/E03).
**Q40.** 87 (distinct LEIs).
**Q41.** BB+ (A44).
**Q42.** DE. E10 is the RATINGS record, and E17 (LU) is a duplicate research record with the same LEI.
**Q43.** 0. The only LU record, E17, duplicates the DE entity E10.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.
**Q45.** Yes. I07 is rated BBB-, above the VD ceiling of BB.
**Q46.** No. E11 has only a counterparty rating (A46), not a long-term issuer rating.
**Q47.** None. I08's only action is an EX action (A47), which I treat as not an in-force rating.
**Q48.** 113.
**Q49.** E5167, as the chain runs E5047 → E5035 → E5023 → E5011 → E5167.
**Q50.** 4.
**Q51.** 55.
**Q52.** 19. I excluded the research duplicate E5168, which carries a conflicting Rotam parent link.
**Q53.** No. E5062 is under Belir, and E5168 is a duplicate record that conflicts.
**Q54.** E5124 and E5130.
**Q55.** 23.
**Q56.** BB- (E5144).
**Q57.** None found. E5011's chain ends at E5167, and E5013's chain runs E5006 → E5002 → E5001 with no overlap.
**Q58.** E5145 guarantees I5007, issued by E5133 in a different group.
**Q59.** 11.
**Q60.** The holder takes the guarantor E5145's risk. It is not in the same group as the issuer E5133, which sits under E5132.
**Q61.** 18.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E1285","E1300","E1151","E1167","E1080","E5113","E1051","E10","E1034","E1347","E1343","E1290","E1350","E1341","E1229","E1342","E5097","E1351","E5059","E1255","E1340","E16","E1186","E1161","E1263","E1058","E1349","E1112","E08","E5116","E1170","E1344","E1228","E1163","E1243","E5033","E1299","E5019","E1053","E1348","E1213","E1346","E1159","E1057","E1345","E1064","E1294","E1093","E1144","E1307","E5156"]},"Q8":{"entities":["E08"]},"Q9":{"count":391},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E1300","E5099","E1064","E5113","E5039","E1161","E5141","E1080","E1105","E1072","E1211","E1005","E1034","E1347","E1343","E1271","E1118","E1158","E1056","E1248","E1350","E1345","E5062","E1342","E5057","E1055","E5097","E1351","E1046","E5059","E5020","E1340","E1263","E1348","E5073","E1188","E1282","E01","E5102","E1029","E5131","E5023","E5116","E09","E1344","E1228","E1060","E1079","E5019","E5050","E1262","E5013","E1190","E5119","E1294","E5170","E5156"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1002","E1084","E1032","E1234","E1219","E1206","E1107","E1244","E1172","E1159","E1057","E1041","E07","E1062","E1277","E1155","E1254","E1121","E1063","E1166","E1021","E1200","E1048","E1124","E1076","E1138","E1140","E1316","E1308","E1007","E1218","E1225","E1205","E1320","E1233"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":72},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E1194","E15","E5116","E1039","E1101","E1028","E1126","E5012","E1236","E5047","E5124","E5091","E05"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":87},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5167"},"Q50":{"count":4},"Q51":{"count":55},"Q52":{"count":19},"Q53":{"same_group":"no"},"Q54":{"entities":["E5124","E5130"]},"Q55":{"count":23},"Q56":{"rating":"BB-"},"Q57":{"entity":"none"},"Q58":{"entities":["E5145"]},"Q59":{"count":11},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":18}}
```