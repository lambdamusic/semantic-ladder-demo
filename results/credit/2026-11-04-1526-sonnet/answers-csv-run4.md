**Q1.** A-. The last action before 1 Jan 2025 was A01 (2024-03-12, assigned A-). The downgrade to BBB (A02) came only on 2025-06-20.

**Q2.** No. The only 2026 actions on Kestrel (E01) are A03 and A04, both affirmations (AF), with the LTIDR held at BBB. The outlook moved to negative, but that is not a downgrade.

**Q3.** No. The 2031 note (I02) was rated BBB (A23) and then downgraded to BB+ (A07), which is below investment grade.

**Q4.** Positive (POS). E03 shares E02's LEI (NWND00HOLDINGS00GB42), so I treat it as the same entity, a duplicate from the RESEARCH source. Its latest action, A09 (2025-09-15), affirmed A with a POS outlook, later than A08's STA.

**Q5.** The holder takes the credit risk of Northwind Holdings plc (E02), the guarantor of I03, which is rated A. The issuer, E04, has no rating of its own. I03's rating (A10, affirmed in A11) is A, in line with E02's A.

**Q6.** The data doesn't state a reason. The FC LTIDR of BB (A14) equals the sovereign's CC record for Valdoria (A12, BB), which may be a country ceiling, but the data doesn't say that is why. The LC rating of BBB- (A13) is above it.

**Q7.** Only Saxby Shipping (E08). It was downgraded to CCC (A21) and then to RD (A22). E06's action in 2026 (A17) is a rating watch, not a downgrade.

**Q8.** Only E08. A22 (2026-07-08) put it at RD after a distressed debt exchange, and there was no later action.

**Q9.** 5. As of 1 Oct 2026 the issuers holding an LTIDR are E01, E02 (counting E03 as the same entity), E05, E06 (A-, on watch but still rated) and E08 (RD). E07 was withdrawn (A19), E04 has no issuer rating, and the sovereign's CC record isn't an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade, but the foreign-currency rating is BB (A14), which is not. The data doesn't say which one governs.

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