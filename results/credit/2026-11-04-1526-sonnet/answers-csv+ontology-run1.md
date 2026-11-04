**Q1.** A-. The latest Kestrel LTIDR (FC) action on or before 1 Jan 2025 is A01 (A-); the downgrade A02 came later, on 2025-06-20.

**Q2.** No. The only 2026 Kestrel actions are A03 and A04, both affirmations. A03 changed the outlook to negative, which is not a downgrade.

**Q3.** No. The 2031 note I02 is subordinated, and its latest rating is BB+ (A07, 2025-06-20), which is speculative grade.

**Q4.** Positive. E03 shares its LEI with E02, so they are the same entity. The latest action on that entity is A09 (2025-09-15), an affirmation at A with a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is issued by the finance subsidiary E04 but guaranteed by E02. E02's latest LTIDR is A (A09, recorded under E03).

**Q6.** Not in the JSON. Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings. So the FC rating is BB (A14), while the uncapped LC rating is BBB- (A13).

**Q7.** E08 (Saxby Shipping). It was downgraded to CCC (A21) and then to RD (A22) in 2026. Kestrel's A03 was an affirmation, and Orrin's A17 was only a Rating Watch (RW), not a downgrade.

**Q8.** E08. Its latest rating on 1 Oct 2026 is RD (A22), which is a default. E07's withdrawal (A19) is not a credit event.

**Q9.** 5. The issuers holding an LTIDR or STIDR on 1 Oct 2026 are E01, E02/E03 (one entity), E05, E06 and E08. E08's RD is still a rating. E07 was withdrawn (A19), E04 has no rating of its own, and VD has only a Country Ceiling.

**Q10.** It depends on the currency basis. Its LC rating is BBB- (A13), which is investment grade. Its FC rating, the headline one, is BB (A14), which is speculative grade.

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