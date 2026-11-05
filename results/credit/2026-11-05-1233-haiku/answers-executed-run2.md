**Q1.** A-. E01's FC LTIDR was A- from 2024-03-12 to 2025-06-20 (A01), which covers 1 Jan 2025.

**Q2.** No. The 2026-02-10 change (A03) was an affirmation (AF) that moved the outlook to NEG while the rating stayed BBB. The last downgrade was in June 2025 (A02).

**Q3.** No, rating BB+. I02 has been BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive (POS). E02's current LTIDR is A with outlook POS from 2025-09-15 (A09).

**Q5.** The holder takes E02's credit risk, and the notes are rated A. I03 credit_risk_of is E02, and I03 is A (A11) with E02 also A POS.

**Q6.** The data doesn't state the reason explicitly. E05's FC rating is BB (A14), which equals the VD ceiling of BB (ceilings.csv), while its LC rating is BBB- (A13), which sits above that ceiling.

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and then RD (A22) in 2026, and E10 was downgraded to BBB+ on 2026-04-15 (A27). E06's 2026 RW and E07's WD are not downgrades.

**Q8.** E08. Its RD rating (A22) is in force, which is the default code. E07's WD is a withdrawal, not a default.

**Q9.** 12. These are the entities with an LTIDR valid on 1 Oct 2026: CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15. I excluded E07 because its rating is WD (withdrawn, A19).

**Q10.** Depends. The FC issuer rating is BB (A14), which is not investment grade, but the LC rating is BBB- (A13), which is.

**Q11.** BBB+. E14 was BBB+ from 2024-09-30 to 2025-11-20 (A36), which covers 1 Jun 2025.

**Q12.** A-. E14's A- ran from 2023-01-15 to 2024-09-30 (A34).

**Q13.** Once. The only downgrade action is A36 (DG, 2024-09-30). The RW and AF records that follow are not downgrades.

**Q14.** None. E12's first rating (A30) starts on 2024-02-01, after 1 Jan 2024.

**Q15.** A-. E10's A- ran until 2026-04-15 (A26), so it was still in force on 1 Jan 2026.

**Q16.** No. E14's rating stayed BBB+ throughout. Its watch (A35) and affirmation (A33) changed, but not the rating symbol.

**Q17.** No. E06 was A- until 2026-09-03, then went on RWN (A17), which is a watch placement, not a downgrade.

**Q18.** E06. A17 is RWN with no end date. E14's RWN ended on 2026-05-01.

**Q19.** E01 and E09. Both have NEG outlooks in force (A03, A25).

**Q20.** No. E07's current rating is WD (A19), which is withdrawal, not default.

**Q21.** E07. Its last rating is WD, so it has no active rating on 1 Oct 2026. This follows the Q9 treatment.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. E01's STIDR is F2 from 2026-02-10 (A04).

**Q24.** Yes, BBB. E01's LTIDR is BBB (A06), the lowest investment-grade category.

**Q25.** 5. The IG instruments in force are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+. E15's LC LTIDR is A+ (A40).

**Q27.** A-. I06 is A- from 2024-03-01 (A42).

**Q28.** BBB+. CV's FC LTIDR is BBB+ (A38).

**Q29.** None. VD has no rating records.

**Q30.** E05 and E15. E15's FC A equals the CV ceiling of A, and E05's FC BB equals the VD ceiling of BB.

**Q31.** No. No entity's FC issuer rating is above its country ceiling.

**Q32.** E09 (Halden Group plc). E11's ultimate_parent_id is E09.

**Q33.** The holder takes E10's credit risk, and the notes are rated BBB+. I05 credit_risk_of is E10, and I05 is BBB+ from 2026-04-15 (A29).

**Q34.** No. E12 has no parent or ultimate parent, while E10's ultimate parent is E09.

**Q35.** 3: E09, E10 and E11. E17 is a record merged into E10, not a separate entity.

**Q36.** 2: E02 and E04. E03 is a record merged into E02.

**Q37.** 16. entities.csv lists 16 entities (E03 and E17 are merged into E02 and E10).

**Q38.** No. They have different LEIs, countries (DE vs US), and no ancestry link.

**Q39.** A (positive outlook). E02's current LTIDR is A POS (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is GB but is excluded because it is withdrawn.

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** LU. Halden Bank (E10) is domiciled in Luxembourg.

**Q43.** 1. Only E10 is domiciled in LU.

**Q44.** Yes. I07 is marked local_currency = yes (currency XVD).

**Q45.** Yes. I07's rating of BBB- (A45) is above the VD ceiling of BB. The ceiling table doesn't say whether it applies only to foreign-currency ratings.

**Q46.** No. E11 has no LTIDR records.

**Q47.** None. I08 has no rating records.

**Q48.** 7. The rated instruments are I01, I02, I03, I04, I05, I06 and I07. I08 has no rating.

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
  "Q45": {"above_ceiling": "yes"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```