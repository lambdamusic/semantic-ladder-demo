**Q1.** A-. The latest LTIDR (FC) action for E01 on or before 2025-01-01 is A01 (2024-03-12, A-). The downgrade A02 came later, on 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 (LTIDR affirmed at BBB, outlook moved to NEG) and A04 (STIDR affirmed at F2). An affirmation or a negative outlook is not a downgrade.

**Q3.** No. I02 is rated BB+ (A07, 2025-06-20, which supersedes A23's BBB), and BB+ is speculative grade.

**Q4.** Positive (POS). E02 and E03 share the same LEI, so they are one entity. The latest LTIDR action is A09 (2025-09-15, recorded on E03), which affirmed A with a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is guaranteed by E02 (issuer E04 is a finance subsidiary). E02's current LTIDR is A (A08, affirmed by A09), and I03 is also rated A (A11).

**Q6.** The Country Ceiling for Valdoria (VD) is BB (A12), and it caps foreign-currency ratings. E05's FC LTIDR is therefore BB (A14), while its LC LTIDR of BBB- (A13) is not capped.

**Q7.** Only E08. A21 (2026-01-20, to CCC) and A22 (2026-07-08, to RD) are both downgrades. E06's A17 is a Rating Watch, not a downgrade.

**Q8.** E08. Its rating has been RD since A22 (2026-07-08), and RD counts as a default. No other entity is rated RD or D.

**Q9.** 5. The issuers are E01, E02 (E03 is the same entity), E05, E06 and E08. E04 has no issuer rating, E07's was withdrawn (A19), and the sovereign VD has only a Country Ceiling.

**Q10.** No. Its headline FC rating is BB (A14, speculative grade). Only its LC rating, BBB- (A13), is investment grade, and that rating is not the headline.

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