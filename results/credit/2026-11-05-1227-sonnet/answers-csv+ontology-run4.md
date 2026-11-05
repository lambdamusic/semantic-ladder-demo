**Q1.** A-. A01 set A- on 2024-03-12, and the next action (A02) came on 2025-06-20.

**Q2.** No. The only 2026 action on Kestrel (E01) is A03, an affirmation (AF) with the outlook moved to negative, which is not a downgrade.

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is guaranteed by E02, whose latest rating is A (A09).

**Q6.** The foreign-currency rating is capped by Valdoria's Country Ceiling of BB (A12). The local-currency rating of BBB- (A13) is not capped, while the FC rating is BB (A14).

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 is an instrument rating and A44 is a QA record, so both are excluded.

**Q8.** E08. A22 moved it to RD, which is a default, on 2026-07-08.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E04, E11 and VD have no issuer rating, and E16 is QA.

**Q10.** No. Its headline foreign-currency rating is BB (A14), which is speculative grade. Only the local-currency rating, BBB- (A13), is investment grade.

**Q11.** BBB+. A36 downgraded Marlow (E14) to BBB+ on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-, from A34.

**Q13.** 1, from A36. A35 is a Watch and A33 is an affirmation.

**Q14.** None. Halden Foods (E12) was first rated on 2024-02-01 (A30).

**Q15.** A-. E17 is the same entity as E10, and the downgrade to BBB+ (A27) came only on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 was a Watch and A33 an affirmation.

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-.

**Q18.** E06, from A17. E14's Watch (A35) was superseded by the affirmation A33, which carries no watch.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The rating is BBB (A02, affirmed by A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only an expected rating (EX).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings, not above them, and no other country has a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link, so it is outside the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 duplicates E02, E17 duplicates E10, and E16 is QA test data.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A, from A09 (E03 is the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, because the RESEARCH record E17 holds for country.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH holds on domicile, and E17 says LU.

**Q43.** 1, Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, and its BBB- (A45) is fine.

**Q46.** No. E11 has only a credit opinion (A46, type CO), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated until an Assigned action confirms it.

**Q48.** 7, which is I01 to I07. I08 is unrated.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
"Q10": {"investment_grade": "no"},
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
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```