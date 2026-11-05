**Q1.** A-. E01's FC rating was A- from 2024-03-12 to 2025-06-20 (LTIDR, A01), which covers 1 January 2025.

**Q2.** No. E01's FC rating was BBB from 2025-06-20 and is unchanged in 2026; the 2026-02-10 record (A03) only moved the outlook to NEG.

**Q3.** No, rating BB+. I02 is rated BB+ (A07, from 2025-06-20), below investment grade.

**Q4.** POS (Positive). E02's LTIDR FC outlook is POS from 2025-09-15, still open (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03's credit_risk_of is E02 (guarantor), and I03 is rated A (A11), matching E02's A rating (A09).

**Q6.** Probably the Valdoria country ceiling. E05's FC rating is BB, equal to the VD ceiling of BB (ceilings.csv, from 2025-04-01), while its LC rating is BBB-. The data does not state the reason, so this is inferred.

**Q7.** E08 and E10. E08 went B → CCC (2026-01-20, A21) and then to RD (2026-07-08, A22). E10 went A- → BBB+ (2026-04-15, A27).

**Q8.** E08. Its current rating is RD (A22, from 2026-07-08).

**Q9.** 12. These entities hold an open LTIDR issuer rating: CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15. I excluded E07 (WD, withdrawn), and VD, E04 and E11 have no ratings. This count includes the sovereign CV.

**Q10.** Depends. E05's FC issuer rating is BB (non-IG), but its LC rating is BBB- (IG).

**Q11.** BBB+. E14 was BBB+ from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. E14 was A- from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. E14's only downgrade was A- → BBB+ on 2024-09-30 (A36). Later records (A35, A33) are a watch placement and an affirmation.

**Q14.** None. E12's first rating (BB-) starts 2024-02-01 (A30), after 1 January 2024.

**Q15.** A-. E10 was A- from 2023-05-01 to 2026-04-15 (A26).

**Q16.** No. E14 stayed at BBB+ from 2024-09-30 onward; the 2025-11-20 Rating Watch (A35) did not change the rating.

**Q17.** No. E06 stayed at A-; the 2026-09-03 change is a Rating Watch Negative (A17), not a downgrade.

**Q18.** E06. It is on RWN from 2026-09-03 (A17), still open. E14's RWN ended 2026-05-01.

**Q19.** E01 and E09. E01's LTIDR outlook is NEG from 2026-02-10 (A03), and E09's is NEG from 2026-03-01 (A25).

**Q20.** No. E07 is WD (withdrawn, A19), not a default rating.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19), so it had a rating earlier (A18) but none on 1 October 2026.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. E01's STIDR FC is F2 from 2026-02-10 (A04).

**Q24.** Yes. E01's LTIDR FC is BBB (A02, A03), which is investment grade.

**Q25.** 5. The investment-grade instrument ratings in force on 1 October 2026 are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are non-IG, and I08 has no rating.

**Q26.** A+. E15's LTIDR LC rating is A+ from 2024-03-01 (A40).

**Q27.** A-. I06 is rated A- from 2024-03-01 (A42).

**Q28.** BBB+. CV's LTIDR FC rating is BBB+ from 2024-01-01 (A38).

**Q29.** None. VD has no rating records in ratings.csv.

**Q30.** E05 and E15. E05 (VD, BB) and E15 (CV, A) have FC ratings exactly equal to their country ceilings (BB and A). CV's own rating (BBB+) is below its ceiling.

**Q31.** No. E05 (BB) and E15 (A) are at their ceilings, not above them. The ceilings table only covers CV and VD, so I cannot check other countries.

**Q32.** E09 (Halden Group plc). E11's ultimate_parent_id is E09 (ancestors: E10 at 1 level, E09 at 2).

**Q33.** E10 (Halden Bank), rated BBB+. I05's credit_risk_of and guarantor are E10, and I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent or ultimate parent, and Halden Bank's group (E09, E10, E11) doesn't include it. The shared name is the only link.

**Q35.** 3. The Halden group is E09, E10 and E11.

**Q36.** 2. The Northwind group is E02 and E04.

**Q37.** 16. There are 16 entity records in entities.csv (including the two sovereigns, CV and VD). E03 and E17 are merged into other entities, not counted separately.

**Q38.** No. They have different IDs, LEIs and countries (E06 is DE; E13 is US) and no parent link.

**Q39.** A. E02's LTIDR FC rating is A (A09).

**Q40.** 5. The GB issuers with an issuer rating on 1 October 2026 are E01, E02, E09, E12 and E14. E07 is also GB but is withdrawn.

**Q41.** None. Brindle Capital does not appear in the dataset.

**Q42.** LU (Luxembourg). E10's country is LU.

**Q43.** 1. Only E10 is domiciled in LU.

**Q44.** Yes. I07 is marked local_currency = yes (XVD).

**Q45.** Depends. I07 is rated BBB- and VD's ceiling is BB, so it is numerically above the ceiling. However, the ceiling table doesn't say whether it applies to local-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 has no LTIDR records in ratings.csv.

**Q47.** None. I08 has no rating record in ratings.csv.

**Q48.** 7. Instruments I01 through I07 have ratings in force on 1 October 2026; I08 does not.

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
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```