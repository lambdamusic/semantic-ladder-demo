# Credit ratings: a teaching ontology

Entities, instruments, rating actions and the codes the data uses, each with a definition that states what it means and how to read it. Invented for an experiment; not a model of any real rating agency.

## Classes

### Entity

A legal entity: a company, bank, finance subsidiary or sovereign. An entity is identified by its LEI (LEI), not by its name or record ID. The data holds records from more than one source system (source system), so the same entity can appear as several records with different IDs and differently spelled names: two records with the same LEI are the same entity, and every fact recorded against either record is a fact about that one entity.

### Instrument

A debt instrument, such as a bond or note, issued by an entity (issuer). An instrument's rating is not the issuer's rating: it can sit above or below it depending on seniority (seniority) and on any guarantee (guarantor).

### Rating action

Something a rating agency did to a rating on a date (date): assigned, affirmed, upgraded, downgraded, placed on Watch or withdrawn it. Each action applies to one rated thing (rated thing), one rating type (rating type) and, for issuer ratings, one currency basis (currency basis). A rating holds from its action date until the next action on the same thing, type and basis: so the rating on a date D is the one set by the latest action on or before D, and the current rating is the latest action overall. rating always holds the rating as it stands after the action, including when it did not change.

## Properties

### name (CSV column `name`)

The name as the source system spells it. Names are not identifiers: the same entity can be spelled differently in different systems.

### LEI (CSV column `lei`)

Legal Entity Identifier: the identifier that says which legal entity a record describes. Same LEI, same entity. Sovereigns have none.

### country (CSV column `country`)

ISO-style code of the country where the entity is domiciled. It decides which Country Ceiling, if any, applies to the entity's foreign-currency ratings. VD is the Republic of Valdoria and CV the Republic of Corvenia (both invented).

### entity type (CSV column `entity_type`)

What kind of entity it is: a concept of the scheme Entity types.

### parent (CSV column `parent_id`)

The entity that owns and controls this one.

### source system (CSV column `source_system`)

The internal system the record comes from (RATINGS, RESEARCH). Each system keeps its own records of the same entities; see Entity.

### description (CSV column `description`)

The instrument's name: issuer, coupon and maturity year.

### issuer (CSV column `issuer_id`)

The entity that issued the instrument and owes the payments. Not necessarily the entity whose credit risk the investor takes: see guarantor.

### guarantor (CSV column `guarantor_id`)

An entity that guarantees the instrument's payments if the issuer does not pay. A guaranteed instrument carries the guarantor's credit risk, so it is rated in line with the guarantor's issuer rating, not the issuer's.

### seniority (CSV column `seniority`)

Where the instrument ranks in repayment if the issuer fails: a concept of the scheme Seniorities.

### currency (CSV column `currency`)

The currency the instrument pays in. Debt in a currency other than the domestic one of the issuer's country is exposed to that country's transfer and convertibility risk: see Country Ceiling (CC).

### maturity (CSV column `maturity`)

The date the instrument is due to be repaid.

### date (CSV column `date`)

The date the action took effect.

### rated thing (CSV column `rated_id`)

What the action is about: an entity (for issuer ratings and Country Ceilings) or an instrument (for instrument ratings).

### rating type (CSV column `rating_type`)

Which kind of rating the action concerns: a concept of the scheme Rating types. Different types are different ratings and are never compared or combined with each other.

### currency basis (CSV column `ccy_basis`)

For issuer ratings, whether the rating covers foreign-currency (FC) or local-currency (LC) obligations: a concept of the scheme Currency bases. An entity can have both, with different values.

### action (CSV column `action`)

What was done: a concept of the scheme Action types. Only upgrades and downgrades change a rating.

### rating (CSV column `rating`)

The rating after the action, on the scale of its rating type. Long-term scale, strongest to weakest: AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, CCC, CC, C, RD, D. Investment grade means BBB- or higher; BB+ and below is speculative grade (high yield). RD (restricted default) means the issuer has defaulted on some material obligations, for instance by completing a distressed debt exchange, without being wound up: RD is a default. D means a general default. Short-term scale, strongest to weakest: F1+, F1, F2, F3, B, C, RD, D. WD means the rating was withdrawn (see Withdrawn (WD)): it is not a point on either scale.

### outlook (CSV column `outlook`)

The likely direction of a long-term rating over the next one to two years: a concept of the scheme Outlooks. An outlook is not a rating: revising it does not change the rating.

### rating watch (CSV column `watch`)

Set when the rating is on Rating Watch: a concept of the scheme Rating Watches. A Watch is not a rating change.

### comment (CSV column `comment`)

The analyst's note on the action, such as the reason for a withdrawal.

## Codes

The codes as they appear in the data, grouped by list.

### Rating types

- **LTIDR**, Long-term Issuer Default Rating: The issuer's own creditworthiness: how likely it is to default on its obligations, on the long-term scale. This is what people usually mean by an entity's rating. The foreign-currency (FC) one is the headline rating; there may also be a local-currency (LC) one.
- **STIDR**, Short-term Issuer Default Rating: The issuer's ability to meet obligations falling due within about a year, on the short-term scale (F1+ to D). Not comparable with long-term ratings.
- **INST**, Instrument rating: The rating of one specific instrument. It starts from the issuer's long-term rating and is notched for the instrument's seniority and expected recovery: subordinated debt is usually rated below the issuer, and guaranteed debt is rated on the guarantor. An instrument rating is never the rating of the issuer.
- **CC**, Country Ceiling: Not a rating of anyone. A cap, set for a country, on the foreign-currency ratings of entities domiciled there and of their foreign-currency debt. It reflects transfer and convertibility risk: the risk that the government stops money being converted or sent abroad, so even a sound company could not pay foreign-currency debt. Foreign-currency ratings of entities in the country are generally no higher than the ceiling; local-currency ratings are not capped. A Country Ceiling is not the sovereign's own issuer rating.

### Currency bases

- **FC**, Foreign currency: Covers obligations in foreign currency, so it is subject to the Country Ceiling.
- **LC**, Local currency: Covers obligations in the currency of the entity's own country; not subject to the Country Ceiling.

### Action types

- **AS**, Assigned: A first rating is given.
- **AF**, Affirmed: The rating is reviewed and kept the same. The outlook may be revised in the same action; that does not make it an upgrade or a downgrade.
- **UG**, Upgraded: The rating is raised.
- **DG**, Downgraded: The rating is lowered. The only action that counts as a downgrade.
- **RW**, Placed on Rating Watch: The rating is flagged as likely to change soon, usually within about six months, in the direction rating watch gives. The rating itself is unchanged: not a downgrade.
- **WD**, Withdrawn: The agency stops maintaining the rating, often for commercial reasons (the issuer no longer pays for it, or the debt is repaid). After a withdrawal the entity has no rating of that type. A withdrawal is not a credit event: it says nothing about default, and is not a downgrade.

### Outlooks

- **STA**, Stable: No direction expected.
- **POS**, Positive: The rating may go up over one to two years.
- **NEG**, Negative: The rating may go down over one to two years. Not a downgrade.

### Rating Watches

- **RWN**, Rating Watch Negative: A downgrade is likely in the near term. Not a downgrade yet.

### Seniorities

- **SU**, Senior unsecured: Ranks with the issuer's ordinary debts; usually rated at the level of the issuer's long-term rating.
- **SUB**, Subordinated: Repaid only after senior debt, so investors recover less in a default; usually rated one or more notches below the issuer's long-term rating.

### Entity types

- **CORP**, Corporate: A non-financial company.
- **BANK**, Bank: A bank.
- **FINSUB**, Finance subsidiary: A subsidiary that exists to raise debt for its parent group. It usually has no issuer rating of its own; its debt is guaranteed by the parent, so investors take the parent's credit risk.
- **SOV**, Sovereign: A national government. A sovereign record can carry a Country Ceiling, issuer ratings, or both: they are different things, and the ceiling is not the sovereign's rating.
