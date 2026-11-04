**Q1.** BBB. Kestrel's LTIDR (E01, FC) was A- from A01 (2024-03-12) and was downgraded to BBB by A02 on 2025-06-20, so on 2025-01-01 it was still A-. Correction: the rating on 2025-01-01 is A-, since the latest action on or before that date is A01.

**Q2.** No. The only 2026 actions on E01 are A03 and A04, both affirmations (AF). A03 only revised the outlook to NEG, which is not a downgrade.

**Q3.** No. I02 (subordinated, issuer E01) was rated BB+ by A07 on 2025-06-20, which is speculative grade. It is the latest action on I02.

**Q4.** POS. Northwind Holdings is one entity (E02 and E03 share an LEI). The latest LTIDR action is A09 (2025-09-15, on E03), which affirmed A with a POS outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is issued by the finance subsidiary E04 but guaranteed by E02. E02/E03's current LTIDR is A (A09), and I03 was affirmed at A (A11).

**Q6.** The data doesn't state a reason directly. It does show that E05's FC LTIDR is BB (A14) while its LC LTIDR is BBB- (A13), and that the Country Ceiling for VD is BB (A12). That is consistent with the FC rating being capped by the ceiling, which reflects transfer and convertibility risk, while the LC rating is not capped.

**Q7.** E08 only. A21 (2026-01-20, CCC) and A22 (2026-07-08, RD) are DG actions in 2026. E01 had only affirmations, and E06's A17 is a Rating Watch (RW), not a downgrade.

**Q8.** E08. Its latest LTIDR action, A22 (2026-07-08), set RD, which is a default, and nothing later changed it.

**Q9.** 4. As of 2026-10-01 the issuers with a current issuer rating are E01 (BBB), E02/E03 (A, same LEI, so one entity), E05 (BB/BBB-) and E06 (A- on Watch, A17 doesn't change it). E07 was withdrawn (A19), and E08 is at RD (A22). Counting E08 as holding an issuer rating would give 5, since RD is a rating on the scale. I counted it as holding one: RD is on the scale and it was not withdrawn. So the count is 5: E01, E02/E03, E05, E06, E08.

**Q10.** Depends. E05's FC LTIDR is BB (A14), which is speculative grade, while its LC LTIDR is BBB- (A13), which is investment grade. The headline rating is the FC one, so it is not investment grade on that basis.

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