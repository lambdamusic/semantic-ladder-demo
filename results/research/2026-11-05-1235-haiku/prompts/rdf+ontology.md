<!-- system: You answer questions about a research-analytics dataset of works, authors, institutions, sources and citations. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

### facts.ttl (RDF, Turtle)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix res: <https://example.org/research/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

res:A39 a res:Author ;
    rdfs:label "Julien Nakagawa" ;
    res:name "Julien Nakagawa" ;
    res:orcid "0000-0003-8265-3845" .

res:AS-W01-A01-1 a res:Authorship ;
    rdfs:label "W01 A01 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A01 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W01 .

res:AS-W01-A07-1 a res:Authorship ;
    rdfs:label "W01 A07 I03" ;
    res:affiliationSeq 1 ;
    res:author res:A07 ;
    res:authorPosition 2 ;
    res:institution res:I03 ;
    res:work res:W01 .

res:AS-W02-A02-1 a res:Authorship ;
    rdfs:label "W02 A02 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A02 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W02 .

res:AS-W02-A07-1 a res:Authorship ;
    rdfs:label "W02 A07 I03" ;
    res:affiliationSeq 1 ;
    res:author res:A07 ;
    res:authorPosition 2 ;
    res:institution res:I03 ;
    res:work res:W02 .

res:AS-W03-A03-1 a res:Authorship ;
    rdfs:label "W03 A03 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A03 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W03 .

res:AS-W03-A07-1 a res:Authorship ;
    rdfs:label "W03 A07 I03" ;
    res:affiliationSeq 1 ;
    res:author res:A07 ;
    res:authorPosition 2 ;
    res:institution res:I03 ;
    res:work res:W03 .

res:AS-W04-A01-1 a res:Authorship ;
    rdfs:label "W04 A01 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A01 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W04 .

res:AS-W05-A01-1 a res:Authorship ;
    rdfs:label "W05 A01 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A01 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W05 .

res:AS-W05-A07-1 a res:Authorship ;
    rdfs:label "W05 A07 I03" ;
    res:affiliationSeq 1 ;
    res:author res:A07 ;
    res:authorPosition 2 ;
    res:institution res:I03 ;
    res:work res:W05 .

res:AS-W06-A01-1 a res:Authorship ;
    rdfs:label "W06 A01 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A01 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W06 .

res:AS-W06-A15-1 a res:Authorship ;
    rdfs:label "W06 A15 I13" ;
    res:affiliationSeq 1 ;
    res:author res:A15 ;
    res:authorPosition 2 ;
    res:institution res:I13 ;
    res:work res:W06 .

res:AS-W07-A02-1 a res:Authorship ;
    rdfs:label "W07 A02 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A02 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W07 .

res:AS-W08-A04-1 a res:Authorship ;
    rdfs:label "W08 A04 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A04 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W08 .

res:AS-W101-A30-1 a res:Authorship ;
    rdfs:label "W101 A30 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A30 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W101 .

res:AS-W101-A42-1 a res:Authorship ;
    rdfs:label "W101 A42 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A42 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W101 .

res:AS-W102-A36-1 a res:Authorship ;
    rdfs:label "W102 A36 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A36 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W102 .

res:AS-W102-A38-1 a res:Authorship ;
    rdfs:label "W102 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W102 .

res:AS-W102-A42-1 a res:Authorship ;
    rdfs:label "W102 A42 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A42 ;
    res:authorPosition 3 ;
    res:institution res:I15 ;
    res:work res:W102 .

res:AS-W103-A34-1 a res:Authorship ;
    rdfs:label "W103 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 3 ;
    res:institution res:I15 ;
    res:work res:W103 .

res:AS-W103-A35-1 a res:Authorship ;
    rdfs:label "W103 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W103 .

res:AS-W103-A41-1 a res:Authorship ;
    rdfs:label "W103 A41 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A41 ;
    res:authorPosition 2 ;
    res:institution res:I18 ;
    res:work res:W103 .

res:AS-W104-A37-1 a res:Authorship ;
    rdfs:label "W104 A37 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A37 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W104 .

res:AS-W104-A44-1 a res:Authorship ;
    rdfs:label "W104 A44 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A44 ;
    res:authorPosition 2 ;
    res:institution res:I17 ;
    res:work res:W104 .

res:AS-W104-A45-1 a res:Authorship ;
    rdfs:label "W104 A45 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A45 ;
    res:authorPosition 3 ;
    res:institution res:I18 ;
    res:work res:W104 .

res:AS-W105-A31-1 a res:Authorship ;
    rdfs:label "W105 A31 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A31 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W105 .

res:AS-W105-A40-1 a res:Authorship ;
    rdfs:label "W105 A40 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A40 ;
    res:authorPosition 2 ;
    res:institution res:I17 ;
    res:work res:W105 .

res:AS-W106-A38-1 a res:Authorship ;
    rdfs:label "W106 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W106 .

res:AS-W106-A45-1 a res:Authorship ;
    rdfs:label "W106 A45 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A45 ;
    res:authorPosition 2 ;
    res:institution res:I18 ;
    res:work res:W106 .

res:AS-W107-A32-1 a res:Authorship ;
    rdfs:label "W107 A32 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A32 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W107 .

res:AS-W107-A43-1 a res:Authorship ;
    rdfs:label "W107 A43 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A43 ;
    res:authorPosition 2 ;
    res:institution res:I16 ;
    res:work res:W107 .

res:AS-W108-A34-1 a res:Authorship ;
    rdfs:label "W108 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 3 ;
    res:institution res:I15 ;
    res:work res:W108 .

res:AS-W108-A35-1 a res:Authorship ;
    rdfs:label "W108 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W108 .

res:AS-W108-A42-1 a res:Authorship ;
    rdfs:label "W108 A42 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A42 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W108 .

res:AS-W109-A36-1 a res:Authorship ;
    rdfs:label "W109 A36 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A36 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W109 .

res:AS-W109-A42-1 a res:Authorship ;
    rdfs:label "W109 A42 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A42 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W109 .

res:AS-W109-A43-1 a res:Authorship ;
    rdfs:label "W109 A43 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A43 ;
    res:authorPosition 3 ;
    res:institution res:I16 ;
    res:work res:W109 .

res:AS-W110-A34-1 a res:Authorship ;
    rdfs:label "W110 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W110 .

res:AS-W111-A34-1 a res:Authorship ;
    rdfs:label "W111 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W111 .

res:AS-W112-A44-1 a res:Authorship ;
    rdfs:label "W112 A44 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A44 ;
    res:authorPosition 2 ;
    res:institution res:I17 ;
    res:work res:W112 .

res:AS-W112-A45-1 a res:Authorship ;
    rdfs:label "W112 A45 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A45 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W112 .

res:AS-W113-A32-1 a res:Authorship ;
    rdfs:label "W113 A32 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A32 ;
    res:authorPosition 2 ;
    res:institution res:I17 ;
    res:work res:W113 .

res:AS-W113-A43-1 a res:Authorship ;
    rdfs:label "W113 A43 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A43 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W113 .

res:AS-W114-A35-1 a res:Authorship ;
    rdfs:label "W114 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 2 ;
    res:institution res:I16 ;
    res:work res:W114 .

res:AS-W114-A38-1 a res:Authorship ;
    rdfs:label "W114 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W114 .

res:AS-W114-A42-1 a res:Authorship ;
    rdfs:label "W114 A42 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A42 ;
    res:authorPosition 3 ;
    res:institution res:I15 ;
    res:work res:W114 .

res:AS-W115-A35-1 a res:Authorship ;
    rdfs:label "W115 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W115 .

res:AS-W116-A43-1 a res:Authorship ;
    rdfs:label "W116 A43 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A43 ;
    res:authorPosition 2 ;
    res:institution res:I16 ;
    res:work res:W116 .

res:AS-W116-A44-1 a res:Authorship ;
    rdfs:label "W116 A44 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A44 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W116 .

res:AS-W117-A36-1 a res:Authorship ;
    rdfs:label "W117 A36 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A36 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W117 .

res:AS-W118-A35-1 a res:Authorship ;
    rdfs:label "W118 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W118 .

res:AS-W119-A36-1 a res:Authorship ;
    rdfs:label "W119 A36 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A36 ;
    res:authorPosition 2 ;
    res:institution res:I17 ;
    res:work res:W119 .

res:AS-W119-A41-1 a res:Authorship ;
    rdfs:label "W119 A41 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A41 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W119 .

res:AS-W12-A01-1 a res:Authorship ;
    rdfs:label "W12 A01 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A01 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W12 .

res:AS-W12-A16-1 a res:Authorship ;
    rdfs:label "W12 A16 I05" ;
    res:affiliationSeq 1 ;
    res:author res:A16 ;
    res:authorPosition 2 ;
    res:institution res:I05 ;
    res:work res:W12 .

res:AS-W120-A37-1 a res:Authorship ;
    rdfs:label "W120 A37 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A37 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W120 .

res:AS-W121-A32-1 a res:Authorship ;
    rdfs:label "W121 A32 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A32 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W121 .

res:AS-W121-A37-1 a res:Authorship ;
    rdfs:label "W121 A37 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A37 ;
    res:authorPosition 2 ;
    res:institution res:I18 ;
    res:work res:W121 .

res:AS-W122-A32-1 a res:Authorship ;
    rdfs:label "W122 A32 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A32 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W122 .

res:AS-W123-A30-1 a res:Authorship ;
    rdfs:label "W123 A30 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A30 ;
    res:authorPosition 3 ;
    res:institution res:I15 ;
    res:work res:W123 .

res:AS-W123-A38-1 a res:Authorship ;
    rdfs:label "W123 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W123 .

res:AS-W123-A45-1 a res:Authorship ;
    rdfs:label "W123 A45 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A45 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W123 .

res:AS-W124-A31-1 a res:Authorship ;
    rdfs:label "W124 A31 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A31 ;
    res:authorPosition 1 ;
    res:institution res:I16 ;
    res:work res:W124 .

res:AS-W125-A36-1 a res:Authorship ;
    rdfs:label "W125 A36 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A36 ;
    res:authorPosition 2 ;
    res:institution res:I17 ;
    res:work res:W125 .

res:AS-W125-A37-1 a res:Authorship ;
    rdfs:label "W125 A37 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A37 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W125 .

res:AS-W13-A07-1 a res:Authorship ;
    rdfs:label "W13 A07 I03" ;
    res:affiliationSeq 1 ;
    res:author res:A07 ;
    res:authorPosition 1 ;
    res:institution res:I03 ;
    res:work res:W13 .

res:AS-W14-A05-1 a res:Authorship ;
    rdfs:label "W14 A05 I05" ;
    res:affiliationSeq 1 ;
    res:author res:A05 ;
    res:authorPosition 1 ;
    res:institution res:I05 ;
    res:work res:W14 .

res:AS-W15-A15-1 a res:Authorship ;
    rdfs:label "W15 A15 I13" ;
    res:affiliationSeq 1 ;
    res:author res:A15 ;
    res:authorPosition 1 ;
    res:institution res:I13 ;
    res:work res:W15 .

res:AS-W16-A04-1 a res:Authorship ;
    rdfs:label "W16 A04 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A04 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W16 .

res:AS-W17-A13-1 a res:Authorship ;
    rdfs:label "W17 A13 I11" ;
    res:affiliationSeq 1 ;
    res:author res:A13 ;
    res:authorPosition 1 ;
    res:institution res:I11 ;
    res:work res:W17 .

res:AS-W18-A11-1 a res:Authorship ;
    rdfs:label "W18 A11 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A11 ;
    res:authorPosition 1 ;
    res:institution res:I09 ;
    res:work res:W18 .

res:AS-W19-A02-1 a res:Authorship ;
    rdfs:label "W19 A02 I02" ;
    res:affiliationSeq 1 ;
    res:author res:A02 ;
    res:authorPosition 1 ;
    res:institution res:I02 ;
    res:work res:W19 .

res:AS-W20-A09-1 a res:Authorship ;
    rdfs:label "W20 A09 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A09 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W20 .

res:AS-W20-A13-1 a res:Authorship ;
    rdfs:label "W20 A13 I11" ;
    res:affiliationSeq 1 ;
    res:author res:A13 ;
    res:authorPosition 2 ;
    res:institution res:I11 ;
    res:work res:W20 .

res:AS-W21-A09-1 a res:Authorship ;
    rdfs:label "W21 A09 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A09 ;
    res:authorPosition 2 ;
    res:institution res:I07 ;
    res:work res:W21 .

res:AS-W21-A10-1 a res:Authorship ;
    rdfs:label "W21 A10 I08" ;
    res:affiliationSeq 1 ;
    res:author res:A10 ;
    res:authorPosition 1 ;
    res:institution res:I08 ;
    res:work res:W21 .

res:AS-W21-A11-1 a res:Authorship ;
    rdfs:label "W21 A11 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A11 ;
    res:authorPosition 3 ;
    res:institution res:I09 ;
    res:work res:W21 .

res:AS-W21-A12-1 a res:Authorship ;
    rdfs:label "W21 A12 I10" ;
    res:affiliationSeq 1 ;
    res:author res:A12 ;
    res:authorPosition 4 ;
    res:institution res:I10 ;
    res:work res:W21 .

res:AS-W22-A09-1 a res:Authorship ;
    rdfs:label "W22 A09 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A09 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W22 .

res:AS-W23-A09-1 a res:Authorship ;
    rdfs:label "W23 A09 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A09 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W23 .

res:AS-W24-A10-1 a res:Authorship ;
    rdfs:label "W24 A10 I08" ;
    res:affiliationSeq 1 ;
    res:author res:A10 ;
    res:authorPosition 1 ;
    res:institution res:I08 ;
    res:work res:W24 .

res:AS-W27-A13-1 a res:Authorship ;
    rdfs:label "W27 A13 I11" ;
    res:affiliationSeq 1 ;
    res:author res:A13 ;
    res:authorPosition 2 ;
    res:institution res:I11 ;
    res:work res:W27 .

res:AS-W27-A14-1 a res:Authorship ;
    rdfs:label "W27 A14 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A14 ;
    res:authorPosition 3 ;
    res:institution res:I12 ;
    res:work res:W27 .

res:AS-W27-A17-1 a res:Authorship ;
    rdfs:label "W27 A17 I14" ;
    res:affiliationSeq 1 ;
    res:author res:A17 ;
    res:authorPosition 4 ;
    res:institution res:I14 ;
    res:work res:W27 .

res:AS-W27-A18-1 a res:Authorship ;
    rdfs:label "W27 A18 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A18 ;
    res:authorPosition 1 ;
    res:institution res:I09 ;
    res:work res:W27 .

res:AS-W28-A06-1 a res:Authorship ;
    rdfs:label "W28 A06 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A06 ;
    res:authorPosition 4 ;
    res:institution res:I12 ;
    res:work res:W28 .

res:AS-W28-A15-1 a res:Authorship ;
    rdfs:label "W28 A15 I13" ;
    res:affiliationSeq 1 ;
    res:author res:A15 ;
    res:authorPosition 2 ;
    res:institution res:I13 ;
    res:work res:W28 .

res:AS-W28-A16-1 a res:Authorship ;
    rdfs:label "W28 A16 I05" ;
    res:affiliationSeq 1 ;
    res:author res:A16 ;
    res:authorPosition 3 ;
    res:institution res:I05 ;
    res:work res:W28 .

res:AS-W28-A19-1 a res:Authorship ;
    rdfs:label "W28 A19 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A19 ;
    res:authorPosition 1 ;
    res:institution res:I09 ;
    res:work res:W28 .

res:AS-W29-A13-1 a res:Authorship ;
    rdfs:label "W29 A13 I11" ;
    res:affiliationSeq 1 ;
    res:author res:A13 ;
    res:authorPosition 4 ;
    res:institution res:I11 ;
    res:work res:W29 .

res:AS-W29-A15-1 a res:Authorship ;
    rdfs:label "W29 A15 I13" ;
    res:affiliationSeq 1 ;
    res:author res:A15 ;
    res:authorPosition 3 ;
    res:institution res:I13 ;
    res:work res:W29 .

res:AS-W29-A16-1 a res:Authorship ;
    rdfs:label "W29 A16 I05" ;
    res:affiliationSeq 1 ;
    res:author res:A16 ;
    res:authorPosition 2 ;
    res:institution res:I05 ;
    res:work res:W29 .

res:AS-W29-A20-1 a res:Authorship ;
    rdfs:label "W29 A20 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A20 ;
    res:authorPosition 1 ;
    res:institution res:I09 ;
    res:work res:W29 .

res:AS-W30-A15-1 a res:Authorship ;
    rdfs:label "W30 A15 I13" ;
    res:affiliationSeq 1 ;
    res:author res:A15 ;
    res:authorPosition 1 ;
    res:institution res:I13 ;
    res:work res:W30 .

res:AS-W31-A17-1 a res:Authorship ;
    rdfs:label "W31 A17 I14" ;
    res:affiliationSeq 1 ;
    res:author res:A17 ;
    res:authorPosition 1 ;
    res:institution res:I14 ;
    res:work res:W31 .

res:AS-W32-A11-1 a res:Authorship ;
    rdfs:label "W32 A11 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A11 ;
    res:authorPosition 1 ;
    res:institution res:I09 ;
    res:work res:W32 .

res:AS-W32-A18-1 a res:Authorship ;
    rdfs:label "W32 A18 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A18 ;
    res:authorPosition 2 ;
    res:institution res:I09 ;
    res:work res:W32 .

res:AS-W32-A19-1 a res:Authorship ;
    rdfs:label "W32 A19 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A19 ;
    res:authorPosition 3 ;
    res:institution res:I09 ;
    res:work res:W32 .

res:AS-W32-A20-1 a res:Authorship ;
    rdfs:label "W32 A20 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A20 ;
    res:authorPosition 4 ;
    res:institution res:I09 ;
    res:work res:W32 .

res:AS-W33-A14-1 a res:Authorship ;
    rdfs:label "W33 A14 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A14 ;
    res:authorPosition 1 ;
    res:institution res:I12 ;
    res:work res:W33 .

res:AS-W34-A06-1 a res:Authorship ;
    rdfs:label "W34 A06 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A06 ;
    res:authorPosition 1 ;
    res:institution res:I12 ;
    res:work res:W34 .

res:AS-W35-A14-1 a res:Authorship ;
    rdfs:label "W35 A14 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A14 ;
    res:authorPosition 1 ;
    res:institution res:I12 ;
    res:work res:W35 .

res:AS-W36-A13-1 a res:Authorship ;
    rdfs:label "W36 A13 I11" ;
    res:affiliationSeq 1 ;
    res:author res:A13 ;
    res:authorPosition 1 ;
    res:institution res:I11 ;
    res:work res:W36 .

res:AS-W37-A05-1 a res:Authorship ;
    rdfs:label "W37 A05 I05" ;
    res:affiliationSeq 1 ;
    res:author res:A05 ;
    res:authorPosition 1 ;
    res:institution res:I05 ;
    res:work res:W37 .

res:AS-W38-A06-1 a res:Authorship ;
    rdfs:label "W38 A06 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A06 ;
    res:authorPosition 1 ;
    res:institution res:I12 ;
    res:work res:W38 .

res:AS-W39-A17-1 a res:Authorship ;
    rdfs:label "W39 A17 I14" ;
    res:affiliationSeq 1 ;
    res:author res:A17 ;
    res:authorPosition 1 ;
    res:institution res:I14 ;
    res:work res:W39 .

res:AS-W40-A11-1 a res:Authorship ;
    rdfs:label "W40 A11 I09" ;
    res:affiliationSeq 1 ;
    res:author res:A11 ;
    res:authorPosition 1 ;
    res:institution res:I09 ;
    res:work res:W40 .

res:AS-W41-A14-1 a res:Authorship ;
    rdfs:label "W41 A14 I12" ;
    res:affiliationSeq 1 ;
    res:author res:A14 ;
    res:authorPosition 1 ;
    res:institution res:I12 ;
    res:work res:W41 .

res:AS-W42-A17-1 a res:Authorship ;
    rdfs:label "W42 A17 I14" ;
    res:affiliationSeq 1 ;
    res:author res:A17 ;
    res:authorPosition 1 ;
    res:institution res:I14 ;
    res:work res:W42 .

res:AS-W50-A17-1 a res:Authorship ;
    rdfs:label "W50 A17 I14" ;
    res:affiliationSeq 1 ;
    res:author res:A17 ;
    res:authorPosition 1 ;
    res:institution res:I14 ;
    res:work res:W50 .

res:AS-W51-A12-1 a res:Authorship ;
    rdfs:label "W51 A12 I10" ;
    res:affiliationSeq 1 ;
    res:author res:A12 ;
    res:authorPosition 1 ;
    res:institution res:I10 ;
    res:work res:W51 .

res:AS-W52-A13-1 a res:Authorship ;
    rdfs:label "W52 A13 I11" ;
    res:affiliationSeq 1 ;
    res:author res:A13 ;
    res:authorPosition 1 ;
    res:institution res:I11 ;
    res:work res:W52 .

res:AS-W60-A34-1 a res:Authorship ;
    rdfs:label "W60 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W60 .

res:AS-W61-A35-1 a res:Authorship ;
    rdfs:label "W61 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 2 ;
    res:institution res:I16 ;
    res:work res:W61 .

res:AS-W61-A38-1 a res:Authorship ;
    rdfs:label "W61 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W61 .

res:AS-W62-A34-1 a res:Authorship ;
    rdfs:label "W62 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W62 .

res:AS-W62-A38-1 a res:Authorship ;
    rdfs:label "W62 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W62 .

res:AS-W63-A33-1 a res:Authorship ;
    rdfs:label "W63 A33 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A33 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W63 .

res:AS-W63-A34-1 a res:Authorship ;
    rdfs:label "W63 A34 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A34 ;
    res:authorPosition 2 ;
    res:institution res:I15 ;
    res:work res:W63 .

res:AS-W63-A44-1 a res:Authorship ;
    rdfs:label "W63 A44 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A44 ;
    res:authorPosition 3 ;
    res:institution res:I17 ;
    res:work res:W63 .

res:AS-W64-A40-1 a res:Authorship ;
    rdfs:label "W64 A40 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A40 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W64 .

res:AS-W65-A35-1 a res:Authorship ;
    rdfs:label "W65 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 3 ;
    res:institution res:I16 ;
    res:work res:W65 .

res:AS-W65-A36-1 a res:Authorship ;
    rdfs:label "W65 A36 I17" ;
    res:affiliationSeq 1 ;
    res:author res:A36 ;
    res:authorPosition 1 ;
    res:institution res:I17 ;
    res:work res:W65 .

res:AS-W65-A45-1 a res:Authorship ;
    rdfs:label "W65 A45 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A45 ;
    res:authorPosition 2 ;
    res:institution res:I18 ;
    res:work res:W65 .

res:AS-W66-A38-1 a res:Authorship ;
    rdfs:label "W66 A38 I15" ;
    res:affiliationSeq 1 ;
    res:author res:A38 ;
    res:authorPosition 1 ;
    res:institution res:I15 ;
    res:work res:W66 .

res:AS-W67-A35-1 a res:Authorship ;
    rdfs:label "W67 A35 I16" ;
    res:affiliationSeq 1 ;
    res:author res:A35 ;
    res:authorPosition 2 ;
    res:institution res:I16 ;
    res:work res:W67 .

res:AS-W67-A45-1 a res:Authorship ;
    rdfs:label "W67 A45 I18" ;
    res:affiliationSeq 1 ;
    res:author res:A45 ;
    res:authorPosition 1 ;
    res:institution res:I18 ;
    res:work res:W67 .

res:AS-W70-A08-1 a res:Authorship ;
    rdfs:label "W70 A08 I04" ;
    res:affiliationSeq 1 ;
    res:author res:A08 ;
    res:authorPosition 1 ;
    res:institution res:I04 ;
    res:work res:W70 .

res:AS-W70-A08-2 a res:Authorship ;
    rdfs:label "W70 A08 I06" ;
    res:affiliationSeq 2 ;
    res:author res:A08 ;
    res:authorPosition 1 ;
    res:institution res:I06 ;
    res:work res:W70 .

res:AS-W71-A08-1 a res:Authorship ;
    rdfs:label "W71 A08 I06" ;
    res:affiliationSeq 1 ;
    res:author res:A08 ;
    res:authorPosition 1 ;
    res:institution res:I06 ;
    res:work res:W71 .

res:AS-W71-A08-2 a res:Authorship ;
    rdfs:label "W71 A08 I04" ;
    res:affiliationSeq 2 ;
    res:author res:A08 ;
    res:authorPosition 1 ;
    res:institution res:I04 ;
    res:work res:W71 .

res:AS-W72-A07-1 a res:Authorship ;
    rdfs:label "W72 A07 I03" ;
    res:affiliationSeq 1 ;
    res:author res:A07 ;
    res:authorPosition 2 ;
    res:institution res:I03 ;
    res:work res:W72 .

res:AS-W72-A08-1 a res:Authorship ;
    rdfs:label "W72 A08 I04" ;
    res:affiliationSeq 1 ;
    res:author res:A08 ;
    res:authorPosition 1 ;
    res:institution res:I04 ;
    res:work res:W72 .

res:AS-W73-A08-1 a res:Authorship ;
    rdfs:label "W73 A08 I06" ;
    res:affiliationSeq 1 ;
    res:author res:A08 ;
    res:authorPosition 1 ;
    res:institution res:I06 ;
    res:work res:W73 .

res:AS-W74-A22-1 a res:Authorship ;
    rdfs:label "W74 A22 I06" ;
    res:affiliationSeq 1 ;
    res:author res:A22 ;
    res:authorPosition 1 ;
    res:institution res:I06 ;
    res:work res:W74 .

res:AS-W75-A15-1 a res:Authorship ;
    rdfs:label "W75 A15 I13" ;
    res:affiliationSeq 1 ;
    res:author res:A15 ;
    res:authorPosition 1 ;
    res:institution res:I13 ;
    res:work res:W75 .

res:AS-W90-A21-1 a res:Authorship ;
    rdfs:label "W90 A21 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A21 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W90 .

res:AS-W91-A21-1 a res:Authorship ;
    rdfs:label "W91 A21 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A21 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W91 .

res:AS-W92-A21-1 a res:Authorship ;
    rdfs:label "W92 A21 I07" ;
    res:affiliationSeq 1 ;
    res:author res:A21 ;
    res:authorPosition 1 ;
    res:institution res:I07 ;
    res:work res:W92 .

res:C-W103-W101 a res:Citation ;
    rdfs:label "W103 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W103 .

res:C-W103-W60 a res:Citation ;
    rdfs:label "W103 cites W60" ;
    res:citedWork res:W60 ;
    res:citingWork res:W103 .

res:C-W104-W101 a res:Citation ;
    rdfs:label "W104 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W104 .

res:C-W105-W60 a res:Citation ;
    rdfs:label "W105 cites W60" ;
    res:citedWork res:W60 ;
    res:citingWork res:W105 .

res:C-W106-W104 a res:Citation ;
    rdfs:label "W106 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W106 .

res:C-W106-W61 a res:Citation ;
    rdfs:label "W106 cites W61" ;
    res:citedWork res:W61 ;
    res:citingWork res:W106 .

res:C-W107-W101 a res:Citation ;
    rdfs:label "W107 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W107 .

res:C-W107-W104 a res:Citation ;
    rdfs:label "W107 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W107 .

res:C-W108-W101 a res:Citation ;
    rdfs:label "W108 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W108 .

res:C-W108-W104 a res:Citation ;
    rdfs:label "W108 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W108 .

res:C-W108-W60 a res:Citation ;
    rdfs:label "W108 cites W60" ;
    res:citedWork res:W60 ;
    res:citingWork res:W108 .

res:C-W109-W101 a res:Citation ;
    rdfs:label "W109 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W109 .

res:C-W109-W104 a res:Citation ;
    rdfs:label "W109 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W109 .

res:C-W110-W60 a res:Citation ;
    rdfs:label "W110 cites W60" ;
    res:citedWork res:W60 ;
    res:citingWork res:W110 .

res:C-W111-W104 a res:Citation ;
    rdfs:label "W111 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W111 .

res:C-W111-W107 a res:Citation ;
    rdfs:label "W111 cites W107" ;
    res:citedWork res:W107 ;
    res:citingWork res:W111 .

res:C-W111-W64 a res:Citation ;
    rdfs:label "W111 cites W64" ;
    res:citedWork res:W64 ;
    res:citingWork res:W111 .

res:C-W113-W110 a res:Citation ;
    rdfs:label "W113 cites W110" ;
    res:citedWork res:W110 ;
    res:citingWork res:W113 .

res:C-W114-W104 a res:Citation ;
    rdfs:label "W114 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W114 .

res:C-W115-W114 a res:Citation ;
    rdfs:label "W115 cites W114" ;
    res:citedWork res:W114 ;
    res:citingWork res:W115 .

res:C-W116-W104 a res:Citation ;
    rdfs:label "W116 cites W104" ;
    res:citedWork res:W104 ;
    res:citingWork res:W116 .

res:C-W118-W106 a res:Citation ;
    rdfs:label "W118 cites W106" ;
    res:citedWork res:W106 ;
    res:citingWork res:W118 .

res:C-W118-W66 a res:Citation ;
    rdfs:label "W118 cites W66" ;
    res:citedWork res:W66 ;
    res:citingWork res:W118 .

res:C-W119-W109 a res:Citation ;
    rdfs:label "W119 cites W109" ;
    res:citedWork res:W109 ;
    res:citingWork res:W119 .

res:C-W119-W114 a res:Citation ;
    rdfs:label "W119 cites W114" ;
    res:citedWork res:W114 ;
    res:citingWork res:W119 .

res:C-W12-W03 a res:Citation ;
    rdfs:label "W12 cites W03" ;
    res:citedWork res:W03 ;
    res:citingWork res:W12 .

res:C-W120-W108 a res:Citation ;
    rdfs:label "W120 cites W108" ;
    res:citedWork res:W108 ;
    res:citingWork res:W120 .

res:C-W120-W112 a res:Citation ;
    rdfs:label "W120 cites W112" ;
    res:citedWork res:W112 ;
    res:citingWork res:W120 .

res:C-W121-W112 a res:Citation ;
    rdfs:label "W121 cites W112" ;
    res:citedWork res:W112 ;
    res:citingWork res:W121 .

res:C-W121-W113 a res:Citation ;
    rdfs:label "W121 cites W113" ;
    res:citedWork res:W113 ;
    res:citingWork res:W121 .

res:C-W123-W101 a res:Citation ;
    rdfs:label "W123 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W123 .

res:C-W123-W60 a res:Citation ;
    rdfs:label "W123 cites W60" ;
    res:citedWork res:W60 ;
    res:citingWork res:W123 .

res:C-W124-W101 a res:Citation ;
    rdfs:label "W124 cites W101" ;
    res:citedWork res:W101 ;
    res:citingWork res:W124 .

res:C-W124-W107 a res:Citation ;
    rdfs:label "W124 cites W107" ;
    res:citedWork res:W107 ;
    res:citingWork res:W124 .

res:C-W124-W114 a res:Citation ;
    rdfs:label "W124 cites W114" ;
    res:citedWork res:W114 ;
    res:citingWork res:W124 .

res:C-W125-W105 a res:Citation ;
    rdfs:label "W125 cites W105" ;
    res:citedWork res:W105 ;
    res:citingWork res:W125 .

res:C-W125-W108 a res:Citation ;
    rdfs:label "W125 cites W108" ;
    res:citedWork res:W108 ;
    res:citingWork res:W125 .

res:C-W125-W61 a res:Citation ;
    rdfs:label "W125 cites W61" ;
    res:citedWork res:W61 ;
    res:citingWork res:W125 .

res:C-W13-W03 a res:Citation ;
    rdfs:label "W13 cites W03" ;
    res:citedWork res:W03 ;
    res:citingWork res:W13 .

res:C-W14-W03 a res:Citation ;
    rdfs:label "W14 cites W03" ;
    res:citedWork res:W03 ;
    res:citingWork res:W14 .

res:C-W15-W02 a res:Citation ;
    rdfs:label "W15 cites W02" ;
    res:citedWork res:W02 ;
    res:citingWork res:W15 .

res:C-W15-W03 a res:Citation ;
    rdfs:label "W15 cites W03" ;
    res:citedWork res:W03 ;
    res:citingWork res:W15 .

res:C-W16-W03 a res:Citation ;
    rdfs:label "W16 cites W03" ;
    res:citedWork res:W03 ;
    res:citingWork res:W16 .

res:C-W17-W03 a res:Citation ;
    rdfs:label "W17 cites W03" ;
    res:citedWork res:W03 ;
    res:citingWork res:W17 .

res:C-W18-W02 a res:Citation ;
    rdfs:label "W18 cites W02" ;
    res:citedWork res:W02 ;
    res:citingWork res:W18 .

res:C-W32-W20 a res:Citation ;
    rdfs:label "W32 cites W20" ;
    res:citedWork res:W20 ;
    res:citingWork res:W32 .

res:C-W33-W21 a res:Citation ;
    rdfs:label "W33 cites W21" ;
    res:citedWork res:W21 ;
    res:citingWork res:W33 .

res:C-W34-W22 a res:Citation ;
    rdfs:label "W34 cites W22" ;
    res:citedWork res:W22 ;
    res:citingWork res:W34 .

res:C-W35-W20 a res:Citation ;
    rdfs:label "W35 cites W20" ;
    res:citedWork res:W20 ;
    res:citingWork res:W35 .

res:C-W36-W20 a res:Citation ;
    rdfs:label "W36 cites W20" ;
    res:citedWork res:W20 ;
    res:citingWork res:W36 .

res:C-W36-W21 a res:Citation ;
    rdfs:label "W36 cites W21" ;
    res:citedWork res:W21 ;
    res:citingWork res:W36 .

res:C-W39-W23 a res:Citation ;
    rdfs:label "W39 cites W23" ;
    res:citedWork res:W23 ;
    res:citingWork res:W39 .

res:C-W40-W01 a res:Citation ;
    rdfs:label "W40 cites W01" ;
    res:citedWork res:W01 ;
    res:citingWork res:W40 .

res:C-W41-W01 a res:Citation ;
    rdfs:label "W41 cites W01" ;
    res:citedWork res:W01 ;
    res:citingWork res:W41 .

res:C-W50-W40 a res:Citation ;
    rdfs:label "W50 cites W40" ;
    res:citedWork res:W40 ;
    res:citingWork res:W50 .

res:C-W51-W40 a res:Citation ;
    rdfs:label "W51 cites W40" ;
    res:citedWork res:W40 ;
    res:citingWork res:W51 .

res:C-W51-W41 a res:Citation ;
    rdfs:label "W51 cites W41" ;
    res:citedWork res:W41 ;
    res:citingWork res:W51 .

res:C-W52-W41 a res:Citation ;
    rdfs:label "W52 cites W41" ;
    res:citedWork res:W41 ;
    res:citingWork res:W52 .

res:C-W60-W30 a res:Citation ;
    rdfs:label "W60 cites W30" ;
    res:citedWork res:W30 ;
    res:citingWork res:W60 .

res:C-W61-W30 a res:Citation ;
    rdfs:label "W61 cites W30" ;
    res:citedWork res:W30 ;
    res:citingWork res:W61 .

res:C-W62-W30 a res:Citation ;
    rdfs:label "W62 cites W30" ;
    res:citedWork res:W30 ;
    res:citingWork res:W62 .

res:C-W62-W31 a res:Citation ;
    rdfs:label "W62 cites W31" ;
    res:citedWork res:W31 ;
    res:citingWork res:W62 .

res:C-W63-W30 a res:Citation ;
    rdfs:label "W63 cites W30" ;
    res:citedWork res:W30 ;
    res:citingWork res:W63 .

res:C-W64-W30 a res:Citation ;
    rdfs:label "W64 cites W30" ;
    res:citedWork res:W30 ;
    res:citingWork res:W64 .

res:C-W65-W31 a res:Citation ;
    rdfs:label "W65 cites W31" ;
    res:citedWork res:W31 ;
    res:citingWork res:W65 .

res:C-W66-W31 a res:Citation ;
    rdfs:label "W66 cites W31" ;
    res:citedWork res:W31 ;
    res:citingWork res:W66 .

res:C-W67-W42 a res:Citation ;
    rdfs:label "W67 cites W42" ;
    res:citedWork res:W42 ;
    res:citingWork res:W67 .

res:C-W90-W22 a res:Citation ;
    rdfs:label "W90 cites W22" ;
    res:citedWork res:W22 ;
    res:citingWork res:W90 .

res:C-W90-W41 a res:Citation ;
    rdfs:label "W90 cites W41" ;
    res:citedWork res:W41 ;
    res:citingWork res:W90 .

res:C-W91-W22 a res:Citation ;
    rdfs:label "W91 cites W22" ;
    res:citedWork res:W22 ;
    res:citingWork res:W91 .

res:C-W92-W22 a res:Citation ;
    rdfs:label "W92 cites W22" ;
    res:citedWork res:W22 ;
    res:citingWork res:W92 .

res:W09 a res:Work ;
    rdfs:label "Issue information" ;
    res:doi "10.55555/s01.2023.4542" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Issue information" ;
    res:workType res:wtype-PTX ;
    res:year "2023"^^xsd:gYear .

res:W10 a res:Work ;
    rdfs:label "Front matter" ;
    res:doi "10.55555/s02.2024.9718" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Front matter" ;
    res:workType res:wtype-PTX ;
    res:year "2024"^^xsd:gYear .

res:W76 a res:Work ;
    rdfs:label "Foreword to the Forum proceedings" ;
    res:doi "10.55555/s06.2025.4219" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S06 ;
    res:title "Foreword to the Forum proceedings" ;
    res:workType res:wtype-EDT ;
    res:year "2025"^^xsd:gYear .

res:A03 a res:Author ;
    rdfs:label "Ellison, Mara J." ;
    res:name "Ellison, Mara J." ;
    res:orcid "0000-0002-9841-6229" .

res:A22 a res:Author ;
    rdfs:label "Niamh Corrigan" ;
    res:name "Niamh Corrigan" ;
    res:orcid "0000-0009-9065-9397" .

res:A33 a res:Author ;
    rdfs:label "Daichi Pruitt" ;
    res:name "Daichi Pruitt" ;
    res:orcid "0000-0009-1102-8594" .

res:W04 a res:Work ;
    rdfs:label "Editorial: a new decade of marine autonomy" ;
    res:doi "10.55555/s01.2023.1032" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Editorial: a new decade of marine autonomy" ;
    res:workType res:wtype-EDT ;
    res:year "2023"^^xsd:gYear .

res:W07 a res:Work ;
    rdfs:label "Low-cost sonar arrays for coastal monitoring" ;
    res:doi "10.55555/s04.2020.7029" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S04 ;
    res:title "Low-cost sonar arrays for coastal monitoring" ;
    res:workType res:wtype-ART ;
    res:year "2020"^^xsd:gYear .

res:W08 a res:Work ;
    rdfs:label "Turbulent wake modelling behind tidal turbines" ;
    res:doi "10.55555/s01.2025.5958" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Turbulent wake modelling behind tidal turbines" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W117 a res:Work ;
    rdfs:label "Uncertainty in beach profiles estimates" ;
    res:doi "10.55555/s08.2024.4202" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Uncertainty in beach profiles estimates" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W122 a res:Work ;
    rdfs:label "Observations of storm surge" ;
    res:doi "10.55555/s08.2025.1686" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Observations of storm surge" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W19 a res:Work ;
    rdfs:label "Glider-borne turbidity sensing" ;
    res:doi "10.55555/s02.2025.2198" ;
    res:recordSource res:origin-CRIS ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Glider-borne turbidity sensing" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W24 a res:Work ;
    rdfs:label "Vortex shedding in shallow channels" ;
    res:doi "10.55555/s06.2025.6698" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S06 ;
    res:title "Vortex shedding in shallow channels" ;
    res:workType res:wtype-SUP ;
    res:year "2025"^^xsd:gYear .

res:W37 a res:Work ;
    rdfs:label "Port traffic and seabed disturbance" ;
    res:doi "10.55555/s03.2022.9107" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Port traffic and seabed disturbance" ;
    res:workType res:wtype-ART ;
    res:year "2022"^^xsd:gYear .

res:W38 a res:Work ;
    rdfs:label "Seagrass mapping from aerial imagery" ;
    res:doi "10.55555/s02.2023.6112" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Seagrass mapping from aerial imagery" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W73 a res:Work ;
    rdfs:label "Saltmarsh retreat on the Halloran shore" ;
    res:doi "10.55555/s02.2022.7603" ;
    res:recordSource res:origin-CRIS ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Saltmarsh retreat on the Halloran shore" ;
    res:workType res:wtype-ART ;
    res:year "2022"^^xsd:gYear .

res:W74 a res:Work ;
    rdfs:label "Coastal squeeze and managed realignment: a review" ;
    res:doi "10.55555/s01.2023.6139" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Coastal squeeze and managed realignment: a review" ;
    res:workType res:wtype-REV ;
    res:year "2023"^^xsd:gYear .

res:W75 a res:Work ;
    rdfs:label "Rip currents at tourist beaches" ;
    res:doi "10.55555/s04.2023.3895" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S04 ;
    res:title "Rip currents at tourist beaches" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:A04 a res:Author ;
    rdfs:label "M. Ellison" ;
    res:name "M. Ellison" ;
    res:orcid "0000-0004-8662-8360" .

res:A05 a res:Author ;
    rdfs:label "Jonas Brandt" ;
    res:name "Jonas Brandt" ;
    res:orcid "0000-0001-6105-5008" .

res:A10 a res:Author ;
    rdfs:label "Dirk Hallmann" ;
    res:name "Dirk Hallmann" ;
    res:orcid "0000-0003-8222-6468" .

res:A12 a res:Author ;
    rdfs:label "Pieter Maas" ;
    res:name "Pieter Maas" ;
    res:orcid "0000-0007-6472-5877" .

res:A18 a res:Author ;
    rdfs:label "Bram Kuipers" ;
    res:name "Bram Kuipers" ;
    res:orcid "0000-0001-6210-5218" .

res:A19 a res:Author ;
    rdfs:label "Femke Hoogeveen" ;
    res:name "Femke Hoogeveen" ;
    res:orcid "0000-0005-4914-5244" .

res:A20 a res:Author ;
    rdfs:label "Joost Verhaar" ;
    res:name "Joost Verhaar" ;
    res:orcid "0000-0001-0646-0013" .

res:A30 a res:Author ;
    rdfs:label "Ana Aranda" ;
    res:name "Ana Aranda" ;
    res:orcid "0000-0006-1584-6450" .

res:A31 a res:Author ;
    rdfs:label "Ben Fujimura" ;
    res:name "Ben Fujimura" ;
    res:orcid "0000-0006-0454-1465" .

res:A40 a res:Author ;
    rdfs:label "Kai Carver" ;
    res:name "Kai Carver" ;
    res:orcid "0000-0003-5577-8794" .

res:A41 a res:Author ;
    rdfs:label "Lucia Hartwell" ;
    res:name "Lucia Hartwell" ;
    res:orcid "0000-0003-2627-0586" .

res:I01 a res:Institution ;
    rdfs:label "Albury University System" ;
    res:country "GB" ;
    res:institutionType res:itype-SYS ;
    res:name "Albury University System" ;
    res:ror "0hygr4985" .

res:I08 a res:Institution ;
    rdfs:label "Kesting Institute of Hydrodynamics" ;
    res:country "DE" ;
    res:institutionType res:itype-LAB ;
    res:name "Kesting Institute of Hydrodynamics" ;
    res:parent res:I07 ;
    res:ror "0brjdg570" .

res:I10 a res:Institution ;
    rdfs:label "Marrow Instruments BV" ;
    res:country "NL" ;
    res:institutionType res:itype-CO ;
    res:name "Marrow Instruments BV" ;
    res:ror "0t3x83535" .

res:S04 a res:Source ;
    rdfs:label "Global Marine Science Reports" ;
    res:issn "8864-5325" ;
    res:name "Global Marine Science Reports" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K0 .

res:W05 a res:Work ;
    rdfs:label "Erratum: Drift-aware mapping with low-cost sonar" ;
    res:doi "10.55555/s02.2024.7136" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Erratum: Drift-aware mapping with low-cost sonar" ;
    res:workType res:wtype-ERR ;
    res:year "2024"^^xsd:gYear .

res:W06 a res:Work ;
    rdfs:label "Shoreline change detection from glider transects" ;
    res:doi "10.55555/s03.2024.2042" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Shoreline change detection from glider transects" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W115 a res:Work ;
    rdfs:label "Remote sensing of internal waves: a review" ;
    res:doi "10.55555/s08.2025.4950" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Remote sensing of internal waves: a review" ;
    res:workType res:wtype-REV ;
    res:year "2025"^^xsd:gYear .

res:W13 a res:Work ;
    rdfs:label "Fleet coordination for survey gliders" ;
    res:doi "10.55555/s01.2024.5065" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Fleet coordination for survey gliders" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W14 a res:Work ;
    rdfs:label "Harbour mapping with autonomous surface vessels" ;
    res:doi "10.55555/s03.2025.3072" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Harbour mapping with autonomous surface vessels" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W16 a res:Work ;
    rdfs:label "Sonar-based wake detection" ;
    res:doi "10.55555/s02.2025.6345" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Sonar-based wake detection" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W17 a res:Work ;
    rdfs:label "Acoustic positioning near the shore" ;
    res:doi "10.55555/s06.2024.8939" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S06 ;
    res:title "Acoustic positioning near the shore" ;
    res:workType res:wtype-SUP ;
    res:year "2024"^^xsd:gYear .

res:W18 a res:Work ;
    rdfs:label "Comparing sonar odometry methods" ;
    res:doi "10.55555/s05.2022.2759" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S05 ;
    res:title "Comparing sonar odometry methods" ;
    res:workType res:wtype-PPR ;
    res:year "2022"^^xsd:gYear .

res:W23 a res:Work ;
    rdfs:label "Anomalous dissipation in estuarine plumes" ;
    res:doi "10.55555/s02.2023.2925" ;
    res:recordSource res:origin-FEED ;
    res:retracted true ;
    res:source res:S02 ;
    res:title "Anomalous dissipation in estuarine plumes" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W33 a res:Work ;
    rdfs:label "Mixing efficiency in stratified tidal flows" ;
    res:doi "10.55555/s02.2025.6654" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Mixing efficiency in stratified tidal flows" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W34 a res:Work ;
    rdfs:label "Evaluating turbulence closures against flume data" ;
    res:doi "10.55555/s03.2025.2352" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Evaluating turbulence closures against flume data" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W35 a res:Work ;
    rdfs:label "Sediment resuspension by storms: a review" ;
    res:doi "10.55555/s02.2025.2131" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Sediment resuspension by storms: a review" ;
    res:workType res:wtype-REV ;
    res:year "2025"^^xsd:gYear .

res:W39 a res:Work ;
    rdfs:label "Replicating dissipation estimates in plumes" ;
    res:doi "10.55555/s03.2024.5346" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Replicating dissipation estimates in plumes" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W42 a res:Work ;
    rdfs:label "Machine-learned tidal forecasts" ;
    res:doi "10.55555/s05.2023.6876" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S05 ;
    res:title "Machine-learned tidal forecasts" ;
    res:versionOf res:W31 ;
    res:workType res:wtype-PPR ;
    res:year "2023"^^xsd:gYear .

res:W50 a res:Work ;
    rdfs:label "Battery ageing in autonomous platforms" ;
    res:doi "10.55555/s03.2024.6324" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Battery ageing in autonomous platforms" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W52 a res:Work ;
    rdfs:label "Route optimisation for ocean drones" ;
    res:doi "10.55555/s01.2025.9294" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Route optimisation for ocean drones" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W70 a res:Work ;
    rdfs:label "Optical backscatter in turbid estuaries" ;
    res:doi "10.55555/s02.2023.6434" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Optical backscatter in turbid estuaries" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W71 a res:Work ;
    rdfs:label "Low-power optical sensors for gliders" ;
    res:doi "10.55555/s01.2024.6287" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Low-power optical sensors for gliders" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W72 a res:Work ;
    rdfs:label "Integrating optical sensors on survey gliders" ;
    res:doi "10.55555/s03.2024.9080" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Integrating optical sensors on survey gliders" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W91 a res:Work ;
    rdfs:label "Closure models for wave boundary layers" ;
    res:doi "10.55555/s01.2025.4607" ;
    res:recordSource res:origin-STG ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Closure models for wave boundary layers" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W92 a res:Work ;
    rdfs:label "Coastal turbulence: a review" ;
    res:doi "10.55555/s03.2025.6710" ;
    res:recordSource res:origin-STG ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Coastal turbulence: a review" ;
    res:workType res:wtype-REV ;
    res:year "2025"^^xsd:gYear .

res:A02 a res:Author ;
    rdfs:label "M. Ellison" ;
    res:name "M. Ellison" ;
    res:orcid "0000-0002-9841-6229" .

res:A06 a res:Author ;
    rdfs:label "Jonas Brandt" ;
    res:name "Jonas Brandt" ;
    res:orcid "0000-0007-5475-1779" .

res:A16 a res:Author ;
    rdfs:label "Rhys Calloway" ;
    res:name "Rhys Calloway" .

res:A21 a res:Author ;
    rdfs:label "Petra Lindqvist" ;
    res:name "Petra Lindqvist" ;
    res:orcid "0000-0000-4118-9557" .

res:I04 a res:Institution ;
    rdfs:label "Tessel Laboratory for Ocean Sensing" ;
    res:country "GB" ;
    res:institutionType res:itype-LAB ;
    res:name "Tessel Laboratory for Ocean Sensing" ;
    res:parent res:I03 ;
    res:ror "0002ezf81" .

res:S05 a res:Source ;
    rdfs:label "OceanArXiv" ;
    res:name "OceanArXiv" ;
    res:sourceType res:stype-REP .

res:S06 a res:Source ;
    rdfs:label "Proceedings of the Hydrodynamics Forum" ;
    res:issn "9804-2748" ;
    res:name "Proceedings of the Hydrodynamics Forum" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K2 .

res:W102 a res:Work ;
    rdfs:label "Long-term trends in dune erosion" ;
    res:doi "10.55555/s07.2023.1186" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Long-term trends in dune erosion" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W110 a res:Work ;
    rdfs:label "Editorial: beach profiles" ;
    res:doi "10.55555/s07.2021.3358" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Editorial: beach profiles" ;
    res:workType res:wtype-EDT ;
    res:year "2021"^^xsd:gYear .

res:W116 a res:Work ;
    rdfs:label "A model of coastal upwelling" ;
    res:doi "10.55555/s08.2022.6950" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "A model of coastal upwelling" ;
    res:workType res:wtype-ART ;
    res:year "2022"^^xsd:gYear .

res:W118 a res:Work ;
    rdfs:label "Long-term trends in internal waves" ;
    res:doi "10.55555/s07.2025.4335" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Long-term trends in internal waves" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W12 a res:Work ;
    rdfs:label "Sonar mosaics from glider fleets" ;
    res:doi "10.55555/s02.2024.3526" ;
    res:recordSource res:origin-CRIS ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Sonar mosaics from glider fleets" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W120 a res:Work ;
    rdfs:label "Remote sensing of tidal asymmetry: a review" ;
    res:doi "10.55555/s07.2021.6881" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Remote sensing of tidal asymmetry: a review" ;
    res:workType res:wtype-REV ;
    res:year "2021"^^xsd:gYear .

res:W15 a res:Work ;
    rdfs:label "Low-cost sonar: a review" ;
    res:doi "10.55555/s02.2025.2741" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Low-cost sonar: a review" ;
    res:workType res:wtype-REV ;
    res:year "2025"^^xsd:gYear .

res:W36 a res:Work ;
    rdfs:label "Shear and mixing in a macrotidal estuary" ;
    res:doi "10.55555/s03.2025.2439" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Shear and mixing in a macrotidal estuary" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W51 a res:Work ;
    rdfs:label "Benchmarks for marine path planners" ;
    res:doi "10.55555/s02.2024.8087" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Benchmarks for marine path planners" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W64 a res:Work ;
    rdfs:label "Remote sensing of internal waves" ;
    res:doi "10.55555/s08.2025.7711" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Remote sensing of internal waves" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W66 a res:Work ;
    rdfs:label "Remote sensing of wave runup" ;
    res:doi "10.55555/s07.2025.5131" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Remote sensing of wave runup" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W67 a res:Work ;
    rdfs:label "Seasonal variability in tidal asymmetry" ;
    res:doi "10.55555/s08.2023.1192" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Seasonal variability in tidal asymmetry" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W90 a res:Work ;
    rdfs:label "Sediment transport in tidal inlets" ;
    res:doi "10.55555/s02.2025.8585" ;
    res:recordSource res:origin-STG ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Sediment transport in tidal inlets" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:A09 a res:Author ;
    rdfs:label "Lena Vossberg" ;
    res:name "Lena Vossberg" ;
    res:orcid "0000-0000-8073-7028" .

res:A11 a res:Author ;
    rdfs:label "Sofie de Raat" ;
    res:name "Sofie de Raat" ;
    res:orcid "0000-0006-1642-5247" .

res:A14 a res:Author ;
    rdfs:label "Hugo Marchetti" ;
    res:name "Hugo Marchetti" ;
    res:orcid "0000-0007-5682-0525" .

res:A32 a res:Author ;
    rdfs:label "Chiara Kincaid" ;
    res:name "Chiara Kincaid" ;
    res:orcid "0000-0009-0853-8012" .

res:A37 a res:Author ;
    rdfs:label "Haruto Dorsey" ;
    res:name "Haruto Dorsey" ;
    res:orcid "0000-0004-5291-2808" .

res:A43 a res:Author ;
    rdfs:label "Noor Beaulieu" ;
    res:name "Noor Beaulieu" ;
    res:orcid "0000-0000-8394-9066" .

res:A44 a res:Author ;
    rdfs:label "Oscar Galvez" ;
    res:name "Oscar Galvez" ;
    res:orcid "0000-0008-8281-1265" .

res:I06 a res:Institution ;
    rdfs:label "Halloran Institute for Coastal Studies" ;
    res:country "GB" ;
    res:institutionType res:itype-AFF ;
    res:name "Halloran Institute for Coastal Studies" ;
    res:parent res:I02 ;
    res:ror "0175f3924" .

res:W01 a res:Work ;
    rdfs:label "Adaptive path planning for underwater gliders" ;
    res:doi "10.55555/s01.2021.1465" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Adaptive path planning for underwater gliders" ;
    res:workType res:wtype-ART ;
    res:year "2021"^^xsd:gYear .

res:W02 a res:Work ;
    rdfs:label "Drift-aware mapping with low-cost sonar" ;
    res:doi "10.55555/s05.2022.2911" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S05 ;
    res:title "Drift-aware mapping with low-cost sonar" ;
    res:versionOf res:W03 ;
    res:workType res:wtype-PPR ;
    res:year "2022"^^xsd:gYear .

res:W105 a res:Work ;
    rdfs:label "Seasonal variability in harbour seiches" ;
    res:doi "10.55555/s08.2021.9028" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Seasonal variability in harbour seiches" ;
    res:workType res:wtype-ART ;
    res:year "2021"^^xsd:gYear .

res:W111 a res:Work ;
    rdfs:label "Observations of storm surge" ;
    res:doi "10.55555/s08.2025.5383" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Observations of storm surge" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W112 a res:Work ;
    rdfs:label "Observations of tidal asymmetry" ;
    res:doi "10.55555/s07.2020.9946" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Observations of tidal asymmetry" ;
    res:workType res:wtype-ART ;
    res:year "2020"^^xsd:gYear .

res:W113 a res:Work ;
    rdfs:label "Seasonal variability in coastal upwelling" ;
    res:doi "10.55555/s07.2021.6316" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Seasonal variability in coastal upwelling" ;
    res:workType res:wtype-ART ;
    res:year "2021"^^xsd:gYear .

res:W119 a res:Work ;
    rdfs:label "A model of internal waves" ;
    res:doi "10.55555/s08.2019.1156" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "A model of internal waves" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:W121 a res:Work ;
    rdfs:label "Long-term trends in internal waves" ;
    res:doi "10.55555/s08.2024.8676" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Long-term trends in internal waves" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W124 a res:Work ;
    rdfs:label "A model of coastal upwelling" ;
    res:doi "10.55555/s08.2019.2165" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "A model of coastal upwelling" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:W27 a res:Work ;
    rdfs:label "Sensor fusion for moored buoys" ;
    res:doi "10.55555/s03.2024.8772" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Sensor fusion for moored buoys" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W28 a res:Work ;
    rdfs:label "Calibration drift in conductivity sensors" ;
    res:doi "10.55555/s02.2024.9171" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Calibration drift in conductivity sensors" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W29 a res:Work ;
    rdfs:label "Open hardware for ocean observation: a review" ;
    res:doi "10.55555/s01.2024.2981" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Open hardware for ocean observation: a review" ;
    res:workType res:wtype-REV ;
    res:year "2024"^^xsd:gYear .

res:W40 a res:Work ;
    rdfs:label "Energy budgets for long-range gliders" ;
    res:doi "10.55555/s02.2022.4703" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Energy budgets for long-range gliders" ;
    res:workType res:wtype-ART ;
    res:year "2022"^^xsd:gYear .

res:W62 a res:Work ;
    rdfs:label "Seasonal variability in dune erosion" ;
    res:doi "10.55555/s08.2023.5393" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Seasonal variability in dune erosion" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W63 a res:Work ;
    rdfs:label "Seasonal variability in sediment flux" ;
    res:doi "10.55555/s07.2024.8504" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Seasonal variability in sediment flux" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W65 a res:Work ;
    rdfs:label "Observations of dune erosion" ;
    res:doi "10.55555/s08.2024.6414" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Observations of dune erosion" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:A01 a res:Author ;
    rdfs:label "Mara Ellison" ;
    res:name "Mara Ellison" ;
    res:orcid "0000-0002-9841-6229" .

res:A17 a res:Author ;
    rdfs:label "Ingrid Solberg" ;
    res:name "Ingrid Solberg" ;
    res:orcid "0000-0003-9494-8214" .

res:A42 a res:Author ;
    rdfs:label "Mateo Morrow" ;
    res:name "Mateo Morrow" ;
    res:orcid "0000-0000-2145-8421" .

res:I05 a res:Institution ;
    rdfs:label "Albury Metropolitan University" ;
    res:country "GB" ;
    res:institutionType res:itype-UNI ;
    res:name "Albury Metropolitan University" ;
    res:parent res:I01 ;
    res:ror "0ww7kxb57" .

res:I14 a res:Institution ;
    rdfs:label "Oskel Polytechnic" ;
    res:country "NL" ;
    res:institutionType res:itype-UNI ;
    res:name "Oskel Polytechnic" ;
    res:ror "06t6n5818" .

res:W103 a res:Work ;
    rdfs:label "A model of harbour seiches" ;
    res:doi "10.55555/s07.2020.2380" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "A model of harbour seiches" ;
    res:workType res:wtype-ART ;
    res:year "2020"^^xsd:gYear .

res:W106 a res:Work ;
    rdfs:label "Seasonal variability in harbour seiches: a review" ;
    res:doi "10.55555/s07.2022.7552" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Seasonal variability in harbour seiches: a review" ;
    res:workType res:wtype-REV ;
    res:year "2022"^^xsd:gYear .

res:W123 a res:Work ;
    rdfs:label "Editorial: river plumes" ;
    res:doi "10.55555/s08.2023.3508" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Editorial: river plumes" ;
    res:workType res:wtype-EDT ;
    res:year "2023"^^xsd:gYear .

res:W125 a res:Work ;
    rdfs:label "Remote sensing of sediment flux" ;
    res:doi "10.55555/s08.2024.4906" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Remote sensing of sediment flux" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W20 a res:Work ;
    rdfs:label "Bed shear stress under breaking waves" ;
    res:doi "10.55555/s01.2024.7245" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Bed shear stress under breaking waves" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W22 a res:Work ;
    rdfs:label "Turbulence closures for coastal models: a review" ;
    res:doi "10.55555/s03.2024.5939" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Turbulence closures for coastal models: a review" ;
    res:workType res:wtype-REV ;
    res:year "2024"^^xsd:gYear .

res:W31 a res:Work ;
    rdfs:label "Machine-learned tidal forecasts" ;
    res:doi "10.55555/s01.2023.5047" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Machine-learned tidal forecasts" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W32 a res:Work ;
    rdfs:label "Wave-current interaction over sandbars" ;
    res:doi "10.55555/s01.2025.8470" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S01 ;
    res:title "Wave-current interaction over sandbars" ;
    res:workType res:wtype-ART ;
    res:year "2025"^^xsd:gYear .

res:W41 a res:Work ;
    rdfs:label "Path planning under uncertain currents" ;
    res:doi "10.55555/s03.2023.3758" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Path planning under uncertain currents" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W61 a res:Work ;
    rdfs:label "Uncertainty in marsh accretion estimates" ;
    res:doi "10.55555/s07.2022.2930" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Uncertainty in marsh accretion estimates" ;
    res:workType res:wtype-ART ;
    res:year "2022"^^xsd:gYear .

res:A07 a res:Author ;
    rdfs:label "Priya Ramanathan" ;
    res:name "Priya Ramanathan" ;
    res:orcid "0000-0009-2298-3695" .

res:A08 a res:Author ;
    rdfs:label "Tomasz Wierzba" ;
    res:name "Tomasz Wierzba" ;
    res:orcid "0000-0007-9318-6032" .

res:A13 a res:Author ;
    rdfs:label "Claire Fontanet" ;
    res:name "Claire Fontanet" ;
    res:orcid "0000-0001-8841-3301" .

res:A15 a res:Author ;
    rdfs:label "Aisha Okonjo" ;
    res:name "Aisha Okonjo" ;
    res:orcid "0000-0008-9831-9489" .

res:A36 a res:Author ;
    rdfs:label "Grace Olmedo" ;
    res:name "Grace Olmedo" ;
    res:orcid "0000-0004-2300-4876" .

res:A45 a res:Author ;
    rdfs:label "Paula Lefebvre" ;
    res:name "Paula Lefebvre" ;
    res:orcid "0000-0008-4409-3244" .

res:I11 a res:Institution ;
    rdfs:label "Brevin Ocean Agency" ;
    res:country "FR" ;
    res:institutionType res:itype-GOV ;
    res:name "Brevin Ocean Agency" ;
    res:ror "0wvack776" .

res:I13 a res:Institution ;
    rdfs:label "Dunmore College" ;
    res:country "GB" ;
    res:institutionType res:itype-UNI ;
    res:name "Dunmore College" ;
    res:ror "095cwy722" .

res:W107 a res:Work ;
    rdfs:label "Observations of marsh accretion: a review" ;
    res:doi "10.55555/s08.2019.9349" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Observations of marsh accretion: a review" ;
    res:workType res:wtype-REV ;
    res:year "2019"^^xsd:gYear .

res:W109 a res:Work ;
    rdfs:label "A model of river plumes" ;
    res:doi "10.55555/s07.2019.5434" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "A model of river plumes" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:W21 a res:Work ;
    rdfs:label "A field campaign on tidal mixing" ;
    res:doi "10.55555/s02.2024.5301" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "A field campaign on tidal mixing" ;
    res:workType res:wtype-ART ;
    res:year "2024"^^xsd:gYear .

res:W30 a res:Work ;
    rdfs:label "Tidal stream resource maps for the Dunmore coast" ;
    res:doi "10.55555/s03.2019.9502" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S03 ;
    res:title "Tidal stream resource maps for the Dunmore coast" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:A34 a res:Author ;
    rdfs:label "Elif Esposito" ;
    res:name "Elif Esposito" ;
    res:orcid "0000-0000-6925-6663" .

res:A38 a res:Author ;
    rdfs:label "Ines Ishida" ;
    res:name "Ines Ishida" ;
    res:orcid "0000-0004-5850-0370" .

res:I03 a res:Institution ;
    rdfs:label "Albury Centre for Marine Robotics" ;
    res:country "GB" ;
    res:institutionType res:itype-LAB ;
    res:name "Albury Centre for Marine Robotics" ;
    res:parent res:I02 ;
    res:ror "06a9yq342" .

res:I12 a res:Institution ;
    rdfs:label "Université de Lorvain" ;
    res:country "FR" ;
    res:institutionType res:itype-UNI ;
    res:name "Université de Lorvain" ;
    res:ror "091pt9775" .

res:W114 a res:Work ;
    rdfs:label "Observations of estuarine salinity" ;
    res:doi "10.55555/s08.2019.1460" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Observations of estuarine salinity" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:W60 a res:Work ;
    rdfs:label "Remote sensing of dune erosion" ;
    res:doi "10.55555/s08.2020.8236" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Remote sensing of dune erosion" ;
    res:workType res:wtype-ART ;
    res:year "2020"^^xsd:gYear .

res:A35 a res:Author ;
    rdfs:label "Felipe Jaramillo" ;
    res:name "Felipe Jaramillo" ;
    res:orcid "0000-0006-3228-0886" .

res:W108 a res:Work ;
    rdfs:label "Seasonal variability in tidal asymmetry" ;
    res:doi "10.55555/s07.2021.9650" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Seasonal variability in tidal asymmetry" ;
    res:workType res:wtype-ART ;
    res:year "2021"^^xsd:gYear .

res:W03 a res:Work ;
    rdfs:label "Drift-aware mapping with low-cost sonar" ;
    res:doi "10.55555/s02.2023.9437" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S02 ;
    res:title "Drift-aware mapping with low-cost sonar" ;
    res:workType res:wtype-ART ;
    res:year "2023"^^xsd:gYear .

res:W101 a res:Work ;
    rdfs:label "Long-term trends in estuarine salinity" ;
    res:doi "10.55555/s08.2019.4427" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S08 ;
    res:title "Long-term trends in estuarine salinity" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:I07 a res:Institution ;
    rdfs:label "Kesting University" ;
    res:country "DE" ;
    res:institutionType res:itype-UNI ;
    res:name "Kesting University" ;
    res:ror "0593t4875" .

res:I09 a res:Institution ;
    rdfs:label "Rostval Technical University" ;
    res:country "NL" ;
    res:institutionType res:itype-UNI ;
    res:name "Rostval Technical University" ;
    res:ror "0k8rh7879" .

res:I02 a res:Institution ;
    rdfs:label "University of Albury" ;
    res:country "GB" ;
    res:institutionType res:itype-UNI ;
    res:name "University of Albury" ;
    res:parent res:I01 ;
    res:ror "06safhw22" .

res:W104 a res:Work ;
    rdfs:label "Remote sensing of wave runup" ;
    res:doi "10.55555/s07.2019.6591" ;
    res:recordSource res:origin-FEED ;
    res:retracted false ;
    res:source res:S07 ;
    res:title "Remote sensing of wave runup" ;
    res:workType res:wtype-ART ;
    res:year "2019"^^xsd:gYear .

res:I18 a res:Institution ;
    rdfs:label "Universidad de Ventolera" ;
    res:country "ES" ;
    res:institutionType res:itype-UNI ;
    res:name "Universidad de Ventolera" ;
    res:ror "0ay9jr885" .

res:S01 a res:Source ;
    rdfs:label "Journal of Marine Autonomy" ;
    res:issn "9866-3925" ;
    res:name "Journal of Marine Autonomy" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K3 .

res:S03 a res:Source ;
    rdfs:label "Coastal Engineering Review" ;
    res:issn "1154-9679" ;
    res:name "Coastal Engineering Review" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K1 .

res:I16 a res:Institution ;
    rdfs:label "Hoshimine Institute of Technology" ;
    res:country "JP" ;
    res:institutionType res:itype-UNI ;
    res:name "Hoshimine Institute of Technology" ;
    res:ror "06afa6f88" .

res:S07 a res:Source ;
    rdfs:label "Journal of Estuarine Dynamics" ;
    res:issn "1483-2835" ;
    res:name "Journal of Estuarine Dynamics" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K2 .

res:I17 a res:Institution ;
    rdfs:label "Université de Mallois" ;
    res:country "CA" ;
    res:institutionType res:itype-UNI ;
    res:name "Université de Mallois" ;
    res:ror "0pshcv029" .

res:S02 a res:Source ;
    rdfs:label "Ocean Sensing Letters" ;
    res:issn "3195-4973" ;
    res:name "Ocean Sensing Letters" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K2 .

res:S08 a res:Source ;
    rdfs:label "Hydrology Notes" ;
    res:issn "9832-2482" ;
    res:name "Hydrology Notes" ;
    res:sourceType res:stype-JOU ;
    res:tier res:tier-K1 .

res:I15 a res:Institution ;
    rdfs:label "Carrow State University" ;
    res:country "US" ;
    res:institutionType res:itype-UNI ;
    res:name "Carrow State University" ;
    res:ror "0v91gp428" .
```

### ontology.ttl (the vocabulary the data uses)
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
