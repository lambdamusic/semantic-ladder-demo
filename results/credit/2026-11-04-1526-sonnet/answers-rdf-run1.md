**Q1.** A-. E01's long-term IDR was A- from A01 (2024-03-12, affirmed) and stayed there until the downgrade in A02 on 2025-06-20, so it was A- on 1 Jan 2025.

**Q2.** No. E01's only 2026 actions are the affirmations A03 (BBB, outlook Negative) and A04 (F2) on 2026-02-10. The downgrade to BBB was A02 in 2025.

**Q3.** No. The 2031 note (I02, subordinated, issued by E01) was downgraded to BB+ in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive. E02 and E03 share the same LEI, so I treat E03 ("NORTHWIND HLDGS") as a duplicate record of E02. The latest action is A09 (2025-09-15, affirmed A, outlook Positive), which supersedes the Stable outlook in A08.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. I03 is issued by E04, a finance subsidiary with no rating of its own, and guaranteed by E02. The note is rated A (A10, A11), which matches E02's rating in A08/A09.

**Q6.** The data does not state a reason. E05 is rated BBB- on a local-currency basis (A13) and BB on a foreign-currency basis (A14), and neither record has a comment. The sovereign VD has a "CC" type rating of BB (A12), which matches the FC rating. That suggests a country ceiling, but the data does not define that type, so it is only an inference.

**Q7.** E08. It was downgraded to CCC (A21, 2026-01-20) and then to RD (A22, 2026-07-08). E06's rating watch (A17) is not a downgrade, and E07's withdrawal (A19) is not one either.

**Q8.** E08. Its RD rating (A22, 2026-07-08) is the latest action and indicates a completed distressed debt exchange. E07's withdrawal (A19) is not a default.

**Q9.** 5. The issuers with a current issuer rating are E01, E02 (counted once with E03, same LEI), E05, E06 (A- on watch, A17) and E08 (RD). E07 is excluded because its rating was withdrawn (A19). VD's rating is of a different type (CC), which I did not count as an issuer rating, and E04 has no rating.

**Q10.** Depends. E05's local-currency rating is BBB- (A13), which is investment grade, but its foreign-currency rating is BB (A14), as is its bond I04 (A15), which is not.

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