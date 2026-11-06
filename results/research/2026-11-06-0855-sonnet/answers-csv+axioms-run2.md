**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01, A02 and A03 combined. A04 (W08, W16) has a different ORCID and is excluded.

**Q3.** No. A05 (W37) and A06 (W38) have different ORCIDs, so I treat them as different people. The data cannot rule out one person holding two ORCIDs, but nothing links them.

**Q4.** 2. A05 authored W14 and W37.

**Q5.** No. W08's M. Ellison is A04, whose ORCID differs from Mara Ellison's.

**Q6.** A01, meaning the Mara Ellison person (lowest record ID A01). She has 5 research works credited to I02: W01, W03, W06, W12, W19. A07 has 4.

**Q7.** 5: W01, W03, W06, W12, W19. W02 is a preprint merged into W03, and W07 is in a delisted source (S04, K0).

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 8: W01, W03, W06, W12, W13, W19, W71, W72. W70, W73 and W74 are credited only to I06. I06 is an affiliated institute, so it does not roll up to I02.

**Q10.** 12. The 8 Albury works plus W14, W28, W29 and W37 via I05.

**Q11.** 6: W08, W16, W20, W21, W22, W24. W23 is retracted, and W90–W92 are staging records.

**Q12.** Full 3, fractional 2. W20, W21 and W22 are the 2024 works. They score 0.5, 0.5 and 1.

**Q13.** Full: I09 (4 against 3). Fractional: I07 (2 against 1). I09's 2024 works are W21, W27, W28 and W29, each with one of four authors from I09.

**Q14.** Full 7, fractional 6. The works are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 count 0.5 each, and the other five count 1 each.

**Q15.** 4: W12, W21, W28, W51.

**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4: W01, W03, W13, W72. W02 is a merged preprint and W05 is an erratum.

**Q19.** 7: W12, W13, W14, W15, W16, W17, W18. W15 cites both versions but counts once.

**Q20.** W02 (preprint of W03) and W42 (preprint of W31).

**Q21.** 4: W27, W31, W39, W50. W42 is a merged preprint.

**Q22.** In total W30 has more (5 against 4), but within the window W31 has more (4 against 1). W30's citers are W60–W64. W31's are W62, W65, W66, plus W67 via its preprint W42. The windows are 2019–2021 for W30 and 2023–2025 for W31.

**Q23.** Total 5, within the window 1 (only W60, 2020).

**Q24.** 3: W20, W21, W22. W23 is retracted.

**Q25.** 6. W20 has 3 citations (W32, W35, W36), W21 has 2 (W33, W36), and W22 has 1 (W34). The staging citers W90–W92 are excluded.

**Q26.** No. W23 is retracted, so it is not a research work.

**Q27.** I12, with 3 citing works: W33, W34, W35. I09 and I11 have 1 each, and the staging works are excluded.

**Q28.** 1 (W32).

**Q29.** Authors 2 (W12, W13), University of Albury 2 (W12, W13), countries 4 (W12, W13, W14, W15, all GB).

**Q30.** 3 (W12, W13, W14). W14 counts through I05, which is part of I01.

**Q31.** W50, W51, W52. W01 is cited by W40 and W41. W90 is excluded as staging.

**Q32.** 5: W40, W41, W50, W51, W52.

**Q33.** W20, with 3 citations.

**Q34.** 3: W08, W16, W24.

**Q35.** 2 (W21, W24).

**Q36.** 2 (W17, W24). W76 is an editorial.

**Q37.** I06. A08's highest affiliation sequence on W70 is 2, which is I06.

**Q38.** I04, I03, I02, I01. On W71 the highest sequence is I04, and the credit rolls up through its parents.

**Q39.** 3 (W01, W13, W71, all in S01).

**Q40.** S01, tier K3.

**Q41.** No. S03 is K1, the lowest of the ranked tiers, and S02 is K2.

**Q42.** 0. S04 is delisted (K0), so W07 and W75 do not count.

**Q43.** No. W07 is in a delisted source.

**Q44.** I02, I03, I04, I05. I06 is only an affiliated institute and does not count as a unit.

**Q45.** 3 (W70, W73, W74).

**Q46.** I06. As an affiliated institute it has no unit-of link, so it is its own ultimate parent.

**Q47.** I09's 4 works in 2024 (W21, W27, W28, W29) each give it only one author share out of four, so it scores 1.0 under fractional counting. I07's three works (W20, W21, W22) have fewer co-authors, so it scores 2.0. I09 leads on full counting (4 against 3), and I07 leads on fractional counting.

**Q48.** Credit goes to the author's highest-numbered affiliation on the work. On W70, A08 lists I04 (sequence 1) and I06 (sequence 2), so W70 is credited to I06, which is an affiliated institute that does not roll up to I02.

```json
{
"Q1": {"count": 1},
"Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},
"Q3": {"same": "no"},
"Q4": {"count": 2},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 5},
"Q8": {"parent": "I01"},
"Q9": {"count": 8},
"Q10": {"count": 12},
"Q11": {"count": 6},
"Q12": {"full": 3, "fractional": 2},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 7, "fractional": 6},
"Q15": {"count": 4},
"Q16": {"count": 10},
"Q17": {"works": ["W04","W05"]},
"Q18": {"count": 4},
"Q19": {"count": 7},
"Q20": {"works": ["W02","W42"]},
"Q21": {"count": 4},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 5, "in_window": 1},
"Q24": {"count": 3},
"Q25": {"count": 6},
"Q26": {"counts": "no"},
"Q27": {"institution": "I12", "citing_works": 3},
"Q28": {"count": 1},
"Q29": {"author": 2, "institution": 2, "country": 4},
"Q30": {"count": 3},
"Q31": {"works": ["W50","W51","W52"]},
"Q32": {"count": 5},
"Q33": {"work": "W20"},
"Q34": {"count": 3},
"Q35": {"count": 2},
"Q36": {"count": 2},
"Q37": {"institution": "I06"},
"Q38": {"institutions": ["I04","I03","I02","I01"]},
"Q39": {"count": 3},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 0},
"Q43": {"research": "no"},
"Q44": {"institutions": ["I02","I03","I04","I05"]},
"Q45": {"count": 3},
"Q46": {"parent": "I06"}
}
```