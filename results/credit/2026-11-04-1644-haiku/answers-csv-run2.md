**Q1.** A-. The rating was assigned on 2024-03-12 (A01) and not cut until 2025-06-20 (A02, to BBB), so it was still A- on 1 January 2025.

**Q2.** No. The 2026 actions on E01 are an affirmation to BBB (A03) and an affirmation of F2 (A04).

**Q3.** No, rated BB+. I02 is subordinated and was cut to BB+ on 2025-06-20 (A07).

**Q4.** Positive, but the data conflicts. The latest action (A09, 2025-09-15) is on E03, which has the same LEI as E02 and comes from the RESEARCH system, and it says POS. E02's own record says STA (A08), so the data can't settle which is current.

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02 (guarantor_id), and the instrument carries A (A11).

**Q6.** The data doesn't state a reason. The timing fits the sovereign country ceiling of BB set the same day (A12, against FC BB in A14 and LC BBB- in A13), but this is inference.

**Q7.** E08, E10 and E16. Each has a 2026 downgrade: A21/A22, A27 and A44. (A29 downgrades an instrument, not an issuer.)

**Q8.** E08. Its distressed debt exchange was rated RD on 2026-07-08 (A22), and no later action changes that.

**Q9.** 13. Counted are E01, E02 (E03 is the same LEI), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. Excluded are E07 (withdrawn, A19), E11 (only a CO rating, A46), E04 (no rating) and VD (only a country ceiling, A12).

**Q10.** Depends on currency. The FC rating is BB (A14), which is non-IG, and the LC rating is BBB- (A13), which is IG.

**Q11.** BBB+. The downgrade to BBB+ took effect on 2024-09-30 (A36), and the later RW (A35) didn't change the rating.

**Q12.** A-. This is the rating set on 2023-01-15 (A34), and no action came before 1 January 2024.

**Q13.** 1. The only downgrade is A36 (A- to BBB+, 2024-09-30). The later watch action (A35) isn't a downgrade.

**Q14.** None. Halden Foods' first rating is BB- on 2024-02-01 (A30), after 1 January 2024.

**Q15.** A-. E10 (Halden Bank) was A- until its cut to BBB+ on 2026-04-15 (A27). E17 has the same LEI and no rating actions.

**Q16.** No. The rating stayed BBB+ after 1 January 2025 (A36, A35, A33). The Nov 2025 watch placement (A35) and the May 2026 affirmation (A33) don't change the rating.

**Q17.** No. The only 2026 action on E06 is a Rating Watch Negative on A- (A17), and watch placement isn't a downgrade.

**Q18.** E06 only, on the A17 watch. E14's watch from A35 appears to have been cleared by the later affirmation A33, which carries no watch flag.

**Q19.** E01 (outlook NEG, A03) and E09 (NEG, A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19), and no other entity lost its rating.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2 (A04, 2026-02-10).

**Q24.** Yes. The issuer rating is BBB (A03), which is investment grade.

**Q25.** 6. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A) are investment grade. I08 depends on A47, whose action code EX isn't defined in the data. Without I08 the count is 5.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38, FC). This is below the country ceiling of A (A37).

**Q29.** None. VD has only a country ceiling record (A12, CC), not an issuer rating.

**Q30.** E05 (FC BB, A14, equal to the Valdoria ceiling of BB, A12) and E15 (FC A, A41, equal to the Corvenia ceiling of A, A37).

**Q31.** No. Both FC ratings in the ceiling countries sit exactly at the ceiling, not above it. The data has no ceilings for other countries.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank AG), rated BBB+ (A29). I05 is guaranteed by E10 (guarantor_id).

**Q34.** No. E12 has no parent_id and a different LEI from the Halden group entities.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10, so it isn't a separate entity.

**Q36.** 2: E02 and E04. E03 has the same LEI as E02, so it isn't a separate entity.

**Q37.** 17 counting the two sovereigns, which appear as entities in the data. There are 19 rows, and E03 and E17 duplicate E02 and E10 by LEI. Excluding the sovereigns, which have no LEI, gives 15.

**Q38.** No. They have different LEIs, countries (DE vs US) and no parent link.

**Q39.** A (A08 and A09 both give A for Northwind Holdings), though their outlooks differ.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded (withdrawn), and E03 is a duplicate of E02.

**Q41.** BB+ (A44, 2026-06-01), a downgrade from BBB- (A43).

**Q42.** DE, per E10 (the rated record). E17 gives LU for the same LEI, so the data conflicts.

**Q43.** 0 under the DE reading of E10. The only LU record is E17, and it shares an LEI with the DE entity E10. It would be 1 if E17's LU domicile is correct.

**Q44.** Depends. XVD is not defined in the data, and I07 has no ccy_basis field. It is probably Valdoria's local currency, but the data doesn't say so.

**Q45.** Depends. I07 is rated BBB-, above the BB Valdoria ceiling (A12). But ceilings cap only foreign-currency ratings, so this holds only if XVD is not local currency (see Q44).

**Q46.** No. E11 has only a CO rating (A46), and CO is not an issuer-rating type.

**Q47.** A (A47). The action code EX is undefined in the data, so the rating is taken from the record's rating field.

**Q48.** 8: all instruments, including I08 with its A rating (A47). Without I08 the count is 7. This depends on the same undefined EX code as Q25.

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