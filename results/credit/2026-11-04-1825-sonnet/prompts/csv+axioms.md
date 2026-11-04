<!-- system: You answer questions about a credit-ratings dataset. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

### entities.csv
```csv
entity_id,name,lei,country,entity_type,parent_id,source_system
E01,Kestrel Energy plc,7245002OOPBG04092E43,GB,CORP,,RATINGS
E02,Northwind Holdings plc,213800PHEIYNJMHTDV74,GB,CORP,,RATINGS
E03,NORTHWIND HLDGS,213800PHEIYNJMHTDV74,GB,CORP,,RESEARCH
E04,Northwind Finance BV,213800LA5RYJLGXV2T85,NL,FINSUB,E02,RATINGS
E05,Valdoria Telecom SA,391200LESH03LMOY2U61,VD,CORP,,RATINGS
E06,Orrin Bank AG,549300AMVE3VRVG7HK43,DE,BANK,,RATINGS
E07,Pellam Retail Ltd,969500B6IUACELPI2291,GB,CORP,,RATINGS
E08,Saxby Shipping SA,969500KOTZ1JFIZSG796,GR,CORP,,RATINGS
VD,Republic of Valdoria,,VD,SOV,,RATINGS
E09,Halden Group plc,815600ASM9EHDG931T89,GB,CORP,,RATINGS
E10,Halden Bank AG,391200QYPVFF2O9K2039,DE,BANK,E09,RATINGS
E11,Halden Leasing SA,549300XBZH4ULO9MQV55,FR,FINSUB,E10,RATINGS
E12,Halden Foods Ltd,213800IJDL4OJ4DG5T19,GB,CORP,,RATINGS
E13,Orrin Bancorp Inc,815600O8X8K2F154N214,US,BANK,,RATINGS
E14,Marlow Utilities plc,3912005AH2C1I9YF8106,GB,CORP,,RATINGS
CV,Republic of Corvenia,,CV,SOV,,RATINGS
E15,Corvenia Power SA,213800PBQVHVBBH6GV02,CV,CORP,,RATINGS
E16,Brindle Capital Ltd,5493003Z3PXXR7KNFM81,GB,CORP,,QA
E17,HALDEN BANK,391200QYPVFF2O9K2039,LU,BANK,,RESEARCH
```

### instruments.csv
```csv
instrument_id,description,issuer_id,guarantor_id,seniority,currency,maturity
I01,Kestrel Energy 4.50% notes due 2030,E01,,SU,GBP,2030-03-15
I02,Kestrel Energy 6.25% notes due 2031,E01,,SUB,GBP,2031-09-30
I03,Northwind Finance 3.75% notes due 2030,E04,E02,SU,EUR,2030-05-01
I04,Valdoria Telecom 5.00% notes due 2029,E05,,SU,USD,2029-11-20
I05,Halden Leasing 2.90% notes due 2028,E11,E10,SU,EUR,2028-06-30
I06,Corvenia Power 7.10% notes due 2032,E15,,SUB,USD,2032-02-15
I07,Valdoria Telecom 4.25% notes due 2027,E05,,SU,XVD,2027-08-31
I08,Corvenia Power 6.00% notes due 2034,E15,,SU,USD,2034-09-01
```

### rating_actions.csv
```csv
action_id,date,rated_id,rating_type,ccy_basis,action,rating,outlook,watch,comment
A01,2024-03-12,E01,LTIDR,FC,AS,A-,STA,,
A02,2025-06-20,E01,LTIDR,FC,DG,BBB,STA,,weaker cash flow after asset sale
A03,2026-02-10,E01,LTIDR,FC,AF,BBB,NEG,,
A04,2026-02-10,E01,STIDR,FC,AF,F2,,,
A05,2024-03-12,I01,INST,,AS,A-,,,
A06,2025-06-20,I01,INST,,DG,BBB,,,
A07,2025-06-20,I02,INST,,DG,BB+,,,
A08,2023-11-01,E02,LTIDR,FC,AS,A,STA,,
A09,2025-09-15,E03,LTIDR,FC,AF,A,POS,,
A10,2023-11-01,I03,INST,,AS,A,,,
A11,2025-09-15,I03,INST,,AF,A,,,
A12,2025-04-01,VD,CC,,AS,BB,,,
A13,2025-04-01,E05,LTIDR,LC,AS,BBB-,STA,,
A14,2025-04-01,E05,LTIDR,FC,AS,BB,STA,,
A15,2025-04-01,I04,INST,,AS,BB,,,
A16,2024-05-01,E06,LTIDR,FC,AS,A-,STA,,
A17,2026-09-03,E06,LTIDR,FC,RW,A-,,RWN,
A18,2024-01-10,E07,LTIDR,FC,AS,BB,STA,,
A19,2026-05-12,E07,LTIDR,FC,WD,WD,,,commercial reasons
A20,2024-06-01,E08,LTIDR,FC,AS,B,STA,,
A21,2026-01-20,E08,LTIDR,FC,DG,CCC,,,
A22,2026-07-08,E08,LTIDR,FC,DG,RD,,,distressed debt exchange completed
A23,2024-03-12,I02,INST,,AS,BBB,,,
A24,2023-05-01,E09,LTIDR,FC,AS,A,STA,,
A25,2026-03-01,E09,LTIDR,FC,AF,A,NEG,,
A26,2023-05-01,E10,LTIDR,FC,AS,A-,STA,,support from parent
A27,2026-04-15,E10,LTIDR,FC,DG,BBB+,STA,,
A28,2023-06-01,I05,INST,,AS,A-,,,
A29,2026-04-15,I05,INST,,DG,BBB+,,,
A30,2024-02-01,E12,LTIDR,FC,AS,BB-,STA,,
A31,2025-08-01,E12,LTIDR,FC,UG,BB,STA,,
A32,2024-07-01,E13,LTIDR,FC,AS,BBB,STA,,
A33,2026-05-01,E14,LTIDR,FC,AF,BBB+,STA,,
A34,2023-01-15,E14,LTIDR,FC,AS,A-,STA,,
A35,2025-11-20,E14,LTIDR,FC,RW,BBB+,,RWN,
A36,2024-09-30,E14,LTIDR,FC,DG,BBB+,STA,,
A37,2024-01-01,CV,CC,,AS,A,,,
A38,2024-01-01,CV,LTIDR,FC,AS,BBB+,STA,,
A39,2024-01-01,CV,LTIDR,LC,AS,A-,STA,,
A40,2024-03-01,E15,LTIDR,LC,AS,A+,STA,,
A41,2024-03-01,E15,LTIDR,FC,AS,A,STA,,
A42,2024-03-01,I06,INST,,AS,A-,,,
A43,2024-04-01,E16,LTIDR,FC,AS,BBB-,STA,,
A44,2026-06-01,E16,LTIDR,FC,DG,BB+,STA,,
A45,2025-04-01,I07,INST,,AS,BBB-,,,
A46,2025-02-01,E11,CO,,AS,BBB,,,
A47,2026-09-01,I08,INST,,EX,A,,,
```

### ontology.ttl, without its definitions (the vocabulary the data uses)
The codes in the CSV files are the skos:notation values of the concepts below.
```turtle
@prefix lad: <https://example.org/ladder/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

lad:Entity a owl:Class ;
    rdfs:label "Entity" .

lad:Instrument a owl:Class ;
    rdfs:label "Instrument" .

lad:RatingAction a owl:Class ;
    rdfs:label "Rating action" .

lad:action a owl:ObjectProperty ;
    rdfs:label "action" .

lad:action-AF a skos:Concept ;
    rdfs:label "Affirmed" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "AF" ;
    skos:prefLabel "Affirmed" .

lad:action-AS a skos:Concept ;
    rdfs:label "Assigned" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "AS" ;
    skos:prefLabel "Assigned" .

lad:action-DG a skos:Concept ;
    rdfs:label "Downgraded" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "DG" ;
    skos:prefLabel "Downgraded" .

lad:action-EX a skos:Concept ;
    rdfs:label "Expected" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "EX" ;
    skos:prefLabel "Expected rating" .

lad:action-RW a skos:Concept ;
    rdfs:label "Placed on Rating Watch" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "RW" ;
    skos:prefLabel "Placed on Rating Watch" .

lad:action-UG a skos:Concept ;
    rdfs:label "Upgraded" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "UG" ;
    skos:prefLabel "Upgraded" .

lad:action-WD a skos:Concept ;
    rdfs:label "Withdrawn" ;
    skos:inScheme lad:ActionTypes ;
    skos:notation "WD" ;
    skos:prefLabel "Withdrawn" .

lad:basis-FC a skos:Concept ;
    rdfs:label "Foreign currency" ;
    skos:inScheme lad:CurrencyBases ;
    skos:notation "FC" ;
    skos:prefLabel "Foreign currency" .

lad:basis-LC a skos:Concept ;
    rdfs:label "Local currency" ;
    skos:inScheme lad:CurrencyBases ;
    skos:notation "LC" ;
    skos:prefLabel "Local currency" .

lad:ccyBasis a owl:ObjectProperty ;
    rdfs:label "currency basis" .

lad:comment a owl:DatatypeProperty ;
    rdfs:label "comment" .

lad:country a owl:DatatypeProperty ;
    rdfs:label "country" .

lad:currency a owl:DatatypeProperty ;
    rdfs:label "currency" .

lad:date a owl:DatatypeProperty ;
    rdfs:label "date" .

lad:description a owl:DatatypeProperty ;
    rdfs:label "description" .

lad:entityType a owl:ObjectProperty ;
    rdfs:label "entity type" .

lad:etype-BANK a skos:Concept ;
    rdfs:label "Bank" ;
    skos:inScheme lad:EntityTypes ;
    skos:notation "BANK" ;
    skos:prefLabel "Bank" .

lad:etype-CORP a skos:Concept ;
    rdfs:label "Corporate" ;
    skos:inScheme lad:EntityTypes ;
    skos:notation "CORP" ;
    skos:prefLabel "Corporate" .

lad:etype-FINSUB a skos:Concept ;
    rdfs:label "Finance subsidiary" ;
    skos:inScheme lad:EntityTypes ;
    skos:notation "FINSUB" ;
    skos:prefLabel "Finance subsidiary" .

lad:etype-SOV a skos:Concept ;
    rdfs:label "Sovereign" ;
    skos:inScheme lad:EntityTypes ;
    skos:notation "SOV" ;
    skos:prefLabel "Sovereign" .

lad:guarantor a owl:ObjectProperty ;
    rdfs:label "guarantor" .

lad:issuer a owl:ObjectProperty ;
    rdfs:label "issuer" .

lad:lei a owl:DatatypeProperty ;
    rdfs:label "LEI" .

lad:maturity a owl:DatatypeProperty ;
    rdfs:label "maturity" .

lad:name a owl:DatatypeProperty ;
    rdfs:label "name" .

lad:ontology a owl:Ontology ;
    rdfs:label "Credit ratings: a teaching ontology" ;
    owl:versionInfo "0.1" .

lad:outlook a owl:ObjectProperty ;
    rdfs:label "outlook" .

lad:outlook-NEG a skos:Concept ;
    rdfs:label "Negative" ;
    skos:inScheme lad:Outlooks ;
    skos:notation "NEG" ;
    skos:prefLabel "Negative" .

lad:outlook-POS a skos:Concept ;
    rdfs:label "Positive" ;
    skos:inScheme lad:Outlooks ;
    skos:notation "POS" ;
    skos:prefLabel "Positive" .

lad:outlook-STA a skos:Concept ;
    rdfs:label "Stable" ;
    skos:inScheme lad:Outlooks ;
    skos:notation "STA" ;
    skos:prefLabel "Stable" .

lad:parent a owl:ObjectProperty ;
    rdfs:label "parent" .

lad:ratedThing a owl:ObjectProperty ;
    rdfs:label "rated thing" .

lad:rating a owl:DatatypeProperty ;
    rdfs:label "rating" .

lad:ratingType a owl:ObjectProperty ;
    rdfs:label "rating type" .

lad:seniority a owl:ObjectProperty ;
    rdfs:label "seniority" .

lad:seniority-SU a skos:Concept ;
    rdfs:label "Senior unsecured" ;
    skos:inScheme lad:Seniorities ;
    skos:notation "SU" ;
    skos:prefLabel "Senior unsecured" .

lad:seniority-SUB a skos:Concept ;
    rdfs:label "Subordinated" ;
    skos:inScheme lad:Seniorities ;
    skos:notation "SUB" ;
    skos:prefLabel "Subordinated" .

lad:sourceSystem a owl:DatatypeProperty ;
    rdfs:label "source system" .

lad:type-CC a skos:Concept ;
    rdfs:label "Country Ceiling" ;
    skos:inScheme lad:RatingTypes ;
    skos:notation "CC" ;
    skos:prefLabel "Country Ceiling" .

lad:type-CO a skos:Concept ;
    rdfs:label "Credit opinion" ;
    skos:inScheme lad:RatingTypes ;
    skos:notation "CO" ;
    skos:prefLabel "Credit opinion" .

lad:type-INST a skos:Concept ;
    rdfs:label "Instrument rating" ;
    skos:inScheme lad:RatingTypes ;
    skos:notation "INST" ;
    skos:prefLabel "Instrument rating" .

lad:type-LTIDR a skos:Concept ;
    rdfs:label "Long-term IDR" ;
    skos:inScheme lad:RatingTypes ;
    skos:notation "LTIDR" ;
    skos:prefLabel "Long-term Issuer Default Rating" .

lad:type-STIDR a skos:Concept ;
    rdfs:label "Short-term IDR" ;
    skos:inScheme lad:RatingTypes ;
    skos:notation "STIDR" ;
    skos:prefLabel "Short-term Issuer Default Rating" .

lad:watch a owl:ObjectProperty ;
    rdfs:label "rating watch" .

lad:watch-RWN a skos:Concept ;
    rdfs:label "Rating Watch Negative" ;
    skos:inScheme lad:Watches ;
    skos:notation "RWN" ;
    skos:prefLabel "Rating Watch Negative" .

lad:Watches a skos:ConceptScheme ;
    rdfs:label "Rating Watches" .

lad:CurrencyBases a skos:ConceptScheme ;
    rdfs:label "Currency bases" .

lad:Seniorities a skos:ConceptScheme ;
    rdfs:label "Seniorities" .

lad:Outlooks a skos:ConceptScheme ;
    rdfs:label "Outlooks" .

lad:EntityTypes a skos:ConceptScheme ;
    rdfs:label "Entity types" .

lad:RatingTypes a skos:ConceptScheme ;
    rdfs:label "Rating types" .

lad:ActionTypes a skos:ConceptScheme ;
    rdfs:label "Action types" .
```

### axioms.ttl (OWL axioms and SHACL rules over the vocabulary)
```turtle
@prefix lad:  <https://example.org/ladder/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/ladder/axioms> a owl:Ontology ;
    rdfs:label "Credit ratings: axioms and rules" ;
    owl:imports <https://example.org/ladder/ontology> ;
    sh:declare [ sh:prefix "lad" ; sh:namespace "https://example.org/ladder/"^^xsd:anyURI ] ,
               [ sh:prefix "rdf" ; sh:namespace "http://www.w3.org/1999/02/22-rdf-syntax-ns#"^^xsd:anyURI ] .

# === Classes and properties =================================================================

lad:Entity a owl:Class ; rdfs:label "Entity" ; owl:hasKey ( lad:lei ) .
lad:Instrument a owl:Class ; rdfs:label "Instrument" ; owl:disjointWith lad:Entity .
lad:RatingAction a owl:Class ; rdfs:label "Rating action" .

lad:name a owl:DatatypeProperty ; rdfs:domain lad:Entity ; rdfs:range xsd:string .
lad:lei a owl:DatatypeProperty, owl:FunctionalProperty ; rdfs:domain lad:Entity ; rdfs:range xsd:string .
lad:country a owl:DatatypeProperty ; rdfs:domain lad:Entity ; rdfs:range xsd:string .
lad:entityType a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:Entity ; rdfs:range skos:Concept .
lad:sourceSystem a owl:DatatypeProperty, owl:FunctionalProperty ; rdfs:domain lad:Entity ; rdfs:range xsd:string .
lad:parent a owl:ObjectProperty ; rdfs:domain lad:Entity ; rdfs:range lad:Entity ; rdfs:subPropertyOf lad:ancestor .
lad:ancestor a owl:ObjectProperty, owl:TransitiveProperty ; rdfs:label "ancestor" .

lad:description a owl:DatatypeProperty ; rdfs:domain lad:Instrument .
lad:issuer a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:Instrument ; rdfs:range lad:Entity .
lad:guarantor a owl:ObjectProperty ; rdfs:domain lad:Instrument ; rdfs:range lad:Entity .
lad:seniority a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:Instrument ; rdfs:range skos:Concept .
lad:currency a owl:DatatypeProperty, owl:FunctionalProperty ; rdfs:domain lad:Instrument ; rdfs:range xsd:string .
lad:maturity a owl:DatatypeProperty ; rdfs:domain lad:Instrument ; rdfs:range xsd:date .

lad:date a owl:DatatypeProperty, owl:FunctionalProperty ; rdfs:domain lad:RatingAction ; rdfs:range xsd:date .
lad:ratedThing a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:RatingAction ;
    rdfs:range [ owl:unionOf ( lad:Entity lad:Instrument ) ] .
lad:ratingType a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:RatingAction ; rdfs:range skos:Concept .
lad:ccyBasis a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:RatingAction ; rdfs:range skos:Concept .
lad:action a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:RatingAction ; rdfs:range skos:Concept .
lad:rating a owl:DatatypeProperty, owl:FunctionalProperty ; rdfs:domain lad:RatingAction ; rdfs:range xsd:string .
lad:outlook a owl:ObjectProperty ; rdfs:domain lad:RatingAction ; rdfs:range skos:Concept .
lad:watch a owl:ObjectProperty ; rdfs:domain lad:RatingAction ; rdfs:range skos:Concept .
lad:comment a owl:DatatypeProperty ; rdfs:domain lad:RatingAction .

# Derived by the rules below.
lad:sameEntityAs a owl:ObjectProperty, owl:SymmetricProperty, owl:TransitiveProperty ; rdfs:subPropertyOf owl:sameAs .
lad:validTo a owl:DatatypeProperty ; rdfs:domain lad:RatingAction ; rdfs:range xsd:date .
lad:domicile a owl:DatatypeProperty, owl:FunctionalProperty ; rdfs:domain lad:Entity .
lad:creditRiskOf a owl:ObjectProperty, owl:FunctionalProperty ; rdfs:domain lad:Instrument ; rdfs:range lad:Entity .
lad:localCurrency a owl:DatatypeProperty ; rdfs:domain lad:Instrument ; rdfs:range xsd:boolean .

# === Code lists as classes of actions ======================================================

lad:IssuerRatingAction owl:equivalentClass [ a owl:Class ; owl:unionOf (
        [ a owl:Restriction ; owl:onProperty lad:ratingType ; owl:hasValue lad:type-LTIDR ]
        [ a owl:Restriction ; owl:onProperty lad:ratingType ; owl:hasValue lad:type-STIDR ] ) ] .
lad:InstrumentRatingAction owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:ratingType ; owl:hasValue lad:type-INST ] ;
    owl:disjointWith lad:IssuerRatingAction .
lad:CeilingAction owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:ratingType ; owl:hasValue lad:type-CC ] ;
    owl:disjointWith lad:IssuerRatingAction, lad:InstrumentRatingAction .
lad:CreditOpinionAction owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:ratingType ; owl:hasValue lad:type-CO ] ;
    owl:disjointWith lad:IssuerRatingAction, lad:InstrumentRatingAction, lad:RatingInForce .

lad:Downgrade owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:action ; owl:hasValue lad:action-DG ] .
lad:Upgrade owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:action ; owl:hasValue lad:action-UG ] .
lad:RatingChange owl:equivalentClass [ a owl:Class ; owl:unionOf ( lad:Downgrade lad:Upgrade ) ] .
lad:WatchPlacement owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:action ; owl:hasValue lad:action-RW ] ;
    owl:disjointWith lad:RatingChange .
lad:Affirmation owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:action ; owl:hasValue lad:action-AF ] ;
    owl:disjointWith lad:RatingChange .
lad:Withdrawal owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:action ; owl:hasValue lad:action-WD ] ;
    owl:disjointWith lad:RatingChange, lad:DefaultRating, lad:RatingInForce .
lad:ExpectedRating owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:action ; owl:hasValue lad:action-EX ] ;
    owl:disjointWith lad:RatingInForce .
lad:DefaultRating owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:rating ; owl:oneOf ( "RD" "D" ) ] .

lad:TestRecord owl:equivalentClass [ a owl:Restriction ; owl:onProperty lad:sourceSystem ; owl:hasValue "QA" ] ;
    rdfs:subClassOf lad:Entity ; owl:disjointWith lad:Issuer .
lad:Issuer owl:equivalentClass [ a owl:Restriction ; owl:onProperty [ owl:inverseOf lad:ratedThing ] ;
        owl:someValuesFrom [ owl:intersectionOf ( lad:IssuerRatingAction lad:RatingInForce ) ] ] .

# === The rating scales ======================================================================

lad:LongTermScale rdfs:label "long-term scale, strongest first" ;
    rdf:value ( "AAA" "AA+" "AA" "AA-" "A+" "A" "A-" "BBB+" "BBB" "BBB-" "BB+" "BB" "BB-" "B+" "B" "B-" "CCC" "CC" "C" "RD" "D" ) .
lad:InvestmentGradeRatings rdf:value ( "AAA" "AA+" "AA" "AA-" "A+" "A" "A-" "BBB+" "BBB" "BBB-" ) .
lad:ShortTermScale rdfs:label "short-term scale, strongest first" ;
    rdf:value ( "F1+" "F1" "F2" "F3" "B" "C" "RD" "D" ) .

# === Currencies =============================================================================

lad:domesticCurrency a owl:DatatypeProperty ; rdfs:label "domestic currency (country code, currency code)" .
lad:VD lad:domesticCurrency "XVD" .   lad:CV lad:domesticCurrency "CVK" .
lad:GB lad:domesticCurrency "GBP" .   lad:US lad:domesticCurrency "USD" .
lad:DE lad:domesticCurrency "EUR" .   lad:FR lad:domesticCurrency "EUR" .   lad:NL lad:domesticCurrency "EUR" .
lad:GR lad:domesticCurrency "EUR" .   lad:IT lad:domesticCurrency "EUR" .   lad:ES lad:domesticCurrency "EUR" .
lad:LU lad:domesticCurrency "EUR" .

# === Rules (SHACL-AF), run in this order ====================================================

lad:IdentityRule a sh:NodeShape ; sh:targetClass lad:Entity ;
    sh:rule [ a sh:SPARQLRule ; sh:order 1 ; sh:prefixes <https://example.org/ladder/axioms> ; sh:construct """
        CONSTRUCT { $this lad:sameEntityAs ?other }
        WHERE { $this lad:lei ?lei . ?other lad:lei ?lei . FILTER (?other != $this) }""" ] ;
    sh:rule [ a sh:SPARQLRule ; sh:order 2 ; sh:prefixes <https://example.org/ladder/axioms> ; sh:construct """
        CONSTRUCT { $this lad:domicile ?c }
        WHERE {
          { $this lad:sourceSystem "RATINGS" ; lad:country ?c }
          UNION
          { $this lad:sameEntityAs ?r . ?r lad:sourceSystem "RATINGS" ; lad:country ?c }
          UNION
          { $this lad:country ?c FILTER NOT EXISTS { $this lad:sameEntityAs/lad:sourceSystem "RATINGS" }
                                 FILTER NOT EXISTS { $this lad:sourceSystem "RATINGS" } }
        }""" ] .

lad:RatingPeriodRule a sh:NodeShape ; sh:targetClass lad:RatingAction ;
    sh:rule [ a sh:SPARQLRule ; sh:order 3 ; sh:prefixes <https://example.org/ladder/axioms> ; sh:construct """
        CONSTRUCT { $this lad:validTo ?to }
        WHERE {
          $this lad:ratedThing ?t ; lad:ratingType ?type ; lad:date ?d .
          OPTIONAL { $this lad:ccyBasis ?basis }
          { SELECT $this (MIN(?d2) AS ?to) WHERE {
              $this lad:ratedThing ?t ; lad:ratingType ?type ; lad:date ?d .
              OPTIONAL { $this lad:ccyBasis ?basis }
              ?later lad:ratingType ?type ; lad:date ?d2 ; lad:ratedThing ?t2 .
              OPTIONAL { ?later lad:ccyBasis ?basis2 }
              FILTER (?d2 > ?d && COALESCE(?basis2, "") = COALESCE(?basis, ""))
              FILTER (?t2 = ?t || EXISTS { ?t2 lad:sameEntityAs ?t })
              FILTER NOT EXISTS { ?later lad:action lad:action-EX }
            } GROUP BY $this }
        }""" ] ;
    sh:rule [ a sh:SPARQLRule ; sh:order 4 ; sh:prefixes <https://example.org/ladder/axioms> ; sh:construct """
        CONSTRUCT { $this a lad:RatingInForce }
        WHERE {
          $this lad:ratedThing ?t .
          FILTER NOT EXISTS { $this lad:validTo ?to }
          FILTER NOT EXISTS { $this lad:action lad:action-WD }
          FILTER NOT EXISTS { $this lad:action lad:action-EX }
          FILTER NOT EXISTS { $this lad:ratingType lad:type-CO }
          FILTER NOT EXISTS { ?t lad:sourceSystem "QA" }
        }""" ] .

lad:InstrumentRule a sh:NodeShape ; sh:targetClass lad:Instrument ;
    sh:rule [ a sh:SPARQLRule ; sh:order 5 ; sh:prefixes <https://example.org/ladder/axioms> ; sh:construct """
        CONSTRUCT { $this lad:creditRiskOf ?who ; lad:localCurrency ?local }
        WHERE {
          $this lad:issuer ?issuer ; lad:currency ?ccy .
          OPTIONAL { $this lad:guarantor ?g }
          BIND (COALESCE(?g, ?issuer) AS ?who)
          ?issuer lad:domicile ?c .
          BIND (IRI(CONCAT(STR(lad:), ?c)) AS ?country)
          OPTIONAL { ?country lad:domesticCurrency ?home }
          BIND (?ccy = COALESCE(?home, "") AS ?local)
        }""" ] .

# === Constraints (SHACL) ====================================================================

lad:CeilingShape a sh:NodeShape ; sh:targetClass lad:RatingInForce ;
    sh:sparql [ sh:prefixes <https://example.org/ladder/axioms> ; sh:message "a foreign-currency rating above its country's ceiling" ; sh:select """
        SELECT $this WHERE {
          $this lad:ccyBasis lad:basis-FC ; lad:ratingType lad:type-LTIDR ; lad:rating ?r ; lad:ratedThing ?e .
          ?e lad:domicile ?c ; lad:entityType ?type . FILTER (?type != lad:etype-SOV)
          ?sov lad:entityType lad:etype-SOV ; lad:country ?c .
          ?ceil lad:ratedThing ?sov ; lad:ratingType lad:type-CC ; lad:rating ?cap ; a lad:RatingInForce .
          lad:LongTermScale rdf:value ?scale .
          ?scale rdf:rest* ?fromR . ?fromR rdf:first ?r .
          ?scale rdf:rest* ?fromCap . ?fromCap rdf:first ?cap .
          FILTER NOT EXISTS { ?fromCap rdf:rest* ?fromR }
        }""" ] .

lad:TestRecordShape a sh:NodeShape ; sh:targetClass lad:TestRecord ;
    sh:property [ sh:path [ sh:inversePath lad:ratedThing ] ; sh:maxCount 0 ; sh:severity sh:Info ;
                  sh:message "a test record's actions are not rating actions" ] .
```

## Questions

Answer each question below from the data above. Start each answer on a new line with its
number in bold, like **Q1.**, give the direct answer first, then at most two sentences of
reasoning that cite the records (IDs) you relied on.

Then end with one JSON block (```json) holding the structured answer to each question listed
here, with exactly these fields, shaped like {"Q1": {"field": value}, ...}. Name entities by their record ID: the entity_id in the CSV files, or the part of the IRI after lad: in the RDF (E01, not Kestrel Energy plc).

- Q1: rating (a rating, or "none")
- Q2: downgraded ("yes", "no" or "depends")
- Q3: investment_grade ("yes", "no" or "depends"), rating (a rating, or "none")
- Q4: outlook (an outlook)
- Q5: risk_of (a record ID), rating (a rating, or "none")
- Q7: issuers (a list of record IDs)
- Q8: entities (a list of record IDs)
- Q9: count (a number)
- Q10: investment_grade ("yes", "no" or "depends")
- Q11: rating (a rating, or "none")
- Q12: rating (a rating, or "none")
- Q13: count (a number)
- Q14: rating (a rating, or "none")
- Q15: rating (a rating, or "none")
- Q16: changed ("yes", "no" or "depends")
- Q17: downgraded ("yes", "no" or "depends")
- Q18: issuers (a list of record IDs)
- Q19: issuers (a list of record IDs)
- Q20: in_default ("yes", "no" or "depends")
- Q21: entities (a list of record IDs)
- Q22: entities (a list of record IDs)
- Q23: rating (a rating, or "none")
- Q24: investment_grade ("yes", "no" or "depends")
- Q25: count (a number)
- Q26: rating (a rating, or "none")
- Q27: rating (a rating, or "none")
- Q28: rating (a rating, or "none")
- Q29: rating (a rating, or "none")
- Q30: entities (a list of record IDs)
- Q31: any ("yes", "no" or "depends")
- Q32: parent (a record ID)
- Q33: risk_of (a record ID), rating (a rating, or "none")
- Q34: same_group ("yes", "no" or "depends")
- Q35: count (a number)
- Q36: count (a number)
- Q37: count (a number)
- Q38: same ("yes", "no" or "depends")
- Q39: rating (a rating, or "none")
- Q40: count (a number)
- Q41: rating (a rating, or "none")
- Q42: country (a country code)
- Q43: count (a number)
- Q44: local_currency ("yes", "no" or "depends")
- Q45: above_ceiling ("yes", "no" or "depends")
- Q46: issuer_rating ("yes", "no" or "depends")
- Q47: rating (a rating, or "none")
- Q48: count (a number)

Q1. What was Kestrel Energy's rating on 1 January 2025?
Q2. Has Kestrel Energy been downgraded in 2026?
Q3. Is Kestrel Energy's 2031 note investment grade?
Q4. What is Northwind Holdings' current outlook?
Q5. Whose credit risk does a holder of the Northwind Finance 2030 notes take, and how is it rated?
Q6. Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?
Q7. Which issuers were downgraded in 2026?
Q8. Which entities were in default on 1 October 2026?
Q9. As of 1 October 2026, how many distinct issuers hold an issuer rating?
Q10. Is Valdoria Telecom investment grade?
Q11. What was Marlow Utilities' rating on 1 June 2025?
Q12. What was Marlow Utilities' rating on 1 January 2024?
Q13. How many times has Marlow Utilities been downgraded?
Q14. What was Halden Foods' rating on 1 January 2024?
Q15. What was Halden Bank's rating on 1 January 2026?
Q16. Has Marlow Utilities' rating changed since 1 January 2025?
Q17. Was Orrin Bank downgraded in 2026?
Q18. Which issuers were on Rating Watch Negative on 1 October 2026?
Q19. Which issuers had a Negative outlook on 1 October 2026?
Q20. Is Pellam Retail in default?
Q21. Which entities had an issuer rating at some point but no longer had one on 1 October 2026?
Q22. Which entities have ever been in default?
Q23. What is Kestrel Energy's short-term rating?
Q24. Is Kestrel Energy's issuer rating investment grade?
Q25. How many instruments held an investment-grade rating on 1 October 2026?
Q26. What is Corvenia Power's local-currency rating?
Q27. How is Corvenia Power's 2032 note rated?
Q28. What is the Republic of Corvenia's foreign-currency issuer rating?
Q29. What is the Republic of Valdoria's issuer rating?
Q30. Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?
Q31. Did any company have a foreign-currency issuer rating above its country's ceiling on 1 October 2026?
Q32. Who is Halden Leasing's ultimate parent?
Q33. Whose credit risk does a holder of the Halden Leasing 2028 notes take, and how is it rated?
Q34. Is Halden Foods part of the same group as Halden Bank?
Q35. How many entities are in the Halden group, the parent included?
Q36. How many entities are in the Northwind group, the parent included?
Q37. How many distinct legal entities does the data describe?
Q38. Are Orrin Bank AG and Orrin Bancorp Inc the same entity?
Q39. What is Northwind Holdings' current rating?
Q40. How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?
Q41. What is Brindle Capital's current rating?
Q42. In which country is Halden Bank domiciled?
Q43. How many distinct entities are domiciled in Luxembourg (LU)?
Q44. Is Valdoria Telecom's 2027 note a local-currency obligation?
Q45. Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?
Q46. Does Halden Leasing have an issuer rating?
Q47. How is Corvenia Power's 2034 note rated?
Q48. How many instruments held a rating on 1 October 2026?
