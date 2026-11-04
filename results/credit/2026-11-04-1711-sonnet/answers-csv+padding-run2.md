**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action on E01 (A02) came in June 2025.

**Q2.** No. A03 on E01 (2026-02-10) affirmed BBB with a Negative outlook, so it was not a downgrade.

**Q3.** No, it is rated BB+. I02 was assigned BBB (A23) and cut to BB+ by A07.

**Q4.** Positive. E03 is a RESEARCH duplicate of E02 (same LEI), and its latest action A09 (2025-09-15) gives a POS outlook.

**Q5.** The holder takes the risk of the guarantor, E02 (Northwind Holdings), which is rated A. I03 is issued by E04 and guaranteed by E02 (A08, affirmed by A09 on the duplicate record).

**Q6.** The data does not state a reason. It does show that the Valdoria Country Ceiling is BB (A12) and E05's foreign-currency rating is BB, against BBB- in local currency (A13, A14). That is consistent with the foreign-currency rating being capped at the ceiling.

**Q7.** E08, E10 and E16. A21/A22 downgraded E08, A27 downgraded E10 and A44 downgraded E16. I counted issuer ratings only, so the 2026 downgrade of the instrument I05 does not add E11.

**Q8.** E08. Its latest action, A22 (2026-07-08), is a downgrade to RD, and nothing follows it.

**Q9.** 13. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), and VD has only a country ceiling, which is not an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30.

**Q12.** A-. This is A34, assigned 2023-01-15.

**Q13.** 1. Only A36 is a downgrade of E14.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- (A26) and not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+. A35 only placed it on watch, and A33 affirmed the rating in 2026.

**Q17.** No. A17 on E06 is a Rating Watch Negative action that keeps the A- rating.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's earlier watch (A35) was superseded by the A33 affirmation with no watch.

**Q19.** E01 and E09, from A03 and A25. E06's outlook is blank on A17 because it is on watch.

**Q20.** No. E07 was rated BB and then withdrawn for commercial reasons (A19), not defaulted.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which has RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08 expired.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals the Valdoria ceiling (A12, A14), and E15's A equals the Corvenia ceiling (A37, A41). No other country has a ceiling in the data.

**Q31.** No. E05 (BB) and E15 (A) are both at their ceilings, not above them.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the risk of the guarantor, E10 (Halden Bank), which is rated BBB+ after A27. I05 is guaranteed by E10.

**Q34.** No. E12 has no parent_id and no link to E09 or E10.

**Q35.** 3. These are E09, E10 and E11. E17 is a duplicate of E10, with the same LEI.

**Q36.** 2. These are E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and no link between them.

**Q39.** A. E02's rating is A (A08), affirmed by A09 on its duplicate record.

**Q40.** 6. These are E01, E02, E09, E12, E14 and E16. E07 was withdrawn and E10 is domiciled in DE.

**Q41.** BB+, from A44.

**Q42.** DE. The RATINGS record E10 says DE. The LU on E17 is a RESEARCH duplicate with the same LEI.

**Q43.** 0. The only LU record is E17, a duplicate of the DE-domiciled E10.

**Q44.** Yes, probably. I07 is in XVD, which appears to be Valdoria's currency, and its BBB- matches E05's local-currency rating. The data does not define XVD explicitly.

**Q45.** No. The ceiling (BB, A12) caps foreign-currency obligations, and I07 is a local-currency obligation.

**Q46.** No. E11 has only a "CO" type record (A46), not an issuer rating (LTIDR or STIDR). The data does not define CO.

**Q47.** None. A47 shows I08 as expired (EX) on 2026-09-01.

**Q48.** 7. I01 to I07 hold ratings, and I08 expired.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10", "E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 13},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06"]},
"Q19": {"issuers": ["E01", "E09"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 5},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05", "E15"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```