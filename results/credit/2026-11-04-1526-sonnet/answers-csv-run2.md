**Q1.** A-. A01 (2024-03-12) set E01's LTIDR at A-, and the next action, A02, is not until 2025-06-20.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, which are affirmations (AF) at BBB and F2. A03 moved the outlook to negative but did not change the rating.

**Q3.** No, it is BB+. I02 is rated BB+ after A07 (2025-06-20), which supersedes the earlier BBB in A23.

**Q4.** POS. E02 and E03 share the same LEI, so they are the same entity under two source systems. The latest action, A09 (2025-09-15), gives a positive outlook, replacing the STA in A08.

**Q5.** The risk is E02's (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02 (guarantor_id). E02's A rating comes from A08 and A09, and I03 itself is rated A (A10, A11).

**Q6.** The data does not state a reason. A12 gives the Republic of Valdoria (VD) a "CC" rating of BB, which is consistent with a sovereign country ceiling capping the foreign-currency rating at BB (A14). The local-currency rating is BBB- (A13).

**Q7.** E08 (Saxby Shipping). A21 (CCC) and A22 (RD) are downgrades in 2026. E06's A17 is a Rating Watch, not a downgrade, and E01's A03 is an affirmation.

**Q8.** E08. A22 (2026-07-08) rated it RD, and nothing later changes that. E07's rating was withdrawn (A19), which is not a default.

**Q9.** 5. The issuers with a current LTIDR are E01, E02/E03 (counted once because they share an LEI), E05, E06 and E08 (RD). E07's rating is withdrawn (A19). E04 has only an instrument rating. I did not count VD, because its "CC" rating (A12) appears to be a country ceiling rather than an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade, but the foreign-currency rating is BB (A14), which is not.

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