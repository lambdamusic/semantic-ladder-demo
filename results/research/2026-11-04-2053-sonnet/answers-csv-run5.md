**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person. A04 ("M. Ellison") has a different ORCID.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. These are the works of A01, A02 and A03, who are the same person.

**Q3.** No. W37 is by A05 and W38 is by A06, and their ORCIDs differ.

**Q4.** 2 (W14, W37).

**Q5.** No. W08's author is A04, whose ORCID differs from Mara Ellison's.

**Q6.** A01, Mara Ellison, with 6 research works (W01, W03, W06, W07, W12, W19). Priya Ramanathan (A07) and Brandt-Wierzba's A08 have 4 each.

**Q7.** 6 (W01, W03, W06, W07, W12, W19). W02 is the preprint of W03, so it is counted once.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 12 (W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74). I count I02, I03, I04 and I06.

**Q10.** 16. These are the 12 above plus W14, W28, W29 and W37 from I05.

**Q11.** 6 (W08, W16, W20, W21, W22, W23).

**Q12.** Full 3, fractional 2.0. In 2024 W20 gives 0.5, W21 gives 0.5 and W22 gives 1.

**Q13.** Full: I09 (4 works against 3). Fractional: I07 (2.0 against 1.0).

**Q14.** Full 7, fractional 6.0. The 2024 works with GB authors are W06, W12, W13, W28, W29, W71 and W72. W28 and W29 each count 0.5 and the rest count 1.

**Q15.** 4 (W12, W21, W28, W51).

**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).

**Q17.** W04 (editorial) and W05 (erratum).

**Q18.** 4 (W01, W03, W13, W72). W02 duplicates W03 and W05 is an erratum.

**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18).

**Q20.** W02 (of W03) and W42 (of W31).

**Q21.** 4 (W27, W31, W39, W50). W42 is the preprint of W31.

**Q22.** In total, W30 has more citations (5 against 4). Within its publication year and the two years after, W31 has more (4 against 1).

**Q23.** Total 5, in window 1. W30 is cited by W60, W61, W62, W63 and W64, and only W60 (2020) falls in 2019–2021.

**Q24.** 4 (W20, W21, W22, W23).

**Q25.** 7. W20 has 3, W21 has 2, W22 has 1 and W23 has 1. I excluded the staging records W90–W92 as citers.

**Q26.** Yes. W23 is retracted, but it is still an article by Kesting.

**Q27.** I12, with 3 citing works (W33, W34, W35).

**Q28.** 1 (W32).

**Q29.** Author 2 (W12, W13), institution 2 (W12, W13), country 4 (W12, W13, W14, W15). W16's author A04 is a different person from Mara Ellison.

**Q30.** 3 (W12, W13, W14). W14 comes from I05, which is also in the Albury University System.

**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and these three cite those.

**Q32.** 5 (W40, W41, W50, W51, W52).

**Q33.** W20, with 3 citations.

**Q34.** 2 (W08, W16). W90–W92 are staging records and are excluded.

**Q35.** 1 (W21). W24 is a SUP item and is excluded.

**Q36.** 0. W17 and W24 are SUP and W76 is an editorial, none of which I count as research.

**Q37.** I04, listed first (affil_seq 1). W70 also lists I06 second.

**Q38.** I06 and I04 directly, plus their ancestors I03, I02 and I01.

**Q39.** 4 (W01, W13, W71, W74), taking S01 as the highest tier.

**Q40.** S01. The tier order is not defined, so I assumed K3 is the highest.

**Q41.** No, on that same assumption: S03 is K1 and S02 is K2.

**Q42.** 2 (W07, W75).

**Q43.** Yes. W07 is an ART, although its source has tier K0.

**Q44.** I02, I03, I04, I05, I06.

**Q45.** 4 (W70, W71, W73, W74).

**Q46.** I01.

**Q47.** Kesting has fewer 2024 works (3 against 4) but holds larger authorship shares in them. Rostval is only one of four authors on W21, W27, W28 and W29, so it scores 1.0 against Kesting's 2.0.

**Q48.** The premise is wrong. I04 sits under I03, which sits under I02, so W70 is one of the University of Albury's works and is included in my count of 12.

Assumptions: research works are ART, REV and PPR, with preprints deduplicated against their published versions. EDT, ERR, PTX and SUP are excluded, and so are STG (staging) records.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":7},"Q26":{"counts":"yes"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```