Assumptions I used because the data does not define them:
- Research output means ART, REV and PPR records. A preprint is folded into the work named in its `version_of`.
- EDT, ERR, PTX and SUP records are not research output.
- STG (staging) records are excluded.
- Retracted works still count, because they remain published and are only flagged.
- Authors sharing an ORCID are treated as one person.
- A larger tier number is a higher tier (K3 is the highest).

**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229. The other "M. Ellison" records A04 and A102 have different ORCIDs.

**Q2.** Mara Ellison's 32 works are listed in the JSON, taken across her ORCID-linked records A01, A02, A03 and A101.

**Q3.** No. W37 has A05 and W38 has A06, with different ORCIDs.

**Q4.** 9. Counting A05 and A104 (same ORCID): W14, W37, W554, W565, W785, W792, W1038 (with its preprint W556), W702 and W725.

**Q5.** No. W08 is by A04 (ORCID 0000-0004-8662-8360) and W01 is by A01 (0000-0002-9841-6229).

**Q6.** A01. Mara Ellison has 23 research works credited to the University of Albury. The next closest is Quinn Yelland (A110) with 16.

**Q7.** 23. She has 32 records in total. I removed the editorials, errata and preprints (W02, W663, W612, which sit under W03, W464 and W869), leaving 23.

**Q8.** I01. I04 → I03 → I02 → I01.

**Q9.** 119, after merging preprints into their published versions (two retracted works are included).

**Q10.** 176. That is the 119 works above plus 57 more from I05, I20 and I21.

**Q11.** 68 for I07, I08 and I22 combined, with STG records excluded.

**Q12.** Full counting gives 14 and fractional counting gives 12.0. The 14 works are W20, W21, W22, W203, W333, W1027, W419, W421, W504, W528, W595, W624, W675 and W705.

**Q13.** Full counting favours I09 (15 works against Kesting's 14). Fractional counting favours I07 (12.0 against Rostval's 3.75).

**Q14.** Full counting gives 48 works and fractional counting gives 44, from my hand scan of the 2024 records.

**Q15.** 27 research works in S02 in 2024, including the retracted W520 and W922.

**Q16.** 89 research works in S01.

**Q17.** W04, W05, W271, W813, W936 and W949 are editorials or errata.

**Q18.** 15 distinct works. The preprints W02 and W219 collapse into W03 and W251.

**Q19.** 29. The 29 distinct citers of W02 or W03 include W17, W397 and W569, which are non-research or staging records.

**Q20.** 23 preprints have a `version_of` target that is in the data. They are listed in the JSON.

**Q21.** 46 research works for I14.

**Q22.** W30 has more citations in total (18 against 13). W31 has more within its window (13 against 2). For W31 I counted both versions, W31 and W42.

**Q23.** W30 has 18 citations in total, 2 of them in 2019–2021 (W60 and W988).

**Q24.** 15. Counting A09 and A103 (same ORCID), I excluded the staging records W268, W714 and W802.

**Q25.** 42. The citation counts are W20 14, W22 19, W21 3, W417 2, W23 1, W366 1, W967 1 and W531 1; the other works have none.

**Q26.** Yes. W23 is an ART from I07 and is flagged retracted but not removed. I counted it, though this rests on my assumption about retractions.

**Q27.** I12 (Université de Lorvain), with 14 citing works, mostly citing W20.

**Q28.** 4 works: W32, W357, W586 and W777.

**Q29.** At author level there are 7 self-citing works. At University of Albury level there are 12. At country level (GB) there are 21.

**Q30.** 18 at Albury University System level (the 12 above plus W14, W214, W349, W544, W748 and W812).

**Q31.** 14 works cite a work that cites W01. W01's citers are W40, W41, W229, W602, W657, W660, W844 and W895.

**Q32.** 20. These are W01's 8 direct citers plus 12 further works.

**Q33.** W22, with 19 citations. W20 is next with 14.

**Q34.** 7. They are W08, W16, W260, W603, W693, W850 and W956.

**Q35.** 25 research works for I08.

**Q36.** 26 research works in S06.

**Q37.** I04 (affil_seq 1). The same author also lists I06 as a second affiliation.

**Q38.** I04, I03, I02 and I01 via the Tessel Laboratory, and I06, I02 and I01 via Halloran. In total: I01, I02, I03, I04, I06.

**Q39.** 21. These University of Albury works are in S01, the only K3 source.

**Q40.** S01.

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 13 research works in S04.

**Q43.** Yes. W07 is an ART, and its source's K0 tier does not change its document type.

**Q44.** I02, I03, I04, I05, I06, I19, I20, I21.

**Q45.** 22 research works for I06.

**Q46.** I01. I06 → I02 → I01.

**Q47.** In 2024 Rostval has 15 works against Kesting's 14, so Rostval leads under full counting. Rostval's works typically have one Rostval author among about four, giving 0.25 each (3.75 in total). Kesting's works are mostly written entirely by Kesting authors, giving 12.0. Kesting therefore leads under fractional counting.

**Q48.** The premise is wrong. W70 is a University of Albury work: I04 → I03 → I02, and its other affiliation I06 is also under I02. The two affiliations count once.

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
"Q9": {"count": 119},
"Q10": {"count": 176},
"Q11": {"count": 68},
"Q12": {"full": 14, "fractional": 12},
"Q13": {"full": "I09", "fractional": "I07"},
"Q14": {"full": 48, "fractional": 44},
"Q15": {"count": 27},
"Q16": {"count": 89},
"Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
"Q18": {"count": 15},
"Q19": {"count": 29},
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