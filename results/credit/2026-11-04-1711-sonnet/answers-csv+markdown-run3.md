**Q1.** A-. A01 (2024-03-12) set E01 at A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation (AF), and an AF is not a downgrade.

**Q3.** No. I02 is rated BB+ (A07, 2025-06-20), which is speculative grade.

**Q4.** Positive. E03 shares its LEI with E02, so they are one entity. A09 (2025-09-15) is the latest action and gives POS.

**Q5.** The holder takes the risk of E02, the guarantor of I03, rated A. The latest action on that entity is A09, which affirms A.

**Q6.** Valdoria's Country Ceiling is BB (A12) and caps the foreign-currency rating (A14, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27 (E17 is the same entity as E10). E16's downgrade (A44) is QA data and is ignored. I05's downgrade (A29) is an instrument rating, not an issuer rating.

**Q8.** E08. A22 (2026-07-08) moved it to RD, which is a default.

**Q9.** 12 issuers: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19). E11 has only a credit opinion (A46). E04 and VD have no issuer rating (VD has only a Country Ceiling).

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and A35 is only a Watch.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, which is A36. A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 set E10 at A- in 2023, and the downgrade A27 came only on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33).

**Q17.** No. A17 is a Rating Watch (RW) that leaves the rating at A-.

**Q18.** E06 (A17, RWN). E14's Watch from A35 was cleared by A33, which carries no watch.

**Q19.** E01 and E09. A03 and A25 both carry a NEG outlook, and E02's outlook is POS.

**Q20.** No. E07 was withdrawn (A19, WD), which is not a default.

**Q21.** E07. It had a rating, but A19 withdrew it.

**Q22.** E08, because of the RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's current rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only an expected rating.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The Country Ceiling of A (A37) is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB, and E15's foreign-currency rating of A equals CV's ceiling of A.

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05, rated BBB+ (A27).

**Q34.** Yes. E12 has no parent record, so it is not part of the Halden group (E09, E10, E11).

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. The 19 records contain two duplicates (E03 is E02, and E17 is E10) and one QA record (E16).

**Q38.** No. The two records have different LEIs.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA data.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** DE. The RATINGS record E10 overrides the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, and RATINGS holds for that entity, which makes it DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of E05's country VD.

**Q45.** No. I07 is rated BBB- (A45). It is a local-currency obligation, so the BB ceiling does not apply.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX), so I08 stays unrated.

**Q48.** 7, which is I01 to I07.

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
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```