**Q1.** A-. The 2025-06-20 downgrade (A02) came after 1 January 2025, so the rating still stood at A- from A01.

**Q2.** No. The only 2026 action on Kestrel's issuer rating (A03) affirmed BBB. It moved the outlook to negative, which is not a downgrade.

**Q3.** No, BB+. The 2031 note is I02, and its latest action (A07, 2025-06-20) downgraded it to BB+, below investment grade.

**Q4.** Positive (POS). E03 shares E02's LEI, so it appears to be a duplicate record of Northwind Holdings. Its latest action (A09, 2025-09-15) affirmed A with a positive outlook, superseding the stable outlook in A08.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by E04 but guaranteed by E02, and both I03 (A11) and E02 (A09, via the duplicate E03) were affirmed at A.

**Q6.** The data does not state a reason, since A13 and A14 carry no comment. The foreign-currency rating (A14, BB) equals the sovereign's country ceiling (A12, BB), which is consistent with a cap, but this is an inference rather than something the data says.

**Q7.** E08 (Saxby Shipping). It was downgraded to CCC (A21) and then to RD (A22) in 2026. E06's rating watch negative (A17) is not a downgrade.

**Q8.** E08. Its latest rating on 1 October 2026 was RD (A22), following a distressed debt exchange.

**Q9.** 5. The issuers are E01, E02 (counted once with its duplicate E03), E05, E06 and E08. E07's rating was withdrawn (A19). E04 has only instrument-level ratings, and VD's "CC" rating (A12) is a country ceiling rather than an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (A13), which is investment grade. The foreign-currency rating is BB (A14), which is not.

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