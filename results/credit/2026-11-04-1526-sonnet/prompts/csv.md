<!-- system: You answer questions about a credit-ratings dataset. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

### entities.csv
```csv
entity_id,name,lei,country,entity_type,parent_id,source_system
E01,Kestrel Energy plc,KSTL00ENERGY000000A1,GB,CORP,,RATINGS
E02,Northwind Holdings plc,NWND00HOLDINGS00GB42,GB,CORP,,RATINGS
E03,NORTHWIND HLDGS,NWND00HOLDINGS00GB42,GB,CORP,,RESEARCH
E04,Northwind Finance BV,NWND00FINANCE000NL07,NL,FINSUB,E02,RATINGS
E05,Valdoria Telecom SA,VLDT00TELECOM0000V19,VD,CORP,,RATINGS
E06,Orrin Bank AG,ORRN00BANK00000DE233,DE,BANK,,RATINGS
E07,Pellam Retail Ltd,PLLM00RETAIL0000GB88,GB,CORP,,RATINGS
E08,Saxby Shipping SA,SXBY00SHIPPING00GR51,GR,CORP,,RATINGS
VD,Republic of Valdoria,,VD,SOV,,RATINGS
```

### instruments.csv
```csv
instrument_id,description,issuer_id,guarantor_id,seniority,currency,maturity
I01,Kestrel Energy 4.50% notes due 2030,E01,,SU,GBP,2030-03-15
I02,Kestrel Energy 6.25% notes due 2031,E01,,SUB,GBP,2031-09-30
I03,Northwind Finance 3.75% notes due 2030,E04,E02,SU,EUR,2030-05-01
I04,Valdoria Telecom 5.00% notes due 2029,E05,,SU,USD,2029-11-20
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
