**Q1.** 3. The people table lists Mara Ellison (A01), M. Ellison (A04) and M. Ellison (A102) as separate people with different ORCIDs; "Ellison, Mara J." is not a name in the people table, so I treated it as one of the records merged into A01.
**Q2.** 30 works: W01, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W608, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050. These are all the credits for A01.
**Q3.** No. W37 credits A05 (I05) and W38 credits A06 (I12), who have different ORCIDs.
**Q4.** 9. A05's research works are W14, W37, W554, W565, W702, W725, W785, W792 and W1038.
**Q5.** No. W08 credits A04 and W01 credits A01, who are separate people with different ORCIDs.
**Q6.** A01. A01 has 20 research works credited to I02, more than anyone else (for example A111 has about 9).
**Q7.** 20. These are A01's works after dropping editorials, errata, retracted works and delisted-source works.
**Q8.** I01. I04 sits under I03, then I02, then I01, per institution_units.
**Q9.** 93. This counts distinct research works credited to I02, I03, I04 or I19; I06 does not roll up into I02 in institution_units.
**Q10.** 138. The 93 above plus 38 more works from I05 and 7 more from I20.
**Q11.** 59. This counts distinct research works credited to I07 or I08.
**Q12.** Full 13, fractional 11. The 2024 works are W20, W21, W22, W203, W333, W419, W504, W528, W595, W624, W675, W705 and W1027, with shares totalling 11.
**Q13.** Full counting: I09 (16 works against 13). Fractional counting: I07 (11 against 4).
**Q14.** Full 46, fractional 42. I counted 2024 research works with at least one GB-credited author, and summed the GB share of authors per work; I scanned the list by hand, so a miss is possible.
**Q15.** 24 research works in S02 in 2024.
**Q16.** 86 research works in S01.
**Q17.** W04, W05, W271, W813, W936 and W949 are editorials or errata. W07, W374, W449 and W763 fail for other reasons (delisted source or retraction), not document type.
**Q18.** 15. A07's research works are W01, W03, W13, W72, W251, W262, W292, W293, W435, W553, W598, W758, W787, W833 and W969, not counting the erratum W05; A108 is a different person.
**Q19.** 26 distinct works cite W03, which already includes its merged preprint W02.
**Q20.** None. The merged preprint records (W02, W42 and others) are folded into their published works, and the PPR works that remain have no published version in the data.
**Q21.** 45 research works are credited to I14.
**Q22.** W30 has more in total (16 against 11). In the window W31 has more (11 against 2), counting the years 2019–2021 for W30 and 2023–2025 for W31.
**Q23.** W30 has 16 citations in total and 2 in its window (W60 and W988).
**Q24.** 12. A09's research works are W20, W21, W22, W203, W232, W366, W417, W478, W531, W686, W738 and W967.
**Q25.** 20. The citation counts are W20 13, W21 2, W22 1, W366 1, W417 2 and W531 1, with the rest at 0.
**Q26.** No. W23 is retracted, so it is not research output.
**Q27.** I12 has 12 citing works, the most among other institutions (I09 and I11 have 4 each).
**Q28.** 4. The I09 works citing Kesting's research are W32, W357, W586 and W777.
**Q29.** Author 7, institution 10, country 20, out of the 26 citing works.
**Q30.** 14. This adds works credited to I05 or I20 to the 10 University of Albury citers.
**Q31.** 11 works: W50, W51, W52, W337, W338, W396, W546, W682, W801, W895, W1042. They cite one of W01's citers (W40, W41, W229, W602, W657, W660, W895).
**Q32.** 17. W01 has 7 direct citers and 11 two-hop citers, and W895 appears in both groups.
**Q33.** W20, with 13 citations.
**Q34.** 7. The 2025 works are W08, W16, W24, W260, W603, W850 and W956.
**Q35.** 25 research works are credited to I08.
**Q36.** 37 research works appeared in S06.
**Q37.** I06. W70's only credit is A08 at I06 (Halloran).
**Q38.** I04, I03, I02 and I01. W71's credit is A08 at I04, which rolls up through I03 and I02 to I01.
**Q39.** 19. Of the University of Albury's 93 research works, 19 appeared in S01, the only rank-1 source.
**Q40.** S01.
**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, and rank 1 is the highest.
**Q42.** 0. S04 is delisted, so none of its works count as research output.
**Q43.** No. W07 is in S04, a delisted source.
**Q44.** I02, I03, I04, I05, I19 and I20, per institution_units. I06 and I21 have parent_ids but are not rolled up.
**Q45.** 16 research works are credited to I06.
**Q46.** I01 by parent_id (I06 → I02 → I01), although institution_units does not count I06's works towards I02 or I01.
**Q47.** Kesting's 2024 works mostly have only Kesting authors, so its fractional total stays at 11 against 13 under full counting. Each of Rostval's 16 works has just one Rostval author in four, so its total drops to 4.
**Q48.** W70's only credit is A08 at the Halloran Institute (I06), not at Tessel (I04). I06 is an affiliate and institution_units does not count it towards the University of Albury.

```json
{"Q1":{"count":3},
"Q2":{"works":["W01","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W608","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":20},
"Q8":{"parent":"I01"},
"Q9":{"count":93},
"Q10":{"count":138},
"Q11":{"count":59},
"Q12":{"full":13,"fractional":11},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":46,"fractional":42},
"Q15":{"count":24},
"Q16":{"count":86},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":26},
"Q20":{"works":[]},
"Q21":{"count":45},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":16,"in_window":2},
"Q24":{"count":12},
"Q25":{"count":20},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":12},
"Q28":{"count":4},
"Q29":{"author":7,"institution":10,"country":20},
"Q30":{"count":14},
"Q31":{"works":["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W1042"]},
"Q32":{"count":17},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":25},
"Q36":{"count":37},
"Q37":{"institution":"I06"},
"Q38":{"institutions":["I04","I03","I02","I01"]},
"Q39":{"count":19},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":0},
"Q43":{"research":"no"},
"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I01"}}
```