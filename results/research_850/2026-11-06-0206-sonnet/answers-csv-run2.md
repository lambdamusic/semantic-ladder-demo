**Assumptions.** The data has no codebook, so I used these conventions.
- **Research works:** ART, REV and PPR types only. EDT, ERR, PTX and SUP are excluded.
- **Preprints:** a PPR with a `version_of` is merged into its published version.
- **Staging records:** STG records are excluded.
- **Retracted works:** they are kept and counted.
- **Tiers:** K3 is the highest tier.
- **Institution roll-ups:** "units included" means all descendants via `parent_id`. The Halloran Institute (I06) is an AFF unit whose `parent_id` is I02, and I counted it as part of Albury.
- **Same person:** author records with the same ORCID are one person.

The counts are hand-tallied, so the larger ones (Q9, Q10, Q16) are the most likely to be off by a few.

**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229. A04 (…8662-8360) and A102 (…4738-8328) are different people.
**Q2.** 32 works across A01, A02, A03 and A101, listed in the JSON.
**Q3.** No. W37 is by A05 and W38 by A06, with different ORCIDs.
**Q4.** 9. A05 and A104 share ORCID …6105-5008: W14, W37, W554, W565, W785, W792, W1038, W702 and W725. W556 is a preprint of W1038.
**Q5.** No. W08's A04 has a different ORCID from Mara's A01.
**Q6.** A01, with 23 research works. The next highest is about 15 (A07, A118).
**Q7.** 23. Her 32 works minus EDT/ERR (W04, W05, W271, W813, W936, W949) and the preprints W02, W612 and W663.
**Q8.** I01. I04 → I03 → I02 → I01.
**Q9.** 118, counting I02, I03, I04, I06 and I19.
**Q10.** 174: the 118 above plus 56 more via I05, I20 and I21.
**Q11.** 70, via I07, I08 and I22. W90–W92 are staging records and W24 is SUP, so they are excluded.
**Q12.** Full 14, fractional 12.0. The fractional total is 6 works at 1, W20 and W21 at 0.5 each, W203 at 5/6, W419 at 2/3 and W675 at 0.5.
**Q13.** Full counting favours I09 (15 vs 14). Fractional favours I07 (12.0 vs 3.75).
**Q14.** Full 48, fractional 44.0.
**Q15.** 26, including the retracted W520 and W922.
**Q16.** 89. This is the least certain tally.
**Q17.** W04, W05, W271, W813, W936 and W949. The first, third and fifth are EDT; the others are ERR.
**Q18.** 15. A08's namesake A108 is a different person.
**Q19.** 30 distinct citing works, citing W02 or W03.
**Q20.** 23 works: W02, W42, W210, W219, W226, W263, W322, W407, W416, W432, W460, W506, W522, W524, W545, W556, W611, W612, W663, W728, W730, W877 and W1049. Each has a `version_of` that exists in the data.
**Q21.** 46.
**Q22.** W30 has more in total (18 vs 13 for W31 plus W42). W31 has more within its window (13 vs 2).
**Q23.** 18 in total. Only 2 fall in 2019–2021 (W60 and W988).
**Q24.** 15. A09 and A103 are the same person (ORCID …8073-7028). STG works W268, W714 and W802 are excluded.
**Q25.** 42: W20 has 14, W21 has 3, W22 has 19, W23 has 1, W366 has 1, W417 has 2, W967 has 1 and W531 has 1.
**Q26.** Yes by my convention. W23 is an ART at I07 but is flagged `is_retracted`, so it would drop out if retractions are excluded.
**Q27.** I12 (Université de Lorvain), with 14 citing works, versus 4 each for I09, I11, I14 and I19.
**Q28.** 4: W32, W357, W586 and W777.
**Q29.** Author 7, institution 12, country 21.
**Q30.** 18.
**Q31.** 14 works, listed in the JSON.
**Q32.** 20 (8 direct citers plus 12 further works).
**Q33.** W22, with 19 citations. W20 has 14.
**Q34.** 7.
**Q35.** 25.
**Q36.** 26.
**Q37.** I04. It is the first-listed affiliation (`affil_seq` 1) for A08 on W70, and I06 is listed second.
**Q38.** I01, I02, I03, I04 and I06 (I06 → I02 → I01; I04 → I03 → I02 → I01).
**Q39.** 21.
**Q40.** S01.
**Q41.** No. S03 is K1 and S02 is K2.
**Q42.** 13.
**Q43.** Yes. W07 is an ART.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22.
**Q46.** I01 (I06 → I02 → I01).

**Q47.** Kesting's 2024 works are mostly sole- or few-author, so fractional counting keeps nearly all the credit (12.0 of 14). Rostval's 15 works are almost all four-author papers with one Rostval author each, so each is worth only 0.25 (3.75 total).

**Q48.** The premise doesn't hold. W70 is an ART, and its author lists I04 and I06. I04 sits under I03 and then I02, and I06 sits under I02, so W70 does count towards the University of Albury when units are included. It would be missed only if credit were taken at the directly listed institution.

```json
{
"Q1": {"count": 3},
"Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3": {"same": "no"},
"Q4": {"count": 9},
"Q5": {"same": "no"},
"Q6": {"author": "A01"},
"Q7": {"count": 23},
"Q8": {"parent": "I01"},
"Q9": {"count": 118},
"Q10": {"count": 174},
"Q11": {"count": 70},
"Q12": {"full": 14, "fractional": 12},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 48, "fractional": 44},
"Q15": {"count": 26},
"Q16": {"count": 89},
"Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
"Q18": {"count": 15},
"Q19": {"count": 30},
"Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21": {"count": 46},
"Q22": {"more_in_total": "W30", "more_in_window": "W31"},
"Q23": {"total": 18, "in_window": 2},
"Q24": {"count": 15},
"Q25": {"count": 42},
"Q26": {"counts": "yes"},
"Q27": {"institution": "I12", "citing_works": 14},
"Q28": {"count": 4},
"Q29": {"author": 7, "institution": 12, "country": 21},
"Q30": {"count": 18},
"Q31": {"works": ["W50","W51","W52","W90","W337","W338","W396","W546","W682","W801","W844","W895","W922","W1042"]},
"Q32": {"count": 20},
"Q33": {"work": "W22"},
"Q34": {"count": 7},
"Q35": {"count": 25},
"Q36": {"count": 26},
"Q37": {"institution": "I04"},
"Q38": {"institutions": ["I01","I02","I03","I04","I06"]},
"Q39": {"count": 21},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": 13},
"Q43": {"research": "yes"},
"Q44": {"institutions": ["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45": {"count": 22},
"Q46": {"parent": "I01"}
}
```