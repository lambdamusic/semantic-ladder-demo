**Q1.** A-. A01 (2024-03-12) assigned E01 A-, and the next action is A02 on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation at BBB with a Negative outlook, which is not a downgrade.

**Q3.** No. The 2031 note I02 is subordinated and was downgraded to BB+ by A07, so it is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and A09 (2025-09-15) affirmed A with a Positive outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02, same entity as E03). I03 is guaranteed by E02, whose rating is A.

**Q6.** The Country Ceiling for Valdoria (VD) is BB (A12). It caps the foreign-currency rating at BB (A14), while the local-currency rating of BBB- (A13) is not capped.

**Q7.** Thirty-one issuers were downgraded in 2026, listed in the JSON. QA records are excluded, and research-record actions are mapped to the RATINGS record of the same entity.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, a default, and nothing has followed.

**Q9.** 278. This counts distinct entities (merged by LEI) whose latest long-term issuer rating is not a withdrawal and which are not QA. It includes E1158, E1115 and E1303, which have rating actions dated after a withdrawal (e.g. A1337/A1338 after A1339), so I treated them as rated.

**Q10.** Depends. Its foreign-currency rating is BB (speculative grade) and its local-currency rating is BBB- (investment grade) (A13, A14).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30.

**Q12.** A-. A34 assigned it on 2023-01-15, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 assigned E10 A- in 2023, and the downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A35 is a Watch, A33 an affirmation).

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch, which is not a downgrade.

**Q18.** Thirty-two issuers, listed in the JSON, are on Rating Watch Negative. Their latest action is a Watch (or a later action does not remove it). E1019 and E1059 are included because their local-currency ratings are on watch.

**Q19.** Twenty-six issuers have a Negative outlook, listed in the JSON. I excluded issuers whose latest action is a Watch, because that row carries no outlook.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, which is not a default.

**Q21.** Thirty-five entities, listed in the JSON, were rated at some point but have no issuer rating on 2026-10-01. In every case the latest action is a withdrawal. E1106 and E1279 are not on the list because a foreign-currency or local-currency rating remains.

**Q22.** Only E08. Its A22 rating of RD is the only default rating anywhere in the data.

**Q23.** F2 (A04).

**Q24.** Yes. Its long-term rating is BBB (A03).

**Q25.** 66. By the latest instrument rating, 5 of the 7 rated instruments among I01–I08 are investment grade (I01, I03, I05, I06, I07), and so are 61 of the 99 rated among I1001–I1107. Expected ratings (EX) are not ratings.

**Q26.** A+ (A40).

**Q27.** A-. I06 is subordinated and rated A- (A42), which is below Corvenia's A ceiling (A37).

**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** The ceilings are VD = BB and CV = A. At the ceiling are E05, E1028, E1101, E1126 and E1236 (all BB, VD), and E15, E1039 and E1194 (all A, CV).

**Q31.** No. No VD entity is rated above BB and no CV entity is rated above A on a foreign-currency basis. E1245 is domiciled in FR per RESEARCH.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes Halden Bank's credit risk (E10), because it guarantees I05. E10 is rated BBB+ (A27), and I05 is also BBB+ (A29).

**Q34.** No. E12 has no parent, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 331. There are 370 records, less 13 QA records and 26 duplicate records sharing an LEI.

**Q38.** No. Their LEIs differ (E06 549300AMVE…, E13 815600O8X8…).

**Q39.** A. E02/E03 were last affirmed at A (A11 relates to the instrument; A09 for the issuer).

**Q40.** 64. This counts GB-domiciled entities with a live issuer rating, again treating E1115 as rated after its post-withdrawal upgrade A1250.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** LU. RATINGS says DE, but RESEARCH (E17) holds for domicile and says LU.

**Q43.** 1: Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, which is Valdoria's domestic currency, and the issuer E05 is domiciled in VD.

**Q45.** No. It is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 is a finance subsidiary with only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 106 (7 of I01–I08 plus 99 of I1001–I1107). The instruments excluded as only Expected are I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046 and I1049.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1064","E1163","E1058","E1213","E1228","E1034","E1169","E1307","E1186","E1160","E1112","E1159","E1263","E1080","E1285","E1167","E1298","E1300","E1051","E1053","E1144","E1294","E1093","E1057","E1255","E1243","E1290","E1151","E1229"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 278},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1194","E1203","E1133","E1019","E1088","E1264","E1181","E1260","E1168","E1099","E1109","E1209","E1006","E1013","E1037","E1066","E1098","E1126","E1132","E1146","E1238","E1266","E1297","E1314","E1317","E1323","E1059","E1061"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1034","E1056","E1228","E1263","E1160","E1105","E1080","E1046","E1029","E1294","E1064","E1072","E1271","E1261","E1211","E1282","E1248","E1079","E1190","E1055","E1005","E1300"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
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
"Q40": {"count": 64},
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