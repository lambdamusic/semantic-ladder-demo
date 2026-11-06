**Q1.** A- (Kestrel Energy, E01). A01 set the long-term rating at A- on 2024-03-12, and the next change, A02 (BBB), came on 2025-06-20.

**Q2.** No. E01 was downgraded in 2025 (A02); in 2026 it was only affirmed at BBB with a Negative outlook (A03).

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated): A23 rated it BBB, and A07 downgraded it to BB+ on 2025-06-20.

**Q4.** Positive. The Northwind Holdings records E02 and E03 share one LEI. The latest action is A09 (2025-09-15, affirmed A, Positive outlook), which supersedes A08 (Stable).

**Q5.** The guarantor, Northwind Holdings (E02), rated A. The Finance 2030 notes (I03) are issued by E04 but guaranteed by E02, and I03 is rated A (A11).

**Q6.** The data does not state a reason. E05 has a foreign-currency (FC) rating of BB (A14) and a local-currency (LC) rating of BBB- (A13). Valdoria's country ceiling is BB (A12), which is a likely explanation but is not stated.

**Q7.** 42 issuers had a downgrade dated in 2026; see the JSON for the list. I excluded E1341's downgrade (A1720) because it is dated 2026-11-09, after today. I also excluded E11, whose only 2026 downgrade (A29) is on an instrument.

**Q8.** E08 only. A22 downgraded E08 to RD on 2026-07-08, and nothing follows it. Withdrawn ratings are not defaults.

**Q9.** 288. This counts entities whose latest dated action by 2026-10-01 is a long-term issuer rating that is not a withdrawal, merging duplicate-LEI records. It treats a withdrawal as covering the whole entity, and entities with a rating action dated after their withdrawal as still rated.

**Q10.** Depends. Valdoria Telecom (E05) is BB in foreign currency (A14, not investment grade) and BBB- in local currency (A13, investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and it was unchanged on 2025-06-01.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once, by A36 on 2024-09-30. A35 is a watch and A33 an affirmation.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was rated A- from A28/A26's era (2023) until A27 downgraded it to BBB+ on 2026-04-15. The LU record E17 is a research duplicate of E10.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. Orrin Bank (E06) was only placed on Rating Watch Negative on 2026-09-03 (A17); no downgrade is recorded.

**Q18.** 32 issuers; see the JSON. These are entities whose latest action by 2026-10-01 is a Rating Watch Negative, not cleared by a later action.

**Q19.** 36 issuers; see the JSON. These are entities whose latest outlook-bearing action by 2026-10-01 is Negative. Entities on watch, withdrawn, or later changed are excluded. I left out E1060/E1059, which is ambiguous.

**Q20.** No. E07 was withdrawn on 2026-05-12 (A19, "commercial reasons"), which is not a default.

**Q21.** 37 entities; see the JSON. These are entities whose last action is a withdrawal (WD). For E1106 and E1279 the withdrawal is tagged to one currency basis, but I treated it as covering the whole entity.

**Q22.** E08 only (A22, RD).

**Q23.** F2 (A04, 2026-02-10).

**Q24.** Yes. Kestrel Energy's issuer rating is BBB (A03).

**Q25.** 66. Instruments with a latest rating of BBB- or better on 2026-10-01, excluding those whose rating has expired (EX records).

**Q26.** A+ (A40, local-currency basis).

**Q27.** A- (A42, I06 subordinated).

**Q28.** BBB+ (A38, foreign-currency basis).

**Q29.** None. The Republic of Valdoria has only a country-ceiling record of BB (A12), no issuer rating.

**Q30.** E15, E1039, E1194 (Corvenia, ceiling A) and E05, E1028, E1101, E1126, E1236 (Valdoria, ceiling BB). Their foreign-currency ratings equal the sovereign's country-ceiling rating (A37 and A12).

**Q31.** No. No Corvenia or Valdoria company has a foreign-currency rating above A or BB respectively.

**Q32.** E09, Halden Group plc. E11 has parent E10, and E10 has parent E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is issued by E11 and guaranteed by E10, and E10 is BBB+ after A27.

**Q34.** No. E12 has no parent link to E09, E10 or E11.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04). E03 is a duplicate record of E02.

**Q37.** 344. That is 370 entity records minus 26 duplicate-LEI records.

**Q38.** No. E06 (DE) and E13 (US) have different LEIs and countries.

**Q39.** A (A09).

**Q40.** 74 GB-domiciled entities held an issuer rating on 2026-10-01. This is a long manual tally and may be off by a few.

**Q41.** BB+. Brindle Capital (E16) was BBB- (A43) and was downgraded to BB+ (A44) on 2026-06-01.

**Q42.** DE (E10, RATINGS system). The research duplicate E17 says LU, so the sources conflict.

**Q43.** 0. The only LU record, E17, duplicates E10, whose authoritative record says DE.

**Q44.** Yes, by inference. The I07 note is in XVD and rated BBB-, matching E05's local-currency rating (A13).

**Q45.** No. It is a local-currency note, so the foreign-currency ceiling of BB does not apply.

**Q46.** No. E11 has only a counterparty-type (CO) rating, A46, not an issuer rating.

**Q47.** None. I08's only record is EX (expiry) on 2026-09-01 (A47).

**Q48.** 106 instruments held a rating on 2026-10-01, excluding expired ones.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1093","E1213","E1228","E1229","E1243","E1263","E1285","E1294","E1299","E1300","E1307","E1290","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351","E1186"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 288},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1210","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1064","E1072","E1079","E1080","E1118","E1158","E1161","E1188","E1190","E1211","E1228","E1248","E1262","E1263","E1271","E1294","E1300","E1340","E1342","E1343","E1344","E1345","E1346","E1347","E1348","E1349","E1350","E1351"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 66},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 344},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 74},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```