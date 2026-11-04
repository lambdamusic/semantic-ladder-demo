**Q1.** A-. The latest E01 long-term foreign-currency action on or before 1 Jan 2025 is A01 (A-, 2024-03-12). The downgrade to BBB (A02) came in June 2025.

**Q2.** No. E01's only 2026 action is A03 (2026-02-10), an affirmation at BBB with the outlook revised to Negative, which is not a downgrade. The downgrades A02, A06 and A07 were all in 2025.

**Q3.** No. The 2031 note is I02, subordinated, and its latest rating is BB+ (A07, 2025-06-20), which is speculative grade.

**Q4.** Positive. E02 and E03 share the LEI NWND00HOLDINGS00GB42, so they are the same entity. The latest action is A09 (E03, 2025-09-15), an affirmation at A with a Positive outlook, which supersedes the Stable outlook in A08.

**Q5.** The holder takes the credit risk of Northwind Holdings (E02, the same entity as E03), rated A. I03 is issued by E04 but guaranteed by E02, so it carries the guarantor's risk. I03's own rating is A (A11), in line with E02/E03's A (A09).

**Q6.** The Country Ceiling for Valdoria (VD, A12) is BB, and it caps foreign-currency ratings. E05's FC rating is BB (A14) against BBB- on a local-currency basis (A13), and local-currency ratings are not capped.

**Q7.** E08. A21 (CCC, 2026-01-20) and A22 (RD, 2026-07-08) are both downgrades. E06's Rating Watch (A17) and E07's withdrawal (A19) are not downgrades.

**Q8.** E08. Its rating was RD from A22 (2026-07-08), and RD is a default. No other entity has an RD or D rating.

**Q9.** 5. The rated issuers are E01, E02 (the same entity as E03), E05, E06 and E08. E07 was withdrawn (A19), E04 has no rating of its own, and VD has only a Country Ceiling, which is not an issuer rating. I counted E08's RD as a rating because it sits on the long-term scale.

**Q10.** Depends. E05's foreign-currency rating is BB, which is speculative grade (A14), but its local-currency rating is BBB-, which is investment grade (A13). The FC rating is the headline one.

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