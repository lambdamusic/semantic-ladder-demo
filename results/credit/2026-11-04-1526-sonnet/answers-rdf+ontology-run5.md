**Q1.** A-. The latest action on or before 1 Jan 2025 for E01's long-term foreign-currency rating is A01 (assigned A- on 2024-03-12). The downgrade to BBB (A02) came later, on 2025-06-20.

**Q2.** No. E01's only 2026 actions are A03 (affirmed BBB, outlook moved to Negative) and A04 (affirmed short-term F2). Neither is a downgrade, and a Negative outlook is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02, a subordinated Kestrel note, and its latest action is A07 (downgraded to BB+ on 2025-06-20). BB+ is speculative grade.

**Q4.** Positive. E02 and E03 share the same LEI, so they are one entity. Its latest action is A09 (E03, affirmed A, outlook Positive, 2025-09-15), which supersedes the Stable outlook in A08.

**Q5.** Northwind Holdings, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes the guarantor's risk. E02 is the same entity as E03, whose latest rating is A (A09), and I03's own rating is A (A11).

**Q6.** Valdoria Telecom (E05) is rated BB on a foreign-currency basis (A14) and BBB- on a local-currency basis (A13). The Country Ceiling for Valdoria (VD, A12) is BB and caps foreign-currency ratings, but not local-currency ones.

**Q7.** E08. Its downgrades are A21 (to CCC, 2026-01-20) and A22 (to RD, 2026-07-08). E06's Rating Watch Negative (A17) is not a downgrade.

**Q8.** E08. A22 put it at RD on 2026-07-08, and RD is a default. E07's withdrawal (A19) is not a default.

**Q9.** 5. The issuers with an issuer rating on 1 Oct 2026 are E01, E02 (the same entity as E03), E05, E06 and E08 (currently RD). E07 was withdrawn (A19). E04 has no issuer rating. VD has only a Country Ceiling, which is not a rating of anyone.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (speculative grade, A14). The foreign-currency rating is the headline rating, so the answer depends on which basis is meant.

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