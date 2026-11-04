**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) and was not changed until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is the affirmation A03 (BBB, outlook revised to Negative), and the 2025 downgrades (A02, A06, A07) fall outside 2026.

**Q3.** No. I02, the 2031 note, was downgraded to BB+ in A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity, and its latest action is A09 (2025-09-15), which carries a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and its latest instrument rating is A (A11).

**Q6.** The data does not state a reason directly. E05's FC rating is BB (A14) and its LC rating is BBB- (A13), and the Valdoria Country Ceiling is BB (A12), which caps FC ratings but not LC ratings.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05 is an instrument, and E16 is QA test data, so both are ignored.

**Q8.** E08. Its latest rating is RD (A22, 2026-07-08), which counts as a default.

**Q9.** 12. The issuers holding an LTIDR are E01, E02 (same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. E05's LC rating is BBB- (investment grade), but its FC rating is BB (speculative grade).

**Q11.** BBB+. E14 was downgraded to BBB+ in A36 (2024-09-30), and the Watch (A35) did not come until 2025-11-20.

**Q12.** A-. E14 was assigned A- in A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade, as the Watch (A35) and the affirmation (A33) do not count.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in A26 (2023-05-01) and was downgraded only on 2026-04-15 (A27). E17 is the same entity by LEI and has no actions.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after the 2026 affirmation (A33).

**Q17.** No. E06's only 2026 action is the Rating Watch Negative in A17, which leaves the rating at A-.

**Q18.** E06 (A17, 2026-09-03). E14's earlier Watch (A35) was superseded by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). E06's latest action (A17) records no outlook.

**Q20.** No. E07 was withdrawn (A19, "commercial reasons"), and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08. It reached RD in A22.

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The instruments rated investment grade are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+. This is E15's LC rating from A40.

**Q27.** A-. I06 was assigned A- in A42.

**Q28.** BBB+. This is CV's FC LTIDR from A38; the A in A37 is the Country Ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating BB equals the VD ceiling BB, and E15's FC rating A equals the CV ceiling A (A37).

**Q31.** No. No company's FC rating is above its ceiling; E05 and E15 sit exactly at theirs.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose LTIDR is BBB+ (A27) and whose instrument rating is also BBB+ (A29).

**Q34.** No. Nothing in the data links E12 to E09, E10 or E11, and the similar name is not evidence.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. E17 duplicates E10 and E03 duplicates E02, and E16 is QA test data, which leaves 16.

**Q38.** No. They have different LEIs (E06 ORRN00BANK00000DE233, E13 ORBC00BANCORP000US45).

**Q39.** A. E02/E03 was affirmed at A in A09.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. E10 is the RATINGS record, which holds over E17's LU.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, and E10 is domiciled in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and its issuer E05 is domiciled in VD.

**Q45.** No. I07 is BBB- (A45) against a ceiling of BB, but local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated until an Assigned action confirms it.

**Q48.** 7: I01 to I07. I08 is unrated.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06"]},
"Q19": {"issuers": ["E01", "E09"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 5},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05", "E15"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```