**Q1.** A-. Rating on 1 Jan 2025 is set by A01 (AS, A-, 2024-03-12); A02 (DG to BBB) came later.

**Q2.** No. The only 2026 actions on E01 are A03 (AF) and A04 (STIDR AF); the downgrade was A02 in 2025.

**Q3.** No, rated BB+. I02 is subordinated and its latest rating is A07 (DG to BB+, 2025-06-20).

**Q4.** POS (Positive). E02 and E03 are the same entity (same LEI), and the latest LTIDR action is A09 (AF, POS, 2025-09-15).

**Q5.** E02, rated A. I03 is guaranteed by E02, so it carries E02's credit risk, and its latest rating is A11 (AF, A).

**Q6.** Not in the JSON spec, so no field. The data does not state the reason. The likely cause is the Valdoria Country Ceiling (A12, BB): E05's FC rating is BB (A14), at the ceiling, while its LC rating BBB- (A13) is not capped, per the ontology.

**Q7.** E08 and E10. Both have 2026 DG actions (A21, A22 for E08; A27 for E10). I05 is also downgraded (A29), but it is an instrument, not an issuer.

**Q8.** E08. A22 (DG to RD, 2026-07-08) is the latest action, and RD is a default.

**Q9.** 12. Counting by LEI, the issuers with an LTIDR rating on 1 Oct 2026 are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is out (WD, A19), E04 and E11 have no LTIDR, VD has only a CC, and E16 is QA.

**Q10.** No on the headline FC rating: E05 is BB (A14). Its LC rating is BBB- (A13), which is investment grade, so the answer depends on which basis you mean.

**Q11.** BBB+. A36 (DG to BBB+, 2024-09-30) was the latest action before 1 June 2025.

**Q12.** A-. A34 (AS, 2023-01-15) was the latest action before 1 Jan 2024.

**Q13.** 1. A36 is the only DG action for E14.

**Q14.** None. E12's first rating is A30 (AS, BB-, 2024-02-01), which is after 1 Jan 2024.

**Q15.** A-. A26 (AS, 2023-05-01) was the rating until A27 (DG to BBB+) on 2026-04-15. E10 and E17 are the same entity, and RATINGS holds the parent and country.

**Q16.** No. The rating was BBB+ from A36 (2024-09-30) through A35 (RW, unchanged) and A33 (AF). Rating Watch and outlook changes do not change the rating.

**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative (RW), not a downgrade. The rating is still A-.

**Q18.** E06. A17 placed it on RWN with no later action. E14's RWN (A35) was followed by an affirmation (A33) with no watch flag, so I took that as resolved; the data does not say this explicitly.

**Q19.** E01 and E09. Their latest outlooks are NEG (A03 and A25). Outlooks not revised by a later action are assumed to carry forward.

**Q20.** No. A19 is a withdrawal (WD), which the ontology says is not a default.

**Q21.** E07. It had a rating (A18, BB) and was withdrawn (A19). E11 and VD never had an issuer rating (A46 is a credit opinion; A12 is a Country Ceiling).

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2. This is the latest STIDR action for E01 (A04, AF).

**Q24.** Yes. E01's latest LTIDR rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade on 1 Oct 2026. I02 is BB+, I04 is BB, and I08 is only an expected rating (EX, A47), so it is unrated.

**Q26.** A+. This is the LC rating from A40 (2024-03-01).

**Q27.** A-. I06 is subordinated and its latest rating is A42 (AS, A-), one notch below the A issuer rating (A41).

**Q28.** BBB+. This is CV's FC LTIDR from A38 (2024-01-01).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which the ontology says is not the sovereign's issuer rating.

**Q30.** E05 and E15. E05 is at its BB ceiling (A14, A12) and E15 is at its A ceiling (A41, A37). CV's issuer rating BBB+ (A38) is below its A ceiling.

**Q31.** No. E05 (BB) and E15 (A) are both exactly at their ceilings, not above.

**Q32.** E09 (Halden Group plc). E11's parent is E10, and E10's parent is E09, which has no parent.

**Q33.** E10 (Halden Bank AG), rated BBB+. I05 is guaranteed by E10, so its credit risk is E10's, and its latest rating is A29 (DG, BBB+).

**Q34.** No. E12 has no parent recorded and is not linked to E09 or E10; sharing the name "Halden" is not evidence of group membership.

**Q35.** 3. The Halden group is E09 (parent), E10 (also E17) and E11. E12 is not linked to the group.

**Q36.** 2. The Northwind group is E02 (also E03) and E04.

**Q37.** 16. There are 18 records; E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA and excluded. The two sovereigns have no LEI, so they count as their own entities (VD, CV).

**Q38.** No. E06 and E13 have different LEIs (ORRN00BANK00000DE233 and ORBC00BANCORP000US45).

**Q39.** A. E02/E03's latest LTIDR is A09 (AF, A, 2025-09-15).

**Q40.** 5. The GB issuers with an issuer rating on 1 Oct 2026 are E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, which the ontology says must be ignored.

**Q42.** DE. RATINGS (E10) holds the country, and RESEARCH (E17) says LU, which is overridden.

**Q43.** 0. The only LU record is E17, which is the same entity as E10 (DE per RATINGS).

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD, so it is local-currency debt.

**Q45.** No. The ceiling applies only to FC debt, and I07 is local-currency, so it is not capped even though BBB- is above BB numerically.

**Q46.** No. E11's only rating is a credit opinion (CO, A46), which the ontology says is not an issuer rating.

**Q47.** None. I08 has only an expected rating (EX, A47), which is not a rating until an AS action confirms it.

**Q48.** 7. I01 through I07 have ratings. I08 does not, since its only action is EX.

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
  "Q42": {"country": "DE"},
  "Q43": {"count": 0},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```