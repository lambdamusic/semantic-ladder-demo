**Q1.** A-. The latest action before 1 Jan 2025 was A01 (2024-03-12, LTIDR A-); the downgrade A02 came later, in June 2025.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, and both are affirmations (BBB, F2). The outlook moved to negative, but the rating was not lowered.

**Q3.** No. I02 was cut to BB+ on 2025-06-20 (A07), which is below investment grade. The earlier BBB (A23) is superseded.

**Q4.** Positive. E03 shares its LEI with E02, so it appears to be a duplicate record of Northwind Holdings. A09 (2025-09-15) is the latest LTIDR action, with outlook POS; it supersedes the STA in A08.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02), the guarantor of I03, which is rated A. The guarantee is recorded in I03 (guarantor E02), and A09 affirmed E02 at A. The notes themselves are also rated A (A11).

**Q6.** The data does not state a reason. The pattern fits a sovereign ceiling: the Republic of Valdoria (VD) has a "CC" rating of BB (A12), which equals E05's foreign-currency rating of BB (A14). E05's local-currency rating is BBB- (A13). I am inferring that "CC" means country ceiling.

**Q7.** E08 (Saxby Shipping) was downgraded twice in 2026: to CCC (A21) and to RD (A22). E06's rating watch negative (A17) is not a downgrade.

**Q8.** E08. A22 (2026-07-08) put it at RD after a distressed debt exchange, and nothing later changes that. This treats RD as in default, which is a restricted default.

**Q9.** 5. The issuers with a current issuer rating are E01, E02 (E03 is the same entity), E05, E06 and E08. E07's rating was withdrawn (A19), E04 has no issuer rating, and VD's "CC" is a country-ceiling rating rather than an issuer rating. Counting E08 depends on treating RD as a rating.

**Q10.** Depends. Its local-currency rating is BBB-, which is investment grade (A13), but its foreign-currency rating is BB, which is not (A14). The notes I04 are rated BB (A15).

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