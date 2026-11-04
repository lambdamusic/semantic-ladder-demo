**Q1.** A-. The latest Kestrel Energy (E01) LTIDR FC action on or before 1 Jan 2025 is A01 (A-, 2024-03-12). The downgrade to BBB (A02) came later, on 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 and A04, which are affirmations (AF). A03 changed the outlook to negative, but that is not a downgrade.

**Q3.** No. The 2031 note is I02 (subordinated), and its latest rating is BB+ (A07, 2025-06-20), which is speculative grade. The earlier BBB (A23) was superseded.

**Q4.** Positive (POS). E03 shares its LEI with E02, so they are the same entity, and the latest LTIDR action is A09 (2025-09-15, POS) on E03. It overrides the stable outlook in A08.

**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is guaranteed by E02 (the issuer E04 is a finance subsidiary). E02's LTIDR is A (A08, affirmed in A09 under E03), and I03 is also A (A11).

**Q6.** The Country Ceiling for Valdoria (VD, A12) is BB. It caps foreign-currency ratings, so E05's FC rating is BB (A14), while its LC rating is BBB- (A13) because local-currency ratings are not capped.

**Q7.** E08 (Saxby Shipping). Downgrades (DG) in 2026 are A21 (CCC) and A22 (RD), both on E08. E06's A17 is a Rating Watch, not a downgrade.

**Q8.** E08. A22 (2026-07-08) set its rating to RD, which is a default, and nothing later changes that.

**Q9.** 5. As of 1 Oct 2026 the issuers holding an issuer rating are:
- E01 (BBB)
- E02/E03 (A, one entity)
- E05 (BB FC and BBB- LC)
- E06 (A-, on Watch only)
- E08 (RD)

Excluded:
- E04 has no rating of its own.
- E07's rating was withdrawn (A19).
- VD has only a Country Ceiling.

**Q10.** No. The headline FC LTIDR is BB (A14), which is speculative grade. Only its LC rating (BBB-, A13) is investment grade.

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
  "Q10": {"investment_grade": "no"}
}
```