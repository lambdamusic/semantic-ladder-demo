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
```

### background.md

# Scholarly publishing mechanics: a short glossary

How a manuscript becomes a published article: submission, review, production, registration and licensing. General background on how journals work.

## Submission

### Manuscript

The text an author sends to a journal, with its figures, tables and any data files. Most journals ask for it in a set format, often a word-processor file or a LaTeX source, together with a cover letter that says why the work suits the journal.

### Submission system

The web application a journal uses to receive manuscripts and track them through review. Authors upload files, reviewers download them and return reports, and editors record decisions, all in one place, so that every step leaves a dated trace.

### Scope

The range of topics a journal publishes. An editor's first check is whether a manuscript falls within it; a manuscript outside the scope is usually returned within days, without review, so that the author can send it elsewhere.

### Author guidelines

The journal's instructions on length, structure, reference style, figure resolution and the statements a manuscript must carry, such as funding and competing interests. Following them closely saves a round of back-and-forth before review begins.

## Peer review

### Handling editor

The editor who takes charge of a manuscript, chooses its reviewers and makes the decision. In large journals this is an associate editor with expertise close to the topic; the editor-in-chief sets policy and settles disputes.

### Reviewer

A researcher asked to assess a manuscript: whether its question matters, whether the methods can answer it, whether the conclusions follow from the results, and whether it is clearly written. Reviewers are usually unpaid and give their time as part of their professional duties.

### Single-blind review

The reviewers know who the authors are, but the authors do not learn who reviewed them. It is the most common arrangement in the natural sciences.

### Double-blind review

Neither side knows the other. The authors must remove their names and obvious self-references from the manuscript. It aims to reduce bias, though in a small field reviewers can often guess the authors anyway.

### Open review

The reviewers' names, and sometimes their reports, are published with the article. Supporters argue that it makes reviews more careful and gives reviewers credit; critics worry that junior reviewers will hesitate to criticise senior authors.

### Decision letter

The editor's message to the authors after review: accept, minor revision, major revision or reject. It gathers the reviewers' reports and states what the authors must change. A revised manuscript usually returns with a letter answering each point in turn.

### Revision round

One cycle of revision and re-review. Most articles go through one or two. Each round can take weeks or months, which is why the time from submission to publication varies so widely between fields.

### Desk rejection

A rejection by the editor before review, typically because the manuscript is out of scope, too preliminary or poorly prepared. It is fast, and spares reviewers' time.

### Manuscript transfer

An offer, after rejection, to move the manuscript and its reviews to another journal from the same publisher, so that the authors need not start again. The receiving editor may accept the earlier reviews or ask for new ones.

### Reviewer report

The written assessment a reviewer returns: a summary of the work, its main strengths and weaknesses, and specific requests. Many journals also ask for a confidential comment to the editor and a recommendation, which the editor weighs but need not follow.

## Production

### Copyediting

Checking the accepted text for grammar, consistency, house style and the completeness of references. A copyeditor queries anything unclear rather than changing the meaning, and the queries go back to the authors with the proofs.

### Typesetting

Laying out the edited text, figures and tables in the journal's design, for print, PDF and the web. Most publishers now typeset from a structured source, usually XML, so that the same content can be rendered in several formats.

### JATS

The Journal Article Tag Suite, an XML vocabulary for the structure of articles: front matter, body sections, figures, tables, references and back matter. Publishers, archives and indexing services exchange articles in it, which spares each of them from parsing PDFs.

### Proofs

The typeset article sent to the authors for a last check, often with a short deadline of a few days. Authors are expected to correct typesetting errors at this stage, not to rewrite the content.

### Figure preparation

Converting authors' images into formats and resolutions that print and display well, and checking colour, legibility and labelling. Line art is usually kept as vector graphics; photographs as high-resolution bitmaps.

### Accessibility

Making the published article usable by readers with disabilities: text alternatives for figures, tables marked up as tables rather than images, sufficient colour contrast and mathematics that screen readers can speak.

### Reference linking

Turning each entry in a reference list into a link to the work it names, by matching it against registration databases. Linked references let readers follow a chain of reading with one click.

## Issues and publication

### Volume and issue

The traditional way of grouping articles: a volume per year, divided into issues. Many journals now publish articles one at a time as soon as they are ready and assign them to an issue later, or have given up issues altogether.

### Continuous publication

Publishing each article when its production is complete, rather than waiting for an issue to fill. It shortens delays and suits online reading, where issues matter less.

### Article number

An identifier for an article within a volume, used in place of page numbers by journals that publish online only. It lets an article be cited before its position in an issue is known.

### Publication date

The date an article first became publicly available in its final form. Some journals record several dates: received, revised, accepted and published, which together show how long each stage took.

### Embargo

A period during which an article may not be reported by the press, or may not be shared freely, depending on the context. Press embargoes usually lift at the moment of publication.

## Identifiers and registration

### DOI

A Digital Object Identifier: a persistent identifier for a digital object, made of a prefix that identifies the registrant and a suffix the registrant chooses. A DOI is resolved through a central service to the object's current location, so a link built on it keeps working when a publisher moves its website.

### Registration agency

An organisation that assigns DOIs to its members and keeps the metadata that goes with them. Different agencies serve different communities: scholarly publishers, data repositories, film archives and others.

### Deposit

The metadata a publisher sends to a registration agency when it registers a DOI: title, contributors, journal, dates, references, licence and funding. The richer the deposit, the more useful the record is to the services that build on it.

### Resolver

The service that takes a DOI and redirects the reader to the page the registrant has registered for it. It is what makes the identifier persistent: the registrant updates the target, and every existing link follows.

### ISSN

The International Standard Serial Number, an eight-digit code for a serial publication such as a journal. A journal with print and online editions often has one ISSN for each, linked by a common identifier.

## Licensing and access

### Copyright transfer

An agreement in which the authors assign copyright in the article to the publisher, which then controls reuse. It was the norm for subscription journals and is still common there.

### Licence to publish

An agreement in which the authors keep copyright and grant the publisher the rights it needs to publish and distribute the article. It has become more common as authors and funders have asked to retain their rights.

### Open access

Making articles free to read online, without a subscription. It can be arranged in several ways, distinguished by who pays and where the free copy lives.

### Article processing charge

A fee paid, usually by the author's funder or institution, to publish an article open access in a journal that charges one. It replaces subscription income as the publisher's source of revenue for that article.

### Creative Commons licences

A family of standard public licences that let authors grant reuse rights in advance. The most permissive, CC BY, allows any reuse with attribution; others add conditions such as no commercial use or no derivative works.

### Author accepted manuscript

The author's final text after peer review, before the publisher's copyediting and typesetting. Many funders and institutions ask authors to deposit it in a repository so that a free copy exists whatever the journal's model.

### Self-archiving

Authors placing a copy of their work in an institutional or subject repository. Publishers' policies say which version may be archived, where and when.

### Transformative agreement

A contract between a publisher and a library consortium that combines reading access with open-access publishing for the consortium's authors, intended to move journals gradually from subscriptions to open access.

## Ethics and policy

### Competing interests

Financial or personal ties that could be seen to influence a piece of work. Authors, reviewers and editors are asked to declare them, so that readers can judge for themselves.

### Authorship criteria

The conditions a person must meet to be listed as an author, such as a substantial contribution to the work and approval of the final text. Contributions that fall short of them are acknowledged instead.

### Contributor roles

A standard list of roles, such as conceptualisation, data curation, formal analysis and writing, used to say who did what on an article, beyond the order of names in the byline.

### Data availability statement

A short statement in an article saying where the data behind it can be found, and on what terms, or why it cannot be shared.

### Plagiarism check

Comparing a submitted manuscript against published literature and the web with text-matching software, to find copied passages before review. Editors read the report themselves; a high match score is a prompt to look, not a verdict.

### Image integrity

Checks that figures have not been manipulated in ways that change what they show, for example by splicing gel lanes or duplicating panels. Some journals screen every accepted article.

### Publication ethics body

An organisation that publishes guidance on handling misconduct, disputes over authorship and conflicts of interest, and that journals join to signal they follow it.

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
