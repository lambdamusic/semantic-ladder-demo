**Q1.** A-. E01's long-term issuer rating on 1 Jan 2025 was the A- assigned in A01 (2024-03-12). The downgrade to BBB (A02) only came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation of BBB on 2026-02-10 with the outlook set to Negative. The downgrade to BBB was A02, in 2025.

**Q3.** No. The 2031 note is I02, subordinated, and its latest rating is BB+ (A07, 2025-06-20), which is sub-investment grade. It was BBB before that (A23).

**Q4.** Positive. E02 and E03 share the same LEI, so they look like the same entity (Northwind Holdings). The latest action is A09 (E03, 2025-09-15), which affirmed A with a Positive outlook. That supersedes the Stable outlook in A08 (E02, 2023). This relies on treating the shared LEI as the same entity.

**Q5.** A holder takes the credit risk of E02 (Northwind Holdings), the guarantor of the notes (I03), which are rated A. The issuer is E04, a finance subsidiary with no rating of its own. I03's latest rating is A (A11), and E02/E03 are also rated A.

**Q6.** The data doesn't say. It shows E05's foreign-currency rating at BB (A14) and its local-currency rating at BBB- (A13), with no comment on the gap. The sovereign VD has a BB "CC" record (A12), but the data doesn't define that type, so I can't confirm it is the cause.

**Q7.** E08 only. It was downgraded to CCC (A21) and then to RD (A22) in 2026. E06 was only placed on Rating Watch (A17) and E07's rating was withdrawn (A19), neither of which is a downgrade.

**Q8.** E08. Its latest rating on 1 Oct 2026 was RD (A22, "distressed debt exchange completed"). RD indicates a restricted default. E07's withdrawal (A19) is not a default.

**Q9.** 5. As of 1 Oct 2026, E01, E02 (same entity as E03 by LEI), E05, E06 and E08 hold long-term issuer ratings (A03, A09, A13/A14, A17, A22). E07 is excluded because its rating was withdrawn (A19), and E04 has no rating of its own. I also excluded VD, because its record (A12) is a "CC" type that isn't clearly an issuer rating. Counting it would give 6.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13), but its foreign-currency rating is BB (not investment grade, A14).

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