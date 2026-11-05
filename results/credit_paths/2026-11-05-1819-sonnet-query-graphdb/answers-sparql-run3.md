Several answers below are only partly supported. My last round of queries partly failed, so some totals rest on partial results and a few fields are null.

**Q1.** A-. Kestrel Energy (E01) was assigned A- on 2024-03-12 (A01) and was not downgraded until 2025-06-20 (A02).
**Q2.** No. The 2026-02-10 action (A03) is an affirmation at BBB with a Negative outlook, not a downgrade.
**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is below investment grade.
**Q4.** Positive. E03 carries the same LEI as Northwind Holdings (E02) and is the latest record, with Positive on 2025-09-15 (A09). E02's own record still shows Stable from 2023 (A08).
**Q5.** E02, rated A. The Northwind Finance 2030 notes (I03) are issued by E04 but guaranteed by E02, so the holder takes E02's risk.
**Q6.** The Valdoria Country Ceiling is BB (A12), which caps the foreign-currency rating, while the local-currency rating is BBB- (A13).
**Q7.** Incomplete. The downgrades I could confirm are E08 (A21, A22), E10 (A27), E16 (A44) and E5019 (A5012). I did not get a complete list for the large block of E1xxx and E5xxx entities.
**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22).
**Q9.** 190, counting distinct issuers by LEI. This is the latest long-term rating per entity as of 2026-10-01, excluding withdrawn ratings.
**Q10.** Depends. The local-currency rating is BBB- (investment grade) and the foreign-currency rating is BB (not).
**Q11.** BBB+. Marlow Utilities (E14) was downgraded to BBB+ on 2024-09-30 (A36).
**Q12.** A-, from A34 (2023-01-15).
**Q13.** 1, from A36. A35 is a watch action and A33 is an affirmation.
**Q14.** None. Halden Foods' first rating is dated 2024-02-01 (A30).
**Q15.** A-. The downgrade to BBB+ for Halden Bank (E10) only came on 2026-04-15 (A27).
**Q16.** No. It was BBB+ throughout, and the Rating Watch is not a rating change.
**Q17.** No. Orrin Bank (E06) only has a Rating Watch Negative on 2026-09-03 (A17), with the rating held at A-.
**Q18.** E06 (A17).
**Q19.** Incomplete. The ones I could see with a latest Negative outlook are E01, E09, E5013, E5019, E5020, E5039, E5050 and E5057. The one query meant to list them returned an implausible result (E08, which has no outlook), so I discarded it.
**Q20.** No. Pellam Retail (E07) had its rating withdrawn (A19, WD), which is not a default.
**Q21.** E07 is the one I confirmed (withdrawn by A19, 2026-05-12). The check across the other entities did not run.
**Q22.** E08 is the only one I could confirm (RD, A22). The check across all other entities did not run.
**Q23.** F2 (A04).
**Q24.** Yes. The issuer rating is BBB (A03).
**Q25.** Could not be determined; that query did not run.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. The Republic of Valdoria (VD) has only a Country Ceiling of BB (A12), not an issuer rating.
**Q30.** Partial: E15 (A foreign-currency rating at the A ceiling for CV), E05 (BB at the BB ceiling for VD) and E5012 (BB, VD). The full check did not run, so there may be others.
**Q31.** No among the entities I could see. E15 and E05 sit exactly at their ceilings, but the full check did not run.
**Q32.** E09. Halden Leasing (E11) has parent E10, whose parent is E09.
**Q33.** E10, rated BBB+. The Halden Leasing 2028 notes (I05) are guaranteed by E10, and I05 is also rated BBB+ (A29).
**Q34.** No. Halden Foods (E12) has no parent link to E09, so it is not in the Halden group.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 and E04.
**Q37.** 511, by inference. There are 509 distinct LEIs across 540 entity records, plus the two sovereigns (CV, VD), which have no LEI. I did not confirm that those are the only entities without one.
**Q38.** No. They have different LEIs (E06 and E13).
**Q39.** A (A08 for E02, A09 for E03).
**Q40.** 51, counting distinct GB-domiciled issuers by LEI.
**Q41.** BB+ (A44).
**Q42.** DE. Halden Bank AG (E10) is DE. E17 is a LU-domiciled research-source duplicate with the same LEI.
**Q43.** 1: E17, which is itself a duplicate record of E10.
**Q44.** Yes. The 2027 note (I07) is denominated in XVD, the Valdoria currency.
**Q45.** Yes. It is rated BBB- (A45) against a ceiling of BB.
**Q46.** No. Halden Leasing (E11) only has a BBB counterparty-obligation rating (A46), not an issuer rating.
**Q47.** None. The 2034 note (I08) had its rating expired (action EX) on 2026-09-01 (A47).
**Q48.** Could not be determined; that query did not run.
**Q49.** E5001. Cerid Rosor Holdings (E5084) goes up through E5083, E5082 and E5081 to E5001.
**Q50.** 4 levels.
**Q51.** 170, including the parent.
**Q52.** 18, including the parent.
**Q53.** No. Belir Mining (E5060) sits under E5059, which sits under E5105 (Wonod Group), not Rotam Group (E5086). The chain result for Belir Mining looked odd, though, with E5105 repeated.
**Q54.** Could not be determined; the query returned nothing usable.
**Q55.** Could not be determined; that query did not run.
**Q56.** Could not be determined; that query did not run.
**Q57.** E5002. Cerid Telecom (E5013) has parent E5002, and Cerid Guven Energy (E5121) goes through E5011 to E5002.
**Q58.** E5145, from what I could see. It guarantees the Cross-group 2031 note (I5007) issued by E5133, which is in the Vesol group. The full check did not run, so there may be others.
**Q59.** Could not be determined. The one result (170) equals the whole group size, so I discarded it.
**Q60.** E5145. The Cross-group note (I5007) is issued by E5133 but guaranteed by E5145, and I judge them to be in different groups (E5133 near Vesol's E5132, E5145 tied to Geren's I5006), so not the same group. I did not confirm this with a chain query.
**Q61.** Could not be determined; that query did not run.

```json
{"Q1":{"rating":"A-"},"Q2":{"downgraded":"no"},"Q3":{"investment_grade":"no","rating":"BB+"},"Q4":{"outlook":"Positive"},"Q5":{"risk_of":"E02","rating":"A"},"Q7":{"issuers":["E08","E10","E16","E5019"]},"Q8":{"entities":["E08"]},"Q9":{"count":190},"Q10":{"investment_grade":"depends"},"Q11":{"rating":"BBB+"},"Q12":{"rating":"A-"},"Q13":{"count":1},"Q14":{"rating":"none"},"Q15":{"rating":"A-"},"Q16":{"changed":"no"},"Q17":{"downgraded":"no"},"Q18":{"issuers":["E06"]},"Q19":{"issuers":["E01","E09","E5013","E5019","E5020","E5039","E5050","E5057"]},"Q20":{"in_default":"no"},"Q21":{"entities":["E07"]},"Q22":{"entities":["E08"]},"Q23":{"rating":"F2"},"Q24":{"investment_grade":"yes"},"Q25":{"count":null},"Q26":{"rating":"A+"},"Q27":{"rating":"A-"},"Q28":{"rating":"BBB+"},"Q29":{"rating":"none"},"Q30":{"entities":["E15","E05","E5012"]},"Q31":{"any":"no"},"Q32":{"parent":"E09"},"Q33":{"risk_of":"E10","rating":"BBB+"},"Q34":{"same_group":"no"},"Q35":{"count":3},"Q36":{"count":2},"Q37":{"count":511},"Q38":{"same":"no"},"Q39":{"rating":"A"},"Q40":{"count":51},"Q41":{"rating":"BB+"},"Q42":{"country":"DE"},"Q43":{"count":1},"Q44":{"local_currency":"yes"},"Q45":{"above_ceiling":"yes"},"Q46":{"issuer_rating":"no"},"Q47":{"rating":"none"},"Q48":{"count":null},"Q49":{"parent":"E5001"},"Q50":{"count":4},"Q51":{"count":170},"Q52":{"count":18},"Q53":{"same_group":"no"},"Q54":{"entities":[]},"Q55":{"count":null},"Q56":{"rating":null},"Q57":{"entity":"E5002"},"Q58":{"entities":["E5145"]},"Q59":{"count":null},"Q60":{"risk_of":"E5145","same_group":"no"},"Q61":{"count":null}}
```