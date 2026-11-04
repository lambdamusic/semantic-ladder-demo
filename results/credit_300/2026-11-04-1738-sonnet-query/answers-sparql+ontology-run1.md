**Q1.** A-. E01's rating was A- (A01, assigned 2024-03-12) until the downgrade to BBB on 2025-06-20 (A02).
**Q2.** No. The only 2026 action on E01 is A03, an affirmation with the outlook revised to Negative, which is not a downgrade.
**Q3.** No. The 2031 note is I02 (subordinated) and has been rated BB+ since A07 on 2025-06-20, which is speculative grade.
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and the latest action is A09 (2025-09-15) with outlook POS.
**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, whose latest rating is A (A09).
**Q6.** The data doesn't state a reason. It shows E05 at BB foreign-currency (A14) and BBB- local-currency (A13), and the Valdoria ceiling at BB (A12). That is consistent with a country-ceiling cap on FC, but no record says so.
**Q7.** The 31 issuers are listed in the JSON, counting only issuer long-term (LTIDR) downgrades dated 2026 (e.g. E08 A21/A22, E10 A27).
**Q8.** E08. It was rated RD on 2026-07-08 (A22); E07 was only withdrawn.
**Q9.** 278. This counts distinct LEIs, plus the sovereign CV, with a non-withdrawn long-term issuer rating on 2026-10-01 and QA excluded.
**Q10.** No on the headline foreign-currency rating, which is BB (A14). Its local-currency rating is BBB- (A13), which is investment grade.
**Q11.** BBB+. E14 was downgraded on 2024-09-30 (A36) and nothing changed before 2025-06-01.
**Q12.** A-, from A34 (assigned 2023-01-15).
**Q13.** 1. Only A36 is a downgrade; the Rating Watch (A35) is not.
**Q14.** None. E12 was first rated on 2024-02-01 (A30).
**Q15.** A-. E10's rating was A- (A26) until the downgrade on 2026-04-15 (A27).
**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now (A35 and A33 leave it unchanged).
**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative, which is not a downgrade.
**Q18.** The 32 issuers are in the JSON. They are the entities whose latest long-term action on 2026-10-01 carried Rating Watch Negative.
**Q19.** The 28 issuers are in the JSON. They are the entities whose latest long-term action on 2026-10-01 carried a Negative outlook.
**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.
**Q21.** The 37 entities in the JSON have a latest long-term action of WD. This includes E07 (A19) and excludes E1106, which was withdrawn on local currency only and still has a foreign-currency rating.
**Q22.** E08 only, rated RD (A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's long-term issuer rating is BBB (A03).
**Q25.** 66 instruments held an investment-grade rating on 2026-10-01, with expected-rating (EX) actions ignored.
**Q26.** A+ (A40, E15 local-currency).
**Q27.** A- (A42, I06).
**Q28.** BBB+ (A38).
**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.
**Q30.** Five VD-domiciled entities sit at the BB ceiling, and E1039, E1194 and E15 sit at the A ceiling for CV. The sovereign CV is excluded.
**Q31.** No. Every VD entity is at or below BB and every CV entity is at or below A.
**Q32.** E09, via E11 → E10 → E09.
**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ by A27.
**Q34.** No. E12 has no parent recorded, so the data links it to no group.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.
**Q36.** 2: E02 and E04. E03 is the same entity as E02.
**Q37.** 331. This counts distinct LEIs plus the two sovereigns, with QA records excluded.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A (A09).
**Q40.** 66 distinct GB-domiciled issuers (by RATINGS-record country) hold an issuer rating.
**Q41.** None. E16 is a QA record and must be ignored.
**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.
**Q43.** 0. The only LU record is E17, which is the same entity as E10 (DE per RATINGS).
**Q44.** Yes. I07 is in XVD, the domestic currency of VD.
**Q45.** No. I07 is rated BBB- (A45), but local-currency debt is not capped by the ceiling.
**Q46.** No. E11 has no issuer-rating actions; it is a finance subsidiary relying on its parent.
**Q47.** None. I08 has only an Expected rating (A47, EX), not an assigned rating.
**Q48.** 106 instruments held a rating on 2026-10-01, with expected-rating (EX) actions ignored.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307","E08","E10"]},
"Q8":{"entities":["E08"]},"Q9":{"count":278},"Q10":{"investment_grade":"no"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323","E06"]},
"Q19":{"issuers":["E01","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1282","E1294","E1300","E09"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320","E07"]},
"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":66},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},
"Q30":{"entities":["E1028","E1101","E1126","E05","E1236","E1039","E1194","E15"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":331},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":66},"Q41":{"rating":"none"},"Q42":{"country":"DE"},"Q43":{"count":0},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"no"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":106}}
```