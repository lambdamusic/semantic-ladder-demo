<!-- system: You answer questions about a credit-ratings dataset. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

### facts.ttl (RDF, Turtle)
```turtle
@prefix lad: <https://example.org/ladder/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

lad:A01 a lad:RatingAction ;
    rdfs:label "E01 AS A- 2024-03-12" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-03-12"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E01 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-LTIDR .

lad:A02 a lad:RatingAction ;
    rdfs:label "E01 DG BBB 2025-06-20" ;
    lad:action lad:action-DG ;
    lad:ccyBasis lad:basis-FC ;
    lad:comment "weaker cash flow after asset sale" ;
    lad:date "2025-06-20"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E01 ;
    lad:rating "BBB" ;
    lad:ratingType lad:type-LTIDR .

lad:A03 a lad:RatingAction ;
    rdfs:label "E01 AF BBB 2026-02-10" ;
    lad:action lad:action-AF ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-02-10"^^xsd:date ;
    lad:outlook lad:outlook-NEG ;
    lad:ratedThing lad:E01 ;
    lad:rating "BBB" ;
    lad:ratingType lad:type-LTIDR .

lad:A04 a lad:RatingAction ;
    rdfs:label "E01 AF F2 2026-02-10" ;
    lad:action lad:action-AF ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-02-10"^^xsd:date ;
    lad:ratedThing lad:E01 ;
    lad:rating "F2" ;
    lad:ratingType lad:type-STIDR .

lad:A05 a lad:RatingAction ;
    rdfs:label "I01 AS A- 2024-03-12" ;
    lad:action lad:action-AS ;
    lad:date "2024-03-12"^^xsd:date ;
    lad:ratedThing lad:I01 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-INST .

lad:A06 a lad:RatingAction ;
    rdfs:label "I01 DG BBB 2025-06-20" ;
    lad:action lad:action-DG ;
    lad:date "2025-06-20"^^xsd:date ;
    lad:ratedThing lad:I01 ;
    lad:rating "BBB" ;
    lad:ratingType lad:type-INST .

lad:A07 a lad:RatingAction ;
    rdfs:label "I02 DG BB+ 2025-06-20" ;
    lad:action lad:action-DG ;
    lad:date "2025-06-20"^^xsd:date ;
    lad:ratedThing lad:I02 ;
    lad:rating "BB+" ;
    lad:ratingType lad:type-INST .

lad:A08 a lad:RatingAction ;
    rdfs:label "E02 AS A 2023-11-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2023-11-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E02 ;
    lad:rating "A" ;
    lad:ratingType lad:type-LTIDR .

lad:A09 a lad:RatingAction ;
    rdfs:label "E03 AF A 2025-09-15" ;
    lad:action lad:action-AF ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2025-09-15"^^xsd:date ;
    lad:outlook lad:outlook-POS ;
    lad:ratedThing lad:E03 ;
    lad:rating "A" ;
    lad:ratingType lad:type-LTIDR .

lad:A10 a lad:RatingAction ;
    rdfs:label "I03 AS A 2023-11-01" ;
    lad:action lad:action-AS ;
    lad:date "2023-11-01"^^xsd:date ;
    lad:ratedThing lad:I03 ;
    lad:rating "A" ;
    lad:ratingType lad:type-INST .

lad:A11 a lad:RatingAction ;
    rdfs:label "I03 AF A 2025-09-15" ;
    lad:action lad:action-AF ;
    lad:date "2025-09-15"^^xsd:date ;
    lad:ratedThing lad:I03 ;
    lad:rating "A" ;
    lad:ratingType lad:type-INST .

lad:A12 a lad:RatingAction ;
    rdfs:label "VD AS BB 2025-04-01" ;
    lad:action lad:action-AS ;
    lad:date "2025-04-01"^^xsd:date ;
    lad:ratedThing lad:VD ;
    lad:rating "BB" ;
    lad:ratingType lad:type-CC .

lad:A13 a lad:RatingAction ;
    rdfs:label "E05 AS BBB- 2025-04-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-LC ;
    lad:date "2025-04-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E05 ;
    lad:rating "BBB-" ;
    lad:ratingType lad:type-LTIDR .

lad:A14 a lad:RatingAction ;
    rdfs:label "E05 AS BB 2025-04-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2025-04-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E05 ;
    lad:rating "BB" ;
    lad:ratingType lad:type-LTIDR .

lad:A15 a lad:RatingAction ;
    rdfs:label "I04 AS BB 2025-04-01" ;
    lad:action lad:action-AS ;
    lad:date "2025-04-01"^^xsd:date ;
    lad:ratedThing lad:I04 ;
    lad:rating "BB" ;
    lad:ratingType lad:type-INST .

lad:A16 a lad:RatingAction ;
    rdfs:label "E06 AS A- 2024-05-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-05-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E06 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-LTIDR .

lad:A17 a lad:RatingAction ;
    rdfs:label "E06 RW A- 2026-09-03" ;
    lad:action lad:action-RW ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-09-03"^^xsd:date ;
    lad:ratedThing lad:E06 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-LTIDR ;
    lad:watch lad:watch-RWN .

lad:A18 a lad:RatingAction ;
    rdfs:label "E07 AS BB 2024-01-10" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-01-10"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E07 ;
    lad:rating "BB" ;
    lad:ratingType lad:type-LTIDR .

lad:A19 a lad:RatingAction ;
    rdfs:label "E07 WD WD 2026-05-12" ;
    lad:action lad:action-WD ;
    lad:ccyBasis lad:basis-FC ;
    lad:comment "commercial reasons" ;
    lad:date "2026-05-12"^^xsd:date ;
    lad:ratedThing lad:E07 ;
    lad:rating "WD" ;
    lad:ratingType lad:type-LTIDR .

lad:A20 a lad:RatingAction ;
    rdfs:label "E08 AS B 2024-06-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-06-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E08 ;
    lad:rating "B" ;
    lad:ratingType lad:type-LTIDR .

lad:A21 a lad:RatingAction ;
    rdfs:label "E08 DG CCC 2026-01-20" ;
    lad:action lad:action-DG ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-01-20"^^xsd:date ;
    lad:ratedThing lad:E08 ;
    lad:rating "CCC" ;
    lad:ratingType lad:type-LTIDR .

lad:A22 a lad:RatingAction ;
    rdfs:label "E08 DG RD 2026-07-08" ;
    lad:action lad:action-DG ;
    lad:ccyBasis lad:basis-FC ;
    lad:comment "distressed debt exchange completed" ;
    lad:date "2026-07-08"^^xsd:date ;
    lad:ratedThing lad:E08 ;
    lad:rating "RD" ;
    lad:ratingType lad:type-LTIDR .

lad:A23 a lad:RatingAction ;
    rdfs:label "I02 AS BBB 2024-03-12" ;
    lad:action lad:action-AS ;
    lad:date "2024-03-12"^^xsd:date ;
    lad:ratedThing lad:I02 ;
    lad:rating "BBB" ;
    lad:ratingType lad:type-INST .

lad:A24 a lad:RatingAction ;
    rdfs:label "E09 AS A 2023-05-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2023-05-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E09 ;
    lad:rating "A" ;
    lad:ratingType lad:type-LTIDR .

lad:A25 a lad:RatingAction ;
    rdfs:label "E09 AF A 2026-03-01" ;
    lad:action lad:action-AF ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-03-01"^^xsd:date ;
    lad:outlook lad:outlook-NEG ;
    lad:ratedThing lad:E09 ;
    lad:rating "A" ;
    lad:ratingType lad:type-LTIDR .

lad:A26 a lad:RatingAction ;
    rdfs:label "E10 AS A- 2023-05-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:comment "support from parent" ;
    lad:date "2023-05-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E10 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-LTIDR .

lad:A27 a lad:RatingAction ;
    rdfs:label "E10 DG BBB+ 2026-04-15" ;
    lad:action lad:action-DG ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-04-15"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E10 ;
    lad:rating "BBB+" ;
    lad:ratingType lad:type-LTIDR .

lad:A28 a lad:RatingAction ;
    rdfs:label "I05 AS A- 2023-06-01" ;
    lad:action lad:action-AS ;
    lad:date "2023-06-01"^^xsd:date ;
    lad:ratedThing lad:I05 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-INST .

lad:A29 a lad:RatingAction ;
    rdfs:label "I05 DG BBB+ 2026-04-15" ;
    lad:action lad:action-DG ;
    lad:date "2026-04-15"^^xsd:date ;
    lad:ratedThing lad:I05 ;
    lad:rating "BBB+" ;
    lad:ratingType lad:type-INST .

lad:A30 a lad:RatingAction ;
    rdfs:label "E12 AS BB- 2024-02-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-02-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E12 ;
    lad:rating "BB-" ;
    lad:ratingType lad:type-LTIDR .

lad:A31 a lad:RatingAction ;
    rdfs:label "E12 UG BB 2025-08-01" ;
    lad:action lad:action-UG ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2025-08-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E12 ;
    lad:rating "BB" ;
    lad:ratingType lad:type-LTIDR .

lad:A32 a lad:RatingAction ;
    rdfs:label "E13 AS BBB 2024-07-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-07-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E13 ;
    lad:rating "BBB" ;
    lad:ratingType lad:type-LTIDR .

lad:A33 a lad:RatingAction ;
    rdfs:label "E14 AF BBB+ 2026-05-01" ;
    lad:action lad:action-AF ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2026-05-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E14 ;
    lad:rating "BBB+" ;
    lad:ratingType lad:type-LTIDR .

lad:A34 a lad:RatingAction ;
    rdfs:label "E14 AS A- 2023-01-15" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2023-01-15"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E14 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-LTIDR .

lad:A35 a lad:RatingAction ;
    rdfs:label "E14 RW BBB+ 2025-11-20" ;
    lad:action lad:action-RW ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2025-11-20"^^xsd:date ;
    lad:ratedThing lad:E14 ;
    lad:rating "BBB+" ;
    lad:ratingType lad:type-LTIDR ;
    lad:watch lad:watch-RWN .

lad:A36 a lad:RatingAction ;
    rdfs:label "E14 DG BBB+ 2024-09-30" ;
    lad:action lad:action-DG ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-09-30"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E14 ;
    lad:rating "BBB+" ;
    lad:ratingType lad:type-LTIDR .

lad:A37 a lad:RatingAction ;
    rdfs:label "CV AS A 2024-01-01" ;
    lad:action lad:action-AS ;
    lad:date "2024-01-01"^^xsd:date ;
    lad:ratedThing lad:CV ;
    lad:rating "A" ;
    lad:ratingType lad:type-CC .

lad:A38 a lad:RatingAction ;
    rdfs:label "CV AS BBB+ 2024-01-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-01-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:CV ;
    lad:rating "BBB+" ;
    lad:ratingType lad:type-LTIDR .

lad:A39 a lad:RatingAction ;
    rdfs:label "CV AS A- 2024-01-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-LC ;
    lad:date "2024-01-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:CV ;
    lad:rating "A-" ;
    lad:ratingType lad:type-LTIDR .

lad:A40 a lad:RatingAction ;
    rdfs:label "E15 AS A+ 2024-03-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-LC ;
    lad:date "2024-03-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E15 ;
    lad:rating "A+" ;
    lad:ratingType lad:type-LTIDR .

lad:A41 a lad:RatingAction ;
    rdfs:label "E15 AS A 2024-03-01" ;
    lad:action lad:action-AS ;
    lad:ccyBasis lad:basis-FC ;
    lad:date "2024-03-01"^^xsd:date ;
    lad:outlook lad:outlook-STA ;
    lad:ratedThing lad:E15 ;
    lad:rating "A" ;
    lad:ratingType lad:type-LTIDR .

lad:A42 a lad:RatingAction ;
    rdfs:label "I06 AS A- 2024-03-01" ;
    lad:action lad:action-AS ;
    lad:date "2024-03-01"^^xsd:date ;
    lad:ratedThing lad:I06 ;
    lad:rating "A-" ;
    lad:ratingType lad:type-INST .

lad:E03 a lad:Entity ;
    rdfs:label "NORTHWIND HLDGS" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "NWND00HOLDINGS00GB42" ;
    lad:name "NORTHWIND HLDGS" ;
    lad:sourceSystem "RESEARCH" .

lad:E04 a lad:Entity ;
    rdfs:label "Northwind Finance BV" ;
    lad:country "NL" ;
    lad:entityType lad:etype-FINSUB ;
    lad:lei "NWND00FINANCE000NL07" ;
    lad:name "Northwind Finance BV" ;
    lad:parent lad:E02 ;
    lad:sourceSystem "RATINGS" .

lad:E11 a lad:Entity ;
    rdfs:label "Halden Leasing SA" ;
    lad:country "FR" ;
    lad:entityType lad:etype-FINSUB ;
    lad:lei "HLDN00LEASING000FR30" ;
    lad:name "Halden Leasing SA" ;
    lad:parent lad:E10 ;
    lad:sourceSystem "RATINGS" .

lad:E13 a lad:Entity ;
    rdfs:label "Orrin Bancorp Inc" ;
    lad:country "US" ;
    lad:entityType lad:etype-BANK ;
    lad:lei "ORBC00BANCORP000US45" ;
    lad:name "Orrin Bancorp Inc" ;
    lad:sourceSystem "RATINGS" .

lad:I04 a lad:Instrument ;
    rdfs:label "Valdoria Telecom 5.00% 2029" ;
    lad:currency "USD" ;
    lad:description "Valdoria Telecom 5.00% notes due 2029" ;
    lad:issuer lad:E05 ;
    lad:maturity "2029-11-20"^^xsd:date ;
    lad:seniority lad:seniority-SU .

lad:I06 a lad:Instrument ;
    rdfs:label "Corvenia Power 7.10% 2032" ;
    lad:currency "USD" ;
    lad:description "Corvenia Power 7.10% notes due 2032" ;
    lad:issuer lad:E15 ;
    lad:maturity "2032-02-15"^^xsd:date ;
    lad:seniority lad:seniority-SUB .

lad:VD a lad:Entity ;
    rdfs:label "Republic of Valdoria" ;
    lad:country "VD" ;
    lad:entityType lad:etype-SOV ;
    lad:name "Republic of Valdoria" ;
    lad:sourceSystem "RATINGS" .

lad:E06 a lad:Entity ;
    rdfs:label "Orrin Bank AG" ;
    lad:country "DE" ;
    lad:entityType lad:etype-BANK ;
    lad:lei "ORRN00BANK00000DE233" ;
    lad:name "Orrin Bank AG" ;
    lad:sourceSystem "RATINGS" .

lad:E07 a lad:Entity ;
    rdfs:label "Pellam Retail Ltd" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "PLLM00RETAIL0000GB88" ;
    lad:name "Pellam Retail Ltd" ;
    lad:sourceSystem "RATINGS" .

lad:E12 a lad:Entity ;
    rdfs:label "Halden Foods Ltd" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "HLDF00FOODS00000GB77" ;
    lad:name "Halden Foods Ltd" ;
    lad:sourceSystem "RATINGS" .

lad:I01 a lad:Instrument ;
    rdfs:label "Kestrel Energy 4.50% 2030" ;
    lad:currency "GBP" ;
    lad:description "Kestrel Energy 4.50% notes due 2030" ;
    lad:issuer lad:E01 ;
    lad:maturity "2030-03-15"^^xsd:date ;
    lad:seniority lad:seniority-SU .

lad:I02 a lad:Instrument ;
    rdfs:label "Kestrel Energy 6.25% 2031" ;
    lad:currency "GBP" ;
    lad:description "Kestrel Energy 6.25% notes due 2031" ;
    lad:issuer lad:E01 ;
    lad:maturity "2031-09-30"^^xsd:date ;
    lad:seniority lad:seniority-SUB .

lad:I03 a lad:Instrument ;
    rdfs:label "Northwind Finance 3.75% 2030" ;
    lad:currency "EUR" ;
    lad:description "Northwind Finance 3.75% notes due 2030" ;
    lad:guarantor lad:E02 ;
    lad:issuer lad:E04 ;
    lad:maturity "2030-05-01"^^xsd:date ;
    lad:seniority lad:seniority-SU .

lad:I05 a lad:Instrument ;
    rdfs:label "Halden Leasing 2.90% 2028" ;
    lad:currency "EUR" ;
    lad:description "Halden Leasing 2.90% notes due 2028" ;
    lad:guarantor lad:E10 ;
    lad:issuer lad:E11 ;
    lad:maturity "2028-06-30"^^xsd:date ;
    lad:seniority lad:seniority-SU .

lad:CV a lad:Entity ;
    rdfs:label "Republic of Corvenia" ;
    lad:country "CV" ;
    lad:entityType lad:etype-SOV ;
    lad:name "Republic of Corvenia" ;
    lad:sourceSystem "RATINGS" .

lad:E02 a lad:Entity ;
    rdfs:label "Northwind Holdings plc" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "NWND00HOLDINGS00GB42" ;
    lad:name "Northwind Holdings plc" ;
    lad:sourceSystem "RATINGS" .

lad:E05 a lad:Entity ;
    rdfs:label "Valdoria Telecom SA" ;
    lad:country "VD" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "VLDT00TELECOM0000V19" ;
    lad:name "Valdoria Telecom SA" ;
    lad:sourceSystem "RATINGS" .

lad:E08 a lad:Entity ;
    rdfs:label "Saxby Shipping SA" ;
    lad:country "GR" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "SXBY00SHIPPING00GR51" ;
    lad:name "Saxby Shipping SA" ;
    lad:sourceSystem "RATINGS" .

lad:E09 a lad:Entity ;
    rdfs:label "Halden Group plc" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "HLDN00GROUP00000GB15" ;
    lad:name "Halden Group plc" ;
    lad:sourceSystem "RATINGS" .

lad:E15 a lad:Entity ;
    rdfs:label "Corvenia Power SA" ;
    lad:country "CV" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "CRVP00POWER00000CV58" ;
    lad:name "Corvenia Power SA" ;
    lad:sourceSystem "RATINGS" .

lad:E10 a lad:Entity ;
    rdfs:label "Halden Bank AG" ;
    lad:country "DE" ;
    lad:entityType lad:etype-BANK ;
    lad:lei "HLDN00BANK000000DE62" ;
    lad:name "Halden Bank AG" ;
    lad:parent lad:E09 ;
    lad:sourceSystem "RATINGS" .

lad:E14 a lad:Entity ;
    rdfs:label "Marlow Utilities plc" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "MRLW00UTILITIES0GB26" ;
    lad:name "Marlow Utilities plc" ;
    lad:sourceSystem "RATINGS" .

lad:E01 a lad:Entity ;
    rdfs:label "Kestrel Energy plc" ;
    lad:country "GB" ;
    lad:entityType lad:etype-CORP ;
    lad:lei "KSTL00ENERGY000000A1" ;
    lad:name "Kestrel Energy plc" ;
    lad:sourceSystem "RATINGS" .
```

### ontology.ttl (the vocabulary the data uses)
```turtle
@prefix lad:  <https://example.org/ladder/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

# A deliberately small ontology for the semantics-ladder experiment.
# The semantics live in the definitions (skos:definition), in plain English, not in OWL
# axioms: the point is to see how much an LLM gains from being told what things mean.
# Each code used in the CSV files (LTIDR, AF, RWN, ...) is a concept here, with
# skos:notation giving the code as it appears in the data.
#
# Loosely follows public rating-agency conventions. It is not any agency's definitions,
# and all the data it describes is invented.

<https://example.org/ladder/ontology> a owl:Ontology ;
    rdfs:label "Credit ratings: a teaching ontology" ;
    rdfs:comment "Entities, instruments, rating actions and the codes the data uses, each with a definition that states what it means and how to read it. Invented for an experiment; not a model of any real rating agency." ;
    owl:versionInfo "0.1" .


# === Classes ==============================================================================

lad:Entity a owl:Class ;
    rdfs:label "Entity" ;
    skos:definition "A legal entity: a company, bank, finance subsidiary or sovereign. An entity is identified by its LEI (lad:lei), not by its name or record ID. The data holds records from more than one source system (lad:sourceSystem), so the same entity can appear as several records with different IDs and differently spelled names: two records with the same LEI are the same entity, and every fact recorded against either record is a fact about that one entity." .

lad:Instrument a owl:Class ;
    rdfs:label "Instrument" ;
    skos:definition "A debt instrument, such as a bond or note, issued by an entity (lad:issuer). An instrument's rating is not the issuer's rating: it can sit above or below it depending on seniority (lad:seniority) and on any guarantee (lad:guarantor)." .

lad:RatingAction a owl:Class ;
    rdfs:label "Rating action" ;
    skos:definition "Something a rating agency did to a rating on a date (lad:date): assigned, affirmed, upgraded, downgraded, placed on Watch or withdrawn it. Each action applies to one rated thing (lad:ratedThing), one rating type (lad:ratingType) and, for issuer ratings, one currency basis (lad:ccyBasis). A rating holds from its action date until the next action on the same thing, type and basis: so the rating on a date D is the one set by the latest action on or before D, and the current rating is the latest action overall. lad:rating always holds the rating as it stands after the action, including when it did not change." .


# === Properties: entities =================================================================

lad:name a owl:DatatypeProperty ; rdfs:label "name" ;
    skos:definition "The name as the source system spells it. Names are not identifiers: the same entity can be spelled differently in different systems." .

lad:lei a owl:DatatypeProperty ; rdfs:label "LEI" ;
    skos:definition "Legal Entity Identifier: the identifier that says which legal entity a record describes. Same LEI, same entity. Sovereigns have none." .

lad:country a owl:DatatypeProperty ; rdfs:label "country" ;
    skos:definition "ISO-style code of the country where the entity is domiciled. It decides which Country Ceiling, if any, applies to the entity's foreign-currency ratings. VD is the Republic of Valdoria and CV the Republic of Corvenia (both invented)." .

lad:entityType a owl:ObjectProperty ; rdfs:label "entity type" ;
    skos:definition "What kind of entity it is: a concept of the scheme lad:EntityTypes." .

lad:parent a owl:ObjectProperty ; rdfs:label "parent" ;
    skos:definition "The entity that owns and controls this one." .

lad:sourceSystem a owl:DatatypeProperty ; rdfs:label "source system" ;
    skos:definition "The internal system the record comes from (RATINGS, RESEARCH). Each system keeps its own records of the same entities; see lad:Entity." .


# === Properties: instruments ==============================================================

lad:description a owl:DatatypeProperty ; rdfs:label "description" ;
    skos:definition "The instrument's name: issuer, coupon and maturity year." .

lad:issuer a owl:ObjectProperty ; rdfs:label "issuer" ;
    skos:definition "The entity that issued the instrument and owes the payments. Not necessarily the entity whose credit risk the investor takes: see lad:guarantor." .

lad:guarantor a owl:ObjectProperty ; rdfs:label "guarantor" ;
    skos:definition "An entity that guarantees the instrument's payments if the issuer does not pay. A guaranteed instrument carries the guarantor's credit risk, so it is rated in line with the guarantor's issuer rating, not the issuer's." .

lad:seniority a owl:ObjectProperty ; rdfs:label "seniority" ;
    skos:definition "Where the instrument ranks in repayment if the issuer fails: a concept of the scheme lad:Seniorities." .

lad:currency a owl:DatatypeProperty ; rdfs:label "currency" ;
    skos:definition "The currency the instrument pays in. Debt in a currency other than the domestic one of the issuer's country is exposed to that country's transfer and convertibility risk: see lad:type-CC." .

lad:maturity a owl:DatatypeProperty ; rdfs:label "maturity" ;
    skos:definition "The date the instrument is due to be repaid." .


# === Properties: rating actions ===========================================================

lad:date a owl:DatatypeProperty ; rdfs:label "date" ;
    skos:definition "The date the action took effect." .

lad:ratedThing a owl:ObjectProperty ; rdfs:label "rated thing" ;
    skos:definition "What the action is about: an entity (for issuer ratings and Country Ceilings) or an instrument (for instrument ratings)." .

lad:ratingType a owl:ObjectProperty ; rdfs:label "rating type" ;
    skos:definition "Which kind of rating the action concerns: a concept of the scheme lad:RatingTypes. Different types are different ratings and are never compared or combined with each other." .

lad:ccyBasis a owl:ObjectProperty ; rdfs:label "currency basis" ;
    skos:definition "For issuer ratings, whether the rating covers foreign-currency (FC) or local-currency (LC) obligations: a concept of the scheme lad:CurrencyBases. An entity can have both, with different values." .

lad:action a owl:ObjectProperty ; rdfs:label "action" ;
    skos:definition "What was done: a concept of the scheme lad:ActionTypes. Only upgrades and downgrades change a rating." .

lad:rating a owl:DatatypeProperty ; rdfs:label "rating" ;
    skos:definition "The rating after the action, on the scale of its rating type. Long-term scale, strongest to weakest: AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, CCC, CC, C, RD, D. Investment grade means BBB- or higher; BB+ and below is speculative grade (high yield). RD (restricted default) means the issuer has defaulted on some material obligations, for instance by completing a distressed debt exchange, without being wound up: RD is a default. D means a general default. Short-term scale, strongest to weakest: F1+, F1, F2, F3, B, C, RD, D. WD means the rating was withdrawn (see lad:action-WD): it is not a point on either scale." .

lad:outlook a owl:ObjectProperty ; rdfs:label "outlook" ;
    skos:definition "The likely direction of a long-term rating over the next one to two years: a concept of the scheme lad:Outlooks. An outlook is not a rating: revising it does not change the rating." .

lad:watch a owl:ObjectProperty ; rdfs:label "rating watch" ;
    skos:definition "Set when the rating is on Rating Watch: a concept of the scheme lad:Watches. A Watch is not a rating change." .

lad:comment a owl:DatatypeProperty ; rdfs:label "comment" ;
    skos:definition "The analyst's note on the action, such as the reason for a withdrawal." .


# === Code lists (the codes used in the CSV files) =========================================

lad:RatingTypes a skos:ConceptScheme ; rdfs:label "Rating types" .

lad:type-LTIDR a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "LTIDR" ;
    rdfs:label "Long-term IDR" ; skos:prefLabel "Long-term Issuer Default Rating" ;
    skos:definition "The issuer's own creditworthiness: how likely it is to default on its obligations, on the long-term scale. This is what people usually mean by an entity's rating. The foreign-currency (FC) one is the headline rating; there may also be a local-currency (LC) one." .

lad:type-STIDR a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "STIDR" ;
    rdfs:label "Short-term IDR" ; skos:prefLabel "Short-term Issuer Default Rating" ;
    skos:definition "The issuer's ability to meet obligations falling due within about a year, on the short-term scale (F1+ to D). Not comparable with long-term ratings." .

lad:type-INST a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "INST" ;
    rdfs:label "Instrument rating" ; skos:prefLabel "Instrument rating" ;
    skos:definition "The rating of one specific instrument. It starts from the issuer's long-term rating and is notched for the instrument's seniority and expected recovery: subordinated debt is usually rated below the issuer, and guaranteed debt is rated on the guarantor. An instrument rating is never the rating of the issuer." .

lad:type-CC a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "CC" ;
    rdfs:label "Country Ceiling" ; skos:prefLabel "Country Ceiling" ;
    skos:definition "Not a rating of anyone. A cap, set for a country, on the foreign-currency ratings of entities domiciled there and of their foreign-currency debt. It reflects transfer and convertibility risk: the risk that the government stops money being converted or sent abroad, so even a sound company could not pay foreign-currency debt. Foreign-currency ratings of entities in the country are generally no higher than the ceiling; local-currency ratings are not capped. A Country Ceiling is not the sovereign's own issuer rating." .

lad:CurrencyBases a skos:ConceptScheme ; rdfs:label "Currency bases" .
lad:basis-FC a skos:Concept ; skos:inScheme lad:CurrencyBases ; skos:notation "FC" ;
    rdfs:label "Foreign currency" ; skos:prefLabel "Foreign currency" ;
    skos:definition "Covers obligations in foreign currency, so it is subject to the Country Ceiling." .
lad:basis-LC a skos:Concept ; skos:inScheme lad:CurrencyBases ; skos:notation "LC" ;
    rdfs:label "Local currency" ; skos:prefLabel "Local currency" ;
    skos:definition "Covers obligations in the currency of the entity's own country; not subject to the Country Ceiling." .

lad:ActionTypes a skos:ConceptScheme ; rdfs:label "Action types" .
lad:action-AS a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "AS" ;
    rdfs:label "Assigned" ; skos:prefLabel "Assigned" ; skos:definition "A first rating is given." .
lad:action-AF a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "AF" ;
    rdfs:label "Affirmed" ; skos:prefLabel "Affirmed" ;
    skos:definition "The rating is reviewed and kept the same. The outlook may be revised in the same action; that does not make it an upgrade or a downgrade." .
lad:action-UG a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "UG" ;
    rdfs:label "Upgraded" ; skos:prefLabel "Upgraded" ; skos:definition "The rating is raised." .
lad:action-DG a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "DG" ;
    rdfs:label "Downgraded" ; skos:prefLabel "Downgraded" ; skos:definition "The rating is lowered. The only action that counts as a downgrade." .
lad:action-RW a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "RW" ;
    rdfs:label "Placed on Rating Watch" ; skos:prefLabel "Placed on Rating Watch" ;
    skos:definition "The rating is flagged as likely to change soon, usually within about six months, in the direction lad:watch gives. The rating itself is unchanged: not a downgrade." .
lad:action-WD a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "WD" ;
    rdfs:label "Withdrawn" ; skos:prefLabel "Withdrawn" ;
    skos:definition "The agency stops maintaining the rating, often for commercial reasons (the issuer no longer pays for it, or the debt is repaid). After a withdrawal the entity has no rating of that type. A withdrawal is not a credit event: it says nothing about default, and is not a downgrade." .

lad:Outlooks a skos:ConceptScheme ; rdfs:label "Outlooks" .
lad:outlook-STA a skos:Concept ; skos:inScheme lad:Outlooks ; skos:notation "STA" ; rdfs:label "Stable" ; skos:prefLabel "Stable" ;
    skos:definition "No direction expected." .
lad:outlook-POS a skos:Concept ; skos:inScheme lad:Outlooks ; skos:notation "POS" ; rdfs:label "Positive" ; skos:prefLabel "Positive" ;
    skos:definition "The rating may go up over one to two years." .
lad:outlook-NEG a skos:Concept ; skos:inScheme lad:Outlooks ; skos:notation "NEG" ; rdfs:label "Negative" ; skos:prefLabel "Negative" ;
    skos:definition "The rating may go down over one to two years. Not a downgrade." .

lad:Watches a skos:ConceptScheme ; rdfs:label "Rating Watches" .
lad:watch-RWN a skos:Concept ; skos:inScheme lad:Watches ; skos:notation "RWN" ; rdfs:label "Rating Watch Negative" ; skos:prefLabel "Rating Watch Negative" ;
    skos:definition "A downgrade is likely in the near term. Not a downgrade yet." .

lad:Seniorities a skos:ConceptScheme ; rdfs:label "Seniorities" .
lad:seniority-SU a skos:Concept ; skos:inScheme lad:Seniorities ; skos:notation "SU" ; rdfs:label "Senior unsecured" ; skos:prefLabel "Senior unsecured" ;
    skos:definition "Ranks with the issuer's ordinary debts; usually rated at the level of the issuer's long-term rating." .
lad:seniority-SUB a skos:Concept ; skos:inScheme lad:Seniorities ; skos:notation "SUB" ; rdfs:label "Subordinated" ; skos:prefLabel "Subordinated" ;
    skos:definition "Repaid only after senior debt, so investors recover less in a default; usually rated one or more notches below the issuer's long-term rating." .

lad:EntityTypes a skos:ConceptScheme ; rdfs:label "Entity types" .
lad:etype-CORP a skos:Concept ; skos:inScheme lad:EntityTypes ; skos:notation "CORP" ; rdfs:label "Corporate" ; skos:prefLabel "Corporate" ;
    skos:definition "A non-financial company." .
lad:etype-BANK a skos:Concept ; skos:inScheme lad:EntityTypes ; skos:notation "BANK" ; rdfs:label "Bank" ; skos:prefLabel "Bank" ;
    skos:definition "A bank." .
lad:etype-FINSUB a skos:Concept ; skos:inScheme lad:EntityTypes ; skos:notation "FINSUB" ; rdfs:label "Finance subsidiary" ; skos:prefLabel "Finance subsidiary" ;
    skos:definition "A subsidiary that exists to raise debt for its parent group. It usually has no issuer rating of its own; its debt is guaranteed by the parent, so investors take the parent's credit risk." .
lad:etype-SOV a skos:Concept ; skos:inScheme lad:EntityTypes ; skos:notation "SOV" ; rdfs:label "Sovereign" ; skos:prefLabel "Sovereign" ;
    skos:definition "A national government. A sovereign record can carry a Country Ceiling, issuer ratings, or both: they are different things, and the ceiling is not the sovereign's rating." .
```

## Questions

Answer each question below from the data above. Start each answer on a new line with its
number in bold, like **Q1.**, give the direct answer first, then at most two sentences of
reasoning that cite the records (IDs) you relied on.

Then end with one JSON block (```json) holding the structured answer to each question listed
here, with exactly these fields, shaped like {"Q1": {"field": value}, ...}. Name entities by their record ID: the entity_id in the CSV files, or the part of the IRI after lad: in the RDF (E01, not Kestrel Energy plc).

- Q1: rating (a rating)
- Q2: downgraded ("yes", "no" or "depends")
- Q3: investment_grade ("yes", "no" or "depends"), rating (a rating)
- Q4: outlook (an outlook)
- Q5: risk_of (a record ID), rating (a rating)
- Q7: issuers (a list of record IDs)
- Q8: entities (a list of record IDs)
- Q9: count (a number)
- Q10: investment_grade ("yes", "no" or "depends")
- Q11: rating (a rating)
- Q12: rating (a rating)
- Q13: count (a number)
- Q14: rating (a rating)
- Q15: rating (a rating)
- Q16: changed ("yes", "no" or "depends")
- Q17: downgraded ("yes", "no" or "depends")
- Q18: issuers (a list of record IDs)
- Q19: issuers (a list of record IDs)
- Q20: in_default ("yes", "no" or "depends")
- Q21: entities (a list of record IDs)
- Q22: entities (a list of record IDs)
- Q23: rating (a rating)
- Q24: investment_grade ("yes", "no" or "depends")
- Q25: count (a number)
- Q26: rating (a rating)
- Q27: rating (a rating)
- Q28: rating (a rating)
- Q29: rating (a rating)
- Q30: entities (a list of record IDs)
- Q31: any ("yes", "no" or "depends")
- Q32: parent (a record ID)
- Q33: risk_of (a record ID), rating (a rating)
- Q34: same_group ("yes", "no" or "depends")
- Q35: count (a number)
- Q36: count (a number)
- Q37: count (a number)
- Q38: same ("yes", "no" or "depends")
- Q39: rating (a rating)
- Q40: count (a number)

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
