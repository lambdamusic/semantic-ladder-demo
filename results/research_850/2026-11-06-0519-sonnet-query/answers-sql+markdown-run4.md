**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229, so they are one person.

**Q2.** 32 works, listed in the JSON. They are every work against A01, A02, A03 or A101, since all share that ORCID, and they include the editorials, errata and the retracted W374. I did not check whether any of W555, W843, W905 and W984 is a staging record. The list is "of any type", so I kept them.

**Q3.** No. W37 is by A05 (ORCID …5008) and W38 is by A06 (ORCID …1779). The ORCIDs differ, so they are different people.

**Q4.** 9. This is ORCID 0000-0001-6105-5008, which covers A05 and A104, counted as research works only.

**Q5.** No. W08 is by A04, whose ORCID is …8360. W01 is by A01, whose ORCID is …6229.

**Q6.** A01. The person with ORCID 0000-0002-9841-6229 has 19 research works credited to I02 and its units, the most of anyone.

**Q7.** 29, counting each preprint and its published version once.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 111.

**Q10.** 159.

**Q11.** 92.

**Q12.** Full 13, fractional 11.0.

**Q13.** Full: I09 (16 against 13 for I07). Fractional: I07 (11.0 against 4.0 for I09).

**Q14.** Full 46, fractional 42.

**Q15.** 25.

**Q16.** 88.

**Q17.** W04, W05, W271, W813, W936 and W949. W04, W271 and W936 are editorials and W05, W813 and W949 are errata. W936 is recorded under A101, the same person.

**Q18.** 16.

**Q19.** 27. These are the distinct non-staging, non-retracted works that cite W03 or its preprint W02.

**Q20.** The 23 preprints listed in the JSON, from W02 to W877. Each names a published version that is also in the data.

**Q21.** 49.

**Q22.** In total W30 has more (16 against 11). Within its publication year and the two years after, W31 has more (11 against 2).

**Q23.** 16 in total, 2 within 2019–2021.

**Q24.** 18.

**Q25.** 20.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12 (Université de Lorvain), with 12 citing works.

**Q28.** 4.

**Q29.** Author 7, University of Albury 10, country 20.

**Q30.** 14.

**Q31.** 11 works: W1042, W337, W338, W396, W50, W51, W52, W546, W682, W801 and W895.

**Q32.** 17.

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 26.

**Q36.** 36.

**Q37.** I06. Its author's last-listed affiliation on W70 (sequence 2) is I06, so the work is credited there.

**Q38.** I04, I03, I02 and I01. The last-listed affiliation on W71 is I04, so the work is also credited up its chain.

**Q39.** 19. These are the research works credited to I02 and its units that appeared in S01.

**Q40.** S01. It is the only K3 source.

**Q41.** No. S03 is K1 and S02 is K2, so S03 is lower.

**Q42.** 0. S04 is delisted (K0), so none of its works count.

**Q43.** No. W07 appeared in S04, which is delisted.

**Q44.** I02, I03, I04, I19, I05 and I20. The affiliated institutes I06 and I21 are excluded.

**Q45.** 16.

**Q46.** I06. It is an affiliated institute, so its parent link is not followed and its ultimate parent is itself.

**Q47.** Full counting favours I09 because it has more works, 16 against 13. Under fractional counting I09's works are split among many authors, so most of each work's share goes to other institutions and countries. That leaves I09 with 4.0 against 11.0 for I07.

**Q48.** W70's author listed I04 first and I06 second, and only the last-listed affiliation counts, so W70 is credited to I06. I06 is an affiliated institute, so its works are never credited to I02.

```json
{
"Q1":{"count":1},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":29},
"Q8":{"parent":"I01"},
"Q9":{"count":111},
"Q10":{"count":159},
"Q11":{"count":92},
"Q12":{"full":13,"fractional":11},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":46,"fractional":42},
"Q15":{"count":25},
"Q16":{"count":88},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":16},
"Q19":{"count":27},
"Q20":{"works":["W02","W1049","W210","W219","W226","W263","W322","W407","W416","W42","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877"]},
"Q21":{"count":49},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":16,"in_window":2},
"Q24":{"count":18},
"Q25":{"count":20},
"Q26":{"counts":"no"},
"Q27":{"institution":"I12","citing_works":12},
"Q28":{"count":4},
"Q29":{"author":7,"institution":10,"country":20},
"Q30":{"count":14},
"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W895"]},
"Q32":{"count":17},
"Q33":{"work":"W20"},
"Q34":{"count":7},
"Q35":{"count":26},
"Q36":{"count":36},
"Q37":{"institution":"I06"},
"Q38":{"institutions":["I04","I03","I02","I01"]},
"Q39":{"count":19},
"Q40":{"source":"S01"},
"Q41":{"higher":"no"},
"Q42":{"count":0},
"Q43":{"research":"no"},
"Q44":{"institutions":["I02","I03","I04","I19","I05","I20"]},
"Q45":{"count":16},
"Q46":{"parent":"I06"}
}
```