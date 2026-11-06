**Q1.** A-. E01's last rating before 1 Jan 2025 was A- (A01, 2024-03-12). The downgrade to BBB came later, on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), and the outlook went to Negative.

**Q3.** No, BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest action is A09 (2025-09-15), with a Positive outlook.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 but guaranteed by E02, and I03 itself is rated A (A10, A11).

**Q6.** Not answered. The data does not state a reason, only the ratings.

**Q7.** Incomplete. The 2026 downgrades I could see are E08, E10, E16, E1034, E1080 and E1161. My count query returned 0, so I could not confirm the full list.

**Q8.** E08. Its latest rating is RD (A22, 2026-07-08).

**Q9.** 291. These are distinct issuers, with duplicate records merged by LEI, whose latest long-term issuer rating on 1 Oct 2026 was not WD.

**Q10.** Depends. E05 is BBB- on a local-currency basis (A13) but BB on a foreign-currency basis (A14).

**Q11.** BBB+ (A36, 2024-09-30).

**Q12.** A- (A34).

**Q13.** 1. Only A36 is a downgrade. The rating watch (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A- (A26). E10 was downgraded only on 2026-04-15.

**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is still BBB+ (A33).

**Q17.** No. E06 was only placed on Rating Watch Negative (A17), and its rating stayed A-.

**Q18.** Incomplete. Visible issuers with a latest foreign-currency action of Rating Watch Negative are listed in the JSON. About 47 further rows were truncated.

**Q19.** Incomplete. The visible issuers whose latest foreign-currency outlook was Negative are listed in the JSON. Truncated rows may hold more.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), not because of a default.

**Q21.** E07 and the 36 other issuers whose latest long-term action is a withdrawal (WD). Duplicate-LEI records were not reconciled.

**Q22.** E08, the only entity with an RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01 is BBB (A03).

**Q25.** 66. This counts instruments whose latest rating on 1 Oct 2026 was BBB- or better, excluding expired or withdrawn ratings.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05 is BB against a ceiling of BB (A12, A14), and E15 is A against a ceiling of A for CV (A37, A41). Other entities with hidden records are not checked.

**Q31.** No, based on the visible records. Both E05 and E15 sit exactly at their ceilings.

**Q32.** E09 (E11's parent is E10, whose parent is E09).

**Q33.** The guarantor, E10, rated BBB+ (A27). I05 is issued by E11 and guaranteed by E10.

**Q34.** No. E12 has no parent link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10, so it is a duplicate record.

**Q36.** 2: E02 and E04. E03 has the same LEI as E02, so it is a duplicate.

**Q37.** 344. There are 370 entity records, with 342 distinct LEIs plus 2 records without an LEI.

**Q38.** No. E06 and E13 have different LEIs and countries (DE and US).

**Q39.** A (A09).

**Q40.** 74. This counts distinct GB issuers, merged by LEI, with a latest long-term rating on 1 Oct 2026 that was not WD.

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE. E10 is DE, though its duplicate record E17 says LU.

**Q43.** 1. Only E17 is in LU, and it is a duplicate of E10.

**Q44.** Yes. I07 is denominated in XVD, Valdoria's own currency.

**Q45.** Yes. I07 is rated BBB- (A45), above VD's BB ceiling (A12).

**Q46.** No. E11 has only a Credit Opinion (A46, BBB), not an issuer rating.

**Q47.** None. I08's only action is an EX at A on 2026-09-01, which I took to mean the rating ended; the data does not define EX.

**Q48.** 106. This is 66 investment-grade instruments plus 40 rated BB+ or lower, excluding EX and WD.

```json
{
"Q1":{"rating":"A-"},
"Q2":{"downgraded":"no"},
"Q3":{"investment_grade":"no","rating":"BB+"},
"Q4":{"outlook":"Positive"},
"Q5":{"risk_of":"E02","rating":"A"},
"Q7":{"issuers":["E08","E10","E16","E1034","E1080","E1161"]},
"Q8":{"entities":["E08"]},
"Q9":{"count":291},
"Q10":{"investment_grade":"depends"},
"Q11":{"rating":"BBB+"},
"Q12":{"rating":"A-"},
"Q13":{"count":1},
"Q14":{"rating":"none"},
"Q15":{"rating":"A-"},
"Q16":{"changed":"no"},
"Q17":{"downgraded":"no"},
"Q18":{"issuers":["E06","E1006","E1013","E1037","E1039","E1061","E1066","E1088","E1098","E1099","E1109","E1126","E1132","E1133","E1146","E1168","E1181","E1194"]},
"Q19":{"issuers":["E01","E09","E1005","E1029","E1034","E1046","E1055","E1056","E1060","E1064","E1072","E1079","E1080","E1105","E1118","E1158","E1161","E1188","E1190"]},
"Q20":{"in_default":"no"},
"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1106","E1107","E1121","E1124","E1138","E1140","E1155","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1279","E1308","E1316","E1320"]},
"Q22":{"entities":["E08"]},
"Q23":{"rating":"F2"},
"Q24":{"investment_grade":"yes"},
"Q25":{"count":66},
"Q26":{"rating":"A+"},
"Q27":{"rating":"A-"},
"Q28":{"rating":"BBB+"},
"Q29":{"rating":"none"},
"Q30":{"entities":["E05","E15"]},
"Q31":{"any":"no"},
"Q32":{"parent":"E09"},
"Q33":{"risk_of":"E10","rating":"BBB+"},
"Q34":{"same_group":"no"},
"Q35":{"count":3},
"Q36":{"count":2},
"Q37":{"count":344},
"Q38":{"same":"no"},
"Q39":{"rating":"A"},
"Q40":{"count":74},
"Q41":{"rating":"BB+"},
"Q42":{"country":"DE"},
"Q43":{"count":1},
"Q44":{"local_currency":"yes"},
"Q45":{"above_ceiling":"yes"},
"Q46":{"issuer_rating":"no"},
"Q47":{"rating":"none"},
"Q48":{"count":106}
}
```