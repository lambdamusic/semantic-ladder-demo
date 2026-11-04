**Q1.** A-. E01's LTIDR was A- from A01 (2024-03-12) and was not cut to BBB until A02 (2025-06-20), so it was A- on 1 Jan 2025.

**Q2.** No. E01's only 2026 actions are affirmations (A03 BBB, A04 F2 on 2026-02-10). The outlook moved to Negative, but that is not a downgrade.

**Q3.** No. The 2031 note is I02 (subordinated), whose latest rating is BB+ (A07, 2025-06-20), which is below investment grade.

**Q4.** Positive. E02 and E03 share the same LEI, so I treated them as one entity. The latest action is A09 (2025-09-15), an affirmation at A with a Positive outlook; it supersedes A08's Stable.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04, which has no rating of its own, but E02 guarantees it. I03's A rating (A10, A11) matches E02's A.

**Q6.** The data doesn't say. E05 is rated BB in foreign currency (A14) and BBB- in local currency (A13), with no comment explaining the gap. The sovereign VD has a "CC" type rating of BB (A12), which may be a country ceiling, but the data doesn't define that type, so I can't confirm it.

**Q7.** E08. It was downgraded to CCC (A21, 2026-01-20) and then to RD (A22, 2026-07-08). No other issuer had a 2026 downgrade.

**Q8.** E08. Its RD rating (A22, 2026-07-08) was still in effect on 1 Oct 2026. E07's withdrawal (A19) is not a default.

**Q9.** 5. The issuers are E01, E02 (same entity as E03), E05, E06 (A17 is a Watch Negative, not a withdrawal) and E08 (RD). I excluded E07 (withdrawn, A19) and E04 (no rating of its own). I also excluded VD, whose only rating is the "CC" type (A12), which I don't read as an issuer rating; including it would make 6.

**Q10.** Depends. E05's local-currency rating is BBB- (A13, investment grade), but its foreign-currency rating is BB (A14, not investment grade).

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "Positive"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 5},
  "Q10": {"investment_grade": "depends"}
}
```