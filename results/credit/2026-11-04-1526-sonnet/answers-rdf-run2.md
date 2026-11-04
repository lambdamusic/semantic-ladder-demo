**Q1.** A-. On 1 Jan 2025 Kestrel Energy (E01) held its long-term IDR (foreign-currency basis) at A- from A01 (2024-03-12). The downgrade to BBB came later, on 2025-06-20 (A02).

**Q2.** No. E01's only 2026 actions are A03 and A04 (2026-02-10), which affirm BBB and F2. A03 does move the outlook to Negative, but that is not a downgrade.

**Q3.** No. The 2031 note (I02) is subordinated, was rated BBB in A23, and was cut to BB+ on 2025-06-20 (A07). BB+ is below investment grade.

**Q4.** Positive. E02 and E03 are the same entity: they share LEI NWND00HOLDINGS00GB42, and E03 is the duplicate "NORTHWIND HLDGS" record. The latest action is A09 (2025-09-15), an affirmation at A with a Positive outlook, which is more recent than A08.

**Q5.** The guarantor, Northwind Holdings (E02), rated A. The notes (I03) are issued by E04, which has no rating of its own, but E02 guarantees them. I03 is rated A (A10, affirmed in A11), and E02's own IDR is also A (A08, A09).

**Q6.** The data cannot settle this. E05 is rated BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13), but no record gives a reason. Neither action has a comment.

**Q7.** E08. It was downgraded to CCC (A21, 2026-01-20) and then to RD (A22, 2026-07-08). The other 2026 actions are affirmations (A03, A04), a Rating Watch (A17) and a withdrawal (A19), none of which is a downgrade.

**Q8.** E08. Its RD rating (A22, 2026-07-08) has no later action, so it was still in default on 1 Oct 2026.

**Q9.** 5. The issuers are E01, E02 (the same entity as E03), E05, E06 and E08. E07 is excluded because its rating was withdrawn (A19). VD is excluded because its rating is of type CC (A12), which I read as a country ceiling rather than an issuer rating, though the data does not define it. This count would be 6 if VD were included.

**Q10.** Depends. E05 is investment grade on a local-currency basis (BBB-, A13) but not on a foreign-currency basis (BB, A14). Its 2029 note (I04) is also BB (A15).

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