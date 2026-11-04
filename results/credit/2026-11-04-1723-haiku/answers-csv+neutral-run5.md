**Q1.** A-
A01 (2024-03-12, LTIDR FC) is the latest action on or before 2025-01-01; the next action is A02 (2025-06-20).

**Q2.** No.
The 2026 actions on E01 (A03, A04) are affirmations, and A03 only moved the outlook to NEG.

**Q3.** No, BB+.
I02 (subordinated) was last set to BB+ by A07 (2025-06-20), which is speculative grade.

**Q4.** POS (Positive).
E02 and E03 are the same entity (same LEI), and the latest outlook is set by A09 (2025-09-15).

**Q5.** Northwind Holdings (E02), rated A.
I03 is guaranteed by E02, so holders carry E02's credit risk, and A11 (2025-09-15) rates the notes A.

**Q6.** The FC rating (BB, A14) sits at the Valdoria Country Ceiling of BB (A12), while the LC rating (BBB-, A13) is not capped. The ontology says FC ratings are generally no higher than the ceiling, but the data does not record the analyst's reasoning. (Q6 is not in the JSON spec, so it is omitted there.)

**Q7.** E08, E10.
A21 and A22 downgrade E08 in 2026, and A27 (2026-04-15) downgrades E10. A29 downgrades an instrument, not an issuer.

**Q8.** E08.
A22 (2026-07-08) sets E08 to RD, a default.

**Q9.** 12.
Issuer ratings are held by E01, E02, E05, E06, E08 (RD), E09, E10, E12, E13, E14, CV and E15. E04, E07 (withdrawn by A19), E11 (CO only) and VD (ceiling only) do not hold one, and E16 is QA.

**Q10.** Depends.
Its LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative, A14).

**Q11.** BBB+.
A36 (2024-09-30, DG to BBB+) is the latest action on or before 2025-06-01; A35 (2025-11-20) comes later.

**Q12.** A-.
A34 (2023-01-15) is the latest action on or before 2024-01-01.

**Q13.** 1.
A36 (2024-09-30) is the only DG on E14. A35 is a Watch and A33 is an affirmation.

**Q14.** None.
E12's first action, A30 (2024-02-01), comes after 2024-01-01.

**Q15.** A-.
A26 (2023-05-01) is the latest action on or before 2026-01-01; A27 (BBB+) is dated 2026-04-15.

**Q16.** No.
The rating was BBB+ from A36 (2024-09-30) through A33 (2026-05-01). A35 placed it on Watch, which is not a rating change.

**Q17.** No.
E06's actions are A16 (2024, AS) and A17 (2026-09-03, Watch), with no downgrade.

**Q18.** E06.
A17 (2026-09-03) sets RWN. A35 (E14) was superseded by the AF in A33 (2026-05-01), which carries no watch.

**Q19.** E01, E09.
A03 (E01) and A25 (E09) set NEG, and no later action on either changes the outlook.

**Q20.** No.
E07's rating was withdrawn by A19 (2026-05-12), and a withdrawal is not a default.

**Q21.** E07.
E07 had a BB rating (A18) that was withdrawn (A19). E11 and VD never held an issuer rating.

**Q22.** E08.
E08 went to RD (A22), and no other entity has D or RD.

**Q23.** F2.
A04 (2026-02-10, STIDR) is E01's latest short-term action.

**Q24.** Yes, BBB.
A03 (2026-02-10, AF) keeps E01's LTIDR at BBB, which is investment grade.

**Q25.** 5.
I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 is BB+, I04 is BB, and I08 is only expected (A47).

**Q26.** A+.
A40 (2024-03-01, LC) is the only LC action on E15.

**Q27.** A-.
A42 (2024-03-01) rates I06, the 2032 subordinated note.

**Q28.** BBB+.
A38 (2024-01-01, FC) is the sovereign's FC issuer rating. A37 (A) is the ceiling, not the rating.

**Q29.** None.
VD has only a Country Ceiling (A12, BB) and no LTIDR action.

**Q30.** E05, E15.
E05 (FC BB, A14) matches the VD ceiling of BB (A12), and E15 (FC A, A41) matches the CV ceiling of A (A37). E06, E08 and E13 have no ceilings in the data.

**Q31.** No.
No company's FC rating is above its ceiling. E05 is at BB and E15 is at A.

**Q32.** E09.
E11's parent is E10, and E10's parent is E09, which has no parent.

**Q33.** E10, rated BBB+.
I05 is guaranteed by E10, so holders carry E10's risk, and A29 (2026-04-15) rates the notes BBB+.

**Q34.** No.
E12 has no parent and no link to E09 or E10. The shared name is not evidence of a group.

**Q35.** 3.
The Halden group is E09, E10 and E11. E17 is the same entity as E10, and E12 is not linked.

**Q36.** 2.
The Northwind group is E02 (with E03 as the same entity) and E04.

**Q37.** 16.
There are 18 records, but E03 and E17 duplicate E02 and E10, and E16 is a QA record. The 16 real entities include the two sovereigns, VD and CV.

**Q38.** No.
E06 (LEI 549300AMVE…) and E13 (LEI 815600O8X…) have different LEIs.

**Q39.** A.
A09 (2025-09-15, AF) is the latest LTIDR action on E02/E03.

**Q40.** 5.
GB issuers with a rating are E01, E02, E09, E12 and E14. E07 was withdrawn, and E16 is QA.

**Q41.** None.
E16 is a QA record, which must be ignored, so Brindle has no rating.

**Q42.** DE.
RATINGS is the system of record and holds E10's country as DE, not the RESEARCH record's LU (E17).

**Q43.** 0.
No entity is domiciled in LU once the RATINGS record (DE) is applied to E17's conflicting LU value.

**Q44.** Yes.
I07 is in XVD, the domestic currency of VD, so it is local-currency debt.

**Q45.** No.
The ceiling applies only to FC ratings and FC debt, and local-currency debt is not capped. I07 is local-currency debt, so it is not subject to the BB ceiling.

**Q46.** No.
E11 has only a credit opinion (A46, CO), which is never counted as a rating.

**Q47.** None.
A47 (2026-09-01) is an Expected (EX) action, and the instrument stays unrated until an AS action confirms it.

**Q48.** 7.
I01 through I07 are rated. I08 is unrated because its only action is EX (A47).

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