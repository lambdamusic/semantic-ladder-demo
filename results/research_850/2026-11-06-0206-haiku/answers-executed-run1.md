**Q1.** 3 people: A01, A04 and A102. "Ellison, Mara J." has no record in people.csv, so it adds nothing. A01 and A04 have different ORCIDs, and A102 is separate too.

**Q2.** 29 works, all types: W01, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050. These are every credits row with person A01.

**Q3.** No. W37 credits A05 and W38 credits A06, which people.csv keeps as separate people with different ORCIDs.

**Q4.** 9 research works. A05's credits are W14, W37, W554, W565, W702, W725, W785, W792 and W1038, all at I05 and all research output.

**Q5.** No. W08 credits A04 and W01 credits A01, which are different people.

**Q6.** A01 (Mara Ellison), with 19 research works in the I02 family. The next highest are A110 and A118 with 14 each. A01's I02 credits are W01, W03, W06, W12, W19, W206, W238, W464, W555, W676, W817, W843, W869, W905, W972, W984, W1005, W1048 and W1050.

**Q7.** 19. These are A01's research credits, the same list as Q6.

**Q8.** I01. I04 → I03 → I02 → I01 by levels_up in institution_units.

**Q9.** 87 research works. I02's units are I02, I03, I04 and I19 (institution_units), and I counted distinct works credited to any of them. This is a manual tally across the credits file.

**Q10.** 132 research works. I01's units are I01, I02, I03, I04, I05, I19 and I20, and I took the union of their distinct works. This is a manual tally.

**Q11.** 58 research works. Kesting's units are I07 and I08 (institution_units), and I took distinct works credited to either. This is a manual tally.

**Q12.** Full 13, fractional 11. The 2024 works are W20, W21, W22, W203, W333, W419, W504, W528, W595, W624, W675, W705 and W1027. Fractional shares use each work's credited authors, so W21 gives 2/4 and W203 gives 5/6.

**Q13.** I07 on both. Full counting gives I07 13 and I09 11. Fractional counting gives I07 11 and I09 2.75, since I09 gets 0.25 on each of its 11 works.

**Q14.** Not completed. Working this out needs the GB-affiliated authors on every 2024 research work, and I did not finish that tally reliably.

**Q15.** 22 research works. These are the 2024 works sourced from S02, including W12, W21, W28, W217, W270, W378, W419, W421, W497, W501, W571, W646, W648, W661, W705, W721, W787, W791, W830, W842, W854 and W1004. This is a manual scan.

**Q16.** 88 research works. These are the works sourced from S01 with research_output = yes. This is a manual scan of works.csv and may be off by a few.

**Q17.** W04, W05, W271, W813, W936 and W949. Their types are EDT or ERR, which are not research output. W07, W449 and W763 are excluded by source delisting and W374 by retraction, so they are not type-based.

**Q18.** 15 research works. These are the credits to person A07, the person kept separate from A108, and the list is W01, W03, W13, W72, W251, W262, W292, W293, W435, W553, W598, W758, W787, W833 and W969.

**Q19.** 27 works. Citations to W03 come from 27 distinct citing works, and W02 has no citations because it is not in the works table.

**Q20.** None. The PPR records in the data (W18, W221, W306, W336, W566, W745, W747, W780, W781, W824, W1054) are unmerged, and none of them lists another in-data work in its record_ids. W824 and W1054 have similar titles, but the data does not link them.

**Q21.** 39 research works. These are the credits to I14, with I14 having no sub-units. This is a manual tally.

**Q22.** W30 has more citations in total, and W31 has more within its window. Total: W30 16 vs W31 11. Within 2019–2021 for W30 and 2023–2025 for W31: W30 2 vs W31 11.

**Q23.** 16 in total and 2 within 2019–2021 (W60 in 2020 and W988 in 2021).

**Q24.** 11 research works. A09's research credits are W20, W21, W22, W203, W232, W366, W417, W478, W531, W686 and W967. W23 and W693 are excluded as not research output, and W1025 is excluded by retraction.

**Q25.** 20 citations in total. W20 accounts for 13, W21 for 2, W417 for 2, and W22, W366 and W531 for 1 each.

**Q26.** No. W23 is retracted, so its research_output is "no".

**Q27.** I12 (Université de Lorvain), with 12 citing works. Those are W33, W34, W35, W282, W300, W302, W515, W592, W621, W783, W853 and W904.

**Q28.** 4 works: W32, W357, W586 and W777.

**Q29.** Author 7, institution 10, country 20. The citing works are the 27 from Q19. Shared author A01 or A07 gives 7 self-citations. Any I02/I03/I04/I19 credit gives 10. Any GB institution gives 20.

**Q30.** 14. These are the citing works with a credited author in an I01 unit (I01, I02, I03, I04, I05, I19 or I20). I06 is excluded because institution_units does not roll it up to I01.

**Q31.** W50, W51, W52, W337, W338, W396, W546, W682, W801, W895 and W1042. Each cites one of W01's citers: W40, W41, W229, W602, W657, W660 or W895.

**Q32.** 17 works. Two hops give 7 citers of W01 (W40, W41, W229, W602, W657, W660, W895) and 10 citers of those, for 17 in total.

**Q33.** W20, with 13 citations. The next highest Kesting work has 2.

**Q34.** 7 research works. These are W08, W16, W24, W260, W603, W850 and W956 for I07 (with I08), all dated 2025.

**Q35.** 25 research works credited directly to I08.

**Q36.** 36 research works. These are the research-output works sourced from S06, including W17, W24, W229, W232, W233 and W1036. This is a manual scan.

**Q37.** I06. W70's only credit is A08 at I06.

**Q38.** I04, I03, I02 and I01. W71's credit is A08 at I04, and I04 counts towards I03, I02 and I01 by levels_up.

**Q39.** 16 research works. S01 is the tier_rank 1 source, and I counted University of Albury works (I02 family) sourced from S01.

**Q40.** S01 (Journal of Marine Autonomy), tier K3 with tier_rank 1.

**Q41.** No. S03 has tier_rank 3, and S02 has tier_rank 2, so S02 is higher.

**Q42.** 0. S04 is delisted, so none of its works are research output.

**Q43.** No. W07 is in S04, which is delisted.

**Q44.** I02, I03, I04, I05, I19 and I20, per institution_units. I06 and I21 have a parent in the Albury tree in institutions.csv, but institution_units does not count them towards I01.

**Q45.** 16 research works credited to I06, which has no sub-units in institution_units.

**Q46.** I01. The parent chain in institutions.csv is I06 → I02 → I01. institution_units does not roll I06 up, so this follows the institutions table.

**Q47.** They do not swap in this data, so the premise does not hold. Full: I07 13 vs I09 11. Fractional: I07 11 vs I09 2.75, so I07 leads on both.

**Q48.** W70 is credited to A08 at I06 (Halloran), not I04. The Tessel lab (I04) is credited only on W71. I06 counts only towards itself in institution_units, so W70 is not in the University of Albury family.

```json
{
  "Q1": {"count": 3},
  "Q2": {"works": ["W01","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 9},
  "Q5": {"same": "no"},
  "Q6": {"author": "A01"},
  "Q7": {"count": 19},
  "Q8": {"parent": "I01"},
  "Q9": {"count": 87},
  "Q10": {"count": 132},
  "Q11": {"count": 58},
  "Q12": {"full": 13, "fractional": 11},
  "Q13": {"full": "I07", "fractional": "I07"},
  "Q14": {"full": null, "fractional": null},
  "Q15": {"count": 22},
  "Q16": {"count": 88},
  "Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
  "Q18": {"count": 15},
  "Q19": {"count": 27},
  "Q20": {"works": []},
  "Q21": {"count": 39},
  "Q22": {"more_in_total": "W30", "more_in_window": "W31"},
  "Q23": {"total": 16, "in_window": 2},
  "Q24": {"count": 11},
  "Q25": {"count": 20},
  "Q26": {"counts": "no"},
  "Q27": {"institution": "I12", "citing_works": 12},
  "Q28": {"count": 4},
  "Q29": {"author": 7, "institution": 10, "country": 20},
  "Q30": {"count": 14},
  "Q31": {"works": ["W50","W51","W52","W337","W338","W396","W546","W682","W801","W895","W1042"]},
  "Q32": {"count": 17},
  "Q33": {"work": "W20"},
  "Q34": {"count": 7},
  "Q35": {"count": 25},
  "Q36": {"count": 36},
  "Q37": {"institution": "I06"},
  "Q38": {"institutions": ["I04","I03","I02","I01"]},
  "Q39": {"count": 16},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 0},
  "Q43": {"research": "no"},
  "Q44": {"institutions": ["I02","I03","I04","I05","I19","I20"]},
  "Q45": {"count": 16},
  "Q46": {"parent": "I01"}
}
```