**Q1.** 3. The data has Mara Ellison (A01), M. Ellison (A04) and M. Ellison (A102), with three different ORCIDs. "Ellison, Mara J." matches no person record, so I can't place it.
**Q2.** Mara Ellison (A01) is credited on 30 works: W01, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W608, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050.
**Q3.** No. W37 is by A05 (I05) and W38 by A06 (I12), who have different ORCIDs.
**Q4.** 9. A05's research works are W14, W37, W554, W565, W702, W725, W785, W792 and W1038.
**Q5.** No. M. Ellison on W08 is A04, a different person from A01, with a different ORCID.
**Q6.** A01. She has 20 research works credited to I02. Units that count towards I02 are I03, I04 and I19.
**Q7.** 20 research works, namely the works in Q2 minus the non-research ones (W04, W05, W07, W271, W374, W449, W763, W813, W936, W949).
**Q8.** I01, via I04 → I03 → I02 → I01.
**Q9.** 93. This counts distinct research works credited to I02, I03, I04 or I19; I06 does not roll up into I02 in institution_units. I counted this by hand, so treat it as approximate.
**Q10.** 138. The 93 above plus 45 more credited to I05 or I20; I06 and I21 do not roll up into I01. Also a hand count.
**Q11.** 59. These are the research works credited to I07 or I08; W23 (retracted) is excluded.
**Q12.** Full 13, fractional 11 (2024 works credited to I07 or I08).
**Q13.** Full counting favours I09 (14 against 13), while fractional counting favours I07 (11 against 4.25).
**Q14.** Full 46, fractional 42 (2024 research works with GB-credited authors).
**Q15.** 23 research works in S02 in 2024.
**Q16.** 83 research works in S01.
**Q17.** W04, W05, W271, W813, W936 and W949 (editorials and errata). W07, W374, W449 and W763 fail for other reasons: a delisted source or a retraction.
**Q18.** 15 distinct research works for A07; A108 is a different person with a different ORCID.
**Q19.** 27 works cite W03. W02 is merged into it, and W18 is included.
**Q20.** None. Preprints W02, W219 and similar are already merged into their published versions, and the remaining PPR works have no published counterpart in the data.
**Q21.** 43 research works credited to I14.
**Q22.** W30 has more citations in total (16 against 11). W31 has more within its publication year and the two years after (11 against 2).
**Q23.** W30 has 16 citations in total and 2 in 2019–2021 (W60 and W988).
**Q24.** 12 research works for A09. W23 and W693 are excluded as retracted.
**Q25.** 20. The citation counts are W20 13, W21 2, W22 1, W366 1, W417 2, W531 1, and 0 for the other six.
**Q26.** No. W23 is retracted, so it is not research output.
**Q27.** I12 (Université de Lorvain), with 12 of its works citing Kesting's research works.
**Q28.** 4 works (W32, W586, W777, W357).
**Q29.** Author level 7, institution (University of Albury) level 10, country level 20.
**Q30.** 14 at Albury University System level, which adds W14, W349, W544 and W748 to the 10 from Q29.
**Q31.** W50, W51, W52, W337, W338, W396, W546, W682, W801, W895 and W1042. The works citing W01 are W40, W41, W229, W602, W657, W660 and W895.
**Q32.** 17 (the 7 works citing W01 plus 10 more, with W895 in both).
**Q33.** W20, with 13 citations.
**Q34.** 7 (W08, W16, W24, W260, W603, W850, W956).
**Q35.** 25 research works.
**Q36.** 36 research works in S06.
**Q37.** I06, the Halloran Institute (A08's credit on W70).
**Q38.** I04, I03, I02 and I01.
**Q39.** 19 of the 93 appeared in S01, the only rank-1 source.
**Q40.** S01.
**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, and rank 1 is highest, so S02 is higher.
**Q42.** 0. S04 is delisted, so none of its works are research output.
**Q43.** No. W07 is in delisted S04.
**Q44.** I02, I03, I04, I05, I19 and I20 (from institution_units; I06 and I21 are affiliates and do not roll up).
**Q45.** 16 research works.
**Q46.** I01. I06's parent is I02, whose parent is I01, even though its works don't count towards them.
**Q47.** Kesting has more works under full counting only if you count whole works. Its 2024 works are 13 against Rostval's 14, but many of Rostval's have four authors from different institutions, so each Rostval work is worth about 0.25. Kesting's works are mostly single-institution or tightly shared, so fractionally it leads, 11 to 4.25.
**Q48.** W70's only credit (A08) goes to I06, the Halloran Institute. In institution_units I06 counts only towards itself, not I02, so the work doesn't roll up into the University of Albury. The Tessel Laboratory (I04) is not the credited institution.

```json
{"Q1":{"count":3},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W608","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},"Q3":{"same":"no"},"Q4":{"count":9},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":20},"Q8":{"parent":"I01"},"Q9":{"count":93},"Q10":{"count":138},"Q11":{"count":59},"Q12":{"full":13,"fractional":11},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":46,"fractional":42},"Q15":{"count":23},"Q16":{"count":83},"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},"Q18":{"count":15},"Q19":{"count":27},"Q20":{"works":[]},"Q21":{"count":43},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":16,"in_window":2},"Q24":{"count":12},"Q25":{"count":20},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":12},"Q28":{"count":4},"Q29":{"author":7,"institution":10,"country":20},"Q30":{"count":14},"Q31":{"works":["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W1042"]},"Q32":{"count":17},"Q33":{"work":"W20"},"Q34":{"count":7},"Q35":{"count":25},"Q36":{"count":36},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":19},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},"Q45":{"count":16},"Q46":{"parent":"I01"}}
```