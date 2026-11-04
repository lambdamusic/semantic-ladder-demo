**Q1.** A-. E01's LTIDR (foreign currency) was assigned at A- on 2024-03-12 (A01) and not changed until 2025-06-20 (A02).

**Q2.** No. The only 2026 E01 actions are affirmations (A03, A04); the downgrade was in 2025 (A02).

**Q3.** No. The 2031 note is I02, rated BB+ after the 2025-06-20 downgrade (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 share the LEI NWND00HOLDINGS00GB42, so I treated them as one entity. The latest action is A09 (E03, affirmed A, Positive, 2025-09-15), which supersedes A08's Stable.

**Q5.** The guarantor, E02 (same entity as E03), rated A. I03's issuer is E04 but E02 guarantees it (A09, A08).

**Q6.** The data doesn't state a reason. E05 has an LC rating of BBB- (A13) and an FC rating of BB (A14), and VD's Country Ceiling is BB (A12). The ceiling is consistent with the FC rating, but that is inference.

**Q7.** E08, E10, E16. Their issuer-level downgrades in 2026 are A21/A22, A27 and A44. I05's downgrade (A29) is an instrument rating, so I didn't count its issuer E11.

**Q8.** E08. It was rated RD on 2026-07-08 (A22), with no later action.

**Q9.** 13. They are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19), VD has only a country ceiling, and E11's "CO" rating type isn't defined as an issuer rating.

**Q10.** Depends. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), before the 2025-11-20 watch (A35).

**Q12.** A-, from A34 (2023-01-15).

**Q13.** Once (A36).

**Q14.** None. E12's first rating is dated 2024-02-01 (A30).

**Q15.** A-. E10's A- (A26) stood until the 2026-04-15 downgrade (A27). E17 "HALDEN BANK" has the same LEI as E10 and no ratings of its own.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). Only the watch status changed (A35).

**Q17.** No. E06's only 2026 action is a Rating Watch Negative at A- (A17), which is not a downgrade. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17, no later action). E14's watch (A35) was followed by an affirmation with a Stable outlook (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and there is no default rating.

**Q21.** E07 (withdrawn, A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. They are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 was expired on 2026-09-01 (A47), and I02 and I04 are sub-investment grade.

**Q26.** A+ (A40).

**Q27.** A- (A42, subordinated note I06).

**Q28.** BBB+ (A38). A37 is the ceiling (A) and A39 is the LC rating (A-).

**Q29.** None. VD only has a Country Ceiling of BB (A12), which is not an issuer rating.

**Q30.** E05 (FC BB = VD ceiling BB) and E15 (FC A = CV ceiling A).

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. E10 guarantees I05 (issuer E11), and its latest rating is A27.

**Q34.** No, going by the data. E12 has no parent or group link, and the shared "Halden" name is not evidence.

**Q35.** 3 (E09, E10, E11). E17 duplicates E10 by LEI.

**Q36.** 2 (E02/E03 and E04).

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10, both by LEI.

**Q38.** No. They have different LEIs and names (E06 vs E13).

**Q39.** A (A09 and A08).

**Q40.** 5. They are E01, E02 (=E03), E09, E12 and E14. E07 is excluded because it was withdrawn.

**Q41.** BB+ (A44). The record's source system is "QA".

**Q42.** DE (E10). E17 says LU, but it shares E10's LEI, which ends "DE62", and E10 comes from the RATINGS source.

**Q43.** 0. The only LU record is E17, which is a duplicate of E10 (DE) by LEI. If E17 were counted separately the answer would be 1.

**Q44.** Yes, by inference. I07 is in XVD, and its BBB- rating matches E05's LC rating (A13). The data doesn't state that XVD is Valdoria's currency.

**Q45.** No. The BB ceiling (A12) applies to foreign-currency ratings, and I07 is a local-currency obligation.

**Q46.** No. E11 only has a "CO" rating (A46), which is not an LTIDR/STIDR issuer rating.

**Q47.** None. I08's A rating expired on 2026-09-01 (A47).

**Q48.** 7 (I01–I07). I08 had expired.

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
"Q40": {"count": 5},
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