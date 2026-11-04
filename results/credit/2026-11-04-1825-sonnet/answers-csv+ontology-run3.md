**Q1.** A-. A01 assigned A- on 2024-03-12, and the next E01 LTIDR action (A02) is not until 2025-06-20.

**Q2.** No. The only 2026 E01 action is A03, an affirmation (AF) with a NEG outlook, which is not a downgrade.

**Q3.** No, BB+. I02 is subordinated, and A07 (2025-06-20) downgraded it to BB+, which is speculative grade.

**Q4.** Positive (POS). E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action, with a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02), rated A. I03 is guaranteed by E02, and the latest E02/E03 LTIDR is A (A09).

**Q6.** The Country Ceiling for VD is BB (A12), and it caps foreign-currency ratings, so the FC LTIDR is BB (A14). The LC LTIDR is BBB- (A13) because local-currency ratings are not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 downgrades the instrument I05, not an issuer. A44 is on QA record E16 and is ignored.

**Q8.** E08. A22 (2026-07-08) set RD, which is a default, and nothing later changes it.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), E04 and E11 have no issuer rating (E11 has only a credit opinion, A46), and VD has only a ceiling.

**Q10.** No. The headline FC rating is BB (A14), which is speculative grade. The LC rating of BBB- (A13) is investment grade, but it is not the headline rating.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action (A35) is on 2025-11-20.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade (A36) came later.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.

**Q15.** A-. E17 is the same entity as E10, and the A27 downgrade did not happen until 2026-04-15, so A26's A- still held.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33). The Watch (A35) did not change it.

**Q17.** No. A17 is a Rating Watch (RW), which leaves the rating at A- and is not a downgrade.

**Q18.** E06. A17 put it on RWN on 2026-09-03. E14's RWN (A35) was cleared by the later affirmation A33, which carries no watch.

**Q19.** E01 and E09 (A03 and A25). E06's A17 and E08's later actions record no outlook, so I did not count them.

**Q20.** No. E07's rating was withdrawn (A19), which is a commercial withdrawal and not a credit event, and there is no default record.

**Q21.** E07. It was rated (A18) and then withdrawn (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The current LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. These are I01 (BBB), I03 (A, via guarantor E02), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 has only an Expected action (A47), so it is unrated.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not an issuer rating.

**Q29.** None. VD has only a Country Ceiling record (A12).

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB (A14 vs A12). E15's FC rating of A equals the CV ceiling of A (A41 vs A37).

**Q31.** No. No FC rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes Halden Bank's credit risk (E10), rated BBB+. I05 is guaranteed by E10, whose LTIDR is BBB+ after A27.

**Q34.** No. E12 has no parent, so it is not in E09's group.

**Q35.** 3. These are E09, E10 and E11. E17 duplicates E10.

**Q36.** 2. These are E02 and E04. E03 duplicates E02.

**Q37.** 16. There are 19 records, less 2 duplicates (E03 and E17) and the QA record E16.

**Q38.** No. Their LEIs differ (E06 and E13).

**Q39.** A (A09, via E03, the same entity as E02).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in DE per RATINGS.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, and RATINGS puts that entity in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. It is local-currency debt, so the ceiling does not apply. Its BBB- (A45) is above the BB ceiling, but that is not a breach.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating (EX), so I08 stays unrated.

**Q48.** 7. I01 to I07 are rated, and I08 is not.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
"Q10": {"investment_grade": "no"},
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