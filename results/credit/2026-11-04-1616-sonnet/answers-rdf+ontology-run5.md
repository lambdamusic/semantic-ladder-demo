**Q1.** A-. A05-style history for E01: A01 assigned A- (2024-03-12), and the downgrade A02 only came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03/A04, which are affirmations (the outlook went to Negative, which is not a downgrade).

**Q3.** No. The 2031 note is I02, subordinated, and has been BB+ since A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E03 and E02 share one LEI, so they are the same entity. The latest action is A09 (E03, 2025-09-15), which has a Positive outlook and supersedes A08.

**Q5.** The holder takes E02's credit risk (E02 is the same entity as E03), rated A. I03 is guaranteed by E02 (guarantor, not the issuer E04), and I03's rating is A (A10, A11).

**Q6.** The data doesn't state a reason, but it is consistent with the Country Ceiling. E05 is domiciled in VD, whose ceiling is BB (A12). E05's FC rating is BB (A14), while its LC rating is BBB- (A13) and is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 downgrades the instrument I05, not its issuer.

**Q8.** E08. A22 put it at RD (a default) on 2026-07-08, and nothing came after.

**Q9.** 12. These are E01, E02 (= E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is excluded because it was withdrawn (A19), and VD has only a Country Ceiling (A12).

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (speculative, A14).

**Q11.** BBB+. The downgrade A36 (2024-09-30) was in force, and the RW in A35 came later (2025-11-20).

**Q12.** A-. Assigned in A34 (2023-01-15) and not changed until A36.

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch and A33 is an affirmation.

**Q14.** No rating. E12's first action is A30 (2024-02-01), which is after that date.

**Q15.** A-. E10 was assigned A- (A26) and was not downgraded until A27 (2026-04-15).

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A35, A33). Only a Watch and an affirmation have occurred since.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch, which leaves the rating unchanged. Orrin Bancorp (E13) is a different entity, with a different LEI.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's earlier Watch (A35) was superseded by A33.

**Q19.** E01 and E09. A03 and A25 are their latest actions and both carry a Negative outlook. E06's latest action (A17) records no outlook, so it isn't counted.

**Q20.** No. E07's last action is a withdrawal (A19), which is not a default.

**Q21.** E07. It was rated BB (A18) and withdrawn on 2026-05-12 (A19).

**Q22.** E08. A22 gives it RD, a default; no other record has RD or D.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 4. On 2026-10-01, I01 is BBB, I03 is A, I05 is BBB+ and I06 is A-. I02 (BB+) and I04 (BB) are speculative.

**Q26.** A+ (A40). The LC basis is not capped; the FC rating is A (A41).

**Q27.** A- (A42). I06 is subordinated.

**Q28.** BBB+ (A38). A37 is the Country Ceiling (A), which is not the sovereign's rating, and A39 is the LC rating (A-).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB (A14, A12). E15's FC rating is A, equal to CV's ceiling of A (A41, A37).

**Q31.** No. E05 (BB) and E15 (A) are at their ceilings, not above. No other country has a ceiling in the data.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10 (not the issuer E11), and E10 was downgraded to BBB+ (A27). I05 itself is BBB+ (A29).

**Q34.** No, going by the data. E12 has no parent link or ownership tie to the E09/E10 group, and a similar name is not evidence of one.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (= E03, same LEI) and its subsidiary E04.

**Q37.** 16. There are 17 entity records, but E02 and E03 share an LEI.

**Q38.** No. Orrin Bank AG (E06, LEI ORRN00BANK00000DE233) and Orrin Bancorp Inc (E13, LEI ORBC00BANCORP000US45) have different LEIs.

**Q39.** A, from A09 (E03, same entity as E02).

**Q40.** 5: E01, E02 (= E03), E09, E12 and E14 (all GB). E07 is GB but was withdrawn.

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
"Q14": {"rating": "NR"},
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
"Q25": {"count": 4},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "NR"},
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
"Q40": {"count": 5}
}
```

Q6 is not in the JSON field list, so it is answered in prose only.