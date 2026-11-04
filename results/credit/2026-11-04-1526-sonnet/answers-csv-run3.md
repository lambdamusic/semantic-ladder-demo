**Q1.** A-. The LTIDR was A- from A01 (2024-03-12) until the downgrade in A02 on 2025-06-20, so it was A- on 2025-01-01.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, which are affirmations (AF) of BBB/F2. The outlook moved to negative, but the rating did not change.

**Q3.** No, it is BB+. I02 is rated BB+ after the downgrade in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive (POS). E03 shares E02's LEI, so it is a duplicate record of the same entity, and A09 (2025-09-15) is the latest action with POS. It supersedes the STA in A08.

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, rated A. I03 is issued by the finance subsidiary E04 but guaranteed by E02 (guarantor_id), and I03 is rated A (A10, affirmed in A11).

**Q6.** The data doesn't state a reason. E05's foreign-currency LTIDR is BB (A14) and its local-currency rating is BBB- (A13). The FC rating equals the Republic of Valdoria's BB "CC" record (A12), which is consistent with a country ceiling. No comment confirms that, and I can't verify what CC means.

**Q7.** E08. A21 (CCC) and A22 (RD) are both downgrades in 2026. E06's A17 is a Rating Watch Negative, not a downgrade, and E01's actions are affirmations.

**Q8.** E08. A22 put it at RD on 2026-07-08, with no later action by 1 October 2026.

**Q9.** 5. The issuers are E01, E02 (with E03 as the same LEI), E05, E06 and E08. E07's rating was withdrawn (A19), E04 has no issuer rating, and VD's CC record is not an issuer rating.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14). The answer depends on which currency basis is meant.

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