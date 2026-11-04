**Q1.** BBB+? No: **A-**. On 2025-01-01 the latest LTIDR (FC) action on E01 was A01 (A-, 2024-03-12); the downgrade to BBB (A02) came on 2025-06-20.

**Q2.** **No.** E01's only 2026 action is A03/A04 (affirmations on 2026-02-10), and the 2026 downgrade in the data (A22) concerns E08, not E01; the negative outlook in A03 is not a downgrade.

**Q3.** **No**, the rating is BB+. I02 (the 6.25% 2031 subordinated note, issuer E01) was downgraded to BB+ in A07 (2025-06-20), which is speculative grade.

**Q4.** **Positive.** E03 (NORTHWIND HLDGS, A09) shares its LEI with E02 (Northwind Holdings plc), so they are the same entity. The latest LTIDR action is A09 (2025-09-15, outlook POS), later than A08 (STA).

**Q5.** The holder takes **E02**'s credit risk, rated **A**. I03 is issued by E04 but guaranteed by E02, so it is rated on the guarantor (I03's rating is A, A11), in line with E02/E03's LTIDR of A (A09).

**Q6.** The data doesn't state a reason explicitly. E05 (domiciled in VD) has FC BB (A14) versus LC BBB- (A13), and VD's Country Ceiling is BB (A12). The ceiling caps FC ratings but not LC ratings, which is consistent with the gap.

**Q7.** **E08** (and no others). In 2026 the only downgrades are A21 and A22, both on E08. A22 is the move to RD. Instrument downgrades in 2025 (I01, I02) are outside 2026.

**Q8.** **E08.** A22 (RD, 2026-07-08) is the latest LTIDR action on E08 before 2026-10-01 and RD is a default. E07's withdrawal (A19) says nothing about default.

**Q9.** **6.** Holders of a current issuer rating (LTIDR/STIDR) on 2026-10-01 are E01 (A03/A04), E02/E03 (same LEI, A08/A09), E05 (A13/A14), E06 (A17, a Watch leaves the rating A-), and E08 (RD, A22). E07 was withdrawn (A19), VD has only a Country Ceiling, and E04 has no issuer rating.

**Q10.** **Depends.** E05's local-currency LTIDR is BBB- (A13, investment grade), but its foreign-currency LTIDR is BB (A14, speculative grade), and the FC rating is the headline rating.

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

Correction to Q9: my count above is inconsistent. The list gives E01, E02/E03 (one entity), E05, E06 and E08, which is **5** distinct issuers, as in the JSON, not 6.