**Q1.** A-. E01's long-term rating on 1 Jan 2025 was A- (A01, affirmed/assigned 2024-03-12). The downgrade to BBB (A02) came later, on 2025-06-20.

**Q2.** No. In 2026 E01 was only affirmed: A03 (BBB, outlook moved to Negative) and A04 (F2) are both AF actions on 2026-02-10. The only downgrade was in 2025 (A02).

**Q3.** No. The 2031 note is I02 (subordinated, issued by E01), and its latest rating is BB+ (A07, 2025-06-20), which is below investment grade.

**Q4.** Positive. E02 and E03 share the same LEI, so I treat them as one entity. The latest action is A09 (2025-09-15, affirmed A, Positive), which supersedes A08 (Stable). This relies on the LEI match, since the names differ slightly.

**Q5.** The guarantor, E02 (Northwind Holdings), rated A. I03 is issued by E04, which has no rating of its own in the data, but it is guaranteed by E02. I03's A rating (A10, A11) matches E02's A rating (A08, A09).

**Q6.** The data doesn't say. E05 is rated BBB- on a local-currency basis (A13) and BB on a foreign-currency basis (A14), both on 2025-04-01, and neither record has a comment explaining the gap. A sovereign-related cap is plausible, since E05 is in VD, but the data doesn't state that.

**Q7.** E08. It was downgraded to CCC (A21, 2026-01-20) and then to RD (A22, 2026-07-08). No other issuer has a 2026 downgrade.

**Q8.** E08. It was rated RD from 2026-07-08 (A22, distressed debt exchange) with no later action, so it was in default on 1 Oct 2026.

**Q9.** 5: E01, E02 (same entity as E03), E05, E06 and E08.
- E07 is excluded because its rating was withdrawn (A19).
- E04 has no rating of its own.
- VD is excluded because its only rating is type CC (A12), which I read as a country ceiling rather than an issuer rating. The data doesn't define CC, so if it is an issuer rating the count would be 6.

**Q10.** Depends. E05's local-currency rating is BBB- (A13), which is investment grade. Its foreign-currency rating is BB (A14), and its 2029 note I04 is rated BB (A15); both are below investment grade.

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