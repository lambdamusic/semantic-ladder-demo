<!-- system: You answer questions about a research-analytics dataset of works, authors, institutions, sources and citations. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

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
I19,Albury Laboratory for Acoustic Imaging,0xe2n1515,GB,LAB,I02
I20,Albury Metropolitan Centre for Port Studies,0bp5b1111,GB,LAB,I05
I21,Wexcombe Institute for Estuary Research,0ms1zdt74,GB,AFF,I05
I22,Sandhaven Institute for Wave Research,0rn08b412,DE,AFF,I07
I23,Rostval Laboratory for Offshore Structures,0zekfva10,NL,LAB,I09
I24,Pellmore University,0n0j86p46,US,UNI,
I25,Università di Calvessa,08mz9rf83,IT,UNI,
I26,Tarnowa University of Technology,0189z6431,PL,UNI,
I27,Kirrabay University,0wam41j64,AU,UNI,
I28,Nordvik University,00etvqe29,NO,UNI,
I29,Hanseo Ocean Institute,0g18r1r20,KR,GOV,
I30,Universidade de Arvela,0ha4xax60,PT,UNI,
I31,Corrimal Marine Systems Inc,0nq63kw54,US,CO,
```

### authors.csv
```csv
author_id,name,orcid
A01,Mara Ellison,0000-0002-9841-6229
A02,M. Ellison,0000-0002-9841-6229
A03,"Ellison, Mara J.",0000-0002-9841-6229
A04,M. Ellison,0000-0004-8662-8360
A05,Jonas Brandt,0000-0001-6105-5008
A06,Jonas Brandt,0000-0007-5475-1779
A07,Priya Ramanathan,0000-0009-2298-3695
A08,Tomasz Wierzba,0000-0007-9318-6032
A09,Lena Vossberg,0000-0000-8073-7028
A10,Dirk Hallmann,0000-0003-8222-6468
A11,Sofie de Raat,0000-0006-1642-5247
A12,Pieter Maas,0000-0007-6472-5877
A13,Claire Fontanet,0000-0001-8841-3301
A14,Hugo Marchetti,0000-0007-5682-0525
A15,Aisha Okonjo,0000-0008-9831-9489
A16,Rhys Calloway,
A17,Ingrid Solberg,0000-0003-9494-8214
A18,Bram Kuipers,0000-0001-6210-5218
A19,Femke Hoogeveen,0000-0005-4914-5244
A20,Joost Verhaar,0000-0001-0646-0013
A21,Petra Lindqvist,0000-0000-4118-9557
A22,Niamh Corrigan,0000-0009-9065-9397
A30,Ana Aranda,0000-0006-1584-6450
A31,Ben Fujimura,0000-0006-0454-1465
A32,Chiara Kincaid,0000-0009-0853-8012
A33,Daichi Pruitt,0000-0009-1102-8594
A34,Elif Esposito,0000-0000-6925-6663
A35,Felipe Jaramillo,0000-0006-3228-0886
A36,Grace Olmedo,0000-0004-2300-4876
A37,Haruto Dorsey,0000-0004-5291-2808
A38,Ines Ishida,0000-0004-5850-0370
A39,Julien Nakagawa,0000-0003-8265-3845
A40,Kai Carver,0000-0003-5577-8794
A41,Lucia Hartwell,0000-0003-2627-0586
A42,Mateo Morrow,0000-0000-2145-8421
A43,Noor Beaulieu,0000-0000-8394-9066
A44,Oscar Galvez,0000-0008-8281-1265
A45,Paula Lefebvre,0000-0008-4409-3244
A101,M. Ellison,0000-0002-9841-6229
A102,M. Ellison,0000-0008-4738-8328
A103,L. Vossberg,0000-0000-8073-7028
A104,J. Brandt,0000-0001-6105-5008
A105,Jonas Brandt,0000-0004-9046-7961
A106,T. Wierzba,0000-0007-9318-6032
A107,S. de Raat,0000-0006-1642-5247
A108,Priya Ramanathan,0000-0007-1802-8393
A109,Greta Yelland,0000-0002-6545-4969
A110,Quinn Yelland,0000-0003-7597-9990
A111,Hester Falconer,0000-0007-5409-8704
A112,Katrin Elphick,0000-0008-6293-8407
A113,Henrik Corbridge,0000-0001-7569-4541
A114,Ivo Brockmann,0000-0009-9653-9901
A115,Tamsin Vandersloot,0000-0008-5622-7508
A116,Emrys Bellamore,0000-0001-3732-2664
A117,Viggo Bellamore,0000-0002-5926-5216
A118,Dorian Bellamore,0000-0000-4633-9010
A119,Jarno Quarrie,0000-0009-8605-0541
A120,Linus Haverkamp,0000-0000-3133-9422
A121,Marit Sallis,0000-0001-8432-2588
A122,Katrin Dannecker,0000-0005-9430-8644
A123,Florin Penhallow,0000-0008-6186-9535
A124,Niko Vandersloot,0000-0008-3786-7418
A125,Greta Ostergaard,0000-0002-5410-0810
A126,Yara Quarrie,0000-0002-3972-8364
A127,Delphine Ashdown,0000-0000-5148-3260
A128,Jarno Tregunna,
A129,Delphine Ibbotson,0000-0000-6389-2468
A130,Tamsin Castellan,0000-0004-8526-1242
A131,Emrys Nordahl,0000-0000-3843-6782
A132,Linus Penhallow,0000-0000-9780-0868
A133,Liesel Lachance,0000-0003-1768-1087
A134,Silas Castellan,0000-0003-3481-4429
A135,Olwen Quarrie,0000-0001-4750-0051
A136,Jolien Haverkamp,0000-0009-6519-3014
A137,Olwen Uttley,0000-0006-0842-6639
A138,Olwen Whitcombe,0000-0008-9432-6799
A139,Odile Tregunna,0000-0002-2495-1719
A140,Jolien Bellamore,0000-0009-0548-3869
A141,Delphine Bellamore,0000-0003-0209-4519
A142,Greta Rademaker,0000-0009-9961-6216
A143,Marit Ibbotson,0000-0009-8383-5608
A144,Silas Ashdown,0000-0007-8521-8973
A145,Ivo Corbridge,0000-0006-1367-0053
A146,Cosimo Bellamore,0000-0002-3308-6027
A147,Niko Uttley,0000-0009-7757-5966
A148,Kester Aldous,0000-0004-3203-0789
A149,Liesel Whitcombe,0000-0008-7432-0373
A150,Yara Castellan,0000-0006-4842-1959
A151,Elsa Penhallow,0000-0008-1093-6341
A152,Florin Whitcombe,
A153,Emrys Merriman,0000-0008-9865-6168
A154,Henrik Lachance,0000-0000-6078-6579
A155,Delphine Dewhurst,
A156,Greta Elphick,0000-0000-1295-1089
A157,Dorian Falconer,0000-0009-2170-6438
A158,Kester Jansma,0000-0009-6522-6126
A159,Wren Whitcombe,0000-0009-7906-1807
A160,Kester Zandvoort,0000-0006-9930-9118
A161,Jolien Dewhurst,0000-0005-3613-9857
A162,Liesel Ibbotson,0000-0007-2655-6310
A163,Nils Jansma,0000-0004-7426-1752
A164,Silas Corbridge,0000-0001-8029-9865
A165,Niko Penhallow,0000-0002-5295-8953
A166,Henrik Sallis,0000-0003-9677-7161
A167,Henrik Haverkamp,0000-0007-4485-0931
A168,Henrik Yelland,0000-0001-2141-4246
A169,Ulla Haverkamp,0000-0000-8586-5161
A170,Bastian Ashdown,0000-0005-3547-5180
A171,Ulla Aldous,0000-0005-5058-4742
A172,Hester Aldous,0000-0009-3776-6819
A173,Fenna Uttley,0000-0000-4008-7950
A174,Tamsin Gisborne,0000-0004-4300-1807
A175,Jarno Whitcombe,0000-0000-2155-5864
A176,Yara Dewhurst,0000-0004-7256-8312
A177,Carys Uttley,0000-0008-3085-0372
A178,Elsa Merriman,
A179,Alba Ashdown,0000-0001-5735-1490
A180,Ilse Aldous,0000-0002-8044-9596
A181,Henrik Kerridge,0000-0009-5689-0994
A182,Ulla Penhallow,0000-0003-2191-4747
A183,Bastian Kerridge,0000-0007-6448-2483
A184,Odile Ashdown,
A185,Olwen Ostergaard,0000-0005-9437-0650
A186,Carys Tregunna,0000-0002-3962-9717
A187,Jolien Aldous,0000-0002-8271-6177
A188,Bastian Tregunna,
A189,Zeno Aldous,0000-0006-2989-6155
A190,Maelle Ashdown,0000-0009-5279-0424
A191,Silas Zandvoort,0000-0005-2590-0644
A192,Pim Aldous,0000-0002-0569-8605
A193,Niko Yelland,
A194,Alba Corbridge,0000-0001-5776-4679
A195,Yara Penhallow,0000-0003-6890-9836
A196,Fenna Gisborne,0000-0008-9819-5281
A197,Maelle Brockmann,0000-0005-2578-6292
A198,Jarno Ashdown,0000-0001-4780-0378
A199,Delphine Merriman,0000-0005-5487-7183
A200,Ivo Penhallow,0000-0000-9986-0432
A201,Hester Dewhurst,0000-0002-8179-0448
A202,Marit Ostergaard,0000-0007-5698-5981
A203,Jolien Quarrie,0000-0007-9816-0934
A204,Katrin Kerridge,0000-0002-0159-1367
A205,Yara Lachance,
A206,Olwen Yelland,
A207,Maelle Dannecker,0000-0007-9373-7702
A208,Liesel Jansma,0000-0005-1693-8254
A209,Jolien Kerridge,0000-0001-6525-8467
A210,Ilse Bellamore,
A211,Ivo Rademaker,0000-0002-7687-0223
A212,Jarno Elphick,0000-0006-5440-8972
A213,Odile Whitcombe,0000-0003-3309-8851
A214,Anouk Castellan,0000-0005-5240-8672
A215,Zeno Dannecker,0000-0008-4772-3832
A216,Nils Rademaker,0000-0001-3498-1824
A217,Odile Rademaker,0000-0009-2609-6797
A218,Bryony Jansma,0000-0003-3146-5873
A219,Bryony Jansma,0000-0002-4103-1118
A220,Hester Ostergaard,0000-0008-3455-9598
A221,Hester Ostergaard,0000-0003-8085-8585
A222,Liesel Aldous,0000-0009-2600-3022
A223,Liesel Aldous,0000-0008-4203-7095
A224,Ilse Eberhardt,0000-0009-6534-9320
A225,Ilse Eberhardt,0000-0000-0712-5619
A226,Cosimo Penhallow,0000-0000-1869-5361
A227,Cosimo Penhallow,0000-0008-9935-6581
A228,Gideon Yelland,0000-0009-3500-8530
A229,Gideon Yelland,0000-0003-6264-2564
```

### sources.csv
```csv
source_id,name,issn,type,tier
S01,Journal of Marine Autonomy,9866-3925,JOU,K3
S02,Ocean Sensing Letters,3195-4973,JOU,K2
S03,Coastal Engineering Review,1154-9679,JOU,K1
S04,Global Marine Science Reports,8864-5325,JOU,K0
S05,OceanArXiv,,REP,
S06,Proceedings of the Hydrodynamics Forum,9804-2748,JOU,K2
S07,Journal of Estuarine Dynamics,1483-2835,JOU,K2
S08,Hydrology Notes,9832-2482,JOU,K1
S09,Journal of Coastal Hydraulics,3431-7424,JOU,K2
S10,Marine Technology Bulletin,7809-8515,JOU,K1
S11,Annals of Ocean Observation,8324-8964,JOU,K2
S12,Shelf Sea Letters,8103-2767,JOU,K1
S13,International Journal of Ocean Frontiers,1765-9671,JOU,K0
S14,CoastRxiv,,REP,
```

### works.csv
```csv
work_id,title,year,type,source_id,doi,version_of,is_retracted,record_source
W01,Adaptive path planning for underwater gliders,2021,ART,S01,10.55555/s01.2021.1465,,false,FEED
W02,Drift-aware mapping with low-cost sonar,2022,PPR,S05,10.55555/s05.2022.2911,W03,false,FEED
W03,Drift-aware mapping with low-cost sonar,2023,ART,S02,10.55555/s02.2023.9437,,false,FEED
W04,Editorial: a new decade of marine autonomy,2023,EDT,S01,10.55555/s01.2023.1032,,false,FEED
W05,Erratum: Drift-aware mapping with low-cost sonar,2024,ERR,S02,10.55555/s02.2024.7136,,false,FEED
W06,Shoreline change detection from glider transects,2024,ART,S03,10.55555/s03.2024.2042,,false,FEED
W07,Low-cost sonar arrays for coastal monitoring,2020,ART,S04,10.55555/s04.2020.7029,,false,FEED
W08,Turbulent wake modelling behind tidal turbines,2025,ART,S01,10.55555/s01.2025.5958,,false,FEED
W09,Issue information,2023,PTX,S01,10.55555/s01.2023.4542,,false,FEED
W10,Front matter,2024,PTX,S02,10.55555/s02.2024.9718,,false,FEED
W12,Sonar mosaics from glider fleets,2024,ART,S02,10.55555/s02.2024.3526,,false,CRIS
W13,Fleet coordination for survey gliders,2024,ART,S01,10.55555/s01.2024.5065,,false,FEED
W14,Harbour mapping with autonomous surface vessels,2025,ART,S03,10.55555/s03.2025.3072,,false,FEED
W15,Low-cost sonar: a review,2025,REV,S02,10.55555/s02.2025.2741,,false,FEED
W16,Sonar-based wake detection,2025,ART,S02,10.55555/s02.2025.6345,,false,FEED
W17,Acoustic positioning near the shore,2024,SUP,S06,10.55555/s06.2024.8939,,false,FEED
W18,Comparing sonar odometry methods,2022,PPR,S05,10.55555/s05.2022.2759,,false,FEED
W19,Glider-borne turbidity sensing,2025,ART,S02,10.55555/s02.2025.2198,,false,CRIS
W20,Bed shear stress under breaking waves,2024,ART,S01,10.55555/s01.2024.7245,,false,FEED
W21,A field campaign on tidal mixing,2024,ART,S02,10.55555/s02.2024.5301,,false,FEED
W22,Turbulence closures for coastal models: a review,2024,REV,S03,10.55555/s03.2024.5939,,false,FEED
W23,Anomalous dissipation in estuarine plumes,2023,ART,S02,10.55555/s02.2023.2925,,true,FEED
W24,Vortex shedding in shallow channels,2025,SUP,S06,10.55555/s06.2025.6698,,false,FEED
W27,Sensor fusion for moored buoys,2024,ART,S03,10.55555/s03.2024.8772,,false,FEED
W28,Calibration drift in conductivity sensors,2024,ART,S02,10.55555/s02.2024.9171,,false,FEED
W29,Open hardware for ocean observation: a review,2024,REV,S01,10.55555/s01.2024.2981,,false,FEED
W30,Tidal stream resource maps for the Dunmore coast,2019,ART,S03,10.55555/s03.2019.9502,,false,FEED
W31,Machine-learned tidal forecasts,2023,ART,S01,10.55555/s01.2023.5047,,false,FEED
W32,Wave-current interaction over sandbars,2025,ART,S01,10.55555/s01.2025.8470,,false,FEED
W33,Mixing efficiency in stratified tidal flows,2025,ART,S02,10.55555/s02.2025.6654,,false,FEED
W34,Evaluating turbulence closures against flume data,2025,ART,S03,10.55555/s03.2025.2352,,false,FEED
W35,Sediment resuspension by storms: a review,2025,REV,S02,10.55555/s02.2025.2131,,false,FEED
W36,Shear and mixing in a macrotidal estuary,2025,ART,S03,10.55555/s03.2025.2439,,false,FEED
W37,Port traffic and seabed disturbance,2022,ART,S03,10.55555/s03.2022.9107,,false,FEED
W38,Seagrass mapping from aerial imagery,2023,ART,S02,10.55555/s02.2023.6112,,false,FEED
W39,Replicating dissipation estimates in plumes,2024,ART,S03,10.55555/s03.2024.5346,,false,FEED
W40,Energy budgets for long-range gliders,2022,ART,S02,10.55555/s02.2022.4703,,false,FEED
W41,Path planning under uncertain currents,2023,ART,S03,10.55555/s03.2023.3758,,false,FEED
W42,Machine-learned tidal forecasts,2023,PPR,S05,10.55555/s05.2023.6876,W31,false,FEED
W50,Battery ageing in autonomous platforms,2024,ART,S03,10.55555/s03.2024.6324,,false,FEED
W51,Benchmarks for marine path planners,2024,ART,S02,10.55555/s02.2024.8087,,false,FEED
W52,Route optimisation for ocean drones,2025,ART,S01,10.55555/s01.2025.9294,,false,FEED
W60,Remote sensing of dune erosion,2020,ART,S08,10.55555/s08.2020.8236,,false,FEED
W61,Uncertainty in marsh accretion estimates,2022,ART,S07,10.55555/s07.2022.2930,,false,FEED
W62,Seasonal variability in dune erosion,2023,ART,S08,10.55555/s08.2023.5393,,false,FEED
W63,Seasonal variability in sediment flux,2024,ART,S07,10.55555/s07.2024.8504,,false,FEED
W64,Remote sensing of internal waves,2025,ART,S08,10.55555/s08.2025.7711,,false,FEED
W65,Observations of dune erosion,2024,ART,S08,10.55555/s08.2024.6414,,false,FEED
W66,Remote sensing of wave runup,2025,ART,S07,10.55555/s07.2025.5131,,false,FEED
W67,Seasonal variability in tidal asymmetry,2023,ART,S08,10.55555/s08.2023.1192,,false,FEED
W70,Optical backscatter in turbid estuaries,2023,ART,S02,10.55555/s02.2023.6434,,false,FEED
W71,Low-power optical sensors for gliders,2024,ART,S01,10.55555/s01.2024.6287,,false,FEED
W72,Integrating optical sensors on survey gliders,2024,ART,S03,10.55555/s03.2024.9080,,false,FEED
W73,Saltmarsh retreat on the Halloran shore,2022,ART,S02,10.55555/s02.2022.7603,,false,CRIS
W74,Coastal squeeze and managed realignment: a review,2023,REV,S01,10.55555/s01.2023.6139,,false,FEED
W75,Rip currents at tourist beaches,2023,ART,S04,10.55555/s04.2023.3895,,false,FEED
W76,Foreword to the Forum proceedings,2025,EDT,S06,10.55555/s06.2025.4219,,false,FEED
W90,Sediment transport in tidal inlets,2025,ART,S02,10.55555/s02.2025.8585,,false,STG
W91,Closure models for wave boundary layers,2025,ART,S01,10.55555/s01.2025.4607,,false,STG
W92,Coastal turbulence: a review,2025,REV,S03,10.55555/s03.2025.6710,,false,STG
W101,Long-term trends in estuarine salinity,2019,ART,S08,10.55555/s08.2019.4427,,false,FEED
W102,Long-term trends in dune erosion,2023,ART,S07,10.55555/s07.2023.1186,,false,FEED
W103,A model of harbour seiches,2020,ART,S07,10.55555/s07.2020.2380,,false,FEED
W104,Remote sensing of wave runup,2019,ART,S07,10.55555/s07.2019.6591,,false,FEED
W105,Seasonal variability in harbour seiches,2021,ART,S08,10.55555/s08.2021.9028,,false,FEED
W106,Seasonal variability in harbour seiches: a review,2022,REV,S07,10.55555/s07.2022.7552,,false,FEED
W107,Observations of marsh accretion: a review,2019,REV,S08,10.55555/s08.2019.9349,,false,FEED
W108,Seasonal variability in tidal asymmetry,2021,ART,S07,10.55555/s07.2021.9650,,false,FEED
W109,A model of river plumes,2019,ART,S07,10.55555/s07.2019.5434,,false,FEED
W110,Editorial: beach profiles,2021,EDT,S07,10.55555/s07.2021.3358,,false,FEED
W111,Observations of storm surge,2025,ART,S08,10.55555/s08.2025.5383,,false,FEED
W112,Observations of tidal asymmetry,2020,ART,S07,10.55555/s07.2020.9946,,false,FEED
W113,Seasonal variability in coastal upwelling,2021,ART,S07,10.55555/s07.2021.6316,,false,FEED
W114,Observations of estuarine salinity,2019,ART,S08,10.55555/s08.2019.1460,,false,FEED
W115,Remote sensing of internal waves: a review,2025,REV,S08,10.55555/s08.2025.4950,,false,FEED
W116,A model of coastal upwelling,2022,ART,S08,10.55555/s08.2022.6950,,false,FEED
W117,Uncertainty in beach profiles estimates,2024,ART,S08,10.55555/s08.2024.4202,,false,FEED
W118,Long-term trends in internal waves,2025,ART,S07,10.55555/s07.2025.4335,,false,FEED
W119,A model of internal waves,2019,ART,S08,10.55555/s08.2019.1156,,false,FEED
W120,Remote sensing of tidal asymmetry: a review,2021,REV,S07,10.55555/s07.2021.6881,,false,FEED
W121,Long-term trends in internal waves,2024,ART,S08,10.55555/s08.2024.8676,,false,FEED
W122,Observations of storm surge,2025,ART,S08,10.55555/s08.2025.1686,,false,FEED
W123,Editorial: river plumes,2023,EDT,S08,10.55555/s08.2023.3508,,false,FEED
W124,A model of coastal upwelling,2019,ART,S08,10.55555/s08.2019.2165,,false,FEED
W125,Remote sensing of sediment flux,2024,ART,S08,10.55555/s08.2024.4906,,false,FEED
W201,Machine learning for marsh accretion,2019,ART,S09,10.55555/s09.2019.3873,,false,FEED
W202,Issue information,2023,PTX,S02,10.55555/s02.2023.6274,,false,FEED
W203,A community intercomparison of beach profiles,2024,ART,S03,10.55555/s03.2024.9368,,false,FEED
W204,Long-term trends in tidal asymmetry in the Brevin shelf,2024,ART,S09,10.55555/s09.2024.3604,,false,FEED
W205,Uncertainty in sensor calibration estimates: a review,2025,REV,S03,10.55555/s03.2025.2579,,false,FEED
W206,Observations of buoy telemetry in a semi-enclosed sea,2020,ART,S01,10.55555/s01.2020.8424,,false,FEED
W208,A framework for sensor calibration in tidal inlets,2019,ART,S10,10.55555/s10.2019.9187,,false,FEED
W209,Remote sensing of turbulent wakes in sandy coasts,2025,ART,S02,10.55555/s02.2025.2983,,false,FEED
W210,Low-cost methods for estuarine salinity,2021,PPR,S14,10.55555/s14.2021.5188,W902,false,FEED
W211,Long-term trends in internal waves in the Wexcombe marshes,2019,ART,S10,10.55555/s10.2019.3569,,false,FEED
W212,Issue information,2019,PTX,S03,10.55555/s03.2019.4582,,false,FEED
W214,A framework for buoy telemetry in shallow channels,2023,ART,S03,10.55555/s03.2023.5869,,false,FEED
W215,Long-term trends in harbour seiches in harbour basins,2024,ART,S12,10.55555/s12.2024.4967,,false,FEED
W216,Observations of vortex shedding in the Albury estuary,2025,ART,S03,10.55555/s03.2025.8866,,false,FEED
W217,Machine learning for estuarine salinity in harbour basins,2024,ART,S02,10.55555/s02.2024.4926,,false,FEED
W218,Field measurements of wave runup in the Albury estuary,2021,ART,S11,10.55555/s11.2021.6637,,false,FEED
W219,Remote sensing of sensor calibration,2022,PPR,S05,10.55555/s05.2022.9710,W251,false,FEED
W220,Revisiting river plumes in tidal inlets,2021,ART,S09,10.55555/s09.2021.2494,,false,FEED
W221,A model of marsh accretion in mixed-energy coasts,2023,PPR,S14,10.55555/s14.2023.3805,,false,FEED
W222,Low-cost methods for harbour seiches,2023,ART,S07,10.55555/s07.2023.3997,,false,FEED
W223,Low-cost methods for tidal asymmetry in the Wexcombe marshes,2021,ART,S11,10.55555/s11.2021.2080,,false,FEED
W224,Editorial: scaling laws for harbour seiches,2025,EDT,S09,10.55555/s09.2025.4466,,false,FEED
W225,Revisiting breaking waves in shallow channels,2025,ART,S09,10.55555/s09.2025.3393,,false,FEED
W226,Uncertainty in estuarine plumes estimates,2023,PPR,S05,10.55555/s05.2023.4761,W710,false,FEED
W227,Low-cost methods for estuarine plumes: a review,2020,REV,S01,10.55555/s01.2020.3822,,false,FEED
W228,Observations of coastal upwelling in the Brevin shelf,2024,ART,S09,10.55555/s09.2024.1383,,false,FEED
W229,Observations of sensor calibration in a semi-enclosed sea,2023,ART,S06,10.55555/s06.2023.9154,,false,FEED
W230,Low-cost methods for wave runup,2024,ART,S03,10.55555/s03.2024.3582,,false,FEED
W232,A model of channel hydraulics,2019,ART,S06,10.55555/s06.2019.8227,,false,FEED
W233,A framework for seabed classification,2024,ART,S06,10.55555/s06.2024.5906,,false,FEED
W235,Scaling laws for coastal upwelling,2025,ART,S07,10.55555/s07.2025.4477,,false,FEED
W237,Field measurements of tidal asymmetry in the open shelf,2020,ART,S12,10.55555/s12.2020.2545,,false,FEED
W238,Observations of survey vessel autonomy in tidal inlets,2023,ART,S02,10.55555/s02.2023.9675,,false,FEED
W239,Observations of beach profiles in harbour basins,2019,ART,S10,10.55555/s10.2019.9025,,false,FEED
W240,Issue information,2025,PTX,S01,10.55555/s01.2025.5660,,false,FEED
W241,Seasonal variability in internal waves in a laboratory flume,2020,ART,S02,10.55555/s02.2020.1199,,false,FEED
W242,Remote sensing of estuarine salinity,2024,ART,S03,10.55555/s03.2024.5114,,false,FEED
W243,Field measurements of acoustic positioning in the open shelf,2019,ART,S02,10.55555/s02.2019.6029,,false,FEED
W246,Low-cost methods for wave runup in a semi-enclosed sea,2023,ART,S11,10.55555/s11.2023.8049,,false,FEED
W247,A framework for harbour seiches,2025,ART,S09,10.55555/s09.2025.8273,,false,FEED
W249,Observations of stratified flows in tidal inlets,2025,ART,S09,10.55555/s09.2025.1434,,false,FEED
W251,Remote sensing of sensor calibration,2023,ART,S02,10.55555/s02.2023.5427,,false,FEED
W252,Machine learning for beach profiles in the North Sea,2025,ART,S02,10.55555/s02.2025.2973,,false,FEED
W253,Field measurements of dune erosion in the North Sea,2025,ART,S07,10.55555/s07.2025.2883,,false,FEED
W254,Observations of storm surge in a laboratory flume,2023,ART,S12,10.55555/s12.2023.8407,,false,FEED
W255,Observations of sediment flux,2025,ART,S03,10.55555/s03.2025.4955,,false,FEED
W256,Machine learning for beach profiles: a review,2019,REV,S02,10.55555/s02.2019.6603,,false,FEED
W257,Uncertainty in dune erosion estimates in the North Sea,2023,ART,S07,10.55555/s07.2023.5247,,false,FEED
W258,A framework for tidal asymmetry,2020,ART,S10,10.55555/s10.2020.1248,,false,FEED
W259,A framework for estuarine salinity,2022,ART,S07,10.55555/s07.2022.4755,,false,FEED
W260,Remote sensing of stratified flows,2025,ART,S02,10.55555/s02.2025.7233,,false,FEED
W261,Field measurements of sediment flux in a semi-enclosed sea: a review,2023,REV,S08,10.55555/s08.2023.7081,,false,FEED
W262,Revisiting sensor calibration in a semi-enclosed sea,2025,ART,S01,10.55555/s01.2025.3687,,false,FEED
W263,Low-cost methods for storm surge in shallow channels,2019,PPR,S05,10.55555/s05.2019.4392,W279,false,FEED
W264,Seasonal variability in tidal mixing in sandy coasts,2022,ART,S10,10.55555/s10.2022.1503,,false,FEED
W265,Remote sensing of coastal upwelling in tidal inlets,2025,ART,S08,10.55555/s08.2025.3453,,false,FEED
W266,Low-cost methods for wave boundary layers,2024,ART,S01,10.55555/s01.2024.3995,,false,FEED
W267,A framework for tidal mixing in the open shelf,2023,ART,S11,10.55555/s11.2023.8676,,false,FEED
W268,Remote sensing of turbulent wakes in a laboratory flume,2025,ART,S02,10.55555/s02.2025.4471,,false,STG
W269,Low-cost methods for tidal asymmetry,2020,ART,S10,10.55555/s10.2020.1871,,false,FEED
W270,Revisiting turbulent wakes,2024,ART,S02,10.55555/s02.2024.5947,,false,FEED
W271,Editorial: battery endurance,2019,EDT,S01,10.55555/s01.2019.6724,,false,FEED
W272,Field measurements of marsh accretion in a semi-enclosed sea: a review,2025,REV,S11,10.55555/s11.2025.9074,,false,FEED
W273,Revisiting underwater docking in sandy coasts,2024,ART,S06,10.55555/s06.2024.7050,,false,FEED
W274,Remote sensing of harbour seiches,2024,ART,S11,10.55555/s11.2024.9547,,false,FEED
W275,Low-cost methods for marsh accretion in a macrotidal bay,2020,ART,S07,10.55555/s07.2020.5876,,false,FEED
W276,A model of dune erosion in the open shelf,2022,ART,S08,10.55555/s08.2022.2667,,false,FEED
W277,A model of marsh accretion in fjords: a review,2019,REV,S09,10.55555/s09.2019.7655,,false,FEED
W278,A model of sediment flux in the North Sea,2020,ART,S10,10.55555/s10.2020.2396,,false,FEED
W279,Low-cost methods for storm surge in shallow channels,2019,ART,S01,10.55555/s01.2019.1190,,false,FEED
W281,Field measurements of sediment resuspension,2021,ART,S03,10.55555/s03.2021.2574,,false,FEED
W282,A framework for bed shear stress,2025,ART,S01,10.55555/s01.2025.8575,,false,FEED
W284,Field measurements of sediment flux,2024,ART,S10,10.55555/s10.2024.6669,,false,FEED
W285,Long-term trends in tidal mixing,2023,ART,S11,10.55555/s11.2023.4596,,false,FEED
W286,Front matter,2022,PTX,S03,10.55555/s03.2022.9263,,false,FEED
W289,Revisiting tidal asymmetry in the open shelf,2022,ART,S09,10.55555/s09.2022.2616,,false,FEED
W291,Seasonal variability in dune erosion in the open shelf,2019,ART,S07,10.55555/s07.2019.7163,,false,FEED
W292,A model of underwater docking in the Albury estuary,2020,ART,S01,10.55555/s01.2020.6227,,false,FEED
W293,Low-cost methods for buoy telemetry,2023,ART,S02,10.55555/s02.2023.1027,,false,FEED
W294,A model of sediment flux,2019,ART,S06,10.55555/s06.2019.3962,,false,FEED
W296,Observations of sensor calibration,2019,ART,S02,10.55555/s02.2019.3432,,false,FEED
W297,A framework for estuarine plumes,2019,ART,S11,10.55555/s11.2019.7764,,false,FEED
W299,Remote sensing of marsh accretion in the Albury estuary,2024,ART,S12,10.55555/s12.2024.9010,,false,FEED
W300,A framework for vortex shedding,2025,ART,S03,10.55555/s03.2025.9744,,false,FEED
W301,A framework for wave boundary layers in shallow channels,2020,ART,S02,10.55555/s02.2020.2955,,false,FEED
W302,A framework for estuarine plumes in a laboratory flume,2024,ART,S11,10.55555/s11.2024.9681,,false,FEED
W303,A framework for tidal asymmetry in the Albury estuary,2020,ART,S03,10.55555/s03.2020.9436,,false,FEED
W304,Long-term trends in estuarine salinity in harbour basins,2024,ART,S01,10.55555/s01.2024.9643,,false,FEED
W305,Uncertainty in marsh accretion estimates in the Albury estuary,2023,ART,S09,10.55555/s09.2023.7844,,false,FEED
W306,Seasonal variability in sediment flux in the Brevin shelf,2023,PPR,S14,10.55555/s14.2023.5478,,false,FEED
W308,A model of ocean optics in the open shelf,2024,ART,S01,10.55555/s01.2024.4225,,false,FEED
W309,Scaling laws for vortex shedding,2019,ART,S10,10.55555/s10.2019.5629,,false,FEED
W310,Machine learning for tidal asymmetry in fjords,2025,ART,S11,10.55555/s11.2025.8764,,false,FEED
W312,Observations of estuarine plumes,2021,ART,S03,10.55555/s03.2021.8491,,false,FEED
W313,Uncertainty in turbidity sensing estimates in the Albury estuary,2021,ART,S04,10.55555/s04.2021.1580,,false,FEED
W314,Observations of seabed classification in the open shelf,2025,ART,S01,10.55555/s01.2025.2601,,false,FEED
W315,Seasonal variability in acoustic positioning,2024,ART,S11,10.55555/s11.2024.3037,,false,FEED
W317,A framework for beach profiles,2021,ART,S11,10.55555/s11.2021.2440,,false,FEED
W318,A framework for internal waves,2025,ART,S11,10.55555/s11.2025.1115,,false,FEED
W319,Revisiting seabed classification in shallow channels,2023,ART,S09,10.55555/s09.2023.4827,,false,FEED
W320,Field measurements of coastal upwelling in the Brevin shelf,2024,ART,S08,10.55555/s08.2024.9420,,true,FEED
W321,Erratum: A model of breaking waves in the North Sea,2025,ERR,S03,10.55555/s03.2025.6357,,false,FEED
W322,A framework for fleet coordination,2019,PPR,S14,10.55555/s14.2019.9512,W453,false,FEED
W323,A model of wave runup in the Albury estuary,2020,ART,S10,10.55555/s10.2020.5947,,false,FEED
W324,A model of wave runup in sandy coasts,2019,ART,S12,10.55555/s12.2019.6638,,false,FEED
W325,Remote sensing of vortex shedding in the Wexcombe marshes,2023,ART,S04,10.55555/s04.2023.9647,,false,FEED
W326,Seasonal variability in tidal asymmetry in the North Sea,2020,ART,S10,10.55555/s10.2020.4586,,false,FEED
W329,Field measurements of channel hydraulics in mixed-energy coasts,2025,ART,S01,10.55555/s01.2025.8849,,false,STG
W330,Low-cost methods for dune erosion in the Wexcombe marshes,2025,ART,S09,10.55555/s09.2025.7821,,false,FEED
W331,Editorial: ocean optics,2019,EDT,S02,10.55555/s02.2019.4747,,false,FEED
W332,Scaling laws for marsh accretion in mixed-energy coasts,2022,ART,S11,10.55555/s11.2022.6992,,false,FEED
W333,Low-cost methods for tidal mixing,2024,ART,S01,10.55555/s01.2024.5072,,false,FEED
W334,A model of tidal asymmetry in a semi-enclosed sea,2023,ART,S09,10.55555/s09.2023.3033,,false,FEED
W335,Seasonal variability in dune erosion in tidal inlets,2022,ART,S09,10.55555/s09.2022.7815,,false,FEED
W336,Uncertainty in river plumes estimates in a semi-enclosed sea,2021,PPR,S14,10.55555/s14.2021.3671,,false,FEED
W337,Machine learning for acoustic positioning in the open shelf,2022,ART,S11,10.55555/s11.2022.6556,,false,FEED
W338,Seasonal variability in acoustic positioning in a semi-enclosed sea,2025,ART,S01,10.55555/s01.2025.5509,,false,FEED
W339,Uncertainty in storm surge estimates in the North Sea,2022,ART,S10,10.55555/s10.2022.3624,,false,FEED
W341,Remote sensing of estuarine plumes,2020,ART,S03,10.55555/s03.2020.2906,,false,FEED
W342,Field measurements of stratified flows,2023,ART,S03,10.55555/s03.2023.8139,,false,FEED
W343,Revisiting battery endurance in the open shelf,2025,ART,S02,10.55555/s02.2025.5231,,false,FEED
W344,Machine learning for underwater docking in the Wexcombe marshes,2020,ART,S03,10.55555/s03.2020.4113,,false,FEED
W345,A framework for beach profiles in a macrotidal bay,2021,ART,S12,10.55555/s12.2021.9722,,false,FEED
W346,Revisiting sonar imaging in the Albury estuary,2019,ART,S11,10.55555/s11.2019.4207,,false,FEED
W348,Scaling laws for ocean optics in fjords,2021,ART,S11,10.55555/s11.2021.6494,,false,FEED
W349,Scaling laws for turbidity sensing in a laboratory flume,2024,ART,S01,10.55555/s01.2024.3743,,false,FEED
W350,Revisiting ocean optics,2023,ART,S03,10.55555/s03.2023.5242,,false,FEED
W352,Scaling laws for storm surge in the North Sea,2024,ART,S12,10.55555/s12.2024.1961,,false,FEED
W354,Scaling laws for wave runup in sandy coasts,2021,ART,S01,10.55555/s01.2021.9856,,false,FEED
W355,Scaling laws for wave boundary layers in the North Sea,2024,ART,S09,10.55555/s09.2024.5466,,false,FEED
W356,Long-term trends in underwater docking,2022,ART,S02,10.55555/s02.2022.3480,,false,FEED
W357,Observations of tidal mixing,2025,ART,S10,10.55555/s10.2025.5331,,false,FEED
W358,Scaling laws for tidal asymmetry,2024,ART,S08,10.55555/s08.2024.1604,,false,FEED
W359,Seasonal variability in sediment flux in the Wexcombe marshes,2022,ART,S01,10.55555/s01.2022.7873,,false,FEED
W361,A model of dune erosion,2019,ART,S01,10.55555/s01.2019.9767,,false,FEED
W362,A model of beach profiles in the North Sea,2022,ART,S08,10.55555/s08.2022.8115,,false,FEED
W365,Low-cost methods for channel hydraulics in a macrotidal bay,2021,ART,S03,10.55555/s03.2021.1932,,false,FEED
W366,Scaling laws for tidal mixing in harbour basins,2022,ART,S03,10.55555/s03.2022.2739,,false,FEED
W367,Low-cost methods for dune erosion in mixed-energy coasts,2022,ART,S02,10.55555/s02.2022.4438,,false,FEED
W368,Scaling laws for seabed classification in the Wexcombe marshes: a review,2023,REV,S02,10.55555/s02.2023.1556,,false,FEED
W369,Remote sensing of internal waves in shallow channels: a review,2019,REV,S11,10.55555/s11.2019.7258,,false,FEED
W370,Revisiting survey vessel autonomy in the Wexcombe marshes,2025,ART,S02,10.55555/s02.2025.5705,,false,FEED
W371,Editorial: a model of coastal upwelling in tidal inlets,2024,EDT,S10,10.55555/s10.2024.9940,,false,FEED
W372,A framework for channel hydraulics in fjords,2025,SUP,S02,10.55555/s02.2025.3633,,false,STG
W373,A framework for harbour seiches in a macrotidal bay: a review,2020,REV,S11,10.55555/s11.2020.1542,,false,FEED
W374,Machine learning for underwater docking in the open shelf,2023,ART,S02,10.55555/s02.2023.9914,,true,FEED
W376,Scaling laws for storm surge in a semi-enclosed sea,2024,ART,S10,10.55555/s10.2024.1001,,false,FEED
W377,Long-term trends in marsh accretion,2021,ART,S10,10.55555/s10.2021.9832,,false,FEED
W378,Seasonal variability in tidal asymmetry in mixed-energy coasts: a review,2024,REV,S02,10.55555/s02.2024.7988,,false,FEED
W380,A model of marsh accretion in the Brevin shelf,2023,ART,S10,10.55555/s10.2023.5051,,false,FEED
W382,Machine learning for river plumes in a semi-enclosed sea,2020,ART,S07,10.55555/s07.2020.9152,,false,FEED
W383,Field measurements of turbidity sensing: a review,2023,REV,S03,10.55555/s03.2023.3064,,false,FEED
W384,Machine learning for storm surge,2025,ART,S10,10.55555/s10.2025.3246,,false,FEED
W385,A model of fleet coordination in mixed-energy coasts: a review,2024,REV,S09,10.55555/s09.2024.8249,,false,FEED
W387,Uncertainty in internal waves estimates in the open shelf,2024,ART,S07,10.55555/s07.2024.2387,,false,FEED
W388,Observations of buoy telemetry in sandy coasts,2019,ART,S01,10.55555/s01.2019.9333,,false,FEED
W389,A framework for turbidity sensing in shallow channels,2025,ART,S04,10.55555/s04.2025.9599,,false,FEED
W390,A model of river plumes in the Brevin shelf,2022,ART,S03,10.55555/s03.2022.5366,,false,FEED
W392,Field measurements of internal waves in the Wexcombe marshes,2021,ART,S11,10.55555/s11.2021.9626,,false,FEED
W393,Remote sensing of tidal asymmetry in the Wexcombe marshes,2023,ART,S11,10.55555/s11.2023.9629,,false,FEED
W396,Seasonal variability in battery endurance in the North Sea,2024,ART,S06,10.55555/s06.2024.8221,,false,FEED
W397,Scaling laws for acoustic positioning,2025,ART,S01,10.55555/s01.2025.9888,,false,STG
W398,Machine learning for internal waves in mixed-energy coasts,2023,ART,S12,10.55555/s12.2023.6906,,false,FEED
W399,A model of marsh accretion in harbour basins,2019,ART,S09,10.55555/s09.2019.6768,,false,FEED
W400,Observations of glider navigation,2019,ART,S02,10.55555/s02.2019.4353,,false,FEED
W401,Long-term trends in wave boundary layers in tidal inlets,2019,ART,S10,10.55555/s10.2019.3057,,false,FEED
W402,Observations of wave runup in shallow channels,2019,ART,S03,10.55555/s03.2019.1468,,false,FEED
W403,Machine learning for marsh accretion in the Brevin shelf,2021,ART,S07,10.55555/s07.2021.5860,,false,FEED
W404,Machine learning for marsh accretion in harbour basins,2021,ART,S07,10.55555/s07.2021.4390,,false,FEED
W405,Field measurements of sediment resuspension in a macrotidal bay,2024,ART,S03,10.55555/s03.2024.1348,,false,FEED
W406,Long-term trends in wave runup in a laboratory flume,2020,ART,S11,10.55555/s11.2020.2202,,false,FEED
W407,Low-cost methods for bed shear stress in fjords: a review,2023,PPR,S14,10.55555/s14.2023.2990,W1027,false,FEED
W408,A framework for coastal upwelling,2024,ART,S13,10.55555/s13.2024.7613,,false,FEED
W410,Low-cost methods for seabed classification in a semi-enclosed sea: a review,2020,REV,S03,10.55555/s03.2020.1868,,false,FEED
W411,Revisiting turbulent wakes in the Brevin shelf,2022,ART,S02,10.55555/s02.2022.5365,,true,FEED
W413,Seasonal variability in sensor calibration in a laboratory flume,2023,ART,S01,10.55555/s01.2023.4722,,false,FEED
W414,Uncertainty in tidal asymmetry estimates in the open shelf,2021,ART,S10,10.55555/s10.2021.1459,,false,FEED
W415,Uncertainty in sediment flux estimates in the Wexcombe marshes: a review,2019,REV,S09,10.55555/s09.2019.3837,,false,FEED
W416,Uncertainty in turbidity sensing estimates in a semi-enclosed sea,2020,PPR,S14,10.55555/s14.2020.9254,W640,false,FEED
W417,A model of turbulent wakes in harbour basins,2023,ART,S02,10.55555/s02.2023.8231,,false,FEED
W418,Editorial: dune erosion,2024,EDT,S02,10.55555/s02.2024.3216,,false,FEED
W419,Seasonal variability in vortex shedding,2024,ART,S02,10.55555/s02.2024.4676,,false,FEED
W420,Observations of coastal upwelling in mixed-energy coasts,2020,ART,S03,10.55555/s03.2020.5603,,false,FEED
W421,Low-cost methods for breaking waves,2024,ART,S02,10.55555/s02.2024.8765,,false,FEED
W422,Remote sensing of coastal upwelling,2023,ART,S01,10.55555/s01.2023.4536,,false,FEED
W423,Seasonal variability in coastal upwelling in tidal inlets,2024,ART,S08,10.55555/s08.2024.1591,,false,FEED
W424,Revisiting marsh accretion in mixed-energy coasts: a review,2019,REV,S10,10.55555/s10.2019.2279,,false,FEED
W425,Uncertainty in sediment flux estimates,2020,ART,S02,10.55555/s02.2020.3211,,false,FEED
W426,Seasonal variability in beach profiles in a laboratory flume,2019,ART,S01,10.55555/s01.2019.7776,,false,FEED
W427,Low-cost methods for coastal upwelling in shallow channels,2023,ART,S09,10.55555/s09.2023.3984,,false,FEED
W428,Revisiting turbulent wakes in the open shelf,2022,ART,S03,10.55555/s03.2022.9134,,false,FEED
W430,Observations of wave runup in harbour basins,2019,ART,S09,10.55555/s09.2019.3545,,false,FEED
W431,Editorial: revisiting dune erosion,2025,EDT,S11,10.55555/s11.2025.5917,,false,FEED
W432,Revisiting tidal asymmetry in tidal inlets,2023,PPR,S05,10.55555/s05.2023.4384,W879,false,FEED
W433,A model of sediment flux in sandy coasts,2023,ART,S09,10.55555/s09.2023.3506,,false,FEED
W434,Long-term trends in beach profiles in harbour basins,2025,ART,S02,10.55555/s02.2025.2778,,false,FEED
W435,Remote sensing of underwater docking in a macrotidal bay,2023,ART,S06,10.55555/s06.2023.1655,,false,FEED
W436,Low-cost methods for estuarine plumes in a laboratory flume,2024,ART,S01,10.55555/s01.2024.7230,,false,FEED
W437,Editorial: low-cost methods for beach profiles in shallow channels,2024,EDT,S08,10.55555/s08.2024.9419,,false,FEED
W438,Seasonal variability in ocean optics in the open shelf,2022,ART,S11,10.55555/s11.2022.9071,,false,FEED
W439,Seasonal variability in wave runup in the Wexcombe marshes,2022,ART,S09,10.55555/s09.2022.7279,,false,FEED
W440,Long-term trends in harbour seiches in fjords,2022,ART,S08,10.55555/s08.2022.7178,,false,FEED
W441,Observations of estuarine plumes in harbour basins,2023,ART,S11,10.55555/s11.2023.7309,,false,FEED
W442,Uncertainty in harbour seiches estimates in sandy coasts,2021,ART,S09,10.55555/s09.2021.9414,,false,FEED
W443,Field measurements of wave runup in a laboratory flume,2024,ART,S11,10.55555/s11.2024.4375,,false,FEED
W444,Low-cost methods for wave boundary layers in a laboratory flume,2019,ART,S03,10.55555/s03.2019.7273,,true,FEED
W445,A framework for wave runup,2021,SUP,S06,10.55555/s06.2021.8886,,false,FEED
W446,Remote sensing of dune erosion in a macrotidal bay: a review,2022,REV,S03,10.55555/s03.2022.2159,,false,FEED
W448,Remote sensing of coastal upwelling in the Albury estuary,2023,ART,S13,10.55555/s13.2023.7244,,false,FEED
W449,Machine learning for glider navigation,2022,ART,S04,10.55555/s04.2022.2709,,false,FEED
W450,Remote sensing of breaking waves in the Wexcombe marshes,2021,SUP,S02,10.55555/s02.2021.8894,,false,FEED
W451,Revisiting coastal upwelling in a laboratory flume: a review,2025,REV,S08,10.55555/s08.2025.2028,,false,FEED
W452,Field measurements of sonar imaging in shallow channels,2021,ART,S02,10.55555/s02.2021.6330,,false,FEED
W453,A framework for fleet coordination,2019,ART,S03,10.55555/s03.2019.3763,,false,FEED
W454,Long-term trends in vortex shedding,2021,ART,S02,10.55555/s02.2021.3382,,false,FEED
W455,Uncertainty in sonar imaging estimates in sandy coasts,2021,ART,S02,10.55555/s02.2021.6875,,false,FEED
W456,Uncertainty in wave runup estimates in shallow channels,2025,ART,S09,10.55555/s09.2025.3320,,false,FEED
W457,A framework for marsh accretion in shallow channels: a review,2020,REV,S10,10.55555/s10.2020.3260,,false,FEED
W458,Uncertainty in beach profiles estimates in a macrotidal bay,2019,ART,S08,10.55555/s08.2019.3618,,false,FEED
W459,Field measurements of harbour seiches,2021,ART,S06,10.55555/s06.2021.1885,,false,FEED
W460,Low-cost methods for sensor calibration,2022,PPR,S14,10.55555/s14.2022.8065,W496,false,FEED
W461,Long-term trends in sediment flux,2019,ART,S10,10.55555/s10.2019.3191,,false,FEED
W462,Machine learning for sediment flux in fjords,2021,ART,S06,10.55555/s06.2021.1053,,false,FEED
W463,Machine learning for battery endurance in tidal inlets,2023,ART,S03,10.55555/s03.2023.1013,,false,FEED
W464,A framework for turbidity sensing,2021,ART,S09,10.55555/s09.2021.3012,,false,FEED
W465,Long-term trends in buoy telemetry in a laboratory flume,2020,ART,S03,10.55555/s03.2020.7103,,false,FEED
W466,Long-term trends in beach profiles,2020,ART,S08,10.55555/s08.2020.3642,,false,FEED
W467,Remote sensing of harbour seiches in fjords: a review,2024,REV,S01,10.55555/s01.2024.6896,,false,FEED
W469,Uncertainty in wave runup estimates in tidal inlets: a review,2020,REV,S10,10.55555/s10.2020.2479,,false,FEED
W470,Uncertainty in tidal asymmetry estimates in a macrotidal bay,2022,ART,S08,10.55555/s08.2022.2679,,false,FEED
W471,Uncertainty in internal waves estimates in sandy coasts,2022,ART,S09,10.55555/s09.2022.1093,,false,FEED
W473,Field measurements of bed shear stress,2023,ART,S02,10.55555/s02.2023.8085,,false,FEED
W474,Long-term trends in ocean optics: a review,2023,REV,S01,10.55555/s01.2023.1515,,false,FEED
W475,Low-cost methods for beach profiles in the Albury estuary,2024,ART,S09,10.55555/s09.2024.6309,,false,FEED
W476,Revisiting beach profiles,2021,ART,S01,10.55555/s01.2021.9653,,false,FEED
W477,Field measurements of channel hydraulics: a review,2024,REV,S06,10.55555/s06.2024.8162,,false,FEED
W478,Long-term trends in bed shear stress in a semi-enclosed sea,2019,ART,S01,10.55555/s01.2019.6241,,false,FEED
W479,Revisiting stratified flows: a review,2020,REV,S02,10.55555/s02.2020.2294,,false,FEED
W480,Editorial: ocean optics,2019,EDT,S03,10.55555/s03.2019.8946,,false,FEED
W481,Erratum: Machine learning for sensor calibration in a laboratory flume,2024,ERR,S09,10.55555/s09.2024.5830,,false,FEED
W483,Observations of marsh accretion in the Albury estuary,2019,ART,S12,10.55555/s12.2019.4182,,false,FEED
W484,Scaling laws for sediment flux in the Wexcombe marshes,2020,ART,S01,10.55555/s01.2020.2410,,false,FEED
W485,Revisiting tidal asymmetry in shallow channels,2021,ART,S07,10.55555/s07.2021.3628,,false,FEED
W486,Uncertainty in vortex shedding estimates in the Brevin shelf,2019,ART,S10,10.55555/s10.2019.2360,,false,FEED
W487,Remote sensing of wave runup in the open shelf,2024,ART,S11,10.55555/s11.2024.1631,,false,FEED
W488,A framework for turbulent wakes,2025,ART,S01,10.55555/s01.2025.9949,,false,STG
W489,Scaling laws for beach profiles in the Albury estuary,2020,ART,S11,10.55555/s11.2020.6314,,false,FEED
W491,Seasonal variability in wave runup in the open shelf,2020,ART,S12,10.55555/s12.2020.4218,,false,FEED
W492,Field measurements of estuarine salinity,2025,ART,S09,10.55555/s09.2025.1360,,false,FEED
W493,Low-cost methods for tidal asymmetry in harbour basins,2024,ART,S11,10.55555/s11.2024.9688,,false,FEED
W496,Low-cost methods for sensor calibration,2022,ART,S02,10.55555/s02.2022.3778,,false,FEED
W497,Remote sensing of vortex shedding in mixed-energy coasts,2024,ART,S02,10.55555/s02.2024.3309,,false,FEED
W498,Remote sensing of wave runup in sandy coasts,2024,ART,S07,10.55555/s07.2024.6095,,false,FEED
W499,Long-term trends in turbidity sensing,2024,ART,S03,10.55555/s03.2024.1107,,false,FEED
W500,Machine learning for dune erosion,2019,ART,S03,10.55555/s03.2019.9740,,false,FEED
W501,Low-cost methods for glider navigation in the open shelf,2024,ART,S02,10.55555/s02.2024.5158,,false,FEED
W502,Field measurements of harbour seiches in mixed-energy coasts,2019,ART,S03,10.55555/s03.2019.4754,,false,FEED
W503,Observations of seabed classification in a macrotidal bay,2021,ART,S01,10.55555/s01.2021.5862,,false,FEED
W504,Field measurements of breaking waves,2024,ART,S03,10.55555/s03.2024.3799,,false,FEED
W505,Field measurements of storm surge in a laboratory flume,2024,ART,S10,10.55555/s10.2024.1506,,false,FEED
W506,Remote sensing of coastal upwelling,2022,PPR,S05,10.55555/s05.2022.7734,W422,false,FEED
W507,Observations of tidal asymmetry in shallow channels,2024,ART,S08,10.55555/s08.2024.9152,,false,FEED
W508,Observations of internal waves in mixed-energy coasts,2021,ART,S10,10.55555/s10.2021.4045,,false,FEED
W509,Uncertainty in harbour seiches estimates in fjords,2024,ART,S08,10.55555/s08.2024.3522,,false,FEED
W510,Field measurements of vortex shedding,2020,ART,S03,10.55555/s03.2020.3398,,false,FEED
W511,Revisiting tidal asymmetry,2023,ART,S08,10.55555/s08.2023.1922,,false,FEED
W512,Long-term trends in estuarine salinity in the open shelf,2025,ART,S07,10.55555/s07.2025.6384,,false,FEED
W513,Field measurements of sonar imaging,2020,ART,S02,10.55555/s02.2020.5677,,false,FEED
W515,Machine learning for bed shear stress,2025,ART,S10,10.55555/s10.2025.3762,,false,FEED
W516,Long-term trends in tidal asymmetry in tidal inlets,2019,ART,S03,10.55555/s03.2019.2384,,false,FEED
W518,Long-term trends in turbulent wakes,2020,ART,S03,10.55555/s03.2020.3210,,false,FEED
W519,A framework for internal waves in the Wexcombe marshes,2021,ART,S10,10.55555/s10.2021.3765,,false,FEED
W520,Low-cost methods for estuarine salinity in mixed-energy coasts,2024,ART,S02,10.55555/s02.2024.3227,,true,FEED
W521,Observations of tidal asymmetry in the open shelf,2024,ART,S08,10.55555/s08.2024.6727,,false,FEED
W522,Observations of estuarine plumes,2020,PPR,S14,10.55555/s14.2020.4281,W312,false,FEED
W523,Seasonal variability in sensor calibration in mixed-energy coasts,2021,ART,S03,10.55555/s03.2021.2677,,false,FEED
W524,Field measurements of harbour seiches in the North Sea,2020,PPR,S05,10.55555/s05.2020.8964,W807,false,FEED
W525,A model of harbour seiches in the open shelf,2024,ART,S02,10.55555/s02.2024.9338,,false,FEED
W526,Long-term trends in storm surge in sandy coasts,2022,ART,S09,10.55555/s09.2022.9881,,false,FEED
W527,Remote sensing of glider navigation,2019,ART,S11,10.55555/s11.2019.6644,,false,FEED
W528,A framework for tidal mixing,2024,ART,S02,10.55555/s02.2024.7151,,false,FEED
W529,Field measurements of survey vessel autonomy in the Brevin shelf,2021,ART,S03,10.55555/s03.2021.3901,,false,FEED
W530,A model of stratified flows in shallow channels,2021,SUP,S06,10.55555/s06.2021.7136,,false,FEED
W531,A framework for stratified flows in shallow channels,2023,ART,S01,10.55555/s01.2023.4752,,false,FEED
W532,Low-cost methods for estuarine salinity in harbour basins,2024,ART,S10,10.55555/s10.2024.2600,,false,FEED
W533,Long-term trends in internal waves in the Albury estuary,2023,ART,S10,10.55555/s10.2023.3693,,false,FEED
W534,Uncertainty in wave runup estimates,2024,ART,S07,10.55555/s07.2024.1162,,false,FEED
W535,A framework for buoy telemetry in the Albury estuary,2025,ART,S01,10.55555/s01.2025.2827,,false,FEED
W536,Seasonal variability in estuarine salinity in the Albury estuary,2020,ART,S11,10.55555/s11.2020.3257,,false,FEED
W538,A framework for sediment flux in the Brevin shelf,2024,ART,S08,10.55555/s08.2024.5964,,false,FEED
W539,A model of stratified flows,2022,ART,S06,10.55555/s06.2022.8112,,false,FEED
W540,Remote sensing of marsh accretion,2023,ART,S07,10.55555/s07.2023.6674,,false,FEED
W541,Scaling laws for dune erosion in the Brevin shelf,2024,ART,S08,10.55555/s08.2024.7243,,false,FEED
W542,Revisiting wave runup in the open shelf,2021,ART,S11,10.55555/s11.2021.8032,,false,FEED
W544,A model of buoy telemetry in mixed-energy coasts,2025,ART,S01,10.55555/s01.2025.1370,,false,FEED
W545,Field measurements of beach profiles,2019,PPR,S14,10.55555/s14.2019.4307,W742,false,FEED
W546,Low-cost methods for sonar imaging,2025,ART,S10,10.55555/s10.2025.8889,,false,FEED
W547,Seasonal variability in internal waves,2021,ART,S11,10.55555/s11.2021.7504,,false,FEED
W548,Editorial: observations of tidal asymmetry in the North Sea,2021,EDT,S09,10.55555/s09.2021.1082,,false,FEED
W549,Observations of wave boundary layers,2024,ART,S11,10.55555/s11.2024.9406,,false,FEED
W550,Uncertainty in internal waves estimates in the Wexcombe marshes,2021,ART,S10,10.55555/s10.2021.7387,,false,FEED
W551,A model of harbour seiches in the Wexcombe marshes,2022,ART,S11,10.55555/s11.2022.2998,,false,FEED
W552,Machine learning for coastal upwelling,2019,ART,S07,10.55555/s07.2019.6027,,false,FEED
W553,Field measurements of buoy telemetry in mixed-energy coasts,2022,ART,S03,10.55555/s03.2022.5263,,false,FEED
W554,Remote sensing of coastal upwelling in a macrotidal bay,2024,ART,S01,10.55555/s01.2024.2480,,false,FEED
W555,A model of underwater docking in a macrotidal bay,2020,ART,S09,10.55555/s09.2020.3444,,false,FEED
W556,Low-cost methods for marsh accretion,2019,PPR,S05,10.55555/s05.2019.3044,W1038,false,FEED
W557,Low-cost methods for underwater docking in mixed-energy coasts,2021,ART,S03,10.55555/s03.2021.3419,,false,FEED
W558,Field measurements of underwater docking in the Wexcombe marshes,2025,ART,S03,10.55555/s03.2025.9898,,false,FEED
W559,Field measurements of storm surge in shallow channels,2022,ART,S11,10.55555/s11.2022.6814,,false,FEED
W560,Scaling laws for tidal asymmetry in mixed-energy coasts,2023,ART,S01,10.55555/s01.2023.4408,,false,FEED
W561,Front matter,2019,PTX,S06,10.55555/s06.2019.5973,,false,FEED
W562,Machine learning for marsh accretion in the open shelf,2019,ART,S08,10.55555/s08.2019.4214,,false,FEED
W563,Low-cost methods for estuarine plumes in the Wexcombe marshes,2021,ART,S01,10.55555/s01.2021.3599,,false,FEED
W564,Scaling laws for battery endurance in a semi-enclosed sea: a review,2022,REV,S01,10.55555/s01.2022.5208,,false,FEED
W565,Observations of beach profiles,2019,ART,S03,10.55555/s03.2019.7754,,false,FEED
W566,A model of wave runup,2023,PPR,S05,10.55555/s05.2023.9828,,false,FEED
W567,Seasonal variability in turbidity sensing,2025,ART,S04,10.55555/s04.2025.3600,,false,FEED
W568,Remote sensing of battery endurance in the Brevin shelf,2024,ART,S01,10.55555/s01.2024.5300,,false,FEED
W569,A framework for fleet coordination in the Brevin shelf,2025,ART,S02,10.55555/s02.2025.9174,,false,STG
W570,Low-cost methods for dune erosion in tidal inlets: a review,2025,REV,S12,10.55555/s12.2025.5362,,false,FEED
W571,Uncertainty in harbour seiches estimates in a macrotidal bay,2024,ART,S02,10.55555/s02.2024.9329,,false,FEED
W572,Editorial: seasonal variability in estuarine salinity,2019,EDT,S10,10.55555/s10.2019.1114,,false,FEED
W573,Long-term trends in estuarine plumes in mixed-energy coasts,2025,REV,S01,10.55555/s01.2025.6255,,false,STG
W574,Revisiting stratified flows in sandy coasts,2020,ART,S02,10.55555/s02.2020.6413,,false,FEED
W575,Seasonal variability in coastal upwelling in fjords: a review,2023,REV,S12,10.55555/s12.2023.9271,,false,FEED
W576,Revisiting wave boundary layers in the North Sea,2021,ART,S03,10.55555/s03.2021.2183,,false,FEED
W578,Seasonal variability in vortex shedding in the Brevin shelf,2024,ART,S09,10.55555/s09.2024.9801,,false,FEED
W579,Machine learning for coastal upwelling in tidal inlets,2020,ART,S12,10.55555/s12.2020.6217,,false,FEED
W580,Remote sensing of harbour seiches in the North Sea,2020,ART,S10,10.55555/s10.2020.2185,,false,FEED
W581,Seasonal variability in sediment flux in a semi-enclosed sea,2023,ART,S10,10.55555/s10.2023.2333,,false,FEED
W582,Field measurements of sediment resuspension in a semi-enclosed sea,2025,ART,S03,10.55555/s03.2025.3135,,false,STG
W583,Long-term trends in dune erosion in tidal inlets,2019,ART,S10,10.55555/s10.2019.7508,,false,FEED
W584,Uncertainty in dune erosion estimates in a semi-enclosed sea,2019,ART,S11,10.55555/s11.2019.4594,,false,FEED
W585,Revisiting battery endurance,2024,ART,S10,10.55555/s10.2024.2511,,false,FEED
W586,Long-term trends in tidal mixing in the open shelf,2025,ART,S02,10.55555/s02.2025.8404,,false,FEED
W587,A framework for harbour seiches in harbour basins,2021,ART,S08,10.55555/s08.2021.1158,,false,FEED
W588,Remote sensing of buoy telemetry,2019,ART,S01,10.55555/s01.2019.1349,,false,FEED
W589,Observations of breaking waves,2020,ART,S11,10.55555/s11.2020.7529,,false,FEED
W590,Front matter,2020,PTX,S02,10.55555/s02.2020.6031,,false,FEED
W592,Remote sensing of estuarine plumes in the Brevin shelf,2025,ART,S03,10.55555/s03.2025.4283,,false,FEED
W593,Seasonal variability in storm surge in sandy coasts: a review,2019,REV,S12,10.55555/s12.2019.6314,,false,FEED
W594,Observations of survey vessel autonomy,2025,ART,S03,10.55555/s03.2025.7998,,false,FEED
W595,Field measurements of stratified flows in a laboratory flume,2024,ART,S11,10.55555/s11.2024.2105,,false,FEED
W598,Revisiting underwater docking in a laboratory flume,2024,ART,S10,10.55555/s10.2024.5249,,false,FEED
W599,Uncertainty in sediment resuspension estimates in the open shelf: a review,2019,REV,S01,10.55555/s01.2019.3968,,false,FEED
W601,Long-term trends in coastal upwelling in a macrotidal bay: a review,2021,REV,S12,10.55555/s12.2021.7790,,false,FEED
W602,Remote sensing of sonar imaging in fjords,2023,ART,S03,10.55555/s03.2023.9987,,false,FEED
W603,Remote sensing of sediment resuspension in shallow channels,2025,ART,S02,10.55555/s02.2025.7119,,false,FEED
W605,Long-term trends in harbour seiches in the Brevin shelf,2019,ART,S03,10.55555/s03.2019.5358,,false,FEED
W606,Scaling laws for beach profiles,2023,ART,S06,10.55555/s06.2023.5454,,false,FEED
W607,Scaling laws for beach profiles in shallow channels,2023,ART,S10,10.55555/s10.2023.4816,,false,FEED
W608,A model of fleet coordination,2020,ART,S01,10.55555/s01.2020.6430,,false,FEED
W609,Machine learning for internal waves in the open shelf,2025,ART,S08,10.55555/s08.2025.8476,,false,FEED
W610,Scaling laws for estuarine plumes in the open shelf,2025,ART,S02,10.55555/s02.2025.5434,,false,STG
W611,A framework for wave boundary layers in shallow channels,2019,PPR,S05,10.55555/s05.2019.5980,W301,false,FEED
W612,A model of survey vessel autonomy in mixed-energy coasts,2023,PPR,S05,10.55555/s05.2023.6455,W869,false,FEED
W613,A model of dune erosion in mixed-energy coasts,2019,ART,S06,10.55555/s06.2019.4535,,false,FEED
W614,Field measurements of marsh accretion in sandy coasts,2023,ART,S10,10.55555/s10.2023.9974,,false,FEED
W615,Low-cost methods for marsh accretion in the Albury estuary,2023,ART,S10,10.55555/s10.2023.3753,,false,FEED
W616,Low-cost methods for storm surge in harbour basins,2020,ART,S11,10.55555/s11.2020.9974,,false,FEED
W617,Scaling laws for dune erosion,2025,ART,S03,10.55555/s03.2025.9852,,false,FEED
W618,Low-cost methods for beach profiles in tidal inlets,2021,ART,S13,10.55555/s13.2021.8504,,false,FEED
W619,Seasonal variability in tidal asymmetry in sandy coasts,2022,ART,S07,10.55555/s07.2022.5383,,false,FEED
W620,Revisiting river plumes in the Wexcombe marshes,2024,ART,S09,10.55555/s09.2024.1747,,false,FEED
W621,Seasonal variability in turbulent wakes,2025,ART,S02,10.55555/s02.2025.2554,,false,FEED
W623,Revisiting wave runup,2020,ART,S09,10.55555/s09.2020.3090,,false,FEED
W624,Low-cost methods for stratified flows in the Albury estuary,2024,ART,S03,10.55555/s03.2024.1326,,false,FEED
W625,Uncertainty in wave boundary layers estimates in fjords,2023,ART,S03,10.55555/s03.2023.8000,,false,FEED
W626,Editorial: beach profiles,2019,EDT,S02,10.55555/s02.2019.6520,,false,FEED
W627,Scaling laws for wave runup in the open shelf,2021,ART,S09,10.55555/s09.2021.1628,,false,FEED
W628,A framework for tidal asymmetry in the open shelf,2021,ART,S12,10.55555/s12.2021.3010,,false,FEED
W629,Low-cost methods for river plumes,2023,ART,S08,10.55555/s08.2023.1974,,false,FEED
W630,Machine learning for estuarine salinity in the North Sea,2019,ART,S09,10.55555/s09.2019.8821,,false,FEED
W631,Low-cost methods for sediment flux,2024,ART,S01,10.55555/s01.2024.1273,,false,FEED
W632,A framework for sediment flux,2025,ART,S03,10.55555/s03.2025.4934,,false,FEED
W633,Long-term trends in breaking waves in sandy coasts,2025,ART,S03,10.55555/s03.2025.8607,,false,FEED
W635,Scaling laws for internal waves,2021,ART,S09,10.55555/s09.2021.7986,,false,FEED
W636,Machine learning for internal waves in the North Sea,2022,ART,S09,10.55555/s09.2022.2840,,false,FEED
W637,Editorial: a model of river plumes in the Albury estuary,2024,EDT,S12,10.55555/s12.2024.2287,,false,FEED
W638,Uncertainty in marsh accretion estimates in the Wexcombe marshes,2021,ART,S09,10.55555/s09.2021.4497,,false,FEED
W639,Seasonal variability in channel hydraulics in the North Sea,2019,SUP,S02,10.55555/s02.2019.5404,,false,FEED
W640,Uncertainty in turbidity sensing estimates in a semi-enclosed sea,2021,ART,S02,10.55555/s02.2021.1205,,false,FEED
W641,A model of beach profiles,2023,ART,S11,10.55555/s11.2023.2011,,false,FEED
W642,Remote sensing of wave runup in the Wexcombe marshes,2021,ART,S09,10.55555/s09.2021.9684,,false,FEED
W643,Uncertainty in estuarine plumes estimates in tidal inlets,2022,ART,S03,10.55555/s03.2022.7484,,false,FEED
W644,Long-term trends in marsh accretion in fjords,2025,ART,S09,10.55555/s09.2025.2662,,false,FEED
W645,A framework for wave runup in mixed-energy coasts: a review,2024,REV,S08,10.55555/s08.2024.7416,,false,FEED
W646,Scaling laws for internal waves in the Brevin shelf,2024,ART,S02,10.55555/s02.2024.6121,,false,FEED
W648,A framework for dune erosion in the Brevin shelf,2024,ART,S02,10.55555/s02.2024.9298,,false,FEED
W649,Remote sensing of tidal asymmetry,2021,ART,S11,10.55555/s11.2021.3654,,false,FEED
W650,Field measurements of wave runup in a macrotidal bay,2024,ART,S12,10.55555/s12.2024.3957,,false,FEED
W651,A framework for breaking waves in harbour basins,2019,ART,S03,10.55555/s03.2019.6678,,false,FEED
W652,Revisiting internal waves in a semi-enclosed sea,2025,ART,S12,10.55555/s12.2025.3292,,false,FEED
W654,A framework for estuarine plumes in the Brevin shelf,2024,ART,S01,10.55555/s01.2024.3834,,false,FEED
W655,Seasonal variability in harbour seiches in a macrotidal bay,2020,ART,S10,10.55555/s10.2020.9455,,false,FEED
W656,Scaling laws for river plumes,2020,ART,S02,10.55555/s02.2020.6712,,false,FEED
W657,Long-term trends in glider navigation,2024,ART,S09,10.55555/s09.2024.6062,,false,FEED
W659,Uncertainty in glider navigation estimates,2023,ART,S10,10.55555/s10.2023.6589,,false,FEED
W660,A framework for buoy telemetry in a macrotidal bay,2022,ART,S01,10.55555/s01.2022.2312,,false,FEED
W661,Revisiting turbidity sensing in the Albury estuary,2024,ART,S02,10.55555/s02.2024.5331,,false,FEED
W662,Observations of marsh accretion,2024,ART,S11,10.55555/s11.2024.9264,,false,FEED
W663,A framework for turbidity sensing,2021,PPR,S14,10.55555/s14.2021.4360,W464,false,FEED
W664,Machine learning for estuarine salinity in the Wexcombe marshes,2020,ART,S02,10.55555/s02.2020.7019,,false,FEED
W665,Uncertainty in wave boundary layers estimates,2019,ART,S03,10.55555/s03.2019.9852,,false,FEED
W666,Field measurements of tidal asymmetry: a review,2023,REV,S09,10.55555/s09.2023.6905,,false,FEED
W667,A model of internal waves in harbour basins,2023,ART,S07,10.55555/s07.2023.6431,,false,FEED
W668,Field measurements of wave runup,2021,ART,S10,10.55555/s10.2021.2689,,false,FEED
W669,Machine learning for river plumes in fjords,2023,ART,S11,10.55555/s11.2023.5633,,false,FEED
W670,Low-cost methods for river plumes in fjords,2025,ART,S03,10.55555/s03.2025.4572,,false,FEED
W671,Seasonal variability in beach profiles,2022,ART,S03,10.55555/s03.2022.3200,,false,FEED
W672,Machine learning for estuarine salinity in a macrotidal bay,2019,ART,S11,10.55555/s11.2019.9549,,false,FEED
W673,A model of seabed classification in harbour basins,2025,ART,S06,10.55555/s06.2025.2155,,false,FEED
W674,Foreword: stratified flows,2022,EDT,S06,10.55555/s06.2022.6198,,false,FEED
W675,Seasonal variability in tidal mixing,2024,ART,S01,10.55555/s01.2024.8449,,false,FEED
W676,Low-cost methods for turbidity sensing,2025,ART,S02,10.55555/s02.2025.6159,,false,FEED
W678,Remote sensing of wave runup in fjords,2020,ART,S01,10.55555/s01.2020.5400,,false,FEED
W679,Remote sensing of battery endurance in tidal inlets,2024,ART,S01,10.55555/s01.2024.5950,,false,FEED
W680,Seasonal variability in breaking waves,2025,REV,S02,10.55555/s02.2025.4880,,false,STG
W681,Field measurements of fleet coordination,2019,ART,S03,10.55555/s03.2019.5212,,false,FEED
W682,Long-term trends in battery endurance,2025,ART,S01,10.55555/s01.2025.3617,,false,FEED
W683,Long-term trends in river plumes in a semi-enclosed sea,2024,ART,S07,10.55555/s07.2024.2985,,false,FEED
W684,Field measurements of dune erosion in tidal inlets,2024,ART,S03,10.55555/s03.2024.1442,,false,FEED
W685,Low-cost methods for dune erosion in the Brevin shelf,2023,ART,S09,10.55555/s09.2023.2998,,false,FEED
W686,Field measurements of wave boundary layers in shallow channels,2022,ART,S03,10.55555/s03.2022.5808,,false,FEED
W688,A model of internal waves in mixed-energy coasts,2025,ART,S10,10.55555/s10.2025.3631,,false,FEED
W690,Observations of turbidity sensing,2023,ART,S02,10.55555/s02.2023.4143,,false,FEED
W691,Uncertainty in turbidity sensing estimates,2023,ART,S11,10.55555/s11.2023.5638,,false,FEED
W692,Low-cost methods for storm surge in a semi-enclosed sea,2020,ART,S12,10.55555/s12.2020.7316,,false,FEED
W693,A framework for wave boundary layers in tidal inlets,2025,ART,S01,10.55555/s01.2025.4141,,true,FEED
W696,Scaling laws for tidal mixing,2019,ART,S06,10.55555/s06.2019.7374,,false,FEED
W697,Observations of vortex shedding,2019,ART,S03,10.55555/s03.2019.2721,,false,FEED
W699,Seasonal variability in sediment flux in mixed-energy coasts,2023,ART,S09,10.55555/s09.2023.6292,,false,FEED
W700,Observations of stratified flows,2025,ART,S03,10.55555/s03.2025.3995,,false,STG
W702,Revisiting marsh accretion,2022,ART,S03,10.55555/s03.2022.5477,,false,FEED
W703,Field measurements of estuarine salinity in the open shelf,2025,ART,S10,10.55555/s10.2025.9900,,false,FEED
W704,Uncertainty in river plumes estimates,2024,ART,S09,10.55555/s09.2024.9163,,false,FEED
W705,Seasonal variability in turbulent wakes in a semi-enclosed sea,2024,ART,S02,10.55555/s02.2024.4059,,false,FEED
W706,Machine learning for sediment flux in the Brevin shelf,2024,REV,S04,10.55555/s04.2024.7328,,false,FEED
W707,Machine learning for channel hydraulics in sandy coasts,2019,ART,S02,10.55555/s02.2019.9758,,false,FEED
W709,Field measurements of estuarine salinity in sandy coasts,2025,ART,S12,10.55555/s12.2025.1295,,false,FEED
W710,Uncertainty in estuarine plumes estimates,2023,ART,S02,10.55555/s02.2023.6237,,false,FEED
W711,Remote sensing of glider navigation in mixed-energy coasts,2025,ART,S02,10.55555/s02.2025.9323,,false,FEED
W713,A model of internal waves in tidal inlets,2019,ART,S09,10.55555/s09.2019.4556,,false,FEED
W714,Low-cost methods for wave boundary layers in the Brevin shelf,2025,ART,S02,10.55555/s02.2025.9707,,false,STG
W715,Field measurements of dune erosion,2021,ART,S02,10.55555/s02.2021.7835,,false,FEED
W716,A framework for river plumes,2020,ART,S06,10.55555/s06.2020.3784,,false,FEED
W718,Uncertainty in marsh accretion estimates in the North Sea: a review,2024,REV,S09,10.55555/s09.2024.8260,,false,FEED
W719,Editorial: long-term trends in wave runup,2025,EDT,S07,10.55555/s07.2025.8025,,false,FEED
W720,Revisiting tidal mixing,2019,ART,S01,10.55555/s01.2019.2517,,false,FEED
W721,Field measurements of wave runup in sandy coasts,2024,ART,S02,10.55555/s02.2024.3360,,false,FEED
W722,Long-term trends in river plumes: a review,2020,REV,S09,10.55555/s09.2020.9978,,false,FEED
W723,A model of vortex shedding in tidal inlets,2020,ART,S03,10.55555/s03.2020.3636,,false,FEED
W724,Revisiting dune erosion in harbour basins,2020,ART,S07,10.55555/s07.2020.4604,,false,FEED
W725,Remote sensing of marsh accretion in shallow channels,2022,ART,S06,10.55555/s06.2022.9264,,false,FEED
W726,Remote sensing of storm surge in the Brevin shelf: a review,2020,REV,S10,10.55555/s10.2020.5895,,false,FEED
W727,Field measurements of breaking waves in the Brevin shelf,2022,ART,S01,10.55555/s01.2022.9629,,false,FEED
W728,Uncertainty in wave boundary layers estimates,2019,PPR,S05,10.55555/s05.2019.7711,W665,false,FEED
W729,Uncertainty in wave runup estimates in a macrotidal bay: a review,2024,REV,S11,10.55555/s11.2024.7189,,false,FEED
W730,A framework for tidal asymmetry in the Albury estuary,2020,PPR,S05,10.55555/s05.2020.4764,W303,false,FEED
W731,Long-term trends in river plumes in mixed-energy coasts,2020,ART,S10,10.55555/s10.2020.5231,,false,FEED
W732,Long-term trends in coastal upwelling in a laboratory flume,2024,ART,S08,10.55555/s08.2024.7170,,false,FEED
W733,Remote sensing of estuarine plumes in mixed-energy coasts,2019,ART,S01,10.55555/s01.2019.7106,,false,FEED
W734,Uncertainty in turbulent wakes estimates in sandy coasts,2025,SUP,S03,10.55555/s03.2025.2334,,false,STG
W735,Low-cost methods for dune erosion in shallow channels,2020,ART,S07,10.55555/s07.2020.8623,,false,FEED
W736,Low-cost methods for beach profiles,2024,ART,S11,10.55555/s11.2024.5981,,false,FEED
W737,A model of stratified flows in the Wexcombe marshes,2019,ART,S10,10.55555/s10.2019.2479,,false,FEED
W738,A framework for turbulent wakes in a laboratory flume,2022,ART,S02,10.55555/s02.2022.5805,,false,FEED
W739,Field measurements of estuarine salinity in a laboratory flume: a review,2019,REV,S11,10.55555/s11.2019.2297,,false,FEED
W740,Observations of marsh accretion in the open shelf,2020,ART,S07,10.55555/s07.2020.4709,,false,FEED
W741,Uncertainty in coastal upwelling estimates,2021,ART,S10,10.55555/s10.2021.3357,,false,FEED
W742,Field measurements of beach profiles,2019,ART,S11,10.55555/s11.2019.1296,,false,FEED
W744,Remote sensing of wave boundary layers,2024,ART,S01,10.55555/s01.2024.8528,,false,FEED
W745,A model of sonar imaging in the Brevin shelf,2020,PPR,S05,10.55555/s05.2020.3478,,false,FEED
W747,Observations of river plumes,2024,PPR,S14,10.55555/s14.2024.1295,,false,FEED
W748,Revisiting battery endurance in the Brevin shelf,2024,ART,S11,10.55555/s11.2024.6265,,false,FEED
W749,Field measurements of marsh accretion: a review,2019,REV,S02,10.55555/s02.2019.3932,,false,FEED
W750,Long-term trends in coastal upwelling,2023,ART,S03,10.55555/s03.2023.6676,,false,FEED
W751,Editorial: sensor calibration,2020,EDT,S03,10.55555/s03.2020.2526,,false,FEED
W752,A framework for internal waves in the Albury estuary,2020,ART,S08,10.55555/s08.2020.6465,,false,FEED
W753,Field measurements of survey vessel autonomy in the Wexcombe marshes,2021,ART,S13,10.55555/s13.2021.5183,,false,FEED
W754,Table of contents,2022,PTX,S01,10.55555/s01.2022.1269,,false,FEED
W755,Machine learning for turbidity sensing in shallow channels,2019,ART,S03,10.55555/s03.2019.4685,,false,FEED
W756,Editorial: low-cost methods for marsh accretion in tidal inlets,2020,EDT,S08,10.55555/s08.2020.8771,,false,FEED
W757,Machine learning for tidal asymmetry in tidal inlets,2023,ART,S12,10.55555/s12.2023.7538,,false,FEED
W758,Low-cost methods for glider navigation in harbour basins: a review,2019,REV,S03,10.55555/s03.2019.1424,,false,FEED
W760,Seasonal variability in marsh accretion in fjords,2025,ART,S11,10.55555/s11.2025.2068,,false,FEED
W761,Long-term trends in battery endurance in a macrotidal bay,2024,ART,S03,10.55555/s03.2024.4054,,false,FEED
W762,Seasonal variability in buoy telemetry in the Albury estuary,2024,ART,S10,10.55555/s10.2024.1283,,false,FEED
W763,A model of glider navigation in a macrotidal bay,2024,ART,S13,10.55555/s13.2024.5312,,false,FEED
W764,Long-term trends in harbour seiches in the Albury estuary,2022,ART,S01,10.55555/s01.2022.9782,,false,FEED
W765,Field measurements of storm surge in harbour basins,2025,ART,S10,10.55555/s10.2025.2383,,false,FEED
W766,Erratum: A model of fleet coordination in mixed-energy coasts: a review,2025,ERR,S09,10.55555/s09.2025.9163,,false,FEED
W768,A model of marsh accretion in the Wexcombe marshes,2020,ART,S11,10.55555/s11.2020.5522,,false,FEED
W769,Scaling laws for estuarine salinity: a review,2020,REV,S10,10.55555/s10.2020.4442,,false,FEED
W770,Machine learning for coastal upwelling in the open shelf,2019,ART,S11,10.55555/s11.2019.6039,,false,FEED
W771,Seasonal variability in tidal mixing in tidal inlets: a review,2019,REV,S02,10.55555/s02.2019.3528,,false,FEED
W772,Field measurements of river plumes,2019,ART,S09,10.55555/s09.2019.2828,,false,FEED
W773,Revisiting estuarine salinity in shallow channels,2022,ART,S11,10.55555/s11.2022.7610,,false,FEED
W774,Seasonal variability in glider navigation,2024,ART,S01,10.55555/s01.2024.4977,,false,FEED
W775,Machine learning for storm surge in mixed-energy coasts,2020,ART,S10,10.55555/s10.2020.7997,,false,FEED
W776,Low-cost methods for harbour seiches in a semi-enclosed sea: a review,2022,REV,S10,10.55555/s10.2022.2098,,false,FEED
W777,Machine learning for turbulent wakes,2023,ART,S01,10.55555/s01.2023.2466,,false,FEED
W778,Long-term trends in sonar imaging,2023,ART,S13,10.55555/s13.2023.7910,,false,FEED
W779,Scaling laws for estuarine plumes in a semi-enclosed sea: a review,2021,REV,S02,10.55555/s02.2021.8337,,false,FEED
W780,Long-term trends in ocean optics in sandy coasts,2019,PPR,S05,10.55555/s05.2019.6565,,false,FEED
W781,Field measurements of turbidity sensing in the Wexcombe marshes,2025,PPR,S05,10.55555/s05.2025.9755,,false,FEED
W782,Long-term trends in storm surge,2020,ART,S11,10.55555/s11.2020.2195,,false,FEED
W783,A framework for stratified flows in harbour basins,2024,ART,S11,10.55555/s11.2024.9909,,false,FEED
W784,Remote sensing of beach profiles in the Albury estuary,2021,ART,S12,10.55555/s12.2021.2613,,false,FEED
W785,A framework for river plumes in fjords: a review,2020,REV,S09,10.55555/s09.2020.9788,,false,FEED
W786,Editorial: observations of storm surge in fjords,2020,EDT,S08,10.55555/s08.2020.6266,,false,FEED
W787,Long-term trends in battery endurance in the Brevin shelf,2024,ART,S02,10.55555/s02.2024.7188,,false,FEED
W788,Seasonal variability in wave boundary layers,2025,ART,S02,10.55555/s02.2025.6486,,false,FEED
W789,Field measurements of tidal mixing,2022,ART,S09,10.55555/s09.2022.9918,,false,FEED
W790,Seasonal variability in breaking waves in a macrotidal bay,2020,ART,S03,10.55555/s03.2020.7464,,false,FEED
W791,Scaling laws for turbulent wakes in mixed-energy coasts,2024,ART,S02,10.55555/s02.2024.7741,,false,FEED
W792,Scaling laws for harbour seiches in the North Sea,2023,ART,S06,10.55555/s06.2023.3994,,false,FEED
W793,A model of stratified flows in sandy coasts,2023,SUP,S06,10.55555/s06.2023.7202,,false,FEED
W794,Revisiting internal waves in tidal inlets,2025,ART,S10,10.55555/s10.2025.3411,,false,FEED
W795,Field measurements of coastal upwelling in a semi-enclosed sea,2024,ART,S09,10.55555/s09.2024.3340,,false,FEED
W797,Revisiting marsh accretion in shallow channels,2021,ART,S11,10.55555/s11.2021.8578,,false,FEED
W798,Long-term trends in channel hydraulics,2023,ART,S02,10.55555/s02.2023.9344,,false,FEED
W799,A framework for coastal upwelling in the North Sea,2022,ART,S01,10.55555/s01.2022.1570,,false,FEED
W800,A model of tidal mixing in the open shelf,2025,SUP,S06,10.55555/s06.2025.5723,,false,FEED
W801,Observations of seabed classification,2022,ART,S03,10.55555/s03.2022.2362,,false,FEED
W802,Observations of estuarine plumes in a laboratory flume,2025,ART,S02,10.55555/s02.2025.8136,,false,STG
W803,Long-term trends in breaking waves,2023,SUP,S06,10.55555/s06.2023.2454,,false,FEED
W804,Long-term trends in harbour seiches,2020,ART,S12,10.55555/s12.2020.9370,,false,FEED
W806,Uncertainty in tidal mixing estimates in sandy coasts,2019,ART,S03,10.55555/s03.2019.2298,,false,FEED
W807,Field measurements of harbour seiches in the North Sea,2020,ART,S03,10.55555/s03.2020.7376,,false,FEED
W808,Uncertainty in beach profiles estimates in the Wexcombe marshes,2021,ART,S09,10.55555/s09.2021.2786,,false,FEED
W809,Revisiting coastal upwelling,2022,ART,S11,10.55555/s11.2022.4289,,false,FEED
W810,Erratum: Uncertainty in internal waves estimates in the North Sea,2025,ERR,S02,10.55555/s02.2025.6696,,false,FEED
W811,A model of buoy telemetry in the Wexcombe marshes,2022,ART,S03,10.55555/s03.2022.2784,,false,FEED
W812,Low-cost methods for buoy telemetry in the open shelf,2024,ART,S10,10.55555/s10.2024.5642,,false,FEED
W813,Erratum: Remote sensing of buoy telemetry in fjords,2025,ERR,S02,10.55555/s02.2025.2143,,false,FEED
W814,Long-term trends in estuarine salinity in the Wexcombe marshes: a review,2025,REV,S07,10.55555/s07.2025.4609,,false,FEED
W815,Low-cost methods for internal waves in fjords,2022,ART,S03,10.55555/s03.2022.7036,,false,FEED
W816,Low-cost methods for sediment flux in a laboratory flume,2020,ART,S07,10.55555/s07.2020.5801,,false,FEED
W817,Remote sensing of survey vessel autonomy in the Brevin shelf,2023,ART,S10,10.55555/s10.2023.6290,,false,FEED
W818,Field measurements of beach profiles in the Albury estuary,2024,ART,S09,10.55555/s09.2024.2786,,false,FEED
W819,Machine learning for wave boundary layers in the open shelf,2025,SUP,S02,10.55555/s02.2025.9700,,false,STG
W820,Long-term trends in tidal asymmetry: a review,2019,REV,S11,10.55555/s11.2019.3624,,false,FEED
W821,Low-cost methods for beach profiles in mixed-energy coasts,2023,ART,S06,10.55555/s06.2023.3335,,false,FEED
W822,A framework for tidal asymmetry in the Brevin shelf,2021,ART,S09,10.55555/s09.2021.7143,,false,FEED
W823,Uncertainty in marsh accretion estimates in mixed-energy coasts,2019,ART,S10,10.55555/s10.2019.9455,,false,FEED
W824,A framework for sonar imaging,2022,PPR,S14,10.55555/s14.2022.5570,,false,FEED
W825,Front matter,2023,PTX,S06,10.55555/s06.2023.9210,,false,FEED
W826,Revisiting wave runup in tidal inlets,2022,ART,S09,10.55555/s09.2022.2879,,false,FEED
W827,Long-term trends in survey vessel autonomy in tidal inlets,2022,ART,S11,10.55555/s11.2022.6278,,false,FEED
W828,A framework for internal waves in the open shelf,2024,ART,S09,10.55555/s09.2024.5979,,false,FEED
W829,Observations of fleet coordination in the Brevin shelf,2025,ART,S02,10.55555/s02.2025.5136,,false,FEED
W830,Scaling laws for turbulent wakes in the Brevin shelf,2024,ART,S02,10.55555/s02.2024.3894,,false,FEED
W831,Revisiting battery endurance in the Wexcombe marshes,2025,ART,S03,10.55555/s03.2025.3877,,false,FEED
W832,Revisiting breaking waves,2021,ART,S10,10.55555/s10.2021.3252,,false,FEED
W833,Observations of fleet coordination in the Albury estuary,2024,ART,S03,10.55555/s03.2024.2508,,false,FEED
W834,Low-cost methods for battery endurance,2023,ART,S13,10.55555/s13.2023.4105,,false,FEED
W835,A model of marsh accretion,2020,ART,S09,10.55555/s09.2020.7114,,false,FEED
W836,Scaling laws for wave runup in harbour basins: a review,2020,REV,S07,10.55555/s07.2020.4614,,false,FEED
W837,Long-term trends in bed shear stress in sandy coasts,2025,ART,S03,10.55555/s03.2025.8651,,true,FEED
W838,Remote sensing of wave runup in harbour basins,2019,ART,S09,10.55555/s09.2019.7832,,false,FEED
W840,A model of ocean optics in the Wexcombe marshes: a review,2025,REV,S11,10.55555/s11.2025.7868,,false,FEED
W842,Uncertainty in internal waves estimates,2024,ART,S02,10.55555/s02.2024.9901,,false,FEED
W843,A framework for ocean optics in the Albury estuary,2023,ART,S02,10.55555/s02.2023.2459,,false,FEED
W844,A framework for seabed classification in fjords,2025,ART,S01,10.55555/s01.2025.4503,,false,STG
W845,Low-cost methods for storm surge in a laboratory flume: a review,2022,REV,S11,10.55555/s11.2022.1648,,false,FEED
W846,Revisiting acoustic positioning in the Wexcombe marshes,2024,ART,S03,10.55555/s03.2024.1652,,false,FEED
W847,Observations of wave runup in mixed-energy coasts,2022,ART,S12,10.55555/s12.2022.3379,,false,FEED
W848,Machine learning for wave runup,2021,ART,S02,10.55555/s02.2021.2822,,false,FEED
W849,Revisiting glider navigation,2020,ART,S04,10.55555/s04.2020.2969,,false,FEED
W850,Long-term trends in stratified flows in the North Sea,2025,ART,S10,10.55555/s10.2025.7663,,false,FEED
W851,Uncertainty in dune erosion estimates,2023,ART,S09,10.55555/s09.2023.4367,,false,FEED
W852,Scaling laws for bed shear stress in the Brevin shelf,2020,ART,S01,10.55555/s01.2020.9443,,true,FEED
W853,Seasonal variability in estuarine plumes,2024,ART,S06,10.55555/s06.2024.3708,,false,FEED
W854,Uncertainty in internal waves estimates in the North Sea,2024,ART,S02,10.55555/s02.2024.1640,,false,FEED
W855,Uncertainty in vortex shedding estimates in the open shelf,2021,ART,S01,10.55555/s01.2021.4438,,false,FEED
W856,Observations of estuarine salinity in tidal inlets,2024,ART,S10,10.55555/s10.2024.9567,,false,FEED
W857,Long-term trends in glider navigation in the North Sea: a review,2020,REV,S06,10.55555/s06.2020.7330,,false,FEED
W858,A model of dune erosion in sandy coasts,2019,ART,S12,10.55555/s12.2019.1831,,false,FEED
W859,Scaling laws for sediment flux in the North Sea: a review,2023,REV,S09,10.55555/s09.2023.2558,,false,FEED
W860,Machine learning for sediment flux in the Wexcombe marshes: a review,2020,REV,S01,10.55555/s01.2020.9597,,false,FEED
W861,Observations of storm surge in a macrotidal bay,2019,ART,S02,10.55555/s02.2019.9911,,false,FEED
W862,Revisiting harbour seiches in a semi-enclosed sea,2024,ART,S09,10.55555/s09.2024.4237,,false,FEED
W863,Uncertainty in harbour seiches estimates in the open shelf,2025,ART,S01,10.55555/s01.2025.7154,,false,FEED
W864,Scaling laws for sediment flux in a semi-enclosed sea,2022,ART,S08,10.55555/s08.2022.1159,,false,FEED
W865,Remote sensing of beach profiles in fjords,2023,ART,S10,10.55555/s10.2023.8011,,false,FEED
W866,Uncertainty in sediment resuspension estimates in shallow channels,2025,SUP,S03,10.55555/s03.2025.9325,,false,STG
W867,Field measurements of internal waves,2023,ART,S11,10.55555/s11.2023.2685,,false,FEED
W868,Scaling laws for breaking waves,2025,ART,S01,10.55555/s01.2025.8064,,false,STG
W869,A model of survey vessel autonomy in mixed-energy coasts,2023,ART,S02,10.55555/s02.2023.6615,,false,FEED
W870,Seasonal variability in wave boundary layers in the Wexcombe marshes,2019,ART,S11,10.55555/s11.2019.4764,,false,FEED
W871,Uncertainty in storm surge estimates in the Albury estuary,2022,ART,S11,10.55555/s11.2022.4343,,false,FEED
W872,Observations of acoustic positioning,2020,ART,S11,10.55555/s11.2020.3206,,false,FEED
W873,Seasonal variability in beach profiles in tidal inlets,2023,ART,S09,10.55555/s09.2023.8810,,false,FEED
W874,Revisiting river plumes,2021,ART,S01,10.55555/s01.2021.9371,,false,FEED
W875,Machine learning for river plumes in the North Sea: a review,2022,REV,S07,10.55555/s07.2022.9264,,false,FEED
W876,Seasonal variability in estuarine plumes in fjords,2019,ART,S02,10.55555/s02.2019.6123,,false,FEED
W877,A model of breaking waves in the North Sea,2023,PPR,S05,10.55555/s05.2023.7929,W965,false,FEED
W878,A model of tidal asymmetry,2025,ART,S08,10.55555/s08.2025.8372,,false,STG
W879,Revisiting tidal asymmetry in tidal inlets,2023,ART,S02,10.55555/s02.2023.6173,,false,FEED
W880,A model of wave boundary layers,2020,ART,S01,10.55555/s01.2020.6134,,false,FEED
W881,Machine learning for vortex shedding,2019,ART,S01,10.55555/s01.2019.2650,,false,FEED
W882,Editorial: stratified flows,2020,EDT,S01,10.55555/s01.2020.7459,,false,FEED
W883,Front matter,2020,PTX,S02,10.55555/s02.2020.4315,,false,FEED
W884,Long-term trends in buoy telemetry,2019,ART,S09,10.55555/s09.2019.2019,,false,FEED
W885,A framework for tidal asymmetry in the North Sea,2025,ART,S09,10.55555/s09.2025.7483,,false,FEED
W886,A framework for underwater docking,2021,ART,S01,10.55555/s01.2021.9824,,false,FEED
W887,Uncertainty in river plumes estimates in the Albury estuary,2020,ART,S12,10.55555/s12.2020.5688,,false,FEED
W888,Remote sensing of sediment flux in a laboratory flume,2020,ART,S10,10.55555/s10.2020.8393,,false,FEED
W889,Observations of battery endurance,2024,ART,S01,10.55555/s01.2024.3798,,false,FEED
W890,Seasonal variability in buoy telemetry,2023,ART,S03,10.55555/s03.2023.1624,,false,FEED
W891,Front matter,2022,PTX,S02,10.55555/s02.2022.4861,,false,FEED
W894,Revisiting harbour seiches,2024,ART,S07,10.55555/s07.2024.7990,,false,FEED
W895,A framework for seabed classification in the Brevin shelf,2023,ART,S10,10.55555/s10.2023.5018,,false,FEED
W896,Field measurements of storm surge in the North Sea,2019,ART,S12,10.55555/s12.2019.6122,,false,FEED
W897,Remote sensing of tidal asymmetry in tidal inlets,2021,ART,S10,10.55555/s10.2021.1577,,false,FEED
W900,Seasonal variability in fleet coordination in the Brevin shelf,2023,ART,S02,10.55555/s02.2023.1438,,false,FEED
W901,Editorial: seasonal variability in dune erosion in sandy coasts,2020,EDT,S07,10.55555/s07.2020.7502,,false,FEED
W902,Low-cost methods for estuarine salinity,2021,ART,S03,10.55555/s03.2021.2331,,false,FEED
W903,Uncertainty in dune erosion estimates in shallow channels: a review,2020,REV,S09,10.55555/s09.2020.6801,,false,FEED
W904,Revisiting sediment resuspension in the Albury estuary,2024,ART,S10,10.55555/s10.2024.9519,,false,FEED
W905,Machine learning for battery endurance in a laboratory flume,2025,ART,S01,10.55555/s01.2025.6186,,false,FEED
W906,Uncertainty in estuarine salinity estimates,2024,ART,S12,10.55555/s12.2024.5239,,false,FEED
W907,Revisiting seabed classification,2025,ART,S03,10.55555/s03.2025.3540,,false,FEED
W908,Scaling laws for sensor calibration: a review,2019,REV,S03,10.55555/s03.2019.5831,,false,FEED
W910,Uncertainty in stratified flows estimates,2021,ART,S03,10.55555/s03.2021.1983,,false,FEED
W913,Revisiting buoy telemetry in tidal inlets,2019,ART,S04,10.55555/s04.2019.1964,,false,FEED
W914,Erratum: Field measurements of channel hydraulics: a review,2025,ERR,S06,10.55555/s06.2025.1637,,false,FEED
W916,A framework for acoustic positioning,2019,ART,S02,10.55555/s02.2019.7042,,false,FEED
W917,Revisiting sediment flux in tidal inlets,2024,ART,S01,10.55555/s01.2024.1306,,false,FEED
W918,Scaling laws for tidal asymmetry in the open shelf,2025,ART,S10,10.55555/s10.2025.5930,,false,FEED
W920,Scaling laws for internal waves in sandy coasts,2025,ART,S11,10.55555/s11.2025.3626,,false,FEED
W921,Uncertainty in estuarine salinity estimates in sandy coasts,2023,ART,S11,10.55555/s11.2023.1834,,false,FEED
W922,Observations of ocean optics,2024,ART,S02,10.55555/s02.2024.8011,,true,FEED
W924,Field measurements of sediment resuspension in shallow channels,2024,ART,S06,10.55555/s06.2024.5766,,false,FEED
W925,Machine learning for internal waves: a review,2024,REV,S09,10.55555/s09.2024.3905,,false,FEED
W926,A framework for wave runup in shallow channels,2022,ART,S02,10.55555/s02.2022.1317,,false,FEED
W927,A model of storm surge in the North Sea,2020,ART,S12,10.55555/s12.2020.8228,,false,FEED
W928,Observations of stratified flows in sandy coasts,2025,ART,S01,10.55555/s01.2025.7881,,false,FEED
W929,Scaling laws for coastal upwelling in shallow channels,2022,ART,S01,10.55555/s01.2022.8694,,false,FEED
W930,Revisiting internal waves in a laboratory flume,2025,ART,S10,10.55555/s10.2025.1395,,false,FEED
W931,Revisiting buoy telemetry,2023,ART,S02,10.55555/s02.2023.1282,,false,FEED
W932,Editorial: machine learning for wave runup in the Wexcombe marshes,2021,EDT,S11,10.55555/s11.2021.6896,,false,FEED
W933,Remote sensing of sensor calibration in the Brevin shelf,2021,ART,S03,10.55555/s03.2021.9638,,false,FEED
W934,Remote sensing of harbour seiches in tidal inlets,2023,ART,S08,10.55555/s08.2023.1324,,false,FEED
W935,Scaling laws for breaking waves in sandy coasts,2023,ART,S03,10.55555/s03.2023.5300,,false,FEED
W936,Editorial: fleet coordination,2019,EDT,S01,10.55555/s01.2019.1595,,false,FEED
W937,A model of estuarine salinity,2019,ART,S01,10.55555/s01.2019.4394,,false,FEED
W940,Low-cost methods for tidal asymmetry in a macrotidal bay,2022,ART,S10,10.55555/s10.2022.3098,,false,FEED
W941,Field measurements of bed shear stress in shallow channels,2022,ART,S02,10.55555/s02.2022.9549,,false,FEED
W942,Uncertainty in river plumes estimates in a macrotidal bay,2021,ART,S07,10.55555/s07.2021.7018,,false,FEED
W943,Observations of estuarine salinity in shallow channels,2020,ART,S10,10.55555/s10.2020.7216,,false,FEED
W944,Low-cost methods for harbour seiches in a laboratory flume,2019,ART,S07,10.55555/s07.2019.8059,,false,FEED
W945,Uncertainty in stratified flows estimates in a semi-enclosed sea,2023,SUP,S06,10.55555/s06.2023.1058,,false,FEED
W946,Low-cost methods for buoy telemetry in the Brevin shelf,2019,ART,S11,10.55555/s11.2019.8918,,false,FEED
W947,Long-term trends in tidal asymmetry in fjords,2021,ART,S11,10.55555/s11.2021.1096,,false,FEED
W948,A framework for wave runup in fjords,2021,ART,S01,10.55555/s01.2021.3775,,false,FEED
W949,Erratum: Observations of survey vessel autonomy in tidal inlets,2024,ERR,S02,10.55555/s02.2024.1996,,false,FEED
W950,A model of storm surge in mixed-energy coasts,2025,ART,S11,10.55555/s11.2025.9754,,false,FEED
W951,Machine learning for wave boundary layers in sandy coasts,2025,SUP,S06,10.55555/s06.2025.1638,,false,FEED
W953,Remote sensing of internal waves in harbour basins,2020,ART,S09,10.55555/s09.2020.4825,,false,FEED
W954,Observations of wave runup in sandy coasts,2024,ART,S09,10.55555/s09.2024.4003,,false,FEED
W955,Long-term trends in coastal upwelling in sandy coasts,2021,ART,S10,10.55555/s10.2021.7664,,false,FEED
W956,Long-term trends in breaking waves in a laboratory flume,2025,ART,S02,10.55555/s02.2025.8664,,false,FEED
W957,Observations of channel hydraulics,2024,ART,S03,10.55555/s03.2024.5461,,false,FEED
W958,Low-cost methods for underwater docking,2020,ART,S03,10.55555/s03.2020.1334,,false,FEED
W959,Editorial: long-term trends in wave runup in sandy coasts,2022,EDT,S12,10.55555/s12.2022.2759,,false,FEED
W960,Revisiting wave runup in shallow channels,2022,ART,S12,10.55555/s12.2022.5927,,false,FEED
W963,Observations of harbour seiches,2025,ART,S08,10.55555/s08.2025.4411,,false,FEED
W964,Revisiting marsh accretion in the open shelf: a review,2020,REV,S12,10.55555/s12.2020.1542,,false,FEED
W965,A model of breaking waves in the North Sea,2024,ART,S03,10.55555/s03.2024.6293,,false,FEED
W966,Editorial: scaling laws for river plumes in fjords,2024,EDT,S07,10.55555/s07.2024.3221,,false,FEED
W967,Seasonal variability in estuarine plumes in shallow channels,2022,ART,S06,10.55555/s06.2022.9084,,false,FEED
W968,Machine learning for sensor calibration in a laboratory flume,2023,ART,S09,10.55555/s09.2023.1201,,false,FEED
W969,Long-term trends in battery endurance in the Wexcombe marshes,2025,ART,S01,10.55555/s01.2025.7064,,false,FEED
W970,Long-term trends in vortex shedding in the Wexcombe marshes,2019,ART,S02,10.55555/s02.2019.4940,,false,FEED
W971,Long-term trends in sediment resuspension in the North Sea,2025,SUP,S01,10.55555/s01.2025.4830,,false,STG
W972,Long-term trends in acoustic positioning,2020,ART,S02,10.55555/s02.2020.5199,,false,FEED
W973,Uncertainty in glider navigation estimates in the Brevin shelf,2024,ART,S03,10.55555/s03.2024.2247,,true,FEED
W975,Remote sensing of acoustic positioning in the North Sea,2019,ART,S13,10.55555/s13.2019.2750,,false,FEED
W976,Foreword: sediment resuspension,2021,EDT,S06,10.55555/s06.2021.6763,,false,FEED
W977,Seasonal variability in coastal upwelling in sandy coasts,2022,ART,S11,10.55555/s11.2022.4113,,false,FEED
W978,Low-cost methods for river plumes in a laboratory flume,2020,ART,S12,10.55555/s12.2020.4935,,false,FEED
W979,Machine learning for battery endurance,2021,ART,S03,10.55555/s03.2021.9378,,false,FEED
W980,A framework for marsh accretion in harbour basins,2022,ART,S12,10.55555/s12.2022.7448,,false,FEED
W981,Remote sensing of wave boundary layers in the Wexcombe marshes,2021,ART,S02,10.55555/s02.2021.6786,,false,FEED
W983,Revisiting internal waves,2025,ART,S11,10.55555/s11.2025.6392,,false,FEED
W984,A model of survey vessel autonomy,2024,ART,S01,10.55555/s01.2024.8952,,false,FEED
W985,Remote sensing of vortex shedding,2023,ART,S09,10.55555/s09.2023.3775,,false,FEED
W986,Remote sensing of storm surge,2020,ART,S04,10.55555/s04.2020.2577,,false,FEED
W987,Machine learning for stratified flows,2025,ART,S02,10.55555/s02.2025.6401,,false,STG
W988,Observations of harbour seiches in the open shelf,2021,ART,S07,10.55555/s07.2021.3121,,false,FEED
W989,Editorial: long-term trends in marsh accretion in the Wexcombe marshes,2020,EDT,S08,10.55555/s08.2020.1702,,false,FEED
W990,Long-term trends in estuarine plumes in tidal inlets,2020,ART,S11,10.55555/s11.2020.4722,,false,FEED
W991,Editorial: revisiting estuarine salinity in a laboratory flume,2023,EDT,S07,10.55555/s07.2023.7046,,false,FEED
W992,Field measurements of harbour seiches in a laboratory flume,2025,ART,S07,10.55555/s07.2025.6267,,false,FEED
W993,Remote sensing of beach profiles in shallow channels,2025,ART,S07,10.55555/s07.2025.8965,,false,FEED
W994,Uncertainty in sediment flux estimates in a laboratory flume,2024,ART,S08,10.55555/s08.2024.6825,,false,FEED
W995,Low-cost methods for buoy telemetry in tidal inlets,2020,REV,S13,10.55555/s13.2020.7694,,false,FEED
W996,Uncertainty in stratified flows estimates in the open shelf,2021,ART,S02,10.55555/s02.2021.6321,,false,FEED
W997,Machine learning for breaking waves in harbour basins,2025,SUP,S01,10.55555/s01.2025.2096,,false,STG
W998,Machine learning for wave boundary layers in harbour basins,2022,ART,S01,10.55555/s01.2022.2392,,false,FEED
W1000,Low-cost methods for internal waves,2024,ART,S01,10.55555/s01.2024.3383,,false,FEED
W1001,Machine learning for harbour seiches in mixed-energy coasts,2024,ART,S09,10.55555/s09.2024.3946,,false,FEED
W1002,A framework for dune erosion,2021,SUP,S06,10.55555/s06.2021.1124,,false,FEED
W1003,Field measurements of sensor calibration in the North Sea,2024,ART,S06,10.55555/s06.2024.1859,,false,FEED
W1004,Revisiting acoustic positioning,2024,ART,S02,10.55555/s02.2024.4429,,false,FEED
W1005,Remote sensing of buoy telemetry in fjords,2025,ART,S02,10.55555/s02.2025.1967,,false,FEED
W1006,Seasonal variability in acoustic positioning in a laboratory flume,2020,REV,S13,10.55555/s13.2020.7568,,false,FEED
W1007,A model of storm surge in sandy coasts,2023,ART,S01,10.55555/s01.2023.1365,,false,FEED
W1008,Machine learning for beach profiles in sandy coasts,2025,ART,S11,10.55555/s11.2025.3712,,false,FEED
W1009,Revisiting sediment flux in the open shelf: a review,2022,REV,S12,10.55555/s12.2022.6992,,false,FEED
W1010,Revisiting vortex shedding in mixed-energy coasts,2020,ART,S02,10.55555/s02.2020.9834,,false,FEED
W1011,Scaling laws for fleet coordination in harbour basins,2021,REV,S04,10.55555/s04.2021.3412,,false,FEED
W1012,Seasonal variability in marsh accretion in the Wexcombe marshes,2020,ART,S08,10.55555/s08.2020.9973,,false,FEED
W1013,Revisiting battery endurance in sandy coasts,2025,ART,S04,10.55555/s04.2025.2015,,false,FEED
W1014,A model of sensor calibration in the North Sea,2023,ART,S01,10.55555/s01.2023.5712,,false,FEED
W1015,Revisiting tidal asymmetry in mixed-energy coasts,2023,ART,S12,10.55555/s12.2023.6449,,false,FEED
W1016,Scaling laws for bed shear stress in a laboratory flume,2025,ART,S06,10.55555/s06.2025.4466,,false,FEED
W1017,A model of tidal asymmetry in tidal inlets,2025,ART,S07,10.55555/s07.2025.7453,,false,FEED
W1018,Remote sensing of estuarine salinity in the Brevin shelf,2025,ART,S08,10.55555/s08.2025.8885,,false,FEED
W1019,Seasonal variability in coastal upwelling in mixed-energy coasts,2020,ART,S03,10.55555/s03.2020.9079,,false,FEED
W1020,Machine learning for vortex shedding in mixed-energy coasts,2020,ART,S13,10.55555/s13.2020.9111,,false,FEED
W1021,Long-term trends in wave boundary layers,2021,ART,S02,10.55555/s02.2021.1763,,false,FEED
W1022,Uncertainty in storm surge estimates in the Wexcombe marshes,2023,ART,S09,10.55555/s09.2023.6605,,false,FEED
W1023,A model of beach profiles in mixed-energy coasts,2024,ART,S09,10.55555/s09.2024.2222,,false,FEED
W1024,Long-term trends in dune erosion in sandy coasts,2020,ART,S12,10.55555/s12.2020.6578,,false,FEED
W1025,Long-term trends in stratified flows,2020,ART,S02,10.55555/s02.2020.8833,,true,FEED
W1026,A model of dune erosion in a macrotidal bay,2019,ART,S09,10.55555/s09.2019.7972,,false,FEED
W1027,Low-cost methods for bed shear stress in fjords: a review,2024,REV,S10,10.55555/s10.2024.9692,,false,FEED
W1028,A model of wave runup in mixed-energy coasts,2019,ART,S03,10.55555/s03.2019.6764,,false,FEED
W1029,Seasonal variability in coastal upwelling in the open shelf,2022,ART,S09,10.55555/s09.2022.3414,,false,FEED
W1030,Low-cost methods for storm surge in the open shelf,2021,ART,S12,10.55555/s12.2021.9246,,false,FEED
W1031,Remote sensing of internal waves in the open shelf,2025,ART,S01,10.55555/s01.2025.6020,,false,FEED
W1032,Low-cost methods for coastal upwelling,2019,ART,S02,10.55555/s02.2019.6372,,false,FEED
W1033,Machine learning for tidal asymmetry,2025,ART,S08,10.55555/s08.2025.1174,,false,FEED
W1034,Foreword: tidal mixing,2025,EDT,S06,10.55555/s06.2025.1338,,false,FEED
W1035,Uncertainty in ocean optics estimates in the Brevin shelf,2021,ART,S03,10.55555/s03.2021.2698,,false,FEED
W1036,Uncertainty in bed shear stress estimates in the Albury estuary,2024,ART,S06,10.55555/s06.2024.2520,,false,FEED
W1037,Low-cost methods for harbour seiches in the Wexcombe marshes,2022,ART,S02,10.55555/s02.2022.9954,,true,FEED
W1038,Low-cost methods for marsh accretion,2020,ART,S02,10.55555/s02.2020.7315,,false,FEED
W1039,Revisiting vortex shedding in sandy coasts,2023,ART,S11,10.55555/s11.2023.6380,,false,FEED
W1040,Field measurements of storm surge,2024,ART,S08,10.55555/s08.2024.3437,,false,FEED
W1041,Editorial: survey vessel autonomy,2025,EDT,S03,10.55555/s03.2025.1894,,false,FEED
W1042,Revisiting seabed classification in a semi-enclosed sea,2025,ART,S01,10.55555/s01.2025.1941,,false,FEED
W1043,Editorial: machine learning for sediment flux,2023,EDT,S08,10.55555/s08.2023.2973,,false,FEED
W1044,Machine learning for acoustic positioning in harbour basins,2021,ART,S02,10.55555/s02.2021.7797,,false,FEED
W1046,Low-cost methods for vortex shedding in a laboratory flume,2024,ART,S01,10.55555/s01.2024.6960,,false,FEED
W1047,Scaling laws for sediment flux,2020,ART,S09,10.55555/s09.2020.3720,,false,FEED
W1048,Long-term trends in fleet coordination in shallow channels,2023,ART,S10,10.55555/s10.2023.6080,,false,FEED
W1049,Field measurements of tidal mixing,2021,PPR,S14,10.55555/s14.2021.1460,W789,false,FEED
W1050,Low-cost methods for glider navigation in the Wexcombe marshes,2024,ART,S09,10.55555/s09.2024.6796,,false,FEED
W1051,Machine learning for estuarine salinity,2020,ART,S03,10.55555/s03.2020.2154,,false,FEED
W1052,Long-term trends in buoy telemetry in the North Sea,2019,ART,S03,10.55555/s03.2019.3020,,false,FEED
W1053,Remote sensing of tidal asymmetry in harbour basins: a review,2019,REV,S01,10.55555/s01.2019.7693,,false,FEED
W1054,A framework for sonar imaging in the Brevin shelf,2021,PPR,S05,10.55555/s05.2021.4988,,false,FEED
W1056,A model of sonar imaging,2023,ART,S02,10.55555/s02.2023.2546,,false,FEED
W1058,A model of turbidity sensing,2021,ART,S11,10.55555/s11.2021.2492,,false,FEED
W1060,Machine learning for tidal mixing,2020,ART,S11,10.55555/s11.2020.6305,,false,FEED
W1061,Remote sensing of turbidity sensing in shallow channels,2023,ART,S01,10.55555/s01.2023.6359,,false,FEED
W1062,Seasonal variability in wave runup in sandy coasts: a review,2019,REV,S02,10.55555/s02.2019.7336,,false,FEED
W1063,Low-cost methods for fleet coordination in a macrotidal bay,2019,ART,S02,10.55555/s02.2019.5813,,false,FEED
W1064,Seasonal variability in marsh accretion,2019,ART,S07,10.55555/s07.2019.5586,,false,FEED
W1065,Revisiting sensor calibration,2020,ART,S02,10.55555/s02.2020.2079,,false,FEED
```

### authorships.csv
```csv
work_id,author_id,author_position,institution_id,affil_seq
W01,A01,1,I02,1
W01,A07,2,I03,1
W02,A02,1,I02,1
W02,A07,2,I03,1
W03,A03,1,I02,1
W03,A07,2,I03,1
W04,A01,1,I02,1
W05,A01,1,I02,1
W05,A07,2,I03,1
W06,A01,1,I02,1
W06,A15,2,I13,1
W07,A02,1,I02,1
W08,A04,1,I07,1
W12,A01,1,I02,1
W12,A16,2,I05,1
W13,A07,1,I03,1
W14,A05,1,I05,1
W15,A15,1,I13,1
W16,A04,1,I07,1
W17,A13,1,I11,1
W18,A11,1,I09,1
W19,A02,1,I02,1
W20,A09,1,I07,1
W20,A13,2,I11,1
W21,A10,1,I08,1
W21,A09,2,I07,1
W21,A11,3,I09,1
W21,A12,4,I10,1
W22,A09,1,I07,1
W23,A09,1,I07,1
W24,A10,1,I08,1
W27,A18,1,I09,1
W27,A13,2,I11,1
W27,A14,3,I12,1
W27,A17,4,I14,1
W28,A19,1,I09,1
W28,A15,2,I13,1
W28,A16,3,I05,1
W28,A06,4,I12,1
W29,A20,1,I09,1
W29,A16,2,I05,1
W29,A15,3,I13,1
W29,A13,4,I11,1
W30,A15,1,I13,1
W31,A17,1,I14,1
W32,A11,1,I09,1
W32,A18,2,I09,1
W32,A19,3,I09,1
W32,A20,4,I09,1
W33,A14,1,I12,1
W34,A06,1,I12,1
W35,A14,1,I12,1
W36,A13,1,I11,1
W37,A05,1,I05,1
W38,A06,1,I12,1
W39,A17,1,I14,1
W40,A11,1,I09,1
W41,A14,1,I12,1
W42,A17,1,I14,1
W50,A17,1,I14,1
W51,A12,1,I10,1
W52,A13,1,I11,1
W60,A34,1,I15,1
W61,A38,1,I15,1
W61,A35,2,I16,1
W62,A34,1,I15,1
W62,A38,2,I15,1
W63,A33,1,I18,1
W63,A34,2,I15,1
W63,A44,3,I17,1
W64,A40,1,I17,1
W65,A36,1,I17,1
W65,A45,2,I18,1
W65,A35,3,I16,1
W66,A38,1,I15,1
W67,A45,1,I18,1
W67,A35,2,I16,1
W70,A08,1,I04,1
W70,A08,1,I06,2
W71,A08,1,I06,1
W71,A08,1,I04,2
W72,A08,1,I04,1
W72,A07,2,I03,1
W73,A08,1,I06,1
W74,A22,1,I06,1
W75,A15,1,I13,1
W90,A21,1,I07,1
W91,A21,1,I07,1
W92,A21,1,I07,1
W101,A30,1,I15,1
W101,A42,2,I15,1
W102,A36,1,I17,1
W102,A38,2,I15,1
W102,A42,3,I15,1
W103,A35,1,I16,1
W103,A41,2,I18,1
W103,A34,3,I15,1
W104,A37,1,I18,1
W104,A44,2,I17,1
W104,A45,3,I18,1
W105,A31,1,I16,1
W105,A40,2,I17,1
W106,A38,1,I15,1
W106,A45,2,I18,1
W107,A32,1,I17,1
W107,A43,2,I16,1
W108,A35,1,I16,1
W108,A42,2,I15,1
W108,A34,3,I15,1
W109,A36,1,I17,1
W109,A42,2,I15,1
W109,A43,3,I16,1
W110,A34,1,I15,1
W111,A34,1,I15,1
W112,A45,1,I18,1
W112,A44,2,I17,1
W113,A43,1,I16,1
W113,A32,2,I17,1
W114,A38,1,I15,1
W114,A35,2,I16,1
W114,A42,3,I15,1
W115,A35,1,I16,1
W116,A44,1,I17,1
W116,A43,2,I16,1
W117,A36,1,I17,1
W118,A35,1,I16,1
W119,A41,1,I18,1
W119,A36,2,I17,1
W120,A37,1,I18,1
W121,A32,1,I17,1
W121,A37,2,I18,1
W122,A32,1,I17,1
W123,A45,1,I18,1
W123,A38,2,I15,1
W123,A30,3,I15,1
W124,A31,1,I16,1
W125,A37,1,I18,1
W125,A36,2,I17,1
W201,A223,1,I30,1
W203,A10,1,I08,1
W203,A09,2,I07,1
W203,A139,3,I07,1
W203,A144,4,I08,1
W203,A143,5,I08,1
W203,A225,6,I28,1
W204,A227,1,I31,1
W204,A184,2,I15,1
W205,A123,1,I19,1
W205,A115,2,I03,1
W205,A113,3,I02,1
W206,A03,1,I02,1
W206,A123,2,I19,1
W208,A124,1,I19,1
W208,A229,2,I17,1
W209,A17,1,I14,1
W210,A102,1,I09,1
W211,A169,1,I13,1
W214,A129,1,I05,1
W214,A129,1,I13,2
W215,A177,1,I25,1
W216,A155,1,I12,1
W216,A156,2,I12,1
W217,A160,1,I11,1
W218,A218,1,I25,1
W219,A07,1,I03,1
W219,A125,2,I19,1
W220,A227,1,I31,1
W221,A188,1,I24,1
W222,A188,1,I24,1
W222,A199,2,I18,1
W222,A186,3,I17,1
W223,A190,1,I26,1
W223,A210,2,I17,1
W224,A177,1,I25,1
W225,A17,1,I14,1
W226,A145,1,I08,1
W227,A146,1,I22,1
W227,A176,2,I24,1
W228,A39,1,I16,1
W228,A185,2,I16,1
W228,A202,3,I26,1
W229,A160,1,I11,1
W230,A160,1,I11,1
W230,A161,2,I11,1
W232,A09,1,I07,1
W232,A137,2,I07,1
W233,A110,1,I02,1
W233,A125,2,I19,1
W235,A189,1,I25,1
W235,A194,2,I30,1
W237,A184,1,I15,1
W237,A208,2,I15,1
W238,A01,1,I02,1
W238,A111,2,I02,1
W238,A32,3,I17,1
W239,A172,1,I15,1
W239,A227,2,I31,1
W241,A128,1,I05,1
W241,A16,2,I05,1
W241,A127,3,I05,1
W242,A105,1,I14,1
W243,A114,1,I02,1
W243,A119,2,I04,1
W246,A221,1,I30,1
W247,A222,1,I31,1
W249,A17,1,I14,1
W251,A07,1,I03,1
W251,A125,2,I19,1
W252,A106,1,I04,1
W252,A106,1,I06,2
W253,A217,1,I29,1
W253,A211,2,I18,1
W253,A229,3,I17,1
W254,A36,1,I17,1
W254,A214,2,I26,1
W254,A204,3,I28,1
W255,A15,1,I13,1
W256,A130,1,I20,1
W256,A159,2,I12,1
W257,A200,1,I24,1
W258,A36,1,I17,1
W258,A201,2,I25,1
W259,A201,1,I25,1
W260,A10,1,I08,1
W260,A141,2,I07,1
W261,A33,1,I18,1
W261,A175,2,I18,1
W262,A07,1,I03,1
W262,A194,2,I30,1
W263,A163,1,I14,1
W264,A144,1,I08,1
W264,A141,2,I07,1
W265,A226,1,I24,1
W266,A149,1,I09,1
W266,A229,2,I17,1
W266,A209,3,I16,1
W266,A43,4,I16,1
W267,A138,1,I07,1
W268,A09,1,I07,1
W268,A109,2,I07,1
W269,A36,1,I17,1
W269,A220,2,I26,1
W269,A206,3,I30,1
W270,A159,1,I12,1
W270,A158,2,I12,1
W270,A227,3,I31,1
W271,A01,1,I02,1
W272,A215,1,I27,1
W272,A221,2,I30,1
W273,A110,1,I02,1
W273,A163,2,I14,1
W274,A15,1,I13,1
W275,A185,1,I16,1
W275,A195,2,I31,1
W276,A158,1,I12,1
W276,A157,2,I12,1
W277,A191,1,I27,1
W278,A185,1,I16,1
W279,A163,1,I14,1
W281,A138,1,I07,1
W281,A139,2,I07,1
W282,A155,1,I12,1
W284,A44,1,I17,1
W284,A43,2,I16,1
W285,A153,1,I23,1
W289,A207,1,I31,1
W289,A201,2,I25,1
W291,A45,1,I18,1
W292,A07,1,I03,1
W292,A155,2,I12,1
W293,A07,1,I03,1
W293,A125,2,I19,1
W294,A15,1,I13,1
W294,A167,2,I13,1
W296,A130,1,I20,1
W296,A219,2,I30,1
W297,A139,1,I12,1
W297,A139,1,I07,2
W299,A191,1,I27,1
W300,A158,1,I12,1
W301,A143,1,I08,1
W301,A140,2,I07,1
W301,A176,3,I24,1
W302,A158,1,I12,1
W303,A162,1,I11,1
W303,A14,2,I12,1
W303,A157,3,I12,1
W304,A133,1,I21,1
W304,A132,2,I21,1
W304,A190,3,I26,1
W305,A222,1,I31,1
W306,A130,1,I20,1
W306,A127,2,I05,1
W308,A117,1,I03,1
W308,A124,2,I19,1
W308,A40,3,I17,1
W309,A14,1,I12,1
W310,A194,1,I30,1
W312,A165,1,I14,1
W313,A166,1,I14,1
W313,A163,2,I14,1
W314,A131,1,I20,1
W314,A129,2,I05,1
W314,A212,3,I24,1
W315,A122,1,I19,1
W317,A198,1,I17,1
W317,A204,2,I28,1
W317,A212,3,I24,1
W318,A164,1,I14,1
W318,A163,2,I14,1
W319,A128,1,I05,1
W320,A41,1,I18,1
W321,A17,1,I14,1
W321,A164,2,I14,1
W322,A118,1,I03,1
W322,A110,2,I02,1
W322,A32,3,I17,1
W323,A177,1,I25,1
W324,A229,1,I17,1
W325,A10,1,I07,1
W326,A192,1,I28,1
W329,A21,1,I07,1
W330,A30,1,I15,1
W330,A218,2,I25,1
W331,A169,1,I13,1
W332,A33,1,I18,1
W332,A228,2,I24,1
W332,A214,3,I26,1
W333,A145,1,I08,1
W334,A157,1,I12,1
W335,A214,1,I26,1
W336,A198,1,I17,1
W337,A211,1,I18,1
W338,A15,1,I13,1
W338,A167,2,I13,1
W339,A184,1,I15,1
W341,A145,1,I08,1
W341,A136,2,I07,1
W342,A136,1,I22,1
W342,A136,1,I07,2
W343,A160,1,I11,1
W344,A13,1,I11,1
W345,A42,1,I15,1
W346,A126,1,I05,1
W348,A118,1,I03,1
W348,A123,2,I19,1
W348,A121,3,I04,1
W349,A130,1,I20,1
W350,A118,1,I03,1
W350,A110,2,I02,1
W350,A116,3,I03,1
W352,A210,1,I17,1
W352,A40,2,I17,1
W354,A152,1,I09,1
W355,A123,1,I19,1
W356,A128,1,I05,1
W357,A20,1,I09,1
W357,A11,2,I09,1
W357,A102,3,I09,1
W357,A148,4,I09,1
W358,A217,1,I29,1
W358,A213,2,I25,1
W358,A199,3,I18,1
W359,A158,1,I12,1
W359,A159,2,I12,1
W361,A14,1,I12,1
W361,A155,2,I12,1
W362,A36,1,I17,1
W365,A138,1,I22,1
W365,A138,1,I07,2
W366,A09,1,I07,1
W366,A219,2,I30,1
W367,A151,1,I09,1
W367,A154,2,I23,1
W367,A11,3,I09,1
W367,A18,4,I09,1
W368,A114,1,I02,1
W369,A180,1,I28,1
W369,A185,2,I16,1
W369,A198,3,I17,1
W370,A111,1,I02,1
W370,A113,2,I02,1
W370,A224,3,I16,1
W371,A32,1,I17,1
W371,A179,2,I27,1
W372,A21,1,I07,1
W373,A34,1,I15,1
W374,A01,1,I02,1
W374,A114,2,I02,1
W376,A215,1,I27,1
W376,A203,2,I27,1
W377,A173,1,I16,1
W378,A22,1,I06,1
W378,A135,2,I06,1
W380,A206,1,I30,1
W380,A200,2,I24,1
W380,A174,3,I17,1
W382,A184,1,I15,1
W383,A110,1,I02,1
W383,A118,2,I03,1
W383,A222,3,I31,1
W384,A06,1,I12,1
W384,A157,2,I12,1
W385,A113,1,I02,1
W385,A173,2,I16,1
W387,A40,1,I17,1
W388,A131,1,I20,1
W388,A37,2,I18,1
W389,A186,1,I17,1
W389,A213,2,I25,1
W390,A18,1,I09,1
W390,A20,2,I09,1
W390,A151,3,I09,1
W390,A148,4,I09,1
W390,A33,5,I18,1
W392,A192,1,I28,1
W392,A180,2,I28,1
W393,A187,1,I18,1
W393,A31,2,I16,1
W396,A15,1,I13,1
W396,A168,2,I13,1
W397,A109,1,I07,1
W398,A36,1,I17,1
W399,A207,1,I31,1
W399,A223,2,I30,1
W399,A173,3,I16,1
W400,A171,1,I10,1
W400,A12,2,I10,1
W400,A170,3,I10,1
W401,A146,1,I22,1
W401,A147,2,I22,1
W402,A169,1,I13,1
W402,A176,2,I24,1
W403,A209,1,I16,1
W403,A205,2,I29,1
W404,A205,1,I29,1
W404,A189,2,I25,1
W404,A219,3,I30,1
W405,A163,1,I14,1
W406,A178,1,I26,1
W407,A143,1,I08,1
W407,A145,2,I08,1
W408,A39,1,I16,1
W408,A216,2,I28,1
W410,A127,1,I05,1
W411,A20,1,I09,1
W411,A18,2,I09,1
W413,A126,1,I05,1
W413,A16,2,I05,1
W414,A207,1,I31,1
W414,A182,2,I30,1
W415,A36,1,I17,1
W415,A212,2,I24,1
W416,A115,1,I03,1
W416,A37,2,I18,1
W417,A09,1,I07,1
W417,A143,2,I08,1
W418,A162,1,I11,1
W419,A137,1,I07,1
W419,A140,2,I07,1
W419,A12,3,I10,1
W420,A127,1,I05,1
W420,A127,1,I21,2
W421,A147,1,I22,1
W422,A152,1,I09,1
W422,A102,2,I09,1
W423,A212,1,I24,1
W424,A218,1,I25,1
W424,A198,2,I17,1
W425,A156,1,I12,1
W425,A14,2,I12,1
W425,A225,3,I28,1
W426,A08,1,I06,1
W426,A08,1,I04,2
W426,A114,2,I02,1
W427,A182,1,I30,1
W428,A04,1,I07,1
W428,A174,2,I17,1
W430,A200,1,I24,1
W431,A188,1,I24,1
W432,A13,1,I11,1
W432,A159,2,I12,1
W433,A40,1,I17,1
W434,A166,1,I14,1
W434,A165,2,I14,1
W434,A163,3,I14,1
W434,A31,4,I16,1
W435,A07,1,I03,1
W435,A125,2,I19,1
W436,A18,1,I09,1
W436,A182,2,I30,1
W436,A219,3,I30,1
W436,A197,4,I16,1
W437,A176,1,I24,1
W437,A108,2,I16,1
W438,A170,1,I10,1
W438,A12,2,I10,1
W439,A185,1,I16,1
W440,A212,1,I24,1
W441,A128,1,I05,1
W442,A228,1,I24,1
W443,A186,1,I17,1
W443,A226,2,I24,1
W444,A10,1,I08,1
W445,A13,1,I11,1
W445,A167,2,I13,1
W446,A155,1,I12,1
W446,A156,2,I12,1
W448,A129,1,I05,1
W449,A02,1,I02,1
W450,A143,1,I08,1
W450,A141,2,I07,1
W451,A207,1,I31,1
W451,A178,2,I26,1
W451,A181,3,I29,1
W452,A119,1,I04,1
W452,A124,2,I19,1
W452,A204,3,I28,1
W453,A118,1,I03,1
W453,A110,2,I02,1
W453,A32,3,I17,1
W454,A143,1,I08,1
W454,A137,2,I07,1
W455,A129,1,I05,1
W456,A182,1,I30,1
W457,A42,1,I15,1
W458,A43,1,I16,1
W458,A44,2,I17,1
W458,A205,3,I29,1
W459,A163,1,I14,1
W460,A12,1,I10,1
W460,A171,2,I10,1
W461,A200,1,I24,1
W462,A155,1,I12,1
W463,A114,1,I02,1
W463,A120,2,I04,1
W464,A01,1,I02,1
W464,A224,2,I16,1
W465,A115,1,I03,1
W466,A192,1,I28,1
W467,A169,1,I13,1
W469,A201,1,I25,1
W469,A185,2,I16,1
W469,A223,3,I30,1
W470,A182,1,I30,1
W471,A44,1,I17,1
W471,A35,2,I16,1
W473,A10,1,I08,1
W474,A118,1,I03,1
W474,A113,2,I02,1
W475,A218,1,I25,1
W476,A163,1,I14,1
W477,A164,1,I14,1
W478,A103,1,I08,1
W478,A103,1,I07,2
W479,A147,1,I22,1
W480,A20,1,I09,1
W481,A111,1,I02,1
W481,A120,2,I04,1
W481,A34,3,I15,1
W483,A181,1,I29,1
W484,A14,1,I12,1
W485,A45,1,I18,1
W485,A41,2,I18,1
W486,A131,1,I20,1
W487,A102,1,I09,1
W487,A195,2,I31,1
W487,A177,3,I25,1
W487,A221,4,I30,1
W488,A21,1,I07,1
W489,A218,1,I25,1
W491,A38,1,I15,1
W492,A177,1,I25,1
W492,A197,2,I16,1
W493,A212,1,I24,1
W493,A35,2,I16,1
W496,A12,1,I10,1
W496,A171,2,I10,1
W497,A20,1,I09,1
W497,A189,2,I25,1
W497,A33,3,I18,1
W497,A165,4,I14,1
W498,A222,1,I31,1
W498,A182,2,I30,1
W499,A111,1,I02,1
W499,A112,2,I02,1
W499,A121,3,I04,1
W500,A15,1,I13,1
W500,A163,2,I14,1
W501,A115,1,I03,1
W502,A22,1,I06,1
W502,A134,2,I06,1
W502,A221,3,I30,1
W503,A111,1,I02,1
W503,A171,2,I10,1
W504,A10,1,I08,1
W505,A220,1,I26,1
W506,A152,1,I09,1
W506,A102,2,I09,1
W507,A214,1,I26,1
W507,A173,2,I16,1
W508,A224,1,I16,1
W509,A183,1,I31,1
W509,A108,2,I16,1
W509,A198,3,I17,1
W510,A140,1,I07,1
W510,A144,2,I08,1
W511,A41,1,I18,1
W512,A198,1,I17,1
W512,A41,2,I18,1
W513,A117,1,I03,1
W515,A159,1,I12,1
W516,A156,1,I12,1
W516,A157,2,I12,1
W516,A158,3,I12,1
W518,A143,1,I08,1
W518,A163,2,I14,1
W519,A189,1,I25,1
W519,A217,2,I29,1
W520,A155,1,I12,1
W521,A200,1,I24,1
W521,A209,2,I16,1
W521,A211,3,I18,1
W522,A165,1,I14,1
W523,A116,1,I03,1
W523,A121,2,I04,1
W523,A203,3,I27,1
W524,A167,1,I13,1
W524,A15,2,I13,1
W525,A06,1,I12,1
W525,A158,2,I12,1
W526,A223,1,I30,1
W527,A122,1,I19,1
W527,A117,2,I03,1
W528,A140,1,I07,1
W529,A130,1,I20,1
W529,A221,2,I30,1
W530,A140,1,I07,1
W530,A145,2,I08,1
W531,A103,1,I08,1
W531,A103,1,I07,2
W532,A184,1,I15,1
W533,A149,1,I09,1
W533,A161,2,I11,1
W534,A36,1,I17,1
W534,A180,2,I28,1
W534,A228,3,I24,1
W535,A168,1,I13,1
W535,A160,2,I11,1
W536,A45,1,I18,1
W536,A211,2,I18,1
W538,A192,1,I28,1
W538,A43,2,I16,1
W539,A152,1,I09,1
W539,A107,2,I09,1
W539,A30,3,I15,1
W540,A203,1,I27,1
W541,A214,1,I26,1
W542,A218,1,I25,1
W542,A202,2,I26,1
W544,A127,1,I05,1
W544,A128,2,I05,1
W545,A160,1,I11,1
W545,A155,2,I12,1
W545,A157,3,I12,1
W545,A228,4,I24,1
W546,A158,1,I12,1
W547,A212,1,I24,1
W547,A174,2,I17,1
W547,A190,3,I26,1
W548,A192,1,I28,1
W548,A33,2,I18,1
W549,A107,1,I09,1
W549,A163,2,I14,1
W549,A217,3,I29,1
W549,A208,4,I15,1
W550,A192,1,I28,1
W550,A213,2,I25,1
W550,A182,3,I30,1
W551,A221,1,I30,1
W552,A179,1,I27,1
W552,A202,2,I26,1
W553,A07,1,I03,1
W554,A05,1,I05,1
W555,A101,1,I02,1
W555,A123,2,I19,1
W556,A104,1,I05,1
W556,A164,2,I14,1
W557,A161,1,I11,1
W557,A160,2,I11,1
W558,A176,1,I24,1
W559,A212,1,I24,1
W560,A163,1,I14,1
W560,A164,2,I14,1
W560,A185,3,I16,1
W562,A34,1,I15,1
W563,A14,1,I12,1
W564,A110,1,I02,1
W564,A120,2,I04,1
W565,A05,1,I05,1
W566,A129,1,I05,1
W566,A130,2,I20,1
W567,A167,1,I13,1
W568,A112,1,I02,1
W568,A122,2,I19,1
W568,A110,3,I02,1
W569,A21,1,I07,1
W570,A176,1,I24,1
W570,A204,2,I28,1
W570,A31,3,I16,1
W571,A164,1,I14,1
W571,A195,2,I31,1
W572,A182,1,I30,1
W573,A21,1,I07,1
W574,A147,1,I22,1
W575,A219,1,I30,1
W575,A178,2,I26,1
W576,A19,1,I09,1
W576,A107,2,I09,1
W576,A151,3,I09,1
W576,A11,4,I09,1
W578,A154,1,I23,1
W578,A191,2,I27,1
W578,A173,3,I16,1
W578,A164,4,I14,1
W579,A34,1,I15,1
W579,A198,2,I17,1
W579,A31,3,I16,1
W580,A180,1,I28,1
W580,A202,2,I26,1
W581,A31,1,I16,1
W582,A109,1,I07,1
W583,A173,1,I16,1
W583,A42,2,I15,1
W584,A182,1,I30,1
W584,A211,2,I18,1
W585,A125,1,I19,1
W586,A152,1,I09,1
W586,A11,2,I09,1
W586,A154,3,I23,1
W586,A148,4,I09,1
W587,A42,1,I15,1
W587,A207,2,I31,1
W588,A117,1,I03,1
W588,A118,2,I03,1
W589,A14,1,I12,1
W589,A156,2,I12,1
W592,A155,1,I12,1
W593,A224,1,I16,1
W594,A120,1,I04,1
W594,A117,2,I03,1
W595,A141,1,I07,1
W598,A07,1,I03,1
W599,A146,1,I22,1
W601,A41,1,I18,1
W601,A181,2,I29,1
W602,A195,1,I31,1
W602,A184,2,I15,1
W603,A04,1,I07,1
W605,A169,1,I13,1
W606,A105,1,I14,1
W606,A163,2,I14,1
W607,A194,1,I30,1
W607,A214,2,I26,1
W608,A111,1,I02,1
W609,A37,1,I18,1
W609,A221,2,I30,1
W610,A21,1,I07,1
W611,A143,1,I08,1
W611,A140,2,I07,1
W611,A176,3,I24,1
W612,A101,1,I02,1
W612,A125,2,I19,1
W612,A191,3,I27,1
W613,A106,1,I06,1
W613,A106,1,I04,2
W613,A110,2,I02,1
W614,A175,1,I18,1
W614,A179,2,I27,1
W615,A108,1,I16,1
W616,A215,1,I27,1
W616,A40,2,I17,1
W617,A106,1,I04,1
W617,A106,1,I06,2
W618,A221,1,I30,1
W618,A194,2,I30,1
W619,A199,1,I18,1
W620,A220,1,I26,1
W620,A182,2,I30,1
W621,A156,1,I12,1
W623,A196,1,I15,1
W623,A33,2,I18,1
W624,A137,1,I07,1
W624,A145,2,I08,1
W625,A146,1,I22,1
W626,A167,1,I13,1
W627,A220,1,I26,1
W627,A31,2,I16,1
W627,A205,3,I29,1
W628,A186,1,I17,1
W628,A180,2,I28,1
W629,A175,1,I18,1
W629,A217,2,I29,1
W629,A225,3,I28,1
W630,A38,1,I15,1
W631,A102,1,I09,1
W631,A212,2,I24,1
W631,A34,3,I15,1
W631,A213,4,I25,1
W632,A134,1,I06,1
W632,A22,2,I06,1
W632,A183,3,I31,1
W633,A162,1,I11,1
W635,A08,1,I06,1
W635,A08,1,I04,2
W636,A39,1,I16,1
W637,A187,1,I18,1
W637,A181,2,I29,1
W637,A209,3,I16,1
W638,A108,1,I16,1
W638,A215,2,I27,1
W638,A228,3,I24,1
W639,A141,1,I07,1
W639,A136,2,I07,1
W640,A115,1,I03,1
W640,A37,2,I18,1
W641,A172,1,I15,1
W641,A219,2,I30,1
W642,A33,1,I18,1
W642,A177,2,I25,1
W643,A20,1,I09,1
W643,A11,2,I09,1
W643,A151,3,I09,1
W643,A18,4,I09,1
W643,A176,5,I24,1
W644,A206,1,I30,1
W644,A199,2,I18,1
W645,A197,1,I16,1
W646,A16,1,I05,1
W646,A126,2,I05,1
W646,A128,3,I05,1
W648,A127,1,I05,1
W649,A20,1,I09,1
W650,A229,1,I17,1
W650,A224,2,I16,1
W651,A20,1,I09,1
W651,A154,2,I23,1
W652,A228,1,I24,1
W654,A151,1,I09,1
W654,A39,2,I16,1
W654,A227,3,I31,1
W654,A162,4,I11,1
W655,A157,1,I12,1
W655,A156,2,I12,1
W656,A08,1,I06,1
W656,A08,1,I04,2
W657,A17,1,I14,1
W657,A163,2,I14,1
W659,A111,1,I02,1
W659,A120,2,I04,1
W659,A118,3,I03,1
W660,A169,1,I13,1
W660,A167,2,I13,1
W661,A110,1,I02,1
W662,A200,1,I24,1
W662,A44,2,I17,1
W663,A02,1,I02,1
W663,A224,2,I16,1
W664,A08,1,I04,1
W664,A08,1,I06,2
W664,A22,2,I06,1
W665,A164,1,I14,1
W666,A133,1,I21,1
W666,A200,2,I24,1
W667,A175,1,I18,1
W667,A198,2,I17,1
W667,A181,3,I29,1
W668,A31,1,I16,1
W668,A207,2,I31,1
W669,A40,1,I17,1
W669,A217,2,I29,1
W670,A164,1,I14,1
W670,A166,2,I14,1
W670,A17,3,I14,1
W670,A213,4,I25,1
W671,A08,1,I04,1
W671,A08,1,I06,2
W672,A22,1,I06,1
W672,A134,2,I06,1
W672,A176,3,I24,1
W673,A130,1,I20,1
W675,A141,1,I07,1
W675,A166,2,I14,1
W676,A01,1,I02,1
W678,A162,1,I11,1
W679,A126,1,I05,1
W680,A109,1,I07,1
W681,A114,1,I02,1
W681,A216,2,I28,1
W682,A224,1,I16,1
W682,A204,2,I28,1
W683,A183,1,I31,1
W684,A102,1,I09,1
W684,A226,2,I24,1
W684,A174,3,I17,1
W684,A187,4,I18,1
W685,A229,1,I17,1
W686,A103,1,I08,1
W686,A103,1,I07,2
W686,A137,2,I07,1
W686,A168,3,I13,1
W688,A220,1,I26,1
W688,A183,2,I31,1
W690,A118,1,I03,1
W691,A123,1,I19,1
W691,A125,2,I19,1
W692,A208,1,I15,1
W692,A196,2,I15,1
W692,A207,3,I31,1
W693,A103,1,I07,1
W696,A18,1,I09,1
W696,A102,2,I09,1
W696,A152,3,I09,1
W696,A150,4,I09,1
W697,A145,1,I08,1
W699,A229,1,I17,1
W699,A39,2,I16,1
W700,A109,1,I07,1
W702,A104,1,I05,1
W703,A219,1,I30,1
W703,A208,2,I15,1
W703,A220,3,I26,1
W704,A223,1,I30,1
W705,A137,1,I07,1
W705,A141,2,I07,1
W706,A30,1,I15,1
W707,A140,1,I07,1
W707,A142,2,I08,1
W709,A39,1,I16,1
W709,A203,2,I27,1
W710,A145,1,I08,1
W711,A156,1,I12,1
W713,A211,1,I18,1
W713,A228,2,I24,1
W713,A191,3,I27,1
W714,A09,1,I07,1
W714,A21,2,I07,1
W715,A18,1,I09,1
W715,A152,2,I09,1
W715,A149,3,I09,1
W716,A126,1,I05,1
W716,A129,2,I05,1
W716,A127,3,I05,1
W718,A191,1,I27,1
W718,A219,2,I30,1
W719,A193,1,I29,1
W719,A229,2,I17,1
W719,A40,3,I17,1
W720,A04,1,I07,1
W720,A34,2,I15,1
W721,A159,1,I12,1
W722,A186,1,I17,1
W723,A138,1,I07,1
W723,A141,2,I07,1
W724,A41,1,I18,1
W724,A194,2,I30,1
W725,A104,1,I05,1
W725,A128,2,I05,1
W725,A36,3,I17,1
W726,A227,1,I31,1
W726,A32,2,I17,1
W727,A165,1,I14,1
W727,A166,2,I14,1
W728,A164,1,I14,1
W729,A224,1,I16,1
W730,A162,1,I11,1
W730,A14,2,I12,1
W730,A157,3,I12,1
W731,A35,1,I16,1
W732,A224,1,I16,1
W732,A199,2,I18,1
W733,A155,1,I12,1
W734,A21,1,I07,1
W735,A183,1,I31,1
W735,A228,2,I24,1
W736,A216,1,I28,1
W737,A164,1,I14,1
W737,A17,2,I14,1
W737,A162,3,I11,1
W738,A09,1,I07,1
W738,A136,2,I07,1
W739,A35,1,I16,1
W740,A188,1,I24,1
W740,A207,2,I31,1
W740,A178,3,I26,1
W741,A212,1,I24,1
W741,A208,2,I15,1
W742,A160,1,I11,1
W742,A155,2,I12,1
W742,A157,3,I12,1
W742,A228,4,I24,1
W744,A13,1,I11,1
W745,A110,1,I02,1
W747,A157,1,I12,1
W747,A14,2,I12,1
W748,A126,1,I05,1
W749,A163,1,I14,1
W749,A164,2,I14,1
W750,A158,1,I12,1
W750,A211,2,I18,1
W751,A162,1,I11,1
W752,A40,1,I17,1
W753,A126,1,I05,1
W755,A113,1,I02,1
W756,A173,1,I16,1
W756,A220,2,I26,1
W756,A195,3,I31,1
W757,A13,1,I11,1
W758,A07,1,I03,1
W758,A124,2,I19,1
W758,A14,3,I12,1
W760,A168,1,I13,1
W760,A15,2,I13,1
W760,A167,3,I13,1
W761,A22,1,I06,1
W762,A171,1,I10,1
W762,A179,2,I27,1
W763,A03,1,I02,1
W763,A110,2,I02,1
W764,A129,1,I05,1
W764,A130,2,I20,1
W764,A128,3,I05,1
W764,A179,4,I27,1
W765,A169,1,I13,1
W765,A219,2,I30,1
W766,A113,1,I02,1
W766,A173,2,I16,1
W768,A40,1,I17,1
W769,A174,1,I17,1
W770,A190,1,I26,1
W770,A217,2,I29,1
W770,A222,3,I31,1
W771,A164,1,I14,1
W771,A165,2,I14,1
W772,A206,1,I30,1
W772,A212,2,I24,1
W773,A180,1,I28,1
W774,A125,1,I19,1
W774,A124,2,I19,1
W775,A222,1,I31,1
W775,A207,2,I31,1
W775,A174,3,I17,1
W776,A193,1,I29,1
W777,A107,1,I09,1
W777,A151,2,I09,1
W777,A148,3,I09,1
W777,A149,4,I09,1
W778,A17,1,I14,1
W779,A156,1,I12,1
W780,A164,1,I14,1
W781,A161,1,I11,1
W781,A162,2,I11,1
W782,A198,1,I17,1
W782,A177,2,I25,1
W783,A158,1,I12,1
W784,A220,1,I26,1
W784,A222,2,I31,1
W785,A05,1,I05,1
W785,A127,2,I05,1
W786,A45,1,I18,1
W786,A228,2,I24,1
W786,A182,3,I30,1
W787,A07,1,I03,1
W787,A114,2,I02,1
W787,A177,3,I25,1
W788,A122,1,I19,1
W789,A141,1,I07,1
W790,A157,1,I12,1
W791,A156,1,I12,1
W791,A185,2,I16,1
W792,A05,1,I05,1
W792,A221,2,I30,1
W793,A144,1,I08,1
W794,A199,1,I18,1
W795,A212,1,I24,1
W795,A180,2,I28,1
W797,A188,1,I24,1
W797,A217,2,I29,1
W797,A32,3,I17,1
W798,A11,1,I09,1
W798,A150,2,I09,1
W798,A153,3,I23,1
W799,A14,1,I12,1
W800,A162,1,I11,1
W800,A168,2,I13,1
W801,A14,1,I12,1
W802,A09,1,I07,1
W802,A21,2,I07,1
W803,A156,1,I12,1
W803,A167,2,I13,1
W804,A211,1,I18,1
W806,A137,1,I07,1
W806,A137,1,I12,2
W807,A167,1,I13,1
W807,A15,2,I13,1
W808,A176,1,I24,1
W809,A42,1,I15,1
W809,A34,2,I15,1
W809,A223,3,I30,1
W810,A167,1,I13,1
W810,A168,2,I13,1
W811,A162,1,I11,1
W812,A132,1,I21,1
W813,A01,1,I02,1
W813,A111,2,I02,1
W813,A198,3,I17,1
W814,A228,1,I24,1
W815,A163,1,I14,1
W815,A165,2,I14,1
W815,A228,3,I24,1
W816,A211,1,I18,1
W816,A184,2,I15,1
W817,A03,1,I02,1
W817,A120,2,I04,1
W817,A32,3,I17,1
W818,A38,1,I15,1
W818,A202,2,I26,1
W819,A21,1,I07,1
W820,A39,1,I16,1
W820,A206,2,I30,1
W820,A187,3,I18,1
W821,A133,1,I21,1
W821,A132,2,I21,1
W821,A188,3,I24,1
W822,A08,1,I06,1
W822,A08,1,I04,2
W822,A114,2,I02,1
W823,A201,1,I25,1
W824,A167,1,I13,1
W826,A39,1,I16,1
W827,A123,1,I19,1
W827,A113,2,I02,1
W827,A118,3,I03,1
W828,A39,1,I16,1
W828,A212,2,I24,1
W829,A161,1,I11,1
W829,A162,2,I11,1
W829,A43,3,I16,1
W830,A11,1,I09,1
W830,A164,2,I14,1
W830,A207,3,I31,1
W830,A190,4,I26,1
W831,A123,1,I19,1
W832,A138,1,I07,1
W833,A07,1,I03,1
W833,A155,2,I12,1
W834,A15,1,I13,1
W834,A167,2,I13,1
W835,A06,1,I12,1
W835,A215,2,I27,1
W836,A194,1,I30,1
W837,A158,1,I12,1
W838,A40,1,I17,1
W840,A125,1,I19,1
W840,A118,2,I03,1
W840,A122,3,I19,1
W842,A105,1,I14,1
W842,A164,2,I14,1
W843,A101,1,I02,1
W843,A164,2,I14,1
W844,A109,1,I07,1
W845,A220,1,I26,1
W845,A38,2,I15,1
W846,A115,1,I03,1
W846,A118,2,I03,1
W846,A119,3,I04,1
W847,A201,1,I25,1
W848,A164,1,I14,1
W848,A165,2,I14,1
W849,A116,1,I03,1
W849,A120,2,I04,1
W850,A138,1,I07,1
W850,A229,2,I17,1
W851,A30,1,I15,1
W852,A138,1,I07,1
W853,A158,1,I12,1
W854,A167,1,I13,1
W854,A168,2,I13,1
W855,A141,1,I07,1
W856,A159,1,I12,1
W856,A156,2,I12,1
W857,A112,1,I02,1
W857,A122,2,I19,1
W857,A125,3,I19,1
W858,A180,1,I28,1
W859,A175,1,I18,1
W859,A108,2,I16,1
W859,A181,3,I29,1
W860,A133,1,I21,1
W860,A132,2,I21,1
W861,A169,1,I13,1
W861,A168,2,I13,1
W861,A178,3,I26,1
W862,A16,1,I21,1
W862,A16,1,I05,2
W863,A13,1,I11,1
W863,A160,2,I11,1
W864,A192,1,I28,1
W864,A32,2,I17,1
W865,A224,1,I16,1
W865,A202,2,I26,1
W866,A21,1,I07,1
W867,A128,1,I05,1
W867,A128,1,I21,2
W868,A109,1,I07,1
W869,A02,1,I02,1
W869,A125,2,I19,1
W869,A191,3,I27,1
W870,A11,1,I09,1
W870,A19,2,I09,1
W870,A151,3,I09,1
W870,A107,4,I09,1
W871,A45,1,I18,1
W871,A35,2,I16,1
W872,A120,1,I04,1
W872,A110,2,I02,1
W873,A214,1,I26,1
W874,A133,1,I21,1
W874,A132,2,I21,1
W874,A37,3,I18,1
W875,A210,1,I17,1
W875,A179,2,I27,1
W875,A37,3,I18,1
W876,A149,1,I09,1
W876,A19,2,I09,1
W876,A11,3,I09,1
W876,A151,4,I09,1
W877,A17,1,I14,1
W877,A164,2,I14,1
W878,A21,1,I07,1
W879,A13,1,I11,1
W879,A159,2,I12,1
W880,A154,1,I23,1
W880,A150,2,I09,1
W881,A166,1,I14,1
W881,A165,2,I14,1
W881,A178,3,I26,1
W882,A160,1,I11,1
W884,A171,1,I10,1
W884,A198,2,I17,1
W885,A19,1,I09,1
W886,A171,1,I10,1
W886,A170,2,I10,1
W886,A201,3,I25,1
W887,A194,1,I30,1
W887,A34,2,I15,1
W888,A163,1,I14,1
W888,A166,2,I14,1
W889,A167,1,I13,1
W890,A04,1,I07,1
W894,A169,1,I13,1
W894,A167,2,I13,1
W895,A167,1,I13,1
W896,A219,1,I30,1
W896,A33,2,I18,1
W896,A186,3,I17,1
W897,A16,1,I05,1
W900,A13,1,I11,1
W900,A160,2,I11,1
W901,A193,1,I29,1
W901,A228,2,I24,1
W901,A33,3,I18,1
W902,A102,1,I09,1
W903,A220,1,I26,1
W903,A228,2,I24,1
W904,A158,1,I12,1
W905,A101,1,I02,1
W905,A118,2,I03,1
W906,A108,1,I16,1
W907,A162,1,I11,1
W907,A160,2,I11,1
W907,A161,3,I11,1
W907,A188,4,I24,1
W908,A116,1,I03,1
W908,A111,2,I02,1
W908,A117,3,I03,1
W910,A148,1,I09,1
W910,A11,2,I09,1
W910,A151,3,I09,1
W910,A205,4,I29,1
W913,A113,1,I02,1
W914,A164,1,I14,1
W916,A118,1,I03,1
W917,A15,1,I13,1
W917,A169,2,I13,1
W918,A172,1,I15,1
W918,A202,2,I26,1
W920,A206,1,I30,1
W920,A45,2,I18,1
W921,A127,1,I21,1
W921,A127,1,I05,2
W922,A227,1,I31,1
W924,A169,1,I13,1
W925,A35,1,I16,1
W925,A213,2,I25,1
W926,A22,1,I06,1
W926,A135,2,I06,1
W927,A188,1,I24,1
W928,A13,1,I11,1
W929,A20,1,I09,1
W929,A154,2,I23,1
W929,A150,3,I09,1
W929,A18,4,I09,1
W930,A221,1,I30,1
W931,A119,1,I04,1
W932,A200,1,I24,1
W933,A128,1,I05,1
W933,A131,2,I20,1
W933,A162,3,I11,1
W934,A183,1,I31,1
W935,A144,1,I08,1
W935,A226,2,I24,1
W936,A101,1,I02,1
W937,A161,1,I11,1
W940,A08,1,I04,1
W940,A08,1,I06,2
W941,A148,1,I09,1
W942,A204,1,I28,1
W942,A202,2,I26,1
W943,A30,1,I15,1
W943,A181,2,I29,1
W944,A205,1,I29,1
W944,A190,2,I26,1
W945,A137,1,I07,1
W946,A118,1,I03,1
W947,A30,1,I15,1
W947,A187,2,I18,1
W948,A153,1,I23,1
W948,A149,2,I09,1
W948,A19,3,I09,1
W948,A102,4,I09,1
W948,A200,5,I24,1
W949,A01,1,I02,1
W949,A111,2,I02,1
W949,A32,3,I17,1
W950,A204,1,I28,1
W951,A167,1,I13,1
W953,A172,1,I15,1
W953,A44,2,I17,1
W954,A31,1,I16,1
W954,A219,2,I30,1
W955,A15,1,I13,1
W956,A140,1,I07,1
W956,A143,2,I08,1
W957,A19,1,I09,1
W957,A178,2,I26,1
W957,A203,3,I27,1
W957,A184,4,I15,1
W958,A130,1,I20,1
W958,A127,2,I05,1
W959,A223,1,I30,1
W960,A183,1,I31,1
W963,A184,1,I15,1
W963,A31,2,I16,1
W964,A172,1,I15,1
W964,A227,2,I31,1
W964,A210,3,I17,1
W965,A17,1,I14,1
W965,A164,2,I14,1
W966,A190,1,I26,1
W967,A09,1,I07,1
W968,A111,1,I02,1
W968,A120,2,I04,1
W968,A34,3,I15,1
W969,A07,1,I03,1
W969,A110,2,I02,1
W970,A156,1,I12,1
W971,A109,1,I07,1
W972,A02,1,I02,1
W972,A117,2,I03,1
W972,A221,3,I30,1
W973,A111,1,I02,1
W975,A186,1,I17,1
W975,A193,2,I29,1
W977,A228,1,I24,1
W977,A42,2,I15,1
W978,A176,1,I24,1
W978,A206,2,I30,1
W979,A116,1,I03,1
W980,A33,1,I18,1
W980,A212,2,I24,1
W980,A229,3,I17,1
W981,A144,1,I08,1
W981,A226,2,I24,1
W983,A213,1,I25,1
W984,A101,1,I02,1
W984,A210,2,I17,1
W985,A04,1,I07,1
W985,A215,2,I27,1
W986,A116,1,I03,1
W987,A21,1,I07,1
W988,A215,1,I27,1
W989,A210,1,I17,1
W989,A36,2,I17,1
W990,A156,1,I12,1
W990,A155,2,I12,1
W991,A211,1,I18,1
W992,A169,1,I13,1
W993,A198,1,I17,1
W993,A31,2,I16,1
W994,A206,1,I30,1
W994,A43,2,I16,1
W995,A14,1,I12,1
W996,A140,1,I07,1
W996,A140,1,I22,2
W997,A109,1,I07,1
W998,A04,1,I07,1
W998,A137,2,I07,1
W1000,A157,1,I12,1
W1001,A202,1,I26,1
W1001,A33,2,I18,1
W1002,A156,1,I12,1
W1002,A162,2,I11,1
W1003,A110,1,I02,1
W1003,A113,2,I02,1
W1004,A160,1,I11,1
W1005,A01,1,I02,1
W1005,A111,2,I02,1
W1005,A198,3,I17,1
W1006,A157,1,I12,1
W1007,A22,1,I06,1
W1008,A160,1,I11,1
W1008,A162,2,I11,1
W1009,A34,1,I15,1
W1009,A44,2,I17,1
W1010,A19,1,I09,1
W1010,A152,2,I09,1
W1011,A130,1,I20,1
W1012,A35,1,I16,1
W1012,A199,2,I18,1
W1013,A168,1,I13,1
W1014,A160,1,I11,1
W1014,A162,2,I11,1
W1014,A158,3,I12,1
W1015,A196,1,I15,1
W1015,A194,2,I30,1
W1015,A225,3,I28,1
W1016,A15,1,I13,1
W1017,A227,1,I31,1
W1017,A196,2,I15,1
W1017,A33,3,I18,1
W1018,A108,1,I16,1
W1019,A15,1,I13,1
W1019,A167,2,I13,1
W1020,A04,1,I07,1
W1021,A137,1,I07,1
W1021,A137,1,I22,2
W1022,A195,1,I31,1
W1022,A37,2,I18,1
W1023,A199,1,I18,1
W1023,A197,2,I16,1
W1024,A187,1,I18,1
W1025,A09,1,I07,1
W1026,A212,1,I24,1
W1026,A41,2,I18,1
W1027,A143,1,I08,1
W1027,A145,2,I08,1
W1028,A11,1,I09,1
W1028,A107,2,I09,1
W1028,A20,3,I09,1
W1029,A208,1,I15,1
W1029,A224,2,I16,1
W1030,A174,1,I17,1
W1031,A06,1,I12,1
W1031,A158,2,I12,1
W1032,A14,1,I12,1
W1032,A157,2,I12,1
W1032,A158,3,I12,1
W1033,A156,1,I12,1
W1033,A14,2,I12,1
W1035,A126,1,I05,1
W1036,A148,1,I09,1
W1036,A43,2,I16,1
W1036,A202,3,I26,1
W1036,A44,4,I17,1
W1037,A159,1,I12,1
W1038,A05,1,I05,1
W1038,A164,2,I14,1
W1039,A165,1,I14,1
W1039,A164,2,I14,1
W1040,A33,1,I18,1
W1040,A179,2,I27,1
W1041,A137,1,I07,1
W1042,A172,1,I15,1
W1043,A43,1,I16,1
W1044,A110,1,I02,1
W1044,A113,2,I02,1
W1044,A111,3,I02,1
W1044,A192,4,I28,1
W1046,A119,1,I04,1
W1047,A227,1,I31,1
W1047,A221,2,I30,1
W1047,A219,3,I30,1
W1048,A02,1,I02,1
W1049,A141,1,I07,1
W1050,A02,1,I02,1
W1050,A114,2,I02,1
W1051,A130,1,I20,1
W1051,A16,2,I05,1
W1052,A127,1,I05,1
W1052,A130,2,I20,1
W1053,A159,1,I12,1
W1053,A155,2,I12,1
W1054,A15,1,I13,1
W1056,A102,1,I09,1
W1058,A170,1,I10,1
W1058,A171,2,I10,1
W1058,A12,3,I10,1
W1060,A166,1,I14,1
W1060,A165,2,I14,1
W1060,A229,3,I17,1
W1061,A126,1,I05,1
W1062,A134,1,I06,1
W1062,A135,2,I06,1
W1063,A170,1,I10,1
W1063,A12,2,I10,1
W1064,A202,1,I26,1
W1064,A32,2,I17,1
W1065,A122,1,I19,1
W1065,A123,2,I19,1
W1065,A119,3,I04,1
W1065,A222,4,I31,1
```

### citations.csv
```csv
citing_work_id,cited_work_id
W12,W03
W13,W03
W14,W03
W15,W02
W15,W03
W16,W03
W17,W03
W18,W02
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
W67,W42
W90,W22
W90,W41
W91,W22
W92,W22
W103,W60
W103,W101
W104,W101
W105,W60
W106,W61
W106,W104
W107,W101
W107,W104
W108,W60
W108,W101
W108,W104
W109,W101
W109,W104
W110,W60
W111,W64
W111,W104
W111,W107
W113,W110
W114,W104
W115,W114
W116,W104
W118,W66
W118,W106
W119,W109
W119,W114
W120,W108
W120,W112
W121,W112
W121,W113
W123,W60
W123,W101
W124,W101
W124,W107
W124,W114
W125,W61
W125,W105
W125,W108
W201,W1063
W203,W291
W204,W425
W205,W502
W208,W361
W209,W341
W209,W1002
W210,W461
W211,W361
W211,W400
W211,W758
W214,W03
W214,W881
W215,W607
W216,W401
W216,W607
W217,W1053
W218,W464
W218,W642
W218,W755
W219,W271
W219,W953
W220,W733
W220,W910
W222,W251
W222,W449
W222,W599
W223,W665
W223,W896
W223,W936
W224,W272
W225,W531
W225,W542
W225,W704
W225,W850
W225,W1063
W227,W946
W228,W620
W228,W696
W228,W732
W229,W01
W229,W206
W229,W873
W230,W557
W230,W691
W233,W215
W235,W400
W238,W869
W239,W562
W239,W1032
W242,W350
W246,W30
W247,W740
W249,W42
W252,W904
W256,W480
W257,W749
W258,W486
W258,W835
W259,W425
W259,W593
W259,W848
W260,W497
W260,W755
W261,W445
W261,W1058
W262,W618
W263,W728
W263,W1063
W265,W430
W265,W682
W266,W430
W267,W275
W267,W547
W267,W879
W268,W436
W269,W227
W270,W779
W270,W1044
W271,W605
W271,W1063
W272,W526
W273,W03
W273,W787
W273,W888
W274,W30
W274,W862
W274,W884
W275,W208
W275,W943
W276,W30
W276,W678
W278,W382
W279,W239
W279,W916
W279,W1063
W281,W932
W282,W20
W282,W341
W282,W398
W284,W312
W284,W534
W284,W559
W285,W730
W285,W798
W289,W30
W289,W486
W291,W562
W292,W807
W293,W319
W294,W239
W296,W402
W296,W572
W296,W876
W297,W256
W299,W575
W300,W20
W300,W855
W302,W20
W302,W217
W302,W454
W303,W552
W304,W1043
W305,W296
W308,W575
W308,W808
W308,W851
W309,W453
W309,W584
W309,W937
W310,W778
W313,W369
W314,W296
W314,W1006
W314,W1017
W315,W02
W315,W03
W315,W227
W317,W465
W317,W887
W318,W31
W318,W511
W318,W800
W320,W30
W320,W31
W320,W476
W320,W637
W320,W958
W322,W324
W322,W346
W325,W335
W325,W834
W325,W880
W326,W227
W326,W516
W329,W22
W329,W595
W330,W422
W331,W605
W331,W749
W334,W30
W334,W319
W334,W383
W334,W989
W337,W660
W338,W40
W338,W465
W338,W602
W338,W736
W338,W843
W339,W716
W339,W864
W341,W453
W341,W804
W348,W403
W348,W681
W349,W03
W349,W524
W349,W773
W349,W851
W354,W410
W354,W500
W354,W995
W355,W264
W355,W528
W357,W333
W357,W530
W357,W674
W357,W842
W359,W277
W365,W323
W366,W550
W369,W296
W369,W737
W369,W1053
W370,W484
W370,W970
W371,W404
W371,W435
W372,W22
W373,W876
W374,W292
W374,W927
W376,W466
W377,W870
W378,W867
W380,W699
W382,W580
W382,W785
W383,W416
W384,W214
W384,W706
W384,W1001
W387,W452
W388,W1063
W389,W593
W396,W40
W396,W803
W397,W02
W397,W03
W398,W350
W399,W400
W399,W426
W399,W565
W401,W291
W403,W958
W405,W419
W405,W710
W406,W269
W406,W849
W406,W896
W407,W414
W407,W635
W407,W1054
W413,W562
W417,W406
W417,W628
W417,W815
W418,W683
W418,W804
W418,W846
W419,W626
W419,W842
W420,W733
W421,W438
W421,W473
W421,W627
W421,W855
W422,W790
W422,W824
W424,W742
W425,W275
W425,W369
W425,W816
W427,W523
W427,W527
W427,W869
W428,W713
W428,W727
W428,W910
W430,W672
W431,W752
W436,W901
W436,W976
W439,W30
W439,W927
W440,W588
W440,W608
W440,W735
W441,W428
W442,W665
W442,W1026
W444,W755
W448,W354
W448,W665
W448,W807
W453,W770
W456,W385
W456,W803
W456,W821
W457,W733
W458,W279
W458,W696
W459,W271
W459,W649
W459,W1026
W460,W269
W460,W1024
W462,W277
W462,W816
W462,W901
W463,W716
W465,W896
W466,W588
W467,W691
W467,W696
W467,W979
W469,W820
W469,W990
W470,W972
W475,W809
W477,W601
W477,W803
W477,W1036
W478,W861
W481,W716
W486,W720
W486,W858
W487,W808
W487,W835
W488,W22
W488,W1060
W489,W807
W491,W401
W496,W237
W496,W555
W496,W771
W499,W725
W501,W376
W501,W458
W503,W369
W503,W527
W503,W555
W505,W565
W505,W777
W507,W1030
W508,W731
W509,W479
W509,W649
W509,W851
W512,W782
W512,W983
W515,W20
W515,W935
W520,W269
W520,W790
W520,W827
W522,W749
W522,W771
W524,W513
W524,W630
W524,W820
W526,W322
W527,W480
W527,W823
W528,W516
W528,W612
W529,W237
W529,W860
W529,W908
W531,W942
W531,W1065
W533,W500
W533,W539
W535,W02
W535,W03
W535,W553
W536,W491
W536,W728
W536,W1047
W538,W669
W539,W901
W541,W630
W542,W584
W544,W02
W544,W751
W544,W807
W544,W1065
W546,W40
W546,W660
W546,W782
W547,W953
W549,W1035
W550,W237
W550,W988
W550,W1010
W551,W211
W551,W489
W552,W742
W555,W978
W557,W323
W557,W580
W558,W02
W558,W706
W559,W564
W560,W491
W562,W728
W562,W749
W567,W599
W567,W696
W567,W948
W569,W03
W569,W319
W569,W411
W570,W465
W570,W666
W570,W944
W572,W613
W572,W713
W573,W22
W573,W303
W573,W932
W573,W954
W575,W331
W575,W500
W576,W880
W579,W524
W579,W588
W579,W790
W580,W616
W581,W1010
W582,W22
W582,W300
W582,W389
W583,W291
W583,W946
W586,W20
W586,W296
W586,W473
W586,W654
W589,W970
W592,W20
W592,W981
W595,W453
W598,W03
W598,W1064
W599,W461
W602,W01
W602,W1011
W605,W388
W610,W22
W610,W235
W610,W300
W610,W564
W610,W967
W612,W574
W613,W296
W613,W322
W613,W820
W614,W459
W615,W331
W615,W715
W615,W959
W617,W373
W618,W913
W619,W259
W619,W430
W619,W502
W621,W20
W621,W624
W625,W832
W626,W758
W626,W1028
W627,W480
W627,W807
W628,W584
W628,W630
W628,W946
W629,W725
W630,W461
W630,W876
W630,W1062
W632,W270
W633,W260
W633,W366
W635,W527
W640,W870
W642,W902
W643,W403
W643,W589
W645,W555
W649,W741
W650,W31
W651,W742
W651,W881
W651,W1064
W652,W645
W652,W836
W655,W361
W655,W489
W656,W545
W656,W651
W656,W858
W657,W01
W659,W817
W659,W934
W660,W01
W660,W940
W660,W1035
W661,W848
W661,W884
W663,W741
W664,W296
W664,W888
W665,W780
W666,W426
W666,W921
W667,W593
W668,W480
W672,W820
W672,W858
W673,W368
W673,W992
W674,W901
W675,W519
W675,W881
W676,W03
W676,W621
W676,W690
W678,W256
W678,W605
W678,W608
W679,W834
W680,W22
W680,W410
W680,W480
W680,W728
W682,W229
W682,W584
W682,W871
W683,W368
W683,W798
W684,W346
W684,W678
W684,W856
W685,W317
W686,W752
W688,W314
W692,W882
W693,W346
W693,W1063
W696,W243
W696,W369
W696,W584
W697,W626
W699,W433
W699,W782
W699,W968
W700,W22
W700,W246
W700,W572
W702,W799
W703,W801
W704,W615
W705,W628
W707,W331
W707,W500
W707,W733
W709,W946
W710,W1047
W711,W03
W711,W505
W714,W382
W714,W722
W715,W516
W718,W413
W719,W858
W721,W970
W722,W275
W722,W346
W722,W730
W724,W579
W724,W972
W725,W354
W725,W886
W725,W995
W727,W430
W729,W420
W730,W849
W732,W243
W732,W465
W733,W279
W733,W502
W733,W772
W734,W22
W734,W985
W734,W1042
W737,W556
W737,W916
W738,W559
W739,W545
W739,W713
W739,W772
W740,W722
W742,W908
W744,W417
W744,W705
W745,W457
W745,W623
W745,W1032
W747,W755
W747,W1007
W748,W03
W749,W858
W750,W285
W750,W655
W750,W976
W751,W263
W751,W373
W751,W516
W752,W880
W753,W1052
W756,W400
W756,W816
W757,W42
W760,W204
W761,W03
W761,W442
W761,W575
W761,W991
W762,W1000
W763,W433
W763,W459
W763,W540
W764,W555
W765,W222
W766,W326
W768,W1064
W769,W522
W772,W545
W774,W275
W776,W668
W777,W267
W777,W896
W778,W465
W779,W388
W780,W696
W782,W903
W783,W20
W783,W707
W783,W787
W784,W430
W784,W583
W784,W618
W785,W206
W785,W838
W785,W1051
W786,W453
W786,W881
W787,W367
W787,W467
W787,W1058
W788,W1027
W789,W616
W791,W208
W791,W305
W791,W976
W792,W1044
W793,W441
W794,W31
W794,W925
W794,W955
W794,W1028
W798,W486
W799,W545
W799,W960
W800,W322
W801,W660
W803,W579
W806,W401
W807,W692
W807,W769
W807,W944
W808,W476
W808,W897
W810,W741
W812,W03
W813,W331
W813,W787
W813,W960
W816,W296
W816,W623
W816,W835
W817,W735
W818,W588
W819,W22
W819,W382
W821,W344
W821,W383
W822,W292
W822,W642
W822,W722
W823,W500
W823,W858
W824,W811
W826,W336
W830,W406
W831,W466
W831,W774
W831,W828
W832,W269
W833,W03
W833,W466
W836,W995
W836,W1053
W836,W1065
W837,W20
W837,W21
W837,W713
W838,W279
W840,W376
W840,W669
W842,W620
W842,W826
W843,W02
W843,W03
W844,W01
W844,W660
W846,W296
W846,W574
W846,W922
W847,W453
W847,W1060
W848,W775
W848,W882
W848,W932
W851,W31
W851,W1063
W852,W401
W852,W944
W853,W20
W853,W616
W853,W981
W854,W480
W855,W836
W856,W30
W856,W588
W857,W790
W857,W820
W857,W989
W858,W896
W859,W927
W860,W424
W860,W755
W860,W756
W861,W772
W861,W1026
W864,W696
W865,W344
W865,W756
W865,W927
W866,W22
W867,W874
W868,W22
W868,W935
W868,W1016
W870,W211
W870,W672
W870,W944
W872,W572
W872,W696
W873,W562
W874,W424
W874,W664
W874,W1019
W875,W496
W875,W941
W875,W975
W876,W271
W876,W331
W876,W424
W877,W471
W877,W784
W878,W30
W878,W31
W879,W583
W879,W599
W880,W835
W881,W613
W882,W309
W882,W324
W882,W916
W884,W322
W885,W946
W889,W03
W889,W277
W889,W337
W889,W867
W890,W03
W890,W218
W890,W664
W890,W811
W894,W30
W894,W433
W894,W536
W895,W01
W895,W40
W895,W41
W897,W241
W897,W601
W897,W663
W900,W579
W901,W735
W903,W373
W903,W908
W903,W964
W904,W20
W904,W450
W904,W921
W905,W466
W907,W713
W908,W458
W908,W502
W908,W780
W910,W1051
W913,W672
W913,W749
W913,W908
W914,W389
W914,W729
W917,W659
W921,W313
W921,W348
W921,W572
W922,W40
W922,W477
W924,W417
W924,W428
W924,W448
W924,W642
W924,W762
W925,W393
W925,W886
W925,W1037
W927,W1028
W928,W450
W928,W707
W930,W420
W930,W437
W930,W894
W931,W03
W931,W519
W931,W755
W932,W638
W933,W618
W934,W668
W934,W1048
W935,W332
W935,W354
W935,W439
W936,W426
W936,W749
W937,W263
W937,W552
W940,W1012
W941,W835
W943,W201
W943,W513
W943,W730
W944,W243
W944,W583
W944,W1052
W946,W277
W946,W556
W946,W630
W947,W415
W947,W453
W947,W784
W948,W807
W949,W208
W949,W1061
W950,W1016
W953,W562
W954,W304
W959,W457
W964,W294
W964,W399
W964,W936
W965,W606
W966,W560
W966,W801
W966,W1036
W967,W1002
W968,W587
W968,W616
W968,W713
W970,W936
W971,W22
W971,W252
W972,W755
W973,W03
W975,W665
W977,W752
W978,W410
W978,W672
W978,W1063
W980,W336
W980,W579
W980,W601
W981,W753
W981,W804
W984,W355
W984,W824
W986,W424
W986,W593
W987,W22
W987,W608
W988,W30
W988,W322
W989,W903
W990,W294
W991,W623
W992,W30
W993,W449
W993,W617
W993,W947
W994,W278
W994,W756
W995,W275
W996,W579
W996,W903
W996,W989
W997,W22
W997,W496
W997,W709
W997,W1033
W1000,W317
W1000,W978
W1001,W797
W1002,W218
W1002,W461
W1002,W742
W1005,W233
W1005,W251
W1005,W706
W1006,W1047
W1007,W458
W1007,W735
W1007,W772
W1009,W988
W1011,W453
W1011,W623
W1011,W910
W1012,W876
W1014,W731
W1016,W242
W1016,W793
W1016,W1046
W1017,W246
W1018,W343
W1020,W556
W1022,W309
W1022,W876
W1024,W401
W1024,W692
W1024,W769
W1025,W275
W1025,W331
W1025,W572
W1026,W626
W1027,W210
W1027,W349
W1027,W728
W1029,W649
W1031,W521
W1031,W699
W1031,W702
W1032,W713
W1033,W30
W1033,W977
W1034,W383
W1034,W631
W1034,W1001
W1037,W312
W1038,W572
W1039,W31
W1039,W42
W1040,W896
W1042,W455
W1042,W602
W1043,W276
W1043,W506
W1043,W784
W1044,W713
W1046,W301
W1047,W870
W1048,W02
W1048,W601
W1048,W821
W1049,W313
W1050,W774
W1051,W522
W1052,W970
W1056,W03
W1058,W555
W1058,W808
W1058,W822
W1060,W271
W1060,W552
W1060,W946
W1061,W522
W1061,W757
W1064,W944
W1064,W1026
W1065,W870
W1065,W1024
```

### ontology.ttl (the vocabulary the data uses)
The codes in the CSV files are the skos:notation values of the concepts below.
```turtle
@prefix res:  <https://example.org/research/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

# A deliberately small ontology for the semantics-ladder experiment, second domain.
# The semantics live in the definitions (skos:definition), in plain English, not in OWL
# axioms. Each code used in the CSV files (ART, LAB, K2, STG, ...) is a concept here, with
# skos:notation giving the code as it appears in the data.
#
# Shaped like OpenAlex's entities (works, authors, institutions, sources), but it is not
# OpenAlex's model, and all the data it describes is invented.

<https://example.org/research/ontology> a owl:Ontology ;
    rdfs:label "Research analytics: a teaching ontology" ;
    rdfs:comment "Works, authors, institutions, sources, authorships, citations and the codes the data uses, each with a definition that states what it means and how to count it. Invented for an experiment; not a model of any real bibliographic database." ;
    owl:versionInfo "0.1" .


# === Classes ==============================================================================

res:Work a owl:Class ;
    rdfs:label "Work" ;
    skos:definition "A record of something published: an article, review, preprint, editorial, erratum or piece of paratext (res:workType). Not every work is research output. A research work is a work that (1) is not a test record (see res:origin-STG), (2) is of a research type: an article (ART), a review (REV), a supplement article (SUP) or a preprint (PPR), (3) is not retracted (res:retracted), and (4) did not appear in a delisted source (res:tier-K0). Editorials, errata and paratext are never research output. A preprint and its published version (res:versionOf) are two records of one research work and count once, under the published version (its year and its source). Every count of works means research works, and citations are counted to research works, unless a question says otherwise." .

res:Author a owl:Class ;
    rdfs:label "Author" ;
    skos:definition "An author record: one person as one source spelled them. A person is identified by their ORCID (res:orcid), not by their name or record ID. The same person can appear as several author records with differently spelled names: records with the same ORCID are the same person, and every work recorded against any of them is that person's. Two records with the same name and different ORCIDs are different people. A record with no ORCID is a person of its own." .

res:Institution a owl:Class ;
    rdfs:label "Institution" ;
    skos:definition "An organisation that authors are affiliated with: a university system, university, lab, company, government body or affiliated institute (res:institutionType). Institutions form a hierarchy through res:parent: a lab can sit under a centre, under a university, under a university system. A work credited to a unit is also credited to every institution above it, to any depth, so counting an institution's works means counting the works of the institution and all its units, each work once. The exception is an affiliated institute (res:itype-AFF): its parent link does not make it a unit." .

res:Source a owl:Class ;
    rdfs:label "Source" ;
    skos:definition "Where a work appeared: a journal or a repository (res:sourceType)." .

res:Authorship a owl:Class ;
    rdfs:label "Authorship" ;
    skos:definition "One author's place on one work, and one of the institutions they gave for it: one record per author, work and affiliation. An author who gave two affiliations on a work has two authorship records for it, with the same res:authorPosition and different res:affiliationSeq. Which one counts is set by res:affiliationSeq." .

res:Citation a owl:Class ;
    rdfs:label "Citation" ;
    skos:definition "One work citing another: res:citingWork lists res:citedWork among its references. A citation happens in the citing work's year. A work's citation count is the number of distinct works, of any type, that cite it, leaving out test records (res:origin-STG) and retracted works. A work citing both a preprint and its published version is one citation of that research work. Citation counts for an author, institution or country add up the counts of their research works. When citations are rolled up to the citing side (which institution or country cites another most), each citing work counts once for each institution credited on it, however many of its authors are from that institution. A self-citation depends on the level: an author self-citation is one where the citing and cited works share at least one author (the same person, whatever the record); an institution self-citation is one where they share a credited institution at the level asked about; a country self-citation is one where they share a country of credited institutions. Each level includes the one below it, so the three are different counts. A citation window counts only the citations made in the cited work's publication year and a given number of years after it, so that older and newer works are compared over the same span." .


# === Properties: institutions =============================================================

res:name a owl:DatatypeProperty ; rdfs:label "name" ;
    skos:definition "The name of an institution, author or source as the record spells it. Names are not identifiers: the same person can be spelled differently, and different people can share a name." .

res:ror a owl:DatatypeProperty ; rdfs:label "ROR ID" ;
    skos:definition "The institution's Research Organization Registry identifier (invented here)." .

res:country a owl:DatatypeProperty ; rdfs:label "country" ;
    skos:definition "ISO code of the country where the institution is. A work's countries are the countries of the institutions credited on it (see res:affiliationSeq), not of every affiliation listed." .

res:institutionType a owl:ObjectProperty ; rdfs:label "institution type" ;
    skos:definition "What kind of institution it is: a concept of the scheme res:InstitutionTypes." .

res:parent a owl:ObjectProperty ; rdfs:label "parent" ;
    skos:definition "The institution this one is a unit of. Follow it upwards, to any depth, to find the institutions a work is also credited to; the ultimate parent is the institution at the top of the chain, the one with no parent. For an affiliated institute (res:itype-AFF) the link records an agreement, not membership: do not follow it." .


# === Properties: authors ==================================================================

res:orcid a owl:DatatypeProperty ; rdfs:label "ORCID" ;
    skos:definition "The person's ORCID identifier (invented here): the identifier that says which person an author record stands for. Same ORCID, same person." .


# === Properties: sources ==================================================================

res:issn a owl:DatatypeProperty ; rdfs:label "ISSN" ;
    skos:definition "The journal's ISSN (invented here). Repositories have none." .

res:sourceType a owl:ObjectProperty ; rdfs:label "source type" ;
    skos:definition "Whether the source is a journal or a repository: a concept of the scheme res:SourceTypes." .

res:tier a owl:ObjectProperty ; rdfs:label "tier" ;
    skos:definition "The source's tier on this dataset's own journal list: a concept of the scheme res:Tiers. The tiers count upwards: K3 is the highest tier and K1 the lowest; K0 is not a tier but a delisting. Repositories have no tier." .


# === Properties: works ====================================================================

res:title a owl:DatatypeProperty ; rdfs:label "title" ;
    skos:definition "The work's title. A preprint and its published version often share a title; two works with the same title are not the same work unless res:versionOf links them." .

res:year a owl:DatatypeProperty ; rdfs:label "publication year" ;
    skos:definition "The year the work was published. A citation's year is the citing work's publication year." .

res:workType a owl:ObjectProperty ; rdfs:label "work type" ;
    skos:definition "What kind of work it is: a concept of the scheme res:WorkTypes. It decides whether the work is research output (see res:Work)." .

res:source a owl:ObjectProperty ; rdfs:label "source" ;
    skos:definition "The journal or repository the work appeared in." .

res:doi a owl:DatatypeProperty ; rdfs:label "DOI" ;
    skos:definition "The work's DOI (invented here). A preprint and its published version have different DOIs, though they are one research work." .

res:versionOf a owl:ObjectProperty ; rdfs:label "version of" ;
    skos:definition "Set on a preprint whose published version is also in the data: it names that published version. The two records are one research work, counted once, under the published version; the authors, institutions and citations of either record belong to that one work." .

res:retracted a owl:DatatypeProperty ; rdfs:label "retracted" ;
    skos:definition "True if the work has been retracted. A retracted work is not research output: leave it out of every count of works, and its citations out of every count of citations." .

res:recordSource a owl:ObjectProperty ; rdfs:label "record source" ;
    skos:definition "The system the work record was loaded from: a concept of the scheme res:RecordSources." .


# === Properties: authorships ==============================================================

res:work a owl:ObjectProperty ; rdfs:label "work" ;
    skos:definition "The work the authorship is on." .

res:author a owl:ObjectProperty ; rdfs:label "author" ;
    skos:definition "The author record: see res:Author for which person it stands for." .

res:authorPosition a owl:DatatypeProperty ; rdfs:label "author position" ;
    skos:definition "The author's place in the byline, from 1. The number of a work's authors is the number of distinct people in its byline." .

res:institution a owl:ObjectProperty ; rdfs:label "institution" ;
    skos:definition "An institution the author gave on this work." .

res:affiliationSeq a owl:DatatypeProperty ; rdfs:label "affiliation sequence" ;
    skos:definition "The order in which the author listed their affiliations on this work, from 1. House rule: when an author lists several affiliations on one work, the work is credited only to the affiliation listed last, the one with the highest sequence number, for that author; the others are ignored in every count. With one affiliation, that one is credited. Under full counting, a work counts once for each institution credited on it (and for the institutions above it). Under fractional counting, a work is split equally among its authors (distinct people), and each author's share goes to the one institution credited for them, and so to its country; an institution's fractional count adds up the shares of its own authors and its units' authors." .


# === Properties: citations ================================================================

res:citingWork a owl:ObjectProperty ; rdfs:label "citing work" ;
    skos:definition "The work that makes the citation." .

res:citedWork a owl:ObjectProperty ; rdfs:label "cited work" ;
    skos:definition "The work that is cited." .


# === Code lists (the codes used in the CSV files) =========================================

res:WorkTypes a skos:ConceptScheme ; rdfs:label "Work types" .

res:wtype-ART a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "ART" ;
    rdfs:label "Article" ; skos:prefLabel "Research article" ;
    skos:definition "A peer-reviewed research article. Research output." .
res:wtype-REV a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "REV" ;
    rdfs:label "Review" ; skos:prefLabel "Review article" ;
    skos:definition "A peer-reviewed article that surveys a field. Research output." .
res:wtype-SUP a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "SUP" ;
    rdfs:label "Supplement article" ; skos:prefLabel "Supplement article" ;
    skos:definition "In this dataset, SUP does not mean supplementary material. It is a full, peer-reviewed research article published in a supplement issue of a journal, such as a proceedings supplement. It is research output and counts exactly like an article (ART)." .
res:wtype-PPR a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "PPR" ;
    rdfs:label "Preprint" ; skos:prefLabel "Preprint" ;
    skos:definition "A version posted to a repository before or without peer review. Research output, but if its published version is in the data (res:versionOf), the two are one research work, counted once." .
res:wtype-EDT a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "EDT" ;
    rdfs:label "Editorial" ; skos:prefLabel "Editorial" ;
    skos:definition "An editor's introduction or opinion piece. Not research output." .
res:wtype-ERR a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "ERR" ;
    rdfs:label "Erratum" ; skos:prefLabel "Erratum" ;
    skos:definition "A correction notice for an earlier work. Not research output, and not a new version of the work it corrects." .
res:wtype-PTX a skos:Concept ; skos:inScheme res:WorkTypes ; skos:notation "PTX" ;
    rdfs:label "Paratext" ; skos:prefLabel "Paratext" ;
    skos:definition "Front matter, issue information, tables of contents and the like: published with a journal issue, but not a contribution. Not research output." .

res:InstitutionTypes a skos:ConceptScheme ; rdfs:label "Institution types" .

res:itype-SYS a skos:Concept ; skos:inScheme res:InstitutionTypes ; skos:notation "SYS" ;
    rdfs:label "University system" ; skos:prefLabel "University system" ;
    skos:definition "A group of universities under one governing body. Its works are the works of all its universities and their units." .
res:itype-UNI a skos:Concept ; skos:inScheme res:InstitutionTypes ; skos:notation "UNI" ;
    rdfs:label "University" ; skos:prefLabel "University" ;
    skos:definition "A university or college." .
res:itype-LAB a skos:Concept ; skos:inScheme res:InstitutionTypes ; skos:notation "LAB" ;
    rdfs:label "Lab or centre" ; skos:prefLabel "Laboratory, centre or institute" ;
    skos:definition "A research unit inside its parent institution. Its works are also its parent's works, and its parent's parent's, to the top." .
res:itype-AFF a skos:Concept ; skos:inScheme res:InstitutionTypes ; skos:notation "AFF" ;
    rdfs:label "Affiliated institute" ; skos:prefLabel "Affiliated institute" ;
    skos:definition "A legally independent institute linked to a university by an agreement. Its parent link records that agreement and nothing more: an affiliated institute is not a unit of its parent, is not part of the parent's system, and its works are never credited to the parent or to anything above it. Its ultimate parent is itself." .
res:itype-CO a skos:Concept ; skos:inScheme res:InstitutionTypes ; skos:notation "CO" ;
    rdfs:label "Company" ; skos:prefLabel "Company" ;
    skos:definition "A company." .
res:itype-GOV a skos:Concept ; skos:inScheme res:InstitutionTypes ; skos:notation "GOV" ;
    rdfs:label "Government body" ; skos:prefLabel "Government body" ;
    skos:definition "A government agency or laboratory." .

res:SourceTypes a skos:ConceptScheme ; rdfs:label "Source types" .

res:stype-JOU a skos:Concept ; skos:inScheme res:SourceTypes ; skos:notation "JOU" ;
    rdfs:label "Journal" ; skos:prefLabel "Journal" ;
    skos:definition "A peer-reviewed journal, including its proceedings or supplement issues." .
res:stype-REP a skos:Concept ; skos:inScheme res:SourceTypes ; skos:notation "REP" ;
    rdfs:label "Repository" ; skos:prefLabel "Repository" ;
    skos:definition "A preprint server or other repository." .

res:Tiers a skos:ConceptScheme ; rdfs:label "Journal tiers" .

res:tier-K3 a skos:Concept ; skos:inScheme res:Tiers ; skos:notation "K3" ;
    rdfs:label "Tier K3" ; skos:prefLabel "Tier K3, the highest" ;
    skos:definition "The highest tier: the journals the list ranks first. A higher number is a higher tier, so K3 ranks above K2, and K2 above K1." .
res:tier-K2 a skos:Concept ; skos:inScheme res:Tiers ; skos:notation "K2" ;
    rdfs:label "Tier K2" ; skos:prefLabel "Tier K2, the middle" ;
    skos:definition "The middle tier: below K3, above K1." .
res:tier-K1 a skos:Concept ; skos:inScheme res:Tiers ; skos:notation "K1" ;
    rdfs:label "Tier K1" ; skos:prefLabel "Tier K1, the lowest" ;
    skos:definition "The lowest tier that is still listed: below K2." .
res:tier-K0 a skos:Concept ; skos:inScheme res:Tiers ; skos:notation "K0" ;
    rdfs:label "Delisted" ; skos:prefLabel "Delisted source" ;
    skos:definition "Not a tier: a source removed from the list for failing its review of editorial practice. Works that appeared in a K0 source are not research output, whatever their type, and are left out of every count of works and citations." .

res:RecordSources a skos:ConceptScheme ; rdfs:label "Record sources" .

res:origin-FEED a skos:Concept ; skos:inScheme res:RecordSources ; skos:notation "FEED" ;
    rdfs:label "Bibliographic feed" ; skos:prefLabel "Bibliographic feed" ;
    skos:definition "Loaded from the external bibliographic feed." .
res:origin-CRIS a skos:Concept ; skos:inScheme res:RecordSources ; skos:notation "CRIS" ;
    rdfs:label "Institutional system" ; skos:prefLabel "Institutional research information system" ;
    skos:definition "Entered by an institution in its own research information system. As good as a feed record." .
res:origin-STG a skos:Concept ; skos:inScheme res:RecordSources ; skos:notation "STG" ;
    rdfs:label "Staging" ; skos:prefLabel "Staging load" ;
    skos:definition "Test records, loaded into staging to check the import and never removed. They describe no real work: ignore an STG work, its authorships and every citation it makes, in every count." .
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
