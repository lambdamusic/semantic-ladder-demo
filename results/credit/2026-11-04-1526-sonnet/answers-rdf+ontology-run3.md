**Q1.** A-. Kestrel Energy (E01) was assigned A- LTIDR (FC) on 2024-03-12 (A01); the next action, a downgrade, came 2025-06-20 (A02), so A- held on 2025-01-01.

**Q2.** No. E01's only 2026 action is an affirmation at BBB with a negative outlook (A03, 2026-02-10), which is not a downgrade; the downgrade was in 2025 (A02).

**Q3.** No, BBB would be wrong: the 2031 note (I02) is subordinated, and its latest rating is BB+ (A07, 2025-06-20), which is speculative grade.

**Q4.** Stable... but wait, this needs care. Northwind Holdings is E02 (LEI NWND00HOLDINGS00GB42), which is the same entity as E03 (same LEI). E02's A08 gave a Stable outlook (2023-11-01), but E03's A09 (2025-09-15) is later and gives Positive. The current outlook is Positive.

**Q5.** Northwind Holdings (E02, same entity as E03), rated A. The notes (I03) are guaranteed by E02, so they carry its credit risk; the guarantor's LTIDR FC is A (A09, affirmed 2025-09-15), and the instrument itself is rated A (A11).

**Q6.** The data doesn't state a cause. It shows E05's FC LTIDR is BB (A14) versus LC BBB- (A13), both 2025-04-01. The Country Ceiling for Valdoria (VD) is BB (A12), and the definitions say FC ratings are generally capped at the ceiling while LC ratings are not, which is consistent with the cap explaining the gap.

**Q7.** E01 is not among them (A03 is an affirmation). The 2026 downgrades are on E08 (A21 to CCC, A22 to RD), so the issuer is E08. No instrument downgrades occurred in 2026.

**Q8.** E08 was in default (RD since A22, 2026-07-08, with no later action). No other entity is at RD or D. E07 was withdrawn (A19), which is not a default.

**Q9.** 5. As of 2026-10-01 the entities with an issuer rating (LTIDR/STIDR) are: E01 (A03/A04), E02/E03 (one entity, A09), E05 (A13/A14), E06 (A17, still A- on watch), and E08 (A22, RD). E07 is withdrawn (A19), and VD has only a Country Ceiling, not an issuer rating. E04 has none.

**Q10.** Depends. Its local-currency LTIDR is BBB- (A13, investment grade), but its foreign-currency LTIDR is BB (A14, speculative grade). The FC rating is the headline rating, which would make it not investment grade.

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