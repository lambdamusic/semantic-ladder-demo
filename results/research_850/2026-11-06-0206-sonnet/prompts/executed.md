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
W201,Machine learning for marsh accretion,2019,ART,S09,false,yes,W201
W202,Issue information,2023,PTX,S02,false,no,W202
W203,A community intercomparison of beach profiles,2024,ART,S03,false,yes,W203
W204,Long-term trends in tidal asymmetry in the Brevin shelf,2024,ART,S09,false,yes,W204
W205,Uncertainty in sensor calibration estimates: a review,2025,REV,S03,false,yes,W205
W206,Observations of buoy telemetry in a semi-enclosed sea,2020,ART,S01,false,yes,W206
W208,A framework for sensor calibration in tidal inlets,2019,ART,S10,false,yes,W208
W209,Remote sensing of turbulent wakes in sandy coasts,2025,ART,S02,false,yes,W209
W211,Long-term trends in internal waves in the Wexcombe marshes,2019,ART,S10,false,yes,W211
W212,Issue information,2019,PTX,S03,false,no,W212
W214,A framework for buoy telemetry in shallow channels,2023,ART,S03,false,yes,W214
W215,Long-term trends in harbour seiches in harbour basins,2024,ART,S12,false,yes,W215
W216,Observations of vortex shedding in the Albury estuary,2025,ART,S03,false,yes,W216
W217,Machine learning for estuarine salinity in harbour basins,2024,ART,S02,false,yes,W217
W218,Field measurements of wave runup in the Albury estuary,2021,ART,S11,false,yes,W218
W220,Revisiting river plumes in tidal inlets,2021,ART,S09,false,yes,W220
W221,A model of marsh accretion in mixed-energy coasts,2023,PPR,S14,false,yes,W221
W222,Low-cost methods for harbour seiches,2023,ART,S07,false,yes,W222
W223,Low-cost methods for tidal asymmetry in the Wexcombe marshes,2021,ART,S11,false,yes,W223
W224,Editorial: scaling laws for harbour seiches,2025,EDT,S09,false,no,W224
W225,Revisiting breaking waves in shallow channels,2025,ART,S09,false,yes,W225
W227,Low-cost methods for estuarine plumes: a review,2020,REV,S01,false,yes,W227
W228,Observations of coastal upwelling in the Brevin shelf,2024,ART,S09,false,yes,W228
W229,Observations of sensor calibration in a semi-enclosed sea,2023,ART,S06,false,yes,W229
W230,Low-cost methods for wave runup,2024,ART,S03,false,yes,W230
W232,A model of channel hydraulics,2019,ART,S06,false,yes,W232
W233,A framework for seabed classification,2024,ART,S06,false,yes,W233
W235,Scaling laws for coastal upwelling,2025,ART,S07,false,yes,W235
W237,Field measurements of tidal asymmetry in the open shelf,2020,ART,S12,false,yes,W237
W238,Observations of survey vessel autonomy in tidal inlets,2023,ART,S02,false,yes,W238
W239,Observations of beach profiles in harbour basins,2019,ART,S10,false,yes,W239
W240,Issue information,2025,PTX,S01,false,no,W240
W241,Seasonal variability in internal waves in a laboratory flume,2020,ART,S02,false,yes,W241
W242,Remote sensing of estuarine salinity,2024,ART,S03,false,yes,W242
W243,Field measurements of acoustic positioning in the open shelf,2019,ART,S02,false,yes,W243
W246,Low-cost methods for wave runup in a semi-enclosed sea,2023,ART,S11,false,yes,W246
W247,A framework for harbour seiches,2025,ART,S09,false,yes,W247
W249,Observations of stratified flows in tidal inlets,2025,ART,S09,false,yes,W249
W251,Remote sensing of sensor calibration,2023,ART,S02,false,yes,W219 W251
W252,Machine learning for beach profiles in the North Sea,2025,ART,S02,false,yes,W252
W253,Field measurements of dune erosion in the North Sea,2025,ART,S07,false,yes,W253
W254,Observations of storm surge in a laboratory flume,2023,ART,S12,false,yes,W254
W255,Observations of sediment flux,2025,ART,S03,false,yes,W255
W256,Machine learning for beach profiles: a review,2019,REV,S02,false,yes,W256
W257,Uncertainty in dune erosion estimates in the North Sea,2023,ART,S07,false,yes,W257
W258,A framework for tidal asymmetry,2020,ART,S10,false,yes,W258
W259,A framework for estuarine salinity,2022,ART,S07,false,yes,W259
W260,Remote sensing of stratified flows,2025,ART,S02,false,yes,W260
W261,Field measurements of sediment flux in a semi-enclosed sea: a review,2023,REV,S08,false,yes,W261
W262,Revisiting sensor calibration in a semi-enclosed sea,2025,ART,S01,false,yes,W262
W264,Seasonal variability in tidal mixing in sandy coasts,2022,ART,S10,false,yes,W264
W265,Remote sensing of coastal upwelling in tidal inlets,2025,ART,S08,false,yes,W265
W266,Low-cost methods for wave boundary layers,2024,ART,S01,false,yes,W266
W267,A framework for tidal mixing in the open shelf,2023,ART,S11,false,yes,W267
W269,Low-cost methods for tidal asymmetry,2020,ART,S10,false,yes,W269
W270,Revisiting turbulent wakes,2024,ART,S02,false,yes,W270
W271,Editorial: battery endurance,2019,EDT,S01,false,no,W271
W272,Field measurements of marsh accretion in a semi-enclosed sea: a review,2025,REV,S11,false,yes,W272
W273,Revisiting underwater docking in sandy coasts,2024,ART,S06,false,yes,W273
W274,Remote sensing of harbour seiches,2024,ART,S11,false,yes,W274
W275,Low-cost methods for marsh accretion in a macrotidal bay,2020,ART,S07,false,yes,W275
W276,A model of dune erosion in the open shelf,2022,ART,S08,false,yes,W276
W277,A model of marsh accretion in fjords: a review,2019,REV,S09,false,yes,W277
W278,A model of sediment flux in the North Sea,2020,ART,S10,false,yes,W278
W279,Low-cost methods for storm surge in shallow channels,2019,ART,S01,false,yes,W263 W279
W281,Field measurements of sediment resuspension,2021,ART,S03,false,yes,W281
W282,A framework for bed shear stress,2025,ART,S01,false,yes,W282
W284,Field measurements of sediment flux,2024,ART,S10,false,yes,W284
W285,Long-term trends in tidal mixing,2023,ART,S11,false,yes,W285
W286,Front matter,2022,PTX,S03,false,no,W286
W289,Revisiting tidal asymmetry in the open shelf,2022,ART,S09,false,yes,W289
W291,Seasonal variability in dune erosion in the open shelf,2019,ART,S07,false,yes,W291
W292,A model of underwater docking in the Albury estuary,2020,ART,S01,false,yes,W292
W293,Low-cost methods for buoy telemetry,2023,ART,S02,false,yes,W293
W294,A model of sediment flux,2019,ART,S06,false,yes,W294
W296,Observations of sensor calibration,2019,ART,S02,false,yes,W296
W297,A framework for estuarine plumes,2019,ART,S11,false,yes,W297
W299,Remote sensing of marsh accretion in the Albury estuary,2024,ART,S12,false,yes,W299
W300,A framework for vortex shedding,2025,ART,S03,false,yes,W300
W301,A framework for wave boundary layers in shallow channels,2020,ART,S02,false,yes,W301 W611
W302,A framework for estuarine plumes in a laboratory flume,2024,ART,S11,false,yes,W302
W303,A framework for tidal asymmetry in the Albury estuary,2020,ART,S03,false,yes,W303 W730
W304,Long-term trends in estuarine salinity in harbour basins,2024,ART,S01,false,yes,W304
W305,Uncertainty in marsh accretion estimates in the Albury estuary,2023,ART,S09,false,yes,W305
W306,Seasonal variability in sediment flux in the Brevin shelf,2023,PPR,S14,false,yes,W306
W308,A model of ocean optics in the open shelf,2024,ART,S01,false,yes,W308
W309,Scaling laws for vortex shedding,2019,ART,S10,false,yes,W309
W310,Machine learning for tidal asymmetry in fjords,2025,ART,S11,false,yes,W310
W312,Observations of estuarine plumes,2021,ART,S03,false,yes,W312 W522
W313,Uncertainty in turbidity sensing estimates in the Albury estuary,2021,ART,S04,false,no,W313
W314,Observations of seabed classification in the open shelf,2025,ART,S01,false,yes,W314
W315,Seasonal variability in acoustic positioning,2024,ART,S11,false,yes,W315
W317,A framework for beach profiles,2021,ART,S11,false,yes,W317
W318,A framework for internal waves,2025,ART,S11,false,yes,W318
W319,Revisiting seabed classification in shallow channels,2023,ART,S09,false,yes,W319
W320,Field measurements of coastal upwelling in the Brevin shelf,2024,ART,S08,true,no,W320
W321,Erratum: A model of breaking waves in the North Sea,2025,ERR,S03,false,no,W321
W323,A model of wave runup in the Albury estuary,2020,ART,S10,false,yes,W323
W324,A model of wave runup in sandy coasts,2019,ART,S12,false,yes,W324
W325,Remote sensing of vortex shedding in the Wexcombe marshes,2023,ART,S04,false,no,W325
W326,Seasonal variability in tidal asymmetry in the North Sea,2020,ART,S10,false,yes,W326
W330,Low-cost methods for dune erosion in the Wexcombe marshes,2025,ART,S09,false,yes,W330
W331,Editorial: ocean optics,2019,EDT,S02,false,no,W331
W332,Scaling laws for marsh accretion in mixed-energy coasts,2022,ART,S11,false,yes,W332
W333,Low-cost methods for tidal mixing,2024,ART,S01,false,yes,W333
W334,A model of tidal asymmetry in a semi-enclosed sea,2023,ART,S09,false,yes,W334
W335,Seasonal variability in dune erosion in tidal inlets,2022,ART,S09,false,yes,W335
W336,Uncertainty in river plumes estimates in a semi-enclosed sea,2021,PPR,S14,false,yes,W336
W337,Machine learning for acoustic positioning in the open shelf,2022,ART,S11,false,yes,W337
W338,Seasonal variability in acoustic positioning in a semi-enclosed sea,2025,ART,S01,false,yes,W338
W339,Uncertainty in storm surge estimates in the North Sea,2022,ART,S10,false,yes,W339
W341,Remote sensing of estuarine plumes,2020,ART,S03,false,yes,W341
W342,Field measurements of stratified flows,2023,ART,S03,false,yes,W342
W343,Revisiting battery endurance in the open shelf,2025,ART,S02,false,yes,W343
W344,Machine learning for underwater docking in the Wexcombe marshes,2020,ART,S03,false,yes,W344
W345,A framework for beach profiles in a macrotidal bay,2021,ART,S12,false,yes,W345
W346,Revisiting sonar imaging in the Albury estuary,2019,ART,S11,false,yes,W346
W348,Scaling laws for ocean optics in fjords,2021,ART,S11,false,yes,W348
W349,Scaling laws for turbidity sensing in a laboratory flume,2024,ART,S01,false,yes,W349
W350,Revisiting ocean optics,2023,ART,S03,false,yes,W350
W352,Scaling laws for storm surge in the North Sea,2024,ART,S12,false,yes,W352
W354,Scaling laws for wave runup in sandy coasts,2021,ART,S01,false,yes,W354
W355,Scaling laws for wave boundary layers in the North Sea,2024,ART,S09,false,yes,W355
W356,Long-term trends in underwater docking,2022,ART,S02,false,yes,W356
W357,Observations of tidal mixing,2025,ART,S10,false,yes,W357
W358,Scaling laws for tidal asymmetry,2024,ART,S08,false,yes,W358
W359,Seasonal variability in sediment flux in the Wexcombe marshes,2022,ART,S01,false,yes,W359
W361,A model of dune erosion,2019,ART,S01,false,yes,W361
W362,A model of beach profiles in the North Sea,2022,ART,S08,false,yes,W362
W365,Low-cost methods for channel hydraulics in a macrotidal bay,2021,ART,S03,false,yes,W365
W366,Scaling laws for tidal mixing in harbour basins,2022,ART,S03,false,yes,W366
W367,Low-cost methods for dune erosion in mixed-energy coasts,2022,ART,S02,false,yes,W367
W368,Scaling laws for seabed classification in the Wexcombe marshes: a review,2023,REV,S02,false,yes,W368
W369,Remote sensing of internal waves in shallow channels: a review,2019,REV,S11,false,yes,W369
W370,Revisiting survey vessel autonomy in the Wexcombe marshes,2025,ART,S02,false,yes,W370
W371,Editorial: a model of coastal upwelling in tidal inlets,2024,EDT,S10,false,no,W371
W373,A framework for harbour seiches in a macrotidal bay: a review,2020,REV,S11,false,yes,W373
W374,Machine learning for underwater docking in the open shelf,2023,ART,S02,true,no,W374
W376,Scaling laws for storm surge in a semi-enclosed sea,2024,ART,S10,false,yes,W376
W377,Long-term trends in marsh accretion,2021,ART,S10,false,yes,W377
W378,Seasonal variability in tidal asymmetry in mixed-energy coasts: a review,2024,REV,S02,false,yes,W378
W380,A model of marsh accretion in the Brevin shelf,2023,ART,S10,false,yes,W380
W382,Machine learning for river plumes in a semi-enclosed sea,2020,ART,S07,false,yes,W382
W383,Field measurements of turbidity sensing: a review,2023,REV,S03,false,yes,W383
W384,Machine learning for storm surge,2025,ART,S10,false,yes,W384
W385,A model of fleet coordination in mixed-energy coasts: a review,2024,REV,S09,false,yes,W385
W387,Uncertainty in internal waves estimates in the open shelf,2024,ART,S07,false,yes,W387
W388,Observations of buoy telemetry in sandy coasts,2019,ART,S01,false,yes,W388
W389,A framework for turbidity sensing in shallow channels,2025,ART,S04,false,no,W389
W390,A model of river plumes in the Brevin shelf,2022,ART,S03,false,yes,W390
W392,Field measurements of internal waves in the Wexcombe marshes,2021,ART,S11,false,yes,W392
W393,Remote sensing of tidal asymmetry in the Wexcombe marshes,2023,ART,S11,false,yes,W393
W396,Seasonal variability in battery endurance in the North Sea,2024,ART,S06,false,yes,W396
W398,Machine learning for internal waves in mixed-energy coasts,2023,ART,S12,false,yes,W398
W399,A model of marsh accretion in harbour basins,2019,ART,S09,false,yes,W399
W400,Observations of glider navigation,2019,ART,S02,false,yes,W400
W401,Long-term trends in wave boundary layers in tidal inlets,2019,ART,S10,false,yes,W401
W402,Observations of wave runup in shallow channels,2019,ART,S03,false,yes,W402
W403,Machine learning for marsh accretion in the Brevin shelf,2021,ART,S07,false,yes,W403
W404,Machine learning for marsh accretion in harbour basins,2021,ART,S07,false,yes,W404
W405,Field measurements of sediment resuspension in a macrotidal bay,2024,ART,S03,false,yes,W405
W406,Long-term trends in wave runup in a laboratory flume,2020,ART,S11,false,yes,W406
W408,A framework for coastal upwelling,2024,ART,S13,false,no,W408
W410,Low-cost methods for seabed classification in a semi-enclosed sea: a review,2020,REV,S03,false,yes,W410
W411,Revisiting turbulent wakes in the Brevin shelf,2022,ART,S02,true,no,W411
W413,Seasonal variability in sensor calibration in a laboratory flume,2023,ART,S01,false,yes,W413
W414,Uncertainty in tidal asymmetry estimates in the open shelf,2021,ART,S10,false,yes,W414
W415,Uncertainty in sediment flux estimates in the Wexcombe marshes: a review,2019,REV,S09,false,yes,W415
W417,A model of turbulent wakes in harbour basins,2023,ART,S02,false,yes,W417
W418,Editorial: dune erosion,2024,EDT,S02,false,no,W418
W419,Seasonal variability in vortex shedding,2024,ART,S02,false,yes,W419
W420,Observations of coastal upwelling in mixed-energy coasts,2020,ART,S03,false,yes,W420
W421,Low-cost methods for breaking waves,2024,ART,S02,false,yes,W421
W422,Remote sensing of coastal upwelling,2023,ART,S01,false,yes,W422 W506
W423,Seasonal variability in coastal upwelling in tidal inlets,2024,ART,S08,false,yes,W423
W424,Revisiting marsh accretion in mixed-energy coasts: a review,2019,REV,S10,false,yes,W424
W425,Uncertainty in sediment flux estimates,2020,ART,S02,false,yes,W425
W426,Seasonal variability in beach profiles in a laboratory flume,2019,ART,S01,false,yes,W426
W427,Low-cost methods for coastal upwelling in shallow channels,2023,ART,S09,false,yes,W427
W428,Revisiting turbulent wakes in the open shelf,2022,ART,S03,false,yes,W428
W430,Observations of wave runup in harbour basins,2019,ART,S09,false,yes,W430
W431,Editorial: revisiting dune erosion,2025,EDT,S11,false,no,W431
W433,A model of sediment flux in sandy coasts,2023,ART,S09,false,yes,W433
W434,Long-term trends in beach profiles in harbour basins,2025,ART,S02,false,yes,W434
W435,Remote sensing of underwater docking in a macrotidal bay,2023,ART,S06,false,yes,W435
W436,Low-cost methods for estuarine plumes in a laboratory flume,2024,ART,S01,false,yes,W436
W437,Editorial: low-cost methods for beach profiles in shallow channels,2024,EDT,S08,false,no,W437
W438,Seasonal variability in ocean optics in the open shelf,2022,ART,S11,false,yes,W438
W439,Seasonal variability in wave runup in the Wexcombe marshes,2022,ART,S09,false,yes,W439
W440,Long-term trends in harbour seiches in fjords,2022,ART,S08,false,yes,W440
W441,Observations of estuarine plumes in harbour basins,2023,ART,S11,false,yes,W441
W442,Uncertainty in harbour seiches estimates in sandy coasts,2021,ART,S09,false,yes,W442
W443,Field measurements of wave runup in a laboratory flume,2024,ART,S11,false,yes,W443
W444,Low-cost methods for wave boundary layers in a laboratory flume,2019,ART,S03,true,no,W444
W445,A framework for wave runup,2021,SUP,S06,false,yes,W445
W446,Remote sensing of dune erosion in a macrotidal bay: a review,2022,REV,S03,false,yes,W446
W448,Remote sensing of coastal upwelling in the Albury estuary,2023,ART,S13,false,no,W448
W449,Machine learning for glider navigation,2022,ART,S04,false,no,W449
W450,Remote sensing of breaking waves in the Wexcombe marshes,2021,SUP,S02,false,yes,W450
W451,Revisiting coastal upwelling in a laboratory flume: a review,2025,REV,S08,false,yes,W451
W452,Field measurements of sonar imaging in shallow channels,2021,ART,S02,false,yes,W452
W453,A framework for fleet coordination,2019,ART,S03,false,yes,W322 W453
W454,Long-term trends in vortex shedding,2021,ART,S02,false,yes,W454
W455,Uncertainty in sonar imaging estimates in sandy coasts,2021,ART,S02,false,yes,W455
W456,Uncertainty in wave runup estimates in shallow channels,2025,ART,S09,false,yes,W456
W457,A framework for marsh accretion in shallow channels: a review,2020,REV,S10,false,yes,W457
W458,Uncertainty in beach profiles estimates in a macrotidal bay,2019,ART,S08,false,yes,W458
W459,Field measurements of harbour seiches,2021,ART,S06,false,yes,W459
W461,Long-term trends in sediment flux,2019,ART,S10,false,yes,W461
W462,Machine learning for sediment flux in fjords,2021,ART,S06,false,yes,W462
W463,Machine learning for battery endurance in tidal inlets,2023,ART,S03,false,yes,W463
W464,A framework for turbidity sensing,2021,ART,S09,false,yes,W464 W663
W465,Long-term trends in buoy telemetry in a laboratory flume,2020,ART,S03,false,yes,W465
W466,Long-term trends in beach profiles,2020,ART,S08,false,yes,W466
W467,Remote sensing of harbour seiches in fjords: a review,2024,REV,S01,false,yes,W467
W469,Uncertainty in wave runup estimates in tidal inlets: a review,2020,REV,S10,false,yes,W469
W470,Uncertainty in tidal asymmetry estimates in a macrotidal bay,2022,ART,S08,false,yes,W470
W471,Uncertainty in internal waves estimates in sandy coasts,2022,ART,S09,false,yes,W471
W473,Field measurements of bed shear stress,2023,ART,S02,false,yes,W473
W474,Long-term trends in ocean optics: a review,2023,REV,S01,false,yes,W474
W475,Low-cost methods for beach profiles in the Albury estuary,2024,ART,S09,false,yes,W475
W476,Revisiting beach profiles,2021,ART,S01,false,yes,W476
W477,Field measurements of channel hydraulics: a review,2024,REV,S06,false,yes,W477
W478,Long-term trends in bed shear stress in a semi-enclosed sea,2019,ART,S01,false,yes,W478
W479,Revisiting stratified flows: a review,2020,REV,S02,false,yes,W479
W480,Editorial: ocean optics,2019,EDT,S03,false,no,W480
W481,Erratum: Machine learning for sensor calibration in a laboratory flume,2024,ERR,S09,false,no,W481
W483,Observations of marsh accretion in the Albury estuary,2019,ART,S12,false,yes,W483
W484,Scaling laws for sediment flux in the Wexcombe marshes,2020,ART,S01,false,yes,W484
W485,Revisiting tidal asymmetry in shallow channels,2021,ART,S07,false,yes,W485
W486,Uncertainty in vortex shedding estimates in the Brevin shelf,2019,ART,S10,false,yes,W486
W487,Remote sensing of wave runup in the open shelf,2024,ART,S11,false,yes,W487
W489,Scaling laws for beach profiles in the Albury estuary,2020,ART,S11,false,yes,W489
W491,Seasonal variability in wave runup in the open shelf,2020,ART,S12,false,yes,W491
W492,Field measurements of estuarine salinity,2025,ART,S09,false,yes,W492
W493,Low-cost methods for tidal asymmetry in harbour basins,2024,ART,S11,false,yes,W493
W496,Low-cost methods for sensor calibration,2022,ART,S02,false,yes,W460 W496
W497,Remote sensing of vortex shedding in mixed-energy coasts,2024,ART,S02,false,yes,W497
W498,Remote sensing of wave runup in sandy coasts,2024,ART,S07,false,yes,W498
W499,Long-term trends in turbidity sensing,2024,ART,S03,false,yes,W499
W500,Machine learning for dune erosion,2019,ART,S03,false,yes,W500
W501,Low-cost methods for glider navigation in the open shelf,2024,ART,S02,false,yes,W501
W502,Field measurements of harbour seiches in mixed-energy coasts,2019,ART,S03,false,yes,W502
W503,Observations of seabed classification in a macrotidal bay,2021,ART,S01,false,yes,W503
W504,Field measurements of breaking waves,2024,ART,S03,false,yes,W504
W505,Field measurements of storm surge in a laboratory flume,2024,ART,S10,false,yes,W505
W507,Observations of tidal asymmetry in shallow channels,2024,ART,S08,false,yes,W507
W508,Observations of internal waves in mixed-energy coasts,2021,ART,S10,false,yes,W508
W509,Uncertainty in harbour seiches estimates in fjords,2024,ART,S08,false,yes,W509
W510,Field measurements of vortex shedding,2020,ART,S03,false,yes,W510
W511,Revisiting tidal asymmetry,2023,ART,S08,false,yes,W511
W512,Long-term trends in estuarine salinity in the open shelf,2025,ART,S07,false,yes,W512
W513,Field measurements of sonar imaging,2020,ART,S02,false,yes,W513
W515,Machine learning for bed shear stress,2025,ART,S10,false,yes,W515
W516,Long-term trends in tidal asymmetry in tidal inlets,2019,ART,S03,false,yes,W516
W518,Long-term trends in turbulent wakes,2020,ART,S03,false,yes,W518
W519,A framework for internal waves in the Wexcombe marshes,2021,ART,S10,false,yes,W519
W520,Low-cost methods for estuarine salinity in mixed-energy coasts,2024,ART,S02,true,no,W520
W521,Observations of tidal asymmetry in the open shelf,2024,ART,S08,false,yes,W521
W523,Seasonal variability in sensor calibration in mixed-energy coasts,2021,ART,S03,false,yes,W523
W525,A model of harbour seiches in the open shelf,2024,ART,S02,false,yes,W525
W526,Long-term trends in storm surge in sandy coasts,2022,ART,S09,false,yes,W526
W527,Remote sensing of glider navigation,2019,ART,S11,false,yes,W527
W528,A framework for tidal mixing,2024,ART,S02,false,yes,W528
W529,Field measurements of survey vessel autonomy in the Brevin shelf,2021,ART,S03,false,yes,W529
W530,A model of stratified flows in shallow channels,2021,SUP,S06,false,yes,W530
W531,A framework for stratified flows in shallow channels,2023,ART,S01,false,yes,W531
W532,Low-cost methods for estuarine salinity in harbour basins,2024,ART,S10,false,yes,W532
W533,Long-term trends in internal waves in the Albury estuary,2023,ART,S10,false,yes,W533
W534,Uncertainty in wave runup estimates,2024,ART,S07,false,yes,W534
W535,A framework for buoy telemetry in the Albury estuary,2025,ART,S01,false,yes,W535
W536,Seasonal variability in estuarine salinity in the Albury estuary,2020,ART,S11,false,yes,W536
W538,A framework for sediment flux in the Brevin shelf,2024,ART,S08,false,yes,W538
W539,A model of stratified flows,2022,ART,S06,false,yes,W539
W540,Remote sensing of marsh accretion,2023,ART,S07,false,yes,W540
W541,Scaling laws for dune erosion in the Brevin shelf,2024,ART,S08,false,yes,W541
W542,Revisiting wave runup in the open shelf,2021,ART,S11,false,yes,W542
W544,A model of buoy telemetry in mixed-energy coasts,2025,ART,S01,false,yes,W544
W546,Low-cost methods for sonar imaging,2025,ART,S10,false,yes,W546
W547,Seasonal variability in internal waves,2021,ART,S11,false,yes,W547
W548,Editorial: observations of tidal asymmetry in the North Sea,2021,EDT,S09,false,no,W548
W549,Observations of wave boundary layers,2024,ART,S11,false,yes,W549
W550,Uncertainty in internal waves estimates in the Wexcombe marshes,2021,ART,S10,false,yes,W550
W551,A model of harbour seiches in the Wexcombe marshes,2022,ART,S11,false,yes,W551
W552,Machine learning for coastal upwelling,2019,ART,S07,false,yes,W552
W553,Field measurements of buoy telemetry in mixed-energy coasts,2022,ART,S03,false,yes,W553
W554,Remote sensing of coastal upwelling in a macrotidal bay,2024,ART,S01,false,yes,W554
W555,A model of underwater docking in a macrotidal bay,2020,ART,S09,false,yes,W555
W557,Low-cost methods for underwater docking in mixed-energy coasts,2021,ART,S03,false,yes,W557
W558,Field measurements of underwater docking in the Wexcombe marshes,2025,ART,S03,false,yes,W558
W559,Field measurements of storm surge in shallow channels,2022,ART,S11,false,yes,W559
W560,Scaling laws for tidal asymmetry in mixed-energy coasts,2023,ART,S01,false,yes,W560
W561,Front matter,2019,PTX,S06,false,no,W561
W562,Machine learning for marsh accretion in the open shelf,2019,ART,S08,false,yes,W562
W563,Low-cost methods for estuarine plumes in the Wexcombe marshes,2021,ART,S01,false,yes,W563
W564,Scaling laws for battery endurance in a semi-enclosed sea: a review,2022,REV,S01,false,yes,W564
W565,Observations of beach profiles,2019,ART,S03,false,yes,W565
W566,A model of wave runup,2023,PPR,S05,false,yes,W566
W567,Seasonal variability in turbidity sensing,2025,ART,S04,false,no,W567
W568,Remote sensing of battery endurance in the Brevin shelf,2024,ART,S01,false,yes,W568
W570,Low-cost methods for dune erosion in tidal inlets: a review,2025,REV,S12,false,yes,W570
W571,Uncertainty in harbour seiches estimates in a macrotidal bay,2024,ART,S02,false,yes,W571
W572,Editorial: seasonal variability in estuarine salinity,2019,EDT,S10,false,no,W572
W574,Revisiting stratified flows in sandy coasts,2020,ART,S02,false,yes,W574
W575,Seasonal variability in coastal upwelling in fjords: a review,2023,REV,S12,false,yes,W575
W576,Revisiting wave boundary layers in the North Sea,2021,ART,S03,false,yes,W576
W578,Seasonal variability in vortex shedding in the Brevin shelf,2024,ART,S09,false,yes,W578
W579,Machine learning for coastal upwelling in tidal inlets,2020,ART,S12,false,yes,W579
W580,Remote sensing of harbour seiches in the North Sea,2020,ART,S10,false,yes,W580
W581,Seasonal variability in sediment flux in a semi-enclosed sea,2023,ART,S10,false,yes,W581
W583,Long-term trends in dune erosion in tidal inlets,2019,ART,S10,false,yes,W583
W584,Uncertainty in dune erosion estimates in a semi-enclosed sea,2019,ART,S11,false,yes,W584
W585,Revisiting battery endurance,2024,ART,S10,false,yes,W585
W586,Long-term trends in tidal mixing in the open shelf,2025,ART,S02,false,yes,W586
W587,A framework for harbour seiches in harbour basins,2021,ART,S08,false,yes,W587
W588,Remote sensing of buoy telemetry,2019,ART,S01,false,yes,W588
W589,Observations of breaking waves,2020,ART,S11,false,yes,W589
W590,Front matter,2020,PTX,S02,false,no,W590
W592,Remote sensing of estuarine plumes in the Brevin shelf,2025,ART,S03,false,yes,W592
W593,Seasonal variability in storm surge in sandy coasts: a review,2019,REV,S12,false,yes,W593
W594,Observations of survey vessel autonomy,2025,ART,S03,false,yes,W594
W595,Field measurements of stratified flows in a laboratory flume,2024,ART,S11,false,yes,W595
W598,Revisiting underwater docking in a laboratory flume,2024,ART,S10,false,yes,W598
W599,Uncertainty in sediment resuspension estimates in the open shelf: a review,2019,REV,S01,false,yes,W599
W601,Long-term trends in coastal upwelling in a macrotidal bay: a review,2021,REV,S12,false,yes,W601
W602,Remote sensing of sonar imaging in fjords,2023,ART,S03,false,yes,W602
W603,Remote sensing of sediment resuspension in shallow channels,2025,ART,S02,false,yes,W603
W605,Long-term trends in harbour seiches in the Brevin shelf,2019,ART,S03,false,yes,W605
W606,Scaling laws for beach profiles,2023,ART,S06,false,yes,W606
W607,Scaling laws for beach profiles in shallow channels,2023,ART,S10,false,yes,W607
W608,A model of fleet coordination,2020,ART,S01,false,yes,W608
W609,Machine learning for internal waves in the open shelf,2025,ART,S08,false,yes,W609
W613,A model of dune erosion in mixed-energy coasts,2019,ART,S06,false,yes,W613
W614,Field measurements of marsh accretion in sandy coasts,2023,ART,S10,false,yes,W614
W615,Low-cost methods for marsh accretion in the Albury estuary,2023,ART,S10,false,yes,W615
W616,Low-cost methods for storm surge in harbour basins,2020,ART,S11,false,yes,W616
W617,Scaling laws for dune erosion,2025,ART,S03,false,yes,W617
W618,Low-cost methods for beach profiles in tidal inlets,2021,ART,S13,false,no,W618
W619,Seasonal variability in tidal asymmetry in sandy coasts,2022,ART,S07,false,yes,W619
W620,Revisiting river plumes in the Wexcombe marshes,2024,ART,S09,false,yes,W620
W621,Seasonal variability in turbulent wakes,2025,ART,S02,false,yes,W621
W623,Revisiting wave runup,2020,ART,S09,false,yes,W623
W624,Low-cost methods for stratified flows in the Albury estuary,2024,ART,S03,false,yes,W624
W625,Uncertainty in wave boundary layers estimates in fjords,2023,ART,S03,false,yes,W625
W626,Editorial: beach profiles,2019,EDT,S02,false,no,W626
W627,Scaling laws for wave runup in the open shelf,2021,ART,S09,false,yes,W627
W628,A framework for tidal asymmetry in the open shelf,2021,ART,S12,false,yes,W628
W629,Low-cost methods for river plumes,2023,ART,S08,false,yes,W629
W630,Machine learning for estuarine salinity in the North Sea,2019,ART,S09,false,yes,W630
W631,Low-cost methods for sediment flux,2024,ART,S01,false,yes,W631
W632,A framework for sediment flux,2025,ART,S03,false,yes,W632
W633,Long-term trends in breaking waves in sandy coasts,2025,ART,S03,false,yes,W633
W635,Scaling laws for internal waves,2021,ART,S09,false,yes,W635
W636,Machine learning for internal waves in the North Sea,2022,ART,S09,false,yes,W636
W637,Editorial: a model of river plumes in the Albury estuary,2024,EDT,S12,false,no,W637
W638,Uncertainty in marsh accretion estimates in the Wexcombe marshes,2021,ART,S09,false,yes,W638
W639,Seasonal variability in channel hydraulics in the North Sea,2019,SUP,S02,false,yes,W639
W640,Uncertainty in turbidity sensing estimates in a semi-enclosed sea,2021,ART,S02,false,yes,W416 W640
W641,A model of beach profiles,2023,ART,S11,false,yes,W641
W642,Remote sensing of wave runup in the Wexcombe marshes,2021,ART,S09,false,yes,W642
W643,Uncertainty in estuarine plumes estimates in tidal inlets,2022,ART,S03,false,yes,W643
W644,Long-term trends in marsh accretion in fjords,2025,ART,S09,false,yes,W644
W645,A framework for wave runup in mixed-energy coasts: a review,2024,REV,S08,false,yes,W645
W646,Scaling laws for internal waves in the Brevin shelf,2024,ART,S02,false,yes,W646
W648,A framework for dune erosion in the Brevin shelf,2024,ART,S02,false,yes,W648
W649,Remote sensing of tidal asymmetry,2021,ART,S11,false,yes,W649
W650,Field measurements of wave runup in a macrotidal bay,2024,ART,S12,false,yes,W650
W651,A framework for breaking waves in harbour basins,2019,ART,S03,false,yes,W651
W652,Revisiting internal waves in a semi-enclosed sea,2025,ART,S12,false,yes,W652
W654,A framework for estuarine plumes in the Brevin shelf,2024,ART,S01,false,yes,W654
W655,Seasonal variability in harbour seiches in a macrotidal bay,2020,ART,S10,false,yes,W655
W656,Scaling laws for river plumes,2020,ART,S02,false,yes,W656
W657,Long-term trends in glider navigation,2024,ART,S09,false,yes,W657
W659,Uncertainty in glider navigation estimates,2023,ART,S10,false,yes,W659
W660,A framework for buoy telemetry in a macrotidal bay,2022,ART,S01,false,yes,W660
W661,Revisiting turbidity sensing in the Albury estuary,2024,ART,S02,false,yes,W661
W662,Observations of marsh accretion,2024,ART,S11,false,yes,W662
W664,Machine learning for estuarine salinity in the Wexcombe marshes,2020,ART,S02,false,yes,W664
W665,Uncertainty in wave boundary layers estimates,2019,ART,S03,false,yes,W665 W728
W666,Field measurements of tidal asymmetry: a review,2023,REV,S09,false,yes,W666
W667,A model of internal waves in harbour basins,2023,ART,S07,false,yes,W667
W668,Field measurements of wave runup,2021,ART,S10,false,yes,W668
W669,Machine learning for river plumes in fjords,2023,ART,S11,false,yes,W669
W670,Low-cost methods for river plumes in fjords,2025,ART,S03,false,yes,W670
W671,Seasonal variability in beach profiles,2022,ART,S03,false,yes,W671
W672,Machine learning for estuarine salinity in a macrotidal bay,2019,ART,S11,false,yes,W672
W673,A model of seabed classification in harbour basins,2025,ART,S06,false,yes,W673
W674,Foreword: stratified flows,2022,EDT,S06,false,no,W674
W675,Seasonal variability in tidal mixing,2024,ART,S01,false,yes,W675
W676,Low-cost methods for turbidity sensing,2025,ART,S02,false,yes,W676
W678,Remote sensing of wave runup in fjords,2020,ART,S01,false,yes,W678
W679,Remote sensing of battery endurance in tidal inlets,2024,ART,S01,false,yes,W679
W681,Field measurements of fleet coordination,2019,ART,S03,false,yes,W681
W682,Long-term trends in battery endurance,2025,ART,S01,false,yes,W682
W683,Long-term trends in river plumes in a semi-enclosed sea,2024,ART,S07,false,yes,W683
W684,Field measurements of dune erosion in tidal inlets,2024,ART,S03,false,yes,W684
W685,Low-cost methods for dune erosion in the Brevin shelf,2023,ART,S09,false,yes,W685
W686,Field measurements of wave boundary layers in shallow channels,2022,ART,S03,false,yes,W686
W688,A model of internal waves in mixed-energy coasts,2025,ART,S10,false,yes,W688
W690,Observations of turbidity sensing,2023,ART,S02,false,yes,W690
W691,Uncertainty in turbidity sensing estimates,2023,ART,S11,false,yes,W691
W692,Low-cost methods for storm surge in a semi-enclosed sea,2020,ART,S12,false,yes,W692
W693,A framework for wave boundary layers in tidal inlets,2025,ART,S01,true,no,W693
W696,Scaling laws for tidal mixing,2019,ART,S06,false,yes,W696
W697,Observations of vortex shedding,2019,ART,S03,false,yes,W697
W699,Seasonal variability in sediment flux in mixed-energy coasts,2023,ART,S09,false,yes,W699
W702,Revisiting marsh accretion,2022,ART,S03,false,yes,W702
W703,Field measurements of estuarine salinity in the open shelf,2025,ART,S10,false,yes,W703
W704,Uncertainty in river plumes estimates,2024,ART,S09,false,yes,W704
W705,Seasonal variability in turbulent wakes in a semi-enclosed sea,2024,ART,S02,false,yes,W705
W706,Machine learning for sediment flux in the Brevin shelf,2024,REV,S04,false,no,W706
W707,Machine learning for channel hydraulics in sandy coasts,2019,ART,S02,false,yes,W707
W709,Field measurements of estuarine salinity in sandy coasts,2025,ART,S12,false,yes,W709
W710,Uncertainty in estuarine plumes estimates,2023,ART,S02,false,yes,W226 W710
W711,Remote sensing of glider navigation in mixed-energy coasts,2025,ART,S02,false,yes,W711
W713,A model of internal waves in tidal inlets,2019,ART,S09,false,yes,W713
W715,Field measurements of dune erosion,2021,ART,S02,false,yes,W715
W716,A framework for river plumes,2020,ART,S06,false,yes,W716
W718,Uncertainty in marsh accretion estimates in the North Sea: a review,2024,REV,S09,false,yes,W718
W719,Editorial: long-term trends in wave runup,2025,EDT,S07,false,no,W719
W720,Revisiting tidal mixing,2019,ART,S01,false,yes,W720
W721,Field measurements of wave runup in sandy coasts,2024,ART,S02,false,yes,W721
W722,Long-term trends in river plumes: a review,2020,REV,S09,false,yes,W722
W723,A model of vortex shedding in tidal inlets,2020,ART,S03,false,yes,W723
W724,Revisiting dune erosion in harbour basins,2020,ART,S07,false,yes,W724
W725,Remote sensing of marsh accretion in shallow channels,2022,ART,S06,false,yes,W725
W726,Remote sensing of storm surge in the Brevin shelf: a review,2020,REV,S10,false,yes,W726
W727,Field measurements of breaking waves in the Brevin shelf,2022,ART,S01,false,yes,W727
W729,Uncertainty in wave runup estimates in a macrotidal bay: a review,2024,REV,S11,false,yes,W729
W731,Long-term trends in river plumes in mixed-energy coasts,2020,ART,S10,false,yes,W731
W732,Long-term trends in coastal upwelling in a laboratory flume,2024,ART,S08,false,yes,W732
W733,Remote sensing of estuarine plumes in mixed-energy coasts,2019,ART,S01,false,yes,W733
W735,Low-cost methods for dune erosion in shallow channels,2020,ART,S07,false,yes,W735
W736,Low-cost methods for beach profiles,2024,ART,S11,false,yes,W736
W737,A model of stratified flows in the Wexcombe marshes,2019,ART,S10,false,yes,W737
W738,A framework for turbulent wakes in a laboratory flume,2022,ART,S02,false,yes,W738
W739,Field measurements of estuarine salinity in a laboratory flume: a review,2019,REV,S11,false,yes,W739
W740,Observations of marsh accretion in the open shelf,2020,ART,S07,false,yes,W740
W741,Uncertainty in coastal upwelling estimates,2021,ART,S10,false,yes,W741
W742,Field measurements of beach profiles,2019,ART,S11,false,yes,W545 W742
W744,Remote sensing of wave boundary layers,2024,ART,S01,false,yes,W744
W745,A model of sonar imaging in the Brevin shelf,2020,PPR,S05,false,yes,W745
W747,Observations of river plumes,2024,PPR,S14,false,yes,W747
W748,Revisiting battery endurance in the Brevin shelf,2024,ART,S11,false,yes,W748
W749,Field measurements of marsh accretion: a review,2019,REV,S02,false,yes,W749
W750,Long-term trends in coastal upwelling,2023,ART,S03,false,yes,W750
W751,Editorial: sensor calibration,2020,EDT,S03,false,no,W751
W752,A framework for internal waves in the Albury estuary,2020,ART,S08,false,yes,W752
W753,Field measurements of survey vessel autonomy in the Wexcombe marshes,2021,ART,S13,false,no,W753
W754,Table of contents,2022,PTX,S01,false,no,W754
W755,Machine learning for turbidity sensing in shallow channels,2019,ART,S03,false,yes,W755
W756,Editorial: low-cost methods for marsh accretion in tidal inlets,2020,EDT,S08,false,no,W756
W757,Machine learning for tidal asymmetry in tidal inlets,2023,ART,S12,false,yes,W757
W758,Low-cost methods for glider navigation in harbour basins: a review,2019,REV,S03,false,yes,W758
W760,Seasonal variability in marsh accretion in fjords,2025,ART,S11,false,yes,W760
W761,Long-term trends in battery endurance in a macrotidal bay,2024,ART,S03,false,yes,W761
W762,Seasonal variability in buoy telemetry in the Albury estuary,2024,ART,S10,false,yes,W762
W763,A model of glider navigation in a macrotidal bay,2024,ART,S13,false,no,W763
W764,Long-term trends in harbour seiches in the Albury estuary,2022,ART,S01,false,yes,W764
W765,Field measurements of storm surge in harbour basins,2025,ART,S10,false,yes,W765
W766,Erratum: A model of fleet coordination in mixed-energy coasts: a review,2025,ERR,S09,false,no,W766
W768,A model of marsh accretion in the Wexcombe marshes,2020,ART,S11,false,yes,W768
W769,Scaling laws for estuarine salinity: a review,2020,REV,S10,false,yes,W769
W770,Machine learning for coastal upwelling in the open shelf,2019,ART,S11,false,yes,W770
W771,Seasonal variability in tidal mixing in tidal inlets: a review,2019,REV,S02,false,yes,W771
W772,Field measurements of river plumes,2019,ART,S09,false,yes,W772
W773,Revisiting estuarine salinity in shallow channels,2022,ART,S11,false,yes,W773
W774,Seasonal variability in glider navigation,2024,ART,S01,false,yes,W774
W775,Machine learning for storm surge in mixed-energy coasts,2020,ART,S10,false,yes,W775
W776,Low-cost methods for harbour seiches in a semi-enclosed sea: a review,2022,REV,S10,false,yes,W776
W777,Machine learning for turbulent wakes,2023,ART,S01,false,yes,W777
W778,Long-term trends in sonar imaging,2023,ART,S13,false,no,W778
W779,Scaling laws for estuarine plumes in a semi-enclosed sea: a review,2021,REV,S02,false,yes,W779
W780,Long-term trends in ocean optics in sandy coasts,2019,PPR,S05,false,yes,W780
W781,Field measurements of turbidity sensing in the Wexcombe marshes,2025,PPR,S05,false,yes,W781
W782,Long-term trends in storm surge,2020,ART,S11,false,yes,W782
W783,A framework for stratified flows in harbour basins,2024,ART,S11,false,yes,W783
W784,Remote sensing of beach profiles in the Albury estuary,2021,ART,S12,false,yes,W784
W785,A framework for river plumes in fjords: a review,2020,REV,S09,false,yes,W785
W786,Editorial: observations of storm surge in fjords,2020,EDT,S08,false,no,W786
W787,Long-term trends in battery endurance in the Brevin shelf,2024,ART,S02,false,yes,W787
W788,Seasonal variability in wave boundary layers,2025,ART,S02,false,yes,W788
W789,Field measurements of tidal mixing,2022,ART,S09,false,yes,W1049 W789
W790,Seasonal variability in breaking waves in a macrotidal bay,2020,ART,S03,false,yes,W790
W791,Scaling laws for turbulent wakes in mixed-energy coasts,2024,ART,S02,false,yes,W791
W792,Scaling laws for harbour seiches in the North Sea,2023,ART,S06,false,yes,W792
W793,A model of stratified flows in sandy coasts,2023,SUP,S06,false,yes,W793
W794,Revisiting internal waves in tidal inlets,2025,ART,S10,false,yes,W794
W795,Field measurements of coastal upwelling in a semi-enclosed sea,2024,ART,S09,false,yes,W795
W797,Revisiting marsh accretion in shallow channels,2021,ART,S11,false,yes,W797
W798,Long-term trends in channel hydraulics,2023,ART,S02,false,yes,W798
W799,A framework for coastal upwelling in the North Sea,2022,ART,S01,false,yes,W799
W800,A model of tidal mixing in the open shelf,2025,SUP,S06,false,yes,W800
W801,Observations of seabed classification,2022,ART,S03,false,yes,W801
W803,Long-term trends in breaking waves,2023,SUP,S06,false,yes,W803
W804,Long-term trends in harbour seiches,2020,ART,S12,false,yes,W804
W806,Uncertainty in tidal mixing estimates in sandy coasts,2019,ART,S03,false,yes,W806
W807,Field measurements of harbour seiches in the North Sea,2020,ART,S03,false,yes,W524 W807
W808,Uncertainty in beach profiles estimates in the Wexcombe marshes,2021,ART,S09,false,yes,W808
W809,Revisiting coastal upwelling,2022,ART,S11,false,yes,W809
W810,Erratum: Uncertainty in internal waves estimates in the North Sea,2025,ERR,S02,false,no,W810
W811,A model of buoy telemetry in the Wexcombe marshes,2022,ART,S03,false,yes,W811
W812,Low-cost methods for buoy telemetry in the open shelf,2024,ART,S10,false,yes,W812
W813,Erratum: Remote sensing of buoy telemetry in fjords,2025,ERR,S02,false,no,W813
W814,Long-term trends in estuarine salinity in the Wexcombe marshes: a review,2025,REV,S07,false,yes,W814
W815,Low-cost methods for internal waves in fjords,2022,ART,S03,false,yes,W815
W816,Low-cost methods for sediment flux in a laboratory flume,2020,ART,S07,false,yes,W816
W817,Remote sensing of survey vessel autonomy in the Brevin shelf,2023,ART,S10,false,yes,W817
W818,Field measurements of beach profiles in the Albury estuary,2024,ART,S09,false,yes,W818
W820,Long-term trends in tidal asymmetry: a review,2019,REV,S11,false,yes,W820
W821,Low-cost methods for beach profiles in mixed-energy coasts,2023,ART,S06,false,yes,W821
W822,A framework for tidal asymmetry in the Brevin shelf,2021,ART,S09,false,yes,W822
W823,Uncertainty in marsh accretion estimates in mixed-energy coasts,2019,ART,S10,false,yes,W823
W824,A framework for sonar imaging,2022,PPR,S14,false,yes,W824
W825,Front matter,2023,PTX,S06,false,no,W825
W826,Revisiting wave runup in tidal inlets,2022,ART,S09,false,yes,W826
W827,Long-term trends in survey vessel autonomy in tidal inlets,2022,ART,S11,false,yes,W827
W828,A framework for internal waves in the open shelf,2024,ART,S09,false,yes,W828
W829,Observations of fleet coordination in the Brevin shelf,2025,ART,S02,false,yes,W829
W830,Scaling laws for turbulent wakes in the Brevin shelf,2024,ART,S02,false,yes,W830
W831,Revisiting battery endurance in the Wexcombe marshes,2025,ART,S03,false,yes,W831
W832,Revisiting breaking waves,2021,ART,S10,false,yes,W832
W833,Observations of fleet coordination in the Albury estuary,2024,ART,S03,false,yes,W833
W834,Low-cost methods for battery endurance,2023,ART,S13,false,no,W834
W835,A model of marsh accretion,2020,ART,S09,false,yes,W835
W836,Scaling laws for wave runup in harbour basins: a review,2020,REV,S07,false,yes,W836
W837,Long-term trends in bed shear stress in sandy coasts,2025,ART,S03,true,no,W837
W838,Remote sensing of wave runup in harbour basins,2019,ART,S09,false,yes,W838
W840,A model of ocean optics in the Wexcombe marshes: a review,2025,REV,S11,false,yes,W840
W842,Uncertainty in internal waves estimates,2024,ART,S02,false,yes,W842
W843,A framework for ocean optics in the Albury estuary,2023,ART,S02,false,yes,W843
W845,Low-cost methods for storm surge in a laboratory flume: a review,2022,REV,S11,false,yes,W845
W846,Revisiting acoustic positioning in the Wexcombe marshes,2024,ART,S03,false,yes,W846
W847,Observations of wave runup in mixed-energy coasts,2022,ART,S12,false,yes,W847
W848,Machine learning for wave runup,2021,ART,S02,false,yes,W848
W849,Revisiting glider navigation,2020,ART,S04,false,no,W849
W850,Long-term trends in stratified flows in the North Sea,2025,ART,S10,false,yes,W850
W851,Uncertainty in dune erosion estimates,2023,ART,S09,false,yes,W851
W852,Scaling laws for bed shear stress in the Brevin shelf,2020,ART,S01,true,no,W852
W853,Seasonal variability in estuarine plumes,2024,ART,S06,false,yes,W853
W854,Uncertainty in internal waves estimates in the North Sea,2024,ART,S02,false,yes,W854
W855,Uncertainty in vortex shedding estimates in the open shelf,2021,ART,S01,false,yes,W855
W856,Observations of estuarine salinity in tidal inlets,2024,ART,S10,false,yes,W856
W857,Long-term trends in glider navigation in the North Sea: a review,2020,REV,S06,false,yes,W857
W858,A model of dune erosion in sandy coasts,2019,ART,S12,false,yes,W858
W859,Scaling laws for sediment flux in the North Sea: a review,2023,REV,S09,false,yes,W859
W860,Machine learning for sediment flux in the Wexcombe marshes: a review,2020,REV,S01,false,yes,W860
W861,Observations of storm surge in a macrotidal bay,2019,ART,S02,false,yes,W861
W862,Revisiting harbour seiches in a semi-enclosed sea,2024,ART,S09,false,yes,W862
W863,Uncertainty in harbour seiches estimates in the open shelf,2025,ART,S01,false,yes,W863
W864,Scaling laws for sediment flux in a semi-enclosed sea,2022,ART,S08,false,yes,W864
W865,Remote sensing of beach profiles in fjords,2023,ART,S10,false,yes,W865
W867,Field measurements of internal waves,2023,ART,S11,false,yes,W867
W869,A model of survey vessel autonomy in mixed-energy coasts,2023,ART,S02,false,yes,W612 W869
W870,Seasonal variability in wave boundary layers in the Wexcombe marshes,2019,ART,S11,false,yes,W870
W871,Uncertainty in storm surge estimates in the Albury estuary,2022,ART,S11,false,yes,W871
W872,Observations of acoustic positioning,2020,ART,S11,false,yes,W872
W873,Seasonal variability in beach profiles in tidal inlets,2023,ART,S09,false,yes,W873
W874,Revisiting river plumes,2021,ART,S01,false,yes,W874
W875,Machine learning for river plumes in the North Sea: a review,2022,REV,S07,false,yes,W875
W876,Seasonal variability in estuarine plumes in fjords,2019,ART,S02,false,yes,W876
W879,Revisiting tidal asymmetry in tidal inlets,2023,ART,S02,false,yes,W432 W879
W880,A model of wave boundary layers,2020,ART,S01,false,yes,W880
W881,Machine learning for vortex shedding,2019,ART,S01,false,yes,W881
W882,Editorial: stratified flows,2020,EDT,S01,false,no,W882
W883,Front matter,2020,PTX,S02,false,no,W883
W884,Long-term trends in buoy telemetry,2019,ART,S09,false,yes,W884
W885,A framework for tidal asymmetry in the North Sea,2025,ART,S09,false,yes,W885
W886,A framework for underwater docking,2021,ART,S01,false,yes,W886
W887,Uncertainty in river plumes estimates in the Albury estuary,2020,ART,S12,false,yes,W887
W888,Remote sensing of sediment flux in a laboratory flume,2020,ART,S10,false,yes,W888
W889,Observations of battery endurance,2024,ART,S01,false,yes,W889
W890,Seasonal variability in buoy telemetry,2023,ART,S03,false,yes,W890
W891,Front matter,2022,PTX,S02,false,no,W891
W894,Revisiting harbour seiches,2024,ART,S07,false,yes,W894
W895,A framework for seabed classification in the Brevin shelf,2023,ART,S10,false,yes,W895
W896,Field measurements of storm surge in the North Sea,2019,ART,S12,false,yes,W896
W897,Remote sensing of tidal asymmetry in tidal inlets,2021,ART,S10,false,yes,W897
W900,Seasonal variability in fleet coordination in the Brevin shelf,2023,ART,S02,false,yes,W900
W901,Editorial: seasonal variability in dune erosion in sandy coasts,2020,EDT,S07,false,no,W901
W902,Low-cost methods for estuarine salinity,2021,ART,S03,false,yes,W210 W902
W903,Uncertainty in dune erosion estimates in shallow channels: a review,2020,REV,S09,false,yes,W903
W904,Revisiting sediment resuspension in the Albury estuary,2024,ART,S10,false,yes,W904
W905,Machine learning for battery endurance in a laboratory flume,2025,ART,S01,false,yes,W905
W906,Uncertainty in estuarine salinity estimates,2024,ART,S12,false,yes,W906
W907,Revisiting seabed classification,2025,ART,S03,false,yes,W907
W908,Scaling laws for sensor calibration: a review,2019,REV,S03,false,yes,W908
W910,Uncertainty in stratified flows estimates,2021,ART,S03,false,yes,W910
W913,Revisiting buoy telemetry in tidal inlets,2019,ART,S04,false,no,W913
W914,Erratum: Field measurements of channel hydraulics: a review,2025,ERR,S06,false,no,W914
W916,A framework for acoustic positioning,2019,ART,S02,false,yes,W916
W917,Revisiting sediment flux in tidal inlets,2024,ART,S01,false,yes,W917
W918,Scaling laws for tidal asymmetry in the open shelf,2025,ART,S10,false,yes,W918
W920,Scaling laws for internal waves in sandy coasts,2025,ART,S11,false,yes,W920
W921,Uncertainty in estuarine salinity estimates in sandy coasts,2023,ART,S11,false,yes,W921
W922,Observations of ocean optics,2024,ART,S02,true,no,W922
W924,Field measurements of sediment resuspension in shallow channels,2024,ART,S06,false,yes,W924
W925,Machine learning for internal waves: a review,2024,REV,S09,false,yes,W925
W926,A framework for wave runup in shallow channels,2022,ART,S02,false,yes,W926
W927,A model of storm surge in the North Sea,2020,ART,S12,false,yes,W927
W928,Observations of stratified flows in sandy coasts,2025,ART,S01,false,yes,W928
W929,Scaling laws for coastal upwelling in shallow channels,2022,ART,S01,false,yes,W929
W930,Revisiting internal waves in a laboratory flume,2025,ART,S10,false,yes,W930
W931,Revisiting buoy telemetry,2023,ART,S02,false,yes,W931
W932,Editorial: machine learning for wave runup in the Wexcombe marshes,2021,EDT,S11,false,no,W932
W933,Remote sensing of sensor calibration in the Brevin shelf,2021,ART,S03,false,yes,W933
W934,Remote sensing of harbour seiches in tidal inlets,2023,ART,S08,false,yes,W934
W935,Scaling laws for breaking waves in sandy coasts,2023,ART,S03,false,yes,W935
W936,Editorial: fleet coordination,2019,EDT,S01,false,no,W936
W937,A model of estuarine salinity,2019,ART,S01,false,yes,W937
W940,Low-cost methods for tidal asymmetry in a macrotidal bay,2022,ART,S10,false,yes,W940
W941,Field measurements of bed shear stress in shallow channels,2022,ART,S02,false,yes,W941
W942,Uncertainty in river plumes estimates in a macrotidal bay,2021,ART,S07,false,yes,W942
W943,Observations of estuarine salinity in shallow channels,2020,ART,S10,false,yes,W943
W944,Low-cost methods for harbour seiches in a laboratory flume,2019,ART,S07,false,yes,W944
W945,Uncertainty in stratified flows estimates in a semi-enclosed sea,2023,SUP,S06,false,yes,W945
W946,Low-cost methods for buoy telemetry in the Brevin shelf,2019,ART,S11,false,yes,W946
W947,Long-term trends in tidal asymmetry in fjords,2021,ART,S11,false,yes,W947
W948,A framework for wave runup in fjords,2021,ART,S01,false,yes,W948
W949,Erratum: Observations of survey vessel autonomy in tidal inlets,2024,ERR,S02,false,no,W949
W950,A model of storm surge in mixed-energy coasts,2025,ART,S11,false,yes,W950
W951,Machine learning for wave boundary layers in sandy coasts,2025,SUP,S06,false,yes,W951
W953,Remote sensing of internal waves in harbour basins,2020,ART,S09,false,yes,W953
W954,Observations of wave runup in sandy coasts,2024,ART,S09,false,yes,W954
W955,Long-term trends in coastal upwelling in sandy coasts,2021,ART,S10,false,yes,W955
W956,Long-term trends in breaking waves in a laboratory flume,2025,ART,S02,false,yes,W956
W957,Observations of channel hydraulics,2024,ART,S03,false,yes,W957
W958,Low-cost methods for underwater docking,2020,ART,S03,false,yes,W958
W959,Editorial: long-term trends in wave runup in sandy coasts,2022,EDT,S12,false,no,W959
W960,Revisiting wave runup in shallow channels,2022,ART,S12,false,yes,W960
W963,Observations of harbour seiches,2025,ART,S08,false,yes,W963
W964,Revisiting marsh accretion in the open shelf: a review,2020,REV,S12,false,yes,W964
W965,A model of breaking waves in the North Sea,2024,ART,S03,false,yes,W877 W965
W966,Editorial: scaling laws for river plumes in fjords,2024,EDT,S07,false,no,W966
W967,Seasonal variability in estuarine plumes in shallow channels,2022,ART,S06,false,yes,W967
W968,Machine learning for sensor calibration in a laboratory flume,2023,ART,S09,false,yes,W968
W969,Long-term trends in battery endurance in the Wexcombe marshes,2025,ART,S01,false,yes,W969
W970,Long-term trends in vortex shedding in the Wexcombe marshes,2019,ART,S02,false,yes,W970
W972,Long-term trends in acoustic positioning,2020,ART,S02,false,yes,W972
W973,Uncertainty in glider navigation estimates in the Brevin shelf,2024,ART,S03,true,no,W973
W975,Remote sensing of acoustic positioning in the North Sea,2019,ART,S13,false,no,W975
W976,Foreword: sediment resuspension,2021,EDT,S06,false,no,W976
W977,Seasonal variability in coastal upwelling in sandy coasts,2022,ART,S11,false,yes,W977
W978,Low-cost methods for river plumes in a laboratory flume,2020,ART,S12,false,yes,W978
W979,Machine learning for battery endurance,2021,ART,S03,false,yes,W979
W980,A framework for marsh accretion in harbour basins,2022,ART,S12,false,yes,W980
W981,Remote sensing of wave boundary layers in the Wexcombe marshes,2021,ART,S02,false,yes,W981
W983,Revisiting internal waves,2025,ART,S11,false,yes,W983
W984,A model of survey vessel autonomy,2024,ART,S01,false,yes,W984
W985,Remote sensing of vortex shedding,2023,ART,S09,false,yes,W985
W986,Remote sensing of storm surge,2020,ART,S04,false,no,W986
W988,Observations of harbour seiches in the open shelf,2021,ART,S07,false,yes,W988
W989,Editorial: long-term trends in marsh accretion in the Wexcombe marshes,2020,EDT,S08,false,no,W989
W990,Long-term trends in estuarine plumes in tidal inlets,2020,ART,S11,false,yes,W990
W991,Editorial: revisiting estuarine salinity in a laboratory flume,2023,EDT,S07,false,no,W991
W992,Field measurements of harbour seiches in a laboratory flume,2025,ART,S07,false,yes,W992
W993,Remote sensing of beach profiles in shallow channels,2025,ART,S07,false,yes,W993
W994,Uncertainty in sediment flux estimates in a laboratory flume,2024,ART,S08,false,yes,W994
W995,Low-cost methods for buoy telemetry in tidal inlets,2020,REV,S13,false,no,W995
W996,Uncertainty in stratified flows estimates in the open shelf,2021,ART,S02,false,yes,W996
W998,Machine learning for wave boundary layers in harbour basins,2022,ART,S01,false,yes,W998
W1000,Low-cost methods for internal waves,2024,ART,S01,false,yes,W1000
W1001,Machine learning for harbour seiches in mixed-energy coasts,2024,ART,S09,false,yes,W1001
W1002,A framework for dune erosion,2021,SUP,S06,false,yes,W1002
W1003,Field measurements of sensor calibration in the North Sea,2024,ART,S06,false,yes,W1003
W1004,Revisiting acoustic positioning,2024,ART,S02,false,yes,W1004
W1005,Remote sensing of buoy telemetry in fjords,2025,ART,S02,false,yes,W1005
W1006,Seasonal variability in acoustic positioning in a laboratory flume,2020,REV,S13,false,no,W1006
W1007,A model of storm surge in sandy coasts,2023,ART,S01,false,yes,W1007
W1008,Machine learning for beach profiles in sandy coasts,2025,ART,S11,false,yes,W1008
W1009,Revisiting sediment flux in the open shelf: a review,2022,REV,S12,false,yes,W1009
W1010,Revisiting vortex shedding in mixed-energy coasts,2020,ART,S02,false,yes,W1010
W1011,Scaling laws for fleet coordination in harbour basins,2021,REV,S04,false,no,W1011
W1012,Seasonal variability in marsh accretion in the Wexcombe marshes,2020,ART,S08,false,yes,W1012
W1013,Revisiting battery endurance in sandy coasts,2025,ART,S04,false,no,W1013
W1014,A model of sensor calibration in the North Sea,2023,ART,S01,false,yes,W1014
W1015,Revisiting tidal asymmetry in mixed-energy coasts,2023,ART,S12,false,yes,W1015
W1016,Scaling laws for bed shear stress in a laboratory flume,2025,ART,S06,false,yes,W1016
W1017,A model of tidal asymmetry in tidal inlets,2025,ART,S07,false,yes,W1017
W1018,Remote sensing of estuarine salinity in the Brevin shelf,2025,ART,S08,false,yes,W1018
W1019,Seasonal variability in coastal upwelling in mixed-energy coasts,2020,ART,S03,false,yes,W1019
W1020,Machine learning for vortex shedding in mixed-energy coasts,2020,ART,S13,false,no,W1020
W1021,Long-term trends in wave boundary layers,2021,ART,S02,false,yes,W1021
W1022,Uncertainty in storm surge estimates in the Wexcombe marshes,2023,ART,S09,false,yes,W1022
W1023,A model of beach profiles in mixed-energy coasts,2024,ART,S09,false,yes,W1023
W1024,Long-term trends in dune erosion in sandy coasts,2020,ART,S12,false,yes,W1024
W1025,Long-term trends in stratified flows,2020,ART,S02,true,no,W1025
W1026,A model of dune erosion in a macrotidal bay,2019,ART,S09,false,yes,W1026
W1027,Low-cost methods for bed shear stress in fjords: a review,2024,REV,S10,false,yes,W1027 W407
W1028,A model of wave runup in mixed-energy coasts,2019,ART,S03,false,yes,W1028
W1029,Seasonal variability in coastal upwelling in the open shelf,2022,ART,S09,false,yes,W1029
W1030,Low-cost methods for storm surge in the open shelf,2021,ART,S12,false,yes,W1030
W1031,Remote sensing of internal waves in the open shelf,2025,ART,S01,false,yes,W1031
W1032,Low-cost methods for coastal upwelling,2019,ART,S02,false,yes,W1032
W1033,Machine learning for tidal asymmetry,2025,ART,S08,false,yes,W1033
W1034,Foreword: tidal mixing,2025,EDT,S06,false,no,W1034
W1035,Uncertainty in ocean optics estimates in the Brevin shelf,2021,ART,S03,false,yes,W1035
W1036,Uncertainty in bed shear stress estimates in the Albury estuary,2024,ART,S06,false,yes,W1036
W1037,Low-cost methods for harbour seiches in the Wexcombe marshes,2022,ART,S02,true,no,W1037
W1038,Low-cost methods for marsh accretion,2020,ART,S02,false,yes,W1038 W556
W1039,Revisiting vortex shedding in sandy coasts,2023,ART,S11,false,yes,W1039
W1040,Field measurements of storm surge,2024,ART,S08,false,yes,W1040
W1041,Editorial: survey vessel autonomy,2025,EDT,S03,false,no,W1041
W1042,Revisiting seabed classification in a semi-enclosed sea,2025,ART,S01,false,yes,W1042
W1043,Editorial: machine learning for sediment flux,2023,EDT,S08,false,no,W1043
W1044,Machine learning for acoustic positioning in harbour basins,2021,ART,S02,false,yes,W1044
W1046,Low-cost methods for vortex shedding in a laboratory flume,2024,ART,S01,false,yes,W1046
W1047,Scaling laws for sediment flux,2020,ART,S09,false,yes,W1047
W1048,Long-term trends in fleet coordination in shallow channels,2023,ART,S10,false,yes,W1048
W1050,Low-cost methods for glider navigation in the Wexcombe marshes,2024,ART,S09,false,yes,W1050
W1051,Machine learning for estuarine salinity,2020,ART,S03,false,yes,W1051
W1052,Long-term trends in buoy telemetry in the North Sea,2019,ART,S03,false,yes,W1052
W1053,Remote sensing of tidal asymmetry in harbour basins: a review,2019,REV,S01,false,yes,W1053
W1054,A framework for sonar imaging in the Brevin shelf,2021,PPR,S05,false,yes,W1054
W1056,A model of sonar imaging,2023,ART,S02,false,yes,W1056
W1058,A model of turbidity sensing,2021,ART,S11,false,yes,W1058
W1060,Machine learning for tidal mixing,2020,ART,S11,false,yes,W1060
W1061,Remote sensing of turbidity sensing in shallow channels,2023,ART,S01,false,yes,W1061
W1062,Seasonal variability in wave runup in sandy coasts: a review,2019,REV,S02,false,yes,W1062
W1063,Low-cost methods for fleet coordination in a macrotidal bay,2019,ART,S02,false,yes,W1063
W1064,Seasonal variability in marsh accretion,2019,ART,S07,false,yes,W1064
W1065,Revisiting sensor calibration,2020,ART,S02,false,yes,W1065
```

### people.csv
```csv
person_id,name,orcid,author_ids
A01,Mara Ellison,0000-0002-9841-6229,A01 A02 A03 A101
A04,M. Ellison,0000-0004-8662-8360,A04
A05,Jonas Brandt,0000-0001-6105-5008,A05 A104
A06,Jonas Brandt,0000-0007-5475-1779,A06
A07,Priya Ramanathan,0000-0009-2298-3695,A07
A08,Tomasz Wierzba,0000-0007-9318-6032,A08 A106
A09,Lena Vossberg,0000-0000-8073-7028,A09 A103
A10,Dirk Hallmann,0000-0003-8222-6468,A10
A102,M. Ellison,0000-0008-4738-8328,A102
A105,Jonas Brandt,0000-0004-9046-7961,A105
A107,S. de Raat,0000-0006-1642-5247,A107 A11
A108,Priya Ramanathan,0000-0007-1802-8393,A108
A109,Greta Yelland,0000-0002-6545-4969,A109
A110,Quinn Yelland,0000-0003-7597-9990,A110
A111,Hester Falconer,0000-0007-5409-8704,A111
A112,Katrin Elphick,0000-0008-6293-8407,A112
A113,Henrik Corbridge,0000-0001-7569-4541,A113
A114,Ivo Brockmann,0000-0009-9653-9901,A114
A115,Tamsin Vandersloot,0000-0008-5622-7508,A115
A116,Emrys Bellamore,0000-0001-3732-2664,A116
A117,Viggo Bellamore,0000-0002-5926-5216,A117
A118,Dorian Bellamore,0000-0000-4633-9010,A118
A119,Jarno Quarrie,0000-0009-8605-0541,A119
A12,Pieter Maas,0000-0007-6472-5877,A12
A120,Linus Haverkamp,0000-0000-3133-9422,A120
A121,Marit Sallis,0000-0001-8432-2588,A121
A122,Katrin Dannecker,0000-0005-9430-8644,A122
A123,Florin Penhallow,0000-0008-6186-9535,A123
A124,Niko Vandersloot,0000-0008-3786-7418,A124
A125,Greta Ostergaard,0000-0002-5410-0810,A125
A126,Yara Quarrie,0000-0002-3972-8364,A126
A127,Delphine Ashdown,0000-0000-5148-3260,A127
A128,Jarno Tregunna,,A128
A129,Delphine Ibbotson,0000-0000-6389-2468,A129
A13,Claire Fontanet,0000-0001-8841-3301,A13
A130,Tamsin Castellan,0000-0004-8526-1242,A130
A131,Emrys Nordahl,0000-0000-3843-6782,A131
A132,Linus Penhallow,0000-0000-9780-0868,A132
A133,Liesel Lachance,0000-0003-1768-1087,A133
A134,Silas Castellan,0000-0003-3481-4429,A134
A135,Olwen Quarrie,0000-0001-4750-0051,A135
A136,Jolien Haverkamp,0000-0009-6519-3014,A136
A137,Olwen Uttley,0000-0006-0842-6639,A137
A138,Olwen Whitcombe,0000-0008-9432-6799,A138
A139,Odile Tregunna,0000-0002-2495-1719,A139
A14,Hugo Marchetti,0000-0007-5682-0525,A14
A140,Jolien Bellamore,0000-0009-0548-3869,A140
A141,Delphine Bellamore,0000-0003-0209-4519,A141
A142,Greta Rademaker,0000-0009-9961-6216,A142
A143,Marit Ibbotson,0000-0009-8383-5608,A143
A144,Silas Ashdown,0000-0007-8521-8973,A144
A145,Ivo Corbridge,0000-0006-1367-0053,A145
A146,Cosimo Bellamore,0000-0002-3308-6027,A146
A147,Niko Uttley,0000-0009-7757-5966,A147
A148,Kester Aldous,0000-0004-3203-0789,A148
A149,Liesel Whitcombe,0000-0008-7432-0373,A149
A15,Aisha Okonjo,0000-0008-9831-9489,A15
A150,Yara Castellan,0000-0006-4842-1959,A150
A151,Elsa Penhallow,0000-0008-1093-6341,A151
A152,Florin Whitcombe,,A152
A153,Emrys Merriman,0000-0008-9865-6168,A153
A154,Henrik Lachance,0000-0000-6078-6579,A154
A155,Delphine Dewhurst,,A155
A156,Greta Elphick,0000-0000-1295-1089,A156
A157,Dorian Falconer,0000-0009-2170-6438,A157
A158,Kester Jansma,0000-0009-6522-6126,A158
A159,Wren Whitcombe,0000-0009-7906-1807,A159
A16,Rhys Calloway,,A16
A160,Kester Zandvoort,0000-0006-9930-9118,A160
A161,Jolien Dewhurst,0000-0005-3613-9857,A161
A162,Liesel Ibbotson,0000-0007-2655-6310,A162
A163,Nils Jansma,0000-0004-7426-1752,A163
A164,Silas Corbridge,0000-0001-8029-9865,A164
A165,Niko Penhallow,0000-0002-5295-8953,A165
A166,Henrik Sallis,0000-0003-9677-7161,A166
A167,Henrik Haverkamp,0000-0007-4485-0931,A167
A168,Henrik Yelland,0000-0001-2141-4246,A168
A169,Ulla Haverkamp,0000-0000-8586-5161,A169
A17,Ingrid Solberg,0000-0003-9494-8214,A17
A170,Bastian Ashdown,0000-0005-3547-5180,A170
A171,Ulla Aldous,0000-0005-5058-4742,A171
A172,Hester Aldous,0000-0009-3776-6819,A172
A173,Fenna Uttley,0000-0000-4008-7950,A173
A174,Tamsin Gisborne,0000-0004-4300-1807,A174
A175,Jarno Whitcombe,0000-0000-2155-5864,A175
A176,Yara Dewhurst,0000-0004-7256-8312,A176
A177,Carys Uttley,0000-0008-3085-0372,A177
A178,Elsa Merriman,,A178
A179,Alba Ashdown,0000-0001-5735-1490,A179
A18,Bram Kuipers,0000-0001-6210-5218,A18
A180,Ilse Aldous,0000-0002-8044-9596,A180
A181,Henrik Kerridge,0000-0009-5689-0994,A181
A182,Ulla Penhallow,0000-0003-2191-4747,A182
A183,Bastian Kerridge,0000-0007-6448-2483,A183
A184,Odile Ashdown,,A184
A185,Olwen Ostergaard,0000-0005-9437-0650,A185
A186,Carys Tregunna,0000-0002-3962-9717,A186
A187,Jolien Aldous,0000-0002-8271-6177,A187
A188,Bastian Tregunna,,A188
A189,Zeno Aldous,0000-0006-2989-6155,A189
A19,Femke Hoogeveen,0000-0005-4914-5244,A19
A190,Maelle Ashdown,0000-0009-5279-0424,A190
A191,Silas Zandvoort,0000-0005-2590-0644,A191
A192,Pim Aldous,0000-0002-0569-8605,A192
A193,Niko Yelland,,A193
A194,Alba Corbridge,0000-0001-5776-4679,A194
A195,Yara Penhallow,0000-0003-6890-9836,A195
A196,Fenna Gisborne,0000-0008-9819-5281,A196
A197,Maelle Brockmann,0000-0005-2578-6292,A197
A198,Jarno Ashdown,0000-0001-4780-0378,A198
A199,Delphine Merriman,0000-0005-5487-7183,A199
A20,Joost Verhaar,0000-0001-0646-0013,A20
A200,Ivo Penhallow,0000-0000-9986-0432,A200
A201,Hester Dewhurst,0000-0002-8179-0448,A201
A202,Marit Ostergaard,0000-0007-5698-5981,A202
A203,Jolien Quarrie,0000-0007-9816-0934,A203
A204,Katrin Kerridge,0000-0002-0159-1367,A204
A205,Yara Lachance,,A205
A206,Olwen Yelland,,A206
A207,Maelle Dannecker,0000-0007-9373-7702,A207
A208,Liesel Jansma,0000-0005-1693-8254,A208
A209,Jolien Kerridge,0000-0001-6525-8467,A209
A21,Petra Lindqvist,0000-0000-4118-9557,A21
A210,Ilse Bellamore,,A210
A211,Ivo Rademaker,0000-0002-7687-0223,A211
A212,Jarno Elphick,0000-0006-5440-8972,A212
A213,Odile Whitcombe,0000-0003-3309-8851,A213
A214,Anouk Castellan,0000-0005-5240-8672,A214
A215,Zeno Dannecker,0000-0008-4772-3832,A215
A216,Nils Rademaker,0000-0001-3498-1824,A216
A217,Odile Rademaker,0000-0009-2609-6797,A217
A218,Bryony Jansma,0000-0003-3146-5873,A218
A219,Bryony Jansma,0000-0002-4103-1118,A219
A22,Niamh Corrigan,0000-0009-9065-9397,A22
A220,Hester Ostergaard,0000-0008-3455-9598,A220
A221,Hester Ostergaard,0000-0003-8085-8585,A221
A222,Liesel Aldous,0000-0009-2600-3022,A222
A223,Liesel Aldous,0000-0008-4203-7095,A223
A224,Ilse Eberhardt,0000-0009-6534-9320,A224
A225,Ilse Eberhardt,0000-0000-0712-5619,A225
A226,Cosimo Penhallow,0000-0000-1869-5361,A226
A227,Cosimo Penhallow,0000-0008-9935-6581,A227
A228,Gideon Yelland,0000-0009-3500-8530,A228
A229,Gideon Yelland,0000-0003-6264-2564,A229
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
W18,A107,I09
W19,A01,I02
W20,A09,I07
W20,A13,I11
W21,A09,I07
W21,A10,I08
W21,A107,I09
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
W32,A107,I09
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
W40,A107,I09
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
W201,A223,I30
W203,A09,I07
W203,A10,I08
W203,A139,I07
W203,A143,I08
W203,A144,I08
W203,A225,I28
W204,A184,I15
W204,A227,I31
W205,A113,I02
W205,A115,I03
W205,A123,I19
W206,A01,I02
W206,A123,I19
W208,A124,I19
W208,A229,I17
W209,A17,I14
W211,A169,I13
W214,A129,I13
W215,A177,I25
W216,A155,I12
W216,A156,I12
W217,A160,I11
W218,A218,I25
W220,A227,I31
W221,A188,I24
W222,A186,I17
W222,A188,I24
W222,A199,I18
W223,A190,I26
W223,A210,I17
W224,A177,I25
W225,A17,I14
W227,A146,I22
W227,A176,I24
W228,A185,I16
W228,A202,I26
W228,A39,I16
W229,A160,I11
W230,A160,I11
W230,A161,I11
W232,A09,I07
W232,A137,I07
W233,A110,I02
W233,A125,I19
W235,A189,I25
W235,A194,I30
W237,A184,I15
W237,A208,I15
W238,A01,I02
W238,A111,I02
W238,A32,I17
W239,A172,I15
W239,A227,I31
W241,A127,I05
W241,A128,I05
W241,A16,I05
W242,A105,I14
W243,A114,I02
W243,A119,I04
W246,A221,I30
W247,A222,I31
W249,A17,I14
W251,A07,I03
W251,A125,I19
W252,A08,I06
W253,A211,I18
W253,A217,I29
W253,A229,I17
W254,A204,I28
W254,A214,I26
W254,A36,I17
W255,A15,I13
W256,A130,I20
W256,A159,I12
W257,A200,I24
W258,A201,I25
W258,A36,I17
W259,A201,I25
W260,A10,I08
W260,A141,I07
W261,A175,I18
W261,A33,I18
W262,A07,I03
W262,A194,I30
W264,A141,I07
W264,A144,I08
W265,A226,I24
W266,A149,I09
W266,A209,I16
W266,A229,I17
W266,A43,I16
W267,A138,I07
W269,A206,I30
W269,A220,I26
W269,A36,I17
W270,A158,I12
W270,A159,I12
W270,A227,I31
W271,A01,I02
W272,A215,I27
W272,A221,I30
W273,A110,I02
W273,A163,I14
W274,A15,I13
W275,A185,I16
W275,A195,I31
W276,A157,I12
W276,A158,I12
W277,A191,I27
W278,A185,I16
W279,A163,I14
W281,A138,I07
W281,A139,I07
W282,A155,I12
W284,A43,I16
W284,A44,I17
W285,A153,I23
W289,A201,I25
W289,A207,I31
W291,A45,I18
W292,A07,I03
W292,A155,I12
W293,A07,I03
W293,A125,I19
W294,A15,I13
W294,A167,I13
W296,A130,I20
W296,A219,I30
W297,A139,I07
W299,A191,I27
W300,A158,I12
W301,A140,I07
W301,A143,I08
W301,A176,I24
W302,A158,I12
W303,A14,I12
W303,A157,I12
W303,A162,I11
W304,A132,I21
W304,A133,I21
W304,A190,I26
W305,A222,I31
W306,A127,I05
W306,A130,I20
W308,A117,I03
W308,A124,I19
W308,A40,I17
W309,A14,I12
W310,A194,I30
W312,A165,I14
W313,A163,I14
W313,A166,I14
W314,A129,I05
W314,A131,I20
W314,A212,I24
W315,A122,I19
W317,A198,I17
W317,A204,I28
W317,A212,I24
W318,A163,I14
W318,A164,I14
W319,A128,I05
W320,A41,I18
W321,A164,I14
W321,A17,I14
W323,A177,I25
W324,A229,I17
W325,A10,I07
W326,A192,I28
W330,A218,I25
W330,A30,I15
W331,A169,I13
W332,A214,I26
W332,A228,I24
W332,A33,I18
W333,A145,I08
W334,A157,I12
W335,A214,I26
W336,A198,I17
W337,A211,I18
W338,A15,I13
W338,A167,I13
W339,A184,I15
W341,A136,I07
W341,A145,I08
W342,A136,I07
W343,A160,I11
W344,A13,I11
W345,A42,I15
W346,A126,I05
W348,A118,I03
W348,A121,I04
W348,A123,I19
W349,A130,I20
W350,A110,I02
W350,A116,I03
W350,A118,I03
W352,A210,I17
W352,A40,I17
W354,A152,I09
W355,A123,I19
W356,A128,I05
W357,A102,I09
W357,A107,I09
W357,A148,I09
W357,A20,I09
W358,A199,I18
W358,A213,I25
W358,A217,I29
W359,A158,I12
W359,A159,I12
W361,A14,I12
W361,A155,I12
W362,A36,I17
W365,A138,I07
W366,A09,I07
W366,A219,I30
W367,A107,I09
W367,A151,I09
W367,A154,I23
W367,A18,I09
W368,A114,I02
W369,A180,I28
W369,A185,I16
W369,A198,I17
W370,A111,I02
W370,A113,I02
W370,A224,I16
W371,A179,I27
W371,A32,I17
W373,A34,I15
W374,A01,I02
W374,A114,I02
W376,A203,I27
W376,A215,I27
W377,A173,I16
W378,A135,I06
W378,A22,I06
W380,A174,I17
W380,A200,I24
W380,A206,I30
W382,A184,I15
W383,A110,I02
W383,A118,I03
W383,A222,I31
W384,A06,I12
W384,A157,I12
W385,A113,I02
W385,A173,I16
W387,A40,I17
W388,A131,I20
W388,A37,I18
W389,A186,I17
W389,A213,I25
W390,A148,I09
W390,A151,I09
W390,A18,I09
W390,A20,I09
W390,A33,I18
W392,A180,I28
W392,A192,I28
W393,A187,I18
W393,A31,I16
W396,A15,I13
W396,A168,I13
W398,A36,I17
W399,A173,I16
W399,A207,I31
W399,A223,I30
W400,A12,I10
W400,A170,I10
W400,A171,I10
W401,A146,I22
W401,A147,I22
W402,A169,I13
W402,A176,I24
W403,A205,I29
W403,A209,I16
W404,A189,I25
W404,A205,I29
W404,A219,I30
W405,A163,I14
W406,A178,I26
W408,A216,I28
W408,A39,I16
W410,A127,I05
W411,A18,I09
W411,A20,I09
W413,A126,I05
W413,A16,I05
W414,A182,I30
W414,A207,I31
W415,A212,I24
W415,A36,I17
W417,A09,I07
W417,A143,I08
W418,A162,I11
W419,A12,I10
W419,A137,I07
W419,A140,I07
W420,A127,I21
W421,A147,I22
W422,A102,I09
W422,A152,I09
W423,A212,I24
W424,A198,I17
W424,A218,I25
W425,A14,I12
W425,A156,I12
W425,A225,I28
W426,A08,I04
W426,A114,I02
W427,A182,I30
W428,A04,I07
W428,A174,I17
W430,A200,I24
W431,A188,I24
W433,A40,I17
W434,A163,I14
W434,A165,I14
W434,A166,I14
W434,A31,I16
W435,A07,I03
W435,A125,I19
W436,A18,I09
W436,A182,I30
W436,A197,I16
W436,A219,I30
W437,A108,I16
W437,A176,I24
W438,A12,I10
W438,A170,I10
W439,A185,I16
W440,A212,I24
W441,A128,I05
W442,A228,I24
W443,A186,I17
W443,A226,I24
W444,A10,I08
W445,A13,I11
W445,A167,I13
W446,A155,I12
W446,A156,I12
W448,A129,I05
W449,A01,I02
W450,A141,I07
W450,A143,I08
W451,A178,I26
W451,A181,I29
W451,A207,I31
W452,A119,I04
W452,A124,I19
W452,A204,I28
W453,A110,I02
W453,A118,I03
W453,A32,I17
W454,A137,I07
W454,A143,I08
W455,A129,I05
W456,A182,I30
W457,A42,I15
W458,A205,I29
W458,A43,I16
W458,A44,I17
W459,A163,I14
W461,A200,I24
W462,A155,I12
W463,A114,I02
W463,A120,I04
W464,A01,I02
W464,A224,I16
W465,A115,I03
W466,A192,I28
W467,A169,I13
W469,A185,I16
W469,A201,I25
W469,A223,I30
W470,A182,I30
W471,A35,I16
W471,A44,I17
W473,A10,I08
W474,A113,I02
W474,A118,I03
W475,A218,I25
W476,A163,I14
W477,A164,I14
W478,A09,I07
W479,A147,I22
W480,A20,I09
W481,A111,I02
W481,A120,I04
W481,A34,I15
W483,A181,I29
W484,A14,I12
W485,A41,I18
W485,A45,I18
W486,A131,I20
W487,A102,I09
W487,A177,I25
W487,A195,I31
W487,A221,I30
W489,A218,I25
W491,A38,I15
W492,A177,I25
W492,A197,I16
W493,A212,I24
W493,A35,I16
W496,A12,I10
W496,A171,I10
W497,A165,I14
W497,A189,I25
W497,A20,I09
W497,A33,I18
W498,A182,I30
W498,A222,I31
W499,A111,I02
W499,A112,I02
W499,A121,I04
W500,A15,I13
W500,A163,I14
W501,A115,I03
W502,A134,I06
W502,A22,I06
W502,A221,I30
W503,A111,I02
W503,A171,I10
W504,A10,I08
W505,A220,I26
W507,A173,I16
W507,A214,I26
W508,A224,I16
W509,A108,I16
W509,A183,I31
W509,A198,I17
W510,A140,I07
W510,A144,I08
W511,A41,I18
W512,A198,I17
W512,A41,I18
W513,A117,I03
W515,A159,I12
W516,A156,I12
W516,A157,I12
W516,A158,I12
W518,A143,I08
W518,A163,I14
W519,A189,I25
W519,A217,I29
W520,A155,I12
W521,A200,I24
W521,A209,I16
W521,A211,I18
W523,A116,I03
W523,A121,I04
W523,A203,I27
W525,A06,I12
W525,A158,I12
W526,A223,I30
W527,A117,I03
W527,A122,I19
W528,A140,I07
W529,A130,I20
W529,A221,I30
W530,A140,I07
W530,A145,I08
W531,A09,I07
W532,A184,I15
W533,A149,I09
W533,A161,I11
W534,A180,I28
W534,A228,I24
W534,A36,I17
W535,A160,I11
W535,A168,I13
W536,A211,I18
W536,A45,I18
W538,A192,I28
W538,A43,I16
W539,A107,I09
W539,A152,I09
W539,A30,I15
W540,A203,I27
W541,A214,I26
W542,A202,I26
W542,A218,I25
W544,A127,I05
W544,A128,I05
W546,A158,I12
W547,A174,I17
W547,A190,I26
W547,A212,I24
W548,A192,I28
W548,A33,I18
W549,A107,I09
W549,A163,I14
W549,A208,I15
W549,A217,I29
W550,A182,I30
W550,A192,I28
W550,A213,I25
W551,A221,I30
W552,A179,I27
W552,A202,I26
W553,A07,I03
W554,A05,I05
W555,A01,I02
W555,A123,I19
W557,A160,I11
W557,A161,I11
W558,A176,I24
W559,A212,I24
W560,A163,I14
W560,A164,I14
W560,A185,I16
W562,A34,I15
W563,A14,I12
W564,A110,I02
W564,A120,I04
W565,A05,I05
W566,A129,I05
W566,A130,I20
W567,A167,I13
W568,A110,I02
W568,A112,I02
W568,A122,I19
W570,A176,I24
W570,A204,I28
W570,A31,I16
W571,A164,I14
W571,A195,I31
W572,A182,I30
W574,A147,I22
W575,A178,I26
W575,A219,I30
W576,A107,I09
W576,A151,I09
W576,A19,I09
W578,A154,I23
W578,A164,I14
W578,A173,I16
W578,A191,I27
W579,A198,I17
W579,A31,I16
W579,A34,I15
W580,A180,I28
W580,A202,I26
W581,A31,I16
W583,A173,I16
W583,A42,I15
W584,A182,I30
W584,A211,I18
W585,A125,I19
W586,A107,I09
W586,A148,I09
W586,A152,I09
W586,A154,I23
W587,A207,I31
W587,A42,I15
W588,A117,I03
W588,A118,I03
W589,A14,I12
W589,A156,I12
W592,A155,I12
W593,A224,I16
W594,A117,I03
W594,A120,I04
W595,A141,I07
W598,A07,I03
W599,A146,I22
W601,A181,I29
W601,A41,I18
W602,A184,I15
W602,A195,I31
W603,A04,I07
W605,A169,I13
W606,A105,I14
W606,A163,I14
W607,A194,I30
W607,A214,I26
W608,A111,I02
W609,A221,I30
W609,A37,I18
W613,A08,I04
W613,A110,I02
W614,A175,I18
W614,A179,I27
W615,A108,I16
W616,A215,I27
W616,A40,I17
W617,A08,I06
W618,A194,I30
W618,A221,I30
W619,A199,I18
W620,A182,I30
W620,A220,I26
W621,A156,I12
W623,A196,I15
W623,A33,I18
W624,A137,I07
W624,A145,I08
W625,A146,I22
W626,A167,I13
W627,A205,I29
W627,A220,I26
W627,A31,I16
W628,A180,I28
W628,A186,I17
W629,A175,I18
W629,A217,I29
W629,A225,I28
W630,A38,I15
W631,A102,I09
W631,A212,I24
W631,A213,I25
W631,A34,I15
W632,A134,I06
W632,A183,I31
W632,A22,I06
W633,A162,I11
W635,A08,I04
W636,A39,I16
W637,A181,I29
W637,A187,I18
W637,A209,I16
W638,A108,I16
W638,A215,I27
W638,A228,I24
W639,A136,I07
W639,A141,I07
W640,A115,I03
W640,A37,I18
W641,A172,I15
W641,A219,I30
W642,A177,I25
W642,A33,I18
W643,A107,I09
W643,A151,I09
W643,A176,I24
W643,A18,I09
W643,A20,I09
W644,A199,I18
W644,A206,I30
W645,A197,I16
W646,A126,I05
W646,A128,I05
W646,A16,I05
W648,A127,I05
W649,A20,I09
W650,A224,I16
W650,A229,I17
W651,A154,I23
W651,A20,I09
W652,A228,I24
W654,A151,I09
W654,A162,I11
W654,A227,I31
W654,A39,I16
W655,A156,I12
W655,A157,I12
W656,A08,I04
W657,A163,I14
W657,A17,I14
W659,A111,I02
W659,A118,I03
W659,A120,I04
W660,A167,I13
W660,A169,I13
W661,A110,I02
W662,A200,I24
W662,A44,I17
W664,A08,I06
W664,A22,I06
W665,A164,I14
W666,A133,I21
W666,A200,I24
W667,A175,I18
W667,A181,I29
W667,A198,I17
W668,A207,I31
W668,A31,I16
W669,A217,I29
W669,A40,I17
W670,A164,I14
W670,A166,I14
W670,A17,I14
W670,A213,I25
W671,A08,I06
W672,A134,I06
W672,A176,I24
W672,A22,I06
W673,A130,I20
W675,A141,I07
W675,A166,I14
W676,A01,I02
W678,A162,I11
W679,A126,I05
W681,A114,I02
W681,A216,I28
W682,A204,I28
W682,A224,I16
W683,A183,I31
W684,A102,I09
W684,A174,I17
W684,A187,I18
W684,A226,I24
W685,A229,I17
W686,A09,I07
W686,A137,I07
W686,A168,I13
W688,A183,I31
W688,A220,I26
W690,A118,I03
W691,A123,I19
W691,A125,I19
W692,A196,I15
W692,A207,I31
W692,A208,I15
W693,A09,I07
W696,A102,I09
W696,A150,I09
W696,A152,I09
W696,A18,I09
W697,A145,I08
W699,A229,I17
W699,A39,I16
W702,A05,I05
W703,A208,I15
W703,A219,I30
W703,A220,I26
W704,A223,I30
W705,A137,I07
W705,A141,I07
W706,A30,I15
W707,A140,I07
W707,A142,I08
W709,A203,I27
W709,A39,I16
W710,A145,I08
W711,A156,I12
W713,A191,I27
W713,A211,I18
W713,A228,I24
W715,A149,I09
W715,A152,I09
W715,A18,I09
W716,A126,I05
W716,A127,I05
W716,A129,I05
W718,A191,I27
W718,A219,I30
W719,A193,I29
W719,A229,I17
W719,A40,I17
W720,A04,I07
W720,A34,I15
W721,A159,I12
W722,A186,I17
W723,A138,I07
W723,A141,I07
W724,A194,I30
W724,A41,I18
W725,A05,I05
W725,A128,I05
W725,A36,I17
W726,A227,I31
W726,A32,I17
W727,A165,I14
W727,A166,I14
W729,A224,I16
W731,A35,I16
W732,A199,I18
W732,A224,I16
W733,A155,I12
W735,A183,I31
W735,A228,I24
W736,A216,I28
W737,A162,I11
W737,A164,I14
W737,A17,I14
W738,A09,I07
W738,A136,I07
W739,A35,I16
W740,A178,I26
W740,A188,I24
W740,A207,I31
W741,A208,I15
W741,A212,I24
W742,A155,I12
W742,A157,I12
W742,A160,I11
W742,A228,I24
W744,A13,I11
W745,A110,I02
W747,A14,I12
W747,A157,I12
W748,A126,I05
W749,A163,I14
W749,A164,I14
W750,A158,I12
W750,A211,I18
W751,A162,I11
W752,A40,I17
W753,A126,I05
W755,A113,I02
W756,A173,I16
W756,A195,I31
W756,A220,I26
W757,A13,I11
W758,A07,I03
W758,A124,I19
W758,A14,I12
W760,A15,I13
W760,A167,I13
W760,A168,I13
W761,A22,I06
W762,A171,I10
W762,A179,I27
W763,A01,I02
W763,A110,I02
W764,A128,I05
W764,A129,I05
W764,A130,I20
W764,A179,I27
W765,A169,I13
W765,A219,I30
W766,A113,I02
W766,A173,I16
W768,A40,I17
W769,A174,I17
W770,A190,I26
W770,A217,I29
W770,A222,I31
W771,A164,I14
W771,A165,I14
W772,A206,I30
W772,A212,I24
W773,A180,I28
W774,A124,I19
W774,A125,I19
W775,A174,I17
W775,A207,I31
W775,A222,I31
W776,A193,I29
W777,A107,I09
W777,A148,I09
W777,A149,I09
W777,A151,I09
W778,A17,I14
W779,A156,I12
W780,A164,I14
W781,A161,I11
W781,A162,I11
W782,A177,I25
W782,A198,I17
W783,A158,I12
W784,A220,I26
W784,A222,I31
W785,A05,I05
W785,A127,I05
W786,A182,I30
W786,A228,I24
W786,A45,I18
W787,A07,I03
W787,A114,I02
W787,A177,I25
W788,A122,I19
W789,A141,I07
W790,A157,I12
W791,A156,I12
W791,A185,I16
W792,A05,I05
W792,A221,I30
W793,A144,I08
W794,A199,I18
W795,A180,I28
W795,A212,I24
W797,A188,I24
W797,A217,I29
W797,A32,I17
W798,A107,I09
W798,A150,I09
W798,A153,I23
W799,A14,I12
W800,A162,I11
W800,A168,I13
W801,A14,I12
W803,A156,I12
W803,A167,I13
W804,A211,I18
W806,A137,I12
W807,A15,I13
W807,A167,I13
W808,A176,I24
W809,A223,I30
W809,A34,I15
W809,A42,I15
W810,A167,I13
W810,A168,I13
W811,A162,I11
W812,A132,I21
W813,A01,I02
W813,A111,I02
W813,A198,I17
W814,A228,I24
W815,A163,I14
W815,A165,I14
W815,A228,I24
W816,A184,I15
W816,A211,I18
W817,A01,I02
W817,A120,I04
W817,A32,I17
W818,A202,I26
W818,A38,I15
W820,A187,I18
W820,A206,I30
W820,A39,I16
W821,A132,I21
W821,A133,I21
W821,A188,I24
W822,A08,I04
W822,A114,I02
W823,A201,I25
W824,A167,I13
W826,A39,I16
W827,A113,I02
W827,A118,I03
W827,A123,I19
W828,A212,I24
W828,A39,I16
W829,A161,I11
W829,A162,I11
W829,A43,I16
W830,A107,I09
W830,A164,I14
W830,A190,I26
W830,A207,I31
W831,A123,I19
W832,A138,I07
W833,A07,I03
W833,A155,I12
W834,A15,I13
W834,A167,I13
W835,A06,I12
W835,A215,I27
W836,A194,I30
W837,A158,I12
W838,A40,I17
W840,A118,I03
W840,A122,I19
W840,A125,I19
W842,A105,I14
W842,A164,I14
W843,A01,I02
W843,A164,I14
W845,A220,I26
W845,A38,I15
W846,A115,I03
W846,A118,I03
W846,A119,I04
W847,A201,I25
W848,A164,I14
W848,A165,I14
W849,A116,I03
W849,A120,I04
W850,A138,I07
W850,A229,I17
W851,A30,I15
W852,A138,I07
W853,A158,I12
W854,A167,I13
W854,A168,I13
W855,A141,I07
W856,A156,I12
W856,A159,I12
W857,A112,I02
W857,A122,I19
W857,A125,I19
W858,A180,I28
W859,A108,I16
W859,A175,I18
W859,A181,I29
W860,A132,I21
W860,A133,I21
W861,A168,I13
W861,A169,I13
W861,A178,I26
W862,A16,I05
W863,A13,I11
W863,A160,I11
W864,A192,I28
W864,A32,I17
W865,A202,I26
W865,A224,I16
W867,A128,I21
W869,A01,I02
W869,A125,I19
W869,A191,I27
W870,A107,I09
W870,A151,I09
W870,A19,I09
W871,A35,I16
W871,A45,I18
W872,A110,I02
W872,A120,I04
W873,A214,I26
W874,A132,I21
W874,A133,I21
W874,A37,I18
W875,A179,I27
W875,A210,I17
W875,A37,I18
W876,A107,I09
W876,A149,I09
W876,A151,I09
W876,A19,I09
W879,A13,I11
W879,A159,I12
W880,A150,I09
W880,A154,I23
W881,A165,I14
W881,A166,I14
W881,A178,I26
W882,A160,I11
W884,A171,I10
W884,A198,I17
W885,A19,I09
W886,A170,I10
W886,A171,I10
W886,A201,I25
W887,A194,I30
W887,A34,I15
W888,A163,I14
W888,A166,I14
W889,A167,I13
W890,A04,I07
W894,A167,I13
W894,A169,I13
W895,A167,I13
W896,A186,I17
W896,A219,I30
W896,A33,I18
W897,A16,I05
W900,A13,I11
W900,A160,I11
W901,A193,I29
W901,A228,I24
W901,A33,I18
W902,A102,I09
W903,A220,I26
W903,A228,I24
W904,A158,I12
W905,A01,I02
W905,A118,I03
W906,A108,I16
W907,A160,I11
W907,A161,I11
W907,A162,I11
W907,A188,I24
W908,A111,I02
W908,A116,I03
W908,A117,I03
W910,A107,I09
W910,A148,I09
W910,A151,I09
W910,A205,I29
W913,A113,I02
W914,A164,I14
W916,A118,I03
W917,A15,I13
W917,A169,I13
W918,A172,I15
W918,A202,I26
W920,A206,I30
W920,A45,I18
W921,A127,I05
W922,A227,I31
W924,A169,I13
W925,A213,I25
W925,A35,I16
W926,A135,I06
W926,A22,I06
W927,A188,I24
W928,A13,I11
W929,A150,I09
W929,A154,I23
W929,A18,I09
W929,A20,I09
W930,A221,I30
W931,A119,I04
W932,A200,I24
W933,A128,I05
W933,A131,I20
W933,A162,I11
W934,A183,I31
W935,A144,I08
W935,A226,I24
W936,A01,I02
W937,A161,I11
W940,A08,I06
W941,A148,I09
W942,A202,I26
W942,A204,I28
W943,A181,I29
W943,A30,I15
W944,A190,I26
W944,A205,I29
W945,A137,I07
W946,A118,I03
W947,A187,I18
W947,A30,I15
W948,A102,I09
W948,A149,I09
W948,A153,I23
W948,A19,I09
W948,A200,I24
W949,A01,I02
W949,A111,I02
W949,A32,I17
W950,A204,I28
W951,A167,I13
W953,A172,I15
W953,A44,I17
W954,A219,I30
W954,A31,I16
W955,A15,I13
W956,A140,I07
W956,A143,I08
W957,A178,I26
W957,A184,I15
W957,A19,I09
W957,A203,I27
W958,A127,I05
W958,A130,I20
W959,A223,I30
W960,A183,I31
W963,A184,I15
W963,A31,I16
W964,A172,I15
W964,A210,I17
W964,A227,I31
W965,A164,I14
W965,A17,I14
W966,A190,I26
W967,A09,I07
W968,A111,I02
W968,A120,I04
W968,A34,I15
W969,A07,I03
W969,A110,I02
W970,A156,I12
W972,A01,I02
W972,A117,I03
W972,A221,I30
W973,A111,I02
W975,A186,I17
W975,A193,I29
W977,A228,I24
W977,A42,I15
W978,A176,I24
W978,A206,I30
W979,A116,I03
W980,A212,I24
W980,A229,I17
W980,A33,I18
W981,A144,I08
W981,A226,I24
W983,A213,I25
W984,A01,I02
W984,A210,I17
W985,A04,I07
W985,A215,I27
W986,A116,I03
W988,A215,I27
W989,A210,I17
W989,A36,I17
W990,A155,I12
W990,A156,I12
W991,A211,I18
W992,A169,I13
W993,A198,I17
W993,A31,I16
W994,A206,I30
W994,A43,I16
W995,A14,I12
W996,A140,I22
W998,A04,I07
W998,A137,I07
W1000,A157,I12
W1001,A202,I26
W1001,A33,I18
W1002,A156,I12
W1002,A162,I11
W1003,A110,I02
W1003,A113,I02
W1004,A160,I11
W1005,A01,I02
W1005,A111,I02
W1005,A198,I17
W1006,A157,I12
W1007,A22,I06
W1008,A160,I11
W1008,A162,I11
W1009,A34,I15
W1009,A44,I17
W1010,A152,I09
W1010,A19,I09
W1011,A130,I20
W1012,A199,I18
W1012,A35,I16
W1013,A168,I13
W1014,A158,I12
W1014,A160,I11
W1014,A162,I11
W1015,A194,I30
W1015,A196,I15
W1015,A225,I28
W1016,A15,I13
W1017,A196,I15
W1017,A227,I31
W1017,A33,I18
W1018,A108,I16
W1019,A15,I13
W1019,A167,I13
W1020,A04,I07
W1021,A137,I22
W1022,A195,I31
W1022,A37,I18
W1023,A197,I16
W1023,A199,I18
W1024,A187,I18
W1025,A09,I07
W1026,A212,I24
W1026,A41,I18
W1027,A143,I08
W1027,A145,I08
W1028,A107,I09
W1028,A20,I09
W1029,A208,I15
W1029,A224,I16
W1030,A174,I17
W1031,A06,I12
W1031,A158,I12
W1032,A14,I12
W1032,A157,I12
W1032,A158,I12
W1033,A14,I12
W1033,A156,I12
W1035,A126,I05
W1036,A148,I09
W1036,A202,I26
W1036,A43,I16
W1036,A44,I17
W1037,A159,I12
W1038,A05,I05
W1038,A164,I14
W1039,A164,I14
W1039,A165,I14
W1040,A179,I27
W1040,A33,I18
W1041,A137,I07
W1042,A172,I15
W1043,A43,I16
W1044,A110,I02
W1044,A111,I02
W1044,A113,I02
W1044,A192,I28
W1046,A119,I04
W1047,A219,I30
W1047,A221,I30
W1047,A227,I31
W1048,A01,I02
W1050,A01,I02
W1050,A114,I02
W1051,A130,I20
W1051,A16,I05
W1052,A127,I05
W1052,A130,I20
W1053,A155,I12
W1053,A159,I12
W1054,A15,I13
W1056,A102,I09
W1058,A12,I10
W1058,A170,I10
W1058,A171,I10
W1060,A165,I14
W1060,A166,I14
W1060,A229,I17
W1061,A126,I05
W1062,A134,I06
W1062,A135,I06
W1063,A12,I10
W1063,A170,I10
W1064,A202,I26
W1064,A32,I17
W1065,A119,I04
W1065,A122,I19
W1065,A123,I19
W1065,A222,I31
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
I19,I19,0
I19,I02,1
I19,I01,2
I20,I20,0
I20,I05,1
I20,I01,2
I21,I21,0
I22,I22,0
I23,I23,0
I23,I09,1
I24,I24,0
I25,I25,0
I26,I26,0
I27,I27,0
I28,I28,0
I29,I29,0
I30,I30,0
I31,I31,0
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
S09,Journal of Coastal Hydraulics,3431-7424,JOU,K2,2,no
S10,Marine Technology Bulletin,7809-8515,JOU,K1,3,no
S11,Annals of Ocean Observation,8324-8964,JOU,K2,2,no
S12,Shelf Sea Letters,8103-2767,JOU,K1,3,no
S13,International Journal of Ocean Frontiers,1765-9671,JOU,K0,,yes
S14,CoastRxiv,,REP,,,no
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
W201,W1063
W203,W291
W204,W425
W205,W502
W208,W361
W209,W1002
W209,W341
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
W220,W733
W220,W910
W222,W251
W222,W449
W222,W599
W223,W665
W223,W896
W223,W936
W224,W272
W225,W1063
W225,W531
W225,W542
W225,W704
W225,W850
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
W239,W1032
W239,W562
W242,W350
W246,W30
W247,W740
W249,W31
W251,W271
W251,W953
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
W261,W1058
W261,W445
W262,W618
W265,W430
W265,W682
W266,W430
W267,W275
W267,W547
W267,W879
W269,W227
W270,W1044
W270,W779
W271,W1063
W271,W605
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
W279,W1063
W279,W239
W279,W665
W279,W916
W281,W932
W282,W20
W282,W341
W282,W398
W284,W312
W284,W534
W284,W559
W285,W303
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
W303,W849
W304,W1043
W305,W296
W308,W575
W308,W808
W308,W851
W309,W453
W309,W584
W309,W937
W310,W778
W312,W749
W312,W771
W313,W369
W314,W1006
W314,W1017
W314,W296
W315,W03
W315,W227
W317,W465
W317,W887
W318,W31
W318,W511
W318,W800
W325,W335
W325,W834
W325,W880
W326,W227
W326,W516
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
W349,W773
W349,W807
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
W369,W1053
W369,W296
W369,W737
W370,W484
W370,W970
W371,W404
W371,W435
W373,W876
W376,W466
W377,W870
W378,W867
W380,W699
W382,W580
W382,W785
W383,W640
W384,W1001
W384,W214
W384,W706
W387,W452
W388,W1063
W389,W593
W396,W40
W396,W803
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
W442,W1026
W442,W665
W448,W354
W448,W665
W448,W807
W453,W324
W453,W346
W453,W770
W456,W385
W456,W803
W456,W821
W457,W733
W458,W279
W458,W696
W459,W1026
W459,W271
W459,W649
W462,W277
W462,W816
W462,W901
W463,W716
W464,W741
W465,W896
W466,W588
W467,W691
W467,W696
W467,W979
W469,W820
W469,W990
W470,W972
W475,W809
W477,W1036
W477,W601
W477,W803
W478,W861
W481,W716
W486,W720
W486,W858
W487,W808
W487,W835
W489,W807
W491,W401
W496,W1024
W496,W237
W496,W269
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
W526,W453
W527,W480
W527,W823
W528,W516
W528,W869
W529,W237
W529,W860
W529,W908
W531,W1065
W531,W942
W533,W500
W533,W539
W535,W03
W535,W553
W536,W1047
W536,W491
W536,W665
W538,W669
W539,W901
W541,W630
W542,W584
W544,W03
W544,W1065
W544,W751
W544,W807
W546,W40
W546,W660
W546,W782
W547,W953
W549,W1035
W550,W1010
W550,W237
W550,W988
W551,W211
W551,W489
W552,W742
W555,W978
W557,W323
W557,W580
W558,W03
W558,W706
W559,W564
W560,W491
W562,W665
W562,W749
W567,W599
W567,W696
W567,W948
W570,W465
W570,W666
W570,W944
W572,W613
W572,W713
W575,W331
W575,W500
W576,W880
W579,W588
W579,W790
W579,W807
W580,W616
W581,W1010
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
W613,W296
W613,W453
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
W626,W1028
W626,W758
W627,W480
W627,W807
W628,W584
W628,W630
W628,W946
W629,W725
W630,W1062
W630,W461
W630,W876
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
W651,W1064
W651,W742
W651,W881
W652,W645
W652,W836
W655,W361
W655,W489
W656,W651
W656,W742
W656,W858
W657,W01
W659,W817
W659,W934
W660,W01
W660,W1035
W660,W940
W661,W848
W661,W884
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
W696,W243
W696,W369
W696,W584
W697,W626
W699,W433
W699,W782
W699,W968
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
W715,W516
W718,W413
W719,W858
W721,W970
W722,W275
W722,W303
W722,W346
W724,W579
W724,W972
W725,W354
W725,W886
W725,W995
W727,W430
W729,W420
W732,W243
W732,W465
W733,W279
W733,W502
W733,W772
W737,W1038
W737,W916
W738,W559
W739,W713
W739,W742
W739,W772
W740,W722
W742,W908
W744,W417
W744,W705
W745,W1032
W745,W457
W745,W623
W747,W1007
W747,W755
W748,W03
W749,W858
W750,W285
W750,W655
W750,W976
W751,W279
W751,W373
W751,W516
W752,W880
W753,W1052
W756,W400
W756,W816
W757,W31
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
W769,W312
W772,W742
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
W785,W1051
W785,W206
W785,W838
W786,W453
W786,W881
W787,W1058
W787,W367
W787,W467
W788,W1027
W789,W313
W789,W616
W791,W208
W791,W305
W791,W976
W792,W1044
W793,W441
W794,W1028
W794,W31
W794,W925
W794,W955
W798,W486
W799,W742
W799,W960
W800,W453
W801,W660
W803,W579
W806,W401
W807,W513
W807,W630
W807,W692
W807,W769
W807,W820
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
W836,W1053
W836,W1065
W836,W995
W838,W279
W840,W376
W840,W669
W842,W620
W842,W826
W843,W03
W846,W296
W846,W574
W846,W922
W847,W1060
W847,W453
W848,W775
W848,W882
W848,W932
W851,W1063
W851,W31
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
W861,W1026
W861,W772
W864,W696
W865,W344
W865,W756
W865,W927
W867,W874
W869,W574
W870,W211
W870,W672
W870,W944
W872,W572
W872,W696
W873,W562
W874,W1019
W874,W424
W874,W664
W875,W496
W875,W941
W875,W975
W876,W271
W876,W331
W876,W424
W879,W583
W879,W599
W880,W835
W881,W613
W882,W309
W882,W324
W882,W916
W884,W453
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
W897,W464
W897,W601
W900,W579
W901,W735
W902,W461
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
W924,W417
W924,W428
W924,W448
W924,W642
W924,W762
W925,W1037
W925,W393
W925,W886
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
W934,W1048
W934,W668
W935,W332
W935,W354
W935,W439
W936,W426
W936,W749
W937,W279
W937,W552
W940,W1012
W941,W835
W943,W201
W943,W303
W943,W513
W944,W1052
W944,W243
W944,W583
W946,W1038
W946,W277
W946,W630
W947,W415
W947,W453
W947,W784
W948,W807
W949,W1061
W949,W208
W950,W1016
W953,W562
W954,W304
W959,W457
W964,W294
W964,W399
W964,W936
W965,W471
W965,W606
W965,W784
W966,W1036
W966,W560
W966,W801
W967,W1002
W968,W587
W968,W616
W968,W713
W970,W936
W972,W755
W975,W665
W977,W752
W978,W1063
W978,W410
W978,W672
W980,W336
W980,W579
W980,W601
W981,W753
W981,W804
W984,W355
W984,W824
W986,W424
W986,W593
W988,W30
W988,W453
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
W1016,W1046
W1016,W242
W1016,W793
W1017,W246
W1018,W343
W1020,W1038
W1022,W309
W1022,W876
W1024,W401
W1024,W692
W1024,W769
W1026,W626
W1027,W1054
W1027,W349
W1027,W414
W1027,W635
W1027,W665
W1027,W902
W1029,W649
W1031,W521
W1031,W699
W1031,W702
W1032,W713
W1033,W30
W1033,W977
W1034,W1001
W1034,W383
W1034,W631
W1038,W572
W1039,W31
W1040,W896
W1042,W455
W1042,W602
W1043,W276
W1043,W422
W1043,W784
W1044,W713
W1046,W301
W1047,W870
W1048,W03
W1048,W601
W1048,W821
W1050,W774
W1051,W312
W1052,W970
W1056,W03
W1058,W555
W1058,W808
W1058,W822
W1060,W271
W1060,W552
W1060,W946
W1061,W312
W1061,W757
W1064,W1026
W1064,W944
W1065,W1024
W1065,W870
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
