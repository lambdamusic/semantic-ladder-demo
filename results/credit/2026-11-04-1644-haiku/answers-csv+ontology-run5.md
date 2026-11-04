**Q1.** A-
Latest LTIDR FC action on or before 2025-01-01 is A01 (AS, A-), since A02 (DG to BBB) came later.

**Q2.** No
The 2026 actions on E01 are affirmations (A03, A04), not downgrades.

**Q3.** No, BB+
I02 (subordinated) was downgraded to BB+ by A07 (2025-06-20), which is speculative grade.

**Q4.** POS
E02 and E03 share an LEI, so they are one entity; the latest action is A09 (AF, outlook POS, 2025-09-15).

**Q5.** Northwind Holdings (E02), rated A
I03 is guaranteed by E02, so holders take E02's risk, and the instrument rating is A (A11).

**Q6.** The FC rating is capped by Valdoria's Country Ceiling, while the LC rating is not.
E05's FC rating is BB (A14), equal to the VD ceiling of BB (A12); its LC rating of BBB- (A13) is not subject to the ceiling per lad:type-CC.

**Q7.** E08 and E10
E08 was downgraded to CCC (A21) and then RD (A22); E10 was downgraded to BBB+ (A27). I05 was also downgraded, but it is an instrument, not an issuer.

**Q8.** E08
A22 (RD, 2026-07-08) is a default that took effect before 1 October 2026.

**Q9.** 12
E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15 hold LTIDR ratings. VD holds only a Country Ceiling, E11 only a CO, and E07 was withdrawn, so none of them count.

**Q10.** No
Its headline FC rating is BB (A14), while its LC rating is BBB- (A13), which is investment grade but is the secondary rating.

**Q11.** BBB+
A36 (DG to BBB+, 2024-09-30) is the latest action on or before 2025-06-01; A35 (RW) does not change the rating.

**Q12.** A-
The only action before 2024-01-01 is A34 (AS, A-, 2023-01-15).

**Q13.** 1
Only A36 is a downgrade; A35 is a Rating Watch and A33 an affirmation.

**Q14.** None
E12's first rating is A30 (AS, BB-), dated 2024-02-01, which is after 1 January 2024.

**Q15.** A-
E10 and E17 share an LEI, so they are one entity; the 2026 downgrade (A27) came after 1 January 2026, so the rating then was A- from A26.

**Q16.** No
The rating was BBB+ on 2025-01-01 (A36), and later actions (A35, A33) left it at BBB+.

**Q17.** No
A17 (2026-09-03) placed E06 on Rating Watch Negative, which is not a downgrade.

**Q18.** E06
A17 set RWN on E06 and nothing later clears it. E14's watch from A35 was cleared by the affirmation A33 (blank watch column).

**Q19.** E01 and E09
Both have a Negative outlook from their latest actions (A03 and A25). E08's DG actions leave the outlook blank, so its last recorded outlook is STA.

**Q20.** No
E07 was withdrawn (A19, WD), and the data states a withdrawal is not a credit event or default.

**Q21.** E07
It had a rating (A18) and was withdrawn (A19). E11 and VD only have a CO and a Country Ceiling, which do not count as issuer ratings.

**Q22.** E08
Only E08 has a default rating (RD, A22).

**Q23.** F2
Kestrel's short-term rating is F2 (A04).

**Q24.** Yes
Its FC issuer rating is BBB (A03), which is investment grade.

**Q25.** 5
I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I08 is only Expected (EX), so it is unrated.

**Q26.** A+
Corvenia Power's LC rating is A+ (A40).

**Q27.** A-
I06 was assigned A- (A42).

**Q28.** BBB+
CV's FC issuer rating is BBB+ (A38). Its A rating (A37) is a Country Ceiling, not an issuer rating.

**Q29.** None
VD has only a Country Ceiling (A12, BB), which is not the sovereign's issuer rating.

**Q30.** E05 and E15
E05's FC rating (BB, A14) equals the VD ceiling (BB, A12), and E15's FC rating (A, A41) equals the CV ceiling (A, A37).

**Q31.** No
Neither company's FC rating exceeds its ceiling: E05 is at BB and E15 is at A.

**Q32.** E09
E11's parent is E10, and E10's parent is E09, which has no parent.

**Q33.** Halden Bank AG (E10), rated BBB+
I05 is guaranteed by E10, so holders take E10's risk, and the instrument rating is BBB+ (A29).

**Q34.** No
E12 has no recorded parent, and E10's parent is E09, so the data gives no link. The shared name is not evidence of a common group.

**Q35.** 3
E09 (parent), E10 and E11 are the Halden group in the data.

**Q36.** 2
E02 (parent) and E04 are the Northwind group; E03 is the same entity as E02.

**Q37.** 16
There are 19 records, minus E03 and E17 (duplicate LEIs), minus E16 (QA data), giving 16 distinct entities.

**Q38.** No
They have different LEIs (ORRN00BANK00000DE233 and ORBC00BANCORP000US45).

**Q39.** A
The latest action on E02/E03 is A09 (AF, A, 2025-09-15).

**Q40.** 5
The GB issuers with ratings are E01, E02, E09, E12 and E14; E07 has been withdrawn, and E16 is QA data.

**Q41.** None
E16 is a QA record and must be ignored.

**Q42.** DE
RATINGS holds for country, and E10 is DE. E17's LU is from RESEARCH, which is not the system of record.

**Q43.** 0
No entity is domiciled in LU per RATINGS; E17's LU is from RESEARCH and E10 (same LEI) is DE.

**Q44.** Yes
I07 is in XVD, the domestic currency of VD, so it is local-currency debt.

**Q45.** No
Country Ceilings cap only FC ratings and FC debt; I07 is local-currency debt, so it is not capped.

**Q46.** No
E11 has only a CO (A46), which is not an issuer rating.

**Q47.** None
I08 has only an Expected (EX) action (A47), so it is unrated until an AS action.

**Q48.** 7
I01 through I07 are rated, and I08 is unrated.

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