**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action, A02, came on 2025-06-20.

**Q2.** No. The only 2026 action on Kestrel is A03, an affirmation at BBB.

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) affirmed A with a POS outlook, superseding A08.

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and the current rating is A (A09/A08).

**Q6.** The data gives no stated reason; the comments are empty. It is consistent with the Country Ceiling: VD's CC is BB (A12), and the FC rating is BB (A14) against BBB- for LC (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is excluded because it is a QA test record, and A29 is an instrument rating.

**Q8.** E08. A22 (RD) is its rating in force, and no other in-force rating is RD or D.

**Q9.** 12. These are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, VD has only a ceiling, E11 only a credit opinion, and E16 is a test record.

**Q10.** Depends. LC is BBB- (investment grade, A13) but FC is BB (not, A14).

**Q11.** BBB+. A36 (2024-09-30) was the rating in force, and A35 only came on 2025-11-20.

**Q12.** A-. A34 (2023-01-15) was in force until A36.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 was in force until A27 on 2026-04-15, and E17 has no actions of its own.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33); only the watch and affirmation actions occurred.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch placement with the rating unchanged at A-.

**Q18.** E06 (A17). E14's earlier RWN (A35) was superseded by A33.

**Q19.** E01 and E09 (A03, A25). A17 carries no outlook.

**Q20.** No. E07's last action is a withdrawal (A19), not a default rating.

**Q21.** E07. Its rating was withdrawn in A19. E02 still has a rating through its twin E03.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes, BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 is BB+, I04 is BB, and I08 only has an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB, and E15's FC rating of A equals the CV ceiling of A.

**Q31.** No. E05 is at its ceiling and E15 is at its ceiling, not above it.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, and A27 is its current rating.

**Q34.** No. E12 has no parent link to the Halden group, and only the name is similar.

**Q35.** 3. These are E09, E10 (the same entity as E17) and E11.

**Q36.** 2. These are E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records, E02/E03 and E10/E17 are duplicates by LEI, and E16 is a test record.

**Q38.** No. They have different LEIs and no parent link.

**Q39.** A (A09 on the same entity, superseding A08).

**Q40.** 5. These are E01, E02/E03, E09, E12 and E14. E10 is domiciled in LU, per the RESEARCH record, and E07 was withdrawn.

**Q41.** None. E16 is a QA test record, so its actions are not ratings in force.

**Q42.** LU. The RESEARCH record E17 for the same LEI gives LU and overrides the RATINGS record's DE.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, VD's domestic currency, and E05 is domiciled in VD.

**Q45.** No. The ceiling caps foreign-currency issuer ratings, and I07 is a local-currency instrument rated BBB-. I07's BBB- exceeds the BB ceiling numerically, but the ceiling does not apply to it.

**Q46.** No. E11 has only a credit opinion (A46), not an issuer rating.

**Q47.** None. A47 is only an expected rating, which is not in force.

**Q48.** 7. These are I01 to I07; I08 has only an expected rating.

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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```