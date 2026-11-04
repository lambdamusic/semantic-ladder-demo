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

lad:I04 a lad:Instrument ;
    rdfs:label "Valdoria Telecom 5.00% 2029" ;
    lad:currency "USD" ;
    lad:description "Valdoria Telecom 5.00% notes due 2029" ;
    lad:issuer lad:E05 ;
    lad:maturity "2029-11-20"^^xsd:date ;
    lad:seniority lad:seniority-SU .

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
