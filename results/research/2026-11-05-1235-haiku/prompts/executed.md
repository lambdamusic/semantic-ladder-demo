<!-- system: You answer questions about a research-analytics dataset of works, authors, institutions, sources and citations. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

These tables are the data after its rules have been applied. Test records are gone. A preprint is merged into its published version (record_ids lists the records each work merges). research_output says whether a work counts as research output. Author records are merged into people (author_ids lists them). credits gives the one institution credited for each person on each work. institution_units lists every institution each institution's works count towards, itself included, with how many levels up. citations links merged works, and only from citing works that count. tier_rank ranks journal tiers, 1 the highest; a delisted source's works are not research output.

### works.csv
```csv
work_id,title,year,type,source_id,retracted,research_output,record_ids
W01,Adaptive path planning for underwater gliders,2021,ART,S01,false,yes,W01
W03,Drift-aware mapping with low-cost sonar,2023,ART,S02,false,yes,W02 W03
W04,Editorial: a new decade of marine autonomy,2023,EDT,S01,false,no,W04
W05,Erratum: Drift-aware mapping with low-cost sonar,2024,ERR,S02,false,no,W05
W06,Shoreline change detection from glider transects,2024,ART,S03,false,yes,W06
W07,Low-cost sonar arrays for coastal monitoring,2020,ART,S04,false,no,W07
W08,Turbulent wake modelling behind tidal turbines,2025,ART,S01,false,yes,W08
W09,Issue information,2023,PTX,S01,false,no,W09
W10,Front matter,2024,PTX,S02,false,no,W10
W12,Sonar mosaics from glider fleets,2024,ART,S02,false,yes,W12
W13,Fleet coordination for survey gliders,2024,ART,S01,false,yes,W13
W14,Harbour mapping with autonomous surface vessels,2025,ART,S03,false,yes,W14
W15,Low-cost sonar: a review,2025,REV,S02,false,yes,W15
W16,Sonar-based wake detection,2025,ART,S02,false,yes,W16
W17,Acoustic positioning near the shore,2024,SUP,S06,false,yes,W17
W18,Comparing sonar odometry methods,2022,PPR,S05,false,yes,W18
W19,Glider-borne turbidity sensing,2025,ART,S02,false,yes,W19
W20,Bed shear stress under breaking waves,2024,ART,S01,false,yes,W20
W21,A field campaign on tidal mixing,2024,ART,S02,false,yes,W21
W22,Turbulence closures for coastal models: a review,2024,REV,S03,false,yes,W22
W23,Anomalous dissipation in estuarine plumes,2023,ART,S02,true,no,W23
W24,Vortex shedding in shallow channels,2025,SUP,S06,false,yes,W24
W27,Sensor fusion for moored buoys,2024,ART,S03,false,yes,W27
W28,Calibration drift in conductivity sensors,2024,ART,S02,false,yes,W28
W29,Open hardware for ocean observation: a review,2024,REV,S01,false,yes,W29
W30,Tidal stream resource maps for the Dunmore coast,2019,ART,S03,false,yes,W30
W31,Machine-learned tidal forecasts,2023,ART,S01,false,yes,W31 W42
W32,Wave-current interaction over sandbars,2025,ART,S01,false,yes,W32
W33,Mixing efficiency in stratified tidal flows,2025,ART,S02,false,yes,W33
W34,Evaluating turbulence closures against flume data,2025,ART,S03,false,yes,W34
W35,Sediment resuspension by storms: a review,2025,REV,S02,false,yes,W35
W36,Shear and mixing in a macrotidal estuary,2025,ART,S03,false,yes,W36
W37,Port traffic and seabed disturbance,2022,ART,S03,false,yes,W37
W38,Seagrass mapping from aerial imagery,2023,ART,S02,false,yes,W38
W39,Replicating dissipation estimates in plumes,2024,ART,S03,false,yes,W39
W40,Energy budgets for long-range gliders,2022,ART,S02,false,yes,W40
W41,Path planning under uncertain currents,2023,ART,S03,false,yes,W41
W50,Battery ageing in autonomous platforms,2024,ART,S03,false,yes,W50
W51,Benchmarks for marine path planners,2024,ART,S02,false,yes,W51
W52,Route optimisation for ocean drones,2025,ART,S01,false,yes,W52
W60,Remote sensing of dune erosion,2020,ART,S08,false,yes,W60
W61,Uncertainty in marsh accretion estimates,2022,ART,S07,false,yes,W61
W62,Seasonal variability in dune erosion,2023,ART,S08,false,yes,W62
W63,Seasonal variability in sediment flux,2024,ART,S07,false,yes,W63
W64,Remote sensing of internal waves,2025,ART,S08,false,yes,W64
W65,Observations of dune erosion,2024,ART,S08,false,yes,W65
W66,Remote sensing of wave runup,2025,ART,S07,false,yes,W66
W67,Seasonal variability in tidal asymmetry,2023,ART,S08,false,yes,W67
W70,Optical backscatter in turbid estuaries,2023,ART,S02,false,yes,W70
W71,Low-power optical sensors for gliders,2024,ART,S01,false,yes,W71
W72,Integrating optical sensors on survey gliders,2024,ART,S03,false,yes,W72
W73,Saltmarsh retreat on the Halloran shore,2022,ART,S02,false,yes,W73
W74,Coastal squeeze and managed realignment: a review,2023,REV,S01,false,yes,W74
W75,Rip currents at tourist beaches,2023,ART,S04,false,no,W75
W76,Foreword to the Forum proceedings,2025,EDT,S06,false,no,W76
W101,Long-term trends in estuarine salinity,2019,ART,S08,false,yes,W101
W102,Long-term trends in dune erosion,2023,ART,S07,false,yes,W102
W103,A model of harbour seiches,2020,ART,S07,false,yes,W103
W104,Remote sensing of wave runup,2019,ART,S07,false,yes,W104
W105,Seasonal variability in harbour seiches,2021,ART,S08,false,yes,W105
W106,Seasonal variability in harbour seiches: a review,2022,REV,S07,false,yes,W106
W107,Observations of marsh accretion: a review,2019,REV,S08,false,yes,W107
W108,Seasonal variability in tidal asymmetry,2021,ART,S07,false,yes,W108
W109,A model of river plumes,2019,ART,S07,false,yes,W109
W110,Editorial: beach profiles,2021,EDT,S07,false,no,W110
W111,Observations of storm surge,2025,ART,S08,false,yes,W111
W112,Observations of tidal asymmetry,2020,ART,S07,false,yes,W112
W113,Seasonal variability in coastal upwelling,2021,ART,S07,false,yes,W113
W114,Observations of estuarine salinity,2019,ART,S08,false,yes,W114
W115,Remote sensing of internal waves: a review,2025,REV,S08,false,yes,W115
W116,A model of coastal upwelling,2022,ART,S08,false,yes,W116
W117,Uncertainty in beach profiles estimates,2024,ART,S08,false,yes,W117
W118,Long-term trends in internal waves,2025,ART,S07,false,yes,W118
W119,A model of internal waves,2019,ART,S08,false,yes,W119
W120,Remote sensing of tidal asymmetry: a review,2021,REV,S07,false,yes,W120
W121,Long-term trends in internal waves,2024,ART,S08,false,yes,W121
W122,Observations of storm surge,2025,ART,S08,false,yes,W122
W123,Editorial: river plumes,2023,EDT,S08,false,no,W123
W124,A model of coastal upwelling,2019,ART,S08,false,yes,W124
W125,Remote sensing of sediment flux,2024,ART,S08,false,yes,W125
```

### people.csv
```csv
person_id,name,orcid,author_ids
A01,Mara Ellison,0000-0002-9841-6229,A01 A02 A03
A04,M. Ellison,0000-0004-8662-8360,A04
A05,Jonas Brandt,0000-0001-6105-5008,A05
A06,Jonas Brandt,0000-0007-5475-1779,A06
A07,Priya Ramanathan,0000-0009-2298-3695,A07
A08,Tomasz Wierzba,0000-0007-9318-6032,A08
A09,Lena Vossberg,0000-0000-8073-7028,A09
A10,Dirk Hallmann,0000-0003-8222-6468,A10
A11,Sofie de Raat,0000-0006-1642-5247,A11
A12,Pieter Maas,0000-0007-6472-5877,A12
A13,Claire Fontanet,0000-0001-8841-3301,A13
A14,Hugo Marchetti,0000-0007-5682-0525,A14
A15,Aisha Okonjo,0000-0008-9831-9489,A15
A16,Rhys Calloway,,A16
A17,Ingrid Solberg,0000-0003-9494-8214,A17
A18,Bram Kuipers,0000-0001-6210-5218,A18
A19,Femke Hoogeveen,0000-0005-4914-5244,A19
A20,Joost Verhaar,0000-0001-0646-0013,A20
A21,Petra Lindqvist,0000-0000-4118-9557,A21
A22,Niamh Corrigan,0000-0009-9065-9397,A22
A30,Ana Aranda,0000-0006-1584-6450,A30
A31,Ben Fujimura,0000-0006-0454-1465,A31
A32,Chiara Kincaid,0000-0009-0853-8012,A32
A33,Daichi Pruitt,0000-0009-1102-8594,A33
A34,Elif Esposito,0000-0000-6925-6663,A34
A35,Felipe Jaramillo,0000-0006-3228-0886,A35
A36,Grace Olmedo,0000-0004-2300-4876,A36
A37,Haruto Dorsey,0000-0004-5291-2808,A37
A38,Ines Ishida,0000-0004-5850-0370,A38
A39,Julien Nakagawa,0000-0003-8265-3845,A39
A40,Kai Carver,0000-0003-5577-8794,A40
A41,Lucia Hartwell,0000-0003-2627-0586,A41
A42,Mateo Morrow,0000-0000-2145-8421,A42
A43,Noor Beaulieu,0000-0000-8394-9066,A43
A44,Oscar Galvez,0000-0008-8281-1265,A44
A45,Paula Lefebvre,0000-0008-4409-3244,A45
```

### credits.csv
```csv
work_id,person_id,institution_id
W01,A01,I02
W01,A07,I03
W03,A01,I02
W03,A07,I03
W04,A01,I02
W05,A01,I02
W05,A07,I03
W06,A01,I02
W06,A15,I13
W07,A01,I02
W08,A04,I07
W12,A01,I02
W12,A16,I05
W13,A07,I03
W14,A05,I05
W15,A15,I13
W16,A04,I07
W17,A13,I11
W18,A11,I09
W19,A01,I02
W20,A09,I07
W20,A13,I11
W21,A09,I07
W21,A10,I08
W21,A11,I09
W21,A12,I10
W22,A09,I07
W23,A09,I07
W24,A10,I08
W27,A13,I11
W27,A14,I12
W27,A17,I14
W27,A18,I09
W28,A06,I12
W28,A15,I13
W28,A16,I05
W28,A19,I09
W29,A13,I11
W29,A15,I13
W29,A16,I05
W29,A20,I09
W30,A15,I13
W31,A17,I14
W32,A11,I09
W32,A18,I09
W32,A19,I09
W32,A20,I09
W33,A14,I12
W34,A06,I12
W35,A14,I12
W36,A13,I11
W37,A05,I05
W38,A06,I12
W39,A17,I14
W40,A11,I09
W41,A14,I12
W50,A17,I14
W51,A12,I10
W52,A13,I11
W60,A34,I15
W61,A35,I16
W61,A38,I15
W62,A34,I15
W62,A38,I15
W63,A33,I18
W63,A34,I15
W63,A44,I17
W64,A40,I17
W65,A35,I16
W65,A36,I17
W65,A45,I18
W66,A38,I15
W67,A35,I16
W67,A45,I18
W70,A08,I06
W71,A08,I04
W72,A07,I03
W72,A08,I04
W73,A08,I06
W74,A22,I06
W75,A15,I13
W101,A30,I15
W101,A42,I15
W102,A36,I17
W102,A38,I15
W102,A42,I15
W103,A34,I15
W103,A35,I16
W103,A41,I18
W104,A37,I18
W104,A44,I17
W104,A45,I18
W105,A31,I16
W105,A40,I17
W106,A38,I15
W106,A45,I18
W107,A32,I17
W107,A43,I16
W108,A34,I15
W108,A35,I16
W108,A42,I15
W109,A36,I17
W109,A42,I15
W109,A43,I16
W110,A34,I15
W111,A34,I15
W112,A44,I17
W112,A45,I18
W113,A32,I17
W113,A43,I16
W114,A35,I16
W114,A38,I15
W114,A42,I15
W115,A35,I16
W116,A43,I16
W116,A44,I17
W117,A36,I17
W118,A35,I16
W119,A36,I17
W119,A41,I18
W120,A37,I18
W121,A32,I17
W121,A37,I18
W122,A32,I17
W123,A30,I15
W123,A38,I15
W123,A45,I18
W124,A31,I16
W125,A36,I17
W125,A37,I18
```

### institutions.csv
```csv
institution_id,name,ror,country,type,parent_id
I01,Albury University System,0hygr4985,GB,SYS,
I02,University of Albury,06safhw22,GB,UNI,I01
I03,Albury Centre for Marine Robotics,06a9yq342,GB,LAB,I02
I04,Tessel Laboratory for Ocean Sensing,0002ezf81,GB,LAB,I03
I05,Albury Metropolitan University,0ww7kxb57,GB,UNI,I01
I06,Halloran Institute for Coastal Studies,0175f3924,GB,AFF,I02
I07,Kesting University,0593t4875,DE,UNI,
I08,Kesting Institute of Hydrodynamics,0brjdg570,DE,LAB,I07
I09,Rostval Technical University,0k8rh7879,NL,UNI,
I10,Marrow Instruments BV,0t3x83535,NL,CO,
I11,Brevin Ocean Agency,0wvack776,FR,GOV,
I12,Université de Lorvain,091pt9775,FR,UNI,
I13,Dunmore College,095cwy722,GB,UNI,
I14,Oskel Polytechnic,06t6n5818,NL,UNI,
I15,Carrow State University,0v91gp428,US,UNI,
I16,Hoshimine Institute of Technology,06afa6f88,JP,UNI,
I17,Université de Mallois,0pshcv029,CA,UNI,
I18,Universidad de Ventolera,0ay9jr885,ES,UNI,
```

### institution_units.csv
```csv
institution_id,counts_towards,levels_up
I01,I01,0
I02,I02,0
I02,I01,1
I03,I03,0
I03,I02,1
I03,I01,2
I04,I04,0
I04,I03,1
I04,I02,2
I04,I01,3
I05,I05,0
I05,I01,1
I06,I06,0
I07,I07,0
I08,I08,0
I08,I07,1
I09,I09,0
I10,I10,0
I11,I11,0
I12,I12,0
I13,I13,0
I14,I14,0
I15,I15,0
I16,I16,0
I17,I17,0
I18,I18,0
```

### sources.csv
```csv
source_id,name,issn,type,tier,tier_rank,delisted
S01,Journal of Marine Autonomy,9866-3925,JOU,K3,1,no
S02,Ocean Sensing Letters,3195-4973,JOU,K2,2,no
S03,Coastal Engineering Review,1154-9679,JOU,K1,3,no
S04,Global Marine Science Reports,8864-5325,JOU,K0,,yes
S05,OceanArXiv,,REP,,,no
S06,Proceedings of the Hydrodynamics Forum,9804-2748,JOU,K2,2,no
S07,Journal of Estuarine Dynamics,1483-2835,JOU,K2,2,no
S08,Hydrology Notes,9832-2482,JOU,K1,3,no
```

### citations.csv
```csv
citing_work_id,cited_work_id
W12,W03
W13,W03
W14,W03
W15,W03
W16,W03
W17,W03
W18,W03
W32,W20
W33,W21
W34,W22
W35,W20
W36,W20
W36,W21
W39,W23
W40,W01
W41,W01
W50,W40
W51,W40
W51,W41
W52,W41
W60,W30
W61,W30
W62,W30
W62,W31
W63,W30
W64,W30
W65,W31
W66,W31
W67,W31
W103,W101
W103,W60
W104,W101
W105,W60
W106,W104
W106,W61
W107,W101
W107,W104
W108,W101
W108,W104
W108,W60
W109,W101
W109,W104
W110,W60
W111,W104
W111,W107
W111,W64
W113,W110
W114,W104
W115,W114
W116,W104
W118,W106
W118,W66
W119,W109
W119,W114
W120,W108
W120,W112
W121,W112
W121,W113
W123,W101
W123,W60
W124,W101
W124,W107
W124,W114
W125,W105
W125,W108
W125,W61
```

## Questions

Answer each question below from the data above. Start each answer on a new line with its
number in bold, like **Q1.**, give the direct answer first, then at most two sentences of
reasoning that cite the records (IDs) you relied on.

Then end with one JSON block (```json) holding the structured answer to each question listed
here, with exactly these fields, shaped like {"Q1": {"field": value}, ...}. Name works, authors, institutions and sources by their record ID: the work_id, author_id, institution_id or source_id in the CSV files, or the part of the IRI after res: in the RDF (W01, A07, I02, S03; not their titles or names).

- Q1: count (a number)
- Q2: works (a list of record IDs)
- Q3: same ("yes", "no" or "depends")
- Q4: count (a number)
- Q5: same ("yes", "no" or "depends")
- Q6: author (a record ID)
- Q7: count (a number)
- Q8: parent (a record ID)
- Q9: count (a number)
- Q10: count (a number)
- Q11: count (a number)
- Q12: full (a number), fractional (a number)
- Q13: full (a record ID), fractional (a record ID)
- Q14: full (a number), fractional (a number)
- Q15: count (a number)
- Q16: count (a number)
- Q17: works (a list of record IDs)
- Q18: count (a number)
- Q19: count (a number)
- Q20: works (a list of record IDs)
- Q21: count (a number)
- Q22: more_in_total (a record ID), more_in_window (a record ID)
- Q23: total (a number), in_window (a number)
- Q24: count (a number)
- Q25: count (a number)
- Q26: counts ("yes", "no" or "depends")
- Q27: institution (a record ID), citing_works (a number)
- Q28: count (a number)
- Q29: author (a number), institution (a number), country (a number)
- Q30: count (a number)
- Q31: works (a list of record IDs)
- Q32: count (a number)
- Q33: work (a record ID)
- Q34: count (a number)
- Q35: count (a number)
- Q36: count (a number)
- Q37: institution (a record ID)
- Q38: institutions (a list of record IDs)
- Q39: count (a number)
- Q40: source (a record ID)
- Q41: higher ("yes", "no" or "depends")
- Q42: count (a number)
- Q43: research ("yes", "no" or "depends")
- Q44: institutions (a list of record IDs)
- Q45: count (a number)
- Q46: parent (a record ID)

Q1. How many distinct people do the author records named "Mara Ellison", "M. Ellison" and "Ellison, Mara J." stand for?
Q2. List every work, of any type, that Mara Ellison (A01) is an author of.
Q3. Is the Jonas Brandt who wrote W37 the same person as the Jonas Brandt who wrote W38?
Q4. How many research works has the Jonas Brandt of Albury Metropolitan University (A05) authored?
Q5. Is the M. Ellison who wrote W08 the same person as the Mara Ellison who wrote W01?
Q6. Which author has the most research works credited to the University of Albury, its units included?
Q7. How many research works has Mara Ellison authored?
Q8. What is the ultimate parent of the Tessel Laboratory for Ocean Sensing (I04)?
Q9. How many research works is the University of Albury (I02) credited with, its units included?
Q10. How many research works is the Albury University System (I01) credited with, all its units included?
Q11. How many research works is Kesting University (I07) credited with, its units included?
Q12. How many research works did Kesting University (I07, units included) publish in 2024, under full counting and under fractional counting (each work split equally among its authors)?
Q13. In 2024, which had more research works, Kesting University (I07) or Rostval Technical University (I09): under full counting, and under fractional counting?
Q14. How many research works did GB institutions publish in 2024, under full counting and under fractional counting (each work split equally among its authors, each author's share going to their institution's country)?
Q15. How many research works appeared in Ocean Sensing Letters (S02) in 2024?
Q16. How many research works appeared in the Journal of Marine Autonomy (S01)?
Q17. Which of Mara Ellison's works are not research output because of their document type?
Q18. How many distinct research works has Priya Ramanathan (A07) authored?
Q19. How many distinct works cite "Drift-aware mapping with low-cost sonar", in either of its versions?
Q20. Which works in the data are preprints of another work that is also in the data?
Q21. How many research works is Oskel Polytechnic (I14) credited with?
Q22. Which has more citations, W30 or W31 (counting both versions of each): in total, and within its publication year and the two years after?
Q23. How many citations has W30 received in total, and how many within its publication year and the two years after?
Q24. How many research works has Lena Vossberg (A09) authored?
Q25. What is the total of the citation counts of Lena Vossberg's research works?
Q26. Does W23 count towards Kesting University's research output?
Q27. Which other institution's works cite Kesting University's research works the most, each citing work counted once per institution, and how many of its works do?
Q28. How many distinct works from Rostval Technical University (I09) cite Kesting University's research works?
Q29. Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of authors, of the University of Albury (units included), and of countries?
Q30. Of the works citing "Drift-aware mapping with low-cost sonar" (either version), how many are self-citations at the level of the Albury University System?
Q31. Which works cite at least one of the works that cite W01?
Q32. How many distinct works are within two citation hops of W01 (citing it, or citing a work that cites it)?
Q33. Which of Kesting University's research works has the most citations?
Q34. How many research works was Kesting University (units included) credited with in 2025?
Q35. How many research works is the Kesting Institute of Hydrodynamics (I08) credited with?
Q36. How many research works appeared in the Proceedings of the Hydrodynamics Forum (S06)?
Q37. Which institution is W70 credited to?
Q38. Which institutions is W71 credited to, at every level?
Q39. How many of the University of Albury's research works (units included) appeared in a source of the highest tier?
Q40. Which source is in the highest tier?
Q41. Is Coastal Engineering Review (S03) in a higher tier than Ocean Sensing Letters (S02)?
Q42. How many research works appeared in Global Marine Science Reports (S04)?
Q43. Is W07 research output?
Q44. Which institutions are part of the Albury University System, at any level below it?
Q45. How many research works is the Halloran Institute for Coastal Studies (I06) credited with?
Q46. What is the ultimate parent of the Halloran Institute for Coastal Studies (I06)?
Q47. Why do Kesting University and Rostval Technical University swap places in 2024 between full and fractional counting?
Q48. Why is W70 not one of the University of Albury's research works, though its author lists the Tessel Laboratory?
