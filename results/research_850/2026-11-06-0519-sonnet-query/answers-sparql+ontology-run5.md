**Q1.** 1 person. A01, A02 and A03 all carry ORCID 0000-0002-9841-6229, so they are the same person.

**Q2.** 32 works: every work recorded against A01, A02, A03 or A101, which share that ORCID. They include editorials, errata, a retracted work and K0-source works.

**Q3.** No. W37 is by A05 (ORCID …5008) and W38 is by A06 (ORCID …1779).

**Q4.** 9. Using A05 and A104 (same ORCID), W556 is a preprint of W1038 and counts once, and the other 8 works are research works.

**Q5.** No. A04 (ORCID …8662) wrote W08, and A01 (ORCID …9841) wrote W01.

**Q6.** A01, Mara Ellison, with 19 research works credited to I02. The next is Priya Ramanathan with 15.

**Q7.** 19. This is her 32 works minus 3 editorials (W04, W271, W936), 3 errata (W05, W813, W949), 1 retracted (W374), 3 in K0 sources (W07, W449, W763), and 3 preprints that merge into their published versions (W02, W612, W663).

**Q8.** I01. The chain is I04, then I03, then I02, then I01.

**Q9.** 95. This is the sum of the yearly counts credited to I02.

**Q10.** 140. This is the sum of the yearly counts for I01.

**Q11.** 59. This is the sum of the yearly counts for I07, units included.

**Q12.** Full 13, fractional about 5.83. These are I07's 2024 counts.

**Q13.** Full counting favours I07 (13 against 11). Fractional counting favours I09 (about 6.58 against 5.83).

**Q14.** Full 29, fractional 15.5.

**Q15.** 25.

**Q16.** 88. This is the sum of the yearly counts for S01.

**Q17.** W04, W271, W936 (editorials) and W05, W813, W949 (errata).

**Q18.** 15. These are A07's works, with W02 merged into W03 and W219 into W251, and the erratum W05 excluded.

**Q19.** 27. These are the distinct non-staging, non-retracted, non-K0 works citing W02 or W03.

**Q20.** 23 preprints, listed in the JSON below.

**Q21.** 45.

**Q22.** W30 has more in total (16 against 11). W31 has more within its window (11 against 2).

**Q23.** Total 16. In the window (2019–2021) there are 2, from W60 in 2020 and W988 in 2021.

**Q24.** 12. These are A09's works plus A103 (same ORCID), excluding retracted (W1025, W23, W693) and staging (W268, W714, W802) records.

**Q25.** 20. The cited works are W20 (13), W21 (2), W417 (2), W22 (1), W366 (1) and W531 (1); her other research works have none.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12, with 12 citing works.

**Q28.** 4.

**Q29.** Author 7, institution 10, country 19.

**Q30.** 14.

**Q31.** The 11 works at hop 2 (W1042, W337, W338, W396, W50, W51, W52, W546, W682, W801, W895).

**Q32.** 17. There are 7 at hop 1 and 11 at hop 2, and W895 is in both.

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 25.

**Q36.** 36.

**Q37.** I06. A08 lists I04 with sequence 1 and I06 with sequence 2, and only the last-listed affiliation counts.

**Q38.** I04, I03, I02 and I01. For W71, A08's last-listed affiliation is I04 (sequence 2), and the credit passes up through its parents.

**Q39.** 19. These are I02's works in S01, the only K3 source.

**Q40.** S01.

**Q41.** No. S03 is K1 and S02 is K2, so S03 is lower.

**Q42.** 0. S04 is delisted (K0), so none of its works count.

**Q43.** No. W07 appeared in S04, which is delisted.

**Q44.** I02, I03, I04, I05, I19 and I20. The affiliated institutes I06 and I21 are excluded.

**Q45.** 16.

**Q46.** I06. It is an affiliated institute, so its parent link is not followed.

**Q47.** Full counting gives each work to I07 or I09 once, regardless of how many authors it has. Fractional counting splits a work among its authors, so I09's works, which have fewer authors each, carry larger shares and I09 moves ahead.

**Q48.** A08's credited affiliation on W70 is the last-listed one, I06, which is an affiliated institute. Its parent link to I02 is not membership, so the work is not credited to I02. The Tessel Laboratory (I04) was listed first and is ignored.

```json
{
"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":19},
"Q8":{"parent":"I01"},
"Q9":{"count":95},
"Q10":{"count":140},
"Q11":{"count":59},
"Q12":{"full":13,"fractional":5.83},
"Q13":{"full":"I07","fractional":"I09"},
"Q14":{"full":29,"fractional":15.5},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W04","W271","W936","W05","W813","W949"]},
"Q18":{"count":15},
"Q19":{"count":27},
"Q20":{"works":["W02","W1049","W210","W219","W226","W263","W322","W407","W416","W42","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877"]},
"Q21":{"count":45},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":16,"in_window":2},
"Q24":{"count":12},
"Q25":{"count":20},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":12},
"Q28":{"count":4},
"Q29":{"author":7,"institution":10,"country":19},
"Q30":{"count":14},
"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W895"]},
"Q32":{"count":17},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":25},
"Q36":{"count":36},
"Q37":{"institution":"I06"},
"Q38":{"institutions":["I04","I03","I02","I01"]},
"Q39":{"count":19},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":0},
"Q43":{"research":"no"},
"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I06"}
}
```