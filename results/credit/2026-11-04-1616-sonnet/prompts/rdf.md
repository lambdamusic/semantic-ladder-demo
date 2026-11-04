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
