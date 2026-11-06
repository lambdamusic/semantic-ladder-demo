Six files, shown as the model gets them in the conditions that read CSV. `generate_data.py` writes them from a fixed seed.

There are 52 designed works and 33 background works. The background works are noise: their authors are at four background institutions, and they cite only each other, except for the few that set up the citation-window questions.

The hierarchy: Tessel Laboratory (I04, LAB) sits under the Albury Centre for Marine Robotics (I03, LAB), under the University of Albury (I02, UNI), under the Albury University System (I01, SYS), which also holds Albury Metropolitan University (I05). Halloran Institute (I06, AFF) has I02 as its parent but is not a unit of it. Kesting Institute of Hydrodynamics (I08, LAB) sits under Kesting University (I07).

### The traps, and the questions that test each

| Trap | Questions | How the data sets it |
|---|---|---|
| Who is who | [Q1](/domains/research/questions/#Q1) to [Q7](/domains/research/questions/#Q7) | A01, A02 and A03 are Mara Ellison (one ORCID); A04, also "M. Ellison", is someone else at Kesting; A05 and A06 are two Jonas Brandts. By record, Priya Ramanathan (A07, 4 works) beats each Mara record; merged, Mara has 5 ([Q6](/domains/research/questions/#Q6)). [Q7](/domains/research/questions/#Q7) combines identity, versions, document types and the delisted source |
| Institution hierarchy | [Q8](/domains/research/questions/#Q8) to [Q11](/domains/research/questions/#Q11) (also [Q38](/domains/research/questions/#Q38), [Q44](/domains/research/questions/#Q44), [Q46](/domains/research/questions/#Q46)) | Ultimate parent three levels up ([Q8](/domains/research/questions/#Q8)); a university's count includes its labs ([Q9](/domains/research/questions/#Q9)); a system's count includes both universities, with W12 shared between them counted once ([Q10](/domains/research/questions/#Q10)) |
| Counting method | [Q12](/domains/research/questions/#Q12) to [Q14](/domains/research/questions/#Q14), [Q47](/domains/research/questions/#Q47) | Kesting 2024: full 3, fractional 2. Rostval 2024: full 4, fractional 1 (four works, one author of four from Rostval on each), so the ranking flips ([Q13](/domains/research/questions/#Q13)). GB 2024: full 7, fractional 6. All fractional answers are whole numbers by design |
| Document types | [Q15](/domains/research/questions/#Q15) to [Q17](/domains/research/questions/#Q17) | Editorials (W04, W76), an erratum (W05), paratext (W09, W10) |
| Versions | [Q18](/domains/research/questions/#Q18) to [Q21](/domains/research/questions/#Q21) | W02 is the preprint of W03 and W42 of W31 (`version_of`); W18 is a preprint with no published version; W15 cites both W02 and W03 |
| Citation windows | [Q22](/domains/research/questions/#Q22), [Q23](/domains/research/questions/#Q23) | W30 (2019) has 5 citations in all but 1 within its year plus two; W31 (2023) has 4 in all, all within the window |
| Retractions | [Q24](/domains/research/questions/#Q24) to [Q26](/domains/research/questions/#Q26) | W23 (Lena Vossberg, Kesting) is retracted and cited once (W39) |
| Citations at several levels | [Q27](/domains/research/questions/#Q27) to [Q32](/domains/research/questions/#Q32) | Kesting is cited by three single-author Lorvain works and by one Rostval work with four Rostval authors (counted per author, Rostval would win: [Q27](/domains/research/questions/#Q27), [Q28](/domains/research/questions/#Q28)). The sonar paper (W02/W03) is cited by 7 works: author self-citations 2, University of Albury 2, the system 3, GB 4 ([Q29](/domains/research/questions/#Q29), [Q30](/domains/research/questions/#Q30)). Two hops from W01: W40 and W41, then W50, W51 and W52, with W51 citing both and a test record W90 left out ([Q31](/domains/research/questions/#Q31), [Q32](/domains/research/questions/#Q32)) |
| Local rules | [Q33](/domains/research/questions/#Q33) to [Q46](/domains/research/questions/#Q46), [Q48](/domains/research/questions/#Q48) | see below |

[Q7](/domains/research/questions/#Q7), [Q9](/domains/research/questions/#Q9), [Q11](/domains/research/questions/#Q11), [Q16](/domains/research/questions/#Q16) and [Q25](/domains/research/questions/#Q25) also depend on the local rules: they combine several traps.

### The local rules, and where the ontology states them

Each is stated only in the ontology, and none can be guessed from a code's name or from general conventions.

| Rule | Where it's stated | Questions |
|---|---|---|
| **STG records are test data.** Works with `record_source` STG (W90 to W92, at Kesting, by A21) describe no real work: they're ignored, with their authorships and the citations they make. With them, W22 would be Kesting's most-cited work (4 citations against W20's 3) | `res:origin-STG`; `res:Work` (condition 1); `res:Citation` | [Q33](/domains/research/questions/#Q33), [Q34](/domains/research/questions/#Q34) (also [Q11](/domains/research/questions/#Q11), [Q16](/domains/research/questions/#Q16), [Q25](/domains/research/questions/#Q25), [Q31](/domains/research/questions/#Q31)) |
| **SUP means supplement article, not supplementary material.** A peer-reviewed article in a supplement issue, counted like an article (W17, W24) | `res:wtype-SUP`; `res:Work` (condition 2) | [Q34](/domains/research/questions/#Q34), [Q35](/domains/research/questions/#Q35), [Q36](/domains/research/questions/#Q36) |
| **Only the affiliation listed last counts.** When an author gives several affiliations on one work, only the one with the highest `affil_seq` is credited. W70 lists Tessel and then Halloran, so it goes to Halloran; W71 lists Halloran and then Tessel, so it goes to Tessel | `res:affiliationSeq` (also `res:Authorship`, `res:country`) | [Q37](/domains/research/questions/#Q37), [Q38](/domains/research/questions/#Q38), [Q45](/domains/research/questions/#Q45) (also [Q9](/domains/research/questions/#Q9), [Q48](/domains/research/questions/#Q48)) |
| **Journal tiers count upwards, and K0 is a delisting.** K3 is the highest tier and K1 the lowest, the reverse of the natural guess. Works in a K0 source (W07, W75) aren't research output | `res:tier`, `res:tier-K3` to `res:tier-K0`; `res:Work` (condition 4) | [Q39](/domains/research/questions/#Q39), [Q40](/domains/research/questions/#Q40), [Q41](/domains/research/questions/#Q41) (tiers); [Q42](/domains/research/questions/#Q42), [Q43](/domains/research/questions/#Q43) (K0; also [Q7](/domains/research/questions/#Q7)) |
| **An affiliated institute (AFF) is not a unit of its parent.** Halloran's parent link records an agreement, so its works are never credited to the University of Albury or the system, and its ultimate parent is itself | `res:itype-AFF`; `res:Institution`; `res:parent` | [Q44](/domains/research/questions/#Q44), [Q45](/domains/research/questions/#Q45), [Q46](/domains/research/questions/#Q46) (also [Q9](/domains/research/questions/#Q9), [Q48](/domains/research/questions/#Q48)) |

The `executed` condition gets the tables `execute.py` writes:
- test records dropped;
- preprints merged into their published versions;
- each work flagged as research output or not;
- authors merged into people;
- one credited institution per person and work;
- the institution roll-ups;
- tiers ranked.
