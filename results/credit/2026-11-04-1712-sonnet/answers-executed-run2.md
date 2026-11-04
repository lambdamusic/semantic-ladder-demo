**Q1.** A-. E01's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. E01's only downgrade was on 2025-06-20 (A02). On 2026-02-10 only the outlook changed to NEG (A03, affirmed).

**Q3.** No. I02 is rated BB+ (A07 since 2025-06-20), which is below investment grade.

**Q4.** Positive (POS), per E02's A09 (affirmed 2025-09-15, still in force).

**Q5.** The credit risk is Northwind Holdings (E02), the guarantor of I03, rated A (A09). The instrument rating is also A (A11).

**Q6.** The data does not state a reason. It does show a Country Ceiling for VD of BB from 2025-04-01. E05's FC rating is BB (A14) and its LC rating is BBB- (A13), so the FC rating sits at the ceiling and the LC rating does not.

**Q7.** E08 and E10. E08 went to CCC (A21) and then RD (A22). E10 went to BBB+ (A27).

**Q8.** E08. Its RD rating (A22) was in force on 1 October 2026.

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07's rating was withdrawn (A19), and E04 and E11 have no issuer rating.

**Q10.** Depends. E05 is BB on foreign currency (A14, non-investment grade) and BBB- on local currency (A13, investment grade).

**Q11.** BBB+ (A36, 2024-09-30 to 2025-11-20).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade is A36. A35 is a Watch placement and A33 is an affirmation.

**Q14.** None. E12's first rating (A30) starts on 2024-02-01.

**Q15.** A- (A26, in force until 2026-04-15).

**Q16.** No. E14 was BBB+ on 1 January 2025 (A36) and is BBB+ now (A33). It went through a Watch period (A35) in between.

**Q17.** No. E06 was placed on Rating Watch Negative (A17) with the rating unchanged at A-.

**Q18.** E06 (A17). E14's Watch (A35) ended on 2026-05-01.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), and no default rating is recorded for it.

**Q21.** E07. Its rating was withdrawn (WD, A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating records, only a ceiling.

**Q30.** E05 and E15. E05 is BB (A14) against a VD ceiling of BB, and E15 is A (A41) against a CV ceiling of A.

**Q31.** No. Among the countries that have ceilings, E05 and E15 are at their ceilings, not above. No ceilings are given for other countries.

**Q32.** E09, Halden Group plc.

**Q33.** The credit risk is Halden Bank (E10), the guarantor of I05, rated BBB+ (A27). The instrument rating is also BBB+ (A29).

**Q34.** No. E12 has no parent, while E10's ultimate parent is E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 15. entities.csv has 15 rows, and the merged duplicates are already collapsed.

**Q38.** No. E06 and E13 have different entity IDs, LEIs and countries (DE and US), and neither is a merged duplicate of the other.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07's rating was withdrawn.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** DE.

**Q43.** 0. No entity is domiciled in LU.

**Q44.** Yes. I07 has local_currency = yes (XVD).

**Q45.** No. The note (BBB-, A45) is above the BB ceiling, but it is a local-currency obligation, and the ceiling is read here as applying to foreign-currency ratings. E05's LC rating is also BBB- (A13).

**Q46.** No. E11 has no ratings of its own. I05 is rated and E10 is the guarantor.

**Q47.** None. I08 has no rating records.

**Q48.** 7: I01 to I07. I08 is unrated.

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
"Q37": {"count": 15},
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