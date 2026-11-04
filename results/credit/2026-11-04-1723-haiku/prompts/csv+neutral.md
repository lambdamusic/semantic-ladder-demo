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

### ontology.ttl (the vocabulary the data uses)
The codes in the CSV files are the skos:notation values of the concepts below.
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
    skos:definition "The internal system the record comes from (RATINGS, RESEARCH, QA). Each system keeps its own records of the same entities; see lad:Entity. RATINGS is the system of record: where records of the same entity disagree on name, country or parent, the RATINGS record holds. QA records are test data, created to check the systems: they describe no real entity, so a QA record, and every action recorded against it, must be ignored." .


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
    skos:definition "The currency the instrument pays in, as an ISO 4217 code, or one of two local codes: XVD, the Valdorian dollar, the domestic currency of VD; and CVK, the Corvenian krone, the domestic currency of CV. Debt in a currency other than the domestic one of the issuer's country is exposed to that country's transfer and convertibility risk: see lad:type-CC. Debt in the domestic currency is local-currency debt and is not capped by the ceiling." .

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
    skos:definition "The issuer's own creditworthiness: how likely it is to default on its obligations, on the long-term scale. This is what people usually mean by an entity's rating. An entity may have a foreign-currency (FC) one, a local-currency (LC) one, or both." .

lad:type-STIDR a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "STIDR" ;
    rdfs:label "Short-term IDR" ; skos:prefLabel "Short-term Issuer Default Rating" ;
    skos:definition "The issuer's ability to meet obligations falling due within about a year, on the short-term scale (F1+ to D). Not comparable with long-term ratings." .

lad:type-INST a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "INST" ;
    rdfs:label "Instrument rating" ; skos:prefLabel "Instrument rating" ;
    skos:definition "The rating of one specific instrument. It starts from the issuer's long-term rating and is notched for the instrument's seniority and expected recovery: subordinated debt is usually rated below the issuer, and guaranteed debt is rated on the guarantor. An instrument rating is never the rating of the issuer." .

lad:type-CC a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "CC" ;
    rdfs:label "Country Ceiling" ; skos:prefLabel "Country Ceiling" ;
    skos:definition "Not a rating of anyone. A cap, set for a country, on the foreign-currency ratings of entities domiciled there and of their foreign-currency debt. It reflects transfer and convertibility risk: the risk that the government stops money being converted or sent abroad, so even a sound company could not pay foreign-currency debt. Foreign-currency ratings of entities in the country are generally no higher than the ceiling; local-currency ratings are not capped. A Country Ceiling is not the sovereign's own issuer rating." .

lad:type-CO a skos:Concept ; skos:inScheme lad:RatingTypes ; skos:notation "CO" ;
    rdfs:label "Credit opinion" ; skos:prefLabel "Credit opinion" ;
    skos:definition "A private, point-in-time view of an entity's credit, given to one client. It is not a published rating and not an issuer rating: never count it as a rating, and never report its value as the entity's rating." .

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

lad:action-EX a skos:Concept ; skos:inScheme lad:ActionTypes ; skos:notation "EX" ;
    rdfs:label "Expected" ; skos:prefLabel "Expected rating" ;
    skos:definition "A rating signalled before an instrument's final documents are signed. It is not yet a rating: the instrument stays unrated until an Assigned (AS) action confirms it." .

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
