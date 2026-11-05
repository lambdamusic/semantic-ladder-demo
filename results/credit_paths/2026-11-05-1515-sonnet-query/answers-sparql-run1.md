**Q1.** A-. The 2024-03-12 assignment (A01) held until the 2025-06-20 downgrade (A02).
**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the outlook went to Negative but the rating stayed BBB.
**Q3.** No. The 2031 note I02 is rated BB+ (A07), which is below investment grade.
**Q4.** Positive. E03 shares E02's LEI, so it is the same company, and its latest action is A09 (2025-09-15), which carries a Positive outlook.
**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 and guaranteed by E02, and I03 itself is rated A (A11).
**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13).
**Q7.** E08, E10, E16 and the block E1121–E1324 had a downgrade on an issuer rating in 2026 (the IDs are listed in the JSON). I did not check whether any of the E11xx–E13xx block were later restored.
**Q8.** E08 (Saxby Shipping). It was rated RD from 2026-07-08 (A22).
**Q9.** 391. I counted distinct LEIs that had a long-term issuer rating on 1 October 2026 that was not withdrawn, which merges alias records. This includes the sovereign CV and excludes the withdrawn E07.
**Q10.** Depends. It is BB on a foreign-currency basis and BBB- on a local-currency basis (A14, A13).
**Q11.** BBB+. The downgrade in A36 (2024-09-30) was still in force on 1 June 2025.
**Q12.** A-. Marlow was A- from 2023-01-15 (A34) until the 2024-09-30 downgrade.
**Q13.** 1. The only downgrade is A36; A35 is a Rating Watch Negative, not a downgrade.
**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.
**Q15.** A-. Halden Bank's downgrade to BBB+ (A27) came on 2026-04-15, after that date.
**Q16.** No. Marlow was BBB+ on 1 January 2025 and is still BBB+ (A33). Only the watch status moved.
**Q17.** No. The only 2026 action on Orrin Bank (E06) is a Rating Watch Negative at A- (A17).
**Q18.** E06 and a large block of E11xx–E13xx entities (listed in the JSON). I took the latest long-term rating action per currency basis as of 1 October 2026.
**Q19.** E01, E09 and E1122–E1324 (205 issuers), using the same latest-action rule.
**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19) and there is no default rating on it.
**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).
**Q22.** E08 only (RD, A22).
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** Not determined. My queries for instrument counts returned nothing usable.
**Q26.** A+ (A40, local-currency).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. Valdoria (VD) has only a Country Ceiling of BB (A12) and no issuer rating.
**Q30.** Not fully determined. E05 at BB (ceiling BB) and E15 at A (ceiling A) are at the ceiling, but I could not scan all CV and VD entities.
**Q31.** Not determined, for the same reason. The two cases I checked (E05, E15) are exactly at the ceiling, not above it.
**Q32.** E09 (E11 → E10 → E09).
**Q33.** Halden Bank (E10), rated BBB+. I05 is issued by E11 and guaranteed by E10, and I05 itself is rated BBB+ (A29).
**Q34.** No. E12 has no parent, while E10 sits under E09.
**Q35.** 3: E09, E10, E11.
**Q36.** 2: E02 and E04. E03 is an alias of E02 (same LEI).
**Q37.** 511. There are 540 records, 509 distinct LEIs, and 2 records without an LEI (CV, VD).
**Q38.** No. E06 (DE) and E13 (US) have different LEIs and no link between them.
**Q39.** A, per the E02/E03 records (same LEI). The latest action is A09 on 2025-09-15, an affirmation of A.
**Q40.** 87. This is distinct LEIs among non-sovereign GB-domiciled issuers rated on 1 October 2026.
**Q41.** BB+ (A44, downgraded 2026-06-01).
**Q42.** DE (E10). E17 is a duplicate record with the same LEI, shown with domicile LU.
**Q43.** 1. The only LU record is E17, which is an alias of Halden Bank.
**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.
**Q45.** Yes. I07 is rated BBB- (A45) against a BB ceiling for VD (A12).
**Q46.** No. E11 has only a counterparty-type rating (A46, BBB), not a long-term issuer rating.
**Q47.** A (A47). The action is coded EX, which the data does not explain.
**Q48.** Not determined, for the same reason as Q25.
**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 → E5001, and E5167 is a research-system duplicate of E5001 (same LEI).
**Q50.** 4 levels, because E5167 is the same entity as E5001 and adds no level.
**Q51.** 166. The group query returned 167 records, one of which is the duplicate E5167.
**Q52.** 19 (E5086–E5104).
**Q53.** No. Belir Mining (E5062) sits under root E5059 and Rotam under E5086.
**Q54.** Not determined. The Wonod member countries came back truncated.
**Q55.** Not determined. The query returned nothing usable.
**Q56.** Not determined. The Vesol ratings query returned nothing usable.
**Q57.** E5001. E5011's parent is E5167, which is an alias of E5001, and E5013's chain (E5006 → E5002) also ends at E5001.
**Q58.** E5145, guaranteeing I5007. Its issuer E5133 sits in the E5132 group. I could not fully verify the E1093–E1107 pairs, which looked group-internal.
**Q59.** 12, estimated from the tree structure. The 12 are E5012–E5022 (11 entities) plus E5035, which I count one level higher because E5011 hangs off E5167. I could not confirm this against the full 167-member group.
**Q60.** Vesol Group's E5145. It is not in the same group as the issuer E5133, which is under the E5132 root.
**Q61.** Not determined. The query returned nothing usable.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1121","E1122","E1123","E1124","E1125","E1126","E1127","E1128","E1129","E1130","E1131","E1132","E1133","E1134","E1135","E1136","E1137","E1138","E1139","E1140","E1141","E1142","E1143","E1144","E1145","E1146","E1147","E1148","E1149","E1150","E1151","E1152","E1153","E1154","E1155","E1156","E1157","E1158","E1159","E1160","E1161","E1162","E1163","E1164","E1165","E1166","E1167","E1168","E1169","E1170","E1171","E1172","E1173","E1174","E1175","E1176","E1177","E1178","E1179","E1180","E1181","E1182","E1183","E1184","E1185","E1186","E1187","E1188","E1189","E1190","E1191","E1192","E1193","E1194","E1195","E1196","E1197","E1198","E1199","E1200","E1201","E1202","E1203","E1204","E1205","E1206","E1207","E1208","E1209","E1210","E1211","E1212","E1213","E1214","E1215","E1216","E1217","E1218","E1219","E1220","E1221","E1222","E1223","E1224","E1225","E1226","E1227","E1228","E1229","E1230","E1231","E1232","E1233","E1234","E1235","E1236","E1237","E1238","E1239","E1240","E1241","E1242","E1243","E1244","E1245","E1246","E1247","E1248","E1249","E1250","E1251","E1252","E1253","E1254","E1255","E1256","E1257","E1258","E1259","E1260","E1261","E1262","E1263","E1264","E1265","E1266","E1267","E1268","E1269","E1270","E1271","E1272","E1273","E1274","E1275","E1276","E1277","E1278","E1279","E1280","E1281","E1282","E1283","E1284","E1285","E1286","E1287","E1288","E1289","E1290","E1291","E1292","E1293","E1294","E1295","E1296","E1297","E1298","E1299","E1300","E1301","E1302","E1303","E1304","E1305","E1306","E1307","E1308","E1309","E1310","E1311","E1312","E1313","E1314","E1315","E1316","E1317","E1318","E1319","E1320","E1321","E1322","E1323","E1324"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 391},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1130","E1186","E1196","E1202","E1205","E1206","E1207","E1208","E1209","E1210","E1211","E1212","E1213","E1214","E1216","E1217","E1218","E1219","E1220","E1221","E1222","E1223","E1224","E1225","E1226","E1227","E1229","E1230","E1231","E1232","E1235","E1236","E1237","E1238","E1239","E1240","E1242","E1243","E1244","E1245","E1246","E1247","E1248","E1249","E1250","E1251","E1252","E1253","E1254","E1255","E1256","E1257","E1258","E1259","E1260","E1261","E1262","E1263","E1264","E1265","E1266","E1267","E1268","E1269","E1270","E1271","E1272","E1273","E1274","E1275","E1276","E1277","E1278","E1279","E1280","E1281","E1282","E1283","E1284","E1285","E1286","E1287","E1288","E1289","E1290","E1291","E1292","E1293","E1294","E1295","E1296","E1297","E1298","E1299","E1300","E1301","E1302","E1303","E1304","E1305","E1306","E1307","E1308","E1309","E1310","E1311","E1312","E1313","E1314","E1315","E1316","E1317","E1318","E1319","E1320","E1321","E1322","E1323","E1324"]},
"Q19": {"issuers": ["E01","E09","E1122","E1123","E1124","E1125","E1126","E1127","E1128","E1129","E1130","E1131","E1132","E1133","E1134","E1135","E1136","E1137","E1138","E1139","E1140","E1141","E1142","E1143","E1144","E1145","E1146","E1147","E1148","E1149","E1150","E1151","E1152","E1153","E1154","E1155","E1156","E1157","E1158","E1159","E1160","E1161","E1162","E1163","E1164","E1165","E1166","E1167","E1168","E1169","E1170","E1171","E1172","E1173","E1174","E1175","E1176","E1177","E1178","E1179","E1180","E1181","E1182","E1183","E1184","E1185","E1186","E1187","E1188","E1189","E1190","E1191","E1192","E1193","E1194","E1195","E1196","E1197","E1198","E1199","E1200","E1201","E1202","E1203","E1204","E1205","E1206","E1207","E1208","E1209","E1210","E1211","E1212","E1213","E1214","E1215","E1216","E1217","E1218","E1219","E1220","E1221","E1222","E1223","E1224","E1225","E1226","E1227","E1228","E1229","E1230","E1231","E1232","E1233","E1234","E1235","E1236","E1237","E1238","E1239","E1240","E1241","E1242","E1243","E1244","E1245","E1246","E1247","E1248","E1249","E1250","E1251","E1252","E1253","E1254","E1255","E1256","E1257","E1258","E1259","E1260","E1261","E1262","E1263","E1264","E1265","E1266","E1267","E1268","E1269","E1270","E1271","E1272","E1273","E1274","E1275","E1276","E1277","E1278","E1279","E1280","E1281","E1282","E1283","E1284","E1285","E1286","E1287","E1288","E1289","E1290","E1291","E1292","E1293","E1294","E1295","E1296","E1297","E1298","E1299","E1300","E1301","E1302","E1303","E1304","E1305","E1306","E1307","E1308","E1309","E1310","E1311","E1312","E1313","E1314","E1315","E1316","E1317","E1318","E1319","E1320","E1321","E1322","E1323","E1324"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": null},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05","E15"]},
"Q31": {"any": null},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 511},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 87},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "yes"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "A"},
"Q48": {"count": null},
"Q49": {"parent": "E5001"},
"Q50": {"count": 4},
"Q51": {"count": 166},
"Q52": {"count": 19},
"Q53": {"same_group": "no"},
"Q54": {"entities": []},
"Q55": {"count": null},
"Q56": {"rating": null},
"Q57": {"entity": "E5001"},
"Q58": {"entities": ["E5145"]},
"Q59": {"count": 12},
"Q60": {"risk_of": "E5145", "same_group": "no"},
"Q61": {"count": null}
}
```