**Q1.** A-. The latest action on or before 2025-01-01 is A01 (assigned A-, 2024-03-12); the downgrade to BBB (A02) came on 2025-06-20.

**Q2.** No. E01's 2026 actions (A03, A04) are affirmations (AF); its only downgrade is A02 in 2025.

**Q3.** No, BB+. I02 was BBB in 2024 (A23) but was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E02 and E03 share an LEI, so the latest action is A09 (AF, A, POS, 2025-09-15).

**Q5.** Northwind Holdings (E02), at A. I03 is guaranteed by E02, so it is rated on E02's issuer rating (A10, A11), not on E04's.

**Q6.** Valdoria's foreign-currency ceiling is BB (A12), and E05's FC rating of BB (A14) sits at that cap. Its LC rating of BBB- (A13) is not capped, because the ceiling covers transfer and convertibility risk on FC debt only.

**Q7.** 31 issuers, all with a 2026 DG action on a non-QA issuer record (listed in JSON). I excluded the instrument downgrade A29 and the QA records.

**Q8.** E08. Its RD rating (A22, 2026-07-08) is still the latest action, and no other issuer has RD or D.

**Q9.** 278. Counted once per entity, with a non-withdrawn FC LTIDR in effect on 1 Oct. VD is excluded because its only record is a Country Ceiling (A12). This is a hand tally, so treat it as approximate.

**Q10.** No. The headline FC rating is BB (A14). The LC rating of BBB- (A13) is investment grade, but it is not the headline.

**Q11.** BBB+. The 2024-09-30 downgrade to BBB+ (A36) was still in effect on 2025-06-01.

**Q12.** A-. A34 (assigned 2023-01-15) was the rating on 2024-01-01.

**Q13.** Once. The only downgrade is A36 (A- to BBB+, 2024-09-30).

**Q14.** None. Halden Foods' first rating is A30 (BB-, 2024-02-01), which is after 2024-01-01.

**Q15.** A-. A26 (2023-05-01) was in effect; the downgrade to BBB+ (A27) came on 2026-04-15.

**Q16.** No. The rating has been BBB+ since A36; the later RW (A35) and AF (A33) left it unchanged.

**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative, which is not a downgrade.

**Q18.** 29 issuers, each with a latest action that is RW with RWN as of 1 Oct (listed in JSON). This is a hand tally.

**Q19.** 28 issuers whose most recent stated outlook is NEG (listed in JSON). RW rows carry no outlook, so I carried forward the last stated outlook. This is a judgement call.

**Q20.** No. Pellam's latest action (A19, 2026-05-12) is a withdrawal, not a default.

**Q21.** 35 entities, whose latest issuer-rating action is a withdrawal (WD) with no later rating action (listed in JSON). This is a hand tally.

**Q22.** E08 is the only entity that has ever been in default (RD in A22).

**Q23.** F2. This is the short-term rating from A04 (STIDR, 2026-02-10).

**Q24.** Yes. E01's long-term rating is BBB (A03), which is investment grade.

**Q25.** 66 instruments rated BBB- or higher on 1 Oct (hand tally).

**Q26.** A+. This is the LC rating from A40 (2024-03-01).

**Q27.** A-. I06 (subordinated) was assigned A- in A42.

**Q28.** BBB+. This is the FC issuer rating from A38. The CC of A (A37) is a ceiling, not the issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** Eight entities. Five are at the VD ceiling of BB: E05, E1028, E1101, E1126, E1236. Three are at the CV ceiling of A: E15, E1039, E1194.

**Q31.** No. No VD-domiciled FC rating is above BB, and no CV-domiciled FC rating is above A.

**Q32.** E09. The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** E10, at BBB+. I05 is guaranteed by E10, so it is rated on E10's issuer rating (A29 gives BBB+).

**Q34.** No. E12 has no parent link, and E10 belongs to the group headed by E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 distinct entities. This is the 324 IDs from E1001 to E1324, less 24 RESEARCH duplicates, plus 16 entities from E01 to E15 and 15 finance subsidiaries. It excludes QA records and includes the two sovereigns.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214).

**Q39.** A, from A09 (E03 is E02, AF, POS).

**Q40.** 66 issuers domiciled in GB with a rating in effect on 1 Oct (hand tally). Domicile uses the RESEARCH record where it differs from RATINGS.

**Q41.** None. Brindle Capital (E16) is a QA record, so its actions must be ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile over the RATINGS record's DE.

**Q43.** 1: Halden Bank (E10, same entity as E17).

**Q44.** Yes. I07 is denominated in XVD, Valdoria's domestic currency, and E05 is domiciled in VD.

**Q45.** No. I07 is rated BBB-, which is numerically above the BB ceiling. The ceiling only caps FC ratings, so local-currency debt is not held to it. This answer depends on reading "above what the ceiling allows" as "subject to the cap".

**Q46.** No. E11's only record is a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), which is not a rating until an AS action confirms it.

**Q48.** 106. Of the 115 instruments, nine have only EX actions or none (I08, I1001, I1007, I1008, I1012, I1015, I1021, I1046, I1049).

**Data notes:**
- E1115, E1158 and E1303 have rating actions dated after a withdrawal. I followed the latest-action rule, which gives them a rating, but this conflicts with the ontology's "no rating after withdrawal".
- E1229's A1481 (2026-06-02) is labelled DG but raises the rating from BB to BB+. It still qualifies for Q7 through A1482.
- Actions A1011, A1029, A1078 and A1713 are dated after today (2026-11-05). None changes an answer for 1 October.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300","E1307"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 278},
  "Q10": {"investment_grade": "no"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": ["E06","E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
  "Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1064","E1072","E1079","E1080","E1105","E1118","E1132","E1146","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1263","E1271","E1282","E1294","E1300"]},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": ["E07","E1001","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1277","E1279","E1308","E1316","E1320"]},
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
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 106}
}
```