**Q1.** BBB. Kestrel's LTIDR (E01, FC) was A- from A01 (2024-03-12) and downgraded to BBB on 2025-06-20 (A02), so on 2025-01-01 it was A-. Correction: the rating on 1 January 2025 is A-, since A02 came after that date.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, both affirmations (AF); the NEG outlook in A03 is not a downgrade.

**Q3.** No. I02 (the 2031 subordinated note) was rated BBB on 2024-03-12 (A23) and then BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive (POS). Northwind Holdings is one entity under E02 and E03 (same LEI), and the latest LTIDR action is A09 (2025-09-15, E03), which affirmed A with a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is issued by the finance subsidiary E04 but guaranteed by E02, whose latest LTIDR is A (A09, same entity as E03); the instrument itself was affirmed at A (A11).

**Q6.** Valdoria Telecom's FC LTIDR is BB (A14) versus BBB- for LC (A13). The FC rating is capped by Valdoria's Country Ceiling of BB (A12), which reflects transfer and convertibility risk; LC ratings are not capped.

**Q7.** E08 only. Saxby Shipping was downgraded in 2026 twice (A21 to CCC, A22 to RD). Kestrel's 2026 actions were affirmations (A03, A04), and Orrin's A17 was a Rating Watch, not a downgrade.

**Q8.** E08. Its latest LTIDR is RD (A22, 2026-07-08), which is a default. E07's rating was withdrawn (A19), which says nothing about default.

**Q9.** 5. As of 2026-10-01 the entities with a current LTIDR are E01 (BBB), E02/E03 (A, one entity), E05 (BB FC, BBB- LC), E06 (A-, on Watch but still rated), and E08 (RD), which is five. E07 was withdrawn (A19), E04 has no issuer rating of its own, and VD holds only a Country Ceiling. This counts RD as a rating held.

**Q10.** Depends. The LC LTIDR is BBB- (A13, investment grade), but the headline FC LTIDR is BB (A14, speculative grade).

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 5},
  "Q10": {"investment_grade": "depends"}
}
```