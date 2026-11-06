**Q1.** A-. E01's foreign-currency issuer rating on 1 Jan 2025 was A- (A01, valid 2024-03-12 to 2025-06-20).
**Q2.** No. The only 2026 action on E01 was an affirmation of BBB with a Negative outlook (A03).
**Q3.** No. The 2031 note (I02) has been rated BB+ since the June 2025 downgrade (A07), which is below investment grade.
**Q4.** Positive. E02's current rating is A with a POS outlook (A09).
**Q5.** The Northwind Finance 2030 notes (I03) carry the credit risk of the guarantor E02, and the note is rated A (A11).
**Q6.** The data doesn't state a reason. It shows a Country Ceiling for VD of BB from 2025-04-01. E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13), which is consistent with the ceiling capping the foreign-currency rating.
**Q7.** E08 and E10. E08 was downgraded in January and July 2026 (A21, A22) and E10 in April 2026 (A27).
**Q8.** E08. Its rating has been RD since 2026-07-08 (A22).
**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15, each with an issuer rating in force. E07 is excluded because its rating was withdrawn (A19). I counted the sovereign CV as an issuer; if sovereigns are excluded, the count is 11.
**Q10.** Depends. E05's foreign-currency rating is BB, which is not investment grade, but its local-currency rating is BBB-, which is (A14, A13).
**Q11.** BBB+ (A36).
**Q12.** A- (A34).
**Q13.** 1. The only downgrade of E14 is A36, on 2024-09-30.
**Q14.** None. E12's first rating began on 2024-02-01 (A30).
**Q15.** A- (A26).
**Q16.** No. E14 was BBB+ on 1 Jan 2025 and is BBB+ now. The watch period (A35) came and went without a rating change.
**Q17.** No. E06 was placed on Rating Watch Negative at an unchanged A- (A17).
**Q18.** E06 (A17). E14's watch ended on 2026-05-01.
**Q19.** E01 and E09 (A03, A25).
**Q20.** No. E07's rating was withdrawn (A19), which is not a default. The only default in the data is E08.
**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).
**Q22.** E08, which went to RD in July 2026 (A22).
**Q23.** F2 (A04).
**Q24.** Yes. E01's issuer rating is BBB (A03).
**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) were investment grade. I02 and I04 were not, and I08 has no rating.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38).
**Q29.** None. VD has no rating records.
**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB, and E15's A equals CV's ceiling of A.
**Q31.** No. E05 and E15 are exactly at their ceilings, not above them.
**Q32.** E09.
**Q33.** The Halden Leasing 2028 notes (I05) carry the credit risk of the guarantor E10, and the note is rated BBB+ (A29).
**Q34.** No. E12 has no parent and is not in E09's chain, which covers E10 and E11.
**Q35.** 3: E09, E10 and E11.
**Q36.** 2: E02 and E04.
**Q37.** 16. The entities table has 16 rows after duplicates were merged.
**Q38.** No. They have different LEIs and countries (E06 in DE, E13 in US) and are separate records.
**Q39.** A (A09).
**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.
**Q41.** None. Brindle Capital does not appear in the data.
**Q42.** LU (E10).
**Q43.** 1: E10.
**Q44.** Yes. I07 is flagged as a local-currency instrument and is denominated in XVD.
**Q45.** No. I07 is rated BBB- against a VD ceiling of BB. The ceiling applies to foreign-currency ratings, and I07 is local-currency.
**Q46.** No. E11 has no issuer rating; only its note I05 is rated.
**Q47.** None. I08 has no rating records.
**Q48.** 7. I01 to I07 each had a rating in force, and I08 had none.

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