**Q1.** A-. E01's rating was A- (A01, 2024-03-12) until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only 2026 action on E01 is an affirmation at BBB with a Negative outlook (A03).

**Q3.** No, BB+. The 2031 note is I02, rated BB+ since the downgrade on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its later action A09 (2025-09-15) has a Positive outlook, newer than A08 (Stable).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes E02's risk (A08/A09).

**Q6.** The data does not say why. It shows only the two ratings: FC BB (A14) and LC BBB- (A13), with a Valdoria country ceiling of BB (A12).

**Q7.** I could not retrieve the full list. The 2026 downgrades visible to me include E08, E10, E16 and many E1xxx entities (listed in the JSON). 18 result rows were cut off, so the list is incomplete.

**Q8.** E08, which went to RD on 2026-07-08 (A22). I found no other default rating.

**Q9.** 393, though this may count duplicate records of the same LEI. It is the number of distinct rated entity records whose latest long-term rating on 2026-10-01 was not a withdrawal.

**Q10.** Depends. E05 is BBB- on a local-currency basis (investment grade) but BB on a foreign-currency basis (not).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36 only.

**Q14.** None. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A-. E10's downgrade to BBB+ came only on 2026-04-15 (A26, A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; only the watch and outlook changed (A35, A33).

**Q17.** No. E06 only went on Rating Watch Negative (A17), with the rating held at A-.

**Q18.** E06 (A17). Other watches in the data were not confirmed as still active, so this list may be incomplete.

**Q19.** The ones I could confirm are in the JSON (E01, E09 and others). The result set was truncated, so the list may be incomplete.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** Entities whose last long-term rating was a withdrawal before 2026-10-01 (A19 and similar WD actions); the list is in the JSON. This is partial and may include a few duplicate records.

**Q22.** E08, the only entity with an RD rating (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** I could not determine this. My query had a bug and returned 0.

**Q26.** A+ (A40, LC basis).

**Q27.** A-, from A42 on I06.

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (BB, A12) and no issuer rating.

**Q30.** The ones I could confirm are in the JSON. They sit at the CV ceiling of A or the VD ceiling of BB, but country assignments for some entities were not checked, so the list is partial.

**Q31.** Depends. I could not verify this. Some FC ratings appear above the VD ceiling, but I did not confirm those entities' countries.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** E10 (Halden Bank AG), rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent and is not in E09's tree.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04). E03 is a duplicate record of E02 and is not linked as a child.

**Q37.** 511. There are 540 records but only 509 distinct LEIs, plus 2 records with no LEI.

**Q38.** No. They have different LEIs (E06 549300AMVE..., E13 815600O8X8...).

**Q39.** A (A08/A09, same LEI).

**Q40.** 88. This may include duplicate records of the same LEI.

**Q41.** BB+. E16 was downgraded on 2026-06-01 (A44).

**Q42.** DE. E10 is domiciled in DE; E17 "HALDEN BANK" is a LU duplicate with the same LEI.

**Q43.** 1. Only E17 is recorded as LU, and it duplicates E10, which is DE.

**Q44.** Yes. I07 is denominated in XVD, Valdoria's local currency.

**Q45.** Yes. I07 is rated BBB- (A45), above the VD ceiling of BB (A12).

**Q46.** No. E11 has only a CO-type rating (A46), not an issuer rating.

**Q47.** None. I08's only action is an EX (A47), and I treated it as the rating having expired.

**Q48.** 113.

**Q49.** E5167. The chain is E5047 → E5035 → E5023 → E5011 → E5167.

**Q50.** 4.

**Q51.** 55.

**Q52.** 20.

**Q53.** No. Belir (E5062) sits under E5060/E5059, and E5086 is not among its ancestors.

**Q54.** E5130 and E5124.

**Q55.** 23.

**Q56.** BB-. This is the lowest current FC rating among the Vesol members I could see (E5144).

**Q57.** None. E5011 reaches only E5167 above it, while E5013 reaches E5006, E5002 and E5001.

**Q58.** E5145. It guarantees I5007, which is issued by E5133 in the Vesol group.

**Q59.** 11.

**Q60.** E5145. It is not in the same group as the issuer: E5133's top is E5132, while E5145 is its own top.

**Q61.** 18.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16","E1034","E1051","E1053","E1057","E1058","E1093","E1112","E1144","E1151","E1159","E1161","E1163","E1167","E1170","E1186","E1213","E1228","E1229","E1243","E1255","E1263","E1285","E1290","E1294","E1299","E1300"]},"Q8":{"entities":["E08"]},"Q9":{"count":393},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09","E1034","E1053","E1057","E1072","E1080","E1158","E1161","E1248","E1263","E1294","E1300"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07","E1002","E1007","E1021","E1032","E1041","E1048","E1057","E1062","E1063","E1076","E1084","E1107","E1115","E1121","E1124","E1138","E1140","E1155","E1158","E1159","E1166","E1172","E1200","E1205","E1206","E1218","E1219","E1225","E1233","E1234","E1244","E1254","E1277","E1303","E1308","E1316","E1320"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":null},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E15","E1039","E05","E1028","E5012","E5047"]},"Q31":{"any":"depends"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":88},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":113},"Q49":{"parent":"E5167"},"Q50":{"count":4},"Q51":{"count":55},"Q52":{"count":20},"Q53":{"same_group":"no"},"Q54":{"entities":["E5130","E5124"]},"Q55":{"count":23},"Q56":{"rating":"BB-"},"Q57":{"entity":"none"},"Q58":{"entities":["E5145"]},"Q59":{"count":11},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":18}}
```