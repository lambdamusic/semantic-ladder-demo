**Q1.** A-. Kestrel Energy (E01) held an A- long-term foreign-currency rating from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only 2026 action was an affirmation at BBB with the outlook moved to Negative (A03); the downgrade to BBB was in June 2025 (A02).

**Q3.** No, it is BB+. The 2031 note (I02) was cut to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 (which merges E03) has had an A rating with a Positive outlook since 2025-09-15 (A09).

**Q5.** A holder takes E02's credit risk, rated A. I03 is issued by E04 and guaranteed by E02, and its credit_risk_of is E02; E02 is rated A (A09) and I03 is also A (A11).

**Q6.** Not in the structured answer. The data does not state a reason for the gap. It only shows E05's foreign-currency BB (A14) against its local-currency BBB- (A13), and the Valdoria ceiling of BB.

**Q7.** 31 issuers had a downgrade action in 2026; the IDs are in the JSON. I relied on the action flag "DG" for 2026 long-term rating records.

**Q8.** E08. Its rating has been RD (restricted default) since 2026-07-08 (A22).

**Q9.** 278. This is the count of distinct entities with a current long-term or short-term issuer rating on 1 October 2026, excluding withdrawn (WD) ratings.

**Q10.** Depends. E05 is BB in foreign currency (A14, not investment grade) but BBB- in local currency (A13, investment grade).

**Q11.** BBB+. E14 held BBB+ from 2024-09-30 to 2025-11-20 (A36), a period that includes 2025-06-01.

**Q12.** A-. E14 held A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36); the later watch and affirmation did not change the rating.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30), so it had no rating on 2024-01-01.

**Q15.** A-. E10 held A- until 2026-04-15 (A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A36, A33); only the watch status and outlook changed.

**Q17.** No. E06 stayed at A- and was only placed on Rating Watch Negative on 2026-09-03 (A17).

**Q18.** 32 issuers were on Rating Watch Negative on 1 October 2026; the IDs are in the JSON.

**Q19.** 28 issuers had a Negative outlook on 1 October 2026; the IDs are in the JSON.

**Q20.** No. E07's rating was withdrawn (WD) on 2026-05-12 (A19). That is not a default.

**Q21.** 35 entities. Each had an issuer rating at some point and only withdrawn (WD) ratings as the current one on 1 October 2026; E07 is one example.

**Q22.** Only E08. It is the only entity with a default-grade rating, RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is rated BBB (A03).

**Q25.** 66 instruments held a current rating of BBB- or better on 1 October 2026.

**Q26.** A+. E15's local-currency rating (A40).

**Q27.** A-. I06 (A42).

**Q28.** BBB+. CV's foreign-currency rating (A38).

**Q29.** None. VD has no rating records.

**Q30.** 8 entities. Corvenia's ceiling is A and E15, E1039 and E1194 are rated A. Valdoria's ceiling is BB and E05, E1028, E1101, E1126 and E1236 are rated BB.

**Q31.** No. Every current foreign-currency rating for CV and VD entities is at or below its ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The risk is E10's, rated BBB+. I05 is guaranteed by E10 (A29, BBB+ on both the note and E10's issuer rating, A27).

**Q34.** No. E12 has no parent and is not linked to E09 or E10.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 331 rows in entities, which is already after duplicate records were merged.

**Q38.** No. Orrin Bank AG (E06, DE) and Orrin Bancorp Inc (E13, US) are separate entities with different LEIs.

**Q39.** A (A09).

**Q40.** 66 GB issuers held a current issuer rating on 1 October 2026, excluding withdrawn ratings.

**Q41.** None. No entity named Brindle Capital appears in the data.

**Q42.** LU.

**Q43.** 1 entity is domiciled in LU.

**Q44.** Yes. I07 is denominated in XVD and flagged local_currency = yes.

**Q45.** No. I07 is rated BBB- (A45), above Valdoria's BB ceiling, but the ceiling caps foreign-currency ratings and I07 is a local-currency note.

**Q46.** No. E11 has no issuer rating records; only its note I05 is rated.

**Q47.** None. I08 has no rating records.

**Q48.** 106 instruments held a current, non-withdrawn rating on 1 October 2026.

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
"Q19": {"issuers": ["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1059","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1160","E1188","E1190","E1211","E1228","E1248","E1261","E1263","E1271","E1282","E1294","E1300"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E1076","E1205","E1218","E1159","E1200","E1206","E1234","E1041","E1048","E1107","E1320","E1063","E1140","E1277","E1001","E1244","E1316","E1084","E1032","E1225","E1233","E07","E1124","E1219","E1253","E1308","E1057","E1172","E1007","E1121","E1166","E1155","E1021","E1062","E1138"]},
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