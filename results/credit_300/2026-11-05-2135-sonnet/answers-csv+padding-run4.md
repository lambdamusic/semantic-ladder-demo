**Q1.** A-. A01 assigned A- to E01 on 2024-03-12, and the next action (A02) came on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03 (affirmed BBB, Outlook Negative), and the downgrade A02 was in 2025.

**Q3.** No, BB+. The 2031 note is I02 (subordinated); A07 cut it from BBB (A23) to BB+.

**Q4.** Positive. A09 affirmed A/POS on E03, which shares E02's LEI and is a duplicate (source RESEARCH) of E02. It is the latest action, after A08's STA.

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and E02's latest rating is A (A09).

**Q6.** Not stated in the data directly. The most consistent reading is that VD's Country Ceiling is BB (A12) and caps E05's foreign-currency rating (A14, BB), while the local-currency rating (A13, BBB-) is not capped.

**Q7.** 31 issuers had a downgrade (DG) on a long-term issuer rating in 2026; they are listed in the JSON block. I mapped RESEARCH duplicates to their RATINGS record and excluded QA-source records.

**Q8.** E08. A22 moved it to RD on 2026-07-08 (distressed debt exchange), with no later action.

**Q9.** 277. This counts canonical entities whose latest long-term issuer rating action on or before 2026-10-01 is not a withdrawal (WD), with duplicates merged and QA records excluded. It is a hand count, so treat it as approximate.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was cut from A- to BBB+ by A36 on 2024-09-30.

**Q12.** A-. A34 assigned it on 2023-01-15, before the A36 downgrade.

**Q13.** 1. A36 is the only DG on E14; A35 (RW) and A33 (AF) did not lower the rating.

**Q14.** None. E12's first rating is A30, dated 2024-02-01, after the question date.

**Q15.** A-. E10 was rated A- by A26 in 2023, and the downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A35 put it on watch and A33 affirmed it).

**Q17.** No. E06's only 2026 action is A17, Rating Watch Negative at A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** 32 issuers; they are in the JSON block. These are entities whose latest rating action was an RW with RWN, not later cleared.

**Q19.** 26 issuers; they are in the JSON block. These are entities whose latest foreign-currency long-term action carries a Negative outlook. I excluded those on RWN, which have no outlook.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, which is not a default.

**Q21.** 36 entities, listed in the JSON block. E07 plus 35 others have a WD as their latest action before 2026-10-01.

**Q22.** E08 only. A22 is the only RD or default-category rating in the data.

**Q23.** F2. A04 affirmed E01's short-term issuer rating on 2026-02-10.

**Q24.** Yes. E01's long-term rating is BBB (A03), which is investment grade.

**Q25.** 66. The latest instrument rating is BBB- or better for 5 of I01–I07 and 61 of the I10xx instruments. I treated EX (expired) as ending the rating.

**Q26.** A+. A40 gave E15 a local-currency rating of A+.

**Q27.** A-. A42 rated I06.

**Q28.** BBB+. A38 is CV's foreign-currency long-term rating; the A in A37 is the Country Ceiling.

**Q29.** None. VD has only a Country Ceiling record (A12, BB) and no long-term issuer rating.

**Q30.** Eight entities: E05, E1028, E1101, E1126 and E1236 at VD's BB ceiling, and E15, E1039 and E1194 at CV's A ceiling.

**Q31.** No. No VD entity's foreign-currency rating is above BB and no CV entity's is above A.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is issued by E11 but guaranteed by E10 (A29, BBB+).

**Q34.** No. E12 has no parent, while E10 sits under E09. The shared "Halden" name does not link them.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10, and E12 is not in the group.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 331. There are 370 rows, of which 26 are same-LEI RESEARCH duplicates and 13 are QA-source test records; counting the QA records would give 344.

**Q38.** No. E06 (DE, LEI 549300AMVE3VRVG7HK43) and E13 (US, LEI 815600O8X8K2F154N214) have different LEIs.

**Q39.** A (A09, via E03, which duplicates E02).

**Q40.** 66 GB-domiciled issuers hold an issuer rating, by the same method as Q9.

**Q41.** None. E16 is a QA-source record, which I treat as test data; its record shows BB+ (A44).

**Q42.** DE. E10 is DE; E17 is a RESEARCH duplicate with the same LEI that lists LU.

**Q43.** 0. The only LU record, E17, is a duplicate of the DE entity E10.

**Q44.** Yes, inferred. I07 is in XVD, which looks like Valdoria's currency, but the data does not define it. Its rating of BBB- (A45) matches E05's local-currency rating.

**Q45.** No. The Country Ceiling (A12, BB) limits foreign-currency ratings, and I07 is a local-currency note rated BBB-.

**Q46.** No. E11 has only a CO-type rating (A46, BBB), not a long-term issuer rating.

**Q47.** None. A47 shows EX (expired) on I08 on 2026-09-01; it was last rated A.

**Q48.** 106: 7 of I01–I07 plus 99 of the I10xx instruments. I08 and the I10xx instruments whose only action is EX are excluded.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 277},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06","E1267","E1242","E1039","E1088","E1194","E1133","E1203","E1006","E1066","E1109","E1264","E1099","E1168","E1209","E1260","E1037","E1013","E1019","E1059","E1098","E1132","E1126","E1146","E1181","E1297","E1266","E1314","E1317","E1323","E1061","E1238"]},
"Q19": {"issuers": ["E01","E09","E1158","E1118","E1079","E1056","E1190","E1046","E1055","E1034","E1064","E1263","E1080","E1029","E1160","E1228","E1105","E1211","E1248","E1261","E1271","E1282","E1072","E1300","E1294","E1059"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1253","E1277","E1279","E1308","E1316","E1320"]},
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
"Q40": {"count": 66},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 106}
}
```