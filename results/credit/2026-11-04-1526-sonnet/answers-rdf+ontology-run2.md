**Q1.** A-. The latest LTIDR (FC) action for E01 on or before 2025-01-01 is A02's predecessor A01 (A-, 2024-03-12); the downgrade A02 came 2025-06-20.

**Q2.** No. E01's only 2026 action is the affirmation A03 (2026-02-10, BBB, outlook Negative) plus A04 (STIDR affirmed F2); neither is a downgrade.

**Q3.** No. I02 (subordinated, issuer E01) was downgraded to BB+ on 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. Northwind Holdings plc (E02) and NORTHWIND HLDGS (E03) share the LEI NWND00HOLDINGS00GB42, so they are one entity. The latest LTIDR action is A09 (E03, affirmed A, 2025-09-15, outlook POS), which supersedes A08's Stable.

**Q5.** Northwind Holdings (E02, same entity as E03), rated A. I03 is issued by E04 but guaranteed by E02 (lad:guarantor), and its latest rating is A09/A11 (A, affirmed 2025-09-15).

**Q6.** The data doesn't state why. E05 has an LC LTIDR of BBB- (A13) and an FC LTIDR of BB (A14), both assigned 2025-04-01. The Country Ceiling for VD is BB (A12), and FC ratings are generally capped at the ceiling, which is consistent with the gap, but no record states it as the cause.

**Q7.** E08 was the only issuer downgraded in 2026 (A21 to CCC on 2026-01-20 and A22 to RD on 2026-07-08). E01's 2026 actions are affirmations, E06's is a Rating Watch, and E07's is a withdrawal.

**Q8.** E08 was in default on 2026-10-01. Its latest action by then is A22 (RD, 2026-07-08), and RD counts as a default.

**Q9.** 4. As of 2026-10-01 the issuers with a current (non-withdrawn) LTIDR are E01 (BBB), E02/E03 (one entity, A), E05 (BB FC / BBB- LC), E06 (A-, on Watch), and E08 (RD). E07 was withdrawn (A19) and is excluded. That is E01, E02, E05, E06 and E08, so 5 distinct issuers, not 4. The count is 5. (VD holds only a Country Ceiling, not an issuer rating, and E04 has none.)

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (speculative grade, A14), so the answer depends on the currency basis. The FC rating is the headline rating, which is not investment grade.

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