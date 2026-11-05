**Q1.** A-. A01 assigned A- on 2024-03-12, and the downgrade to BBB (A02) came only on 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the last downgrade was A02 in 2025.

**Q3.** No, it is BB+. I02 was downgraded from BBB to BB+ on 2025-06-20 (A07).

**Q4.** Positive, going by the latest action (A09, 2025-09-15). E02 shows Stable (A08, 2023), but E03 shares E02's LEI and conflicts with it, so the record is ambiguous.

**Q5.** Northwind Finance 2030 notes (I03) carry A risk of guarantor E02, not issuer E04. E04 has no rating of its own, and the note's A rating matches E02's A (A08, A11).

**Q6.** Valdoria Telecom's foreign-currency rating (BB, A14) equals Valdoria's country ceiling (BB, A12), while its local-currency rating is BBB- (A13). The data does not state the cause; the ceiling match is the likely explanation.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44). E11 is also named through I05 (A29), but that is an instrument downgrade, not an issuer downgrade.

**Q8.** Saxby Shipping (E08), which was rated RD on 2026-07-08 (A22).

**Q9.** 13 distinct legal entities. E01, E02/E03 (one LEI), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15 and E16 all hold a live LTIDR; E07 was withdrawn (A19).

**Q10.** Depends on currency. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. Marlow's BBB+ came from A36 (2024-09-30), and the rating watch (A35) did not change the level.

**Q12.** A-. A34 assigned A- on 2023-01-15, and nothing changed it before 2024.

**Q13.** Once. The only downgrade is A36 (2024-09-30); A35 is a watch placement, not a downgrade.

**Q14.** None. Halden Foods' first rating is BB- (A30), dated 2024-02-01, after 1 January 2024.

**Q15.** A-. Halden Bank AG (E10) was rated A- (A26); the downgrade to BBB+ (A27) came on 2026-04-15, after 1 January 2026. E17 is the same LEI but has no actions.

**Q16.** No. The rating stayed BBB+ throughout (A36, A35, A33); only the watch status changed.

**Q17.** No. Orrin Bank AG (E06) had a rating watch negative placed on 2026-09-03 (A17), but its A- rating was not lowered.

**Q18.** Orrin Bank AG (E06), on watch from A17. Marlow (E14) had a watch placed in A35, but the 2026-05-01 affirmation (A33) carries no watch flag, so I treated it as resolved.

**Q19.** Kestrel Energy (E01, A03) and Halden Group (E09, A25).

**Q20.** No. Pellam's rating was withdrawn (A19), and no default is recorded.

**Q21.** Pellam Retail (E07), withdrawn on 2026-05-12 (A19). Halden Leasing (E11) had a CO rating (A46), but the code is undefined, so I did not count it as an issuer rating.

**Q22.** Saxby Shipping (E08), rated RD (A22).

**Q23.** F2, from A04 (2026-02-10).

**Q24.** Yes. The issuer rating is BBB (A03), which is investment grade.

**Q25.** 6. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A) are investment grade. I08's latest action is EX (A47), which is undefined in the data; if it means the instrument is gone, the count is 5.

**Q26.** A+, from A40 (local currency, 2024-03-01).

**Q27.** A-, from A42.

**Q28.** BBB+, from A38 (foreign currency, 2024-01-01).

**Q29.** None. The Republic of Valdoria has only a country ceiling (BB, A12), not an issuer rating.

**Q30.** Valdoria Telecom (E05, FC BB = VD ceiling BB) and Corvenia Power (E15, FC A = CV ceiling A). The data records ceilings only for VD and CV, so other countries cannot be checked.

**Q31.** Depends. No company in VD or CV is above its ceiling, but the data has no ceiling for any other country, so the question cannot be fully answered.

**Q32.** Halden Group plc (E09). Halden Leasing (E11) → Halden Bank AG (E10) → E09.

**Q33.** Halden Leasing 2028 notes (I05) carry BBB+ risk of guarantor E10, which matches E10's BBB+ (A27).

**Q34.** No. Halden Foods (E12) has no parent recorded, and its name match with Halden Bank is not a data link.

**Q35.** 3: Halden Group (E09), Halden Bank AG (E10) and Halden Leasing (E11). E17 is a duplicate of E10.

**Q36.** 2 distinct entities (Northwind Holdings E02 and Northwind Finance E04). E03 is a duplicate of E02 by LEI, so there are 3 records but 2 entities.

**Q37.** 17 distinct legal entities across 19 records. E02/E03 and E10/E17 are duplicate pairs by LEI, and the two sovereigns (VD, CV) are counted as entities.

**Q38.** No. Their LEIs and countries differ (E06 DE, E13 US).

**Q39.** A. Both E02 (A08) and E03 (A09) show A.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn.

**Q41.** BB+, from A44 (2026-06-01).

**Q42.** DE, per the rated record E10. E17 records LU, which conflicts with E10.

**Q43.** 1 record (E17). It is the same LEI as E10, which is recorded as DE, so the data conflicts.

**Q44.** Yes. The note is in currency XVD (the Valdoria code), and its BBB- rating matches the local-currency rating (A13), not the foreign-currency rating.

**Q45.** No. The note is BBB- and so numerically above the BB ceiling (A12), but the ceiling constrains foreign-currency obligations and this note is in local currency.

**Q46.** No. Halden Leasing has only a CO rating (A46), which is undefined, not an LTIDR.

**Q47.** A, from A47 (2026-09-01). The EX action code is undefined, so the status is uncertain.

**Q48.** 8. Every instrument has a rating, though I08's EX action is uncertain.

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
  "Q25": {"count": 6},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E15"]},
  "Q31": {"any": "depends"},
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
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```