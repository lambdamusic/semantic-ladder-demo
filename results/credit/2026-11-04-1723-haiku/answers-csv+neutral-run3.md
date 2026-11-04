**Q1.** A-. Kestrel's FC long-term issuer rating was set to A- by A01 (2024-03-12) and not changed until A02 (2025-06-20).

**Q2.** No. The only 2026 action on E01 is an affirmation (A03, A04); the downgrade to BBB was A02 in 2025.

**Q3.** No, rated BB+. I02 was downgraded from BBB to BB+ by A07 (2025-06-20), the latest action on the instrument.

**Q4.** POS. E02 and E03 share LEI 213800PHEIYNJMHTDV74, so A09 (2025-09-15, recorded on E03) is the latest outlook for Northwind Holdings.

**Q5.** Northwind Holdings (E02). I03 is guaranteed by E02, so the holder takes E02's credit risk, and E02's rating is A (A09).

**Q6.** The FC rating (BB, A14) is capped by Valdoria's Country Ceiling of BB (A12). The LC rating (BBB-, A13) is not capped, so the gap reflects transfer and convertibility risk.

**Q7.** E08 and E10. A21 and A22 downgrade E08, and A27 downgrades E10. A29 downgrades instrument I05, not an issuer, and A44 is QA data.

**Q8.** E08. A22 (2026-07-08) set Saxby to RD, which the ontology defines as a default.

**Q9.** 12. The issuers with an LTIDR or STIDR rating on 2026-10-01 are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E04, E11 and VD have no issuer rating, E07 was withdrawn (A19), and E16 is QA.

**Q10.** Depends. Its LC rating is BBB- (A13, investment grade), but its FC rating is BB (A14, speculative grade).

**Q11.** BBB+. The latest action before 2025-06-01 is A36 (2024-09-30, downgrade to BBB+).

**Q12.** A-. A34 (2023-01-15) is the latest action before 2024-01-01.

**Q13.** Once. A36 (2024-09-30) is the only downgrade; A35 is a Rating Watch placement, not a downgrade.

**Q14.** None. Halden Foods' first action is A30 (2024-02-01), after 2024-01-01.

**Q15.** A-. A26 (2023-05-01) is the latest action before 2026-01-01; A27 (2026-04-15) came later. E17 is the same entity as E10.

**Q16.** No. The rating was BBB+ from A36 (2024-09-30) through A33 (affirmed, 2026-05-01), and the watch in A35 does not change the rating.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch placement, not a downgrade.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's watch from A35 was cleared by the later affirmation A33, whose watch field is blank (this reading assumes a blank watch means no watch).

**Q19.** E01 and E09. Their latest outlooks are NEG (A03, A25). E06's last explicit outlook is STA (A16) and E08's is STA (A20), so neither is negative.

**Q20.** No. E07's last action is a withdrawal (A19), which is not a default.

**Q21.** E07. A19 (2026-05-12) withdrew its only rating. E11 has never had an issuer rating; its CO (A46) is not a rating.

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2. A04 (2026-02-10) set the short-term rating on E01.

**Q24.** Yes. E01's LTIDR FC is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only expected (EX), so it is unrated.

**Q26.** A+. A40 (2024-03-01) is the LC rating on E15.

**Q27.** A-. A42 (2024-03-01) rates I06.

**Q28.** BBB+. A38 (2024-01-01) is the sovereign's FC issuer rating. The CV ceiling of A (A37) is not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which the ontology says is not the sovereign's issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB (A12/A14). E15's FC rating is A, equal to the CV ceiling of A (A37/A41).

**Q31.** No. Only VD and CV have ceilings in the data, and neither E05 nor E15 is above its ceiling.

**Q32.** E09 (Halden Group plc). E11 → E10 → E09, and E09 has no parent.

**Q33.** Halden Bank AG (E10). I05 is guaranteed by E10, so its holders take E10's risk, and it is rated BBB+ (A29), in line with E10's issuer rating.

**Q34.** No. E12 has no parent recorded, and E09 does not list it as a subsidiary.

**Q35.** 3. The Halden group is E09, E10 and E11.

**Q36.** 2. The Northwind group is E02 (with E03) and E04.

**Q37.** 16. The 19 records include QA record E16 (excluded) and duplicate records E03 and E17, leaving 16 distinct entities.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214).

**Q39.** A. Northwind Holdings' current LTIDR FC is A (A09, recorded on E03).

**Q40.** 5. The GB issuers with ratings on 2026-10-01 are E01, E02, E09, E12 and E14. E07 was withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, which the data says to ignore.

**Q42.** DE. RATINGS (E10) is the system of record, and E17 (RESEARCH, LU) is the same entity.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, domiciled in DE per RATINGS.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. The ceiling applies only to FC debt, and I07 is in XVD (local currency). Its BBB- rating is numerically above the BB ceiling, but the ceiling does not apply to it.

**Q46.** No. E11 has only a Credit Opinion (A46), which the ontology says is never an issuer rating.

**Q47.** None. I08 is only Expected (EX, A47), and it stays unrated until an AS action confirms it.

**Q48.** 7. I01 through I07 have ratings. I08 does not.

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