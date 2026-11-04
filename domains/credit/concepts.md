# Credit concepts behind the data

Plain-English explanations of the terms the [semantics ladder](README.md) data relies on,
using its invented records as examples. `ontology.ttl` holds the formal definitions, which
are what the LLM sees. This file is for people, and is not sent to the LLM.

## Instruments

An instrument is a specific piece of debt that a company has sold to investors, such as a
bond or note. It is the thing being rated, as distinct from the company that owes the money.

"Kestrel Energy 6.25% notes due 2031" (`I02`) breaks down as:

- **Issuer:** Kestrel Energy (`E01`), which borrowed the money and owes the payments.
- **Coupon:** 6.25% is the annual interest paid to investors.
- **Maturity:** 30 September 2031, when the money must be repaid.
- **Currency:** GBP, the currency it pays in.
- **Seniority:** subordinated (`SUB`), so if Kestrel fails, these investors are repaid after
  the senior ones.

The data has four instruments:

| ID | Instrument | Issuer | Seniority | Currency | Guarantor |
|---|---|---|---|---|---|
| `I01` | Kestrel Energy 4.50% due 2030 | `E01` | Senior unsecured | GBP | none |
| `I02` | Kestrel Energy 6.25% due 2031 | `E01` | Subordinated | GBP | none |
| `I03` | Northwind Finance 3.75% due 2030 | `E04` | Senior unsecured | EUR | `E02` |
| `I04` | Valdoria Telecom 5.00% due 2029 | `E05` | Senior unsecured | USD | none |

One company can have many instruments, each with its own rating. That rating starts from
the issuer's and moves up or down depending on the terms:

- **Seniority:** Kestrel is rated BBB, but its subordinated note `I02` is BB+, below
  investment grade. So "is Kestrel investment grade?" and "is this note investment grade?"
  get different answers (Q3).
- **Guarantees:** Northwind Finance's note `I03` is backed by `E02`, so investors are really
  taking that guarantor's risk, not the issuer's (Q5).
- **Currency:** `I04` pays in USD, so it is exposed to the risk that Valdoria stops money
  leaving the country (Q6, and see [Country Ceilings](#country-ceilings) below).

A knowledge graph therefore has to keep issuers and instruments as separate, linked things:
"the rating of X" is ambiguous until you say which one.

## Instruments, notes and bonds

A note is one kind of instrument. "Instrument" is the general term for any tradable financial
contract, and a note is a specific type of debt instrument.

| Term | What it is |
|---|---|
| **Instrument** | The umbrella term: bonds, notes, loans, shares, derivatives and so on |
| **Debt instrument** | An instrument where someone owes money and must repay it |
| **Bond** | Debt sold to investors, usually long-term |
| **Note** | Much the same as a bond, usually with a shorter term |

The line between a note and a bond is mostly convention. A note is often described as running
for about 1–10 years and a bond for longer, but it varies by market and issuer. The legal
terms matter far more for credit risk: seniority, guarantees and currency.

All four instruments in the data happen to be notes, but `lad:Instrument` is defined as "a
debt instrument, such as a bond or note", so a bond would fit without any change.

## Country Ceilings

A Country Ceiling is a cap on the foreign-currency ratings of entities based in a country.
It is written on the same scale as a rating, but it is not a judgement of anyone's
creditworthiness. In the data, the BB on the Republic of Valdoria (`A12`, type `CC`) is its
Country Ceiling.

**What it captures:** the risk that a government stops money being converted or sent abroad,
for example through capital controls in a currency crisis. Then even a healthy company
couldn't pay its foreign debts, because it couldn't get the dollars out. This is called
transfer and convertibility risk.

**Why currency matters:** the risk only applies to paying in foreign currency.

- **Local currency:** a Valdorian company paying a debt in Valdorian money doesn't need to
  convert anything or send it abroad, so capital controls don't stop it. The ceiling doesn't
  apply.
- **Foreign currency:** a Valdorian company paying dollars has to get through that
  restriction, however strong its business is. The ceiling applies.

Valdoria Telecom (`E05`) shows this directly:

| Action | What is rated | Rating | Ceiling applies? |
|---|---|---|---|
| `A13` | Issuer, local currency | **BBB-** | No, so this reflects the company's own strength |
| `A14` | Issuer, foreign currency | **BB** | Yes, capped at the ceiling |
| `A15` | `I04`, its USD note | **BB** | Yes, because it pays in dollars |

So the same company is investment grade in local currency and below investment grade in
foreign currency. Nothing about the business differs between the two; the gap comes entirely
from the country. Q6 asks why the two ratings differ, and Q10 has no single answer until you
say which rating you mean.

Two distinctions are easy to mix up:

- **The ceiling isn't the sovereign's own rating.** Valdoria the government would have its
  own issuer rating, which is a separate thing and could be a different level. The data
  doesn't include one, as `VD` only carries the ceiling. In real data, ceilings often sit
  somewhat above the sovereign's foreign-currency rating; check an agency's published
  criteria before relying on that.
- **It's a general cap, not an absolute one.** The ontology says foreign-currency ratings are
  "generally no higher than the ceiling". Real exceptions exist, such as a company with
  substantial earnings or support from abroad.

The rule links three things: an entity's country, the currency basis of a rating, and a
separate country-level fact. No row states that link, so a model reading only the CSV has to
bring it from its own training.
