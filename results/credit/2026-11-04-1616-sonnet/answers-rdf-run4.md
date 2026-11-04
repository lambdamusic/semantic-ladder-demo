**Q1.** A-. E01's last action before 1 Jan 2025 was A01 (AS A-, 2024-03-12); the next change, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook. The downgrade (A02) was in 2025.

**Q3.** No. The 2031 note is I02, rated BB+ after A07 (2025-06-20), which is below BBB-.

**Q4.** Positive. E02 and E03 share the same LEI, so they are one entity recorded twice. The latest action is A09 (E03, 2025-09-15), which gives Positive; E02's A08 is older and Stable.

**Q5.** The guarantor, E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02 (A08/A09), so the holder takes E02's credit risk. I03 itself is rated A (A11).

**Q6.** The data does not state a reason. It shows E05's local-currency rating at BBB- (A13) and foreign-currency at BB (A14). The Valdoria country ceiling is BB (A12), which is consistent with a ceiling effect, but that is inference.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. I05's downgrade (A29) is an instrument rating, not an issuer.

**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.

**Q9.** 12. These are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is excluded because it was withdrawn (A19). VD has only a country-ceiling record (A12), not an issuer rating.

**Q10.** Depends. E05 is BBB- in local currency (A13, investment grade) but BB in foreign currency (A14, not investment grade).

**Q11.** BBB+. A36 downgraded E14 on 2024-09-30; the next action, A35, is 2025-11-20.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36. The other E14 actions are an assignment, a watch and an affirmation.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-, from A26. The downgrade, A27, is dated 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+. A35 only added a Rating Watch Negative and A33 affirmed the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative placed on A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17). E14's earlier watch (A35) was superseded by the affirmation with a Stable outlook in A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's last action, A19, is a withdrawal "for commercial reasons", not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's long-term issuer rating is BBB (A03).

**Q25.** 4. I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) are investment grade. I02 (BB+) and I04 (BB) are not.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The local-currency rating is A- (A39) and the country-ceiling record is A (A37).

**Q29.** None. VD has only a country-ceiling record of BB (A12) and no issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB (A14) equals the VD ceiling (A12). E15's foreign-currency rating of A (A41) equals the CV ceiling (A37).

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no company is above one.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** E10 (the guarantor), rated BBB+. E10 was downgraded to BBB+ in A27, and I05 itself is BBB+ (A29).

**Q34.** No. The data shows no ownership link from E12 to the E09/E10/E11 chain, only a similar name.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (=E03) and E04.

**Q37.** 16. There are 17 entity records, but E03 duplicates E02 by LEI. Instruments are not counted.

**Q38.** No. E06 and E13 have different LEIs and countries (DE vs US).

**Q39.** A (A08 and A09).

**Q40.** 5: E01, E02 (=E03), E09, E12 and E14. E07 (GB) is excluded because its rating was withdrawn.

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
"Q25": {"count": 4},
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
"Q40": {"count": 5}
}
```