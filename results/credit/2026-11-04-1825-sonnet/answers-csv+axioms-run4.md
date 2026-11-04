**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed it until A02 on 2025-06-20.

**Q2.** No. The only 2026 action on Kestrel Energy's issuer rating is A03, an affirmation at BBB. The downgrade (A02) was in 2025.

**Q3.** No. Its rating is BB+ (A07), which is below investment grade.

**Q4.** Positive. A09 is booked on E03, which shares E02's LEI, so it is the same entity. A09 (2025-09-15) is the latest action and supersedes A08's Stable.

**Q5.** The credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and the current rating is A09 (via E03).

**Q6.** The foreign-currency rating is capped by the Country Ceiling. VD's ceiling is BB (A12), so the FC rating is BB (A14), while the LC rating is BBB- (A13). The data does not state the reason explicitly, so this is inferred from the ceiling.

**Q7.** E08 and E10. E08 had A21 and A22 in 2026, and E10 had A27. E16's downgrade (A44) is excluded because E16 is a QA test record.

**Q8.** E08. A22 (RD, 2026-07-08) is still in force.

**Q9.** 12. These are E01, E02 (merged with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded it to BBB+.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade. A35 is a watch placement.

**Q14.** None. Halden Foods was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 was in force until the 2026-04-15 downgrade (A27).

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33). A35 was only a watch.

**Q17.** No. A17 is a Rating Watch placement with the rating unchanged at A-.

**Q18.** E06, from A17. E14's watch (A35) was superseded by A33.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. Pellam Retail was withdrawn (A19) and never rated RD or D.

**Q21.** E07. Its rating was withdrawn by A19.

**Q22.** E08, which was rated RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The rating is BBB.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD only has a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 (FC BB, VD ceiling BB) and E15 (FC A, CV ceiling A).

**Q31.** No. E05 and E15 are exactly at their ceilings.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** The credit risk of E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, and A27 is its current rating.

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries and no link.

**Q39.** A, from A09 (booked on E03, the same entity).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is a QA record.

**Q41.** None. E16 is a QA test record, so its actions are not rating actions in force.

**Q42.** DE. The RATINGS record E10 says DE, and E17 (LU, RESEARCH) defers to it.

**Q43.** 0. E17's LU is overridden by E10's DE domicile.

**Q44.** Yes. I07 is in XVD, which is the domestic currency of VD (the domicile of E05).

**Q45.** No. The ceiling applies to foreign-currency issuer ratings, and I07 is a local-currency note rated BBB- (A45).

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (A), not a rating in force.

**Q48.** 7: I01 through I07. I08 has only an expected rating.

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
"Q37": {"count": 17},
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