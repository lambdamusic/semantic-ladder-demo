**Q1.** A-. E01's LTIDR was A- (A01) from 2024-03-12 to 2025-06-20, which covers 1 Jan 2025.

**Q2.** No. In 2026 E01 only had an affirmation with the outlook moved to Negative (A03, BBB), and no downgrade.

**Q3.** No, BB+. The 2031 note is I02 (subordinated), currently rated BB+ (A07).

**Q4.** Positive. E02's current LTIDR is A with a POS outlook (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and `credit_risk_of` is E02. I03 itself is rated A (A11), and E02 is A (A09).

**Q6.** The data does not state a reason. The likely cause is the VD country ceiling of BB (ceilings.csv), which matches E05's FC rating (A14) and sits below its LC rating of BBB- (A13). That is an inference from the ceiling, not something the data states outright.

**Q7.** 31 issuers had a downgrade in 2026 (listed in the JSON). I counted any LTIDR (FC or LC) cut in 2026, judged by the rating level actually falling. Some rows are labelled inconsistently with their rating change, for example E1064 (A1141) and E1290.

**Q8.** E08 only. Its rating was RD (restricted default) on 1 Oct 2026 (A22).

**Q9.** 278. I counted distinct entities holding an open (empty valid_to), non-WD LTIDR on 1 Oct 2026. This includes E08 (RD), E1279 (LC rating only) and E1106 (FC rating only).

**Q10.** Depends. E05's LC rating is BBB- (investment grade) but its FC rating is BB (not).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36).

**Q14.** None. E12's first rating starts on 2024-02-01 (A30).

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now. Only the watch and outlook changed (A35, A33).

**Q17.** No. E06's A- rating is unchanged; it was placed on Rating Watch Negative on 2026-09-03 (A17).

**Q18.** 32 issuers were on RWN with an open record on 1 Oct 2026 (listed in the JSON).

**Q19.** 24 issuers had an open record with a NEG outlook on 1 Oct 2026 (listed in the JSON).

**Q20.** No. E07's rating was withdrawn on 2026-05-12 (A19), and nothing shows a default.

**Q21.** 35 entities had an issuer rating that was later withdrawn, with no rating still open on 1 Oct 2026 (listed in the JSON). E1106, E1279 and E1303 are excluded because they still hold or regained a rating.

**Q22.** E08 only. It is the only entity with an RD rating (A22).

**Q23.** F2. E01's STIDR is F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 66. I counted the instruments whose open rating on 1 Oct 2026 is BBB- or higher.

**Q26.** A+ (A40).

**Q27.** A- (A42). That is the rating on I06.

**Q28.** BBB+ (A38).

**Q29.** None. VD has no entry in ratings.csv.

**Q30.** E15, E1039, E1194 (all CV, FC A, ceiling A) and E05, E1028, E1101, E1126, E1236 (all VD, FC BB, ceiling BB).

**Q31.** No. No CV entity is rated above A and no VD entity above BB on a foreign-currency basis. E1101's LC rating of BB+ is local currency, so the ceiling does not bind it.

**Q32.** E09 (`ultimate_parent_id` for E11, ancestors.csv).

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10 (`credit_risk_of` E10), and I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent and appears in no ancestor chain, while E10 sits under E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is merged into E02.

**Q37.** 331. After merging duplicate records into entities, entities.csv has 331 rows (16 in the E-/CV/VD block and 315 from E1001 to E1339).

**Q38.** No. E06 (DE, LEI 549300AMVE3VRVG7HK43) and E13 (US, LEI 815600O8X8K2F154N214) have different LEIs and countries.

**Q39.** A (A09).

**Q40.** 66. I counted GB-domiciled entities with an open, non-WD LTIDR on 1 Oct 2026.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU. This is E10's country in entities.csv.

**Q43.** 1: E10 only.

**Q44.** Yes. I07 is in XVD and `local_currency` is "yes".

**Q45.** No. The VD ceiling of BB applies to foreign-currency ratings. I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 has no ratings of its own. Its note I05 is rated through the guarantor E10.

**Q47.** None. I08 has no rating row, so it is unrated. Its issuer E15 is rated A, but that is not the note's rating.

**Q48.** 106. I counted the instruments with an open rating row on 1 Oct 2026 (7 from the I01–I07 block plus 99 from I1002–I1107).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08","E10","E1034","E1051","E1053","E1057","E1058","E1064","E1080","E1093","E1112","E1144","E1151","E1159","E1160","E1163","E1167","E1169","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1298","E1300","E1307"]},
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
"Q18": {"issuers": ["E06","E1006","E1013","E1019","E1037","E1039","E1059","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194","E1203","E1209","E1238","E1242","E1260","E1264","E1266","E1267","E1297","E1314","E1317","E1323"]},
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1059","E1064","E1072","E1079","E1080","E1118","E1158","E1160","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
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
"Q30": {"entities": ["E15","E1039","E1194","E05","E1028","E1101","E1126","E1236"]},
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