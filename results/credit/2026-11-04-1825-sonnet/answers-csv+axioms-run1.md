**Q1.** A-. A01 assigned A- on 2024-03-12 and nothing changed until the downgrade A02 on 2025-06-20.

**Q2.** No. The only 2026 issuer actions for Kestrel (E01) are affirmations (A03, A04). Its downgrades (A02, A06, A07) were in 2025.

**Q3.** No, it is BB+. The 2031 note (I02) was assigned BBB (A23) and downgraded to BB+ (A07).

**Q4.** Positive. A09 was filed under E03, which shares Northwind Holdings' LEI, so it is the same entity as E02. It affirmed A with a POS outlook and supersedes A08.

**Q5.** E02, rated A. The note (I03) is guaranteed by E02, so the guarantor's risk applies. E02's current rating is A (A09).

**Q6.** The foreign-currency rating is capped by the Country Ceiling of BB (A12). The foreign-currency rating is BB (A14) and the local-currency rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is excluded because it is a QA test record. E06's A17 is a watch placement, not a downgrade.

**Q8.** E08. A22 put it at RD on 2026-07-08, and that rating is still in force.

**Q9.** 12. These are E01, E02 (same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. VD has only a ceiling (CC), E04 and E11 have no issuer ratings, E07's was withdrawn, and E16 is a test record.

**Q10.** Depends. The local-currency rating is BBB- (A13, investment grade) and the foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. A36 (2024-09-30) was in force until A35 on 2025-11-20.

**Q12.** A-. A34 (2023-01-15) was in force until A36.

**Q13.** 1. A36 is the only downgrade for E14. A35 is a watch placement and A33 is an affirmation.

**Q14.** None. Halden Foods' first rating is A30 on 2024-02-01.

**Q15.** A-. A26 was in force until the downgrade A27 on 2026-04-15. E17 is the same entity (same LEI) and has no actions of its own.

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is still BBB+ after A33. The watch (A35) did not change the rating.

**Q17.** No. A17 is a placement on Rating Watch with A- unchanged.

**Q18.** E06. A17 is still in force. Marlow's RWN (A35) was superseded by A33.

**Q19.** E01 and E09. Their latest actions, A03 and A25, carry Negative outlooks.

**Q20.** No. E07's rating was withdrawn (A19) and was never a default rating. The last rating was BB.

**Q21.** E07. Its rating was withdrawn (A19) and no longer applies. E16 is excluded as a test record.

**Q22.** E08. It reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. Valdoria (VD) has only a Country Ceiling (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB (A14) against a ceiling of BB (A12). E15's is A (A41) against a ceiling of A (A37).

**Q31.** No. E05 and E15 are at their ceilings, not above them, and no other country has a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. E10 guarantees I05, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate record of E10.

**Q36.** 2: E02 (E03 is a duplicate record) and E04.

**Q37.** 17. The data has 19 records, but E03 duplicates E02 and E17 duplicates E10, since each pair shares an LEI.

**Q38.** No. They have different LEIs and are separate entities.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is a test record.

**Q41.** None. E16 is a QA test record, so its actions are not ratings in force.

**Q42.** DE. E10's own RATINGS record says DE. The LU on E17 comes from the RESEARCH record, which defers to the RATINGS record.

**Q43.** 0. E17 resolves to DE, so no entity is domiciled in LU.

**Q44.** Yes. I07 is in XVD, which is the domestic currency of VD, E05's domicile.

**Q45.** No. The ceiling constrains foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 has only a credit opinion (A46).

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating in force.

**Q48.** 7. These are I01 to I07. I08 has only an expected rating.

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
"Q37": {"count": 17},
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