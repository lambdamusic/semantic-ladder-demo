**Q1.** A-. E01's LTIDR FC was A- from AS A01 (2024-03-12) until DG A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions (A03, A04, 2026-02-10) are affirmations; A03 revised the outlook to NEG.

**Q3.** No. The 2031 note is I02 (subordinated); DG A07 put it at BB+, which is speculative grade.

**Q4.** POS. E02 and E03 share an LEI, so they are one entity; the latest action is A09 (2025-09-15), with outlook POS.

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and I03's rating (A38/A10, A11) is A.

**Q6.** The Country Ceiling for VD is BB (A12, from 2025-04-01) and caps foreign-currency ratings. E05's FC rating is BB (A14), and its LC rating is BBB- (A13) because local currency is not capped.

**Q7.** E08 and E10. The 2026 downgrades were A21 and A22 on E08, and A27 on E10 (E17 is the same entity as E10).

**Q8.** E08. Its latest LTIDR action, A22, set RD on 2026-07-08.

**Q9.** 209. This counts distinct entities with a non-withdrawn LTIDR on 2026-10-01, after merging records by LEI and excluding QA.

**Q10.** Depends. E05's FC rating is BB (speculative) and its LC rating is BBB- (investment grade).

**Q11.** BBB+. E14 was downgraded by A36 (2024-09-30), and the RW A35 came later.

**Q12.** A-. E14 was assigned A- by A34 (2023-01-15) and held it until A36.

**Q13.** 1. E14 has a single DG, A36.

**Q14.** none. E12 was first assigned on 2024-02-01 (A30).

**Q15.** A-. E10 and E17 share an LEI; A26 set A- and the DG A27 came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (the RW and AF did not change the rating).

**Q17.** No. E06's only 2026 action is RW A17, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) put it on RWN.

**Q19.** E01 and E09. A03 and A25 set outlook NEG.

**Q20.** No. E07's rating was withdrawn by A19 (commercial reasons); a withdrawal is not a default, and its last rating was BB.

**Q21.** E07. It had a rating (A18) and then a withdrawal (A19), so it has no issuer rating on 2026-10-01.

**Q22.** E08. It reached RD via A22; no other entity ever reached RD or D.

**Q23.** F2 (STIDR, A04).

**Q24.** Yes. E01's LTIDR is BBB.

**Q25.** 52. This counts instruments whose latest non-EX rating on 2026-10-01 is BBB- or better.

**Q26.** A+ (E15 LTIDR LC, A40).

**Q27.** A- (I06, A42, subordinated).

**Q28.** BBB+ (CV, A38).

**Q29.** none. VD has only a Country Ceiling (A12), which is not its issuer rating.

**Q30.** E05 and E15. E05's FC rating BB equals the VD ceiling BB, and E15's A equals the CV ceiling A.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10 (Halden Bank, the guarantor), rated BBB+. I05 was downgraded to BBB+ by A29.

**Q34.** No. E12 has no parent and is its own group, separate from E09's group.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 523. This counts distinct LEIs (sovereigns by ID), excluding QA records.

**Q38.** No. They have different LEIs (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A. E02 and E03 are the same entity, and A09 is the latest action.

**Q40.** 61, using the RESEARCH-held country.

**Q41.** none. E16 is a QA record, so its actions are ignored.

**Q42.** LU. E17 (RESEARCH) holds the country, overriding E10's DE.

**Q43.** 3.

**Q44.** Yes. I07 is in XVD, VD's domestic currency.

**Q45.** No. It is a local-currency obligation, so the ceiling does not cap it, and its BBB- (A45) is above the BB ceiling but not constrained by it.

**Q46.** No. E11 has only a Credit opinion (A46), which is not an issuer rating.

**Q47.** none. I08 has only an Expected rating (A47, EX), so it is unrated.

**Q48.** 98. This counts instruments with a non-withdrawn rating on 2026-10-01, excluding EX.

**Q49.** E5002 (Cerid Group plc), the parent of E5010.

**Q50.** 1. E5010 sits directly under E5002.

**Q51.** 29.

**Q52.** 3.

**Q53.** No. RATINGS (which holds parent links) places E5062 under E5060 and then the Belir group (E5059); the RESEARCH link to E5086 is not used. E5087 is a separate group.

**Q54.** E5093 and E5094.

**Q55.** 4.

**Q56.** B+, the lowest of the FC LTIDRs found for the group (BB+, B+, BB). The Vesol Group BV records E5171–E5173 carry the same LEI as Rotam Group Inc (E5087), so they are the same entity and the same group. The member counts here (Q52, Q56) came from partly garbled query output, so treat them with caution.

**Q57.** E5010. Both E5013 and E5025 have it as their direct parent.

**Q58.** E5037. It guarantees I119, which was issued by E5083 in the Belir group, while E5037 is in the Cerid group.

**Q59.** 8.

**Q60.** E5037 (Cerid Guven Capital SA), the guarantor of I119. It is not in the same group as the issuer E5083, which is in the Belir group. Its own current rating was not retrieved.

**Q61.** 2 (E5016 BB- and E5031 B).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 209},
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
"Q25": {"count": 52},
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
"Q37": {"count": 523},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 61},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 3},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 98},
"Q49": {"parent": "E5002"},
"Q50": {"count": 1},
"Q51": {"count": 29},
"Q52": {"count": 3},
"Q53": {"same_group": "no"},
"Q54": {"entities": ["E5093", "E5094"]},
"Q55": {"count": 4},
"Q56": {"rating": "B+"},
"Q57": {"entity": "E5010"},
"Q58": {"entities": ["E5037"]},
"Q59": {"count": 8},
"Q60": {"risk_of": "E5037", "same_group": "no"},
"Q61": {"count": 2}
}
```