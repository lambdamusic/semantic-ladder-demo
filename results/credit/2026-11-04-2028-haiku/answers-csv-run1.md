**Q1.** A-. Kestrel's rating was A- from A01 (2024-03-12) until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. E01's 2026 actions are affirmations only (A03, A04), and its last downgrade was A02 in 2025.

**Q3.** No, it is BB+. I02 was downgraded from BBB to BB+ on 2025-06-20 (A07).

**Q4.** POS, but the data conflicts. The latest action (A09, 2025-09-15) is on E03, which shares E02's LEI and says Positive, while E02's own record (A08, 2023) says Stable.

**Q5.** The guarantor, E02 (Northwind Holdings), whose guarantee backs the notes issued by E04. The instrument is rated A (A10, A11).

**Q6.** The data does not state a reason. E05's foreign-currency rating (BB, A14) equals the Republic of Valdoria's country ceiling (BB, A12), which is consistent with the ceiling capping FC ratings, while its local-currency rating is BBB- (A13).

**Q7.** E08, E10, E16. These are the issuer-level downgrades (A21, A22, A27, A44). The I05 downgrade (A29) is on an instrument issued by E11, not an issuer rating action.

**Q8.** E08. Its RD rating (A22, 2026-07-08) is a default rating.

**Q9.** 13. These are the entities with a live LTIDR on 2026-10-01: E01, E02 (E03 is a duplicate by LEI), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16, and CV. E07 was withdrawn (A19).

**Q10.** Depends on currency. E05 is BBB- in local currency (A13, investment grade) but BB in foreign currency (A14, not investment grade).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36), and that rating was still in place in 2025.

**Q12.** A-. A34 (2023-01-15) assigned A-, and the first change was A36 on 2024-09-30.

**Q13.** 1. A36 (2024-09-30) is the only downgrade. A35 is a rating watch placement, not a downgrade.

**Q14.** None. E12's first rating is A30 (2024-02-01), after the date asked about.

**Q15.** A-. E10 was A- under A26 until it was downgraded to BBB+ on 2026-04-15 (A27). E17 has the same LEI but no ratings.

**Q16.** No. The rating has been BBB+ since A36 (2024-09-30). The 2025-11-20 watch placement (A35) did not change it, and A33 affirmed it.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement (A17), not a downgrade.

**Q18.** E06. A17 (2026-09-03) placed it on watch, and nothing in the data resolves that before 2026-10-01. E14's watch (A35) was cleared by the affirmation in A33 (2026-05-01).

**Q19.** E01 and E09. Their latest outlooks are NEG (A03, A25). The other entities show STA or POS.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07. Its last LTIDR action was a withdrawal (A19, 2026-05-12). VD and E11 never had an LTIDR.

**Q22.** E08. Only A22 (RD) is a default.

**Q23.** F2. A04 (2026-02-10) affirmed the short-term rating at F2.

**Q24.** Yes, BBB (A03, FC). BBB is investment grade.

**Q25.** 6. Assuming the EX action on I08 (A47) leaves its rating in place, the investment-grade instruments are I01, I03, I05, I06, I07, and I08. I02 and I04 are not.

**Q26.** A+. This is the only LC record for E15 (A40, 2024-03-01).

**Q27.** A-. A42 (2024-03-01) assigned I06 A-.

**Q28.** BBB+. A38 (FC LTIDR for CV, STA) remains the latest action.

**Q29.** None. VD has only a country ceiling rating (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating (BB, A14) equals Valdoria's ceiling (BB, A12), and E15's FC rating (A, A41) equals Corvenia's ceiling (A, A37).

**Q31.** No. E05 and E15 are exactly at their ceilings, not above them.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09.

**Q33.** The guarantor, E10 (Halden Bank AG), whose guarantee backs the notes issued by E11. The instrument is rated BBB+ (A29, 2026-04-15).

**Q34.** No. E12 has no parent link, and the data does not connect it to E09 or E10. Name similarity is not evidence of a shared group.

**Q35.** 3: E09, E10, and E11. E17 duplicates E10's LEI, so it adds no entity.

**Q36.** 2: E02 and E04. E03 duplicates E02's LEI.

**Q37.** 17. There are 19 records, and E03 and E17 duplicate E02 and E10 by LEI. This includes the two sovereigns (VD, CV), which have no LEI; excluding them gives 15.

**Q38.** No. They have different LEIs, countries (DE and US), and no parent link.

**Q39.** A. E02's record (A08) and E03's record (A09) both show A.

**Q40.** 6: E01, E02, E09, E12, E14, and E16. E07 is GB but withdrawn, and E03 duplicates E02.

**Q41.** BB+. A44 (2026-06-01) downgraded it from BBB-.

**Q42.** DE. E10 (Halden Bank AG) is domiciled in DE. E17, which shares its LEI, lists LU, which conflicts.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE). Taking E17's country at face value gives 1.

**Q44.** Depends. XVD is never defined as Valdoria's currency, and I07 has no ccy_basis. The VD prefix suggests it is local.

**Q45.** Depends. BBB- is above the BB ceiling (A12, A45), but the ceiling caps only foreign-currency obligations. If XVD is local currency, the ceiling does not apply.

**Q46.** No. E11 has only a CO rating (A46, BBB), which is not an LTIDR issuer rating. The CO code is undefined, so a different reading would change this answer.

**Q47.** A. A47 (2026-09-01) is the latest action. The EX code is undefined, so I assume the rating stands.

**Q48.** 8. All instruments carry a rating on 2026-10-01. If EX removed I08's rating, the count would be 7.

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
  "Q10": {"investment_grade": "depends", "rating": "BB (FC) / BBB- (LC)"},
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
  "Q24": {"investment_grade": "yes", "rating": "BBB"},
  "Q25": {"count": 6},
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
  "Q44": {"local_currency": "depends"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```