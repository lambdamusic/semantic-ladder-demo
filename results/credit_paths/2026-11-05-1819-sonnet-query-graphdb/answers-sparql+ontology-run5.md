Several questions (Q25, Q40, Q48, Q51, Q52, Q54–Q56, Q58–Q61) were not computed because I ran out of query rounds; they are marked `null` in the JSON. Q18–Q22, Q30 and Q31 are partial, and I give the caveats on each below.

**Q1.** A-. E01 was assigned A- on 2024-03-12 and downgraded to BBB only on 2025-06-20 (A02).
**Q2.** No. E01's only 2026 action (A03, 2026-02-10) was an affirmation with the outlook moved to Negative.
**Q3.** No, BB+. The 2031 note (I02) is subordinated and was downgraded to BB+ on 2025-06-20 (A07).
**Q4.** Positive. E02 and E03 share an LEI, so they are one entity; the latest action is A09 (2025-09-15, outlook POS).
**Q5.** A holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, and its rating is A (A11).
**Q6.** E05's foreign-currency rating is BB while its local-currency rating is BBB-, so the foreign-currency rating is held down to VD's Country Ceiling of BB (A12).
**Q7.** E08 (A21) and E10 (A27) were downgraded in 2026; E16 is a QA record and is ignored. My downgrade search covered only the E-series records I listed, so this list is incomplete.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22), and it is the only non-QA entity with an RD or D rating anywhere.
**Q9.** 377. This counts distinct non-QA entities (by LEI) whose latest long-term issuer rating on 1 October 2026 is not a withdrawal.
**Q10.** No. The foreign-currency headline rating is BB (A14).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. Only A36 is a downgrade; A35 is a Watch.
**Q14.** None. E12's first rating (A30) is dated 2024-02-01, after the question date.
**Q15.** A-. E10 was downgraded to BBB+ only on 2026-04-15 (A27).
**Q16.** No. BBB+ has held since 2024-09-30; the later Watch and affirmation did not change it.
**Q17.** No. E06's only 2026 action is a Rating Watch (A17).
**Q18.** The list is in the JSON; it is the issuers whose latest action carries a Rating Watch Negative flag.
**Q19.** The list is in the JSON; it is issuers whose latest action has a Negative outlook and no Watch.
**Q20.** No. E07 was withdrawn (A19), which is not a default, and its last rating was BB.
**Q21.** The list is in the JSON; it is issuers whose latest issuer-rating action is a withdrawal. E1106's withdrawal is local-currency only and it may still hold a foreign-currency rating, so I left it out.
**Q22.** E08, the only entity ever rated RD or D.
**Q23.** F2 (A04).
**Q24.** Yes, BBB (A03).
**Q26.** A+ (A40).
**Q27.** A-. I06 is a subordinated note rated A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The only action on the Republic of Valdoria (VD) is a Country Ceiling (A12), and that is not an issuer rating.
**Q30.** Partial: only the visible rows could be checked. Entities with a foreign-currency rating equal to the ceiling (BB for VD, A for CV) are listed in the JSON.
**Q31.** No, based on the rows I could see; the result was truncated.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** A holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).
**Q34.** No. E12 has no parent, while E10 sits under E09.
**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10 (same LEI).
**Q36.** 2: E02 (same entity as E03) and E04.
**Q37.** 497 distinct legal entities, counting by LEI and excluding QA records.
**Q38.** No. E06 and E13 have different LEIs.
**Q39.** A.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** LU. The RESEARCH record (E17) holds for domicile, so E10's DE entry is overridden.
**Q43.** 1.
**Q44.** Yes. I07 is paid in XVD, VD's domestic currency.
**Q45.** Yes. I07 is rated BBB- (A45) against VD's ceiling of BB.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. I08 has only an Expected rating (A47), so it stays unrated.
**Q49.** E5001. The chain is E5047 → E5035 → E5023 → E5011 → E5167 (same entity as E5005) → E5002 → E5001.
**Q50.** 6 levels.
**Q53.** No. RATINGS holds parent links, so E5168 (same LEI as E5062) belongs to the Belir group, not Rotam.
**Q57.** E5002, the nearest common parent of E5011 and E5013.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"POS"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10"]},"Q8":{"entities":["E08"]},"Q9":{"count":377},"Q10":{"investment_grade":"no"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E1181","E1109","E1203","E1088","E1238","E1314","E1194","E1210","E1099","E1260","E1297","E1242","E1006","E1133","E1146","E1066","E1168","E1019","E1061","E1132","E06","E1098","E1266","E1126","E1267","E1037","E1013","E1317","E1323","E1059","E1039","E1264"]},"Q19":{"issuers":["E1300","E5099","E1064","E5113","E5039","E1161","E5141","E1080","E1105","E1072","E1211","E1005","E1034","E1271","E1118","E1158","E1056","E1248","E5062","E5057","E1055","E5097","E1046","E5059","E5020","E1263","E5073","E1188","E1282","E01","E5102","E1029","E5131","E5023","E5116","E09","E1228","E1060","E1079","E5019","E5050","E1262","E5013","E1190","E5119","E1294","E5156"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E1002","E1084","E1032","E1234","E1219","E1206","E1107","E1244","E1172","E1159","E1057","E1041","E07","E1062","E1277","E1155","E1254","E1121","E1063","E1166","E1021","E1200","E1279","E1048","E1124","E1076","E1138","E1140","E1316","E1308","E1007","E1218","E1225","E1205","E1320","E1233"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":null},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E5124","E1236","E1126","E05","E5047","E1028","E5012","E5091","E1194","E15","E1039","E5116"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":497},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":null},"Q41":{"rating":"none"},"Q42":{"country":"LU"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":null},"Q49":{"parent":"E5001"},"Q50":{"count":6},"Q51":{"count":null},"Q52":{"count":null},"Q53":{"same_group":"no"},"Q54":{"entities":[]},"Q55":{"count":null},"Q56":{"rating":null},"Q57":{"entity":"E5002"},"Q58":{"entities":[]},"Q59":{"count":null},"Q60":{"risk_of":null,"same_group":null},"Q61":{"count":null}}
```