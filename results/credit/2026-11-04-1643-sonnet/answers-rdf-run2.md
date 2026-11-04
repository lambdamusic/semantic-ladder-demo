**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01) and stayed there until the 2025-06-20 downgrade (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB with Negative outlook (A03, A04); the downgrade was in 2025 (A02).

**Q3.** No, it is BB+. I02 was BBB (A23), then downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E02 and E03 share the same LEI, so they are one entity, and the latest action is A09 (2026-09-15 affirmation, Positive outlook), after A08 (Stable).

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes the guarantor's risk. E02's rating is A (A08, A09).

**Q6.** The data gives no stated reason. E05's FC rating is BB (A14) against LC BBB- (A13), and Valdoria's country-ceiling (CC) record is BB (A12), which is consistent with a ceiling effect, but that is inference.

**Q7.** E08, E10 and E16. These are the issuer-level downgrades in 2026: A21 and A22 (E08), A27 (E10) and A44 (E16). I05's downgrade (A29) is an instrument rating, and E06's action (A17) is only a watch.

**Q8.** E08. It was rated RD from 2026-07-08 (A22) with no later action.

**Q9.** 13. These are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), VD has only a CC rating (A12), and E11 has only a CO-type rating (A46).

**Q10.** Depends. Its LC rating is BBB- (investment grade, A13) but its FC rating is BB (not, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the watch only came later (A35).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** none. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A-. E10 was A- from A26 until the downgrade on 2026-04-15 (A27). E17 is a duplicate record with the same LEI and has no ratings.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A33); only the watch status came and went (A35).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement at A- (A17). E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17, with no later resolution). E14's watch (A35) was resolved by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 has no default rating; its LTIDR was withdrawn for commercial reasons (A19).

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are sub-investment grade, and I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** none. VD has only a country-ceiling-type record (BB, A12), no issuer default rating.

**Q30.** E05 (FC BB = VD ceiling BB) and E15 (FC A = CV ceiling A). CV's own FC rating is BBB+, which is below its ceiling.

**Q31.** No. E05 and E15 are at their ceilings, not above, and no other country has a ceiling record.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. The data records no parent link from E12 to the Halden group, only a similar name.

**Q35.** 3 (E09, E10, E11). E17 is a duplicate of E10, and E12 has no link.

**Q36.** 2 (E02, which is also E03, and E04).

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs (E06 vs E13) and different countries.

**Q39.** A. This is the latest rating for E02/E03 (A09).

**Q40.** 6 (E01, E02, E09, E12, E14, E16). E07 is excluded because it was withdrawn, and E03 is the same entity as E02.

**Q41.** BB+. E16 was downgraded on 2026-06-01 (A44). Its source is "QA", which may mean a test record.

**Q42.** DE. E10 is recorded as DE; E17 shows LU but shares E10's LEI, so it is a conflicting duplicate.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE); if you count E17 separately the answer would be 1.

**Q44.** Yes, by inference. I07 is in XVD and issued by VD-domiciled E05, and its BBB- matches E05's LC rating. The data does not define XVD explicitly.

**Q45.** No. The ceiling (BB) limits foreign-currency ratings, and I07 is a local-currency instrument rated BBB- (A45).

**Q46.** No. E11 has only a CO-type rating of BBB (A46), not an LTIDR. Its notes (I05) are rated through the guarantor E10.

**Q47.** none. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7 (I01–I07). I08's rating had expired (A47).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10", "E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 13},
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
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```